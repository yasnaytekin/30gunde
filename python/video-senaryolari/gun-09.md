# Video senaryosu: Gün 9, Koşullar

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~124 sn

Piko, Mantık Kalesi'nin kapısında programa karar vermeyi öğretiyor: if, elif, else, girinti kuralları ve koşulları and, or, in ile birleştirmek.

Ders metni: [gun-09.md](../gunler/gun-09.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | konusma (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 14 sn | konusma (sag) |
| 4 | anlatim | 10 sn | on (sol) |
| 5 | kod | 14 sn | konusma (sag) |
| 6 | hata | 12 sn | sasirma (sag) |
| 7 | soru | 9 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 13 sn | isaret (sol) |
| 10 | ozet | 8 sn | on (sag) |
| 11 | kapanis | 8 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Piko! Mantık Kalesi'ne vardık. Kalenin kapısı sadece anahtarı olanlara açılır! Oyunlarda her şey kurallarla çalışır: can biterse oyun biter. Bugün bu kuralları Python'a yazıyoruz.

**Ekranda başlık:** Gün 9: Koşullar

**Görsel:** `gorseller/python/harita/kale.webp`

**Maskot:** konusma pozu, sag

*Yönetmen notu: Kalenin büyük kapısına yakınlaşma; kilidin üstünde bir anahtar deliği.*

## Sahne 2: kod (14 sn)

**Seslendirme:** if, eğer demek. Koşul True ise altındaki satır çalışır. else ise değilse demek. İki şeye dikkat: satır sonundaki iki nokta ve dört boşluk girinti. Anahtar yoksa ne olurdu? Kapı kilitli kalırdı.

**Ekranda başlık:** if ve else

**Kod** (vurgulanan satırlar: 2, 4):

```python
has_key = True
if has_key:
    print("Kapı açıldı!")
else:
    print("Kapı kilitli.")
```

**Çıktı:**

```text
Kapı açıldı!
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (14 sn)

**Seslendirme:** Birden fazla durum varsa elif kullanırız: değilse eğer. Python yukarıdan aşağı bakar ve ilk doğru olan bloğu çalıştırır. Kırk beş, yetmişten büyük değil ama otuzdan büyük.

**Ekranda başlık:** elif: değilse eğer

**Kod** (vurgulanan satırlar: 4, 5):

```python
hp = 45
if hp > 70:
    print("Güçlüsün")
elif hp > 30:
    print("Dikkatli ol")
else:
    print("İksir iç!")
```

**Çıktı:**

```text
Dikkatli ol
```

**Maskot:** konusma pozu, sag

## Sahne 4: anlatim (10 sn)

**Seslendirme:** Girinti Python için çok önemli. Hangi satırların if'e ait olduğunu boşluklara bakarak anlar. Editörde iki nokta yazıp Enter'a basınca girinti kendiliğinden gelir.

**Ekranda başlık:** Blok kuralları

**Ekranda maddeler:**

- Koşul satırı : ile biter
- Blok 4 boşluk içeride
- İlk doğru olan blok çalışır, gerisi atlanır

**Maskot:** on pozu, sol

## Sahne 5: kod (14 sn)

**Seslendirme:** Koşulları and, or ve not ile birleştirebilirsin. Burada ikisi de doğru olmalı: yaş on üç ya da daha büyük ve yirmiden küçük. Girdi kutusuna farklı yaşlar yazıp dene.

**Ekranda başlık:** Koşulları birleştir

**Kod** (vurgulanan satırlar: 2):

```python
age = int(input("Kaç yaşındasın? "))
if age >= 13 and age < 20:
    print("Sen bir gençsin!")
else:
    print("Yaşın:", age)
```

**Çıktı:**

```text
Kaç yaşındasın? 15
Sen bir gençsin!
```

**Maskot:** konusma pozu, sag

*Yönetmen notu: Girdi kutusuna 15 yazılır.*

## Sahne 6: hata (12 sn)

**Seslendirme:** İki noktayı unutmak en sık hata. Python SyntaxError diyor ve ne beklediğini bile söylüyor: iki nokta! Girintiyi unutursan da IndentationError alırsın.

**Ekranda başlık:** Unutulan iki nokta

**Kod** (vurgulanan satırlar: 2):

```python
hp = 45
if hp > 30
    print("Dikkatli ol")
```

**Çıktı:**

```text
SyntaxError: expected ':'
```

**Maskot:** sasirma pozu, sag

## Sahne 7: soru (9 sn)

**Seslendirme:** Listelerle de koşul yazabilirsin. Çantada anahtar yok ama kılıç var. Sence bu kod ne yazdırır?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```python
inventory = ["kılıç", "iksir"]
if "anahtar" in inventory:
    print("Kapıyı aç")
elif "kılıç" in inventory:
    print("Savaşa hazır")
else:
    print("Eli boş")
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Savaşa hazır! İlk koşul yanlıştı, çünkü anahtar yok. İkinci koşul doğru çıktı ve Python else'e hiç bakmadı.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 4, 5):

```python
inventory = ["kılıç", "iksir"]
if "anahtar" in inventory:
    print("Kapıyı aç")
elif "kılıç" in inventory:
    print("Savaşa hazır")
else:
    print("Eli boş")
```

**Çıktı:**

```text
Savaşa hazır
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (13 sn)

**Seslendirme:** Görevlerde kalenin kapısını açacak, bir can göstergesi kuracak ve hazine sandığı için iki koşulu birleştireceksin. Sahne görevinde can, kalplerle görünecek. Challenge'da da yaşa göre oyun modu seçeceksin.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Kalenin kapısı
- Görev 2: Can göstergesi
- Görev 3: Hazine sandığı
- Sahne görevi: Can göstergesi
- Challenge: Oyun modu

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (8 sn)

**Seslendirme:** Bugün programımıza karar vermeyi öğrettik. Artık kurallara göre farklı yollar seçebiliyor, tıpkı bir oyun gibi.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- if, elif, else: ilk doğru olan blok çalışır
- Satır sonunda :, blok 4 boşluk içeride
- and, or, not ve in ile koşul birleştir

**Maskot:** on pozu, sag

## Sahne 11: kapanis (8 sn)

**Seslendirme:** Kalenin kapısı açıldı! Yarın kalenin yüz basamaklı kulesine tırmanacağız. Tekrar eden işleri bilgisayara yaptıran döngüleri öğreneceğiz.

**Ekranda başlık:** Yarın: Döngüler

**Görsel:** `gorseller/python/harita/kale.webp`

**Maskot:** tebrik pozu, orta
