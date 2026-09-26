# Piko pozlarından dudak senkronu için parçalar üretir (ders videosu şablonu kullanır).
#   python3 araclar/agiz-rig.py
# Ağzı açık pozlar (konusma, mutlu, isaret, sasirma, tebrik, sol, sag): ağız bulunur, pozdan silinir
# (çevredeki sarıyla doldurulur) ve ayrı bir PNG olarak kesilir. Videoda ağız dikeyde ölçeklenerek açılıp kapanır.
# "on" pozu: yuzler/ klasöründeki ağız kareleri (a, e, i, o, u, kapali) poza hizalanıp ağız bölgesiyle kesilir.
# Çıktı: maskotlar/piko-python/konusma-rig/ + rig.json
import json
from pathlib import Path

import numpy as np
from PIL import Image, ImageFilter
from scipy import ndimage as nd

REPO = Path(__file__).resolve().parent.parent
PIKO = REPO / "maskotlar/piko-python"
OUT = PIKO / "konusma-rig"
OPEN = ["konusma", "mutlu", "isaret", "sasirma", "tebrik", "sol", "sag"]
FACE_SCALE, FACE_DX, FACE_DY = 1.08, 0, 0  # yuzler/*.png → pozlar/on.png hizası (şablon eşleştirmeyle bulundu)
VISEMES = ["kapali", "i", "e", "a", "o", "u"]


def load(p):
    return np.asarray(Image.open(p).convert("RGBA")).astype(np.float32)


def save(a, p):
    Image.fromarray(np.clip(a, 0, 255).astype(np.uint8), "RGBA").save(p, optimize=True)


def mouth_mask(a):
    r, g, b, al = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    red = (r > 140) & (g < 110) & (b < 120) & (r - g > 80) & (al > 200)
    lab, n = nd.label(red)
    sizes = nd.sum(red, lab, range(1, n + 1))
    # başın içindeki en büyük kırmızı bölge (ünlem/kalp gibi süsler başın üstünde ya da kenarında kalır)
    best, bs = 0, 0
    for i, s in enumerate(sizes, 1):
        ys, xs = np.nonzero(lab == i)
        if ys.min() > 60 and ys.max() < 175 and s > bs:
            best, bs = i, s
    inner = lab == best
    skin = (r > 185) & (g > 140) & (b < 170) & (r - b > 60)
    near = nd.binary_dilation(inner, iterations=5)
    m = near & ~skin & (al > 128)
    m = nd.binary_closing(m, iterations=2) | inner
    lab2, _ = nd.label(m)
    keep = np.unique(lab2[inner])
    m = np.isin(lab2, keep[keep > 0])
    return nd.binary_fill_holes(m)


def inpaint(a, hole):
    a = a.copy()
    known = ~hole
    for _ in range(400):
        if known.all():
            break
        s = np.zeros_like(a[..., :3]); c = np.zeros(a.shape[:2])
        for dy, dx in ((-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)):
            sh = np.roll(np.roll(a[..., :3] * known[..., None], dy, 0), dx, 1)
            k = np.roll(np.roll(known, dy, 0), dx, 1)
            s += sh; c += k
        fill = (~known) & (c > 0)
        a[fill, :3] = s[fill] / c[fill, None]
        known = known | fill
    # dolan bölgeyi hafifçe yumuşat
    blur = nd.uniform_filter(a[..., :3], size=(3, 3, 1))
    a[hole, :3] = blur[hole]
    return a


def main():
    OUT.mkdir(exist_ok=True)
    rig = {"aciklama": "Dudak senkronu parçaları. Konumlar poz görselinin boyutuna oranla (0–1).", "pozlar": {}}
    for p in OPEN:
        a = load(PIKO / f"pozlar/{p}.png")
        H, W = a.shape[:2]
        m = mouth_mask(a)
        ys, xs = np.nonzero(m)
        x0, x1, y0, y1 = xs.min() - 2, xs.max() + 3, ys.min() - 2, ys.max() + 3
        base = inpaint(a, nd.binary_dilation(m, iterations=1))
        save(base, OUT / f"{p}-agizsiz.png")
        soft = nd.gaussian_filter(nd.binary_dilation(m, iterations=1).astype(np.float32), 0.7)
        sprite = a.copy(); sprite[..., 3] = np.minimum(a[..., 3], soft * 255)
        save(sprite[y0:y1, x0:x1], OUT / f"{p}-agiz.png")
        rig["pozlar"][p] = {"tur": "olcek", "boyut": [W, H],
                            "agiz": [round(x0 / W, 4), round(y0 / H, 4), round((x1 - x0) / W, 4), round((y1 - y0) / H, 4)]}
    # on pozu + yüz kareleri
    on = Image.open(PIKO / "pozlar/on.png").convert("RGBA")
    W, H = on.size
    fa = Image.open(PIKO / "yuzler/a.png").convert("RGBA")
    fw, fh = round(fa.width * FACE_SCALE), round(fa.height * FACE_SCALE)
    frames = {v: np.asarray(Image.open(PIKO / f"yuzler/{v}.png").convert("RGBA").resize((fw, fh), Image.LANCZOS)).astype(np.float32) for v in VISEMES}
    # ağız bölgesi: 'a' karesindeki kırmızı ağzın çevresi
    m = mouth_mask(frames["a"])
    ys, xs = np.nonzero(m)
    cx, cy = (xs.min() + xs.max()) / 2, (ys.min() + ys.max()) / 2
    rx, ry = (xs.max() - xs.min()) / 2 + 16, (ys.max() - ys.min()) / 2 + 12
    yy, xx = np.mgrid[0:fh, 0:fw]
    ell = np.clip((1.0 - np.sqrt(((xx - cx) / rx) ** 2 + ((yy - cy) / ry) ** 2)) / 0.25, 0, 1)
    x0, x1 = int(cx - rx) - 1, int(cx + rx) + 2
    y0, y1 = int(cy - ry) - 1, int(cy + ry) + 2
    for v, f in frames.items():
        g = f.copy(); g[..., 3] = f[..., 3] * ell
        save(g[y0:y1, x0:x1], OUT / f"on-{v}.png")
    rig["pozlar"]["on"] = {"tur": "kare", "boyut": [W, H], "kareler": VISEMES,
                           "agiz": [round((x0 + FACE_DX) / W, 4), round((y0 + FACE_DY) / H, 4), round((x1 - x0) / W, 4), round((y1 - y0) / H, 4)]}
    (OUT / "rig.json").write_text(json.dumps(rig, ensure_ascii=False, indent=1), "utf8")
    print("hazır:", OUT, ", ".join(rig["pozlar"]))


if __name__ == "__main__":
    main()
