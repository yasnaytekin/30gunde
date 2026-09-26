# Gün 13: List comprehension

**Kurs:** 30 Günde Python  ·  **Bölge:** Alet Atölyesi  ·  **Maskot:** Piko

**Bugünün hedefi:** List comprehension ile kısa ve okunaklı listeler üretmek, lambda fonksiyonlarını tanımak

> Atölyenin köşesinde sihirli bir kalıp duruyor: bir tarafından malzemeleri atıyorsun, öbür tarafından hazır ürünler çıkıyor. Python'da buna **list comprehension** denir. Dört satırlık döngüleri tek satıra sığdırır!

![Alet Atölyesi](../../gorseller/python/harita/atolye.webp)

## Konu anlatımı

### Tek satırda liste

Bir listeden yeni bir liste yapmanın uzun yolu:

```python
doubled = []
for n in nums:
    doubled.append(n * 2)
```

List comprehension ile kısa yolu:

```python
doubled = [n * 2 for n in nums]
```

Okurken şöyle düşün: "nums'taki her n için n * 2'yi al."

### Koşullu seçmek

Sona bir `if` ekleyerek sadece istediğin elemanları alabilirsin:

```python
big = [n for n in nums if n > 10]
evens = [n for n in range(20) if n % 2 == 0]
```

### if ve else ile dönüştürmek

Her eleman için iki sonuçtan birini seçmek istersen `if ... else` **başa** yazılır:

```python
labels = ["çift" if n % 2 == 0 else "tek" for n in nums]
```

Aynı fikir sözlük ve set için de var: `{n: n * n for n in range(4)}`

### lambda: isimsiz mini fonksiyon

Tek satırlık küçük fonksiyonları `lambda` ile yazabilirsin:

```python
square = lambda x: x * x
print(square(5))   # 25

add = lambda a, b: a + b
```

`lambda` özellikle yarın göreceğimiz `sorted`, `map` ve `filter` ile çok işe yarar.

## Örnekler

### Uzun yol, kısa yol

```python
nums = [1, 2, 3, 4, 5]

doubled = []
for n in nums:
    doubled.append(n * 2)
print(doubled)

print([n * 2 for n in nums])
```

### Filtrele

```python
scores = [45, 90, 12, 77, 100, 63]
passed = [s for s in scores if s >= 60]
print("Geçenler:", passed)
print(["geçti" if s >= 60 else "kaldı" for s in scores])
```

### lambda

```python
square = lambda x: x * x
add = lambda a, b: a + b
print(square(6))
print(add(2, 3))
print({n: square(n) for n in range(1, 5)})
```

## Görevler

### Görev 1: İki katı

`nums` listesindeki her sayının iki katını içeren `doubled` listesini **list comprehension** ile yap.

**Başlangıç kodu:**

```python
nums = [3, 7, 10]

doubled = []

print(doubled)
```

**İpuçları:**

1. Kalıp: [ifade for n in nums]
2. doubled = [n * 2 for n in nums]

<details><summary>Çözüm</summary>

```python
nums = [3, 7, 10]

doubled = [n * 2 for n in nums]

print(doubled)
```

</details>

### Görev 2: Büyük harfle

`names` listesindeki isimleri büyük harfe çevirip `loud` listesine koy. Tek satırda yap.

**Başlangıç kodu:**

```python
names = ["piko", "ece", "can"]

loud = []

print(loud)
```

**İpuçları:**

1. Büyük harf için .upper()
2. loud = [name.upper() for name in names]

<details><summary>Çözüm</summary>

```python
names = ["piko", "ece", "can"]

loud = [name.upper() for name in names]

print(loud)
```

</details>

### Görev 3: Değerli ganimet

`prices` listesinden sadece 50 veya daha büyük olanları alıp `valuable` listesine koy.

**Başlangıç kodu:**

```python
prices = [120, 5, 60, 49, 300, 1]

valuable = []

print(valuable)
```

**İpuçları:**

1. Sona if ekle: [p for p in prices if ...]

<details><summary>Çözüm</summary>

```python
prices = [120, 5, 60, 49, 300, 1]

valuable = [p for p in prices if p >= 50]

print(valuable)
```

</details>

## Challenge: lambda ile

`square` adında, verilen sayının karesini döndüren bir **lambda** yaz. Sonra `squares` listesi 1'den `n`'ye kadar sayıların karelerini içersin.

**Başlangıç kodu:**

```python
n = 5

square = None

squares = []

print(squares)
```

**İpuçları:**

1. square = lambda x: x * x
2. range(1, n + 1) 1'den n'ye kadar sayılar verir.

<details><summary>Çözüm</summary>

```python
n = 5

square = lambda x: x * x

squares = [square(i) for i in range(1, n + 1)]

print(squares)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Ganimet filtresi**

### Piko'nun Macerası: Ganimet filtresi

Piko'nun çantasındaki eşyalar `(isim, değer)` tuple'ları olarak duruyor. Tek satırlık listelerle:

- `valuable`: değeri 50 veya üstü olan eşyaların **isimleri**
- `total`: tüm eşyaların değerlerinin toplamı (list comprehension ve `sum()` kullanabilirsin)

**Başlangıç kodu:**

```python
loot = [("kılıç", 120), ("taş", 1), ("iksir", 60), ("ip", 8)]

valuable = []
total = 0

print("Değerli:", valuable)
print("Toplam değer:", total)
```

**İpuçları:**

1. Tuple'ları döngüde açabilirsin: for name, price in loot
2. total = sum([price for name, price in loot])

<details><summary>Çözüm</summary>

```python
loot = [("kılıç", 120), ("taş", 1), ("iksir", 60), ("ip", 8)]

valuable = [name for name, price in loot if price >= 50]
total = sum([price for name, price in loot])

print("Değerli:", valuable)
print("Toplam değer:", total)
```

</details>

### Harcama Defteri: Harcama filtreleri

Kayıtlar `(kategori, tutar)` tuple'ları. Tek satırlık listelerle (list comprehension):

- `big`: tutarı 100 veya üstü olan harcamaların **tutarları**
- `market_total`: kategorisi `"market"` olan harcamaların toplamı

**Başlangıç kodu:**

```python
records = [("market", 120), ("kahve", 35), ("kira", 2000), ("market", 80)]
```

**İpuçları:**

1. [amount for category, amount in records if amount >= 100]
2. sum() içine bir list comprehension yazabilirsin.

<details><summary>Çözüm</summary>

```python
records = [("market", 120), ("kahve", 35), ("kira", 2000), ("market", 80)]
big = [amount for category, amount in records if amount >= 100]
market_total = sum([amount for category, amount in records if category == "market"])
print(big, market_total)
```

</details>

### Görev Asistanı: Görev filtreleri

Görevler `(başlık, öncelik, bitti_mi)` üçlüleri. Öncelik 1 (en önemli) ile 3 arasında. List comprehension ile:

- `pending`: bitmemiş görevlerin başlıkları
- `urgent`: bitmemiş **ve** önceliği 1 olan görevlerin başlıkları, BÜYÜK harfle (`upper()`)

**Başlangıç kodu:**

```python
tasks = [("Rapor yaz", 1, False), ("Kahve", 3, True), ("Faturayı öde", 1, False), ("Spor", 2, False)]
```

**İpuçları:**

1. [title for title, priority, done in tasks if not done]
2. İki koşul: if not done and priority == 1

<details><summary>Çözüm</summary>

```python
tasks = [("Rapor yaz", 1, False), ("Kahve", 3, True), ("Faturayı öde", 1, False), ("Spor", 2, False)]
pending = [title for title, priority, done in tasks if not done]
urgent = [title.upper() for title, priority, done in tasks if not done and priority == 1]
print(pending)
print(urgent)
```

</details>

### Kişisel Web Sitem: Uzun yazılar ve özet

Yazılar `(başlık, kelime sayısı)` tuple'ları. Tek satırlık listelerle (list comprehension):

- `long_titles`: 500 veya daha fazla kelimelik yazıların **başlıkları**
- `total_words`: bütün yazıların toplam kelime sayısı (`sum()` içinde bir list comprehension)

Bir de `lambda` ile `excerpt` adında bir mini fonksiyon yaz: bir metnin ilk 10 karakterini alıp sonuna `...` eklesin. `excerpt("Merhaba dünya, bu ilk yazım")` → `"Merhaba dü..."`

**Başlangıç kodu:**

```python
posts = [("Merhaba Dünya", 350), ("Kodla Oyna", 820), ("Python Notlarım", 1200), ("Kısa Not", 90)]
```

**İpuçları:**

1. [title for title, words in posts if words >= 500]
2. excerpt = lambda text: text[:10] + "..."

<details><summary>Çözüm</summary>

```python
posts = [("Merhaba Dünya", 350), ("Kodla Oyna", 820), ("Python Notlarım", 1200), ("Kısa Not", 90)]
long_titles = [title for title, words in posts if words >= 500]
total_words = sum([words for title, words in posts])
excerpt = lambda text: text[:10] + "..."
print(long_titles, total_words)
print(excerpt("Merhaba dünya, bu ilk yazım"))
```

</details>

### Sohbet Botu: Kelime süzgeci

Yapay zekâ asistanları mesajı önce kelimelere (**token**) ayırır ve işe yaramayanları atar. List comprehension ile:

- `tokens`: `message.split()` içindeki kelimelerden `stop_words` listesinde **olmayanlar**
- `masked`: mesajdaki her kelime; ama kelime `bad_words` içindeyse yerine `"***"` (if ve else ile)

Sonra `tokens`'ı yazdır. `masked`'i de `" ".join(masked)` ile yazdır: `join` listedeki kelimeleri aralarına boşluk koyarak birleştirir.

```
['merhaba', 'bugün', 'aptal', 'soru', 'sordum']
merhaba bot bugün çok *** bir soru sordum
```

**Başlangıç kodu:**

```python
message = "merhaba bot bugün çok aptal bir soru sordum"
stop_words = ["bot", "çok", "bir"]
bad_words = ["aptal", "salak"]
```

**İpuçları:**

1. [word for word in message.split() if word not in stop_words]
2. if ve else birlikte başa yazılır: ["***" if word in bad_words else word for word in ...]

<details><summary>Çözüm</summary>

```python
message = "merhaba bot bugün çok aptal bir soru sordum"
stop_words = ["bot", "çok", "bir"]
bad_words = ["aptal", "salak"]
tokens = [word for word in message.split() if word not in stop_words]
masked = ["***" if word in bad_words else word for word in message.split()]
print(tokens)
print(" ".join(masked))
```

</details>

### Okul Not Defteri: Kalanlar ve bonus

Kayıtlar `(ders, not)` tuple'ları. Tek satırlık listelerle (list comprehension):

- `failed`: notu 50'nin altında olan derslerin **adları**
- `bonus`: öğretmen her nota 5 puan ekledi; yeni notlar listesi. Ama not 100'ü geçemez (`if` ve `else` ile 100'de durdur).

**Başlangıç kodu:**

```python
records = [("Matematik", 85), ("Fizik", 42), ("Tarih", 98), ("Kimya", 48)]
```

**İpuçları:**

1. [lesson for lesson, grade in records if grade < 50]
2. [grade + 5 if grade + 5 <= 100 else 100 for lesson, grade in records]

<details><summary>Çözüm</summary>

```python
records = [("Matematik", 85), ("Fizik", 42), ("Tarih", 98), ("Kimya", 48)]
failed = [lesson for lesson, grade in records if grade < 50]
bonus = [grade + 5 if grade + 5 <= 100 else 100 for lesson, grade in records]
print(failed)
print(bonus)
```

</details>
