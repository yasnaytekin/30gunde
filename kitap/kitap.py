# 30 Günde kitabı: gün gün ders verisinden (veri/gun-XX.json) baskıya ve e-kitaba uygun PDF üretir.
#   python3 kitap/kitap.py python 1-3            # cikti/kitap/30-gunde-python-gun-01-03.pdf
# Kitap siteden bağımsız kullanılabilir: örneklerin çıktıları kodu gerçekten çalıştırarak yazılır, görevlerin
# "kendini kontrol et" maddeleri ve çözümleri (satır satır açıklamalarıyla) kitabın içindedir. Her sayfanın altında
# o günün etkileşimli dersine giden bir QR kod bulunur (isteğe bağlı kullanım).
# Gerekenler: pip install markdown pygments "qrcode[pil]" pypdf reportlab playwright
import argparse, html, io, json, re, subprocess, sys, tempfile
from pathlib import Path

import markdown
import qrcode
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import PythonLexer
from pypdf import PdfReader, PdfWriter
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
FONTS = HERE / "fontlar"
W_MM, H_MM = 148, 210  # A5

KURS = {
    "python": {"ad": "30 Günde Python", "maskot": "Piko", "renk": "#2F6DB5", "renk2": "#FFC83D", "ink": "#13233F",
               "logo": "gorseller/python/logo-128.png", "bolge": "gorseller/python/harita/{}.webp",
               "poz": "maskotlar/piko-python/pozlar/{}.png", "url": "https://30gunde.com.tr/#/ders/{}",
               "varsayilan_proje": "Piko'nun Macerası"},
}

# Yalnızca sitede anlamlı olan ifadelerin kitap karşılıkları
UYARLA = [
    ("Çalıştır'a bas ve çıktıya bak.", "Kodu çalıştır ve çıktıya bak."),
    ("Çalıştır'a bas:", "Kodu çalıştır:"),
    ("Çalıştır'a basınca", "Kodu çalıştırınca"),
    ("Sahnede soluk görünen şekli doldur!", "Aşağıdaki şekli oluştur!"),
    ("Bu sitede `input()` kullanınca cevaplarını editörün altındaki **Girdi** kutusuna yaz. Her satır bir cevaptır.",
     "Programı çalıştırınca `input()` seni bekler: cevabını yaz ve Enter'a bas."),
    ("Girdi kutusundaki adı değiştirip tekrar çalıştır.", "Farklı bir adla tekrar çalıştır."),
    ("sahnede resme dönüşür", "sahnede resme dönüşür (sitede canlı, kitapta çizimle gösteriyoruz)"),
]


def uyarla(s):
    for a, b in UYARLA:
        s = s.replace(a, b)
    return s


def md(s):
    return markdown.markdown(uyarla(s or ""), extensions=["fenced_code", "tables", "codehilite"],
                             extension_configs={"codehilite": {"guess_lang": False, "css_class": "hl"}})


def md_inline(s):
    h = md(s).strip()
    return h[3:-4] if h.startswith("<p>") and h.endswith("</p>") and h.count("<p>") == 1 else h


FORMATTER = HtmlFormatter(cssclass="hl", nowrap=True)


def kod(code, cikti=None, baslik=None, hata=False, sekil=None):
    code = (code or "").rstrip("\n")
    out = f'<div class="code">{f"<div class=cap>{html.escape(baslik)}</div>" if baslik else ""}<pre class="hl">{highlight(code, PythonLexer(), FORMATTER).rstrip()}</pre></div>'
    if cikti is not None:
        out += f'<div class="out{" err" if hata else ""}"><span>{"Hata" if hata else "Çıktı"}</span><pre>{html.escape(cikti.rstrip())}</pre></div>'
    if sekil:
        out += sekil
    return f'<div class="kod-grup">{out}</div>'


def calistir(code, inputs=None):
    """Kodu çalıştırıp konsolda görüneceği gibi çıktıyı döndürür (input() cevapları ekrana yazılır)."""
    pre = ""
    if inputs:
        pre = ("import builtins as _b\n_i = iter(%r)\n"
               "def _inp(p=''):\n    v = next(_i)\n    print(p + v)\n    return v\n_b.input = _inp\n") % (list(inputs),)
    with tempfile.TemporaryDirectory() as d:
        f = Path(d) / "k.py"; f.write_text(pre + code, "utf8")
        r = subprocess.run([sys.executable, str(f)], capture_output=True, text=True, timeout=10, cwd=d)
    if r.returncode != 0:
        last = r.stderr.strip().splitlines()[-1] if r.stderr.strip() else "Hata"
        return (r.stdout + last).strip("\n"), True
    return r.stdout.rstrip("\n"), False


def sahne(rows, root):
    """Sahne ızgarası: * Piko, # duvar, o altın, H kalp."""
    def cell(ch):
        if ch == "*": return f'<i class="c"><img src="{root}/{KURS["python"]["poz"].format("on")}"></i>'
        if ch == "#": return '<i class="c wall"></i>'
        if ch == "o": return '<i class="c"><b class="coin"></b></i>'
        if ch == "H": return '<i class="c heart">♥</i>'
        return '<i class="c"></i>'
    return '<div class="sahne"><span>Sahne</span>' + "".join(f'<div class="row">{"".join(cell(c) for c in r)}</div>' for r in rows) + "</div>"


def qr_png(url):
    img = qrcode.make(url, border=1, box_size=8)
    b = io.BytesIO(); img.save(b, "PNG"); return b.getvalue()


def fontlari_hazirla():
    """Yazı tipleri (SIL OFL, Google Fonts deposu) yoksa indirilir; repoya girmez."""
    base = "https://raw.githubusercontent.com/google/fonts/main/ofl/"
    lst = {"Nunito.ttf": "nunito/Nunito%5Bwght%5D.ttf", "JetBrainsMono.ttf": "jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf"}
    lst.update({f"Poppins-{w}.ttf": f"poppins/Poppins-{w}.ttf" for w in ("Regular", "SemiBold", "Bold", "ExtraBold")})
    FONTS.mkdir(exist_ok=True)
    for ad, yol in lst.items():
        if not (FONTS / ad).exists():
            import urllib.request
            urllib.request.urlretrieve(base + yol, FONTS / ad)


# ---------- HTML parçaları ----------
def css(root):
    f = lambda n: (FONTS / n).as_uri()
    return f"""
@font-face {{ font-family: Body; src: url({f('Nunito.ttf')}); font-weight: 200 1000; }}
@font-face {{ font-family: Mono; src: url({f('JetBrainsMono.ttf')}); font-weight: 100 800; }}
@font-face {{ font-family: Head; src: url({f('Poppins-Bold.ttf')}); font-weight: 700; }}
@font-face {{ font-family: Head; src: url({f('Poppins-SemiBold.ttf')}); font-weight: 600; }}
@font-face {{ font-family: Head; src: url({f('Poppins-ExtraBold.ttf')}); font-weight: 800; }}
@page {{ size: {W_MM}mm {H_MM}mm; margin: 15mm 14mm 22mm 14mm; }}
@page cover {{ margin: 0; }}
:root {{ --c: #2F6DB5; --c2: #FFC83D; --ink: #13233F; --ink2: #4A5B7A; --line: #D8E3F3; --soft: #F4F8FF; }}
* {{ box-sizing: border-box; -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
html {{ font-family: Body, sans-serif; font-size: 9.6pt; line-height: 1.5; color: var(--ink); }}
body {{ margin: 0; }}
h1, h2, h3, h4 {{ font-family: Head, sans-serif; line-height: 1.2; margin: 0; break-after: avoid; }}
h2 {{ font-size: 15pt; color: var(--c); margin: 14pt 0 6pt; display: flex; align-items: center; gap: 6pt; }}
h2::before {{ content: ""; width: 9pt; height: 9pt; border-radius: 3pt; background: var(--c2); box-shadow: inset 0 0 0 1.6pt #E0A800; }}
h3 {{ font-size: 11.5pt; margin: 11pt 0 4pt; }}
p {{ margin: 0 0 6pt; }}
ul, ol {{ margin: 0 0 6pt; padding-left: 14pt; }}
li {{ margin-bottom: 2pt; }}
code, pre {{ font-variant-ligatures: none; font-feature-settings: "liga" 0, "calt" 0; }}
code {{ font-family: Mono; font-size: 0.9em; background: #EAF1FB; padding: 0.5pt 3pt; border-radius: 3pt; }}
pre {{ margin: 0; }}
.kod-grup {{ break-inside: avoid; margin: 5pt 0 9pt; }}
.code {{ background: var(--soft); border: 0.8pt solid var(--line); border-left: 3pt solid var(--c); border-radius: 5pt; padding: 6pt 8pt; }}
.code .cap {{ font-family: Head; font-weight: 600; font-size: 7.5pt; color: var(--ink2); margin-bottom: 3pt; }}
.code pre, .out pre {{ font-family: Mono; font-size: 8.2pt; line-height: 1.45; white-space: pre-wrap; word-break: break-word; }}
.out {{ border: 0.8pt dashed #9DB4D6; border-top: none; border-radius: 0 0 5pt 5pt; padding: 5pt 8pt 6pt; margin: 0 4pt; background: #fff; }}
.out span, .sahne > span {{ display: block; font-family: Head; font-weight: 600; font-size: 6.5pt; letter-spacing: .08em; text-transform: uppercase; color: var(--ink2); margin-bottom: 2pt; }}
.out.err {{ border-color: #E8574A; background: #FFF4F2; }} .out.err span, .out.err pre {{ color: #B3261E; }}
.note {{ font-size: 8.5pt; color: var(--ink2); font-style: italic; margin: -4pt 0 8pt 4pt; }}
.hl .k, .hl .kn, .hl .kc, .hl .ow {{ color: #8B3FC8; font-weight: 600; }} .hl .s, .hl .s1, .hl .s2, .hl .sa, .hl .si, .hl .se {{ color: #2E7D32; }}
.hl .mi, .hl .mf {{ color: #C2410C; }} .hl .c1, .hl .c {{ color: #7A869A; font-style: italic; }} .hl .nb, .hl .nf {{ color: #1D5FB0; }}
.box {{ border-radius: 7pt; padding: 8pt 10pt; margin: 8pt 0; break-inside: avoid; }}
.box h4 {{ font-size: 9pt; margin-bottom: 4pt; }}
.box.hedef {{ background: #FFF7DD; border: 1pt solid #F2D27A; }}
.box.sozluk {{ background: var(--soft); border: 1pt solid var(--line); }}
.box.sozluk dl {{ margin: 0; display: grid; grid-template-columns: auto 1fr; gap: 3pt 8pt; font-size: 8.6pt; }}
.box.sozluk dt {{ font-family: Mono; font-weight: 600; color: var(--c); }} .box.sozluk dd {{ margin: 0; }}
.box.sozluk dd em {{ color: var(--ink2); font-style: normal; font-size: 7.5pt; }}
.gorev {{ border: 1pt solid var(--line); border-radius: 8pt; padding: 9pt 10pt 4pt; margin: 9pt 0; }}
.gorev .bas {{ break-inside: avoid; }}
.ipucu, .kontrol {{ break-inside: avoid; }}
div.hl {{ background: var(--soft); border: 0.8pt solid var(--line); border-left: 3pt solid var(--c); border-radius: 5pt; padding: 6pt 8pt; margin: 4pt 0 8pt; break-inside: avoid; }}
div.hl pre {{ font-family: Mono; font-size: 8.2pt; line-height: 1.45; white-space: pre-wrap; }} div.hl code {{ background: none; padding: 0; font-size: 1em; }}
.gorev .etiket {{ display: inline-block; font-family: Head; font-weight: 700; font-size: 7pt; letter-spacing: .06em; text-transform: uppercase;
  color: #fff; background: var(--c); padding: 1.5pt 6pt; border-radius: 99pt; margin-bottom: 4pt; }}
.gorev.challenge .etiket {{ background: #C2410C; }} .gorev.sahne-g .etiket {{ background: #3E8E41; }} .gorev.proje .etiket {{ background: #8B3FC8; }}
.gorev h3 {{ margin-top: 0; }}
.ipucu {{ font-size: 8.5pt; color: var(--ink2); }} .ipucu b {{ color: var(--ink); }}
.ipucu ol {{ margin-top: 1pt; }}
.kontrol {{ font-size: 8.5pt; background: #EEF8EE; border-radius: 5pt; padding: 4pt 7pt; margin: 4pt 0 6pt; }}
.kontrol code {{ background: #fff; }}
.cozum-ref {{ font-size: 7.5pt; color: var(--ink2); text-align: right; margin: 0 0 5pt; }}
.sahne {{ display: inline-block; background: #E8F4E0; border: 1pt solid #BFDDAA; border-radius: 6pt; padding: 5pt 7pt; margin: 6pt 0 2pt; }}
.sahne > span {{ color: #3E6B2A; }}
.sahne .row {{ display: flex; gap: 2pt; margin-top: 2pt; }}
.sahne .c {{ width: 15pt; height: 15pt; display: grid; place-items: center; font-style: normal; }}
.sahne .c img {{ height: 15pt; }} .sahne .wall {{ background: linear-gradient(#B5652F, #8E4A1F); border-radius: 2pt; }}
.sahne .coin {{ width: 10pt; height: 10pt; border-radius: 50%; background: radial-gradient(circle at 35% 35%, #FFE680, #E0A800); }}
.sahne .heart {{ color: #E8574A; font-size: 12pt; }}
/* gün açılışı */
.acilis {{ break-after: page; position: relative; height: 170mm; }}
.acilis .ust {{ display: flex; align-items: center; gap: 8pt; }}
.acilis .gun {{ font-family: Head; font-weight: 800; font-size: 11pt; background: var(--c2); padding: 2pt 10pt; border-radius: 99pt; }}
.acilis .bolge {{ font-family: Head; font-weight: 600; font-size: 9pt; color: var(--ink2); }}
.acilis h1 {{ font-size: 25pt; margin: 8pt 0 8pt; font-weight: 800; }}
.acilis .harita {{ width: 100%; height: 62mm; object-fit: cover; border-radius: 9pt; display: block; }}
.acilis .konusma {{ display: flex; gap: 8pt; align-items: flex-end; margin-top: 10pt; }}
.acilis .konusma img {{ width: 30mm; flex: none; }}
.acilis .balon {{ position: relative; background: var(--soft); border: 1pt solid var(--line); border-radius: 10pt; padding: 8pt 10pt; font-size: 9.2pt; }}
.acilis .balon::after {{ content: ""; position: absolute; left: -6pt; bottom: 12pt; border: 6pt solid transparent; border-right-color: var(--line); border-left: 0; }}
.acilis .proje {{ font-size: 8.5pt; color: var(--ink2); margin-top: 6pt; }}
.acilis .proje b {{ color: var(--ink); }}
/* kapak */
.kapak {{ page: cover; width: {W_MM}mm; height: {H_MM}mm; position: relative; overflow: hidden; color: #fff;
  background: radial-gradient(120mm 90mm at 85% 8%, #FFE08A 0, rgba(255,224,138,0) 60%), linear-gradient(160deg, #3A7BCB, #1B4C8F 70%); break-after: page; }}
.kapak .logo {{ position: absolute; left: 14mm; top: 14mm; width: 16mm; border-radius: 4mm; }}
.kapak .marka {{ position: absolute; left: 33mm; top: 16.5mm; font-family: Head; font-weight: 700; font-size: 10pt; opacity: .95; }}
.kapak h1 {{ position: absolute; left: 14mm; top: 40mm; width: 120mm; font-size: 36pt; font-weight: 800; line-height: 1.02; }}
.kapak h1 span {{ color: var(--c2); }}
.kapak .alt {{ position: absolute; left: 14mm; top: 84mm; width: 80mm; font-size: 11pt; line-height: 1.35; opacity: .95; }}
.kapak .piko {{ position: absolute; right: 6mm; bottom: 26mm; width: 70mm; filter: drop-shadow(0 4mm 5mm rgba(0,0,0,.3)); }}
.kapak .serit {{ position: absolute; left: 0; right: 0; bottom: 0; height: 20mm; background: var(--c2); color: var(--ink);
  display: flex; align-items: center; justify-content: space-between; padding: 0 14mm; font-family: Head; font-weight: 700; font-size: 9pt; }}
.kapak .etiket {{ position: absolute; left: 14mm; bottom: 28mm; font-family: Head; font-weight: 700; font-size: 9pt; background: rgba(255,255,255,.16);
  border: 1pt solid rgba(255,255,255,.4); padding: 3pt 9pt; border-radius: 99pt; }}
.kapak .bolgeler {{ position: absolute; left: 14mm; top: 112mm; display: flex; gap: 3mm; }}
.kapak .bolgeler img {{ width: 20mm; height: 26mm; object-fit: cover; border-radius: 3mm; border: 0.8mm solid rgba(255,255,255,.7); }}
/* ön bölüm */
.on h1 {{ font-size: 18pt; margin-bottom: 8pt; font-weight: 800; }}
.icindekiler {{ list-style: none; padding: 0; margin: 10pt 0; }}
.icindekiler li {{ display: flex; align-items: baseline; gap: 5pt; padding: 5pt 0; border-bottom: 0.6pt dotted #B9C8DE; font-size: 10pt; }}
.icindekiler li b {{ font-family: Head; font-weight: 700; color: var(--c); min-width: 34pt; }}
.icindekiler li .s {{ margin-left: auto; font-family: Head; font-weight: 600; }}
.adimlar {{ counter-reset: a; list-style: none; padding: 0; }}
.adimlar li {{ counter-increment: a; position: relative; padding-left: 20pt; margin-bottom: 6pt; }}
.adimlar li::before {{ content: counter(a); position: absolute; left: 0; top: 0; width: 14pt; height: 14pt; border-radius: 50%; background: var(--c2);
  font-family: Head; font-weight: 700; font-size: 8pt; display: grid; place-items: center; }}
.sayfa-sonu {{ break-after: page; }}
/* çözümler */
.cozum {{ margin: 8pt 0 12pt; }} .cozum h3 {{ break-after: avoid; }} .aciklama tr {{ break-inside: avoid; }}
.cozum h3 {{ font-size: 10pt; }} .cozum h3 small {{ font-family: Body; font-weight: 700; color: var(--c); margin-right: 4pt; }}
.aciklama {{ font-size: 8.3pt; margin: 4pt 0 0; border-collapse: collapse; width: 100%; }}
.aciklama td {{ padding: 2pt 4pt; vertical-align: top; border-top: 0.5pt solid var(--line); }}
.aciklama td:first-child {{ font-family: Mono; color: var(--ink2); width: 12pt; }}
.aciklama td:nth-child(2) {{ font-family: Mono; white-space: pre-wrap; width: 42%; }}
"""


def page(body, root, lang="tr"):
    return f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><style>{css(root)}</style></head><body>{body}</body></html>'


def gorev_html(t, etiket, cls, ref, root):
    out = f'<div class="gorev {cls}"><div class="bas"><span class="etiket">{etiket}</span><h3>{html.escape(t["title"])}</h3>{md(t["prompt"])}</div>'
    sc = (t.get("scene") or {}).get("target")
    if sc:
        out += sahne(sc, root)
    if (t.get("starter") or "").strip():
        out += kod(t["starter"], baslik="Başlangıç kodu")
    oc = (t.get("check") or {}).get("output_contains")
    if oc:
        out += '<div class="kontrol"><b>Kendini kontrol et:</b> çıktında şunlar olmalı: ' + ", ".join(f"<code>{html.escape(x)}</code>" for x in oc) + "</div>"
    if t.get("hints"):
        out += '<div class="ipucu"><b>İpuçları</b><ol>' + "".join(f"<li>{md_inline(h)}</li>" for h in t["hints"]) + "</ol></div>"
    out += f'<div class="cozum-ref">Çözüm: kitabın sonunda, {ref}</div></div>'
    return out


def gun_html(v, k, root):
    n = int(v["day"])
    reg = next(r for r in json.loads((REPO / "python/veri/kurs.json").read_text("utf8"))["regions"] if r["id"] == v["region"])
    poz = "mutlu" if n % 2 else "konusma"
    body = f"""<section class="acilis">
 <div class="ust"><span class="gun">Gün {n}</span><span class="bolge">{html.escape(reg["name"])}</span></div>
 <h1>{html.escape(v["title"])}</h1>
 <img class="harita" src="{root}/{k["bolge"].format(v["region"])}">
 <div class="box hedef"><h4>Bugünün hedefi</h4>{md_inline(v["objective"])}</div>
 <div class="konusma"><img src="{root}/{k["poz"].format(poz)}"><div class="balon">{md_inline(v["story"])}</div></div>
 <div class="proje">Proje katkısı ({html.escape(k["varsayilan_proje"])}): <b>{html.escape(v["project_contribution"])}</b>. {html.escape(v.get("game_role", ""))}</div>
</section>"""
    body += "<h2>Konu anlatımı</h2>"
    for s in v["sections"]:
        body += f"<h3>{html.escape(s['title'])}</h3>{md(s['body'])}"
    body += "<h2>Örnekler</h2>"
    for e in v["examples"]:
        out, err = calistir(e["code"], e.get("inputs"))
        sc = (e.get("scene") or {}).get("target") if isinstance(e.get("scene"), dict) else None
        if not sc and e.get("scene"):
            sc = out.split("\n")
        body += f"<h3>{html.escape(e['title'])}</h3>" + kod(e["code"], out, hata=err, sekil=sahne(sc, root) if sc else None)
        if e.get("note"):
            body += f'<p class="note">{md_inline(e["note"])}</p>'
    terms = {}
    for t in v["tasks"] + [v.get("challenge") or {}, v.get("visual_task") or {}, v.get("project_task") or {}]:
        for x in ((t or {}).get("explain") or {}).get("terms", []):
            if x.get("kind") != "değişken":  # değişken adları sözlüğü şişirir
                terms.setdefault(x["term"], x)
    if terms:
        body += '<div class="box sozluk"><h4>Bugünün sözlüğü</h4><dl>' + "".join(
            f'<dt>{html.escape(x["term"])}</dt><dd>{md_inline(x["desc"])} <em>{html.escape(x.get("kind", ""))}</em></dd>' for x in terms.values()) + "</dl></div>"
    body += "<h2>Görevler</h2>"
    for i, t in enumerate(v["tasks"], 1):
        body += gorev_html(t, f"Görev {i}", "", f"{n}.{i}", root)
    j = len(v["tasks"])
    if v.get("visual_task"):
        j += 1; body += gorev_html(v["visual_task"], "Sahne görevi", "sahne-g", f"{n}.{j}", root)
    if v.get("challenge"):
        j += 1; body += gorev_html(v["challenge"], "Challenge", "challenge", f"{n}.{j}", root)
    if v.get("project_task"):
        j += 1; body += gorev_html(v["project_task"], f"Proje: {k['varsayilan_proje']}", "proje", f"{n}.{j}", root)
    return body


def cozumler_html(gunler):
    body = '<section class="on"><h1>Çözümler</h1><p>Önce kendin dene! Takıldığında buraya bak. Her çözümün altında kodun satır satır ne yaptığı yazıyor. '
    body += "Senin çözümün farklı olabilir; çıktı aynıysa o da doğrudur.</p>"
    for v in gunler:
        n = int(v["day"])
        body += f'<h2>Gün {n}: {html.escape(v["title"])}</h2>'
        items = [(f"Görev {i}", t) for i, t in enumerate(v["tasks"], 1)]
        if v.get("visual_task"): items.append(("Sahne görevi", v["visual_task"]))
        if v.get("challenge"): items.append(("Challenge", v["challenge"]))
        if v.get("project_task"): items.append(("Proje", v["project_task"]))
        gorulen = set()
        for j, (etiket, t) in enumerate(items, 1):
            out, err = calistir(t["solution"], t.get("inputs") or ["Ece", "12", "Piko", "5"] if "input(" in t["solution"] else None)
            rows = ""
            for x in (t.get("explain") or {}).get("lines", []):
                notes = [nn for nn in x.get("notes", []) if nn not in gorulen]  # aynı açıklama gün içinde bir kez
                gorulen.update(notes)
                if notes:
                    rows += f'<tr><td>{x["n"]}</td><td>{html.escape(x["code"])}</td><td>{" ".join(md_inline(nn) for nn in notes)}</td></tr>'
            body += f'<div class="cozum"><h3><small>{n}.{j}</small>{etiket}: {html.escape(t["title"])}</h3>' + kod(t["solution"], out, hata=err)
            if rows:
                body += f'<table class="aciklama">{rows}</table>'
            body += "</div>"
    return body + "</section>"


def on_bolum_html(k, gunler, sayfalar, root):
    """(nasıl kullanılır, içindekiler): ayrı parçalar olarak basılır."""
    n0, n1 = int(gunler[0]["day"]), int(gunler[-1]["day"])
    toc = "".join(f'<li><b>Gün {int(v["day"])}</b>{html.escape(v["title"])}<span class="s">{sayfalar.get(int(v["day"]), "")}</span></li>' for v in gunler)
    toc += f'<li><b>Ek</b>Çözümler<span class="s">{sayfalar.get("cozum", "")}</span></li>'
    return f"""<section class="on">
<h1>Bu kitap nasıl kullanılır?</h1>
<p>Selam! Ben <b>{k["maskot"]}</b>. Bu kitapta her gün yeni bir şey öğrenip hemen kendi kodunu yazacaksın. Her gün aynı sırayla ilerler:</p>
<ol class="adimlar">
 <li><b>Konu anlatımı:</b> Günün fikirleri, kısa ve örnekli.</li>
 <li><b>Örnekler:</b> Kodu yaz, çalıştır, çıktıyı kitaptakiyle karşılaştır.</li>
 <li><b>Görevler:</b> Önce kendin dene. "Kendini kontrol et" kutusu ne yazman gerektiğini söyler; ipuçları da hazır.</li>
 <li><b>Sahne görevi, Challenge ve Proje:</b> Biraz daha zor ama çok eğlenceli. Proje adımlarıyla 30 günün sonunda kendi oyununu bitireceksin.</li>
 <li><b>Çözümler:</b> Kitabın sonunda, satır satır açıklamalarıyla.</li>
</ol>
<h2>Kodu nerede yazacağım?</h2>
<p>Bilgisayarına <b>python.org</b> adresinden Python'u kur. Kurulumla gelen <b>IDLE</b> programını aç, <i>File → New File</i> ile yeni bir dosya aç, kodunu yaz ve <b>F5</b> tuşuyla çalıştır. Kitabı kullanmak için internete ihtiyacın yok.</p>
<h2>Sayfaların altındaki QR kod</h2>
<p>İstersen her sayfanın altındaki QR kodu telefonunla okut: o günün <b>etkileşimli dersi</b> açılır. Orada kodunu tarayıcıda yazar, tek tıkla kontrol ettirir, rozet toplarsın. Bu tamamen isteğe bağlı; kitap tek başına yeterli.</p>
</section>""", f"""<section class="on"><h1>İçindekiler</h1><ul class="icindekiler">{toc}</ul>
<p style="font-size:8.5pt;color:#4A5B7A;margin-top:14pt">Bu bir örnek bölümdür: {k["ad"]} kitabının {n0}–{n1}. günleri.</p>
<p style="font-size:7.5pt;color:#4A5B7A;margin-top:30pt">© 2026 30 Günde · 30gunde.com.tr. Tüm hakları saklıdır. Maskotlar, görseller ve ders içerikleri 30 Günde'ye aittir; izin alınmadan çoğaltılamaz.</p>
</section>"""


def kapak_html(k, gunler, root):
    n0, n1 = int(gunler[0]["day"]), int(gunler[-1]["day"])
    kurs = json.loads((REPO / "python/veri/kurs.json").read_text("utf8"))
    bolgeler = "".join(f'<img src="{root}/{k["bolge"].format(r["id"])}">' for r in kurs["regions"][:3] if (REPO / k["bolge"].format(r["id"])).exists())
    return f"""<section class="kapak"><img class="logo" src="{root}/{k["logo"]}"><div class="marka">30gunde.com.tr</div>
<h1>30 Günde<br><span>Python</span></h1>
<div class="alt">Macera haritasıyla, her gün bir adım: kodlamaya {k["maskot"]} ile başla.</div>
<div class="bolgeler">{bolgeler}</div>
<div class="etiket">Örnek bölüm · Gün {n0}–{n1}</div>
<img class="piko" src="{root}/{k["poz"].format("tebrik")}">
<div class="serit"><span>12 yaş ve üstü</span><span>Görevler · Çözümler · Proje</span></div></section>"""


# ---------- PDF ----------
def pdf_bas(parcalar, out_dir):
    """Her HTML parçasını ayrı PDF'e basar; sayfa sayılarını döndürür."""
    from playwright.sync_api import sync_playwright
    paths = []
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--allow-file-access-from-files"])
        pg = b.new_page()
        for ad, html_ in parcalar:
            f = out_dir / f"{ad}.html"; f.write_text(html_, "utf8")
            pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready")
            pg.wait_for_load_state("networkidle")
            pdf = out_dir / f"{ad}.pdf"
            pg.pdf(path=str(pdf), width=f"{W_MM}mm", height=f"{H_MM}mm", print_background=True, prefer_css_page_size=True)
            paths.append((ad, pdf, len(PdfReader(str(pdf)).pages)))
        b.close()
    return paths


def altbilgi(writer, sayfa_bilgisi, k):
    """Her sayfanın altına sayfa numarası, gün adı ve o günün QR kodunu basar."""
    pdfmetrics.registerFont(TTFont("Head", str(FONTS / "Poppins-SemiBold.ttf")))
    pdfmetrics.registerFont(TTFont("Body", str(FONTS / "Poppins-Regular.ttf")))
    qr_cache = {}
    for i, (etiket, url) in enumerate(sayfa_bilgisi):
        if etiket is None:
            continue
        buf = io.BytesIO()
        c = canvas.Canvas(buf, pagesize=(W_MM * mm, H_MM * mm))
        no = i + 1
        sol = no % 2 == 0  # çift sayfalar solda: numara dış kenarda
        c.setFillColorRGB(0.07, 0.14, 0.25); c.setFont("Head", 8)
        c.drawString(14 * mm, 9 * mm, str(no)) if sol else c.drawRightString((W_MM - 14) * mm, 9 * mm, str(no))
        c.setFillColorRGB(0.29, 0.36, 0.48); c.setFont("Body", 6.5)
        metin = f"{k['ad']} · {etiket}"
        if url:
            if url not in qr_cache:
                from reportlab.lib.utils import ImageReader
                qr_cache[url] = ImageReader(io.BytesIO(qr_png(url)))
            q = 13 * mm
            qx = (W_MM - 14) * mm - q if sol else 14 * mm
            c.drawImage(qr_cache[url], qx, 4.5 * mm, q, q)
            tx = qx - 2 * mm if sol else qx + q + 2 * mm
            c.setFont("Head", 6.5); c.setFillColorRGB(0.18, 0.43, 0.71)
            (c.drawRightString if sol else c.drawString)(tx, 12.2 * mm, "Etkileşimli ders (isteğe bağlı)")
            c.setFont("Body", 6.5); c.setFillColorRGB(0.29, 0.36, 0.48)
            (c.drawRightString if sol else c.drawString)(tx, 8.6 * mm, metin)
            (c.drawRightString if sol else c.drawString)(tx, 5.4 * mm, url.replace("https://", ""))
        else:
            c.drawCentredString(W_MM / 2 * mm, 9 * mm, metin)
        c.save()
        writer.pages[i].merge_page(PdfReader(buf).pages[0])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kurs", choices=list(KURS))
    ap.add_argument("gunler", help="ör. 1-3")
    a = ap.parse_args()
    k = KURS[a.kurs]
    fontlari_hazirla()
    g0, g1 = map(int, a.gunler.split("-"))
    gunler = [json.loads((REPO / a.kurs / "veri" / f"gun-{d:02d}.json").read_text("utf8")) for d in range(g0, g1 + 1)]
    work = HERE / "is"; work.mkdir(exist_ok=True)
    root = REPO.as_uri()
    gun_parca = [(f"gun-{int(v['day']):02d}", page(gun_html(v, k, root), root)) for v in gunler]
    coz = ("cozumler", page(cozumler_html(gunler), root))
    kapak = ("kapak", page(kapak_html(k, gunler, root), root))
    # ön bölümün uzunluğu sayfa numaralarına bağlı değil: önce boş numaralarla bas, sonra gerçekleriyle
    nasil, toc = on_bolum_html(k, gunler, {}, root)
    bilgi = pdf_bas([kapak, ("on", page(nasil, root)), ("icindekiler", page(toc, root))] + gun_parca + [coz], work)
    sayfa = 1; baslangic = {}
    for ad, _, n in bilgi:
        baslangic[ad] = sayfa; sayfa += n
    nums = {int(v["day"]): baslangic[f"gun-{int(v['day']):02d}"] for v in gunler}
    nums["cozum"] = baslangic["cozumler"]
    bilgi[2] = pdf_bas([("icindekiler", page(on_bolum_html(k, gunler, nums, root)[1], root))], work)[0]
    writer = PdfWriter(); sayfa_bilgisi = []
    for ad, pdf, n in bilgi:
        for p_ in PdfReader(str(pdf)).pages:
            writer.add_page(p_)
        if ad == "kapak":
            sayfa_bilgisi += [(None, None)] * n
        elif ad.startswith("gun-"):
            d = int(ad[4:]); v = next(x for x in gunler if int(x["day"]) == d)
            sayfa_bilgisi += [(f"Gün {d}: {v['title']}", k["url"].format(d))] * n
        else:
            sayfa_bilgisi += [("Çözümler" if ad == "cozumler" else "Giriş", "https://30gunde.com.tr")] * n
    altbilgi(writer, sayfa_bilgisi, k)
    writer.add_metadata({"/Title": f"{k['ad']} · Gün {g0}–{g1} (örnek)", "/Author": "30 Günde", "/Subject": "30gunde.com.tr"})
    out = REPO / "cikti" / "kitap" / f"30-gunde-{a.kurs}-gun-{g0:02d}-{g1:02d}.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "wb") as f:
        writer.write(f)
    print(f"hazır: {out} ({len(writer.pages)} sayfa)")


if __name__ == "__main__":
    main()
