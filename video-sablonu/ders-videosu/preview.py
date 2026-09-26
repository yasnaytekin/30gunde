# Belirli anların ekran görüntüsü: python3 preview.py h 3,15,40   (h = yatay 1920x1080, v = dikey 1080x1920)
import sys, pathlib
from playwright.sync_api import sync_playwright
here = pathlib.Path(__file__).resolve().parent
o = sys.argv[1]; times = [float(x) for x in sys.argv[2].split(",")]
W, H = (1080, 1920) if o == "v" else (1920, 1080)
with sync_playwright() as p:
    b = p.chromium.launch(args=["--allow-file-access-from-files"])
    pg = b.new_page(viewport={"width": W, "height": H})
    errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
    pg.goto((here / "built.html").as_uri() + f"?o={o}")
    pg.evaluate("window.ready")
    for t in times:
        pg.evaluate(f"window.renderAt({t})")
        pg.screenshot(path=str(here / f"onizleme_{o}_{t:06.2f}.png"))
    print("hatalar:", errs[:5])
    b.close()
