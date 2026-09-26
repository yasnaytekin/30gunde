# Video senaryolarını doğrular ve her JSON senaryodan okunabilir bir Markdown üretir.
#   python3 araclar/senaryo-dogrula.py                 # hepsi
#   python3 araclar/senaryo-dogrula.py python 1-15     # bir kurs, gün aralığı
# Denetimler: alanlar, poz adları, görsel yolları, süreler, seslendirme uzunluğu (≈2,3 kelime/sn),
# "calistir": true olan kod sahnelerinde kodu gerçekten çalıştırıp "cikti" ile karşılaştırma.
import json, re, subprocess, sys, tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
POSES = json.loads((REPO / "maskotlar/pozlar.json").read_text("utf8"))["maskotlar"]
TYPES = {"acilis", "anlatim", "kod", "cikti", "hata", "soru", "gorev", "ozet", "kapanis"}
POSITIONS = {"sol", "sag", "alt-sol", "alt-sag", "orta", "yok"}
MASCOT = {"python": "piko", "javascript": "kodi"}
LANG = {"python": "python", "javascript": "js"}
WPS = 2.3  # Türkçe seslendirmede saniyede ortalama kelime


def run_code(course, code):
    with tempfile.TemporaryDirectory() as d:
        if course == "python":
            f = Path(d) / "k.py"; f.write_text(code, "utf8"); cmd = [sys.executable, str(f)]
        else:
            f = Path(d) / "k.mjs"; f.write_text(code, "utf8"); cmd = ["node", str(f)]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=10, input="")
        except subprocess.TimeoutExpired:
            return None, "zaman aşımı"
        return r.stdout, r.stderr


def norm(s):
    return "\n".join(l.rstrip() for l in (s or "").strip("\n").split("\n")).strip()


def check(course, path):
    errs = []
    try:
        v = json.loads(path.read_text("utf8"))
    except Exception as e:
        return [f"{path.name}: JSON okunamadı: {e}"], None
    E = lambda m: errs.append(f"{course}/{path.name}: {m}")
    for k in ("kurs", "gun", "baslik", "maskot", "ozet", "hedef_sure_sn", "sahneler"):
        if k not in v:
            E(f"'{k}' eksik")
    if errs:
        return errs, v
    if v["kurs"] != course or v["maskot"] != MASCOT[course]:
        E("kurs/maskot yanlış")
    day = int(re.search(r"(\d+)", path.name).group(1))
    if v["gun"] != day:
        E("gün numarası dosya adıyla uyuşmuyor")
    poses = POSES[v["maskot"]]["pozlar"]
    total = 0
    words = 0
    sc = v["sahneler"]
    if not 7 <= len(sc) <= 18:
        E(f"sahne sayısı {len(sc)} (7–18 olmalı)")
    for i, s in enumerate(sc, 1):
        P = lambda m: E(f"sahne {i}: {m}")
        if s.get("no") != i:
            P("no sırası bozuk")
        if s.get("tur") not in TYPES:
            P(f"tur '{s.get('tur')}' geçersiz")
        d = s.get("sure_sn")
        if not isinstance(d, (int, float)) or not 2 <= d <= 30:
            P("sure_sn 2–30 arası olmalı")
            d = 0
        total += d
        text = s.get("anlatim", "")
        if not text.strip():
            P("anlatim boş")
        w = len(text.split())
        words += w
        if d and w > d * WPS * 1.35 + 3:
            P(f"seslendirme {w} kelime, {d} sn'ye sığmaz (en çok ~{int(d * WPS * 1.35)})")
        m = s.get("maskot") or {}
        if m.get("konum", "yok") not in POSITIONS:
            P("maskot.konum geçersiz")
        if m.get("konum", "yok") != "yok" and m.get("poz") not in poses:
            P(f"maskot.poz '{m.get('poz')}' yok; olanlar: {', '.join(poses)}")
        ek = s.get("ekran") or {}
        g = ek.get("gorsel")
        if g and not (REPO / g).exists():
            P(f"görsel bulunamadı: {g}")
        if s.get("tur") in ("kod", "hata") and not ek.get("kod"):
            P("kod sahnesinde ekran.kod yok")
        for n in ek.get("vurgu_satirlari") or []:
            if not ek.get("kod") or not 1 <= n <= len(ek["kod"].rstrip("\n").split("\n")):
                P(f"vurgu satırı {n} kodda yok")
        if s.get("calistir"):
            out, err = run_code(course, ek.get("kod", ""))
            if out is None:
                P("kod zaman aşımına uğradı")
            elif s.get("tur") == "hata":
                if not err.strip():
                    P("hata sahnesindeki kod hata vermedi")
            elif err.strip():
                P(f"kod hata verdi: {err.strip().splitlines()[-1]}")
            elif "cikti" in ek and norm(out) != norm(ek["cikti"]):
                P(f"ekran.cikti gerçek çıktıyla aynı değil. Gerçek:\n{out}")
    if not 60 <= total <= 210:
        E(f"toplam süre {total} sn (60–210 olmalı)")
    return errs, v


def to_md(course, v):
    lang = LANG[course]
    total = sum(s.get("sure_sn", 0) for s in v["sahneler"])
    out = [f"# Video senaryosu: Gün {v['gun']}, {v['baslik']}", "",
           f"**Kurs:** {'30 Günde Python' if course == 'python' else '30 Günde JavaScript'}  ·  **Maskot:** {v['maskot'].capitalize()}  ·  **Süre:** ~{total} sn", "",
           v["ozet"], "", f"Ders metni: [gun-{v['gun']:02d}.md](../gunler/gun-{v['gun']:02d}.md)", "",
           "| # | Tür | Süre | Maskot |", "|---|---|---|---|"]
    for s in v["sahneler"]:
        m = s.get("maskot") or {}
        out.append(f"| {s['no']} | {s['tur']} | {s['sure_sn']} sn | {m.get('poz', '-')} ({m.get('konum', 'yok')}) |")
    out.append("")
    for s in v["sahneler"]:
        ek = s.get("ekran") or {}
        m = s.get("maskot") or {}
        out += [f"## Sahne {s['no']}: {s['tur']} ({s['sure_sn']} sn)", ""]
        out += [f"**Seslendirme:** {s['anlatim']}", ""]
        if ek.get("baslik"):
            out += [f"**Ekranda başlık:** {ek['baslik']}", ""]
        if ek.get("maddeler"):
            out += ["**Ekranda maddeler:**", ""] + [f"- {b}" for b in ek["maddeler"]] + [""]
        if ek.get("kod"):
            vs = ek.get("vurgu_satirlari")
            out += [f"**Kod**{' (vurgulanan satırlar: ' + ', '.join(map(str, vs)) + ')' if vs else ''}:", "", f"```{ek.get('dil', lang)}", ek["kod"].rstrip("\n"), "```", ""]
        if ek.get("cikti"):
            out += ["**Çıktı:**", "", "```text", ek["cikti"].rstrip("\n"), "```", ""]
        if ek.get("gorsel"):
            out += [f"**Görsel:** `{ek['gorsel']}`", ""]
        if m.get("konum", "yok") != "yok":
            out += [f"**Maskot:** {m.get('poz')} pozu, {m.get('konum')}" + (f"; {m['not']}" if m.get("not") else ""), ""]
        if s.get("yonetmen_notu"):
            out += [f"*Yönetmen notu: {s['yonetmen_notu']}*", ""]
    return "\n".join(out).rstrip() + "\n"


def main():
    courses = [sys.argv[1]] if len(sys.argv) > 1 else ["python", "javascript"]
    rng = None
    if len(sys.argv) > 2:
        a, b = sys.argv[2].split("-"); rng = (int(a), int(b))
    bad = 0; ok = 0
    for c in courses:
        d = REPO / c / "video-senaryolari"
        for f in sorted(d.glob("gun-*.json")):
            day = int(re.search(r"(\d+)", f.name).group(1))
            if rng and not rng[0] <= day <= rng[1]:
                continue
            errs, v = check(c, f)
            for e in errs:
                print("HATA", e)
            bad += len(errs)
            if not errs:
                ok += 1
                f.with_suffix(".md").write_text(to_md(c, v), "utf8")
    print(f"{ok} senaryo geçerli, {bad} sorun.")
    sys.exit(1 if bad else 0)


main()
