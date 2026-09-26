# Gün 22: Web kazıma

**Kurs:** 30 Günde Python  ·  **Bölge:** Bilgi Limanı  ·  **Maskot:** Piko

**Bugünün hedefi:** BeautifulSoup ile HTML sayfalarından başlık, bağlantı ve metin toplamak

> Limandaki bilgi panosu ilanlarla dolu: gemi saatleri, fiyatlar, kayıp eşyalar... Hepsini elle deftere geçirmek saatler sürer. Web sayfaları da böyle panolardır. Bir programın sayfayı okuyup işine yarayan bilgileri toplamasına **web kazıma** denir.

![Bilgi Limanı](../../gorseller/python/harita/liman.webp)

## Konu anlatımı

### HTML'e hızlı bakış

Web sayfaları **HTML** ile yazılır. HTML, içeriği etiketlerle işaretler:

```
<h1>Başlık</h1>
<p class="fiyat">25 altın</p>
<a href="/harita">Haritaya git</a>
```

- `<h1>`, `<p>`, `<a>` etiket adları
- `class="fiyat"` ve `href="/harita"` etiketin **özellikleri**
- Etiketlerin arasındaki yazı, etiketin metnidir

### BeautifulSoup

`BeautifulSoup` HTML'i okuyup içinde arama yapmamızı sağlayan bir pakettir:

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, "html.parser")
print(soup.title.text)              # <title> etiketinin metni
first = soup.find("p")              # ilk <p>
prices = soup.find_all("p", class_="fiyat")   # tüm fiyat paragrafları
link = soup.find("a")["href"]       # bir özelliğin değeri
```

`class` Python'da özel bir kelime olduğu için sonuna alt çizgi koyarız: `class_`

### Gerçek dünyada

Gerçek bir sayfayı kazırken önce sayfanın HTML'i internetten indirilir:

```python
import requests
html = requests.get("https://ornek.com").text
```

Bu sitede internetten sayfa indiremediğimiz için HTML'i hazır bir yazı olarak vereceğiz. Kazıma kısmı aynen böyle çalışır.

İlk çalıştırmada BeautifulSoup paketi yükleneceği için birkaç saniye bekleyebilirsin.

### Kibar bir kazıyıcı ol

- Bir sitenin kazınmaya izin verip vermediğine bak (sitenin kullanım şartları ve `robots.txt` dosyası)
- Siteye saniyede yüzlerce istek gönderme, sunucuyu yorarsın
- Kişisel bilgileri toplama
- Site bir **API** sunuyorsa kazımak yerine onu kullan (28. günde göreceğiz)

## Örnekler

### Başlık ve paragraflar

```python
from bs4 import BeautifulSoup

html = """
<html><head><title>Liman Panosu</title></head>
<body>
  <h1>Bugünün gemileri</h1>
  <p>Martı saat 10.00'da kalkıyor.</p>
  <p>Yunus saat 14.30'da geliyor.</p>
</body></html>
"""

soup = BeautifulSoup(html, "html.parser")
print(soup.title.text)
print(soup.find("h1").text)
for p in soup.find_all("p"):
    print("-", p.text)
```

### Bağlantılar

```python
from bs4 import BeautifulSoup

html = '<a href="/harita">Harita</a> <a href="/gemiler">Gemiler</a>'
soup = BeautifulSoup(html, "html.parser")
for a in soup.find_all("a"):
    print(a.text, "->", a["href"])
```

### Sınıfa göre bul

```python
from bs4 import BeautifulSoup

html = """
<ul>
  <li class="urun">İp <span class="fiyat">5</span></li>
  <li class="urun">Fener <span class="fiyat">40</span></li>
</ul>
"""
soup = BeautifulSoup(html, "html.parser")
prices = [int(s.text) for s in soup.find_all("span", class_="fiyat")]
print(prices, "toplam:", sum(prices))
```

## Görevler

### Görev 1: Sayfa başlığı

`html` içindeki sayfa başlığını (`<title>`) bul ve `title` değişkenine koy.

**Başlangıç kodu:**

```python
from bs4 import BeautifulSoup

html = "<html><head><title>Piko'nun Günlüğü</title></head><body><h1>Merhaba</h1></body></html>"

soup = BeautifulSoup(html, "html.parser")
title = ""

print(title)
```

**İpuçları:**

1. soup.title başlık etiketini verir.
2. Metni için sonuna .text ekle.

<details><summary>Çözüm</summary>

```python
from bs4 import BeautifulSoup

html = "<html><head><title>Piko'nun Günlüğü</title></head><body><h1>Merhaba</h1></body></html>"

soup = BeautifulSoup(html, "html.parser")
title = soup.title.text

print(title)
```

</details>

### Görev 2: Tüm bağlantılar

Sayfadaki tüm `<a>` etiketlerinin `href` değerlerini sırayla `links` listesine koy.

**Başlangıç kodu:**

```python
from bs4 import BeautifulSoup

html = '<a href="/harita">Harita</a> <p>yazı</p> <a href="/gemiler">Gemiler</a>'
soup = BeautifulSoup(html, "html.parser")

links = []

print(links)
```

**İpuçları:**

1. soup.find_all("a") tüm bağlantıları verir.
2. Bir etiketin özelliği: a["href"]

<details><summary>Çözüm</summary>

```python
from bs4 import BeautifulSoup

html = '<a href="/harita">Harita</a> <p>yazı</p> <a href="/gemiler">Gemiler</a>'
soup = BeautifulSoup(html, "html.parser")

links = [a["href"] for a in soup.find_all("a")]

print(links)
```

</details>

### Görev 3: Fiyatları topla

`class="fiyat"` olan tüm etiketlerdeki sayıları topla ve `total` değişkenine koy.

**Başlangıç kodu:**

```python
from bs4 import BeautifulSoup

html = """
<li>İp <span class="fiyat">5</span></li>
<li>Fener <span class="fiyat">40</span></li>
<li>Harita <span class="fiyat">15</span></li>
"""
soup = BeautifulSoup(html, "html.parser")

total = 0

print("Toplam:", total)
```

**İpuçları:**

1. soup.find_all(class_="fiyat")
2. Metinler yazıdır, toplamadan önce int() ile çevir.

<details><summary>Çözüm</summary>

```python
from bs4 import BeautifulSoup

html = """
<li>İp <span class="fiyat">5</span></li>
<li>Fener <span class="fiyat">40</span></li>
<li>Harita <span class="fiyat">15</span></li>
"""
soup = BeautifulSoup(html, "html.parser")

total = sum([int(s.text) for s in soup.find_all(class_="fiyat")])

print("Toplam:", total)
```

</details>

## Challenge: Tabloyu oku

HTML tablosundaki her satırı `(isim, skor)` tuple'ı olarak `rows` listesine koy. Başlık satırını atla, skoru int yap.

**Başlangıç kodu:**

```python
from bs4 import BeautifulSoup

html = """
<table>
  <tr><th>İsim</th><th>Skor</th></tr>
  <tr><td>Piko</td><td>300</td></tr>
  <tr><td>Ece</td><td>250</td></tr>
</table>
"""
soup = BeautifulSoup(html, "html.parser")

rows = []

print(rows)
```

**İpuçları:**

1. Her satır bir <tr>. İçindeki hücreler: tr.find_all("td")
2. Başlık satırında <td> yoktur, <th> vardır; bu yüzden boş gelir.

<details><summary>Çözüm</summary>

```python
from bs4 import BeautifulSoup

html = """
<table>
  <tr><th>İsim</th><th>Skor</th></tr>
  <tr><td>Piko</td><td>300</td></tr>
  <tr><td>Ece</td><td>250</td></tr>
</table>
"""
soup = BeautifulSoup(html, "html.parser")

rows = []
for tr in soup.find_all("tr"):
    cells = tr.find_all("td")
    if len(cells) == 2:
        rows.append((cells[0].text, int(cells[1].text)))

print(rows)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Hazine ipuçları**

### Piko'nun Macerası: Hazine ipuçları

Limandaki eski bir sayfada hazine ipuçları saklı. Sadece `class="ipucu"` olan maddeler gerçek ipucu, diğerleri tuzak!

- Gerçek ipuçlarının metinlerini sırayla `clues` listesine koy.
- Sonra `1. Deniz fenerine git` gibi numaralı yazdır.

**Başlangıç kodu:**

```python
from bs4 import BeautifulSoup

html = """
<ul>
  <li class="ipucu">Deniz fenerine git</li>
  <li class="tuzak">Mağaraya gir</li>
  <li class="ipucu">Üç adım kuzeye yürü</li>
  <li class="ipucu">Kırmızı taşın altına bak</li>
</ul>
"""
soup = BeautifulSoup(html, "html.parser")

clues = []

# Numaralı yazdır
```

**İpuçları:**

1. soup.find_all("li", class_="ipucu")
2. Numaralar için enumerate(clues, 1)

<details><summary>Çözüm</summary>

```python
from bs4 import BeautifulSoup

html = """
<ul>
  <li class="ipucu">Deniz fenerine git</li>
  <li class="tuzak">Mağaraya gir</li>
  <li class="ipucu">Üç adım kuzeye yürü</li>
  <li class="ipucu">Kırmızı taşın altına bak</li>
</ul>
"""
soup = BeautifulSoup(html, "html.parser")

clues = [li.text.strip() for li in soup.find_all("li", class_="ipucu")]

for i, clue in enumerate(clues, 1):
    print(f"{i}. {clue}")
```

</details>

### Harcama Defteri: Kur tablosunu okuma

Bir sitedeki kur tablosu HTML olarak `html` değişkeninde. Her kur `<td class="kur" data-kod="USD">32.50</td>` gibi.

BeautifulSoup ile `class="kur"` olan hücreleri bul ve `rates` sözlüğünü oluştur: `{"USD": 32.5, "EUR": 35.1}` (değerler float). Sonra `USD: 32.5` gibi her kuru ayrı satırda yazdır.

**Başlangıç kodu:**

```python
from bs4 import BeautifulSoup

html = """
<table>
  <tr><td class="kur" data-kod="USD">32.50</td></tr>
  <tr><td class="kur" data-kod="EUR">35.10</td></tr>
  <tr><td class="not">Kurlar bilgi amaçlıdır</td></tr>
</table>
"""
```

**İpuçları:**

1. soup.find_all("td", class_="kur") kur hücrelerini verir.
2. cell["data-kod"] özelliği, cell.text içindeki yazıyı verir.

<details><summary>Çözüm</summary>

```python
from bs4 import BeautifulSoup

html = """
<table>
  <tr><td class="kur" data-kod="USD">32.50</td></tr>
  <tr><td class="kur" data-kod="EUR">35.10</td></tr>
  <tr><td class="not">Kurlar bilgi amaçlıdır</td></tr>
</table>
"""
soup = BeautifulSoup(html, "html.parser")
rates = {}
for cell in soup.find_all("td", class_="kur"):
    rates[cell["data-kod"]] = float(cell.text)
for code in rates:
    print(f"{code}: {rates[code]}")
```

</details>

### Görev Asistanı: Duyuruları toplama

Okulunun duyuru sayfası `html` değişkeninde. Her duyuru `<div class="duyuru">` içinde bir `<a>` bağlantısı.

BeautifulSoup ile duyuruları bul ve `(başlık, bağlantı)` tuple'larından oluşan `notices` listesini yap. Reklamları (`class="reklam"`) alma. Sonra her birini `- Sınav takvimi: /sinav` gibi yazdır.

**Başlangıç kodu:**

```python
from bs4 import BeautifulSoup

html = """
<div class="duyuru"><a href="/sinav">Sınav takvimi</a></div>
<div class="reklam"><a href="/kampanya">Büyük indirim!</a></div>
<div class="duyuru"><a href="/gezi">Gezi formu</a></div>
"""
```

**İpuçları:**

1. soup.find_all("div", class_="duyuru")
2. box.find("a") bağlantıyı verir; link.text başlık, link["href"] adres.

<details><summary>Çözüm</summary>

```python
from bs4 import BeautifulSoup

html = """
<div class="duyuru"><a href="/sinav">Sınav takvimi</a></div>
<div class="reklam"><a href="/kampanya">Büyük indirim!</a></div>
<div class="duyuru"><a href="/gezi">Gezi formu</a></div>
"""
soup = BeautifulSoup(html, "html.parser")
notices = []
for box in soup.find_all("div", class_="duyuru"):
    link = box.find("a")
    notices.append((link.text, link["href"]))
for title, href in notices:
    print(f"- {title}: {href}")
```

</details>

### Kişisel Web Sitem: Başka bir sayfayı okuma

Bir arkadaşının blogunu kendi sitende önermek istiyorsun. Sayfanın HTML'i `html` değişkeninde.

BeautifulSoup ile:

- `page_title`: sayfanın `<title>` yazısı
- `posts`: `class="post"` olan bağlantılardan `(yazı, adres)` tuple'larının listesi: `[("Oyun Yaptım", "/yazi/oyun.html"), ...]`
- Önce `page_title`'ı, sonra her yazıyı `Oyun Yaptım -> /yazi/oyun.html` gibi ayrı satırda yazdır.

**Başlangıç kodu:**

```python
from bs4 import BeautifulSoup

html = """
<html><head><title>Can'ın Blogu</title></head>
<body>
  <a class="post" href="/yazi/oyun.html">Oyun Yaptım</a>
  <a class="menu" href="/hakkinda.html">Hakkında</a>
  <a class="post" href="/yazi/robot.html">Robot Kolu</a>
</body></html>
"""
```

**İpuçları:**

1. soup.title.text sayfa başlığını verir; soup.find_all("a", class_="post") yazı bağlantılarını.
2. a.text bağlantının yazısını, a["href"] adresini verir.

<details><summary>Çözüm</summary>

```python
from bs4 import BeautifulSoup

html = """
<html><head><title>Can'ın Blogu</title></head>
<body>
  <a class="post" href="/yazi/oyun.html">Oyun Yaptım</a>
  <a class="menu" href="/hakkinda.html">Hakkında</a>
  <a class="post" href="/yazi/robot.html">Robot Kolu</a>
</body></html>
"""
soup = BeautifulSoup(html, "html.parser")
page_title = soup.title.text
posts = []
for a in soup.find_all("a", class_="post"):
    posts.append((a.text, a["href"]))
print(page_title)
for text, href in posts:
    print(f"{text} -> {href}")
```

</details>

### Sohbet Botu: SSS sayfasını okuma

Bot, bir sitenin **Sık Sorulan Sorular** sayfasından cevap öğrensin. Sayfa `html` değişkeninde; her soru-cevap bir `<div class="sss">` içinde: soru `<h3>`, cevap `<p>`.

BeautifulSoup ile `class="sss"` olan kutuları bul ve `faq` sözlüğünü oluştur (soru -> cevap). Reklam kutusunu alma. Sonra her birini iki satırda yazdır:

```
S: Kargo ne zaman gelir?
C: 2-3 iş günü içinde.
```

**Başlangıç kodu:**

```python
from bs4 import BeautifulSoup

html = """
<div class="sss"><h3>Kargo ne zaman gelir?</h3><p>2-3 iş günü içinde.</p></div>
<div class="reklam"><h3>Büyük indirim!</h3><p>Hemen al.</p></div>
<div class="sss"><h3>İade edebilir miyim?</h3><p>Evet, 14 gün içinde.</p></div>
"""
```

**İpuçları:**

1. soup.find_all("div", class_="sss") soru kutularını verir.
2. box.find("h3").text soruyu, box.find("p").text cevabı verir.

<details><summary>Çözüm</summary>

```python
from bs4 import BeautifulSoup

html = """
<div class="sss"><h3>Kargo ne zaman gelir?</h3><p>2-3 iş günü içinde.</p></div>
<div class="reklam"><h3>Büyük indirim!</h3><p>Hemen al.</p></div>
<div class="sss"><h3>İade edebilir miyim?</h3><p>Evet, 14 gün içinde.</p></div>
"""
soup = BeautifulSoup(html, "html.parser")
faq = {}
for box in soup.find_all("div", class_="sss"):
    question = box.find("h3").text
    answer = box.find("p").text
    faq[question] = answer
for question in faq:
    print(f"S: {question}")
    print(f"C: {faq[question]}")
```

</details>

### Okul Not Defteri: Not sayfasını okuma

Okulunun not sayfası HTML olarak `html` değişkeninde. Her ders bir `<tr class="ders">` satırı; içinde ders adı `<td class="ad">`, not `<td class="puan">` hücresinde. Duyuru satırlarını alma.

BeautifulSoup ile `grades` sözlüğünü oluştur: `{"Matematik": 85, "Fizik": 70}` (notlar tam sayı). Sonra her dersi `Matematik: 85` gibi ayrı satırda yazdır.

**Başlangıç kodu:**

```python
from bs4 import BeautifulSoup

html = """
<table>
  <tr><th>Ders</th><th>Not</th></tr>
  <tr class="ders"><td class="ad">Matematik</td><td class="puan">85</td></tr>
  <tr class="ders"><td class="ad">Fizik</td><td class="puan">70</td></tr>
  <tr class="duyuru"><td>Veli toplantısı cuma günü</td></tr>
</table>
"""
```

**İpuçları:**

1. soup.find_all("tr", class_="ders") ders satırlarını verir.
2. row.find("td", class_="puan").text notun yazısını verir; int() ile sayıya çevir.

<details><summary>Çözüm</summary>

```python
from bs4 import BeautifulSoup

html = """
<table>
  <tr><th>Ders</th><th>Not</th></tr>
  <tr class="ders"><td class="ad">Matematik</td><td class="puan">85</td></tr>
  <tr class="ders"><td class="ad">Fizik</td><td class="puan">70</td></tr>
  <tr class="duyuru"><td>Veli toplantısı cuma günü</td></tr>
</table>
"""
soup = BeautifulSoup(html, "html.parser")
grades = {}
for row in soup.find_all("tr", class_="ders"):
    name = row.find("td", class_="ad").text
    grades[name] = int(row.find("td", class_="puan").text)
for name in grades:
    print(f"{name}: {grades[name]}")
```

</details>
