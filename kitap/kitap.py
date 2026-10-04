# 30 Günde kitabı: gün gün ders verisinden (veri/gun-XX.json) baskıya ve e-kitaba uygun PDF üretir.
#   python3 kitap/kitap.py python 1-30           # tam kitap: cikti/kitap/30-gunde-python.pdf
#   python3 kitap/kitap.py python 1-3            # örnek bölüm: cikti/kitap/30-gunde-python-gun-01-03.pdf
#   python3 kitap/kitap.py javascript 1-2        # cikti/kitap/30-gunde-javascript-gun-01-02.pdf
#   python3 kitap/kitap.py python 1-30 --dil en  # İngilizce baskı: cikti/kitap/30-days-of-python.pdf
#     (İngilizce içerik python/veri/en/ altında; satır açıklamaları aciklama_en.py ile koddan üretilir)
# Kitap siteden bağımsız kullanılabilir: örneklerin çıktıları kodu gerçekten çalıştırarak yazılır, görevlerin
# "kendini kontrol et" maddeleri ve çözümleri (satır satır açıklamalarıyla) kitabın içindedir. Her sayfanın altında
# YouTube kanalına (her günün video anlatımı) giden bir QR kod bulunur; günün açılış sayfasında ayrıca o günün
# etkileşimli dersinin adresi vardır (isteğe bağlı kullanım). Tüm günler seçilirse (1-30) tam kitap basılır.
# Gerekenler: pip install markdown pygments "qrcode[pil]" pypdf reportlab playwright
import argparse, html, io, json, re, subprocess, sys, tempfile
from pathlib import Path

import markdown
import qrcode
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import HtmlLexer, JavascriptLexer, PythonLexer
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
    "python": {"kod": "python", "ad": "30 Günde Python", "dil_adi": "Python", "maskot": "Piko",
               "renk": "#2F6DB5", "renk2": "#FFC83D", "ink": "#13233F",
               "logo": "gorseller/python/logo-128.png", "bolge": "gorseller/python/harita/{}.webp", "bolge_tur": "harita",
               "poz": "maskotlar/piko-python/pozlar/{}.png", "kapak_poz": "maskotlar/piko-python/pozlar/tebrik.png",
               "acilis_poz": ("mutlu", "konusma"), "url": "https://30gunde.com.tr",
               "varsayilan_proje": "Piko'nun Macerası", "alt": "Macera haritasıyla, her gün bir adım: kodlamaya Piko ile başla.",
               "kurulum": "Bilgisayarına <b>python.org</b> adresinden Python'u kur. Kurulumla gelen <b>IDLE</b> programını aç, "
                          "<i>File → New File</i> ile yeni bir dosya aç, kodunu yaz ve <b>F5</b> tuşuyla çalıştır."},
    "javascript": {"kod": "javascript", "ad": "30 Günde JavaScript", "dil_adi": "JavaScript", "maskot": "Kodi",
                   "renk": "#2B3A8C", "renk2": "#F7DF1E", "ink": "#0B1026",
                   "logo": "gorseller/javascript/simgeler/icon-512.png", "bolge": "gorseller/javascript/bolgeler/{}.webp", "bolge_tur": "gezegen",
                   "uzay": "gorseller/javascript/arka-plan/bg-space-wide.webp",
                   "poz": "maskotlar/kodi-javascript/pozlar/{}.png", "kapak_poz": "maskotlar/kodi-javascript/kahraman.png",
                   "acilis_poz": ("el-sallama", "konusma"),
                   "url": "https://30gunde.com.tr",  # derslerin gün gün ayrı adresi yok
                   "varsayilan_proje": "Yıldız Avcısı", "alt": "Uzay yolculuğuyla, her gün bir adım: kodlamaya Kodi ile başla.",
                   "kurulum": "Bir tarayıcı aç (Chrome, Edge ya da Firefox) ve <b>F12</b> ile Geliştirici Araçları'nı aç. "
                              "<b>Console</b> sekmesine kodunu yaz ve Enter'a bas; <code>console.log</code> çıktıları orada görünür. "
                              "Sayfa (HTML) görevlerinde kodu bir <code>.html</code> dosyasındaki <code>&lt;script&gt;</code> etiketine yazıp dosyayı tarayıcıda aç."},
}
VIDEO = "https://www.youtube.com/@30gundekod"  # iki kursun da günlük video anlatımları bu kanalda
K = KURS["python"]  # main() seçilen kursa göre değiştirir
DIL = "tr"          # main() --dil ile değiştirir

# İngilizce baskıda kursun değişen alanları
KURS_EN = {
    "python": {"ad": "30 Days of Python", "varsayilan_proje": "Piko's Adventure",
               "alt": "Day by day across an adventure map: start coding with Piko.",
               "kurulum": "Install Python from <b>python.org</b>. Open <b>IDLE</b>, which comes with it, create a new file with "
                          "<i>File → New File</i>, write your code and run it with <b>F5</b>."},
}

# Arayüz metinleri (tr, en)
T = {
    "cikti": ("Çıktı", "Output"), "sayfada": ("Sayfa açılınca", "When the page opens"), "hata": ("Hata", "Error"), "sahne": ("Sahne", "Stage"),
    "html_hazir": ("Sayfanın HTML'i (hazır)", "The page's HTML (ready-made)"), "baslangic": ("Başlangıç kodu", "Starter code"),
    "kontrol": ("Kendini kontrol et:", "Check yourself:"), "cikti_olmali": ("çıktında şunlar olmalı: ", "your output should contain: "),
    "kod_gecmeli": ("kodunda şunlar geçmeli: ", "your code should contain: "), "ipuclari": ("İpuçları", "Hints"),
    "cozum_ref": ("Çözüm: kitabın sonunda, {ref}", "Solution: at the back of the book, {ref}"),
    "gun": ("Gün {n}", "Day {n}"), "gunler": ("Gün {a}–{b}", "Days {a}–{b}"),
    "hedef": ("Bugünün hedefi", "Today's goal"), "proje_katki": ("Proje katkısı", "Project piece"),
    "konu": ("Konu anlatımı", "The lesson"), "ornekler": ("Örnekler", "Examples"), "sozluk": ("Bugünün sözlüğü", "Words of the day"),
    "gorevler": ("Görevler", "Tasks"), "gorev": ("Görev {i}", "Task {i}"), "sahne_g": ("Sahne görevi", "Stage task"),
    "challenge": ("Challenge", "Challenge"), "proje": ("Proje", "Project"),
    "video_kutu": ("<b>Video anlatım</b>YouTube'da <b style=\"display:inline\">30 Günde Kod</b> kanalında „Gün {n} · {title}” videosu",
                   "<b>Video lesson</b>On the <b style=\"display:inline\">30 Günde Kod</b> YouTube channel: the “Day {n} · {title}” video"),
    "site_kutu": ("<b>Etkileşimli ders</b>Görevleri tarayıcında dene:<br>30gunde.com.tr · {kurs} · Gün {n}", ""),
    "paket": ("<b>Bu gün için:</b> kodları kendi bilgisayarında çalıştırmadan önce terminalde <code>pip install {p}</code> yaz (bkz. 20. gün).",
              "<b>For this day:</b> before running the code on your computer, type <code>pip install {p}</code> in the terminal (see Day 20)."),
    "cozumler": ("Çözümler", "Solutions"),
    "cozum_giris": ("Önce kendin dene! Takıldığında buraya bak. ", "Try it yourself first! Look here when you get stuck. "),
    "cozum_satir": ("Her çözümün altında kodun satır satır ne yaptığı yazıyor. ", "Under every solution, you'll find what the code does line by line. "),
    "cozum_cikti": ("Her çözümün altında çıktısı var. ", "Every solution comes with its output. "),
    "cozum_farkli": ("Senin çözümün farklı olabilir; çıktı aynıysa o da doğrudur.", "Your solution may be different; if the output is the same, it's right too."),
    "icindekiler": ("İçindekiler", "Contents"), "ekler": ("Ekler", "Appendix"), "ek": ("Ek", "A"), "son": ("Son", "End"),
    "sertifikan": ("Sertifikan", "Your certificate"), "giris": ("Giriş", "Introduction"),
    "ornek_bolum": ("Bu bir örnek bölümdür: {ad} kitabının {a}–{b}. günleri.", "This is a sample chapter: days {a}–{b} of {ad}."),
    "telif": ("© 2026 30 Günde · 30gunde.com.tr. Tüm hakları saklıdır. Maskotlar, görseller ve ders içerikleri 30 Günde'ye aittir; izin alınmadan çoğaltılamaz.",
              "© 2026 30 Günde · 30gunde.com.tr. All rights reserved. The mascots, images and lesson content belong to 30 Günde and may not be copied without permission."),
    "kapak_baslik": ("30 Günde<br><span>{dil}</span>", "30 Days of<br><span>{dil}</span>"),
    "kapak_tam": ("30 gün · {g} görev · tüm çözümler", "30 days · {g} tasks · all solutions"),
    "kapak_ornek": ("Örnek bölüm · Gün {a}–{b}", "Sample chapter · Days {a}–{b}"),
    "yas": ("12 yaş ve üstü", "Ages 12+"), "serit": ("Görevler · Çözümler · Proje", "Tasks · Solutions · Project"),
    "video_rozet": ("Video anlatımlı", "With video lessons"), "video_rozet_alt": ("Her gün için YouTube'da bir video", "A YouTube video for every day"),
    "srt_ust": ("Başarı sertifikası", "Certificate of achievement"), "srt_baslik": ("Tebrikler!", "Congratulations!"),
    "srt_ad": ("adın soyadın", "your name"),
    "srt_metin": ("<b>{ad}</b> macerasının 30 gününü tamamlayarak {dil} ile kendi programlarını yazmayı öğrendi.",
                  "completed all 30 days of the <b>{ad}</b> adventure and learned to write their own programs in {dil}."),
    "srt_tarih": ("Tarih", "Date"), "srt_maskot": ("{m} · yol arkadaşın", "{m} · your guide"),
    "alt_video_gun": ("Video anlatım: YouTube · „Gün {d}” videosu", "Video lesson: YouTube · “Day {d}” video"),
    "alt_video": ("Video anlatımlar: YouTube", "Video lessons: YouTube"),
}


def t(anahtar, **kw):
    s = T[anahtar][1 if DIL == "en" else 0]
    return s.format(**kw) if kw else s


def veri_dizini(kurs):
    return REPO / kurs / "veri" / ("en" if DIL == "en" else "")


def kurs_json(k):
    return json.loads((veri_dizini(k["kod"]) / "kurs.json").read_text("utf8"))

# Kodları çalıştırmak için ayrıca kurulması gereken paketler (import adı → pip adı)
PAKETLER = {"bs4": "beautifulsoup4", "numpy": "numpy", "pandas": "pandas", "requests": "requests", "flask": "flask", "pymongo": "pymongo"}

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
    ("Çalıştır'a bas ve Çıktı alanına bak.", "Kodu çalıştır ve konsoldaki çıktıya bak."),
    ("yazdığın şeyi **Çıktı** alanına yazar", "yazdığın şeyi konsola (**Console**) yazar"),
    ("bu sayfadaki editöre yazdığın kod doğrudan tarayıcında çalışır", "yazdığın kod doğrudan tarayıcında çalışır"),
    ("Editörde `:` yazıp Enter'a basınca", "IDLE gibi editörlerde `:` yazıp Enter'a basınca"),
    ("Girdi kutusuna farklı yaşlar yazıp dene.", "Programı birkaç kez çalıştırıp farklı yaşlar yazarak dene."),
    ("Cevabı editörün altındaki **Girdi** kutusuna yaz.", "Program sorunca yaşını yaz ve Enter'a bas."),
    ("Girdi kutusuna farklı cevaplar yazıp dene.", "Programı birkaç kez çalıştırıp farklı cevaplar yazarak dene."),
    ("bu sitede 6 saniye sonra durdurulur.", "böyle bir program kendiliğinden durmaz. Başına gelirse **Ctrl+C** tuşlarıyla durdurabilirsin."),
    ("Oyunu Kaydet ve Yükle düğmeleri senin fonksiyonlarını kullanır.", "Oyunun kaydetme ve yükleme özelliği senin fonksiyonlarını kullanır."),
    ("Bu sitede dosyalar", "Görevlerde dosyalar"),
    ("Burada yazdığın dosyalar tarayıcının hafızasında, **sadece o çalıştırma boyunca** yaşar. Bir sonraki çalıştırmada her şey temiz başlar. "
     "Bu yüzden görevlerde önce yazıp sonra aynı kodda okuyacağız.\n\nKendi bilgisayarında Python kurduğunda dosyalar gerçekten diske yazılır ve kalıcı olur.",
     "Bilgisayarında Python dosyaları gerçekten diske yazar: program kapansa da dosya, kodunun bulunduğu klasörde kalır. "
     "Görevlerde yine de önce yazıp sonra **aynı kodda** okuyacağız; böylece her görev tek başına çalışır.\n\n"
     "(Etkileşimli derslerde dosyalar tarayıcının hafızasında, sadece o çalıştırma boyunca yaşar.)"),
    ("Bu sitedeki Python, bazı popüler paketlerle birlikte gelir. `import this` yazıp çalıştır, sana bir sürpriz var.",
     "Küçük bir sürpriz: `import this` yazıp çalıştır. Bu modül Python'la birlikte gelir, kurmana gerek yok."),
    ("Bu sitede internetten sayfa indiremediğimiz için HTML'i hazır bir yazı olarak vereceğiz.",
     "Örnekler internete bağlanmadan da çalışsın diye HTML'i hazır bir yazı olarak vereceğiz."),
    ("İlk çalıştırmada BeautifulSoup paketi yükleneceği için birkaç saniye bekleyebilirsin.",
     "BeautifulSoup bilgisayarında yoksa önce terminalde `pip install beautifulsoup4` yazarak kur (20. gün)."),
    ("Bu sitede bir sunucu başlatamıyoruz, ama aynı fikri düz Python ile deneyeceğiz.",
     "Örneklerde sunucu başlatmadan aynı fikri düz Python ile deneyeceğiz. Flask'ı denemek istersen: `pip install flask`."),
    ("Bu sitede gerçek bir veritabanına bağlanamıyoruz.", "Örneklerde gerçek bir veritabanı kurmakla uğraşmayacağız."),
    ("Bu sitede internete istek gönderemiyoruz.", "Örnekler internetsiz de çalışsın diye gerçek istek göndermeyeceğiz."),
    ("Bu sitede bir sunucu çalıştıramadığımız için aynı mantığı", "Sunucu kurmadan aynı mantığı"),
    ("Kendi bilgisayarına Python kur (python.org) ve bu sitede yazdığın projeleri orada da çalıştır.",
     "Bu kitapta yazdığın kodları sakla: her biri yeni bir maceranın başlangıcı olabilir."),
    ("Bu parçayı da ekleyince **Proje** sayfasına git ve **Oyunumu oyna**'ya bas. 30 gün boyunca", "Bu parçayla 30 gün boyunca"),
    ("Yön tuşlarıyla oynarsın ve hangi parçanın ne yaptığını oyunun günlüğünde görürsün.",
     "İstersen 30gunde.com.tr'deki **Proje** sayfasında **Oyunumu oyna**'ya bas: parçaların yön tuşlarıyla oynanan bir oyuna dönüşür."),
    # JavaScript
    ("; editörün tuş çubuğunda da var.", "."),
    ("Sayfanın HTML'i görevle birlikte hazır gelir; sen yalnızca JavaScript yazarsın. Editörün yanındaki **önizleme** paneli sayfayı gösterir. "
     "Kodun sayfa yüklendikten sonra çalışır, yani bütün elemanlar hazırdır. `console.log` da çalışmaya devam eder; çıktısı yine Çıktı alanında görünür.",
     "Sayfanın HTML'i her görevde hazır verilir; sen yalnızca JavaScript yazarsın. Bir `.html` dosyası oluştur, verilen HTML'i `<body>` içine, "
     "kodunu da en alta bir `<script>` etiketinin içine yaz ve dosyayı tarayıcıda aç. Kod sayfa yüklendikten sonra çalışır, yani bütün elemanlar hazırdır. "
     "`console.log` çıktıları Geliştirici Araçları'nın **Console** sekmesinde görünür. Kitapta her sayfa kodunun altında, sayfa açılınca nasıl "
     "göründüğünü gösteren bir ekran görüntüsü var."),
    ("Kodu değiştirip Çalıştır'a bas; önizleme her çalıştırmada sayfayı baştan kurar.", "Kodu değiştirip sayfayı yenile; tarayıcı her yenilemede sayfayı baştan kurar."),
    ("Kodu çalıştırdıktan sonra önizlemedeki düğmeye kendin tıklayıp dene.", "Sayfayı açtıktan sonra düğmeye kendin tıklayıp dene."),
    ("Çalıştır'a bastıktan sonra önizlemedeki düğmeye birkaç kez tıkla.", "Sayfayı açınca düğmeye birkaç kez tıkla."),
    ("Önizlemede Başla'ya tıklayınca envanteri görürsün. Kontrol, envantere yeni eşya ekleyip `renderInventory()`'yi tekrar çağıracak.",
     "Sayfada Başla'ya tıklayınca envanteri görürsün. Envantere yeni bir eşya ekleyip `renderInventory()`'yi tekrar çağırarak da dene."),
    ("Önizleme tuşları duysun diye önce önizlemenin içine bir kez tıkla.", "Sayfa tuşları duysun diye önce sayfanın içine bir kez tıkla."),
    ("Bu kursun önizlemesinde `localStorage` bir taklittir: aynı görevde çalıştırmalar arasında korunur ama gerçek tarayıcı defterine yazmaz.",
     "Denerken kayıtları silmek istersen Console'a `localStorage.clear()` yaz."),
    ("Bir şey yaz ve Çalıştır'a yeniden bas: notun yerinde duruyor. Gerçek bir sitede sayfa yenilense de kalır.",
     "Bir şey yaz ve sayfayı yenile: notun yerinde duruyor."),
    ("Çıktı alanında", "Console'da"),
    ("(Önizleme 4 ziyaretle başlıyor.)", "(Kitaptaki ekran görüntüsü alınırken defterde 4 ziyaret kayıtlıydı.)"),
    ("(Önizleme 35 rekoruyla başlıyor.)", "(Kitaptaki ekran görüntüsü alınırken rekor 35'ti.)"),
    ("Önizlemedeki kayıt bilerek bozuk bırakıldı.", "Kitaptaki ekran görüntüsünde defterdeki kayıt bilerek bozuk bırakıldı."),
    ("(ve bu editördeki gibi en üst seviyede)", "(ve modül betiklerinde en üst seviyede)"),
    ("Bu kursun editörü her görevde tek bir betik çalıştırdığı için görevlerde `import` kullanamayız; bütün kod tek kutuda.",
     "Kitaptaki görevlerde her şeyi tek bir betikte yazdığımız için `import` kullanmıyoruz."),
    ("Önizlemeye tıkla, sonra", "Sayfaya tıkla, sonra"),
    ("önizlemeye tıklayıp", "sayfaya tıklayıp"),
    ("Birkaç kez tıkla, sonra yeniden Çalıştır:", "Birkaç kez tıkla, sonra sayfayı yenile:"),
    ("Bu kursta önizleme gerçek internete çıkmaz; senin için hazırlanmış bir deneme API'si var:",
     "Bu kurs için hazırlanmış bir deneme API'si var. Etkileşimli derslerde hazırdır; kendi bilgisayarında denerken kitabın sonundaki "
     "**Deneme API'si** ekindeki kodu betiğinin en üstüne yapıştır:"),
    ("Görevleri bitirince 30. günü tamamla ve sertifikanı al.", "Görevleri bitirince 30 günlük macerayı tamamlamış olursun; kitabın sonundaki sertifika seni bekliyor."),
]


def uyarla(s):
    for a, b in UYARLA:
        s = s.replace(a, b)
    return s


def md(s):
    return markdown.markdown(uyarla(s or "") if DIL == "tr" else (s or ""), extensions=["fenced_code", "tables", "codehilite"],
                             extension_configs={"codehilite": {"guess_lang": False, "css_class": "hl"}})


def md_inline(s):
    h = md(s).strip()
    return h[3:-4] if h.startswith("<p>") and h.endswith("</p>") and h.count("<p>") == 1 else h


FORMATTER = HtmlFormatter(cssclass="hl", nowrap=True)


def lexer():
    return PythonLexer() if K["kod"] == "python" else JavascriptLexer()


def kod(code, cikti=None, baslik=None, hata=False, sekil=None, lex=None):
    code = (code or "").rstrip("\n")
    out = f'<div class="code">{f"<div class=cap>{html.escape(baslik)}</div>" if baslik else ""}<pre class="hl">{highlight(code, lex or lexer(), FORMATTER).rstrip()}</pre></div>'
    if cikti is not None:
        out += f'<div class="out{" err" if hata else ""}"><span>{t("hata") if hata else t("cikti")}</span><pre>{html.escape(cikti.rstrip())}</pre></div>'
    if sekil:
        out += sekil
    return f'<div class="kod-grup">{out}</div>'


def calistir(code, inputs=None):
    """Kodu çalıştırıp konsolda görüneceği gibi çıktıyı döndürür (input() cevapları ekrana yazılır)."""
    if K["kod"] == "javascript" and re.search(r"\b(document|window|alert|prompt|localStorage|requestAnimationFrame)\b", code):
        return None, False  # sayfa (DOM) kodu: çıktı tarayıcıda görünür, burada çalıştırılmaz
    pre = ""
    if inputs:
        pre = ("import builtins as _b\n_i = iter(%r)\n"
               "def _inp(p=''):\n    v = next(_i)\n    print(p + v)\n    return v\n_b.input = _inp\n") % (list(inputs),)
    with tempfile.TemporaryDirectory() as d:
        if K["kod"] == "python":
            f = Path(d) / "k.py"; f.write_text(pre + code, "utf8"); cmd = [sys.executable, str(f)]
        else:
            f = Path(d) / "k.mjs"; f.write_text(code, "utf8"); cmd = ["node", str(f)]
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=10, cwd=d)
    if r.returncode != 0:
        last = r.stderr.strip().splitlines()[-1] if r.stderr.strip() else "Hata"
        return (r.stdout + last).strip("\n"), True
    return r.stdout.rstrip("\n"), False


# ---------- JavaScript sayfa (DOM) kodları: tarayıcıda çalıştırılıp ekran görüntüsü alınır ----------
EKRAN = {}  # tembel açılan tarayıcı
EKRAN_CSS = """body { font-family: N, sans-serif; font-size: 15px; color: #13233F; margin: 12px; background: #fff; line-height: 1.4; }
button { font: inherit; padding: 4px 12px; border-radius: 7px; border: 1px solid #9DB4D6; background: #EAF1FB; color: #13233F; }
input, select, textarea { font: inherit; padding: 3px 6px; border: 1px solid #9DB4D6; border-radius: 6px; }
h1, h2, h3 { margin: 4px 0 8px; } canvas { max-width: 100%; }"""


def ekran_kapat():
    if EKRAN:
        EKRAN["b"].close(); EKRAN["p"].stop(); EKRAN.clear()


def sayfa_goruntusu(code, html_="", css_="", storage=None):
    """Sayfa kodunu verilen HTML ile çalıştırır; (görüntü uri'si, konsol çıktısı, hata) döndürür. Sonuçlar önbelleğe alınır."""
    import hashlib
    anahtar = hashlib.sha1(json.dumps([code, html_, css_, storage], ensure_ascii=False).encode()).hexdigest()[:16]
    d = HERE / "is" / "ekran"; d.mkdir(parents=True, exist_ok=True)
    img, meta = d / f"{anahtar}.jpg", d / f"{anahtar}.json"
    if not meta.exists():
        if not EKRAN:
            from playwright.sync_api import sync_playwright
            EKRAN["p"] = sync_playwright().start()
            EKRAN["b"] = EKRAN["p"].chromium.launch()
        ctx = EKRAN["b"].new_context(viewport={"width": round((W_MM - 28) / 25.4 * 96), "height": 700}, device_scale_factor=2)
        pg = ctx.new_page()
        loglar, hatalar = [], []
        pg.on("console", lambda m: loglar.append(m.text) if m.type in ("log", "info", "warning", "error") else None)
        pg.on("pageerror", lambda e: hatalar.append(str(e).splitlines()[0]))

        def yonlendir(route):
            u = route.request.url
            if u.startswith("http://kitap.local/font/"):
                route.fulfill(path=str(FONTS / "Nunito-400.ttf"))
            elif u.startswith("http://kitap.local/"):
                tohum = "".join(f"localStorage.setItem({json.dumps(k_)}, {json.dumps(v_)});" for k_, v_ in (storage or {}).items())
                modul = ' type="module"' if re.search(r"^(for )?await\b", code, re.M) else ""
                sayfa = (f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><style>@font-face {{ font-family: N; src: url(/font/n.ttf); }}'
                         f'{EKRAN_CSS}{css_ or ""}</style></head><body>{html_ or ""}'
                         f'<script>{(HERE / "demo_api.js").read_text("utf8")}\nlocalStorage.clear();{tohum}</script>'
                         f'<script{modul}>{code}</script></body></html>')
                route.fulfill(body=sayfa, content_type="text/html; charset=utf-8")
            else:
                route.abort()
        pg.route("**/*", yonlendir)
        pg.goto("http://kitap.local/index.html")
        pg.wait_for_timeout(2500)  # zamanlayıcılar, fetch ve animasyonlar bir süre çalışsın
        h = pg.evaluate("Math.ceil(document.documentElement.getBoundingClientRect().height)")
        pg.screenshot(path=str(d / f"{anahtar}.png"), clip={"x": 0, "y": 0, "width": pg.viewport_size["width"], "height": max(40, min(h, 520))})
        ctx.close()
        from PIL import Image
        Image.open(d / f"{anahtar}.png").convert("RGB").save(img, "JPEG", quality=88, optimize=True)
        (d / f"{anahtar}.png").unlink()
        meta.write_text(json.dumps({"log": "\n".join(loglar), "hata": hatalar[0] if hatalar else ""}, ensure_ascii=False), "utf8")
    m = json.loads(meta.read_text("utf8"))
    return img.as_uri(), m["log"], m["hata"]


def kod_ve_sonuc(code, girdi=None, sayfa=None, sekil=None):
    """Kod bloğu + çıktısı. Sayfa (DOM) kodlarında çıktının yerine sayfanın ekran görüntüsü gelir."""
    out, err = calistir(code, girdi)
    if out is None and sayfa is not None:
        uri, log, hata = sayfa_goruntusu(code, sayfa.get("html", ""), sayfa.get("css", ""), sayfa.get("storage"))
        ekran = f'<div class="out ekran"><span>{t("sayfada")}</span><img src="{uri}"></div>'
        if hata:
            log = (log + "\n" if log else "") + hata
        return kod(code, log if log else None, hata=bool(hata), sekil=ekran)
    return kod(code, out, hata=err, sekil=sekil)


def sahne(rows, root):
    """Sahne ızgarası: * Piko, # duvar, o altın, H kalp."""
    def cell(ch):
        if ch == "*": return f'<i class="c"><img src="{root}/{K["poz"].format("on")}"></i>'
        if ch == "#": return '<i class="c wall"></i>'
        if ch == "o": return '<i class="c"><b class="coin"></b></i>'
        if ch == "H": return '<i class="c heart">♥</i>'
        return '<i class="c"></i>'
    return f'<div class="sahne"><span>{t("sahne")}</span>' + "".join(f'<div class="row">{"".join(cell(c) for c in r)}</div>' for r in rows) + "</div>"


def jpg(rel, genislik_px, oran=None):
    """Fotoğraf gibi görselleri baskı çözünürlüğünde JPEG'e çevirir (PDF'e sıkıştırılmış gömülür).
    oran (genişlik/yükseklik) verilirse ortadan o orana kırpılır."""
    from PIL import Image, ImageOps
    src = REPO / rel
    out = HERE / "is" / "img" / f"{src.stem}-{genislik_px}{f'-{oran:.2f}' if oran else ''}.jpg"
    if not out.exists():
        out.parent.mkdir(parents=True, exist_ok=True)
        im = Image.open(src).convert("RGB")
        if oran:
            im = ImageOps.fit(im, (genislik_px, round(genislik_px / oran)), Image.LANCZOS)
        im.thumbnail((genislik_px, genislik_px * 4))
        im.save(out, "JPEG", quality=86, optimize=True, progressive=True)
    return out.as_uri()


def png(rel, genislik_px):
    """Şeffaf görselleri (gezegenler, maskotlar) küçültüp PNG olarak saklar."""
    from PIL import Image
    src = REPO / rel
    out = HERE / "is" / "img" / f"{src.stem}-{genislik_px}.png"
    if not out.exists():
        out.parent.mkdir(parents=True, exist_ok=True)
        im = Image.open(src).convert("RGBA")
        im.thumbnail((genislik_px, genislik_px * 4))
        im.save(out, "PNG", optimize=True)
    return out.as_uri()


def bolge_gorseli(k, bolge, genislik_px, oran=None):
    if k["bolge_tur"] == "gezegen":
        return png(k["bolge"].format(bolge), genislik_px)
    return jpg(k["bolge"].format(bolge), genislik_px, oran)


def qr_svg(url, boyut_mm):
    """Sayfa içinde kullanılacak vektör QR (tek path)."""
    q = qrcode.QRCode(border=0, error_correction=qrcode.constants.ERROR_CORRECT_M)
    q.add_data(url); q.make(fit=True)
    m = q.get_matrix(); n = len(m)
    d = "".join(f"M{c} {r}h1v1h-1z" for r, row in enumerate(m) for c, on in enumerate(row) if on)
    return f'<svg class="qr" viewBox="0 0 {n} {n}" style="width:{boyut_mm}mm;height:{boyut_mm}mm" shape-rendering="crispEdges"><path d="{d}" fill="#13233F"/></svg>'


BOLGE_SIMGE = {  # görseli henüz olmayan bölgeler için çizgi simgeler (24×24)
    "compass": '<circle cx="12" cy="12" r="9"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
    "anchor": '<circle cx="12" cy="5" r="2"/><path d="M12 7v14M8 11h8M5 14a7 7 0 0 0 14 0"/>',
    "mountain": '<path d="M2 20l7-12 4 6 3-4 6 10z"/><path d="M7.5 10.5l1.5 1.5 1.5-1.5"/>',
    "tent": '<path d="M3 20l9-15 9 15zM12 20v-6"/>', "house": '<path d="M4 11l8-7 8 7v9H4z"/>',
    "trees": '<path d="M8 3l5 8H3zM8 11v9M16 7l5 8h-10zM16 15v5"/>', "castle": '<path d="M4 21V8h3v3h3V8h4v3h3V8h3v13z"/>',
    "wrench": '<path d="M14 6a4 4 0 0 0 5 5l-9 9-3-3 9-9z"/>',
}
BOLGE_RENK = {"ada": ("#1FA2A8", "#0E5E7A"), "liman": ("#3B6FD6", "#1B2F6B"), "dag": ("#7A5BC7", "#3A2470")}


def bolge_kutusu(k, reg, sinif="harita"):
    """Bölge görseli varsa onu, yoksa bölge adı ve simgesiyle çizilmiş bir şerit döndürür."""
    if (REPO / k["bolge"].format(reg["id"])).exists():
        return f'<img class="{sinif}" src="{bolge_gorseli(k, reg["id"], 1400, 120 / 62)}">'
    a, b = BOLGE_RENK.get(reg["id"], (K["renk"], K["ink"]))
    simge = BOLGE_SIMGE.get(reg.get("icon"), "")
    gunler = reg.get("days") or []
    return (f'<div class="{sinif} yedek" style="background: radial-gradient(70mm 50mm at 80% 20%, rgba(255,255,255,.25), rgba(255,255,255,0) 70%), linear-gradient(135deg, {a}, {b})">'
            f'<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.3" stroke-linejoin="round" stroke-linecap="round">{simge}</svg>'
            f'<div><b>{html.escape(reg["name"])}</b><span>{t("gunler", a=gunler[0], b=gunler[-1])}</span></div></div>')


def gereken_paketler(v):
    kodlar = [e["code"] for e in v["examples"]] + [t["solution"] for t in v["tasks"] + [v.get("visual_task"), v.get("challenge"), v.get("project_task")] if t]
    return sorted({pip for kod_ in kodlar for imp, pip in PAKETLER.items() if re.search(rf"^\s*(import|from)\s+{imp}\b", kod_, re.M)})


def qr_ciz(c, url, x, y, boyut):
    """QR kodu vektör kareler olarak çizer (resim gömmez, PDF küçük kalır)."""
    q = qrcode.QRCode(border=0, error_correction=qrcode.constants.ERROR_CORRECT_M)
    q.add_data(url); q.make(fit=True)
    m = q.get_matrix(); n = len(m); s = boyut / n
    c.setFillColorRGB(0.07, 0.14, 0.25)
    for r, row in enumerate(m):
        for col, on in enumerate(row):
            if on:
                c.rect(x + col * s, y + (n - 1 - r) * s, s * 1.02, s * 1.02, stroke=0, fill=1)


STATIK = {"Nunito": (400, 700, 800), "JetBrainsMono": (400, 600, 700)}


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
    # Chromium değişken (variable) yazı tiplerini PDF'e Type3 olarak gömer ve dosya çok büyür: sabit ağırlıklar üret
    for ad, agirliklar in STATIK.items():
        for w in agirliklar:
            hedef = FONTS / f"{ad}-{w}.ttf"
            if not hedef.exists():
                from fontTools.ttLib import TTFont as FTFont
                from fontTools.varLib.instancer import instantiateVariableFont
                instantiateVariableFont(FTFont(FONTS / f"{ad}.ttf"), {"wght": w}, updateFontNames=False).save(hedef)


# ---------- HTML parçaları ----------
def css(root):
    f = lambda n: (FONTS / n).as_uri()
    return f"""
{"".join(f"@font-face {{ font-family: {aile}; src: url({f(f'{ad}-{w}.ttf')}); font-weight: {w}; }}" for aile, ad in (("Body", "Nunito"), ("Mono", "JetBrainsMono")) for w in STATIK[ad])}
@font-face {{ font-family: Head; src: url({f('Poppins-Bold.ttf')}); font-weight: 700; }}
@font-face {{ font-family: Head; src: url({f('Poppins-SemiBold.ttf')}); font-weight: 600; }}
@font-face {{ font-family: Head; src: url({f('Poppins-ExtraBold.ttf')}); font-weight: 800; }}
@page {{ size: {W_MM}mm {H_MM}mm; margin: 15mm 14mm 22mm 14mm; }}
@page cover {{ margin: 0; }}
:root {{ --c: {K["renk"]}; --c2: {K["renk2"]}; --ink: {K["ink"]}; --ink2: #4A5B7A; --line: #D8E3F3; --soft: #F4F8FF; }}
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
.kod-grup {{ break-inside: avoid; margin: 5pt 0 9pt; }} .kod-grup.bolunebilir {{ break-inside: auto; }}
.code {{ background: var(--soft); border: 0.8pt solid var(--line); border-left: 3pt solid var(--c); border-radius: 5pt; padding: 6pt 8pt; }}
.code .cap {{ font-family: Head; font-weight: 600; font-size: 7.5pt; color: var(--ink2); margin-bottom: 3pt; }}
.code pre, .out pre {{ font-family: Mono; font-size: 8.2pt; line-height: 1.45; white-space: pre-wrap; word-break: break-word; }}
.out {{ border: 0.8pt dashed #9DB4D6; border-top: none; border-radius: 0 0 5pt 5pt; padding: 5pt 8pt 6pt; margin: 0 4pt; background: #fff; }}
.out span, .sahne > span {{ display: block; font-family: Head; font-weight: 600; font-size: 6.5pt; letter-spacing: .08em; text-transform: uppercase; color: var(--ink2); margin-bottom: 2pt; }}
.out.ekran img {{ display: block; width: 100%; border: 0.6pt solid var(--line); border-radius: 4pt; }}
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
.gorev {{ border: 1pt solid var(--line); border-radius: 8pt; padding: 9pt 10pt 4pt; margin: 9pt 0; break-inside: avoid; }}
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
.acilis {{ break-after: page; position: relative; }}
.acilis .ust {{ display: flex; align-items: center; gap: 8pt; }}
.acilis .gun {{ font-family: Head; font-weight: 800; font-size: 11pt; background: var(--c2); padding: 2pt 10pt; border-radius: 99pt; }}
.acilis .bolge {{ font-family: Head; font-weight: 600; font-size: 9pt; color: var(--ink2); }}
.acilis h1 {{ font-size: 24pt; margin: 6pt 0 7pt; font-weight: 800; }}
.acilis .uzay {{ width: 100%; height: 56mm; border-radius: 9pt; background-size: cover; background-position: center; display: grid; place-items: center; }}
.acilis .uzay img {{ height: 54mm; filter: drop-shadow(0 3mm 4mm rgba(0,0,0,.5)); }}
.kapak.uzayli {{ background: linear-gradient(rgba(11,16,38,.35), rgba(11,16,38,.55)), var(--kapak-bg) center / cover, #0B1026; }}
.kapak.uzayli .bolgeler img {{ border: none; object-fit: contain; width: 18mm; height: 18mm; }}
.acilis .harita {{ width: 100%; height: 50mm; object-fit: cover; border-radius: 9pt; display: block; }}
.harita.yedek {{ display: flex; align-items: center; gap: 8mm; padding: 0 12mm; color: #fff; }}
.harita.yedek svg {{ width: 30mm; height: 30mm; flex: none; opacity: .9; }}
.harita.yedek b {{ display: block; font-family: Head; font-weight: 800; font-size: 22pt; line-height: 1.1; }}
.harita.yedek span {{ font-family: Head; font-weight: 600; font-size: 10pt; opacity: .85; }}
.acilis .baglanti {{ display: flex; gap: 6pt; margin-top: 7pt; break-inside: avoid; }}
.acilis .baglanti > div {{ flex: 1; display: flex; gap: 6pt; align-items: center; border: 1pt solid var(--line); border-radius: 8pt; padding: 5pt 7pt; font-size: 7.6pt; line-height: 1.35; }}
.acilis .baglanti > div.video {{ background: #FFF1F0; border-color: #F6C9C4; }}
.acilis .baglanti b {{ display: block; font-family: Head; font-size: 8pt; }}
.acilis .baglanti .qr {{ flex: none; }}
.acilis .paket {{ font-size: 8pt; background: #FFF7DD; border-radius: 5pt; padding: 3pt 7pt; margin-top: 5pt; }}
.icindekiler.tam li {{ padding: 2.2pt 0; font-size: 9pt; }}
.icindekiler li.bolum {{ break-after: avoid; border: none; padding: 7pt 0 1pt; font-family: Head; font-weight: 700; font-size: 8pt; letter-spacing: .06em; text-transform: uppercase; color: var(--ink2); }}
.on .kanal {{ display: flex; gap: 8pt; align-items: center; background: #FFF1F0; border: 1pt solid #F6C9C4; border-radius: 8pt; padding: 7pt 9pt; margin: 6pt 0 8pt; }}
.on .kanal .qr {{ flex: none; }}
/* sertifika */
.sertifika {{ page: cover; width: {W_MM}mm; height: {H_MM}mm; position: relative; overflow: hidden; text-align: center;
  background: radial-gradient(90mm 70mm at 50% 0%, #FFF3C4, rgba(255,243,196,0) 70%), #fff; }}
.sertifika .cerceve {{ position: absolute; inset: 9mm; border: 1.6mm solid var(--c); border-radius: 6mm; box-shadow: inset 0 0 0 1.4mm #fff, inset 0 0 0 2mm var(--c2); }}
.sertifika .ic {{ position: absolute; inset: 22mm 18mm; display: flex; flex-direction: column; align-items: center; }}
.sertifika .ust {{ font-family: Head; font-weight: 700; font-size: 9pt; letter-spacing: .2em; text-transform: uppercase; color: var(--ink2); }}
.sertifika h1 {{ font-size: 26pt; font-weight: 800; color: var(--c); margin: 4mm 0 2mm; }}
.sertifika img {{ width: 48mm; margin: 4mm 0; }}
.sertifika .ad {{ width: 95mm; border-bottom: 0.5mm solid var(--ink); height: 12mm; margin: 4mm 0 1.5mm; }}
.sertifika small {{ font-size: 7.5pt; color: var(--ink2); }}
.sertifika p {{ font-size: 10pt; max-width: 100mm; margin: 5mm 0 0; }}
.sertifika .imza {{ display: flex; gap: 14mm; margin-top: auto; }}
.sertifika .imza div {{ width: 40mm; border-top: 0.4mm solid var(--ink); padding-top: 1.5mm; font-size: 7.5pt; color: var(--ink2); }}
.acilis .konusma {{ display: flex; gap: 8pt; align-items: flex-end; margin-top: 7pt; }}
.acilis .konusma img {{ width: 26mm; flex: none; }}
.acilis .balon {{ position: relative; background: var(--soft); border: 1pt solid var(--line); border-radius: 10pt; padding: 7pt 9pt; font-size: 8.8pt; }}
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
.kapak .video {{ position: absolute; left: 13mm; top: 98mm; display: flex; align-items: center; gap: 2.4mm; background: #fff; color: var(--ink);
  padding: 1.6mm 4mm 1.6mm 1.8mm; border-radius: 99pt; box-shadow: 0 1.2mm 3mm rgba(0,0,0,.25); transform: rotate(-2deg); }}
.kapak .video i {{ flex: none; width: 7.5mm; height: 7.5mm; border-radius: 50%; background: #E5322D; display: grid; place-items: center; }}
.kapak .video i svg {{ width: 3.4mm; height: 3.4mm; margin-left: 0.5mm; }}
.kapak .video b {{ display: block; font-family: Head; font-weight: 800; font-size: 9.5pt; line-height: 1.1; }}
.kapak .video small {{ display: block; font-size: 6.8pt; color: var(--ink2); line-height: 1.2; }}
.kapak .bolgeler {{ position: absolute; left: 14mm; top: 115mm; display: flex; gap: 3mm; }}
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
.cozum {{ margin: 8pt 0 12pt; break-inside: avoid; }} .cozum h3 {{ break-after: avoid; }} .aciklama tr {{ break-inside: avoid; }}
.cozum h3 {{ font-size: 10pt; }} .cozum h3 small {{ font-family: Body; font-weight: 700; color: var(--c); margin-right: 4pt; }}
.aciklama {{ font-size: 8.3pt; margin: 4pt 0 0; border-collapse: collapse; width: 100%; }}
.aciklama td {{ padding: 2pt 4pt; vertical-align: top; border-top: 0.5pt solid var(--line); }}
.aciklama td:first-child {{ font-family: Mono; color: var(--ink2); width: 12pt; }}
.aciklama td:nth-child(2) {{ font-family: Mono; white-space: pre-wrap; width: 42%; }}
"""


def page(body, root):
    return f'<!doctype html><html lang="{DIL}"><head><meta charset="utf-8"><style>{css(root)}</style></head><body>{body}</body></html>'


def gorev_html(gv, etiket, cls, ref, root):
    out = f'<div class="gorev {cls}"><div class="bas"><span class="etiket">{etiket}</span><h3>{html.escape(gv["title"])}</h3>{md(gv["prompt"])}</div>'
    sc = (gv.get("scene") or {}).get("target")
    if sc:
        out += sahne(sc, root)
    if (gv.get("html") or "").strip():
        out += kod(gv["html"], baslik=t("html_hazir"), lex=HtmlLexer())
    if (gv.get("starter") or "").strip():
        out += kod(gv["starter"], baslik=t("baslangic"))
    ch = gv.get("check") or {}
    kontrol = []
    if ch.get("output_contains"):
        kontrol.append(t("cikti_olmali") + ", ".join(f"<code>{html.escape(x)}</code>" for x in ch["output_contains"]))
    if ch.get("code_contains"):
        kontrol.append(t("kod_gecmeli") + ", ".join(f"<code>{html.escape(x)}</code>" for x in ch["code_contains"]))
    if kontrol:
        out += f'<div class="kontrol"><b>{t("kontrol")}</b> ' + "; ".join(kontrol) + "</div>"
    if gv.get("hints"):
        out += f'<div class="ipucu"><b>{t("ipuclari")}</b><ol>' + "".join(f"<li>{md_inline(h)}</li>" for h in gv["hints"]) + "</ol></div>"
    out += f'<div class="cozum-ref">{t("cozum_ref", ref=ref)}</div></div>'
    return out


def sozluk_terimleri(v):
    """Günün sözlüğü: Türkçe veride hazır; İngilizce baskıda aynı terimler sozluk.json'dan çevrilir."""
    kaynak = v.get("_tr", v)
    terms = {}
    for gv in kaynak["tasks"] + [kaynak.get("challenge") or {}, kaynak.get("visual_task") or {}, kaynak.get("project_task") or {}]:
        for x in ((gv or {}).get("explain") or {}).get("terms", []):
            if x.get("kind") != "değişken":  # değişken adları sözlüğü şişirir
                terms.setdefault(x["term"], x)
    if DIL == "en":
        en = json.loads((veri_dizini(K["kod"]) / "sozluk.json").read_text("utf8"))
        terms = {k_: {"term": k_, "kind": en[k_][0], "desc": en[k_][1]} for k_ in terms if k_ in en}
    return terms


def gun_html(v, k, root):
    n = int(v["day"])
    reg = next(r for r in kurs_json(k)["regions"] if r["id"] == v["region"])
    poz = k["acilis_poz"][0 if n % 2 else 1]
    if k["bolge_tur"] == "gezegen":
        gorsel = f'<div class="uzay" style="background-image:url({jpg(k["uzay"], 1400, 120 / 62)})"><img src="{bolge_gorseli(k, v["region"], 700)}"></div>'
    else:
        gorsel = bolge_kutusu(k, reg)
    site = f'<div>{qr_svg(k["url"], 15)}<span>{t("site_kutu", kurs=k["dil_adi"], n=n)}</span></div>' if DIL == "tr" else ""
    baglanti = f"""<div class="baglanti">
  <div class="video">{qr_svg(VIDEO, 15)}<span>{t("video_kutu", n=n, title=html.escape(v["title"]))}</span></div>
  {site}
 </div>"""
    paket = gereken_paketler(v)
    paket = f'<div class="paket">{t("paket", p=" ".join(paket))}</div>' if paket else ""
    rol = uyarla(v.get("game_role", "")) if DIL == "tr" else v.get("game_role", "")
    body = f"""<section class="acilis">
 <div class="ust"><span class="gun">{t("gun", n=n)}</span><span class="bolge">{html.escape(reg["name"])}</span></div>
 <h1>{html.escape(v["title"])}</h1>
 {gorsel}
 <div class="box hedef"><h4>{t("hedef")}</h4>{md_inline(v["objective"])}</div>
 <div class="konusma"><img src="{root}/{k["poz"].format(poz)}"><div class="balon">{md_inline(v["story"])}</div></div>
 <div class="proje">{t("proje_katki")} ({html.escape(k["varsayilan_proje"])}): <b>{html.escape(v.get("project_contribution", ""))}</b>. {html.escape(rol)}</div>
 {paket}
 {baglanti}
</section>"""
    body += f"<h2>{t('konu')}</h2>"
    for sec in v["sections"]:
        baslik = uyarla(sec["title"]) if DIL == "tr" else sec["title"]
        body += f"<h3>{html.escape(baslik)}</h3>{md(sec['body'])}"
    body += f"<h2>{t('ornekler')}</h2>"
    for e in v["examples"]:
        sc = (e.get("scene") or {}).get("target") if isinstance(e.get("scene"), dict) else None
        if not sc and e.get("scene"):
            o, _ = calistir(e["code"], e.get("inputs"))
            sc = o.split("\n") if o else None
        body += f"<h3>{html.escape(e['title'])}</h3>" + kod_ve_sonuc(e["code"], e.get("inputs"), e if e.get("mode") == "page" or e.get("html") else {}, sahne(sc, root) if sc else None)
        if e.get("note"):
            body += f'<p class="note">{md_inline(e["note"])}</p>'
    terms = sozluk_terimleri(v)
    if terms:
        body += f'<div class="box sozluk"><h4>{t("sozluk")}</h4><dl>' + "".join(
            f'<dt>{html.escape(x["term"])}</dt><dd>{md_inline(x["desc"])} <em>{html.escape(x.get("kind", ""))}</em></dd>' for x in terms.values()) + "</dl></div>"
    body += f"<h2>{t('gorevler')}</h2>"
    for i, gv in enumerate(v["tasks"], 1):
        body += gorev_html(gv, t("gorev", i=i), "", f"{n}.{i}", root)
    j = len(v["tasks"])
    if v.get("visual_task"):
        j += 1; body += gorev_html(v["visual_task"], t("sahne_g"), "sahne-g", f"{n}.{j}", root)
    if v.get("challenge"):
        j += 1; body += gorev_html(v["challenge"], t("challenge"), "challenge", f"{n}.{j}", root)
    if v.get("project_task"):
        j += 1; body += gorev_html(v["project_task"], f"{t('proje')}: {k['varsayilan_proje']}", "proje", f"{n}.{j}", root)
    return body


def cozumler_html(gunler):
    if DIL == "en":
        from aciklama_en import explain
    aciklamali = DIL == "en" or any((gv or {}).get("explain") for v in gunler for gv in v["tasks"])
    body = f'<section class="on"><h1>{t("cozumler")}</h1><p>{t("cozum_giris")}'
    body += t("cozum_satir") if aciklamali else t("cozum_cikti")
    body += t("cozum_farkli") + "</p>"
    for v in gunler:
        n = int(v["day"])
        body += f'<h2>{t("gun", n=n)}: {html.escape(v["title"])}</h2>'
        items = [(t("gorev", i=i), gv) for i, gv in enumerate(v["tasks"], 1)]
        if v.get("visual_task"): items.append((t("sahne_g"), v["visual_task"]))
        if v.get("challenge"): items.append((t("challenge"), v["challenge"]))
        if v.get("project_task"): items.append((t("proje"), v["project_task"]))
        gorulen = set()
        varsayilan = ["Emma", "12", "Piko", "5"] if DIL == "en" else ["Ece", "12", "Piko", "5"]
        for j, (etiket, gv) in enumerate(items, 1):
            girdi = gv.get("inputs") or varsayilan if "input(" in gv["solution"] else None
            satirlar = explain(gv["solution"]) if DIL == "en" else (gv.get("explain") or {}).get("lines", [])
            rows = ""
            for x in satirlar:
                notes = [nn for nn in x.get("notes", []) if nn not in gorulen]  # aynı açıklama gün içinde bir kez
                gorulen.update(notes)
                if notes:
                    rows += f'<tr><td>{x["n"]}</td><td>{html.escape(x["code"])}</td><td>{" ".join(md_inline(nn) for nn in notes)}</td></tr>'
            body += f'<div class="cozum"><h3><small>{n}.{j}</small>{etiket}: {html.escape(gv["title"])}</h3>' + kod_ve_sonuc(gv["solution"], girdi, gv)
            if rows:
                body += f'<table class="aciklama">{rows}</table>'
            body += "</div>"
    return body + "</section>"


NASIL = {
    "tr": """<h1>Bu kitap nasıl kullanılır?</h1>
<p>Selam! Ben <b>{m}</b>. Bu kitapta her gün yeni bir şey öğrenip hemen kendi kodunu yazacaksın. Her gün aynı sırayla ilerler:</p>
<ol class="adimlar">
 <li><b>Konu anlatımı:</b> Günün fikirleri, kısa ve örnekli.</li>
 <li><b>Örnekler:</b> Kodu yaz, çalıştır, çıktıyı kitaptakiyle karşılaştır.</li>
 <li><b>Görevler:</b> Önce kendin dene. "Kendini kontrol et" kutusu ne yazman gerektiğini söyler; ipuçları da hazır.</li>
 <li><b>{sahne}Challenge ve Proje:</b> Biraz daha zor ama çok eğlenceli. Proje adımlarıyla 30 günün sonunda kendi oyununu bitireceksin.</li>
 <li><b>Çözümler:</b> Kitabın sonunda, {cozum}.</li>
</ol>
<h2>Kodu nerede yazacağım?</h2>
<p>{kurulum} Kitabı kullanmak için internete ihtiyacın yok.</p>
<h2>Video anlatımlar</h2>
<div class="kanal">{qr}<div>Her günün konusunu kısa bir videoda {m} anlatıyor. Sayfaların altındaki QR kod seni YouTube'daki <b>30 Günde Kod</b> kanalına götürür; o günün <b>„Gün N”</b> videosunu aç. Kanalda hem 30 Günde Python hem 30 Günde JavaScript videoları var.<br><b>youtube.com/@30gundekod</b></div></div>
<p>Her günün ilk sayfasında ayrıca o günün <b>etkileşimli dersinin</b> adresi var (30gunde.com.tr). Orada kodunu tarayıcıda yazar, tek tıkla kontrol ettirir, rozet toplarsın. Videolar da site de isteğe bağlı; kitap tek başına yeterli.</p>""",
    "en": """<h1>How to use this book</h1>
<p>Hi! I'm <b>{m}</b>. In this book you'll learn something new every day and write your own code right away. Every day follows the same steps:</p>
<ol class="adimlar">
 <li><b>The lesson:</b> the ideas of the day, short and with examples.</li>
 <li><b>Examples:</b> type the code, run it, and compare the output with the book.</li>
 <li><b>Tasks:</b> try them yourself first. The "Check yourself" box tells you what to look for, and hints are ready too.</li>
 <li><b>{sahne}Challenge and Project:</b> a bit harder but lots of fun. With the project steps you'll finish your own game at the end of the 30 days.</li>
 <li><b>Solutions:</b> at the back of the book, {cozum}.</li>
</ol>
<h2>Where do I write the code?</h2>
<p>{kurulum} You don't need the internet to use this book.</p>
<h2>Video lessons</h2>
<div class="kanal">{qr}<div>{m} explains the topic of every day in a short video. The QR code at the bottom of each page takes you to the <b>30 Günde Kod</b> channel on YouTube; open that day's <b>“Day N”</b> video.<br><b>youtube.com/@30gundekod</b></div></div>
<p>The videos are optional; the book works on its own.</p>""",
}


def on_bolum_html(k, gunler, sayfalar, root, tam=False):
    """(nasıl kullanılır, içindekiler): ayrı parçalar olarak basılır."""
    n0, n1 = int(gunler[0]["day"]), int(gunler[-1]["day"])
    satir = lambda v: f'<li><b>{t("gun", n=int(v["day"]))}</b>{html.escape(v["title"])}<span class="s">{sayfalar.get(int(v["day"]), "")}</span></li>'
    if tam:  # bölgelere göre gruplanmış
        toc = ""
        for r in kurs_json(k)["regions"]:
            vs = [v for v in gunler if v["region"] == r["id"]]
            if vs:
                toc += f'<li class="bolum">{html.escape(r["name"])}</li>' + "".join(satir(v) for v in vs)
    else:
        toc = "".join(satir(v) for v in gunler)
    toc += f'<li class="bolum">{t("ekler")}</li>' if tam else ""
    toc += f'<li><b>{t("ek")}</b>{t("cozumler")}<span class="s">{sayfalar.get("cozum", "")}</span></li>'
    if k["kod"] == "javascript" and DIL == "tr":
        toc += f'<li><b>{t("ek")}</b>Deneme API\'si<span class="s">{sayfalar.get("demoapi", "")}</span></li>'
    if tam:
        toc += f'<li><b>{t("son")}</b>{t("sertifikan")}<span class="s">{sayfalar.get("sertifika", "")}</span></li>'
    ornek = "" if tam else f'<p style="font-size:8.5pt;color:#4A5B7A;margin-top:14pt">{t("ornek_bolum", ad=k["ad"], a=n0, b=n1)}</p>'
    py = k["kod"] == "python"
    nasil = NASIL[DIL].format(
        m=k["maskot"], kurulum=k["kurulum"], qr=qr_svg(VIDEO, 20),
        sahne=("Sahne görevi, " if DIL == "tr" else "Stage task, ") if py else "",
        cozum=("satır satır açıklamalarıyla" if DIL == "tr" else "with line-by-line explanations") if py else
              ("çıktılarıyla birlikte" if DIL == "tr" else "together with their output"))
    return f"""<section class="on">
{nasil}
</section>""", f"""<section class="on"><h1>{t("icindekiler")}</h1><ul class="icindekiler{" tam" if tam else ""}">{toc}</ul>
{ornek}
<p style="font-size:7.5pt;color:#4A5B7A;margin-top:{6 if tam else 30}pt">{t("telif")}</p>
</section>"""


def demo_api_html():
    return (f'<section class="on"><h1>Deneme API\'si</h1><p>26. günden itibaren örneklerde kullanılan <code>/demo-api/...</code> adresleri '
            "bu kurs için hazırlanmış bir deneme sunucusudur. Etkileşimli derslerde hazırdır. Kendi bilgisayarında denerken aşağıdaki kodu "
            "betiğinin <b>en üstüne</b> yapıştır: <code>fetch</code> istekleri internete çıkmadan bu verilerle cevaplanır.</p>"
            + kod((HERE / "demo_api.js").read_text("utf8"), baslik="demo-api.js").replace('class="kod-grup"', 'class="kod-grup bolunebilir"')
            + "</section>")


def kapak_html(k, gunler, root, tam=False):
    n0, n1 = int(gunler[0]["day"]), int(gunler[-1]["day"])
    gorev = sum(len(v["tasks"]) + sum(bool(v.get(x)) for x in ("visual_task", "challenge", "project_task")) for v in gunler)
    bolgeler = "".join(f'<img src="{bolge_gorseli(k, r["id"], 320)}">' for r in kurs_json(k)["regions"][:3] if (REPO / k["bolge"].format(r["id"])).exists())
    uzay = f' uzayli" style="--kapak-bg: url({jpg("gorseller/javascript/arka-plan/bg-space.webp", 1000)})' if k["bolge_tur"] == "gezegen" else ""
    oynat = '<svg viewBox="0 0 10 10"><path d="M2 1l7 4-7 4z" fill="#fff"/></svg>'
    return f"""<section class="kapak{uzay}"><img class="logo" src="{root}/{k["logo"]}"><div class="marka">30gunde.com.tr</div>
<h1>{t("kapak_baslik", dil=k["dil_adi"])}</h1>
<div class="alt">{k["alt"]}</div>
<div class="video"><i>{oynat}</i><div><b>{t("video_rozet")}</b><small>{t("video_rozet_alt")}</small></div></div>
<div class="bolgeler">{bolgeler}</div>
<div class="etiket">{t("kapak_tam", g=gorev) if tam else t("kapak_ornek", a=n0, b=n1)}</div>
<img class="piko" src="{png(k["kapak_poz"], 900)}">
<div class="serit"><span>{t("yas")}</span><span>{t("serit")}</span></div></section>"""


def sertifika_html(k, root):
    return f"""<section class="sertifika"><div class="cerceve"></div><div class="ic">
<div class="ust">{t("srt_ust")}</div>
<h1>{t("srt_baslik")}</h1>
<img src="{png(k["kapak_poz"], 600)}">
<div class="ad"></div><small>{t("srt_ad")}</small>
<p>{t("srt_metin", ad=k["ad"], dil=k["dil_adi"])}</p>
<div class="imza"><div>{t("srt_tarih")}</div><div>{t("srt_maskot", m=k["maskot"])}</div></div>
</div></section>"""


# ---------- PDF ----------
# Gün açılışı tek sayfaya sığmazsa bölge görselini sığana kadar alçalt (baskı düzeninde ölçülür)
ACILIS_SIGDIR = """() => {
  const mm = 96 / 25.4, a = document.querySelector('.acilis'); if (!a) return;
  const g = a.querySelector('.harita, .uzay'); if (!g) return;
  for (let h = 50; a.offsetHeight > 172 * mm && h > 28; h -= 2) g.style.height = h + 'mm';
}"""


def pdf_bas(parcalar, out_dir):
    """Her HTML parçasını ayrı PDF'e basar; sayfa sayılarını döndürür."""
    from playwright.sync_api import sync_playwright
    paths = []
    with sync_playwright() as p:
        b = p.chromium.launch(args=["--allow-file-access-from-files"])
        pg = b.new_page(viewport={"width": round((W_MM - 28) / 25.4 * 96), "height": 800})
        pg.emulate_media(media="print")
        for ad, html_ in parcalar:
            f = out_dir / f"{ad}.html"; f.write_text(html_, "utf8")
            pg.goto(f.as_uri()); pg.evaluate("document.fonts.ready")
            pg.wait_for_load_state("networkidle")
            pg.evaluate(ACILIS_SIGDIR)
            pdf = out_dir / f"{ad}.pdf"
            pg.pdf(path=str(pdf), width=f"{W_MM}mm", height=f"{H_MM}mm", print_background=True, prefer_css_page_size=True)
            paths.append((ad, pdf, len(PdfReader(str(pdf)).pages)))
        b.close()
    return paths


def altbilgi(writer, sayfa_bilgisi, k):
    """Her sayfanın altına sayfa numarası, gün adı ve video kanalının QR kodunu basar."""
    pdfmetrics.registerFont(TTFont("Head", str(FONTS / "Poppins-SemiBold.ttf")))
    pdfmetrics.registerFont(TTFont("Body", str(FONTS / "Poppins-Regular.ttf")))
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=(W_MM * mm, H_MM * mm))  # tek belge: yazı tipi bir kez gömülür
    for i, (etiket, gun) in enumerate(sayfa_bilgisi):
        if etiket is None:
            c.showPage()
            continue
        no = i + 1
        sol = no % 2 == 0  # çift sayfalar solda: numara dış kenarda
        c.setFillColorRGB(0.07, 0.14, 0.25); c.setFont("Head", 8)
        c.drawString(14 * mm, 9 * mm, str(no)) if sol else c.drawRightString((W_MM - 14) * mm, 9 * mm, str(no))
        q = 13 * mm
        qx = (W_MM - 14) * mm - q if sol else 14 * mm
        qr_ciz(c, VIDEO, qx, 4.5 * mm, q)
        tx = qx - 2 * mm if sol else qx + q + 2 * mm
        yaz = c.drawRightString if sol else c.drawString
        c.setFont("Head", 6.5); c.setFillColorRGB(0.75, 0.16, 0.12)
        yaz(tx, 12.2 * mm, t("alt_video_gun", d=gun) if gun else t("alt_video"))
        c.setFont("Body", 6.5); c.setFillColorRGB(0.29, 0.36, 0.48)
        yaz(tx, 8.6 * mm, f"{k['ad']} · {etiket}")
        yaz(tx, 5.4 * mm, VIDEO.replace("https://www.", ""))
        c.showPage()
    c.save()
    alt = PdfReader(buf)
    for i, (etiket, _) in enumerate(sayfa_bilgisi):
        if etiket is not None:
            writer.pages[i].merge_page(alt.pages[i])
            writer.pages[i].compress_content_streams()  # birleştirme içeriği sıkıştırmasız bırakır


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kurs", choices=list(KURS))
    ap.add_argument("gunler", help="ör. 1-3")
    ap.add_argument("--dil", choices=["tr", "en"], default="tr")
    a = ap.parse_args()
    global K, DIL
    DIL = a.dil
    k = K = dict(KURS[a.kurs], **(KURS_EN.get(a.kurs, {}) if DIL == "en" else {}))
    if DIL == "en" and a.kurs not in KURS_EN:
        sys.exit(f"{a.kurs} için İngilizce içerik yok")
    fontlari_hazirla()
    g0, g1 = map(int, a.gunler.split("-"))
    vd = veri_dizini(a.kurs)
    tam = g0 == 1 and not (vd / f"gun-{g1 + 1:02d}.json").exists()
    gunler = [json.loads((vd / f"gun-{d:02d}.json").read_text("utf8")) for d in range(g0, g1 + 1)]
    if DIL == "en":  # sözlük terimleri Türkçe veriden gelir
        for v in gunler:
            v["_tr"] = json.loads((REPO / a.kurs / "veri" / f"gun-{int(v['day']):02d}.json").read_text("utf8"))
    work = HERE / "is" / DIL; work.mkdir(parents=True, exist_ok=True)
    root = REPO.as_uri()
    gun_parca = [(f"gun-{int(v['day']):02d}", page(gun_html(v, k, root), root)) for v in gunler]
    coz = ("cozumler", page(cozumler_html(gunler), root))
    kapak = ("kapak", page(kapak_html(k, gunler, root, tam), root))
    son = [("demoapi", page(demo_api_html(), root))] if k["kod"] == "javascript" and DIL == "tr" else []
    son += [("sertifika", page(sertifika_html(k, root), root))] if tam else []
    # ön bölümün uzunluğu sayfa numaralarına bağlı değil: önce boş numaralarla bas, sonra gerçekleriyle
    nasil, toc = on_bolum_html(k, gunler, {}, root, tam)
    ekran_kapat()
    bilgi = pdf_bas([kapak, ("on", page(nasil, root)), ("icindekiler", page(toc, root))] + gun_parca + [coz] + son, work)
    sayfa = 1; baslangic = {}
    for ad, _, n in bilgi:
        baslangic[ad] = sayfa; sayfa += n
    nums = {int(v["day"]): baslangic[f"gun-{int(v['day']):02d}"] for v in gunler}
    nums["cozum"] = baslangic["cozumler"]
    nums["sertifika"] = baslangic.get("sertifika", "")
    nums["demoapi"] = baslangic.get("demoapi", "")
    bilgi[2] = pdf_bas([("icindekiler", page(on_bolum_html(k, gunler, nums, root, tam)[1], root))], work)[0]
    writer = PdfWriter(); sayfa_bilgisi = []
    for ad, pdf, n in bilgi:
        for p_ in PdfReader(str(pdf)).pages:
            writer.add_page(p_)
        if ad in ("kapak", "sertifika"):
            sayfa_bilgisi += [(None, None)] * n
        elif ad.startswith("gun-"):
            d = int(ad[4:]); v = next(x for x in gunler if int(x["day"]) == d)
            sayfa_bilgisi += [(f"{t('gun', n=d)}: {v['title']}", d)] * n
        else:
            sayfa_bilgisi += [({"cozumler": t("cozumler"), "demoapi": "Deneme API'si"}.get(ad, t("giris")), None)] * n
    altbilgi(writer, sayfa_bilgisi, k)
    for _ in range(3):  # parçalar arasında ortak görseller bir kez (maskeler birleşince görseller de eşleşir)
        writer.compress_identical_objects(remove_duplicates=True, remove_unreferenced=True)
    ornek = "(örnek)" if DIL == "tr" else "(sample)"
    writer.add_metadata({"/Title": k["ad"] if tam else f"{k['ad']} · {t('gunler', a=g0, b=g1)} {ornek}", "/Author": "30 Günde", "/Subject": "30gunde.com.tr"})
    if DIL == "en":
        ad = f"30-days-of-{a.kurs}" + ("" if tam else f"-days-{g0:02d}-{g1:02d}")
    else:
        ad = f"30-gunde-{a.kurs}" + ("" if tam else f"-gun-{g0:02d}-{g1:02d}")
    out = REPO / "cikti" / "kitap" / f"{ad}.pdf"
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "wb") as f:
        writer.write(f)
    print(f"hazır: {out} ({len(writer.pages)} sayfa)")


if __name__ == "__main__":
    main()
