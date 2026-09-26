# Gün 17: Hata yönetimi

**Kurs:** 30 Günde Python  ·  **Bölge:** Keşif Adası  ·  **Maskot:** Piko

**Bugünün hedefi:** try, except, else ve finally ile hataları yakalamak; raise ile kendi hatanı oluşturmak

> Keşif Adası'nda köprüler çürük olabilir. Akıllı bir kaşif her adımda düşmemek için bir ip bağlar. Python'da da bu ip var: bir hata olursa program çökmek yerine ipe tutunur ve ne yapacağını bilir. Bugün **hata yönetimini** öğreniyoruz.

![Keşif Adası](../../gorseller/python/harita/ada.webp)

## Konu anlatımı

### try ve except

Hata çıkabilecek kodu `try` içine, hata olursa ne yapılacağını `except` içine yazarız:

```python
text = "on iki"
try:
    age = int(text)
    print("Yaşın:", age)
except ValueError:
    print("Lütfen rakamla yaz.")
```

Hata olursa program çökmez; `except` bloğu çalışır ve devam eder.

### Hangi hatayı yakalıyorsun?

`except` yanına hata tipini yaz. Farklı hatalar için farklı cevaplar verebilirsin:

```python
try:
    result = 10 / int(text)
except ValueError:
    print("Sayı değil!")
except ZeroDivisionError:
    print("Sıfıra bölünmez!")
```

Hata mesajını görmek istersen: `except ValueError as err: print(err)`

Sadece `except:` yazıp her hatayı yakalamak kolaydır ama gerçek hataları gizler. Beklediğin hatayı yaz.

### else ve finally

- `else`: hiç hata olmazsa çalışır
- `finally`: hata olsa da olmasa da **her zaman** çalışır

```python
try:
    n = int("5")
except ValueError:
    print("Hata!")
else:
    print("Başarılı:", n)
finally:
    print("Kontrol bitti.")
```

### raise: kendi hatanı fırlat

Bazen yanlış bir değer gelince **bilerek** hata vermek isteriz:

```python
def set_hp(value):
    if value < 0:
        raise ValueError("Can negatif olamaz")
    return value
```

Böylece hata erken, anlaşılır bir mesajla yakalanır.

## Örnekler

### Çökmeyen program

```python
answers = ["12", "on iki", "7"]
for text in answers:
    try:
        age = int(text)
        print("Yaş:", age)
    except ValueError:
        print(f"'{text}' bir sayı değil.")
```

### İki hata tipi

```python
for text in ["5", "0", "beş"]:
    try:
        print(100 / int(text))
    except ValueError:
        print("Sayı değil!")
    except ZeroDivisionError:
        print("Sıfıra bölünmez!")
```

### raise ve yakalama

```python
def set_hp(value):
    if value < 0:
        raise ValueError("Can negatif olamaz")
    return value

try:
    set_hp(-5)
except ValueError as err:
    print("Yakalandı:", err)
finally:
    print("Kontrol bitti.")
```

## Görevler

### Görev 1: Güvenli sayı

`text` sayıya çevrilebiliyorsa iki katını yazdır. Çevrilemiyorsa program çökmesin, `Bu bir sayı değil!` yazsın.

**Başlangıç kodu:**

```python
text = "abc"

number = int(text)
print(number * 2)
```

**İpuçları:**

1. int(text) satırını try: bloğunun içine al.
2. except ValueError: altına mesajı yaz.

<details><summary>Çözüm</summary>

```python
text = "abc"

try:
    number = int(text)
    print(number * 2)
except ValueError:
    print("Bu bir sayı değil!")
```

</details>

### Görev 2: Güvenli bölme

`safe_divide(a, b)` bölmenin sonucunu döndürsün. `b` sıfırsa hata vermek yerine `None` döndürsün. `if` değil, `try` kullan.

**Başlangıç kodu:**

```python
def safe_divide(a, b):
    return a / b

print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

**İpuçları:**

1. try: return a / b
2. except ZeroDivisionError: return None

<details><summary>Çözüm</summary>

```python
def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return None

print(safe_divide(10, 2))
print(safe_divide(10, 0))
```

</details>

### Görev 3: Yaşını sor

Kullanıcıdan yaşını iste. Rakamla yazarsa `Yaşın: 12`, yazamazsa `Lütfen rakamla yaz.` göster. Girdi kutusuna farklı cevaplar yazıp dene.

**Başlangıç kodu:**

```python
age = int(input("Kaç yaşındasın? "))
print("Yaşın:", age)
```

**İpuçları:**

1. input satırını try içine al.
2. except ValueError: ile yakala.

<details><summary>Çözüm</summary>

```python
try:
    age = int(input("Kaç yaşındasın? "))
    print("Yaşın:", age)
except ValueError:
    print("Lütfen rakamla yaz.")
```

</details>

## Challenge: raise ile koru

`set_level(level)` 1 ile 10 arasındaki seviyeleri döndürsün. Bunun dışındaki bir değer gelirse `ValueError` fırlatsın.

**Başlangıç kodu:**

```python
def set_level(level):
    return level

print(set_level(3))
```

**İpuçları:**

1. if level < 1 or level > 10:
2. raise ValueError("...")

<details><summary>Çözüm</summary>

```python
def set_level(level):
    if level < 1 or level > 10:
        raise ValueError("Seviye 1 ile 10 arasında olmalı")
    return level

print(set_level(3))
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Sağlam komutlar**

### Piko'nun Macerası: Sağlam komutlar

Oyuncu kaç adım gideceğini yazıyor ama bazen harf yazıyor. `commands` listesindeki her komutu sayıya çevirmeye çalış:

- Sayıysa `moved`'a ekle.
- Değilse `'iki' anlaşılmadı` yazdır ve devam et.
- En sonda `Toplam adım: 8` yazdır.

**Başlangıç kodu:**

```python
commands = ["3", "iki", "5", "hop"]
moved = 0

# Her komutu dene

print(f"Toplam adım: {moved}")
```

**İpuçları:**

1. for c in commands: içinde try kullan.
2. except ValueError: içinde mesajı yazdır.

<details><summary>Çözüm</summary>

```python
commands = ["3", "iki", "5", "hop"]
moved = 0

for c in commands:
    try:
        moved += int(c)
    except ValueError:
        print(f"'{c}' anlaşılmadı")

print(f"Toplam adım: {moved}")
```

</details>

### Harcama Defteri: Güvenli tutar girişi

Tutarlar bir formdan yazı olarak geliyor ve bazıları hatalı. `entries` listesindeki her girişi `float()` ile sayıya çevirmeye çalış:

- Çevrilebiliyorsa `total`'a ekle.
- Çevrilemiyorsa `'abc' geçersiz` yazdır ve devam et.
- En sonda `Toplam: 165.5` yazdır.

**Başlangıç kodu:**

```python
entries = ["120", "abc", "45.5", ""]
total = 0
```

**İpuçları:**

1. Çevirme işini try: bloğuna koy.
2. float("abc") ValueError verir: except ValueError:

<details><summary>Çözüm</summary>

```python
entries = ["120", "abc", "45.5", ""]
total = 0
for entry in entries:
    try:
        total += float(entry)
    except ValueError:
        print(f"'{entry}' geçersiz")
print("Toplam:", total)
```

</details>

### Görev Asistanı: Saatleri güvenle okuma

Hatırlatma saatleri `"09:30"` gibi yazı olarak geliyor ama bazıları hatalı. `times` listesindeki her birini `split(":")` ve `int()` ile `(saat, dakika)` tuple'ına çevirmeye çalış:

- Çevrilebilirse `parsed` listesine ekle.
- Çevrilemezse (`ValueError`) `'öğlen' geçersiz saat` yazdır ve devam et.
- En sonda `2 saat okundu` gibi yazdır.

**Başlangıç kodu:**

```python
times = ["09:30", "öğlen", "17:45", "yarın"]
parsed = []
```

**İpuçları:**

1. "09:30".split(":") -> ["09", "30"]
2. "öğlen".split(":") tek parça verir; iki değişkene açarken ValueError olur.

<details><summary>Çözüm</summary>

```python
times = ["09:30", "öğlen", "17:45", "yarın"]
parsed = []
for text in times:
    try:
        hour, minute = text.split(":")
        parsed.append((int(hour), int(minute)))
    except ValueError:
        print(f"'{text}' geçersiz saat")
print(f"{len(parsed)} saat okundu")
```

</details>

### Kişisel Web Sitem: Güvenli yazı girişi

Yazılar bir formdan geliyor ve bazıları hatalı. `forms` listesindeki her form için `(form["title"], int(form["words"]))` tuple'ını `posts` listesine eklemeye çalış:

- Başlık yoksa `KeyError` olur: `Başlık eksik, atlandı` yazdır.
- Kelime sayısı sayı değilse `ValueError` olur: `Geçersiz kelime sayısı: çok` gibi yazdır.
- En sonda `2 yazı eklendi` gibi yazdır.

**Başlangıç kodu:**

```python
forms = [{"title": "Merhaba Dünya", "words": "350"}, {"title": "Kodla Oyna", "words": "çok"}, {"words": "120"}, {"title": "Kısa Not", "words": "90"}]
posts = []
```

**İpuçları:**

1. Eklemeyi try: bloğuna koy; altına iki ayrı except yaz.
2. except KeyError: ve except ValueError: farklı hataları ayrı yakalar.

<details><summary>Çözüm</summary>

```python
forms = [{"title": "Merhaba Dünya", "words": "350"}, {"title": "Kodla Oyna", "words": "çok"}, {"words": "120"}, {"title": "Kısa Not", "words": "90"}]
posts = []
for form in forms:
    try:
        posts.append((form["title"], int(form["words"])))
    except KeyError:
        print("Başlık eksik, atlandı")
    except ValueError:
        print(f"Geçersiz kelime sayısı: {form['words']}")
print(f"{len(posts)} yazı eklendi")
```

</details>

### Sohbet Botu: Hesap yeteneği

Botumuza hesap yapmayı öğretelim: kullanıcı `"12 / 4"` gibi bir bölme yazıyor. `calc(message)`:

- Mesajı `"/"` işaretinden böl (`message.split("/")`), iki parçayı `float()` ile sayıya çevir ve birinciyi ikinciye böl. `Sonuç: 3.0` döndür.
- Parçalar sayıya çevrilemezse (`ValueError`): `Sayıları anlayamadım.`
- İkinci sayı 0 ise (`ZeroDivisionError`): `Sıfıra bölemem!`

Sonra `messages` listesindeki her mesaj için `calc`'ın cevabını yazdır.

**Başlangıç kodu:**

```python
messages = ["12 / 4", "5 / 0", "on / 2"]


def calc(message):
    pass
```

**İpuçları:**

1. Çevirme ve bölme işini try: bloğuna koy.
2. Her hata tipi için ayrı bir except yazabilirsin: except ValueError: ve except ZeroDivisionError:

<details><summary>Çözüm</summary>

```python
messages = ["12 / 4", "5 / 0", "on / 2"]


def calc(message):
    parts = message.split("/")
    try:
        result = float(parts[0]) / float(parts[1])
    except ValueError:
        return "Sayıları anlayamadım."
    except ZeroDivisionError:
        return "Sıfıra bölemem!"
    return f"Sonuç: {result}"


for message in messages:
    print(calc(message))
```

</details>

### Okul Not Defteri: Güvenli not girişi

Notlar bir formdan yazı olarak geliyor ve bazıları hatalı.

- `parse_grade(text)`: yazıyı `int()` ile sayıya çevirsin. Not 0'dan küçük ya da 100'den büyükse `raise ValueError(...)` ile hata fırlatsın. Geçerliyse notu döndürsün.
- `entries` listesindeki her girişi `parse_grade` ile çevirmeye çalış: geçerliyse `grades`'e ekle, `ValueError` olursa `'yüz' geçersiz` yazdır ve devam et.
- En sonda `Geçerli notlar: [85, 70]` yazdır.

**Başlangıç kodu:**

```python
def parse_grade(text):
    pass


entries = ["85", "yüz", "70", "120", ""]
grades = []
```

**İpuçları:**

1. int("yüz") zaten ValueError verir; 0-100 dışı için if ... raise ValueError("...") yaz.
2. Döngüde çevirme işini try: bloğuna koy, except ValueError: ile yakala.

<details><summary>Çözüm</summary>

```python
def parse_grade(text):
    grade = int(text)
    if grade < 0 or grade > 100:
        raise ValueError("not 0 ile 100 arasında olmalı")
    return grade


entries = ["85", "yüz", "70", "120", ""]
grades = []
for entry in entries:
    try:
        grades.append(parse_grade(entry))
    except ValueError:
        print(f"'{entry}' geçersiz")
print("Geçerli notlar:", grades)
```

</details>
