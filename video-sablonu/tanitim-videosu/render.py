import pathlib
import sys, subprocess, time
from playwright.sync_api import sync_playwright
o = sys.argv[1]; FPS = 30; DUR = 30.0
W,H = (1080,1920) if o=="v" else (1920,1080)
out = f"./silent_{o}.mp4"
ff = subprocess.Popen(["ffmpeg","-hide_banner","-loglevel","error","-y","-f","image2pipe","-framerate",str(FPS),"-c:v","mjpeg","-i","-",
    "-c:v","libx264","-preset","slow","-crf","17","-pix_fmt","yuv420p","-r",str(FPS),out], stdin=subprocess.PIPE)
t0=time.time()
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={"width":W,"height":H})
    pg.goto(pathlib.Path("built.html").resolve().as_uri() + f"?o={o}")
    pg.evaluate("window.ready")
    n = int(DUR*FPS)
    for i in range(n):
        pg.evaluate(f"window.renderAt({i/FPS})")
        ff.stdin.write(pg.screenshot(type="jpeg", quality=95))
        if i % 150 == 0: print(o, i, round(time.time()-t0,1), flush=True)
    b.close()
ff.stdin.close(); ff.wait(); print("done", out, round(time.time()-t0,1))
