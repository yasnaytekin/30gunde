# Video senaryosu: Gün 26, Python ile web

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~156 sn

Piko, Python Dağı'ndaki gözlem kulesi üzerinden web'in istek ve yanıtla çalışmasını, durum kodlarını, Python ile HTML üretmeyi ve sözlükle yönlendirmeyi anlatıyor.

Ders metni: [gun-26.md](../gunler/gun-26.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | mutlu (sag) |
| 2 | anlatim | 16 sn | isaret (sol) |
| 3 | kod | 12 sn | mutlu (sag) |
| 4 | anlatim | 17 sn | konusma (sag) |
| 5 | kod | 16 sn | isaret (sol) |
| 6 | anlatim | 12 sn | konusma (sag) |
| 7 | soru | 10 sn | dusunme (sag) |
| 8 | cikti | 11 sn | mutlu (sol) |
| 9 | hata | 12 sn | uzgun (sag) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 12 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Gün 26: Python ile web! Bu derste web'in istek ve yanıtla nasıl çalıştığını, durum kodlarını, Python ile HTML üretmeyi ve yönlendirmeyi öğreneceksin.

- İstek, yanıt, durum kodu
- Python ile HTML üretmek
- Sözlükle yönlendirme

## Sahne 1: acilis (14 sn)

**Seslendirme:** Selam, ben Piko! Son bölgeye, Python Dağı'nın eteğine geldik! Tepede dev bir gözlem kulesi var ve dünyanın her yerinden mesaj alıyor. Her mesaj bir istek, kulenin her cevabı bir yanıt. Web siteleri de tam böyle çalışır!

**Ekranda başlık:** Gün 26: Python ile web

**Ekranda maddeler:**

- Yeni bölge: Python Dağı
- İstek, yanıt, HTML üretmek

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Arka plan: Python Dağı bölge görseli (gorseller/python/harita/dag.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Dağın tepesindeki gözlem kulesine ışıklı mesajlar gidip gelir.*

## Sahne 2: anlatim (16 sn)

**Seslendirme:** Tarayıcına bir adres yazınca tarayıcı sunucuya bir istek gönderir: bana profil sayfasını ver. Sunucu sayfayı hazırlar ve bir yanıt döner. Yanıtta HTML ve bir durum kodu vardır.

**Ekranda başlık:** İstek ve yanıt

**Ekranda maddeler:**

- Tarayıcı → istek: GET /profil
- Sunucu → yanıt: HTML + durum kodu
- 200 tamam, 404 bulunamadı, 500 sunucu hatası

**Maskot:** isaret pozu, sol

## Sahne 3: kod (12 sn)

**Seslendirme:** Durum kodlarını bir sözlükte tutuyorum. get ile sorarken sözlükte olmayan bir kod gelirse Bilinmiyor diyor. Dört yüz on sekiz gerçekten var: ben bir çaydanlığım demek!

**Ekranda başlık:** Durum kodları

**Kod** (vurgulanan satırlar: 3):

```python
codes = {200: "Tamam", 404: "Bulunamadı", 500: "Sunucu hatası"}
for code in [200, 404, 500, 418]:
    print(code, codes.get(code, "Bilinmiyor"))
```

**Çıktı:**

```text
200 Tamam
404 Bulunamadı
500 Sunucu hatası
418 Bilinmiyor
```

**Maskot:** mutlu pozu, sag

## Sahne 4: anlatim (17 sn)

**Seslendirme:** Python'da web sitesi yapmanın sevilen yollarından biri Flask. route satırı şunu söyler: biri ana adresi isterse home fonksiyonunu çalıştır. Bu sitede sunucu başlatamıyoruz, o yüzden aynı fikri düz Python ile deneyeceğiz.

**Ekranda başlık:** Flask ile bir site (kendi bilgisayarında)

**Kod** (vurgulanan satırlar: 4):

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Piko'nun sitesine hoş geldin!</h1>"

app.run()
```

**Maskot:** konusma pozu, sag

*Yönetmen notu: Sunucu başlattığı için çalıştırılmaz; sadece yapıyı gösterir.*

## Sahne 5: kod (16 sn)

**Seslendirme:** Bir sunucunun asıl işi veriden HTML yazısı üretmek. Başlığı f-string ile kuruyorum. Listeyi de her eşya için bir li etiketi yapıp join ile birleştiriyorum. İşte tarayıcıya gidecek sayfa!

**Ekranda başlık:** HTML üretmek

**Kod** (vurgulanan satırlar: 4, 5):

```python
name = "Piko"
items = ["kılıç", "iksir", "harita"]

page = f"<h1>{name}'nun çantası</h1>"
page += "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
print(page)
```

**Çıktı:**

```text
<h1>Piko'nun çantası</h1><ul><li>kılıç</li><li>iksir</li><li>harita</li></ul>
```

**Maskot:** isaret pozu, sol

## Sahne 6: anlatim (12 sn)

**Seslendirme:** Hangi adresin hangi fonksiyona gideceğine yönlendirme denir. Bunu bir sözlükle kurabiliriz: anahtar adres, değer de o sayfayı üreten fonksiyon.

**Ekranda başlık:** Yönlendirme (routing)

**Kod** (vurgulanan satırlar: 7):

```python
def home():
    return "<h1>Ana sayfa</h1>"

def about():
    return "<h1>Hakkında</h1>"

routes = {"/": home, "/hakkinda": about}
```

**Maskot:** konusma pozu, sag

## Sahne 7: soru (10 sn)

**Seslendirme:** Üç adres deniyorum: ana sayfa, hakkında ve gizli. Sözlükte olmayan adres gelince ne olur? Sence ekranda ne görürüz?

**Ekranda başlık:** Sence ne yazdırır?

**Kod** (vurgulanan satırlar: 10, 11):

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

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (11 sn)

**Seslendirme:** İlk iki adres kendi sayfalarını getirdi. Gizli sözlükte yok, get None verdi ve biz de dört yüz dört Bulunamadı gösterdik. Flask bunu senin yerine yapar.

**Ekranda başlık:** Cevap: mini yönlendirme

**Kod**:

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

**Çıktı:**

```text
/ -> <h1>Ana sayfa</h1>
/hakkinda -> <h1>Hakkında</h1>
/gizli -> 404 Bulunamadı
```

**Maskot:** mutlu pozu, sol

## Sahne 9: hata (12 sn)

**Seslendirme:** Sık hata: sözlükte olmayan adresi doğrudan köşeli parantezle istemek. Python KeyError verir ve sunucu çöker. get kullanıp olmayan adreslere dört yüz dört dön.

**Ekranda başlık:** Sık hata: olmayan adres

**Kod** (vurgulanan satırlar: 2):

```python
routes = {"/": "Ana sayfa"}
print(routes["/gizli"])
```

**Çıktı:**

```text
KeyError: '/gizli'
```

**Maskot:** uzgun pozu, sag

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görevlerde bir karşılama sayfası ve bir liste sayfası üretecek, durum kodlarını yazıya çeviren bir fonksiyon yazacaksın. Projede de Piko'nun profil sayfasını oluşturuyorsun.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Karşılama sayfası
- Görev 2: Liste sayfası
- Görev 3: Durum kodu
- Challenge: Mini sunucu
- Proje: Oyunun web sayfası

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** Özetle: web istek ve yanıtla çalışır, sunucu veriden HTML üretir, yönlendirme de adresi doğru fonksiyona götürür.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- İstek, yanıt ve durum kodları
- f-string ve join ile HTML
- Sözlükle yönlendirme, yoksa 404

**Maskot:** on pozu, sag

## Sahne 12: kapanis (12 sn)

**Seslendirme:** Kulenin ilk mesajlarını cevapladın, tebrikler! Yarın dağın arşivine iniyoruz. Belge tabanlı veritabanı MongoDB'yi ve insert, find, update işlemlerini keşfedeceğiz. Görüşürüz!

**Ekranda başlık:** Yarın: Python ve MongoDB

**Ekranda maddeler:**

- Belge tabanlı veritabanı
- insert, find, update

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** Bu dersin interaktif hâli 30gunde.com.tr'de seni bekliyor. Kodunu tarayıcıda yaz, hemen çalıştır ve görevleri tamamla!

**Ekranda:** İnteraktif dersler için **30gunde.com.tr**

- Kodunu tarayıcıda yaz ve çalıştır
- Görevleri tamamla, rozet kazan
- 30 günde adım adım Python
