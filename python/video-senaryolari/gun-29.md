# Video senaryosu: Gün 29, API yapmak

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~159 sn

Piko, Python Dağı'nın zirvesine yakın bir istasyonda kendi API'mizi kurmayı; HTTP metotlarını, adresleri, durum kodlarını ve (kod, cevap) döndüren fonksiyonları anlatıyor.

Ders metni: [gun-29.md](../gunler/gun-29.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | mutlu (sag) |
| 2 | anlatim | 16 sn | isaret (sol) |
| 3 | kod | 14 sn | isaret (sag) |
| 4 | anlatim | 16 sn | konusma (sag) |
| 5 | anlatim | 14 sn | dusunme (sol) |
| 6 | kod | 15 sn | isaret (sag) |
| 7 | soru | 9 sn | dusunme (sag) |
| 8 | cikti | 11 sn | mutlu (sol) |
| 9 | hata | 12 sn | uzgun (sag) |
| 10 | gorev | 14 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 13 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Gün 29: API yapmak! Bu derste kendi API'ni kurmayı; GET, POST, PUT ve DELETE metotlarını ve doğru durum kodlarını öğreneceksin.

- GET, POST, PUT, DELETE
- Adresi parçalamak
- Doğru durum kodu

## Sahne 1: acilis (14 sn)

**Seslendirme:** Selam, ben Piko! Zirveye çok az kaldı! Dün başka istasyonlara soru sorduk. Bugün soruları cevaplayan istasyon biz oluyoruz. Arkadaşlarının oyunları, skorları senin yazacağın API'den okuyacak. Hazır mısın?

**Ekranda başlık:** Gün 29: API yapmak

**Ekranda maddeler:**

- Python Dağı
- GET, POST, PUT, DELETE

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Arka plan: Python Dağı bölge görseli (gorseller/python/harita/dag.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Zirveye yakın bir istasyon; Piko telsizin başında cevap veriyor.*

## Sahne 2: anlatim (16 sn)

**Seslendirme:** API'ye gelen her isteğin bir metodu vardır ve ne istendiğini söyler. GET veriyi getirir, POST yeni veri ekler, PUT günceller, DELETE siler. Bu dört işleme kısaca CRUD denir.

**Ekranda başlık:** HTTP metotları

**Ekranda maddeler:**

- GET: oku
- POST: ekle
- PUT: güncelle
- DELETE: sil
- CRUD: Create, Read, Update, Delete

**Maskot:** isaret pozu, sol

## Sahne 3: kod (14 sn)

**Seslendirme:** Adresler düzenlidir: players tüm oyuncular, players bölü iki ise iki numaralı oyuncu. Adresi strip ve split ile parçalara ayırınca hangi kaynağın ve hangi kimliğin istendiğini okuyabiliyorum.

**Ekranda başlık:** Adresi parçala

**Kod** (vurgulanan satırlar: 2):

```python
for path in ["/players", "/players/2", "/scores/10"]:
    parts = path.strip("/").split("/")
    print(path, "->", parts)
```

**Çıktı:**

```text
/players -> ['players']
/players/2 -> ['players', '2']
/scores/10 -> ['scores', '10']
```

**Maskot:** isaret pozu, sag

## Sahne 4: anlatim (16 sn)

**Seslendirme:** Gerçek bir API'yi Flask ile yazarsın. route adresi ve metodu seçer, jsonify cevabı JSON'a çevirir, yanına da durum kodu gelir. Burada sunucu çalıştıramadığımız için her fonksiyon durum kodu ve cevap döndürecek.

**Ekranda başlık:** Flask ile gerçek bir API

**Kod** (vurgulanan satırlar: 5, 9):

```python
from flask import Flask, jsonify, request
app = Flask(__name__)
players = []

@app.route("/players", methods=["POST"])
def create_player():
    data = request.get_json()
    players.append(data)
    return jsonify(data), 201
```

**Maskot:** konusma pozu, sag

*Yönetmen notu: Sunucu gerektirdiği için çalıştırılmaz; sadece gerçek kullanımı gösterir.*

## Sahne 5: anlatim (14 sn)

**Seslendirme:** İyi bir API her zaman anlaşılır bir durum kodu döndürür. İki yüz bir yeni kayıt oluştu, iki yüz dört silindi ama gösterilecek bir şey yok, dört yüz ise isteğin eksik ya da hatalı demek.

**Ekranda başlık:** Doğru durum kodu

**Ekranda maddeler:**

- 200 Tamam (GET, PUT)
- 201 Oluşturuldu (POST)
- 204 İçerik yok (DELETE)
- 400 Hatalı istek
- 404 Bulunamadı

**Maskot:** dusunme pozu, sol

## Sahne 6: kod (15 sn)

**Seslendirme:** İşte mini API'mizin POST kısmı. Önce gövdede isim var mı diye bakıyor, yoksa dört yüzle geri çeviriyor. Varsa yeni bir kimlik verip oyuncuyu ekliyor ve iki yüz bir döndürüyor.

**Ekranda başlık:** Mini API: POST

**Kod** (vurgulanan satırlar: 4, 5, 8):

```python
players = [{"id": 1, "name": "Piko"}]

def create_player(body):
    if "name" not in body:
        return 400, {"hata": "isim gerekli"}
    player = {"id": len(players) + 1, "name": body["name"]}
    players.append(player)
    return 201, player
```

**Maskot:** isaret pozu, sag

## Sahne 7: soru (9 sn)

**Seslendirme:** Bu API'ye iki istek gönderiyorum: biri isimli, biri bomboş. Sence ikisine ne cevap gelir?

**Ekranda başlık:** Sence ne yazdırır?

**Kod** (vurgulanan satırlar: 10, 11):

```python
players = [{"id": 1, "name": "Piko"}]

def create_player(body):
    if "name" not in body:
        return 400, {"hata": "isim gerekli"}
    player = {"id": len(players) + 1, "name": body["name"]}
    players.append(player)
    return 201, player

print(create_player({"name": "Ece"}))
print(create_player({}))
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (11 sn)

**Seslendirme:** Ece iki numaralı kimlikle eklendi ve iki yüz bir geldi. Boş istek ise dört yüz aldı, üstelik ne eksik olduğunu söyleyen bir mesajla.

**Ekranda başlık:** Cevap

**Kod**:

```python
players = [{"id": 1, "name": "Piko"}]

def create_player(body):
    if "name" not in body:
        return 400, {"hata": "isim gerekli"}
    player = {"id": len(players) + 1, "name": body["name"]}
    players.append(player)
    return 201, player

print(create_player({"name": "Ece"}))
print(create_player({}))
```

**Çıktı:**

```text
(201, {'id': 2, 'name': 'Ece'})
(400, {'hata': 'isim gerekli'})
```

**Maskot:** mutlu pozu, sol

## Sahne 9: hata (12 sn)

**Seslendirme:** Sık hata: gövdeyi kontrol etmeden doğrudan name alanını okumak. İstekte isim yoksa KeyError alırsın ve API çöker. Önce in ile kontrol et, eksikse dört yüz dön.

**Ekranda başlık:** Sık hata: kontrolsüz gövde

**Kod** (vurgulanan satırlar: 2):

```python
def create_player(body):
    return 201, {"name": body["name"]}

print(create_player({}))
```

**Çıktı:**

```text
KeyError: 'name'
```

**Maskot:** uzgun pozu, sag

## Sahne 10: gorev (14 sn)

**Seslendirme:** Görevlerde tek oyuncuyu getiren bir GET, yeni oyuncu ekleyen bir POST ve oyuncu silen bir DELETE yazacaksın. Projede de Piko'nun Macerası'nın skor API'sini kuruyorsun!

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: GET: tek oyuncu
- Görev 2: POST: yeni oyuncu
- Görev 3: DELETE: oyuncu sil
- Challenge: Yönlendirici
- Proje: Oyun API'si

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** Özetle: metot ne yapılacağını, adres neyin istendiğini söyler; iyi bir API de her isteğe doğru durum koduyla cevap verir.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- GET, POST, PUT, DELETE = CRUD
- Adresi split ile parçala
- 200, 201, 204, 400, 404

**Maskot:** on pozu, sag

## Sahne 12: kapanis (13 sn)

**Seslendirme:** Artık kendi API'ni yazabiliyorsun, inanılmaz! Yarın zirvedeyiz. Otuz günde öğrendiğin her şeyi birleştirip Piko'nun Macerası'nın final sürümünü yazacağız. Sakın kaçırma!

**Ekranda başlık:** Yarın: Final ve sonrası

**Ekranda maddeler:**

- Zirve!
- Final macerası

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** Bu dersin interaktif hâli 30gunde.com.tr'de seni bekliyor. Kodunu tarayıcıda yaz, hemen çalıştır ve görevleri tamamla!

**Ekranda:** İnteraktif dersler için **30gunde.com.tr**

- Kodunu tarayıcıda yaz ve çalıştır
- Görevleri tamamla, rozet kazan
- 30 günde adım adım Python
