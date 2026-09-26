# Sessiz video üretir (altyazılı): python3 render.py h [fps]  → ders_h.mp4
# Altyazısız istersen:  SUBTITLES=0 python3 render.py h
import os, sys, subprocess, time, pathlib
from playwright.sync_api import sync_playwright
here = pathlib.Path(__file__).resolve().parent
o = sys.argv[1]; FPS = int(sys.argv[2]) if len(sys.argv) > 2 else 30
W, H = (1080, 1920) if o == "v" else (1920, 1080)
out = here / f"ders_{o}.mp4"
ff = subprocess.Popen(["ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-f", "image2pipe", "-framerate", str(FPS), "-c:v", "mjpeg", "-i", "-",
                       "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", "-r", str(FPS), str(out)], stdin=subprocess.PIPE)
t0 = time.time()
with sync_playwright() as p:
    b = p.chromium.launch(args=["--allow-file-access-from-files"])
    pg = b.new_page(viewport={"width": W, "height": H})
    pg.goto((here / "built.html").as_uri() + f"?o={o}")
    if os.environ.get("SUBTITLES") == "0":
        pg.evaluate("window.SUBTITLES = false")
    pg.evaluate("window.ready")
    dur = pg.evaluate("window.DURATION")
    n = int(dur * FPS)
    for i in range(n):
        pg.evaluate(f"window.renderAt({i / FPS})")
        ff.stdin.write(pg.screenshot(type="jpeg", quality=92))
        if i % (FPS * 10) == 0:
            print(f"{i / FPS:.0f}/{dur:.0f} sn  ({time.time() - t0:.0f} sn geçti)", flush=True)
    b.close()
ff.stdin.close(); ff.wait()
print("hazır:", out, round(time.time() - t0), "sn")
