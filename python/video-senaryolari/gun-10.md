# Video senaryosu: Gün 10, Döngüler

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~125 sn

Piko, Mantık Kalesi'nin kulesinde while ve for döngülerini anlatıyor: range(), listelerde gezinmek, enumerate, break, continue ve sonsuz döngü tuzağı.

Ders metni: [gun-10.md](../gunler/gun-10.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | konusma (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 12 sn | konusma (sag) |
| 4 | kod | 12 sn | mutlu (sag) |
| 5 | kod | 12 sn | isaret (sag) |
| 6 | soru | 10 sn | dusunme (sag) |
| 7 | cikti | 10 sn | mutlu (sag) |
| 8 | hata | 12 sn | uzgun (sag) |
| 9 | gorev | 14 sn | isaret (sol) |
| 10 | ozet | 8 sn | on (sag) |
| 11 | kapanis | 9 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Piko! Mantık Kalesi'nin kulesinde yüz basamak var. Her basamak için ayrı print yazsaydık parmaklarımız yorulurdu! Bilgisayarlar tekrar eden işleri hiç sıkılmadan yapar. Bugün döngüleri öğreniyoruz.

**Ekranda başlık:** Gün 10: Döngüler

**Görsel:** `gorseller/python/harita/kale.webp`

**Maskot:** konusma pozu, sag

*Yönetmen notu: Kulenin sarmal merdiveni yukarı doğru uzar.*

## Sahne 2: kod (14 sn)

**Seslendirme:** while, koşul doğru oldukça içindeki kodu tekrar tekrar çalıştırır. Her turda sayı bir azalıyor. Beş, dört, üç, iki, bir... ve sıfıra gelince koşul yanlış olur, döngü biter.

**Ekranda başlık:** while: koşul doğru oldukça

**Kod** (vurgulanan satırlar: 2, 4):

```python
count = 5
while count > 0:
    print(count)
    count -= 1
print("Kalk!")
```

**Çıktı:**

```text
5
4
3
2
1
Kalk!
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (12 sn)

**Seslendirme:** Belli sayıda tekrar için for ve range kullanılır. range bir, dört dediğinde dört dahil değil. Üçüncü sayı ise adım: ikişer ikişer sayar.

**Ekranda başlık:** for ve range()

**Kod** (vurgulanan satırlar: 1, 3):

```python
for i in range(1, 4):
    print("Tur", i)
print(list(range(0, 10, 2)))
```

**Çıktı:**

```text
Tur 1
Tur 2
Tur 3
[0, 2, 4, 6, 8]
```

**Maskot:** konusma pozu, sag

## Sahne 4: kod (12 sn)

**Seslendirme:** Birden yüze kadar sayıları elle toplamak ne kadar sürerdi? Python her turda sayıyı toplama ekliyor ve göz açıp kapayıncaya kadar bitiriyor.

**Ekranda başlık:** Toplama makinesi

**Kod** (vurgulanan satırlar: 3):

```python
total = 0
for n in range(1, 101):
    total += n
print("1'den 100'e toplam:", total)
```

**Çıktı:**

```text
1'den 100'e toplam: 5050
```

**Maskot:** mutlu pozu, sag

## Sahne 5: kod (12 sn)

**Seslendirme:** for bir listenin her elemanını sırayla verir. enumerate yanına sıra numarasını da ekler. break ise döngüden hemen çıkar: harita bulununca anahtara hiç bakılmadı.

**Ekranda başlık:** Listede gezinmek ve break

**Kod** (vurgulanan satırlar: 2, 6):

```python
bag = ["kılıç", "iksir", "harita", "anahtar"]
for i, item in enumerate(bag, 1):
    print(f"{i}. {item}")
    if item == "harita":
        print("Harita bulundu, aramayı bırakıyorum.")
        break
```

**Çıktı:**

```text
1. kılıç
2. iksir
3. harita
Harita bulundu, aramayı bırakıyorum.
```

**Maskot:** isaret pozu, sag

## Sahne 6: soru (10 sn)

**Seslendirme:** continue bu turu atlar ve sıradakine geçer. Peki break ve continue birlikteyken bu kod hangi sayıları yazdırır?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```python
for n in range(1, 10):
    if n == 5:
        break
    if n % 2 == 0:
        continue
    print(n)
```

**Maskot:** dusunme pozu, sag

## Sahne 7: cikti (10 sn)

**Seslendirme:** Bir ve üç! Çift sayılarda continue turu atladı. Beşe gelince de break döngüyü bitirdi, yani beş bile yazılmadı.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 3, 5):

```python
for n in range(1, 10):
    if n == 5:
        break
    if n % 2 == 0:
        continue
    print(n)
```

**Çıktı:**

```text
1
3
```

**Maskot:** mutlu pozu, sag

## Sahne 8: hata (12 sn)

**Seslendirme:** En sık hata: koşulu değiştirmeyi unutmak. count hep üç kalır, koşul hep doğru olur ve döngü hiç bitmez. Buna sonsuz döngü denir; bu sitede altı saniye sonra durdurulur.

**Ekranda başlık:** Sonsuz döngü

**Kod** (vurgulanan satırlar: 2):

```python
count = 3
while count > 0:
    print(count)
```

**Çıktı:**

```text
3
3
3
3
...
```

**Maskot:** uzgun pozu, sag

*Yönetmen notu: Çıktı penceresi durmadan 3 yazarak kayar, sonra 'durduruldu' uyarısı belirir.*

## Sahne 9: gorev (14 sn)

**Seslendirme:** Görevlerde while ile geri sayacak, bir sayının çarpım tablosunu yazdıracak ve altınları sum kullanmadan toplayacaksın. Sahne görevinde bir Piko piramidi kuracaksın. Challenge'da da üçe ve beşe bölünen sayılara özel isimler vereceksin.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Geri sayım
- Görev 2: Çarpım tablosu
- Görev 3: Altınları topla
- Sahne görevi: Piko piramidi
- Challenge: PiKo sayıları

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (8 sn)

**Seslendirme:** Bugün tekrar eden işleri döngülere yaptırdık. Yüz basamak da olsa bin basamak da olsa, artık tek bir döngü yeter.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- while: koşul doğru oldukça; koşulu değiştirmeyi unutma
- for + range(başla, bitir, adım)
- enumerate sıra numarası verir; break çıkar, continue atlar

**Maskot:** on pozu, sag

## Sahne 11: kapanis (9 sn)

**Seslendirme:** Kule fethedildi, tebrikler! Yarın Alet Atölyesi'ne gidiyoruz. Bir kez yazıp istediğin kadar kullanabileceğin kendi aletlerini, yani fonksiyonlarını yapacaksın.

**Ekranda başlık:** Yarın: Fonksiyonlar

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** tebrik pozu, orta

*Yönetmen notu: Harita kaleden atölyeye doğru kayar.*
