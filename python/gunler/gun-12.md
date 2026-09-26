# Gün 12: Modüller

**Kurs:** 30 Günde Python  ·  **Bölge:** Alet Atölyesi  ·  **Maskot:** Piko

**Bugünün hedefi:** Hazır modülleri içe aktarmak ve math ile random modüllerini kullanmak

> Atölyenin duvarında dev bir alet dolabı var. Her çekmecede başka ustaların yaptığı aletler duruyor: biri hesap aletleri, biri zar ve kura aletleri... Python'da bu çekmecelere **modül** denir. Bugün çekmeceleri açıyoruz!

![Alet Atölyesi](../../gorseller/python/harita/atolye.webp)

## Konu anlatımı

### Modül nedir?

Modül, başka birinin (ya da senin) yazdığı fonksiyonlarla dolu bir Python dosyasıdır. `import` ile projene alırsın:

```python
import math
print(math.sqrt(49))   # 7.0
```

Python kurulurken yanında yüzlerce modülle gelir. Buna **standart kütüphane** denir.

### math: hesap aletleri

- `math.sqrt(x)` karekök
- `math.pi` pi sayısı (3.14159...)
- `math.floor(4.7)` aşağı yuvarlar: 4
- `math.ceil(4.2)` yukarı yuvarlar: 5
- `math.pow(2, 3)` üs alır: 8.0

### random: şans aletleri

Oyunların sürprizleri buradan gelir:

- `random.randint(1, 6)` 1 ile 6 arasında (ikisi dahil) rastgele tam sayı
- `random.choice(liste)` listeden rastgele bir eleman
- `random.shuffle(liste)` listeyi karıştırır
- `random.random()` 0 ile 1 arasında rastgele ondalıklı sayı

Her çalıştırmada farklı sonuç çıkar. Aynı sonuçları tekrar görmek istersen başta `random.seed(42)` yazabilirsin.

### from, as ve kendi modülün

Sadece bir parçayı almak için `from` kullanılır, uzun isimleri kısaltmak için `as`:

```python
from math import pi, sqrt
import random as rnd
print(pi, sqrt(16), rnd.randint(1, 3))
```

Kendi bilgisayarında `araclar.py` adında bir dosya yazarsan, aynı klasördeki başka bir dosyada `import araclar` diyerek onun fonksiyonlarını kullanabilirsin. Büyük projeler böyle düzenlenir.

## Örnekler

### Hesap aletleri

```python
import math

print(math.sqrt(81))
print(round(math.pi, 4))
print(math.floor(4.7), math.ceil(4.2))
```

### Zar ve kura

```python
import random

print("Zar:", random.randint(1, 6))
friends = ["Ali", "Ece", "Can", "Zeynep"]
print("Kurada çıkan:", random.choice(friends))
random.shuffle(friends)
print("Karışık sıra:", friends)
```

*Birkaç kez çalıştır, sonuçlar değişiyor mu?*

### from ve as

```python
from math import sqrt, pi
import random as rnd

print(sqrt(144))
print(pi)
rnd.seed(7)
print(rnd.randint(1, 100))
```

*seed sabit olduğu için sayı her seferinde aynı çıkar.*

## Görevler

### Görev 1: Karekök

`math` modülünü kullanarak `area`'nın karekökünü bul ve `side` değişkenine koy.

**Başlangıç kodu:**

```python
area = 81

# math modülünü içe aktar ve side'ı hesapla
side = 0

print("Bir kenar:", side)
```

**İpuçları:**

1. En üste import math yaz.
2. Karekök: math.sqrt(area)

<details><summary>Çözüm</summary>

```python
import math

area = 81

side = math.sqrt(area)

print("Bir kenar:", side)
```

</details>

### Görev 2: Zar at

`random` modülüyle 1 ile 6 arasında bir zar at, sonucu `dice` değişkenine koy ve `Zar: 4` gibi yazdır.

**Başlangıç kodu:**

```python
# random modülünü içe aktar

dice = 1

print(f"Zar: {dice}")
```

**İpuçları:**

1. import random
2. random.randint(1, 6) hem 1'i hem 6'yı içerir.

<details><summary>Çözüm</summary>

```python
import random

dice = random.randint(1, 6)

print(f"Zar: {dice}")
```

</details>

### Görev 3: Rastgele hazine

`treasures` listesinden rastgele bir hazine seç ve `prize` değişkenine koy.

**Başlangıç kodu:**

```python
import random

treasures = ["altın", "elmas", "harita", "iksir"]

prize = treasures[0]

print("Hazine:", prize)
```

**İpuçları:**

1. Listeden rastgele seçmek için random.choice(...)

<details><summary>Çözüm</summary>

```python
import random

treasures = ["altın", "elmas", "harita", "iksir"]

prize = random.choice(treasures)

print("Hazine:", prize)
```

</details>

## Challenge: Daire alanı

`from math import pi` ile pi'yi al. Yarıçapı `radius` olan dairenin alanını hesaplayıp **2 basamağa yuvarla** ve `area` değişkenine koy. Formül: pi x r x r

**Başlangıç kodu:**

```python
radius = 3

# pi'yi math modülünden al

area = 0

print("Alan:", area)
```

**İpuçları:**

1. from math import pi
2. round(sayı, 2) iki basamağa yuvarlar.

<details><summary>Çözüm</summary>

```python
from math import pi

radius = 3

area = round(pi * radius ** 2, 2)

print("Alan:", area)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Rastgele olaylar**

### Piko'nun Macerası: Rastgele olaylar

Macerayı sürprizli yapalım! `random_event()` fonksiyonu `events` listesinden rastgele bir olayı **döndürsün**. `find_gold()` fonksiyonu 5 ile 20 arasında rastgele bir sayı döndürsün.

**Başlangıç kodu:**

```python
import random

events = ["Bir iksir buldun!", "Tuzağa bastın!", "Bir dost geldi!", "Yağmur başladı!"]

def random_event():
    pass

def find_gold():
    pass

print(random_event())
print("Bulunan altın:", find_gold())
```

**İpuçları:**

1. random_event içinde: return random.choice(events)
2. find_gold içinde: return random.randint(5, 20)

<details><summary>Çözüm</summary>

```python
import random

events = ["Bir iksir buldun!", "Tuzağa bastın!", "Bir dost geldi!", "Yağmur başladı!"]

def random_event():
    return random.choice(events)

def find_gold():
    return random.randint(5, 20)

print(random_event())
print("Bulunan altın:", find_gold())
```

</details>

### Harcama Defteri: Günlük harçlık

İki yardımcı fonksiyon yazalım:

- `daily_allowance(left, days)`: kalan parayı kalan günlere böl ve **aşağı yuvarla** (`math.floor`). Gün 0 ise `0` döndür.
- `sample_expenses(n)`: `random.randint` ile 10 ile 500 arasında `n` tane rastgele tutar içeren bir liste döndürsün (programı denemek için).

**Başlangıç kodu:**

```python
import math
import random


def daily_allowance(left, days):
    pass


def sample_expenses(n):
    pass
```

**İpuçları:**

1. math.floor(1100 / 7) 157 verir.
2. random.randint(10, 500) iki sınır dahil rastgele bir tam sayı verir.

<details><summary>Çözüm</summary>

```python
import math
import random


def daily_allowance(left, days):
    if days == 0:
        return 0
    return math.floor(left / days)


def sample_expenses(n):
    result = []
    for _ in range(n):
        result.append(random.randint(10, 500))
    return result
```

</details>

### Görev Asistanı: Rastgele görev seçici

Hangi işe başlayacağına karar veremeyince asistan seçsin:

- `pick_task(tasks)`: listeden **rastgele** bir görev döndürsün (`random.choice`). Liste boşsa `None` döndürsün.
- `focus_blocks(minutes)`: çalışma süresini 25 dakikalık bloklara bölsün ve **yukarı yuvarlayarak** kaç blok gerektiğini döndürsün (`math.ceil`).

**Başlangıç kodu:**

```python
import math
import random


def pick_task(tasks):
    pass


def focus_blocks(minutes):
    pass
```

**İpuçları:**

1. random.choice(liste) rastgele bir eleman verir.
2. math.ceil(60 / 25) 3 verir.

<details><summary>Çözüm</summary>

```python
import math
import random


def pick_task(tasks):
    if not tasks:
        return None
    return random.choice(tasks)


def focus_blocks(minutes):
    return math.ceil(minutes / 25)
```

</details>

### Kişisel Web Sitem: Okuma süresi

İki yardımcı fonksiyon yazalım:

- `reading_time(text, wpm=200)`: yazıdaki kelime sayısını (`len(text.split())`) dakikada okunan kelime sayısına (`wpm`) böl ve **yukarı yuvarla** (`math.ceil`). En az `1` döndürsün (boş yazı için de).
- `pick_featured(titles)`: ana sayfada öne çıkarmak için başlıklardan birini `random.choice` ile rastgele seçip döndürsün.

**Başlangıç kodu:**

```python
import math
import random


def reading_time(text, wpm=200):
    pass


def pick_featured(titles):
    pass
```

**İpuçları:**

1. math.ceil(450 / 200) 3 verir.
2. Sonuç 1'den küçükse 1 döndür. random.choice(titles) listeden rastgele bir eleman verir.

<details><summary>Çözüm</summary>

```python
import math
import random


def reading_time(text, wpm=200):
    minutes = math.ceil(len(text.split()) / wpm)
    if minutes < 1:
        return 1
    return minutes


def pick_featured(titles):
    return random.choice(titles)
```

</details>

### Sohbet Botu: Farklı selamlar

Hep aynı cümleyi söyleyen bot sıkıcıdır! İki yardımcı fonksiyon yazalım:

- `random_greeting()`: `GREETINGS` listesinden **rastgele** bir selam döndürsün (`random.choice`).
- `typing_seconds(message)`: bot cevap yazarken ekranda "yazıyor..." görünsün. Her 20 karakter için 1 saniye say ve **yukarı yuvarla** (`math.ceil`). 45 karakterlik bir cevap 3 saniye sürer.

**Başlangıç kodu:**

```python
import math
import random

GREETINGS = ["Merhaba!", "Selam!", "Hoş geldin!", "Ne var ne yok?"]


def random_greeting():
    pass


def typing_seconds(message):
    pass
```

**İpuçları:**

1. random.choice(liste) listeden rastgele bir eleman verir.
2. math.ceil(45 / 20) 3 verir.

<details><summary>Çözüm</summary>

```python
import math
import random

GREETINGS = ["Merhaba!", "Selam!", "Hoş geldin!", "Ne var ne yok?"]


def random_greeting():
    return random.choice(GREETINGS)


def typing_seconds(message):
    return math.ceil(len(message) / 20)
```

</details>

### Okul Not Defteri: Hedef not

İki yardımcı fonksiyon yazalım:

- `needed_score(average, count, target)`: `count` sınavın ortalaması `average`. Bir sonraki sınavdan kaç alırsan ortalaman `target` olur? Formül: `target * (count + 1) - average * count`. Sonucu `math.ceil` ile **yukarı** yuvarla. 100'den büyükse `None`, 0'dan küçükse `0` döndür.
- `pick_subject(subjects)`: listeden `random.choice` ile rastgele bir ders döndürsün (bugün hangisini çalışsan?).

**Başlangıç kodu:**

```python
import math
import random


def needed_score(average, count, target):
    pass


def pick_subject(subjects):
    pass
```

**İpuçları:**

1. math.ceil(81.1) 82 verir.
2. random.choice(subjects) listeden rastgele bir eleman seçer.

<details><summary>Çözüm</summary>

```python
import math
import random


def needed_score(average, count, target):
    needed = math.ceil(target * (count + 1) - average * count)
    if needed > 100:
        return None
    if needed < 0:
        return 0
    return needed


def pick_subject(subjects):
    return random.choice(subjects)
```

</details>
