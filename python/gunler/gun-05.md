# Gün 5: Listeler

**Kurs:** 30 Günde Python  ·  **Bölge:** Veri Ormanı  ·  **Maskot:** Piko

**Bugünün hedefi:** Liste oluşturmak, eleman eklemek, çıkarmak ve listeyi incelemek

> Veri Ormanı'na hoş geldin! Maceraya çıkan her kahramanın bir çantası vardır: kılıç, iksir, harita... Onlarca eşyayı tek tek değişkende tutmak zor olurdu. Bugün hepsini tek bir **listede** toplayacağız.

![Veri Ormanı](../../gorseller/python/harita/orman.webp)

## Konu anlatımı

### Liste nedir?

Liste, köşeli parantez içinde virgülle ayrılmış değerlerdir:

```python
inventory = ["kılıç", "iksir", "harita"]
scores = [40, 85, 60]
```

Stringlerde olduğu gibi indeks **0'dan başlar**: `inventory[0]` sonucu `"kılıç"`, `inventory[-1]` sonucu `"harita"`. `len(inventory)` listedeki eleman sayısını verir.

### Listeyi değiştirmek

- `append(x)` sona ekler
- `insert(0, x)` istediğin sıraya ekler
- `remove(x)` bulduğu ilk x'i çıkarır
- `pop()` son elemanı çıkarır ve sana verir
- `inventory[1] = "kalkan"` bir elemanı değiştirir

### Listeyi incelemek

- `"iksir" in inventory` eleman var mı? (`True` ya da `False`)
- `inventory.count("iksir")` kaç tane var?
- `sum(scores)`, `max(scores)`, `min(scores)`: toplam, en büyük, en küçük
- `sorted(scores)` sıralanmış yeni bir liste verir, `scores.sort()` listenin kendisini sıralar

### Dilimleme

Stringlerdeki gibi listeleri de dilimleyebilirsin: `scores[0:2]` ilk iki eleman, `scores[::-1]` ters çevrilmiş liste.

## Örnekler

### Çanta

```python
inventory = ["kılıç", "iksir"]
inventory.append("harita")
print(inventory)
print("İlk eşya:", inventory[0])
print("Eşya sayısı:", len(inventory))
```

### Çıkar ve kontrol et

```python
inventory = ["kılıç", "iksir", "taş"]
inventory.remove("taş")
print(inventory)
print("iksir" in inventory)
last = inventory.pop()
print("Çıkan:", last, "Kalan:", inventory)
```

### Skorlar

```python
scores = [40, 85, 60, 95]
print(sum(scores), max(scores), min(scores))
print(sorted(scores))
```

## Görevler

### Görev 1: Çantaya ekle

Çantanın sonuna `"iksir"` ekle.

**Başlangıç kodu:**

```python
inventory = ["kılıç", "kalkan"]

# "iksir" ekle

print(inventory)
```

**İpuçları:**

1. Sona eklemek için append() kullanılır.
2. inventory.append("iksir")

<details><summary>Çözüm</summary>

```python
inventory = ["kılıç", "kalkan"]

inventory.append("iksir")

print(inventory)
```

</details>

### Görev 2: Taşı at

Çantada gereksiz taşlar var. `remove()` ile ilk `"taş"`ı çıkar.

**Başlangıç kodu:**

```python
inventory = ["elma", "taş", "anahtar", "taş"]

# İlk "taş"ı çıkar

print(inventory)
```

**İpuçları:**

1. remove() sadece bulduğu ilk elemanı çıkarır.
2. inventory.remove("taş")

<details><summary>Çözüm</summary>

```python
inventory = ["elma", "taş", "anahtar", "taş"]

inventory.remove("taş")

print(inventory)
```

</details>

### Görev 3: Skor tablosu

`best` en yüksek skor, `total` skorların toplamı, `count` kaç skor olduğu olsun. Hepsini fonksiyonlarla hesapla.

**Başlangıç kodu:**

```python
scores = [40, 85, 60, 95]

best = 0
total = 0
count = 0

print(best, total, count)
```

**İpuçları:**

1. max(), sum() ve len() fonksiyonlarını kullan.
2. best = max(scores)

<details><summary>Çözüm</summary>

```python
scores = [40, 85, 60, 95]

best = max(scores)
total = sum(scores)
count = len(scores)

print(best, total, count)
```

</details>

### Sahne görevi: Odaya Piko koy

`sahne` listesi bir odanın 3 satırını tutuyor ama ortadaki satırda Piko yok. Listenin **1 numaralı** elemanını `"# * #"` ile değiştir. Sonra listenin elemanlarını sırayla (0, 1, 2) yazdır.

**Başlangıç kodu:**

```python
sahne = ["#####", "#   #", "#####"]

print(sahne[0])
```

**İpuçları:**

1. Bir elemanı değiştirmek: sahne[1] = "# * #"
2. İndeksler 0'dan başlar: sahne[0], sahne[1], sahne[2]

<details><summary>Çözüm</summary>

```python
sahne = ["#####", "#   #", "#####"]
sahne[1] = "# * #"

print(sahne[0])
print(sahne[1])
print(sahne[2])
```

</details>

## Challenge: Alfabetik sıralama

`sorted_names` isimlerin alfabetik sıralı hali olsun. `top3` ise sıralı listenin ilk üç ismi. İpucu: `sorted()` ve dilimleme.

**Başlangıç kodu:**

```python
names = ["Zeynep", "Ali", "Deniz", "Can", "Elif"]

sorted_names = []
top3 = []

print(sorted_names)
print(top3)
```

**İpuçları:**

1. sorted(names) sıralı yeni bir liste verir.
2. İlk üç eleman: liste[0:3]

<details><summary>Çözüm</summary>

```python
names = ["Zeynep", "Ali", "Deniz", "Can", "Elif"]

sorted_names = sorted(names)
top3 = sorted_names[0:3]

print(sorted_names)
print(top3)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Envanter**

### Piko'nun Macerası: Envanter

Kahramanımızın çantasını hazırlayalım.

- Boş `inventory` listesine `"fener"`, `"harita"` ve `"anahtar"` ekle
- f-string ve `len()` ile `Çantanda 3 eşya var` yazdır

**Başlangıç kodu:**

```python
inventory = []

# fener, harita ve anahtar ekle

# "Çantanda 3 eşya var" yazdır (sayıyı len() ile bul)
```

**İpuçları:**

1. Üç kez append() kullan.
2. print(f"Çantanda {len(inventory)} eşya var")

<details><summary>Çözüm</summary>

```python
inventory = []

inventory.append("fener")
inventory.append("harita")
inventory.append("anahtar")

print(f"Çantanda {len(inventory)} eşya var")
```

</details>

### Harcama Defteri: Harcama listesi

Harcamaları bir listede tutalım.

- Boş `expenses` listesine sırasıyla `120`, `45` ve `300` ekle (`append`).
- Sonra şu iki satırı yazdır (`len()`, `sum()` ve `max()` kullan):

```
3 harcama, toplam 465 TL
En büyük harcama: 300 TL
```

**Başlangıç kodu:**

```python
expenses = []
```

**İpuçları:**

1. expenses.append(120) listenin sonuna ekler.
2. f"{len(expenses)} harcama, toplam {sum(expenses)} TL"

<details><summary>Çözüm</summary>

```python
expenses = []
expenses.append(120)
expenses.append(45)
expenses.append(300)
print(f"{len(expenses)} harcama, toplam {sum(expenses)} TL")
print(f"En büyük harcama: {max(expenses)} TL")
```

</details>

### Görev Asistanı: Görev listesi

Görevleri bir listede toplayalım.

- Boş `tasks` listesine sırasıyla `"E-postaları oku"`, `"Rapor yaz"` ve `"Spor"` ekle.
- En başa `"Kahve"` ekle (`insert`).
- Sonra `4 görev: Kahve, E-postaları oku, Rapor yaz, Spor` yazdır (`len()` ve `", ".join()`).

**Başlangıç kodu:**

```python
tasks = []
```

**İpuçları:**

1. tasks.insert(0, "Kahve") en başa ekler.
2. ", ".join(tasks) listeyi virgüllerle birleştirir.

<details><summary>Çözüm</summary>

```python
tasks = []
tasks.append("E-postaları oku")
tasks.append("Rapor yaz")
tasks.append("Spor")
tasks.insert(0, "Kahve")
print(f"{len(tasks)} görev: {', '.join(tasks)}")
```

</details>

### Kişisel Web Sitem: Sayfa listesi

Sitenin sayfalarını bir listede tutalım.

- `pages` listesine sırasıyla `"Hakkımda"` ve `"Projeler"` ekle (`append`).
- Sonra şu iki satırı yazdır (`len()`, `", ".join(pages)` ve son eleman için `pages[-1]`):

```
4 sayfa: Ana Sayfa, Blog, Hakkımda, Projeler
Menünün sonu: Projeler
```

**Başlangıç kodu:**

```python
pages = ["Ana Sayfa", "Blog"]
```

**İpuçları:**

1. pages.append("Hakkımda") listenin sonuna ekler.
2. ", ".join(pages) elemanları virgülle birleştirir.

<details><summary>Çözüm</summary>

```python
pages = ["Ana Sayfa", "Blog"]
pages.append("Hakkımda")
pages.append("Projeler")
print(f"{len(pages)} sayfa: {', '.join(pages)}")
print(f"Menünün sonu: {pages[-1]}")
```

</details>

### Sohbet Botu: Selam kelimeleri

Bot hangi kelimelerin selam olduğunu bir listeden öğrensin.

- `greetings` listesine sırasıyla `"hey"` ve `"günaydın"` ekle (`append`).
- Yeni bir metot: `split()` bir yazıyı boşluklardan bölüp kelimelerin listesini verir. `"selam bot".split()` sonucu `['selam', 'bot']`. Bununla mesajın kelimelerinden `words` listesini oluştur.
- `first_word`: mesajın ilk kelimesi

Sonra şöyle yazdır:

```
4 selam kelimesi biliyorum
İlk kelime: selam
Selam mı: True
```

Son satır, ilk kelimenin `greetings` içinde olup olmadığını söyler (`in`).

**Başlangıç kodu:**

```python
greetings = ["merhaba", "selam"]
message = "selam bot nasılsın"
```

**İpuçları:**

1. greetings.append("hey") listenin sonuna ekler.
2. words = message.split() ve first_word = words[0]

<details><summary>Çözüm</summary>

```python
greetings = ["merhaba", "selam"]
message = "selam bot nasılsın"
greetings.append("hey")
greetings.append("günaydın")
words = message.split()
first_word = words[0]
print(f"{len(greetings)} selam kelimesi biliyorum")
print(f"İlk kelime: {first_word}")
print(f"Selam mı: {first_word in greetings}")
```

</details>

### Okul Not Defteri: Not listesi

Bir dersin notlarını listede tutalım.

- Boş `grades` listesine sırasıyla `70`, `85` ve `60` ekle (`append`).
- Sonra şu iki satırı yazdır (`len()`, `max()` ve `min()` kullan):

```
3 not girildi, en yüksek 85
En düşük not: 60
```

**Başlangıç kodu:**

```python
grades = []
```

**İpuçları:**

1. grades.append(70) listenin sonuna ekler.
2. f"{len(grades)} not girildi, en yüksek {max(grades)}"

<details><summary>Çözüm</summary>

```python
grades = []
grades.append(70)
grades.append(85)
grades.append(60)
print(f"{len(grades)} not girildi, en yüksek {max(grades)}")
print(f"En düşük not: {min(grades)}")
```

</details>
