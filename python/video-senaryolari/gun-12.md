# Video senaryosu: Gün 12, Modüller

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~123 sn

Piko, atölyenin alet dolabını açıyor: import ile modül kullanmak, math ve random modülleri, from ve as ile içe aktarmak ve kendi modülünü yazma fikri.

Ders metni: [gun-12.md](../gunler/gun-12.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | mutlu (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 14 sn | konusma (sag) |
| 4 | kod | 14 sn | isaret (sag) |
| 5 | anlatim | 12 sn | on (sol) |
| 6 | hata | 12 sn | sasirma (sag) |
| 7 | soru | 8 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 12 sn | isaret (sol) |
| 10 | ozet | 6 sn | on (sag) |
| 11 | kapanis | 9 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Piko! Atölyenin duvarında dev bir alet dolabı var. Her çekmecede başka ustaların yaptığı aletler duruyor: hesap aletleri, zar ve kura aletleri. Python'da bu çekmecelere modül denir. Hadi açalım!

**Ekranda başlık:** Gün 12: Modüller

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Dolabın çekmeceleri tek tek açılır: math, random.*

## Sahne 2: kod (14 sn)

**Seslendirme:** Modül, fonksiyonlarla dolu bir Python dosyası. import ile projene alırsın. Sonra modülün adı, nokta ve aletin adı: karekök, pi sayısı, aşağı ve yukarı yuvarlama. Python bu modüllerle birlikte gelir.

**Ekranda başlık:** import math

**Kod** (vurgulanan satırlar: 1, 3):

```python
import math

print(math.sqrt(49))
print(round(math.pi, 4))
print(math.floor(4.7), math.ceil(4.2))
```

**Çıktı:**

```text
7.0
3.1416
4 5
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (14 sn)

**Seslendirme:** Oyunların sürprizleri random modülünden gelir. randint iki sayı arasında, ikisi de dahil, rastgele bir tam sayı verir. choice listeden birini seçer, shuffle listeyi karıştırır. Her çalıştırmada sonuç değişir!

**Ekranda başlık:** random: şans aletleri

**Kod** (vurgulanan satırlar: 3, 5, 6):

```python
import random

print("Zar:", random.randint(1, 6))
friends = ["Ali", "Ece", "Can", "Zeynep"]
print("Kurada çıkan:", random.choice(friends))
random.shuffle(friends)
print("Karışık sıra:", friends)
```

**Çıktı:**

```text
Zar: 4
Kurada çıkan: Ece
Karışık sıra: ['Can', 'Ali', 'Zeynep', 'Ece']
```

**Maskot:** konusma pozu, sag

*Yönetmen notu: Kod üç kez çalıştırılır; her seferinde farklı bir çıktı belirir. Gösterilen çıktı bir örnektir.*

## Sahne 4: kod (14 sn)

**Seslendirme:** from ile çekmeceden sadece istediğin aleti alırsın; artık başına math yazmana gerek yok. as ile uzun isimleri kısaltırsın. seed sabit olunca rastgele sayı her seferinde aynı çıkar.

**Ekranda başlık:** from, as ve seed

**Kod** (vurgulanan satırlar: 1, 2, 6):

```python
from math import sqrt, pi
import random as rnd

print(sqrt(144))
print(pi)
rnd.seed(7)
print(rnd.randint(1, 100))
```

**Çıktı:**

```text
12.0
3.141592653589793
42
```

**Maskot:** isaret pozu, sag

## Sahne 5: anlatim (12 sn)

**Seslendirme:** Kendi modülünü de yazabilirsin. Bilgisayarında araclar.py adında bir dosya yaparsan, aynı klasördeki başka bir dosyada import araclar diyerek fonksiyonlarını kullanırsın. Büyük projeler böyle düzenlenir.

**Ekranda başlık:** Kendi modülün

**Ekranda maddeler:**

- araclar.py: kendi fonksiyonların
- Aynı klasörde: import araclar
- Büyük projeler parçalara böyle ayrılır

**Maskot:** on pozu, sol

## Sahne 6: hata (12 sn)

**Seslendirme:** import math dedik ama sqrt'yi tek başına yazdık. Python NameError veriyor: sqrt'yi tanımıyor. Ya math nokta sqrt yaz, ya da from ile sqrt'yi doğrudan al.

**Ekranda başlık:** Modül adı unutulunca

**Kod** (vurgulanan satırlar: 2):

```python
import math
print(sqrt(16))
```

**Çıktı:**

```text
NameError: name 'sqrt' is not defined
```

**Maskot:** sasirma pozu, sag

## Sahne 7: soru (8 sn)

**Seslendirme:** Biri aşağı, biri yukarı yuvarlıyor. Sence bu toplam kaç eder?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```python
import math
print(math.floor(7.9) + math.ceil(7.1))
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** On beş! floor yedi noktayı dokuzu yediye indirdi, ceil yedi nokta biri sekize çıkardı. Yedi artı sekiz, on beş.

**Ekranda başlık:** Cevap

**Kod**:

```python
import math
print(math.floor(7.9) + math.ceil(7.1))
```

**Çıktı:**

```text
15
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (12 sn)

**Seslendirme:** Görevlerde math ile bir karenin kenarını bulacak, random ile zar atacak ve hazine listesinden rastgele bir ödül seçeceksin. Challenge'da pi sayısıyla bir dairenin alanını hesaplayacaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Karekök
- Görev 2: Zar at
- Görev 3: Rastgele hazine
- Challenge: Daire alanı

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (6 sn)

**Seslendirme:** Bugün başka ustaların aletlerini projemize aldık ve oyunumuza şans kattık.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- import modul ile al, modul.alet ile kullan
- math: sqrt, pi, floor, ceil; random: randint, choice, shuffle
- from ... import ve as ile kısa yaz; seed ile tekrarla

**Maskot:** on pozu, sag

## Sahne 11: kapanis (9 sn)

**Seslendirme:** Alet dolabı artık senin! Yarın atölyenin köşesindeki sihirli kalıbı çalıştıracağız: dört satırlık döngüleri tek satıra sığdıran list comprehension.

**Ekranda başlık:** Yarın: List comprehension

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** tebrik pozu, orta
