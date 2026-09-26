# Gün 26: Python ile web

**Kurs:** 30 Günde Python  ·  **Bölge:** Python Dağı  ·  **Maskot:** Piko

**Bugünün hedefi:** Web'in istek ve yanıtla nasıl çalıştığını anlamak, Python ile HTML sayfaları üretmek ve yönlendirme yapmak

> Python Dağı'nın eteğindeyiz! Tepede dev bir gözlem kulesi var ve dünyanın her yerinden mesajlar alıyor. Her mesaj bir istek, kulenin verdiği her cevap bir yanıt. İnternetteki web siteleri de tam böyle çalışır. Bugün Python ile kendi web sayfalarımızı üretiyoruz.

![Python Dağı](../../gorseller/python/harita/dag.webp)

## Konu anlatımı

### İstek ve yanıt

Tarayıcına bir adres yazdığında olanlar:

- Tarayıcı sunucuya bir **istek** gönderir: "Bana `/profil` sayfasını ver."
- Sunucu isteği okur, sayfayı hazırlar ve bir **yanıt** döner.
- Yanıtın içinde HTML ve bir **durum kodu** vardır.

En bilinen durum kodları: `200` her şey yolunda, `404` sayfa bulunamadı, `500` sunucuda hata oldu.

### Flask ile bir site

Python'da web sitesi yapmanın en sevilen yollarından biri **Flask** paketidir. Kendi bilgisayarında şöyle görünür:

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Piko'nun sitesine hoş geldin!</h1>"

app.run()
```

`@app.route("/")` şunu der: "Biri `/` adresini isterse `home` fonksiyonunu çalıştır." Bu sitede bir sunucu başlatamıyoruz, ama aynı fikri düz Python ile deneyeceğiz.

### HTML'i Python ile üretmek

Bir web sunucusunun asıl işi, veriden HTML yazısı üretmektir. f-string ve `join` bunun için yeterli:

```python
name = "Piko"
page = f"<h1>Merhaba {name}</h1>"

items = ["kılıç", "iksir"]
html = "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
```

### Yönlendirme (routing)

Hangi adresin hangi fonksiyona gideceğini bir sözlükle tutabiliriz:

```python
def home():
    return "Ana sayfa"

def about():
    return "Hakkında"

routes = {"/": home, "/hakkinda": about}
print(routes["/hakkinda"]())   # Hakkında
```

Sözlükte olmayan bir adres gelirse `404` sayfasını göstermek gerekir. Flask bunu senin için yapar.

## Örnekler

### Sayfa üret

```python
name = "Piko"
items = ["kılıç", "iksir", "harita"]

page = f"<h1>{name}'nun çantası</h1>"
page += "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
print(page)
```

### Durum kodları

```python
codes = {200: "Tamam", 404: "Bulunamadı", 500: "Sunucu hatası"}
for code in [200, 404, 500, 418]:
    print(code, codes.get(code, "Bilinmiyor"))
```

### Mini yönlendirme

```python
def home():
    return "<h1>Ana sayfa</h1>"

def about():
    return "<h1>Hakkında</h1>"

routes = {"/": home, "/hakkinda": about}

for path in ["/", "/hakkinda", "/gizli"]:
    view = routes.get(path)
    print(path, "->", view() if view else "404 Bulunamadı")
```

## Görevler

### Görev 1: Karşılama sayfası

`page` değişkeni `<h1>Merhaba Piko</h1>` gibi bir HTML başlığı olsun. İsim `name` değişkeninden gelsin.

**Başlangıç kodu:**

```python
name = "Piko"

page = ""

print(page)
```

**İpuçları:**

1. f"<h1>Merhaba {name}</h1>"

<details><summary>Çözüm</summary>

```python
name = "Piko"

page = f"<h1>Merhaba {name}</h1>"

print(page)
```

</details>

### Görev 2: Liste sayfası

`items` listesinden bir HTML listesi üret: `<ul><li>kılıç</li><li>iksir</li></ul>` (boşluk ve satır sonu olmadan).

**Başlangıç kodu:**

```python
items = ["kılıç", "iksir"]

html = ""

print(html)
```

**İpuçları:**

1. Her eşya için f"<li>{i}</li>" üret.
2. Hepsini "".join(...) ile birleştir ve <ul> ile sar.

<details><summary>Çözüm</summary>

```python
items = ["kılıç", "iksir"]

html = "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"

print(html)
```

</details>

### Görev 3: Durum kodu

`status_text(code)` fonksiyonu 200 için `Tamam`, 404 için `Bulunamadı`, 500 için `Sunucu hatası`, diğerleri için `Bilinmiyor` döndürsün.

**Başlangıç kodu:**

```python
def status_text(code):
    return ""

print(status_text(404))
```

**İpuçları:**

1. Bir sözlük ve get() kullanabilirsin.
2. texts.get(code, "Bilinmiyor")

<details><summary>Çözüm</summary>

```python
def status_text(code):
    texts = {200: "Tamam", 404: "Bulunamadı", 500: "Sunucu hatası"}
    return texts.get(code, "Bilinmiyor")

print(status_text(404))
```

</details>

## Challenge: Mini sunucu

`handle(path)` fonksiyonu `(durum_kodu, html)` tuple'ı döndürsün. Adres `routes` içindeyse `(200, sayfa)`, değilse `(404, "<h1>Bulunamadı</h1>")`.

**Başlangıç kodu:**

```python
def home():
    return "<h1>Ana sayfa</h1>"

def about():
    return "<h1>Hakkında</h1>"

routes = {"/": home, "/hakkinda": about}

def handle(path):
    pass

print(handle("/"))
print(handle("/gizli"))
```

**İpuçları:**

1. if path in routes: ile kontrol et.
2. Fonksiyonu çağırmayı unutma: routes[path]()

<details><summary>Çözüm</summary>

```python
def home():
    return "<h1>Ana sayfa</h1>"

def about():
    return "<h1>Hakkında</h1>"

routes = {"/": home, "/hakkinda": about}

def handle(path):
    if path in routes:
        return (200, routes[path]())
    return (404, "<h1>Bulunamadı</h1>")

print(handle("/"))
print(handle("/gizli"))
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Oyunun web sayfası**

### Piko'nun Macerası: Oyunun web sayfası

Piko'nun Macerası'nın oyuncu profili sayfasını üretelim. `render_profile(hero)` bir HTML yazısı döndürsün ve içinde şunlar olsun:

- `<h1>Piko</h1>` (kahramanın adı)
- `<p>Can: 80</p>`
- `<p>Altın: 35</p>`

**Başlangıç kodu:**

```python
def render_profile(hero):
    return ""

print(render_profile({"name": "Piko", "hp": 80, "gold": 35}))
```

**İpuçları:**

1. f-string içinde sözlükten değer alırken farklı tırnak kullan: {hero['name']}
2. Üç parçayı += ile birleştir ve return et.

<details><summary>Çözüm</summary>

```python
def render_profile(hero):
    html = f"<h1>{hero['name']}</h1>"
    html += f"<p>Can: {hero['hp']}</p>"
    html += f"<p>Altın: {hero['gold']}</p>"
    return html

print(render_profile({"name": "Piko", "hp": 80, "gold": 35}))
```

</details>

### Harcama Defteri: HTML rapor sayfası

Raporu bir web sayfası olarak üretelim. `render_report(summary)` bir sözlük alsın (kategori -> toplam) ve bir HTML yazısı döndürsün:

- `<h1>Harcama Raporu</h1>`
- Her kategori için `<li>market: 420 TL</li>` (bir `<ul>` içinde)

**Başlangıç kodu:**

```python
def render_report(summary):
    html = "<h1>Harcama Raporu</h1>"
    return html
```

**İpuçları:**

1. Yazıyı += ile adım adım büyütebilirsin.
2. for category, total in summary.items():

<details><summary>Çözüm</summary>

```python
def render_report(summary):
    html = "<h1>Harcama Raporu</h1>"
    html += "<ul>"
    for category, total in summary.items():
        html += f"<li>{category}: {total} TL</li>"
    html += "</ul>"
    return html


print(render_report({"market": 420, "kira": 2000}))
```

</details>

### Görev Asistanı: HTML yapılacaklar listesi

Görev listesini bir web sayfası olarak gösterelim. `render_todo(tasks)` `(başlık, bitti_mi)` ikililerini alsın ve HTML döndürsün:

- `<h1>Yapılacaklar</h1>`
- Bir `<ul>` içinde her görev için `<li>Spor</li>`; biten görevlerin başlığı üstü çizili olsun: `<li><s>Kahve</s></li>`

**Başlangıç kodu:**

```python
def render_todo(tasks):
    html = "<h1>Yapılacaklar</h1>"
    return html
```

**İpuçları:**

1. Her görev için if done: ile iki farklı <li> yaz.
2. Üstü çizili: <s>...</s>

<details><summary>Çözüm</summary>

```python
def render_todo(tasks):
    html = "<h1>Yapılacaklar</h1><ul>"
    for title, done in tasks:
        if done:
            html += f"<li><s>{title}</s></li>"
        else:
            html += f"<li>{title}</li>"
    html += "</ul>"
    return html


print(render_todo([("Kahve", True), ("Spor", False)]))
```

</details>

### Kişisel Web Sitem: Tam HTML sayfası

Artık her sayfayı tam bir HTML belgesi olarak üretelim. `render_page(title, content, menu)` bir HTML yazısı döndürsün:

- `<!DOCTYPE html>` ile başlasın, `<html>` ile `</html>` arasında olsun.
- `<head>` içinde `<title>başlık</title>`
- `<body>` içinde önce `<nav>`: `menu`'deki her `(ad, dosya)` için `<a href="dosya">ad</a>`, sonra `<h1>başlık</h1>` ve `<p>içerik</p>`

Örneğin `render_page("Hakkımda", "Merhaba, ben Ece!", [("Ana Sayfa", "index.html"), ("Blog", "blog.html")])` şöyle bir sayfa üretmeli:

```
<!DOCTYPE html>
<html>
<head><title>Hakkımda</title></head>
<body>
<nav><a href="index.html">Ana Sayfa</a> <a href="blog.html">Blog</a></nav>
<h1>Hakkımda</h1>
<p>Merhaba, ben Ece!</p>
</body>
</html>
```

**Başlangıç kodu:**

```python
def render_page(title, content, menu):
    html = "<!DOCTYPE html>\n"
    return html
```

**İpuçları:**

1. Yazıyı += ile adım adım büyütebilirsin; satır sonu için \n ekle.
2. Menü bağlantılarını bir listede topla, " ".join(links) ile birleştir.

<details><summary>Çözüm</summary>

```python
def render_page(title, content, menu):
    links = []
    for name, file in menu:
        links.append(f'<a href="{file}">{name}</a>')
    html = "<!DOCTYPE html>\n<html>\n"
    html += f"<head><title>{title}</title></head>\n"
    html += "<body>\n"
    html += "<nav>" + " ".join(links) + "</nav>\n"
    html += f"<h1>{title}</h1>\n"
    html += f"<p>{content}</p>\n"
    html += "</body>\n</html>\n"
    return html


print(render_page("Hakkımda", "Merhaba, ben Ece!", [("Ana Sayfa", "index.html"), ("Blog", "blog.html")]))
```

</details>

### Sohbet Botu: Sohbet sayfası

Konuşmayı bir web sayfası olarak gösterelim. `render_chat(bot_name, messages)` `(gönderen, metin)` ikililerini alsın ve HTML döndürsün:

- `<h1>Bilge ile sohbet</h1>` (ad `bot_name`'den)
- Gönderen `"bot"` ise: `<p class="bot"><b>Bilge:</b> Merhaba!</p>`
- Değilse: `<p class="user"><b>Sen:</b> selam</p>`

**Başlangıç kodu:**

```python
def render_chat(bot_name, messages):
    html = f"<h1>{bot_name} ile sohbet</h1>"
    return html
```

**İpuçları:**

1. for sender, text in messages: ile her mesajı al, html += ile ekle.
2. İçinde çift tırnak olan bir yazıyı tek tırnakla açabilirsin: f'<p class="bot">...'

<details><summary>Çözüm</summary>

```python
def render_chat(bot_name, messages):
    html = f"<h1>{bot_name} ile sohbet</h1>"
    for sender, text in messages:
        if sender == "bot":
            html += f'<p class="bot"><b>{bot_name}:</b> {text}</p>'
        else:
            html += f'<p class="user"><b>Sen:</b> {text}</p>'
    return html


print(render_chat("Bilge", [("user", "selam"), ("bot", "Merhaba!")]))
```

</details>

### Okul Not Defteri: HTML karne

Karneni bir web sayfası olarak üretelim. `render_report_card(student, grades)` öğrencinin adını ve bir sözlüğü (ders -> not) alsın ve HTML yazısı döndürsün:

- `<h1>Karne: Ece</h1>`
- Bir `<table>` içinde her ders için bir satır: `<tr><td>Matematik</td><td>85</td></tr>`
- Notu 50'nin altındaki derslerin satırı işaretli olsun: `<tr class="kaldi"><td>Fizik</td><td>40</td></tr>`

**Başlangıç kodu:**

```python
def render_report_card(student, grades):
    html = f"<h1>Karne: {student}</h1>"
    return html
```

**İpuçları:**

1. for lesson, grade in grades.items(): ve içinde if grade < 50:
2. İçinde çift tırnak olan yazıyı tek tırnakla aç: f'<tr class="kaldi">...'

<details><summary>Çözüm</summary>

```python
def render_report_card(student, grades):
    html = f"<h1>Karne: {student}</h1>"
    html += "<table>"
    for lesson, grade in grades.items():
        if grade < 50:
            html += f'<tr class="kaldi"><td>{lesson}</td><td>{grade}</td></tr>'
        else:
            html += f"<tr><td>{lesson}</td><td>{grade}</td></tr>"
    html += "</table>"
    return html


print(render_report_card("Ece", {"Matematik": 85, "Fizik": 40}))
```

</details>
