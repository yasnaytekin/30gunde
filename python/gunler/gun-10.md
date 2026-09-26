# Gün 10: Döngüler

**Kurs:** 30 Günde Python  ·  **Bölge:** Mantık Kalesi  ·  **Maskot:** Piko

**Bugünün hedefi:** while ve for döngüleriyle tekrar eden işleri otomatik yapmak

> Mantık Kalesi'nin kulesinde 100 basamak var. Her basamak için ayrı ayrı `print` yazmak zorunda olsaydık parmaklarımız yorulurdu! Bilgisayarlar tekrar eden işleri hiç sıkılmadan yapar. Bugün **döngüleri** öğreniyoruz.

![Mantık Kalesi](../../gorseller/python/harita/kale.webp)

## Konu anlatımı

### while: koşul doğru oldukça

`while` döngüsü, koşulu `True` olduğu sürece içindeki kodu tekrar tekrar çalıştırır:

```python
count = 3
while count > 0:
    print(count)
    count -= 1
print("Başla!")
```

Döngünün içinde koşulu değiştirmeyi unutma. `count -= 1` olmasaydı döngü hiç bitmezdi. Buna **sonsuz döngü** denir; bu sitede 6 saniye sonra durdurulur.

### for ve range()

Bir şeyi belli sayıda tekrarlamak için `for` ve `range()` kullanılır:

- `range(5)` 0, 1, 2, 3, 4
- `range(1, 6)` 1, 2, 3, 4, 5 (son sayı dahil değil)
- `range(0, 10, 2)` 0, 2, 4, 6, 8 (ikişer ikişer)

```python
for i in range(1, 4):
    print("Tur", i)
```

### Koleksiyonlarda gezinmek

`for` bir listenin, tuple'ın, set'in, hatta bir yazının her elemanını sırayla verir:

```python
bag = ["kılıç", "iksir", "harita"]
for item in bag:
    print("Çantada:", item)
```

Sözlükte gezinirken `for key, value in hero.items():` kullanabilirsin. Sıra numarası da lazımsa `enumerate()` işe yarar: `for i, item in enumerate(bag, 1):`

### break ve continue

- `break` döngüden hemen çıkar
- `continue` bu turu atlar ve sıradakine geçer

```python
for n in range(1, 10):
    if n == 5:
        break
    if n % 2 == 0:
        continue
    print(n)   # 1 ve 3
```

## Örnekler

### Geri sayım

```python
count = 5
while count > 0:
    print(count)
    count -= 1
print("Kalk!")
```

### Toplama makinesi

```python
total = 0
for n in range(1, 101):
    total += n
print("1'den 100'e toplam:", total)
```

*Bu işlemi elle yapmak ne kadar sürerdi?*

### Çantayı say

```python
bag = ["kılıç", "iksir", "harita", "anahtar"]
for i, item in enumerate(bag, 1):
    print(f"{i}. {item}")
    if item == "harita":
        print("Harita bulundu, aramayı bırakıyorum.")
        break
```

## Görevler

### Görev 1: Geri sayım

`while` döngüsüyle `count`'tan 1'e kadar geri say, en sonda `Başla!` yazdır.

**Başlangıç kodu:**

```python
count = 5

# while ile geri say, sonra "Başla!" yazdır
```

**İpuçları:**

1. while count > 0: ile başla.
2. Döngünün içinde count -= 1 yazmayı unutma.

<details><summary>Çözüm</summary>

```python
count = 5

while count > 0:
    print(count)
    count -= 1

print("Başla!")
```

</details>

### Görev 2: Çarpım tablosu

`n` sayısının çarpım tablosunu 1'den 10'a kadar yazdır. Her satır şöyle olmalı: `7 x 3 = 21`

**Başlangıç kodu:**

```python
n = 7

# for ve range ile n'nin çarpım tablosunu yazdır
```

**İpuçları:**

1. range(1, 11) sana 1'den 10'a kadar sayıları verir.
2. print(f"{n} x {i} = {n * i}")

<details><summary>Çözüm</summary>

```python
n = 7

for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")
```

</details>

### Görev 3: Altınları topla

`for` döngüsüyle `coins` listesindeki altınları topla ve `total` değişkenine yaz. Bu sefer `sum()` kullanmak yok!

**Başlangıç kodu:**

```python
coins = [5, 10, 3, 7]
total = 0

# for ile coins'i dolaş ve total'a ekle

print("Toplam altın:", total)
```

**İpuçları:**

1. for c in coins: yazıp içinde total += c yap.

<details><summary>Çözüm</summary>

```python
coins = [5, 10, 3, 7]
total = 0

for c in coins:
    total += c

print("Toplam altın:", total)
```

</details>

### Sahne görevi: Piko piramidi

Bir `for` döngüsüyle Piko piramidi kur: 1. satırda 1 Piko, 2. satırda 2 Piko... `kat` kadar satır olsun.

`kat = 6` yazınca piramit 6 kat olmalı!

**Başlangıç kodu:**

```python
kat = 4
```

**İpuçları:**

1. for i in range(1, kat + 1):
2. Döngünün içinde print("*" * i)

<details><summary>Çözüm</summary>

```python
kat = 4

for i in range(1, kat + 1):
    print("*" * i)
```

</details>

## Challenge: PiKo sayıları

1'den `n`'ye kadar sayıları yazdır. Ama sayı 3'e bölünüyorsa `Pi`, 5'e bölünüyorsa `Ko`, ikisine de bölünüyorsa `PiKo` yaz.

**Başlangıç kodu:**

```python
n = 15

# 1'den n'ye kadar: 3'e bölünürse Pi, 5'e Ko, ikisine PiKo
```

**İpuçları:**

1. Bölünüyor mu diye % ile kalana bak: i % 3 == 0
2. İkisine de bölünme durumunu en önce kontrol et.

<details><summary>Çözüm</summary>

```python
n = 15

for i in range(1, n + 1):
    if i % 15 == 0:
        print("PiKo")
    elif i % 3 == 0:
        print("Pi")
    elif i % 5 == 0:
        print("Ko")
    else:
        print(i)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Oyun turları**

### Piko'nun Macerası: Oyun turları

Piko'nun canı `hp`. Düşman her turda `attacks` listesindeki kadar hasar veriyor.

- Her tur için canı azalt ve `Tur 1: can 22` gibi yazdır.
- Can 0 veya altına düşerse `Piko yoruldu, oyun bitti!` yazdır ve döngüden çık.
- Tüm turlar bittiğinde can hâlâ 0'dan büyükse `Piko hayatta kaldı!` yazdır.

**Başlangıç kodu:**

```python
hp = 30
attacks = [8, 5, 12, 9]

# Her saldırıda canı azalt ve turu yazdır
```

**İpuçları:**

1. enumerate(attacks, 1) sana tur numarasını ve hasarı birlikte verir.
2. Can 0 veya altına inince break ile çık.
3. Döngüden sonra if hp > 0: ile kontrol et.

<details><summary>Çözüm</summary>

```python
hp = 30
attacks = [8, 5, 12, 9]

for turn, damage in enumerate(attacks, 1):
    hp -= damage
    print(f"Tur {turn}: can {hp}")
    if hp <= 0:
        print("Piko yoruldu, oyun bitti!")
        break

if hp > 0:
    print("Piko hayatta kaldı!")
```

</details>

### Harcama Defteri: Harcama dökümü

`amounts` listesindeki harcamaları bir döngüyle yazdıralım:

```
1. harcama: 120 TL
2. harcama: 45 TL
3. harcama: 300 TL
Toplam: 465 TL
```

Toplamı döngü içinde `total` değişkenine ekleyerek hesapla (`sum()` kullanmadan).

**Başlangıç kodu:**

```python
amounts = [120, 45, 300]
total = 0
```

**İpuçları:**

1. for amount in amounts: ile her harcamayı sırayla al.
2. Sıra numarası için ayrı bir sayaç tutabilirsin: number += 1

<details><summary>Çözüm</summary>

```python
amounts = [120, 45, 300]
total = 0
number = 1
for amount in amounts:
    print(f"{number}. harcama: {amount} TL")
    total += amount
    number += 1
print(f"Toplam: {total} TL")
```

</details>

### Görev Asistanı: Yapılacaklar listesi

Görevler `(başlık, bitti_mi)` ikilileri. Bir döngüyle şöyle bir liste yazdır:

```
[x] Kahve
[ ] Rapor yaz
[ ] Spor
1/3 tamamlandı
```

Bitenleri döngüde `done_count` değişkeninde say.

**Başlangıç kodu:**

```python
tasks = [("Kahve", True), ("Rapor yaz", False), ("Spor", False)]
done_count = 0
```

**İpuçları:**

1. for title, done in tasks: ikiliyi açar.
2. Bitenler için done_count += 1

<details><summary>Çözüm</summary>

```python
tasks = [("Kahve", True), ("Rapor yaz", False), ("Spor", False)]
done_count = 0
for title, done in tasks:
    if done:
        print(f"[x] {title}")
        done_count += 1
    else:
        print(f"[ ] {title}")
print(f"{done_count}/{len(tasks)} tamamlandı")
```

</details>

### Kişisel Web Sitem: Menü çubuğu

Her sayfanın üstünde bir menü olacak. `menu` listesindeki her `(ad, dosya)` için bir döngüyle bir satır yazdır. Şu anki sayfa (`current`) bağlantı olmasın, kalın (`<b>`) yazılsın. Menüyü `<nav>` ve `</nav>` satırları arasına al:

```
<nav>
<a href="index.html">Ana Sayfa</a>
<b>Blog</b>
<a href="hakkimda.html">Hakkımda</a>
</nav>
```

**Başlangıç kodu:**

```python
menu = [("Ana Sayfa", "index.html"), ("Blog", "blog.html"), ("Hakkımda", "hakkimda.html")]
current = "blog.html"
```

**İpuçları:**

1. for name, file in menu: her tuple'ı iki değişkene açar.
2. Döngünün içinde if file == current: ile şu anki sayfayı ayır.

<details><summary>Çözüm</summary>

```python
menu = [("Ana Sayfa", "index.html"), ("Blog", "blog.html"), ("Hakkımda", "hakkimda.html")]
current = "blog.html"
print("<nav>")
for name, file in menu:
    if file == current:
        print(f"<b>{name}</b>")
    else:
        print(f'<a href="{file}">{name}</a>')
print("</nav>")
```

</details>

### Sohbet Botu: Sohbet döngüsü

Konuşmadaki mesajlar `conversation` listesinde. Bir `for` döngüsüyle her mesajı `Sen: merhaba` gibi yazdır ve `count` ile say.

Mesaj `"görüşürüz"` olunca `Bot: Hoşça kal! 3 mesaj konuştuk.` yazdır ve döngüyü **durdur** (`break`); sonraki mesajlar yazılmasın.

```
Sen: merhaba
Sen: hava nasıl
Sen: görüşürüz
Bot: Hoşça kal! 3 mesaj konuştuk.
```

**Başlangıç kodu:**

```python
conversation = ["merhaba", "hava nasıl", "görüşürüz", "orada mısın?"]
count = 0
```

**İpuçları:**

1. for message in conversation: her mesajı sırayla verir.
2. Veda mesajını yazdırdıktan sonra break ile döngüden çık.

<details><summary>Çözüm</summary>

```python
conversation = ["merhaba", "hava nasıl", "görüşürüz", "orada mısın?"]
count = 0
for message in conversation:
    print(f"Sen: {message}")
    count += 1
    if message == "görüşürüz":
        print(f"Bot: Hoşça kal! {count} mesaj konuştuk.")
        break
```

</details>

### Okul Not Defteri: Sınav dökümü

`grades` listesindeki sınav notlarını bir döngüyle yazdıralım. 50 ve üstü `geçti`, altı `kaldı`:

```
1. sınav: 85 - geçti
2. sınav: 42 - kaldı
3. sınav: 70 - geçti
4. sınav: 55 - geçti
Geçilen: 3/4
```

Geçilen sınav sayısını döngü içinde `passed_count` değişkeninde say.

**Başlangıç kodu:**

```python
grades = [85, 42, 70, 55]
passed_count = 0
```

**İpuçları:**

1. for grade in grades: ile her notu sırayla al; içinde if grade >= 50:
2. Sıra numarası için ayrı bir sayaç tut: number += 1

<details><summary>Çözüm</summary>

```python
grades = [85, 42, 70, 55]
passed_count = 0
number = 1
for grade in grades:
    if grade >= 50:
        print(f"{number}. sınav: {grade} - geçti")
        passed_count += 1
    else:
        print(f"{number}. sınav: {grade} - kaldı")
    number += 1
print(f"Geçilen: {passed_count}/{len(grades)}")
```

</details>
