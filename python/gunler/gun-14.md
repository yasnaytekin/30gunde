# Gün 14: Üst düzey fonksiyonlar

**Kurs:** 30 Günde Python  ·  **Bölge:** Alet Atölyesi  ·  **Maskot:** Piko

**Bugünün hedefi:** Fonksiyonları değer gibi kullanmak: map, filter, sorted ve fonksiyon döndüren fonksiyonlar

> Atölyenin ustası Piko'ya bir sır verdi: "Aletleri başka aletlere de takabilirsin!" Bir matkabın ucunu değiştirmek gibi, bir fonksiyona başka bir fonksiyonu verebilirsin. Bugün fonksiyonlarla oynayan fonksiyonları, yani **üst düzey fonksiyonları** öğreniyoruz.

![Alet Atölyesi](../../gorseller/python/harita/atolye.webp)

## Konu anlatımı

### Fonksiyonlar da değerdir

Bir fonksiyonu parantezsiz yazarsan onu çağırmazsın, **kendisini** alırsın. Onu değişkene koyabilir ya da başka fonksiyona verebilirsin:

```python
def shout(text):
    return text.upper() + "!"

def use_twice(func, value):
    return func(func(value))

print(use_twice(shout, "hey"))   # HEY!!
```

### map ve filter

- `map(fonksiyon, liste)` her elemana fonksiyonu uygular
- `filter(fonksiyon, liste)` fonksiyonun `True` dediği elemanları tutar

```python
scores = [40, 75, 90]
bonus = list(map(lambda s: s + 10, scores))       # [50, 85, 100]
passed = list(filter(lambda s: s >= 60, scores))  # [75, 90]
```

Sonucu görmek için `list(...)` içine almayı unutma.

### sorted ve key

`sorted` bir listeyi sıralar. `key` ile **neye göre** sıralanacağını söylersin:

```python
players = [("Ali", 120), ("Piko", 300), ("Ece", 250)]
by_score = sorted(players, key=lambda p: p[1], reverse=True)
```

`reverse=True` büyükten küçüğe sıralar. `min` ve `max` de `key` alır: `max(players, key=lambda p: p[1])`

### Fonksiyon üreten fonksiyon

Bir fonksiyon, içinde yeni bir fonksiyon yapıp onu döndürebilir. İçteki fonksiyon dıştakinin değerlerini hatırlar; buna **closure** denir:

```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

triple = make_multiplier(3)
print(triple(5))   # 15
```

İleride göreceğin **decorator**'lar (`@` ile başlayan satırlar) da bu fikirle çalışır.

## Örnekler

### Fonksiyonu fonksiyona ver

```python
def shout(text):
    return text.upper() + "!"

def use_twice(func, value):
    return func(func(value))

print(use_twice(shout, "hey"))
print(use_twice(lambda n: n * 10, 3))
```

### map ve filter

```python
scores = [40, 75, 90, 55]
print(list(map(lambda s: s + 10, scores)))
print(list(filter(lambda s: s >= 60, scores)))
```

### Sıralama

```python
players = [("Ali", 120), ("Piko", 300), ("Ece", 250)]
for name, score in sorted(players, key=lambda p: p[1], reverse=True):
    print(name, score)
print("Kısa isim önce:", sorted(["Zeynep", "Can", "Ece"], key=len))
```

## Görevler

### Görev 1: Uygula

`apply(func, value)` fonksiyonu, kendisine verilen `func` fonksiyonunu `value` üzerinde çalıştırıp sonucu döndürsün.

**Başlangıç kodu:**

```python
def apply(func, value):
    pass

print(apply(abs, -7))
print(apply(len, "Piko"))
```

**İpuçları:**

1. func bir fonksiyon, onu çağırmak için func(value) yaz.
2. return func(value)

<details><summary>Çözüm</summary>

```python
def apply(func, value):
    return func(value)

print(apply(abs, -7))
print(apply(len, "Piko"))
```

</details>

### Görev 2: Bonus puan

`map` kullanarak her skora 10 puan ekle ve sonucu `bonus` listesine koy.

**Başlangıç kodu:**

```python
scores = [40, 75, 90]

bonus = []

print(bonus)
```

**İpuçları:**

1. map(lambda s: s + 10, scores)
2. Sonucu list(...) içine al.

<details><summary>Çözüm</summary>

```python
scores = [40, 75, 90]

bonus = list(map(lambda s: s + 10, scores))

print(bonus)
```

</details>

### Görev 3: Geçenler

`filter` kullanarak 60 ve üstü skorları `passed` listesine koy.

**Başlangıç kodu:**

```python
scores = [40, 75, 90, 59, 60]

passed = []

print(passed)
```

**İpuçları:**

1. filter(lambda s: s >= 60, scores)
2. Sonucu list(...) içine al.

<details><summary>Çözüm</summary>

```python
scores = [40, 75, 90, 59, 60]

passed = list(filter(lambda s: s >= 60, scores))

print(passed)
```

</details>

## Challenge: Çarpan üretici

`make_multiplier(n)` fonksiyonu, aldığı sayıyı `n` ile çarpan **yeni bir fonksiyon** döndürsün.

**Başlangıç kodu:**

```python
def make_multiplier(n):
    pass

double = make_multiplier(2)
print(double(21))
```

**İpuçları:**

1. İçeride def multiply(x): tanımla.
2. En sonda fonksiyonun kendisini döndür: return multiply (parantezsiz)

<details><summary>Çözüm</summary>

```python
def make_multiplier(n):
    def multiply(x):
        return x * n
    return multiply

double = make_multiplier(2)
print(double(21))
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Skor tablosu**

### Piko'nun Macerası: Skor tablosu

Oyunun skor tablosunu yapalım. `players` listesini skora göre **büyükten küçüğe** sırala ve `ranking` değişkenine koy. Sonra şöyle yazdır:

```
1. Piko: 300
2. Ece: 250
3. Ali: 120
```

**Başlangıç kodu:**

```python
players = [("Ali", 120), ("Piko", 300), ("Ece", 250)]

ranking = players

# Sıralı tabloyu yazdır
```

**İpuçları:**

1. sorted(players, key=lambda p: p[1], reverse=True)
2. Sıra numarası için enumerate(ranking, 1)

<details><summary>Çözüm</summary>

```python
players = [("Ali", 120), ("Piko", 300), ("Ece", 250)]

ranking = sorted(players, key=lambda p: p[1], reverse=True)

for i, (name, score) in enumerate(ranking, 1):
    print(f"{i}. {name}: {score}")
```

</details>

### Harcama Defteri: En büyük 3 harcama

Kayıtları tutara göre **büyükten küçüğe** sırala (`sorted`, `key` ve `lambda`) ve ilk üçünü `top3` değişkenine koy. Sonra şöyle yazdır:

```
1. kira: 2000 TL
2. market: 450 TL
3. ulaşım: 400 TL
```

**Başlangıç kodu:**

```python
records = [("market", 450), ("kahve", 35), ("kira", 2000), ("ulaşım", 400), ("kitap", 90)]
```

**İpuçları:**

1. sorted(records, key=lambda r: r[1], reverse=True)
2. İlk üç eleman için [:3]

<details><summary>Çözüm</summary>

```python
records = [("market", 450), ("kahve", 35), ("kira", 2000), ("ulaşım", 400), ("kitap", 90)]
top3 = sorted(records, key=lambda r: r[1], reverse=True)[:3]
number = 1
for category, amount in top3:
    print(f"{number}. {category}: {amount} TL")
    number += 1
```

</details>

### Görev Asistanı: Günün sırası

Görevler `(başlık, öncelik)` ikilileri. `sorted` ve `lambda` ile önce **önceliğe** (küçükten büyüğe), öncelik aynıysa **başlığa** göre sırala ve `ordered` değişkenine koy. Sonra numaralı yazdır:

```
1. Faturayı öde (1)
2. Rapor yaz (1)
3. Spor (2)
4. Kitap oku (3)
```

**Başlangıç kodu:**

```python
tasks = [("Spor", 2), ("Rapor yaz", 1), ("Kitap oku", 3), ("Faturayı öde", 1)]
```

**İpuçları:**

1. key=lambda t: (t[1], t[0]) önce önceliğe, sonra başlığa bakar.
2. Numara için bir sayaç tut.

<details><summary>Çözüm</summary>

```python
tasks = [("Spor", 2), ("Rapor yaz", 1), ("Kitap oku", 3), ("Faturayı öde", 1)]
ordered = sorted(tasks, key=lambda t: (t[1], t[0]))
number = 1
for title, priority in ordered:
    print(f"{number}. {title} ({priority})")
    number += 1
```

</details>

### Kişisel Web Sitem: Son yazılar

Ana sayfada en yeni 3 yazı görünsün. Tarihler `"yıl-ay-gün"` biçiminde olduğu için yazı olarak da doğru sıralanır.

- `recent`: yazıları tarihe göre **yeniden eskiye** sırala (`sorted`, `key` ve `lambda`) ve ilk üçünü al.
- `titles`: `map` ile `recent`'teki yazıların sadece başlıkları (liste)
- Sonra şöyle yazdır (`" | ".join(titles)`):

```
Son yazılar: Python Notlarım | Kodla Oyna | Merhaba Dünya
```

**Başlangıç kodu:**

```python
posts = [("Merhaba Dünya", "2026-08-02"), ("Python Notlarım", "2026-09-15"), ("Kodla Oyna", "2026-09-01"), ("Kısa Not", "2026-07-20")]
```

**İpuçları:**

1. sorted(posts, key=lambda p: p[1], reverse=True)[:3]
2. list(map(lambda p: p[0], recent)) sadece başlıkları verir.

<details><summary>Çözüm</summary>

```python
posts = [("Merhaba Dünya", "2026-08-02"), ("Python Notlarım", "2026-09-15"), ("Kodla Oyna", "2026-09-01"), ("Kısa Not", "2026-07-20")]
recent = sorted(posts, key=lambda p: p[1], reverse=True)[:3]
titles = list(map(lambda p: p[0], recent))
print("Son yazılar: " + " | ".join(titles))
```

</details>

### Sohbet Botu: En uygun niyet

Bot mesajdaki anahtar kelimeleri sayıp her niyete bir puan verdi: `scores` listesi `(niyet, puan)` ikilileri. En çok puanı alan niyet, kullanıcının büyük ihtimalle istediği şeydir.

- `ranked`: puana göre **büyükten küçüğe** sıralı liste (`sorted`, `key` ve `lambda`)
- `best`: en yüksek puanlı niyetin adı
- `matched`: `ranked` içinden puanı 0'dan büyük olanlar (`filter` ve `lambda`; sonucu `list()` ile listeye çevir)

Sonra şöyle yazdır:

```
En uygun niyet: hava
hava: 2 puan
saat: 1 puan
```

**Başlangıç kodu:**

```python
scores = [("selam", 0), ("hava", 2), ("saat", 1), ("veda", 0)]
```

**İpuçları:**

1. sorted(scores, key=lambda s: s[1], reverse=True)
2. list(filter(lambda s: s[1] > 0, ranked))

<details><summary>Çözüm</summary>

```python
scores = [("selam", 0), ("hava", 2), ("saat", 1), ("veda", 0)]
ranked = sorted(scores, key=lambda s: s[1], reverse=True)
best = ranked[0][0]
matched = list(filter(lambda s: s[1] > 0, ranked))
print(f"En uygun niyet: {best}")
for intent, score in matched:
    print(f"{intent}: {score} puan")
```

</details>

### Okul Not Defteri: En iyi derslerin

Kayıtları nota göre **büyükten küçüğe** sırala (`sorted`, `key` ve `lambda`) ve `ranking` değişkenine koy. `passed`: `filter` ve `lambda` ile notu 50 veya üstü olan kayıtlar (liste olarak).

Sonra şöyle yazdır:

```
1. Tarih: 90
2. Matematik: 85
3. Kimya: 70
4. Fizik: 42
Geçilen ders: 3/4
```

**Başlangıç kodu:**

```python
records = [("Matematik", 85), ("Fizik", 42), ("Tarih", 90), ("Kimya", 70)]
```

**İpuçları:**

1. sorted(records, key=lambda r: r[1], reverse=True)
2. list(filter(lambda r: r[1] >= 50, records))

<details><summary>Çözüm</summary>

```python
records = [("Matematik", 85), ("Fizik", 42), ("Tarih", 90), ("Kimya", 70)]
ranking = sorted(records, key=lambda r: r[1], reverse=True)
passed = list(filter(lambda r: r[1] >= 50, records))
number = 1
for lesson, grade in ranking:
    print(f"{number}. {lesson}: {grade}")
    number += 1
print(f"Geçilen ders: {len(passed)}/{len(records)}")
```

</details>
