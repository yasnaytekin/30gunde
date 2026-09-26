# Gün 15: Hata tipleri

**Kurs:** 30 Günde Python  ·  **Bölge:** Alet Atölyesi  ·  **Maskot:** Piko

**Bugünün hedefi:** Python'ın hata tiplerini tanımak, hata mesajlarını okumak ve hataları düzeltmek

> Atölyenin son odası bir dedektif bürosu! Masada bir sürü bozuk kod var ve hepsi kırmızı hata mesajları veriyor. Ama hata mesajları düşmanımız değil, ipucudur: bize neyin, nerede bozulduğunu söylerler. Bugün hata dedektifi oluyoruz.

![Alet Atölyesi](../../gorseller/python/harita/atolye.webp)

## Konu anlatımı

### Hata mesajı nasıl okunur?

Bir hata mesajında üç önemli bilgi vardır:

- **Satır numarası:** sorun nerede?
- **Hata tipi:** `NameError`, `TypeError` gibi
- **Açıklama:** tipin yanındaki kısa cümle

Önce satıra git, sonra hata tipine bak. Çoğu zaman sorun o satırda ya da hemen bir üstündedir.

### En sık görülen hatalar

- `SyntaxError`: yazım kuralı bozuk (unutulan `:` ya da parantez)
- `IndentationError`: girinti hatalı
- `NameError`: tanımlanmamış bir isim (çoğu zaman yazım hatası)
- `TypeError`: yanlış tipler birlikte kullanılmış (`"Yaş: " + 12`)
- `ValueError`: tip doğru ama değer uygun değil (`int("on iki")`)
- `IndexError`: listede olmayan bir sıra numarası (`items[10]`)
- `KeyError`: sözlükte olmayan bir anahtar
- `ZeroDivisionError`: sıfıra bölme
- `AttributeError`: o tipte olmayan bir metot (`5.upper()`)
- `ModuleNotFoundError`: olmayan bir modül

### Tipleri kontrol etmek

Birçok hata tip karışıklığından çıkar. `type()` ile bir değerin tipine bakabilirsin:

```python
age = "12"
print(type(age))       # <class 'str'>
print(int(age) + 1)    # 13
```

Yazı ile sayıyı birleştirirken `str()` ya da f-string kullan: `f"Yaş: {age}"`

### Dedektif taktikleri

- Değişkenlerin içinde ne olduğunu görmek için ara yerlere `print()` koy
- Kodu küçük parçalar halinde çalıştır
- Hata mesajını yüksek sesle oku, gerçekten çok şey söyler
- Liste boş olabilir mi, sayı sıfır olabilir mi? Uç durumları düşün

Birkaç gün sonra, Keşif Adası'nda bu hataları program çökmeden yakalamayı (`try` ve `except`) öğreneceğiz.

## Örnekler

### Tip karışıklığını çöz

```python
age = 12
print("Yaşım " + str(age))
print(f"Yaşım {age}")
text = "7"
print(int(text) + 3)
```

### Tipine bak

```python
values = [3, "3", 3.0, True, [3]]
for v in values:
    print(repr(v), "->", type(v).__name__)
```

### Güvenli bakış

```python
items = ["kılıç", "kalkan"]
hero = {"name": "Piko"}
print(items[-1])
print(hero.get("gold", 0))
nums = []
print(sum(nums) / len(nums) if nums else 0)
```

*Bu satırların her biri, bir hatayı önlemenin yolunu gösteriyor.*

## Görevler

### Görev 1: TypeError'ı düzelt

Bu kod `TypeError` veriyor. Düzelt ki `Yaşım 12` yazsın.

**Başlangıç kodu:**

```python
age = 12
print("Yaşım " + age)
```

**İpuçları:**

1. Yazı ile sayı + ile birleştirilemez.
2. age'i str(age) ile yazıya çevir ya da f-string kullan.

<details><summary>Çözüm</summary>

```python
age = 12
print("Yaşım " + str(age))
```

</details>

### Görev 2: IndexError'ı düzelt

Bu kod çantadaki son eşyayı yazdırmak istiyor ama hata veriyor. Düzelt. Çanta büyüse de son eşyayı yazdırmalı.

**Başlangıç kodu:**

```python
items = ["kılıç", "kalkan", "iksir"]
print("Son eşya:", items[3])
```

**İpuçları:**

1. Sıra numaraları 0'dan başlar; 3 elemanlı listenin son indeksi 2'dir.
2. Her zaman son elemanı veren kısayol: items[-1]

<details><summary>Çözüm</summary>

```python
items = ["kılıç", "kalkan", "iksir"]
print("Son eşya:", items[-1])
```

</details>

### Görev 3: KeyError'ı düzelt

Sözlükte `gold` anahtarı yok, bu yüzden kod hata veriyor. `get()` kullanarak düzelt: anahtar yoksa `0` yazsın.

**Başlangıç kodu:**

```python
hero = {"name": "Piko", "hp": 100}
print("Altın:", hero["gold"])
```

**İpuçları:**

1. hero.get("gold", 0) anahtar yoksa 0 verir.

<details><summary>Çözüm</summary>

```python
hero = {"name": "Piko", "hp": 100}
print("Altın:", hero.get("gold", 0))
```

</details>

## Challenge: Sıfıra bölme

`average(nums)` ortalamayı döndürüyor ama boş listede `ZeroDivisionError` veriyor. Liste boşsa `0` döndürecek şekilde düzelt.

**Başlangıç kodu:**

```python
def average(nums):
    return sum(nums) / len(nums)

print(average([2, 4, 6]))
print(average([]))
```

**İpuçları:**

1. Bölmeden önce listenin boş olup olmadığına bak.
2. if len(nums) == 0: return 0

<details><summary>Çözüm</summary>

```python
def average(nums):
    if len(nums) == 0:
        return 0
    return sum(nums) / len(nums)

print(average([2, 4, 6]))
print(average([]))
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Hata avı**

### Piko'nun Macerası: Hata avı

Piko'nun oyununa üç hata sızmış! Kodu çalıştır, hata mesajlarını oku ve tek tek düzelt. Düzgün çalıştığında şöyle yazmalı:

```
Oyuncu: Piko
Can: 100
İlk eşya: kılıç
```

**Başlangıç kodu:**

```python
player = {"name": "Piko", "hp": 100}
items = ["kılıç", "iksir"]

print("Oyuncu: " + plyer["name"])
print("Can: " + player["hp"])
print("İlk eşya: " + items[1])
```

**İpuçları:**

1. Birinci hata NameError: değişkenin adına dikkatle bak.
2. İkinci hata TypeError: sayıyı str() ile yazıya çevir.
3. Üçüncü hata sonuç hatası: ilk eleman items[0]

<details><summary>Çözüm</summary>

```python
player = {"name": "Piko", "hp": 100}
items = ["kılıç", "iksir"]

print("Oyuncu: " + player["name"])
print("Can: " + str(player["hp"]))
print("İlk eşya: " + items[0])
```

</details>

### Harcama Defteri: Rapordaki hatalar

Harcama raporuna üç hata sızmış! Kodu çalıştır, hata mesajlarını oku ve tek tek düzelt. Düzgün çalıştığında şöyle yazmalı:

```
Sahip: Ece
Toplam: 465 TL
İlk harcama: 120 TL
```

**Başlangıç kodu:**

```python
owner = "Ece"
amounts = [120, 45, 300]
print("Sahip: " + ownr)
print("Toplam: " + sum(amounts) + " TL")
print(f"İlk harcama: {amounts[3]} TL")
```

**İpuçları:**

1. NameError: değişkenin adını doğru yaz.
2. TypeError: yazı ile sayıyı + ile birleştirmek için str() kullan. IndexError: ilk elemanın indeksi 0.

<details><summary>Çözüm</summary>

```python
owner = "Ece"
amounts = [120, 45, 300]
print("Sahip: " + owner)
print("Toplam: " + str(sum(amounts)) + " TL")
print(f"İlk harcama: {amounts[0]} TL")
```

</details>

### Görev Asistanı: Asistandaki hatalar

Asistanın koduna üç hata sızmış! Kodu çalıştır, hata mesajlarını oku ve düzelt. Düzgün çalışınca şöyle yazmalı:

```
Kullanıcı: Ece
Görev sayısı: 3
İlk görev: Kahve
```

**Başlangıç kodu:**

```python
user = {"name": "Ece"}
tasks = ["Kahve", "Rapor yaz", "Spor"]
print("Kullanıcı: " + user["isim"])
print("Görev sayısı: " + len(tasks))
print("İlk görev: " + task[0])
```

**İpuçları:**

1. KeyError: sözlükte olan anahtarı kullan.
2. TypeError için str(); NameError için değişkenin doğru adı: tasks

<details><summary>Çözüm</summary>

```python
user = {"name": "Ece"}
tasks = ["Kahve", "Rapor yaz", "Spor"]
print("Kullanıcı: " + user["name"])
print("Görev sayısı: " + str(len(tasks)))
print("İlk görev: " + tasks[0])
```

</details>

### Kişisel Web Sitem: Site özetindeki hatalar

Site özetine üç hata sızmış! Kodu çalıştır, hata mesajlarını oku ve tek tek düzelt. Düzgün çalıştığında şöyle yazmalı:

```
Site: Kod Günlüğüm
Yazı sayısı: 3
En yeni yazı: Python Notlarım
```

**Başlangıç kodu:**

```python
site_title = "Kod Günlüğüm"
posts = ["Merhaba Dünya", "Kodla Oyna", "Python Notlarım"]
print("Site: " + site_titel)
print("Yazı sayısı: " + len(posts))
print(f"En yeni yazı: {posts[3]}")
```

**İpuçları:**

1. NameError: değişkenin adını doğru yaz.
2. TypeError: yazı ile sayıyı + ile birleştirmek için str() kullan. IndexError: son eleman için posts[-1] yaz.

<details><summary>Çözüm</summary>

```python
site_title = "Kod Günlüğüm"
posts = ["Merhaba Dünya", "Kodla Oyna", "Python Notlarım"]
print("Site: " + site_title)
print("Yazı sayısı: " + str(len(posts)))
print(f"En yeni yazı: {posts[-1]}")
```

</details>

### Sohbet Botu: Bottaki hatalar

Botun koduna üç hata sızmış! Kodu çalıştır, hata mesajlarını oku ve tek tek düzelt. Son satır, konuşmadaki **ilk** mesajın cevabını yazmalı. Düzgün çalıştığında şöyle yazmalı:

```
Bot: Bilge
Mesaj sayısı: 3
İlk cevap: Merhaba!
```

**Başlangıç kodu:**

```python
bot_name = "Bilge"
replies = {"selam": "Merhaba!", "veda": "Görüşürüz!"}
history = ["selam", "hava", "veda"]
print("Bot: " + bot_nme)
print("Mesaj sayısı: " + len(history))
print("İlk cevap: " + replies[history[3]])
```

**İpuçları:**

1. NameError: değişkenin adını doğru yaz. TypeError: yazı ile sayıyı + ile birleştirmek için str() kullan.
2. IndexError: listenin ilk elemanının indeksi 0.

<details><summary>Çözüm</summary>

```python
bot_name = "Bilge"
replies = {"selam": "Merhaba!", "veda": "Görüşürüz!"}
history = ["selam", "hava", "veda"]
print("Bot: " + bot_name)
print("Mesaj sayısı: " + str(len(history)))
print("İlk cevap: " + replies[history[0]])
```

</details>

### Okul Not Defteri: Not özetindeki hatalar

Not özetine üç hata sızmış! Kodu çalıştır, hata mesajlarını oku ve tek tek düzelt. Düzgün çalıştığında şöyle yazmalı:

```
Öğrenci: Ece
Ders sayısı: 2
Matematik notu: 85
```

**Başlangıç kodu:**

```python
student = "Ece"
grades = {"Matematik": 85, "Fizik": 70}
print("Öğrenci: " + studnet)
print("Ders sayısı: " + len(grades))
print(f"Matematik notu: {grades['matematik']}")
```

**İpuçları:**

1. NameError: değişkenin adını doğru yaz.
2. TypeError: yazı ile sayıyı + ile birleştirmek için str() kullan. KeyError: sözlükteki anahtar büyük harfle başlıyor.

<details><summary>Çözüm</summary>

```python
student = "Ece"
grades = {"Matematik": 85, "Fizik": 70}
print("Öğrenci: " + student)
print("Ders sayısı: " + str(len(grades)))
print(f"Matematik notu: {grades['Matematik']}")
```

</details>
