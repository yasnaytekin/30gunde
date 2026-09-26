import pathlib
import sys, asyncio
from playwright.sync_api import sync_playwright
o = sys.argv[1]; times = [float(x) for x in sys.argv[2].split(",")]
W,H = (1080,1920) if o=="v" else (1920,1080)
with sync_playwright() as p:
    b = p.chromium.launch(args=["--allow-file-access-from-files"])
    pg = b.new_page(viewport={"width":W,"height":H})
    errs=[]; pg.on("pageerror", lambda e: errs.append(str(e))); pg.on("console", lambda m: errs.append(m.text) if m.type=="error" else None)
    pg.goto(pathlib.Path("built.html").resolve().as_uri() + f"?o={o}")
    pg.evaluate("window.ready")
    for t in times:
        pg.evaluate(f"window.renderAt({t})")
        pg.screenshot(path=f"pv_{o}_{t:05.2f}.png")
    print(errs[:5])
    b.close()
