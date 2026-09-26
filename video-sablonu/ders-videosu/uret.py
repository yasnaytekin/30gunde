# Senaryodan sesli, dudak senkronlu, müzikli ders videosu üretir.
#   python3 uret.py python 1                      # Türkçe + İngilizce, yatay + dikey (4 video)
#   python3 uret.py python 1 --dil tr --yon h     # yalnızca Türkçe yatay
#   python3 uret.py python 1 --onizleme 3,20,45   # video yerine birkaç anın ekran görüntüsü
# Gerekenler: bash modelleri-indir.sh (bir kez), pip install sherpa-onnx soundfile numpy scipy playwright imageio-ffmpeg
# Senaryolar: <kurs>/video-senaryolari/gun-XX.json (tr), <kurs>/video-senaryolari/<dil>/gun-XX.json (ör. en)
# Çıktı: cikti/<kurs>/gun-XX/<kurs>-gun-XX-<dil>-<yatay|dikey>.mp4 (+ .srt altyazı)
import argparse, json, subprocess, sys, time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

import numpy as np
import soundfile as sf

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
import build, muzik, ses  # noqa: E402

YON = {"h": ("yatay", 1920, 1080), "v": ("dikey", 1080, 1920)}


def ffmpeg():
    import imageio_ffmpeg
    return imageio_ffmpeg.get_ffmpeg_exe()


def senaryo_yolu(kurs, gun, dil):
    d = REPO / kurs / "video-senaryolari"
    return (d if dil == "tr" else d / dil) / f"gun-{gun:02d}.json"


def srt(zaman, path):
    def ts(x):
        ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
        return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"
    rows = [s for seg in zaman["segs"] for s in seg["subs"]]
    path.write_text("\n".join(f"{i}\n{ts(r['a'])} --> {ts(min(r['b'], r['a'] + 8))}\n{r['text']}\n" for i, r in enumerate(rows, 1)), "utf8")


def hazirla(kurs, gun, dil):
    """Seslendirme + zaman çizelgesi + miksaj + built.html. Önbellek sayesinde tekrar çalıştırmak hızlıdır."""
    src = senaryo_yolu(kurs, gun, dil)
    v = json.loads(src.read_text("utf8"))
    work = HERE / "is" / f"{kurs}-gun-{gun:02d}-{dil}"
    work.mkdir(parents=True, exist_ok=True)
    t = time.time()
    zaman, voice = ses.zaman_cizelgesi(v, ses.Ses(dil, work / "onbellek"))
    sf.write(work / "ses.wav", voice, ses.SR)
    mix = muzik.miksaj(voice, zaman)
    sf.write(work / "miks.wav", mix, muzik.SR)
    (work / "zaman.json").write_text(json.dumps({k: zaman[k] for k in ("sure", "segs")}, ensure_ascii=False, indent=1), "utf8")
    build.build(v, zaman, work / "built.html")
    print(f"[{dil}] ses hazır: {zaman['sure']:.1f} sn, {len(zaman['segs'])} bölüm ({time.time() - t:.0f} sn)", flush=True)
    return v, zaman, work


def kareler(html, o, out, fps=30):
    from playwright.sync_api import sync_playwright
    name, W, H = YON[o]
    ff = subprocess.Popen([ffmpeg(), "-hide_banner", "-loglevel", "error", "-y", "-f", "image2pipe", "-framerate", str(fps), "-c:v", "mjpeg", "-i", "-",
                           "-c:v", "libx264", "-preset", "medium", "-crf", "21", "-pix_fmt", "yuv420p", "-r", str(fps), str(out)], stdin=subprocess.PIPE)
    t0 = time.time()
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": W, "height": H})
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto(Path(html).as_uri() + f"?o={o}")
        pg.evaluate("window.ready")
        if errs:
            raise SystemExit(f"sayfa hatası: {errs[:3]}")
        dur = pg.evaluate("window.DURATION")
        n = int(dur * fps)
        for i in range(n):
            pg.evaluate(f"window.renderAt({i / fps})")
            ff.stdin.write(pg.screenshot(type="jpeg", quality=93))
            if i % (fps * 20) == 0:
                print(f"  {Path(out).parent.name} {name}: {i / fps:.0f}/{dur:.0f} sn ({time.time() - t0:.0f} sn geçti)", flush=True)
        b.close()
    ff.stdin.close(); ff.wait()
    if errs:
        print("sayfa hataları:", errs[:3])


def birlestir(video, audio, out):
    subprocess.run([ffmpeg(), "-hide_banner", "-loglevel", "error", "-y", "-i", str(video), "-i", str(audio),
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "48000",
                    "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", str(out)], check=True)


def video(args):
    kurs, gun, dil, o, work = args
    name = YON[o][0]
    outdir = REPO / "cikti" / kurs / f"gun-{gun:02d}"
    outdir.mkdir(parents=True, exist_ok=True)
    silent = work / f"sessiz-{o}.mp4"
    kareler(work / "built.html", o, silent)
    out = outdir / f"{kurs}-gun-{gun:02d}-{dil}-{name}.mp4"
    birlestir(silent, work / "miks.wav", out)
    return str(out)


def onizleme(work, o, times):
    from playwright.sync_api import sync_playwright
    name, W, H = YON[o]
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": W, "height": H})
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        pg.goto((work / "built.html").as_uri() + f"?o={o}")
        pg.evaluate("window.ready")
        for t in times:
            pg.evaluate(f"window.renderAt({t})")
            pg.screenshot(path=str(work / f"onizleme_{o}_{t:06.2f}.png"))
        b.close()
    print("önizleme:", work, "hatalar:", errs[:5])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kurs", choices=["python", "javascript"])
    ap.add_argument("gun", type=int)
    ap.add_argument("--dil", default="tr,en")
    ap.add_argument("--yon", default="h,v")
    ap.add_argument("--onizleme")
    ap.add_argument("--paralel", type=int, default=4, help="aynı anda çizilecek video sayısı")
    a = ap.parse_args()
    diller, yonler = a.dil.split(","), a.yon.split(",")
    works = {}
    for d in diller:
        v, zaman, work = hazirla(a.kurs, a.gun, d)
        outdir = REPO / "cikti" / a.kurs / f"gun-{a.gun:02d}"
        outdir.mkdir(parents=True, exist_ok=True)
        srt(zaman, outdir / f"{a.kurs}-gun-{a.gun:02d}-{d}.srt")
        works[d] = work
    if a.onizleme:
        times = [float(x) for x in a.onizleme.split(",")]
        for d, w in works.items():
            for o in yonler:
                onizleme(w, o, times)
        return
    jobs = [(a.kurs, a.gun, d, o, works[d]) for d in diller for o in yonler]
    t = time.time()
    with ProcessPoolExecutor(max_workers=a.paralel) as ex:
        for out in ex.map(video, jobs):
            print("hazır:", out, flush=True)
    print(f"bitti: {len(jobs)} video, {time.time() - t:.0f} sn")


if __name__ == "__main__":
    main()
