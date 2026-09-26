# Bir senaryoyu ders.html'e gömer (sessiz önizleme): python3 build.py ../../python/video-senaryolari/gun-01.json
# Çıktı: built.html (bu klasörde). Sonra: python3 preview.py h 5,20  ya da  python3 render.py h
# Sesli, dudak senkronlu, müzikli tam video için: python3 uret.py python 1
import json, sys, pathlib
here = pathlib.Path(__file__).resolve().parent
repo = here.parent.parent


def build(senaryo, zaman=None, out=here / "built.html"):
    rig_f = repo / "maskotlar/piko-python/konusma-rig/rig.json"
    rig = json.loads(rig_f.read_text("utf8")) if senaryo["kurs"] == "python" and rig_f.exists() else None
    js = lambda o: json.dumps(o, ensure_ascii=False).replace("</", "<\\/")
    html = (here / "ders.html").read_text("utf8")
    html = html.replace("__SENARYO__", js(senaryo)).replace("__ZAMAN__", js(zaman)).replace("__RIG__", js(rig))
    html = html.replace("__ROOT__", _root(out))  # repo köküne göreli yol
    pathlib.Path(out).write_text(html, "utf8")
    return out


def _root(out):
    import os
    return os.path.relpath(repo, pathlib.Path(out).resolve().parent).replace(os.sep, "/") + "/"


if __name__ == "__main__":
    src = pathlib.Path(sys.argv[1]).resolve()
    senaryo = json.loads(src.read_text("utf8"))
    build(senaryo)
    total = sum(s["sure_sn"] for s in senaryo["sahneler"])
    print(f"built.html hazır: {senaryo['kurs']} gün {senaryo['gun']}, {len(senaryo['sahneler'])} sahne, ~{total} sn (sessiz önizleme)")
