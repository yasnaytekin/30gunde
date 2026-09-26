# Gün 2: Değişkenler ve hazır fonksiyonlar

**Kurs:** 30 Günde Python  ·  **Bölge:** Başlangıç Kampı  ·  **Maskot:** Piko

**Bugünün hedefi:** Değişken oluşturmak, veri tiplerini tanımak, girdi almak ve hazır fonksiyonları kullanmak

> Oyunumuzun bir kahramanı olacak. Ama bilgisayar kahramanın adını, canını, altınını nasıl hatırlayacak? Bugün bilgisayarın hafızasında etiketli kutular açacağız. Bunlara **değişken** diyoruz!

![Başlangıç Kampı](../../gorseller/python/harita/kamp.webp)

## Konu anlatımı

### Değişken: etiketli bir kutu

Bir değişken, içine bilgi koyduğun etiketli bir kutudur.

```python
name = "Piko"
hp = 100
```

Buradaki `=` işareti matematikteki eşittir değildir. "Sağdaki değeri soldaki kutuya koy" demektir. Sonra kutunun adını yazarak içindekini kullanırsın: `print(name)`

### İsim verme kuralları

- Harfle ya da `_` ile başlar: `score`, `_gizli`
- Boşluk olmaz, yerine `_` kullan: `player_name`
- Büyük/küçük harf farklıdır: `Score` ile `score` ayrı kutulardır
- Türkçe karakterleri (ş, ğ, ı...) değişken adlarında kullanmamak iyi bir alışkanlıktır
- Anlamlı isim seç: `x` yerine `gold`

### Veri tipleri

Kutulara farklı türde bilgiler koyabilirsin:

- `str` (yazı): `"Piko"`
- `int` (tam sayı): `100`
- `float` (ondalıklı sayı): `3.5`
- `bool` (doğru/yanlış): `True` ya da `False`

Bir değerin tipini öğrenmek için `type()` kullanılır: `print(type(100))`

### Kutunun içini değiştirmek

Değişkene yeni bir değer verince eskisinin yerine geçer:

```python
gold = 10
gold = gold + 5
print(gold)  # 15
```

### Kullanıcıdan bilgi almak

`input()` kullanıcıdan bir cevap ister. Gelen cevap **her zaman yazıdır** (str). Sayıya çevirmek için `int()` kullanırız:

```python
age = int(input("Kaç yaşındasın? "))
```

Bu sitede `input()` kullanınca cevaplarını editörün altındaki **Girdi** kutusuna yaz. Her satır bir cevaptır.

Tersini de yapabilirsin: `str(12)` sayıyı yazıya çevirir.

### Python'ın hazır fonksiyonları

Python'ın içinde kullanıma hazır birçok fonksiyon gelir. Bunlara **hazır fonksiyonlar** (built-in functions) denir. Şimdiye kadar `print()`, `input()`, `type()`, `int()` ve `str()` ile tanıştın. Birkaç tane daha:

- `len("Piko")` bir yazının uzunluğunu verir: `4`
- `float("2.5")` yazıyı ondalıklı sayıya çevirir
- `round(7.6)` en yakın tam sayıya yuvarlar: `8`
- `max(3, 9, 4)` en büyüğü, `min(3, 9, 4)` en küçüğü verir

Bir fonksiyonun ne yaptığını unutursan `help(len)` yazıp çalıştırabilirsin.

## Örnekler

### Kahramanın kutuları

```python
name = "Piko"
hp = 100
speed = 2.5
is_alive = True
print(name, hp, speed, is_alive)
print(type(name))
print(type(hp))
```

### Değeri güncelle

```python
gold = 10
print("Başta:", gold)
gold = gold + 25
print("Hazineden sonra:", gold)
```

### Girdi alalım

```python
name = input("Adın ne? ")
print("Merhaba", name)
```

*Girdi kutusundaki adı değiştirip tekrar çalıştır.*

### Hazır fonksiyonlar

```python
name = "Piko"
print(len(name))
print(float("2.5") + 1)
print(round(7.6))
print(max(3, 9, 4), min(3, 9, 4))
```

*Her satırın sonucunu çalıştırmadan önce tahmin etmeye çalış.*

## Görevler

### Görev 1: Kutuyu doldur

`name` değişkeninin içine kendi adını koy ve çalıştır.

**Başlangıç kodu:**

```python
name = "Ahmet"
print(name)
```

**İpuçları:**

1. Sadece tırnakların içindeki adı değiştir.
2. Örnek: name = "Zeynep"

<details><summary>Çözüm</summary>

```python
name = "Deniz"
print(name)
```

</details>

### Görev 2: Kahraman kartı

Üç değişken oluştur: `hero` (kahramanın adı, yazı), `age` (yaşı, tam sayı) ve `hp` (değeri 100). Sonra üçünü de `print()` ile yazdır.

**Başlangıç kodu:**

```python
# Değişkenleri burada oluştur
```

**İpuçları:**

1. Her değişken ayrı bir satırda: hero = ...
2. age tırnaksız bir sayı olmalı: age = 12
3. Hepsini yazdırmak için: print(hero, age, hp)

<details><summary>Çözüm</summary>

```python
hero = "Piko"
age = 12
hp = 100
print(hero, age, hp)
```

</details>

### Görev 3: Tip dedektifi

Bu kod hata veriyor çünkü yazı ile sayı toplanamaz. `a`'yı sayıya çevirerek `total` değerinin 10 olmasını sağla. `a = "7"` satırını değiştirme.

**Başlangıç kodu:**

```python
a = "7"
b = 3
total = a + b  # Bu satır hata veriyor!
print(total)
```

**İpuçları:**

1. Hata mesajını oku: str ile int toplanamıyor.
2. int() yazıyı sayıya çevirir.
3. total = int(a) + b

<details><summary>Çözüm</summary>

```python
a = "7"
b = 3
total = int(a) + b
print(total)
```

</details>

### Sahne görevi: Değişkenli ordu

Ordunun genişliği `genislik` değişkeninde duruyor. **3 satır** yazdır; her satırda `genislik` kadar Piko olsun. Yıldızları elle sayma: `"*" * genislik` yan yana `genislik` tane yıldız yazar.

Değişkeni `genislik = 6` yaparsan ordu kendiliğinden genişlemeli!

**Başlangıç kodu:**

```python
genislik = 4

print("****")
```

**İpuçları:**

1. Bir satır: print("*" * genislik)
2. Bu satırı üç kez yaz.

<details><summary>Çözüm</summary>

```python
genislik = 4

print("*" * genislik)
print("*" * genislik)
print("*" * genislik)
```

</details>

## Challenge: Kutuları değiştir

Eline iki bardak verdiler, birinde süt var diğerinde meyve suyu. İçeriklerini değiştirmek için üçüncü bir bardak gerekir, değil mi? `a` ve `b` değişkenlerinin içeriğini yer değiştir. "elma" ve "armut" kelimelerini bir daha yazmak yok!

**Başlangıç kodu:**

```python
a = "elma"
b = "armut"
# a ile b'nin içeriğini değiştir

print(a, b)
```

**İpuçları:**

1. Üçüncü bir değişken oluştur: temp = a
2. Sonra a'ya b'yi, b'ye de temp'i koy.

<details><summary>Çözüm</summary>

```python
a = "elma"
b = "armut"
temp = a
a = b
b = temp
print(a, b)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Oyuncu bilgileri**

### Piko'nun Macerası: Oyuncu bilgileri

Kahramanımızın bilgilerini değişkenlerde tutalım:

- `player_name`: kahramanın adı
- `player_hp`: 100
- `player_gold`: 0
- `player_level`: 1

Sonra `Kahraman: Piko` gibi bir satır yazdır (ad değişkenden gelsin).

**Başlangıç kodu:**

```python
# Kahramanın bilgileri
```

**İpuçları:**

1. Dört değişkeni tek tek oluştur.
2. print("Kahraman:", player_name)

<details><summary>Çözüm</summary>

```python
player_name = "Piko"
player_hp = 100
player_gold = 0
player_level = 1
print("Kahraman:", player_name)
```

</details>

### Harcama Defteri: Bütçe bilgileri

Defterin bilgilerini değişkenlerde tutalım:

- `owner`: defterin sahibi (senin adın)
- `budget`: aylık bütçe, `5000`
- `currency`: `"TL"`

Sonra değişkenleri kullanarak şu iki satırı yazdır:

```
Sahip: Ece
Bütçe: 5000 TL
```

**Başlangıç kodu:**

```python
owner = "Ece"
# budget ve currency değişkenlerini ekle
```

**İpuçları:**

1. budget = 5000 bir sayı, currency = "TL" bir yazı.
2. print("Bütçe:", budget, currency) virgüllerin yerine boşluk koyar.

<details><summary>Çözüm</summary>

```python
owner = "Ece"
budget = 5000
currency = "TL"
print("Sahip:", owner)
print("Bütçe:", budget, currency)
```

</details>

### Görev Asistanı: Kullanıcı bilgileri

Asistanın bilgilerini değişkenlerde tutalım:

- `user_name`: senin adın
- `task_count`: bugünkü görev sayısı, `3`
- `work_hours`: bugün çalışacağın saat, `6`

Sonra değişkenleri kullanarak şöyle yazdır:

```
Merhaba, Ece
Bugün 3 görevin var.
```

**Başlangıç kodu:**

```python
user_name = "Ece"
# task_count ve work_hours değişkenlerini ekle
```

**İpuçları:**

1. task_count = 3 ve work_hours = 6 sayı.
2. print("Bugün", task_count, "görevin var.")

<details><summary>Çözüm</summary>

```python
user_name = "Ece"
task_count = 3
work_hours = 6
print("Merhaba,", user_name)
print("Bugün", task_count, "görevin var.")
```

</details>

### Kişisel Web Sitem: Site bilgileri

Sitenin bilgilerini değişkenlerde tutalım:

- `owner`: sitenin sahibi (senin adın)
- `site_title`: sitenin adı, `"Kod Günlüğüm"`
- `year`: bu yıl, `2026`

Sonra değişkenleri kullanarak sayfanın üst yazısını (site adı) ve alt yazısını yazdır:

```
Kod Günlüğüm
© 2026 Ece
```

**Başlangıç kodu:**

```python
owner = "Ece"
# site_title ve year değişkenlerini ekle
```

**İpuçları:**

1. site_title = "Kod Günlüğüm" bir yazı, year = 2026 bir sayı.
2. print("©", year, owner) virgüllerin yerine boşluk koyar.

<details><summary>Çözüm</summary>

```python
owner = "Ece"
site_title = "Kod Günlüğüm"
year = 2026
print(site_title)
print("©", year, owner)
```

</details>

### Sohbet Botu: Bot ayarları

Botun ayarlarını değişkenlerde tutalım:

- `bot_name`: botun adı, `"Bilge"`
- `version`: sürüm numarası, `1`
- `user`: botla konuşan kişinin adı (senin adın)

Sonra değişkenleri kullanarak şu üç satırı yazdır:

```
Bot: Bilge
Sürüm: 1
Bilge diyor ki: Merhaba Ece
```

**Başlangıç kodu:**

```python
bot_name = "Bilge"
# version ve user değişkenlerini ekle
```

**İpuçları:**

1. version = 1 bir sayı, user = "Ece" bir yazı.
2. print(bot_name, "diyor ki: Merhaba", user) virgüllerin yerine boşluk koyar.

<details><summary>Çözüm</summary>

```python
bot_name = "Bilge"
version = 1
user = "Ece"
print("Bot:", bot_name)
print("Sürüm:", version)
print(bot_name, "diyor ki: Merhaba", user)
```

</details>

### Okul Not Defteri: Öğrenci bilgileri

Defterin sahibinin bilgilerini değişkenlerde tutalım:

- `student`: öğrencinin adı (senin adın)
- `grade_level`: sınıfın, `10`
- `lesson_count`: bu dönem aldığın ders sayısı, `8`

Sonra değişkenleri kullanarak şu üç satırı yazdır:

```
Öğrenci: Ece
Sınıf: 10
Ders sayısı: 8
```

**Başlangıç kodu:**

```python
student = "Ece"
# grade_level ve lesson_count değişkenlerini ekle
```

**İpuçları:**

1. grade_level = 10 ve lesson_count = 8 birer sayı.
2. print("Sınıf:", grade_level) virgülün yerine boşluk koyar.

<details><summary>Çözüm</summary>

```python
student = "Ece"
grade_level = 10
lesson_count = 8
print("Öğrenci:", student)
print("Sınıf:", grade_level)
print("Ders sayısı:", lesson_count)
```

</details>
