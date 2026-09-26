# Gün 6: Tuple'lar

**Kurs:** 30 Günde Python  ·  **Bölge:** Veri Ormanı  ·  **Maskot:** Piko

**Bugünün hedefi:** Değişmeyen veri grupları olan tuple'ları oluşturmak, açmak ve kullanmak

> Veri Ormanı'nın ağaçlarına eski kaşifler işaretler kazımış: (3, 5), (8, 2)... Bunlar gizli yerlerin koordinatları ve kimse onları değiştiremez. Bugün Python'da değiştirilemeyen bu mühürlü kutuları, yani **tuple**'ları öğreneceğiz.

![Veri Ormanı](../../gorseller/python/harita/orman.webp)

## Konu anlatımı

### Tuple nedir?

Tuple, listeye çok benzer ama **parantezle** yazılır ve bir kez oluşturulduktan sonra **değiştirilemez**.

```python
pos = (3, 5)
colors = ("mavi", "sarı", "yeşil")
print(colors[0])    # mavi
print(len(colors))  # 3
```

Elemanlara listedeki gibi sıra numarasıyla (index) ulaşırsın. `colors[-1]` son elemanı verir.

### Neden değişmesin?

Bazı bilgiler hiç değişmemeli: haritadaki bir noktanın koordinatı, haftanın günleri, bir rengin kodu. Tuple bu bilgileri kazara bozmamızı engeller.

`colors[0] = "kırmızı"` yazarsan Python `TypeError` hatası verir. Değiştirmen gerekiyorsa önce listeye çevir, değiştir, sonra tekrar tuple yap:

```python
items = list(colors)
items.append("mor")
colors = tuple(items)
```

### Tuple açmak

Tuple'daki değerleri tek satırda ayrı değişkenlere dağıtabilirsin. Buna **açma** (unpacking) denir:

```python
pos = (3, 5)
x, y = pos
print(x)  # 3
print(y)  # 5
```

Aynı hileyle iki değişkenin değerini yer değiştirebilirsin: `a, b = b, a`

### Faydalı işlemler

- `"sarı" in colors` tuple'da var mı diye sorar
- `colors.count("mavi")` kaç kez geçtiğini sayar
- `colors.index("sarı")` kaçıncı sırada olduğunu söyler
- `(1, 2) + (3, 4)` iki tuple'ı birleştirip yeni bir tuple yapar

Tek elemanlı tuple yazarken virgülü unutma: `(5,)`. Virgül olmazsa Python onu sadece parantez içindeki bir sayı sanar.

## Örnekler

### Konum

```python
pos = (3, 5)
print("Konum:", pos)
x, y = pos
print("x =", x)
print("y =", y)
```

### Kilidi aç, değiştir, kilitle

```python
colors = ("mavi", "sarı")
items = list(colors)
items.append("yeşil")
colors = tuple(items)
print(colors)
print(type(colors))
```

*Tuple'ı değiştirmenin tek yolu yeni bir tuple yapmaktır.*

### Yer değiştirme

```python
left = "kılıç"
right = "kalkan"
left, right = right, left
print("Sol el:", left)
print("Sağ el:", right)
```

## Görevler

### Görev 1: Konumu aç

`pos` tuple'ını `x` ve `y` değişkenlerine aç. Kod `x = 4, y = 9` yazdırmalı.

**Başlangıç kodu:**

```python
pos = (4, 9)

# pos'u x ve y değişkenlerine aç

print(f"x = {x}, y = {y}")
```

**İpuçları:**

1. Tek satır yeterli: x, y = pos
2. Virgülün solunda iki değişken, sağında tuple olmalı.

<details><summary>Çözüm</summary>

```python
pos = (4, 9)

x, y = pos

print(f"x = {x}, y = {y}")
```

</details>

### Görev 2: Renk paleti

`colors` tuple'ındaki ilk rengi, son rengi ve renk sayısını yazdır:

```
İlk renk: mavi
Son renk: yeşil
Renk sayısı: 3
```

**Başlangıç kodu:**

```python
colors = ("mavi", "sarı", "yeşil")

# İlk rengi, son rengi ve renk sayısını yazdır
```

**İpuçları:**

1. İlk eleman colors[0], son eleman colors[-1]
2. Eleman sayısı için len() kullan.

<details><summary>Çözüm</summary>

```python
colors = ("mavi", "sarı", "yeşil")

print(f"İlk renk: {colors[0]}")
print(f"Son renk: {colors[-1]}")
print(f"Renk sayısı: {len(colors)}")
```

</details>

### Görev 3: Yeni eşya ekle

Tuple değiştirilemez, ama listeye çevirip yeni bir tuple yapabiliriz. `items` tuple'ının sonuna `"kalkan"` ekle. Sonunda `items` yine bir **tuple** olmalı.

**Başlangıç kodu:**

```python
items = ("kılıç", "iksir")

# items'ı listeye çevir, "kalkan" ekle, tekrar tuple yap

print(items)
```

**İpuçları:**

1. list(items) ile tuple'dan liste yap.
2. Listeye append() ile ekle, sonra tuple(...) ile geri çevir.

<details><summary>Çözüm</summary>

```python
items = ("kılıç", "iksir")

bag = list(items)
bag.append("kalkan")
items = tuple(bag)

print(items)
```

</details>

## Challenge: Yer değiştir

`a` ve `b` değişkenlerinin değerlerini **üçüncü bir değişken kullanmadan** yer değiştir. Tuple açma hilesini hatırla.

**Başlangıç kodu:**

```python
a = "sol"
b = "sağ"

# a ile b'yi yer değiştir

print("a:", a)
print("b:", b)
```

**İpuçları:**

1. Tek satırda olur: a, b = b, a

<details><summary>Çözüm</summary>

```python
a = "sol"
b = "sağ"

a, b = b, a

print("a:", a)
print("b:", b)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Harita konumları**

### Piko'nun Macerası: Harita konumları

Piko'nun ormandaki adımları `path` listesinde tuple olarak duruyor. Her tuple bir konum: `(x, y)`.

- `start` ilk konum, `current` son konum olsun.
- Sonra şunları yazdır:

```
Başlangıç: (0, 0)
Şu an: (2, 1)
Adım sayısı: 3
```

Adım sayısı, konum sayısının bir eksiğidir.

**Başlangıç kodu:**

```python
path = [(0, 0), (1, 0), (1, 1), (2, 1)]

# start ve current değişkenlerini oluştur

# Üç satırı yazdır
```

**İpuçları:**

1. İlk konum path[0], son konum path[-1]
2. Adım sayısı: len(path) - 1

<details><summary>Çözüm</summary>

```python
path = [(0, 0), (1, 0), (1, 1), (2, 1)]

start = path[0]
current = path[-1]

print(f"Başlangıç: {start}")
print(f"Şu an: {current}")
print(f"Adım sayısı: {len(path) - 1}")
```

</details>

### Harcama Defteri: Harcama kayıtları

Her harcama bir tuple: `(kategori, tutar)`. Kayıtlar `records` listesinde.

- `first`: ilk kayıt, `last`: son kayıt
- Son kaydı iki değişkene aç: `category, amount = last`
- Sonra şöyle yazdır:

```
İlk kayıt: ('kira', 2000)
Son harcama: market - 120 TL
```

**Başlangıç kodu:**

```python
records = [("kira", 2000), ("ulaşım", 400), ("market", 120)]
```

**İpuçları:**

1. records[0] ilk, records[-1] son eleman.
2. category, amount = last satırı tuple'ı açar.

<details><summary>Çözüm</summary>

```python
records = [("kira", 2000), ("ulaşım", 400), ("market", 120)]
first = records[0]
last = records[-1]
category, amount = last
print("İlk kayıt:", first)
print(f"Son harcama: {category} - {amount} TL")
```

</details>

### Görev Asistanı: Toplantı saati

Toplantılar tuple olarak duruyor: `(ad, saat, dakika)`. Toplantılar `meetings` listesinde.

- `next_meeting`: listedeki ilk toplantı
- Onu üç değişkene aç: `name, hour, minute = next_meeting`
- `Sıradaki: Proje toplantısı saat 14:30` gibi yazdır.
- `count`: toplantı sayısı. `Bugün 2 toplantı var` yazdır.

**Başlangıç kodu:**

```python
meetings = [("Proje toplantısı", 14, 30), ("Ders", 16, 45)]
```

**İpuçları:**

1. meetings[0] ilk toplantı.
2. name, hour, minute = next_meeting

<details><summary>Çözüm</summary>

```python
meetings = [("Proje toplantısı", 14, 30), ("Ders", 16, 45)]
next_meeting = meetings[0]
name, hour, minute = next_meeting
print(f"Sıradaki: {name} saat {hour}:{minute}")
count = len(meetings)
print(f"Bugün {count} toplantı var")
```

</details>

### Kişisel Web Sitem: Yazı kayıtları

Her yazı bir tuple: `(başlık, slug)`. Yazılar `posts` listesinde, eskiden yeniye sıralı.

- `first`: ilk yazı, `latest`: en yeni (son) yazı
- En yeni yazıyı iki değişkene aç: `title, slug = latest`
- Sonra şöyle yazdır:

```
İlk yazı: ('Merhaba Dünya', 'merhaba-dunya')
En yeni yazı: Python Notlarım -> /blog/python-notlarim.html
```

**Başlangıç kodu:**

```python
posts = [("Merhaba Dünya", "merhaba-dunya"), ("Kodla Oyna", "kodla-oyna"), ("Python Notlarım", "python-notlarim")]
```

**İpuçları:**

1. posts[0] ilk, posts[-1] son eleman.
2. title, slug = latest satırı tuple'ı açar.

<details><summary>Çözüm</summary>

```python
posts = [("Merhaba Dünya", "merhaba-dunya"), ("Kodla Oyna", "kodla-oyna"), ("Python Notlarım", "python-notlarim")]
first = posts[0]
latest = posts[-1]
title, slug = latest
print("İlk yazı:", first)
print(f"En yeni yazı: {title} -> /blog/{slug}.html")
```

</details>

### Sohbet Botu: Niyet ve cevap

Botun bildiği **niyetler** (kullanıcının ne istediği) ve cevapları iki tuple'da, aynı sırayla duruyor. Kullanıcının niyeti `intent`.

- `position`: niyetin `intents` içindeki sırası (`index()`)
- `reply`: `replies` içinde aynı sıradaki cevap
- `rule`: `(intent, reply)` tuple'ı

Sonra şöyle yazdır:

```
3 niyet biliyorum
Kural: ('hava', 'Bugün hava güneşli.')
```

**Başlangıç kodu:**

```python
intents = ("selam", "hava", "veda")
replies = ("Merhaba!", "Bugün hava güneşli.", "Görüşürüz!")
intent = "hava"
```

**İpuçları:**

1. intents.index("hava") 1 verir.
2. rule = (intent, reply) iki değeri bir tuple'da toplar.

<details><summary>Çözüm</summary>

```python
intents = ("selam", "hava", "veda")
replies = ("Merhaba!", "Bugün hava güneşli.", "Görüşürüz!")
intent = "hava"
position = intents.index(intent)
reply = replies[position]
rule = (intent, reply)
print(f"{len(intents)} niyet biliyorum")
print("Kural:", rule)
```

</details>

### Okul Not Defteri: Pazartesi programı

Ders programı dönem boyunca değişmez, o yüzden tuple'da tutalım. `monday` pazartesi günkü derslerin sırası.

- `first_lesson`: ilk ders, `last_lesson`: son ders
- `math_hours`: pazartesi kaç saat Matematik var (`count`)
- `history_slot`: Tarih kaçıncı derste (`index` + 1)

Sonra şöyle yazdır:

```
İlk ders: Matematik
Son ders: Beden Eğitimi
Matematik: 2 saat
Tarih 4. derste
```

**Başlangıç kodu:**

```python
monday = ("Matematik", "Fizik", "Matematik", "Tarih", "Beden Eğitimi")
```

**İpuçları:**

1. monday[0] ilk, monday[-1] son eleman.
2. monday.count("Matematik") kaç kez geçtiğini, monday.index("Tarih") sırasını (0'dan başlayarak) verir.

<details><summary>Çözüm</summary>

```python
monday = ("Matematik", "Fizik", "Matematik", "Tarih", "Beden Eğitimi")
first_lesson = monday[0]
last_lesson = monday[-1]
math_hours = monday.count("Matematik")
history_slot = monday.index("Tarih") + 1
print("İlk ders:", first_lesson)
print("Son ders:", last_lesson)
print(f"Matematik: {math_hours} saat")
print(f"Tarih {history_slot}. derste")
```

</details>
