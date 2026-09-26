# Video senaryosu: Gün 30, Final ve sonrası

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~172 sn

Piko, Python Dağı'nın zirvesinde 30 günlük yolculuğu bölge bölge özetliyor, öğrenilenleri tek bir oyunda birleştiriyor, final görevlerini tanıtıyor ve kursu kutlamayla kapatıyor.

Ders metni: [gun-30.md](../gunler/gun-30.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | tebrik (sag) |
| 2 | anlatim | 17 sn | mutlu (sol) |
| 3 | anlatim | 16 sn | isaret (sag) |
| 4 | kod | 16 sn | isaret (sol) |
| 5 | soru | 12 sn | dusunme (sag) |
| 6 | cikti | 12 sn | mutlu (sol) |
| 7 | hata | 11 sn | sasirma (sag) |
| 8 | anlatim | 14 sn | konusma (sag) |
| 9 | anlatim | 16 sn | isaret (sol) |
| 10 | gorev | 16 sn | konusma (sag) |
| 11 | ozet | 12 sn | on (sag) |
| 12 | kapanis | 16 sn | tebrik (orta) |

## Sahne 1: acilis (14 sn)

**Seslendirme:** Selam, ben Piko! Başardın, Python Dağı'nın zirvesindeyiz! Buradan geriye bak: ilk print'ten kendi API'ne kadar uzun bir yol yürüdün. Ben çok gururluyum. Son bir macera kaldı: her şeyi tek bir oyunda birleştirmek!

**Ekranda başlık:** Gün 30: Final ve sonrası

**Ekranda maddeler:**

- Python Dağı: zirve
- Hepsini birleştirme zamanı

**Maskot:** tebrik pozu, sag

*Yönetmen notu: Arka plan: Python Dağı bölge görseli (gorseller/python/harita/dag.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Kamera zirveden aşağı, 30 günlük yola doğru döner; konfeti.*

## Sahne 2: anlatim (17 sn)

**Seslendirme:** Hadi yolu hatırlayalım. Başlangıç Kampı'nda print ve değişkenleri, Köy'de operatör ve stringleri öğrendin. Veri Ormanı'nda liste, tuple, set ve sözlük, Mantık Kalesi'nde koşul ve döngüler. Alet Atölyesi'nde de fonksiyonlar ve modüller vardı.

**Ekranda başlık:** Yolun ilk yarısı

**Ekranda maddeler:**

- Kamp: print, değişkenler
- Köy: operatörler, stringler
- Orman: liste, tuple, set, sözlük
- Kale: koşullar, döngüler
- Atölye: fonksiyonlar, modüller, lambda, hatalar

**Görsel:** `gorseller/python/harita/kamp.webp`

**Maskot:** mutlu pozu, sol

*Yönetmen notu: Harita bölgeleri sırayla parlar: kamp, köy, orman, kale, atölye.*

## Sahne 3: anlatim (16 sn)

**Seslendirme:** Keşif Adası'nda tarihleri, try except'i, düzenli ifadeleri ve dosyaları öğrendin. Bilgi Limanı'nda sınıflar, web kazıma, NumPy ve pandas. Python Dağı'nda da web, veritabanı ve API. Bu, gerçek programcıların alet çantası!

**Ekranda başlık:** Yolun ikinci yarısı

**Ekranda maddeler:**

- Ada: tarih, try/except, regex, dosyalar, pip
- Liman: sınıflar, web kazıma, venv, NumPy, pandas
- Dağ: web, MongoDB, API kullanmak ve yapmak

**Maskot:** isaret pozu, sag

*Yönetmen notu: Ada, liman ve dağ bölgeleri parlar; görseller eklenince buraya konmalı.*

## Sahne 4: kod (16 sn)

**Seslendirme:** İşte hepsi bir arada: bir sınıf, tekrarsız eşyalar için bir set, bir döngü ve f-string. Harita iki kez alındı ama set sayesinde çantada bir tane var. sorted da çantayı alfabetik diziyor.

**Ekranda başlık:** Hepsi bir arada

**Kod** (vurgulanan satırlar: 4, 7, 13):

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.bag = set()

    def pick(self, item):
        self.bag.add(item)
        return f"{self.name} {item} aldı."

piko = Hero("Piko")
for item in ["harita", "anahtar", "harita"]:
    print(piko.pick(item))
print("Çanta:", sorted(piko.bag))
```

**Çıktı:**

```text
Piko harita aldı.
Piko anahtar aldı.
Piko harita aldı.
Çanta: ['anahtar', 'harita']
```

**Maskot:** isaret pozu, sol

## Sahne 5: soru (12 sn)

**Seslendirme:** Final macerasının kalbi bir oda haritası: iç içe sözlükler. Piko kamptan başlıyor ve kuzey, doğu, kuzey yönlerine gitmeye çalışıyor. Sence nerede durur?

**Ekranda başlık:** Sence ne yazdırır?

**Kod** (vurgulanan satırlar: 7, 8):

```python
rooms = {
    "kamp": {"kuzey": "orman"},
    "orman": {"güney": "kamp", "doğu": "mağara"},
    "mağara": {"batı": "orman"},
}
place = "kamp"
for step in ["kuzey", "doğu", "kuzey"]:
    if step in rooms[place]:
        place = rooms[place][step]
        print("Şimdi buradasın:", place)
    else:
        print("Oraya gidemezsin!")
```

**Maskot:** dusunme pozu, sag

## Sahne 6: cikti (12 sn)

**Seslendirme:** Önce ormana, sonra mağaraya gitti. Mağaranın kuzeyinde çıkış yok, o yüzden Oraya gidemezsin dedi. Sözlük, döngü ve koşul el ele!

**Ekranda başlık:** Cevap

**Kod**:

```python
rooms = {
    "kamp": {"kuzey": "orman"},
    "orman": {"güney": "kamp", "doğu": "mağara"},
    "mağara": {"batı": "orman"},
}
place = "kamp"
for step in ["kuzey", "doğu", "kuzey"]:
    if step in rooms[place]:
        place = rooms[place][step]
        print("Şimdi buradasın:", place)
    else:
        print("Oraya gidemezsin!")
```

**Çıktı:**

```text
Şimdi buradasın: orman
Şimdi buradasın: mağara
Oraya gidemezsin!
```

**Maskot:** mutlu pozu, sol

## Sahne 7: hata (11 sn)

**Seslendirme:** En iyi öğretmenin hâlâ hata mesajları. Burada score yerine scroe yazdım, Python NameError veriyor ve hangi ismi tanımadığını söylüyor. Hatayı oku, düzelt, devam et!

**Ekranda başlık:** Hataları oku

**Kod** (vurgulanan satırlar: 2):

```python
score = 100
print(scroe)
```

**Çıktı:**

```text
NameError: name 'scroe' is not defined. Did you mean: 'score'?
```

**Maskot:** sasirma pozu, sag

## Sahne 8: anlatim (14 sn)

**Seslendirme:** Bundan sonra da işine yarayacak alışkanlıklar: küçük adımlarla ilerle, anlamlı isimler seç, tekrar eden kodu fonksiyona çevir ve takıldığında sormaktan çekinme.

**Ekranda başlık:** İyi programcı alışkanlıkları

**Ekranda maddeler:**

- Küçük adımlarla ilerle
- x yerine score, f yerine move_player
- Hata mesajlarını oku
- Tekrar eden kodu fonksiyona çevir
- Takıldığında sor

**Maskot:** konusma pozu, sag

## Sahne 9: anlatim (16 sn)

**Seslendirme:** Peki şimdi ne olacak? pygame ile grafikli oyunlar, Flask ile kendi siten, pandas ile veri hikâyeleri, sıkıcı işleri yapan otomasyonlar, hatta yapay zekâ. Kendi bilgisayarına Python kur ve projelerini orada da çalıştır.

**Ekranda başlık:** Bundan sonra ne yapabilirsin?

**Ekranda maddeler:**

- Oyun: pygame
- Web: Flask
- Veri: pandas ve grafikler
- Otomasyon
- Yapay zekâ
- Python kur: python.org

**Maskot:** isaret pozu, sol

## Sahne 10: gorev (16 sn)

**Seslendirme:** Son görevlerde sesli harf sayacı, kelime sayacı ve bir sayaç sınıfı yazacaksın. Final projesinde Piko odalar arasında dolaşıp eşya toplayacak ve anahtarla hazine kapısını açacak. Sonra Proje sayfasında Oyunumu oyna'ya bas!

**Ekranda başlık:** Son görevler

**Ekranda maddeler:**

- Görev 1: Sesli harf sayacı
- Görev 2: Kelime sayacı
- Görev 3: Sayaç sınıfı
- Challenge: Komut motoru
- Proje: Final macerası
- Sonra: Oyunumu oyna ve sertifikanı al

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (12 sn)

**Seslendirme:** Otuz günün özeti: temelleri kurdun, verini düzenledin, programına karar verdirdin ve onu gerçek dünyaya bağladın.

**Ekranda başlık:** 30 günün özeti

**Ekranda maddeler:**

- Temeller ve veri yapıları
- Koşullar, döngüler, fonksiyonlar, sınıflar
- Dosyalar, paketler, veri, web ve API

**Maskot:** on pozu, sag

## Sahne 12: kapanis (16 sn)

**Seslendirme:** İşte bu kadar! Otuz günü bitirdin ve artık bir Python programcısısın. Tüm parçaların tek bir oyunda birleşti. Seninle bu yolu yürümek harikaydı. Sertifikanı al, kodlamaya devam et ve yeni maceralarda görüşmek üzere!

**Ekranda başlık:** Tebrikler, Python programcısı!

**Ekranda maddeler:**

- 30 gün tamam
- Final projesi rozeti

**Görsel:** `gorseller/python/rozetler/final-projesi.webp`

**Maskot:** tebrik pozu, orta

*Yönetmen notu: Final projesi rozeti ortada parlar, konfeti yağar, Piko el sallayarak kutlar.*
