# Bir senaryoyu ders.html'e gömer: python3 build.py ../../python/video-senaryolari/gun-01.json
# Çıktı: built.html (bu klasörde). Sonra: python3 preview.py h 5,20  ya da  python3 render.py h
import json, sys, pathlib
here = pathlib.Path(__file__).resolve().parent
src = pathlib.Path(sys.argv[1]).resolve()
repo = here.parent.parent
senaryo = json.loads(src.read_text("utf8"))
html = (here / "ders.html").read_text("utf8")
html = html.replace("__SENARYO__", json.dumps(senaryo, ensure_ascii=False).replace("</", "<\\/")).replace("__ROOT__", "../../")
(here / "built.html").write_text(html, "utf8")
total = sum(s["sure_sn"] for s in senaryo["sahneler"])
print(f"built.html hazır: {senaryo['kurs']} gün {senaryo['gun']}, {len(senaryo['sahneler'])} sahne, {total} sn")
