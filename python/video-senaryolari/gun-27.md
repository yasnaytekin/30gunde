# Video senaryosu: Gün 27, Python ve MongoDB

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~160 sn

Piko, Python Dağı'nın kütüphanesinden yola çıkarak belge tabanlı veritabanı fikrini, MongoDB'nin insert, find ve update işlemlerini ve bunları Python sözlükleriyle canlandırmayı anlatıyor.

Ders metni: [gun-27.md](../gunler/gun-27.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 15 sn | konusma (sag) |
| 2 | anlatim | 16 sn | isaret (sol) |
| 3 | anlatim | 17 sn | konusma (sag) |
| 4 | kod | 14 sn | isaret (sag) |
| 5 | anlatim | 15 sn | dusunme (sol) |
| 6 | soru | 10 sn | dusunme (sag) |
| 7 | cikti | 12 sn | mutlu (sol) |
| 8 | kod | 13 sn | isaret (sag) |
| 9 | hata | 12 sn | uzgun (sol) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 12 sn | tebrik (orta) |

## Sahne 1: acilis (15 sn)

**Seslendirme:** Selam, ben Piko! Python Dağı'nın yamacındaki kütüphanede her oyuncunun bir dosyası var. Kütüphaneci bir isim duyunca doğru dosyayı saniyede buluyor, yeni dosya açıyor, seviyeleri güncelliyor. Bilgisayar dünyasında bu kütüphanecinin adı veritabanı!

**Ekranda başlık:** Gün 27: Python ve MongoDB

**Ekranda maddeler:**

- Python Dağı
- Belge, koleksiyon, sorgu

**Maskot:** konusma pozu, sag

*Yönetmen notu: Arka plan: Python Dağı bölge görseli (gorseller/python/harita/dag.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Raflarla dolu bir dağ kütüphanesi; kütüphaneci hızla dosya çeker.*

## Sahne 2: anlatim (16 sn)

**Seslendirme:** Program kapanınca değişkenler kaybolur. Binlerce oyuncunun verisini hızla aramak ve güvende tutmak için veritabanı kullanılır. MongoDB bir belge veritabanı: her kayıt bir sözlüğe benzeyen belge, belgeler de koleksiyonlarda toplanır.

**Ekranda başlık:** Veritabanı nedir?

**Ekranda maddeler:**

- Belge (document): {"name": "Piko", "level": 3}
- Koleksiyon (collection): belgelerin toplandığı yer
- MongoDB = belge veritabanı

**Maskot:** isaret pozu, sol

## Sahne 3: anlatim (17 sn)

**Seslendirme:** Kendi bilgisayarında pymongo paketiyle gerçek MongoDB'ye bağlanırsın. insert_one ekler, find arar, update_one günceller, delete_one siler. Bu sitede veritabanına bağlanamıyoruz, o yüzden koleksiyonu bir sözlük listesiyle canlandıracağız.

**Ekranda başlık:** pymongo ile gerçek MongoDB

**Kod** (vurgulanan satırlar: 5, 6, 8):

```python
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["oyun"]

db.players.insert_one({"name": "Piko", "level": 3})
for p in db.players.find({"level": 3}):
    print(p["name"])
db.players.update_one({"name": "Piko"}, {"$set": {"level": 4}})
```

**Maskot:** konusma pozu, sag

*Yönetmen notu: Veritabanı sunucusu gerektirdiği için çalıştırılmaz; sadece gerçek kullanımı gösterir.*

## Sahne 4: kod (14 sn)

**Seslendirme:** İşte koleksiyonumuz: sözlüklerden oluşan bir liste. Yeni belge eklemek append kadar kolay, yani insert'in ta kendisi. Döngüyle de tüm belgeleri geziyorum.

**Ekranda başlık:** Koleksiyon ve belgeler

**Kod** (vurgulanan satırlar: 5):

```python
players = [
    {"name": "Piko", "level": 3},
    {"name": "Ece", "level": 5},
]
players.append({"name": "Can", "level": 1})
for p in players:
    print(p["name"], "seviye", p["level"])
```

**Çıktı:**

```text
Piko seviye 3
Ece seviye 5
Can seviye 1
```

**Maskot:** isaret pozu, sag

## Sahne 5: anlatim (15 sn)

**Seslendirme:** find içindeki sorgu da bir sözlüktür. Seviye üç derse, seviyesi üç olan tüm belgeleri getirir. Belgenin, sorgudaki tüm alanlarla eşleşmesi gerekir. Hepsi doğru mu sorusunu all fonksiyonu tek satırda cevaplar.

**Ekranda başlık:** Sorgu (query) nedir?

**Ekranda maddeler:**

- find({"level": 3})
- Sorgudaki tüm alanlar eşleşmeli
- all(): hepsi doğru mu?
- any(): en az biri doğru mu?

**Maskot:** dusunme pozu, sol

## Sahne 6: soru (10 sn)

**Seslendirme:** Bir belgeyi dört farklı sorguyla deniyorum. Sonuncusu boş bir sorgu. Sence hangileri True, hangileri False çıkar?

**Ekranda başlık:** Sence ne yazdırır?

**Kod** (vurgulanan satırlar: 3):

```python
doc = {"name": "Piko", "level": 3, "club": "mavi"}
for query in [{"level": 3}, {"level": 3, "club": "mavi"}, {"level": 4}, {}]:
    ok = all(doc.get(k) == v for k, v in query.items())
    print(query, "->", ok)
```

**Maskot:** dusunme pozu, sag

## Sahne 7: cikti (12 sn)

**Seslendirme:** Seviye dört eşleşmedi, o yüzden False. Boş sorgunun kontrol edecek hiç alanı yok, all da boşsa True verir. Yani boş sorgu her belgeye uyar ve hepsini getirir.

**Ekranda başlık:** Cevap

**Kod**:

```python
doc = {"name": "Piko", "level": 3, "club": "mavi"}
for query in [{"level": 3}, {"level": 3, "club": "mavi"}, {"level": 4}, {}]:
    ok = all(doc.get(k) == v for k, v in query.items())
    print(query, "->", ok)
```

**Çıktı:**

```text
{'level': 3} -> True
{'level': 3, 'club': 'mavi'} -> True
{'level': 4} -> False
{} -> True
```

**Maskot:** mutlu pozu, sol

## Sahne 8: kod (13 sn)

**Seslendirme:** Güncelleme için Piko'yu bulup update ile yeni değerleri yazıyorum. break de ilk eşleşmeden sonra aramayı bitiriyor, tıpkı update_one gibi.

**Ekranda başlık:** Güncelleme

**Kod** (vurgulanan satırlar: 4, 5):

```python
players = [{"name": "Piko", "level": 3}, {"name": "Ece", "level": 5}]
for p in players:
    if p["name"] == "Piko":
        p.update({"level": 4})
        break
print(players)
```

**Çıktı:**

```text
[{'name': 'Piko', 'level': 4}, {'name': 'Ece', 'level': 5}]
```

**Maskot:** isaret pozu, sag

## Sahne 9: hata (12 sn)

**Seslendirme:** Sık hata: bazı belgelerde olmayan bir alanı köşeli parantezle okumak. Belgelerin alanları farklı olabilir, Python KeyError verir. Güvenli okumak için get kullan.

**Ekranda başlık:** Sık hata: eksik alan

**Kod** (vurgulanan satırlar: 3):

```python
players = [{"name": "Piko", "level": 3}, {"name": "Can"}]
for p in players:
    print(p["name"], p["level"])
```

**Çıktı:**

```text
Piko 3
KeyError: 'level'
```

**Maskot:** uzgun pozu, sol

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görevlerde kendi insert_one, find ve update_one fonksiyonlarını yazacaksın. Yani MongoDB'nin içini sen kuruyorsun! Projede de oyuncu ekleyip seviye atlatıyorsun.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: insert_one
- Görev 2: find
- Görev 3: update_one
- Challenge: $gt işareti
- Proje: Oyuncu veritabanı

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** Özetle: MongoDB'de belgeler sözlük gibidir ve koleksiyonlarda toplanır. Sorguyla bulunur, update ile güncellenir, delete ile silinir.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- Belge ve koleksiyon
- insert, find, update, delete
- Sorgu eşleşmesi: all()

**Maskot:** on pozu, sag

## Sahne 12: kapanis (12 sn)

**Seslendirme:** Kütüphanenin yeni ustası sensin! Yarın kamp evindeki telsize geçiyoruz. Programların birbiriyle konuştuğu API'leri ve JSON yanıtlarını okumayı öğreneceğiz. Görüşürüz!

**Ekranda başlık:** Yarın: API kullanmak

**Ekranda maddeler:**

- API nedir?
- JSON ve durum kodları

**Maskot:** tebrik pozu, orta
