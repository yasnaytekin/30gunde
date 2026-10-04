# Video senaryosu: Gün 22, Web kazıma

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~155 sn

Piko, Bilgi Limanı'nın ilan panosundan yola çıkarak HTML'in yapısını ve BeautifulSoup ile başlık, bağlantı ve metin toplamayı anlatıyor.

Ders metni: [gun-22.md](../gunler/gun-22.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | sasirma (sag) |
| 2 | anlatim | 15 sn | isaret (sol) |
| 3 | kod | 17 sn | isaret (sag) |
| 4 | kod | 12 sn | isaret (sol) |
| 5 | kod | 15 sn | konusma (sag) |
| 6 | hata | 13 sn | uzgun (sol) |
| 7 | soru | 9 sn | dusunme (sag) |
| 8 | cikti | 9 sn | mutlu (sol) |
| 9 | anlatim | 15 sn | dusunme (sag) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 12 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Gün 22: Web kazıma! Bu derste HTML'in yapısını ve BeautifulSoup ile sayfalardan başlık, bağlantı ve metin toplamayı öğreneceksin.

- HTML etiketleri
- find ve find_all
- Kibar bir kazıyıcı olmak

## Sahne 1: acilis (14 sn)

**Seslendirme:** Selam, ben Piko! Bilgi Limanı'nın panosu ilanlarla dolu: gemi saatleri, fiyatlar, kayıp eşyalar. Hepsini elle deftere geçirmek saatler sürer. Web sayfaları da böyle panolar. Bugün sayfalardan bilgi toplamayı, yani web kazımayı öğreniyoruz!

**Ekranda başlık:** Gün 22: Web kazıma

**Ekranda maddeler:**

- Bilgi Limanı
- HTML ve BeautifulSoup

**Maskot:** sasirma pozu, sag

*Yönetmen notu: Arka plan: Bilgi Limanı bölge görseli (gorseller/python/harita/liman.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Rüzgârda uçuşan ilanlarla dolu bir pano.*

## Sahne 2: anlatim (15 sn)

**Seslendirme:** Web sayfaları HTML ile yazılır. İçerik etiketlerle işaretlenir: h1 başlık, p paragraf, a bağlantı. class ve href etiketin özellikleri, etiketlerin arasındaki yazı da metni.

**Ekranda başlık:** HTML'e hızlı bakış

**Kod** (vurgulanan satırlar: 2, 3):

```html
<h1>Başlık</h1>
<p class="fiyat">25 altın</p>
<a href="/harita">Haritaya git</a>
```

**Maskot:** isaret pozu, sol

## Sahne 3: kod (17 sn)

**Seslendirme:** BeautifulSoup HTML'i okuyup içinde arama yapmamızı sağlar. soup.title başlığı, find ilk eşleşen etiketi, find_all ise hepsini liste olarak getiriyor. Sonundaki .text etiketin içindeki yazıyı veriyor.

**Ekranda başlık:** Başlık ve paragraflar

**Kod** (vurgulanan satırlar: 8, 11):

```python
from bs4 import BeautifulSoup

html = """<title>Liman Panosu</title>
<h1>Bugünün gemileri</h1>
<p>Martı 10.00'da kalkıyor.</p>
<p>Yunus 14.30'da geliyor.</p>"""

soup = BeautifulSoup(html, "html.parser")
print(soup.title.text)
print(soup.find("h1").text)
for p in soup.find_all("p"):
    print("-", p.text)
```

**Çıktı:**

```text
Liman Panosu
Bugünün gemileri
- Martı 10.00'da kalkıyor.
- Yunus 14.30'da geliyor.
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: Kod bs4 (BeautifulSoup) paketini kullanır; doğrulayıcının Python ortamında kurulu olmalı.*

## Sahne 4: kod (12 sn)

**Seslendirme:** Bir özelliğin değerini almak için etikete sözlük gibi davranıyorum: köşeli parantez içinde href. Her bağlantının yazısı ve adresi yan yana geliyor.

**Ekranda başlık:** Bağlantılar

**Kod** (vurgulanan satırlar: 6):

```python
from bs4 import BeautifulSoup

html = '<a href="/harita">Harita</a> <a href="/gemiler">Gemiler</a>'
soup = BeautifulSoup(html, "html.parser")
for a in soup.find_all("a"):
    print(a.text, "->", a["href"])
```

**Çıktı:**

```text
Harita -> /harita
Gemiler -> /gemiler
```

**Maskot:** isaret pozu, sol

*Yönetmen notu: Kod bs4 (BeautifulSoup) paketini kullanır; doğrulayıcının Python ortamında kurulu olmalı.*

## Sahne 5: kod (15 sn)

**Seslendirme:** Sadece fiyatları istiyorum. class Python'da özel bir kelime olduğu için sonuna alt çizgi koyuyorum. Bulunan yazıları int ile sayıya çevirip topluyorum.

**Ekranda başlık:** Sınıfa göre bul: class_

**Kod** (vurgulanan satırlar: 6):

```python
from bs4 import BeautifulSoup

html = """<li>İp <span class="fiyat">5</span></li>
<li>Fener <span class="fiyat">40</span></li>"""
soup = BeautifulSoup(html, "html.parser")
spans = soup.find_all("span", class_="fiyat")
prices = [int(s.text) for s in spans]
print(prices, "toplam:", sum(prices))
```

**Çıktı:**

```text
[5, 40] toplam: 45
```

**Maskot:** konusma pozu, sag

*Yönetmen notu: Kod bs4 (BeautifulSoup) paketini kullanır; doğrulayıcının Python ortamında kurulu olmalı.*

## Sahne 6: hata (13 sn)

**Seslendirme:** Sık hata: sayfada olmayan bir etiketi aramak. find bir şey bulamazsa None döner. None'ın text'i olmadığı için AttributeError alırsın. Önce sonucun None olup olmadığına bak.

**Ekranda başlık:** Sık hata: bulunamayan etiket

**Kod** (vurgulanan satırlar: 4):

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Merhaba</p>", "html.parser")
print(soup.find("h1").text)
```

**Çıktı:**

```text
AttributeError: 'NoneType' object has no attribute 'text'
```

**Maskot:** uzgun pozu, sol

*Yönetmen notu: Kod bs4 (BeautifulSoup) paketini kullanır; doğrulayıcının Python ortamında kurulu olmalı.*

## Sahne 7: soru (9 sn)

**Seslendirme:** Mini soru! Üç paragraf var. Sence find ne getirir, find_all'un uzunluğu kaç çıkar?

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```python
from bs4 import BeautifulSoup

html = "<p>İp</p><p>Fener</p><p>Harita</p>"
soup = BeautifulSoup(html, "html.parser")
print(soup.find("p").text)
print(len(soup.find_all("p")))
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (9 sn)

**Seslendirme:** find sadece ilk paragrafı, yani İp'i getirdi. find_all üçünü de buldu.

**Ekranda başlık:** Cevap

**Kod**:

```python
from bs4 import BeautifulSoup

html = "<p>İp</p><p>Fener</p><p>Harita</p>"
soup = BeautifulSoup(html, "html.parser")
print(soup.find("p").text)
print(len(soup.find_all("p")))
```

**Çıktı:**

```text
İp
3
```

**Maskot:** mutlu pozu, sol

*Yönetmen notu: Kod bs4 (BeautifulSoup) paketini kullanır; doğrulayıcının Python ortamında kurulu olmalı.*

## Sahne 9: anlatim (15 sn)

**Seslendirme:** Gerçek bir sayfada HTML önce requests ile internetten indirilir. Ama kibar bir kazıyıcı ol: sitenin izin verip vermediğine bak, sunucuyu isteklere boğma, kişisel bilgi toplama. Site bir API sunuyorsa onu kullan.

**Ekranda başlık:** Kibar bir kazıyıcı ol

**Ekranda maddeler:**

- Gerçekte: html = requests.get(adres).text
- Kullanım şartları ve robots.txt
- Çok hızlı istek gönderme
- Kişisel bilgi toplama
- API varsa onu kullan

**Maskot:** dusunme pozu, sag

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görevlerde sayfanın başlığını bulacak, tüm bağlantıları toplayacak ve fiyatları toplayacaksın. Projede de eski bir sayfadaki gerçek hazine ipuçlarını tuzaklardan ayırıyorsun.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Sayfa başlığı
- Görev 2: Tüm bağlantılar
- Görev 3: Fiyatları topla
- Challenge: Tabloyu oku
- Proje: Hazine ipuçları

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** Özetle: HTML'i BeautifulSoup'a ver, find ile tekini, find_all ile hepsini bul, sonra text ve özelliklerini al.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- HTML: etiket, özellik, metin
- find, find_all, class_
- .text ve etiket["href"]

**Maskot:** on pozu, sag

## Sahne 12: kapanis (12 sn)

**Seslendirme:** Panoyu okumayı öğrendin, bravo! Yarın projelerimizi düzene sokacağız. Her projeye kendi paket dolabını veren sanal ortamı tanıyacağız. Görüşürüz!

**Ekranda başlık:** Yarın: Sanal ortam

**Ekranda maddeler:**

- venv
- Proje düzeni

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** Bu dersin interaktif hâli 30gunde.com.tr'de seni bekliyor. Kodunu tarayıcıda yaz, hemen çalıştır ve görevleri tamamla!

**Ekranda:** İnteraktif dersler için **30gunde.com.tr**

- Kodunu tarayıcıda yaz ve çalıştır
- Görevleri tamamla, rozet kazan
- 30 günde adım adım Python
