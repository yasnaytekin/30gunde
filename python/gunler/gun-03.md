# Gün 3: Operatörler

**Kurs:** 30 Günde Python  ·  **Bölge:** Python Köyü  ·  **Maskot:** Piko

**Bugünün hedefi:** Aritmetik, atama, karşılaştırma ve mantık operatörlerini kullanmak

> Python Köyü'ne hoş geldin! Oyunlarda her şey sayılarla döner: skor, can, altın, hız... Bugün köyün pazarında hesapları sen yapacaksın.

![Python Köyü](../../gorseller/python/harita/koy.webp)

## Konu anlatımı

### İki çeşit sayı

`int` tam sayıdır: `7`, `-3`, `1000`. `float` ondalıklı sayıdır: `3.14`, `0.5`. Python'da ondalık için **nokta** kullanılır, virgül değil!

İki tam sayıyı `/` ile bölersen sonuç her zaman float olur: `8 / 2` sonucu `4.0`

### Yeni operatörler

- `//` tam bölme: `7 // 2` sonucu `3`
- `%` kalan: `7 % 2` sonucu `1`
- `**` üs: `3 ** 2` sonucu `9`

`%` çok işe yarar: bir sayının çift olup olmadığını anlamak için `sayi % 2` sonucunun 0 olup olmadığına bakarız.

### İşlem önceliği

Python matematikteki sırayı izler: önce parantez, sonra üs, sonra çarpma ve bölme, en son toplama ve çıkarma.

```python
print(2 + 3 * 4)    # 14
print((2 + 3) * 4)  # 20
```

### Kısayollar

`score = score + 10` yerine `score += 10` yazabilirsin. Aynısı `-=`, `*=` ve `/=` için de geçerli.

### Yardımcı fonksiyonlar

- `round(3.14159, 2)` sonucu `3.14`
- `abs(-5)` sonucu `5`
- `max(4, 9, 2)` sonucu `9`
- `min(4, 9, 2)` sonucu `2`

### Karşılaştırma operatörleri

İki değeri karşılaştırınca Python `True` (doğru) ya da `False` (yanlış) cevabı verir. Bu cevaplara **boolean** denir.

- `==` eşit mi? `!=` eşit değil mi?
- `>` büyük mü? `<` küçük mü?
- `>=` büyük ya da eşit mi? `<=` küçük ya da eşit mi?

```python
print(10 > 3)    # True
print(5 == 7)    # False
```

Tek `=` kutuya değer koymaktır, çift `==` soru sormaktır. Bu ikisini karıştırmak çok yaygın bir hatadır.

### Mantık operatörleri

Birden fazla soruyu birleştirmek için:

- `and`: ikisi de doğruysa `True`
- `or`: en az biri doğruysa `True`
- `not`: cevabı tersine çevirir

```python
gold = 30
print(gold > 10 and gold < 50)   # True
print(not gold > 10)             # False
```

Bu operatörleri 9. günde koşullarla birlikte çok kullanacağız.

## Örnekler

### Bölmenin üç hali

```python
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(2 ** 10)
```

### Skor artıyor

```python
score = 0
score += 10
score += 10
score *= 2
print("Skor:", score)
```

### Yuvarlama

```python
pi = 3.14159
print(round(pi, 2))
print(max(12, 45, 7), min(12, 45, 7))
```

### Doğru mu yanlış mı?

```python
hp = 40
gold = 120
print(hp > 50)
print(gold >= 100)
print(hp > 20 and gold > 100)
print(hp > 50 or gold > 100)
print(not hp > 50)
```

*hp ve gold değerlerini değiştirip cevapların nasıl değiştiğine bak.*

## Görevler

### Görev 1: Pizza paylaşımı

17 dilim pizza 5 arkadaşa eşit paylaştırılacak. `each` her kişinin alacağı dilim sayısı, `left` artan dilim sayısı olsun. Sayıları kendin yazma, `slices` ve `people` değişkenleriyle hesapla.

**Başlangıç kodu:**

```python
slices = 17
people = 5

each = 0   # her kişiye kaç dilim?
left = 0   # kaç dilim artar?

print("Kişi başı:", each)
print("Artan:", left)
```

**İpuçları:**

1. Tam bölme için //, kalan için % kullan.
2. each = slices // people

<details><summary>Çözüm</summary>

```python
slices = 17
people = 5

each = slices // people
left = slices % people

print("Kişi başı:", each)
print("Artan:", left)
```

</details>

### Görev 2: Can iksiri

`hp` 40 ile başlıyor. Önce iksir içip canı 25 artır (`+=`), sonra tuzağa basıp 15 azalt (`-=`).

**Başlangıç kodu:**

```python
hp = 40
# iksir iç: +25

# tuzağa bastın: -15

print("Can:", hp)
```

**İpuçları:**

1. hp += 25 canı 25 artırır.
2. Azaltmak için hp -= 15

<details><summary>Çözüm</summary>

```python
hp = 40
hp += 25
hp -= 15
print("Can:", hp)
```

</details>

### Görev 3: Ortalama

Üç skorun ortalamasını hesapla ve `round()` ile virgülden sonra 1 basamağa yuvarlayarak `average` değişkenine koy.

**Başlangıç kodu:**

```python
score1 = 80
score2 = 95
score3 = 72

average = 0
print(average)
```

**İpuçları:**

1. Ortalama = toplam / adet
2. Toplamı paranteze al: (score1 + score2 + score3) / 3
3. round(sayı, 1) virgülden sonra 1 basamak bırakır.

<details><summary>Çözüm</summary>

```python
score1 = 80
score2 = 95
score3 = 72

average = round((score1 + score2 + score3) / 3, 1)
print(average)
```

</details>

### Sahne görevi: Eşit sıralar

`pikolar` kadar Piko, `sira` kadar satıra **eşit** dağıtılacak. Her satırdaki Piko sayısını tam bölmeyle (`//`) hesapla ve `her_sira` değişkenine koy. Sonra 3 satır yazdır: `"*" * her_sira`.

12 Piko 3 satıra 4'er düşer. `pikolar = 15` olunca her satırda 5 Piko olmalı.

**Başlangıç kodu:**

```python
pikolar = 12
sira = 3
her_sira = 0

print("*" * her_sira)
```

**İpuçları:**

1. her_sira = pikolar // sira
2. Sonra üç kez print("*" * her_sira)

<details><summary>Çözüm</summary>

```python
pikolar = 12
sira = 3
her_sira = pikolar // sira

print("*" * her_sira)
print("*" * her_sira)
print("*" * her_sira)
```

</details>

## Challenge: Saniye çevirici

`seconds` değişkenindeki süreyi saate, dakikaya ve saniyeye çevir. 3725 saniye = 1 saat 2 dakika 5 saniye. İpucu: `//` ve `%` senin en iyi arkadaşların.

**Başlangıç kodu:**

```python
seconds = 3725

hours = 0
minutes = 0
secs = 0

print(hours, "saat", minutes, "dakika", secs, "saniye")
```

**İpuçları:**

1. Bir saatte 3600 saniye var.
2. Saatten artan saniyeler: seconds % 3600
3. Onu 60'a tam bölersen dakikayı bulursun.

<details><summary>Çözüm</summary>

```python
seconds = 3725

hours = seconds // 3600
minutes = seconds % 3600 // 60
secs = seconds % 60

print(hours, "saat", minutes, "dakika", secs, "saniye")
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Skor ve puan**

### Piko'nun Macerası: Skor sistemi

Oyunumuzun skor sistemini kuralım. Kahraman 3 altın topladı ve her altın 10 puan. Önce bu puanları `score`'a ekle, sonra boss yenildiği için skoru 2 katına çıkar.

**Başlangıç kodu:**

```python
score = 0
coin_value = 10
coins = 3

# 1) Toplanan altınların puanını score'a ekle

# 2) Boss yenildi! Skoru 2 katına çıkar

print("Skor:", score)
```

**İpuçları:**

1. Altın puanı: coins * coin_value
2. 2 katına çıkarmak için: score *= 2

<details><summary>Çözüm</summary>

```python
score = 0
coin_value = 10
coins = 3

score += coins * coin_value
score *= 2

print("Skor:", score)
```

</details>

### Harcama Defteri: Kalan bütçe

Bu ay kira, market ve ulaşım için para harcadın.

- `spent`: üç harcamanın toplamı
- `left`: bütçeden kalan (`budget - spent`)
- `percent`: bütçenin yüzde kaçı harcandı (`spent / budget * 100`)

Sonra şöyle yazdır:

```
Harcanan: 3900
Kalan: 1100
Yüzde: 78.0
```

**Başlangıç kodu:**

```python
budget = 5000
rent = 2000
food = 1500
transport = 400
```

**İpuçları:**

1. spent = rent + food + transport
2. percent için / ve * operatörlerini kullan: spent / budget * 100

<details><summary>Çözüm</summary>

```python
budget = 5000
rent = 2000
food = 1500
transport = 400
spent = rent + food + transport
left = budget - spent
percent = spent / budget * 100
print("Harcanan:", spent)
print("Kalan:", left)
print("Yüzde:", percent)
```

</details>

### Görev Asistanı: Toplam süre

Her görev ortalama `minutes_per_task` dakika sürüyor.

- `total_minutes`: görev sayısı × görev başına dakika
- `hours`: tam saat (`//` ile)
- `minutes`: artan dakika (`%` ile)

Sonra `Toplam süre: 2 saat 15 dakika` gibi yazdır.

**Başlangıç kodu:**

```python
task_count = 3
minutes_per_task = 45
```

**İpuçları:**

1. 135 // 60 = 2, 135 % 60 = 15
2. total_minutes = task_count * minutes_per_task

<details><summary>Çözüm</summary>

```python
task_count = 3
minutes_per_task = 45
total_minutes = task_count * minutes_per_task
hours = total_minutes // 60
minutes = total_minutes % 60
print("Toplam süre:", hours, "saat", minutes, "dakika")
```

</details>

### Kişisel Web Sitem: Blog sayfaları

Blog sayfasının her sayfasına `per_page` kadar yazı sığıyor. Toplam `post_count` yazın var.

- `full_pages`: tamamen dolu sayfa sayısı (`//` ile)
- `last_page`: artan, son sayfaya kalan yazı sayısı (`%` ile)
- `needs_extra`: artan yazı var mı? (`last_page > 0`, True ya da False)

Sonra şöyle yazdır:

```
Dolu sayfa: 4
Son sayfada: 3 yazı
Ekstra sayfa gerekli mi: True
```

**Başlangıç kodu:**

```python
post_count = 23
per_page = 5
```

**İpuçları:**

1. 23 // 5 = 4, 23 % 5 = 3
2. needs_extra = last_page > 0 bir karşılaştırma; sonucu True ya da False olur.

<details><summary>Çözüm</summary>

```python
post_count = 23
per_page = 5
full_pages = post_count // per_page
last_page = post_count % per_page
needs_extra = last_page > 0
print("Dolu sayfa:", full_pages)
print("Son sayfada:", last_page, "yazı")
print("Ekstra sayfa gerekli mi:", needs_extra)
```

</details>

### Sohbet Botu: Mesaj uzunluğu

Botlar çok uzun mesajları sevmez; bizim botumuzun sınırı `limit` karakter. Kullanıcının mesajı `message` değişkeninde.

- `length`: mesajın karakter sayısı (`len()`)
- `left`: sınıra kaç karakter kaldı (`limit - length`)
- `too_long`: mesaj sınırdan uzun mu? (`length > limit`, sonuç `True` ya da `False`)

Sonra şöyle yazdır:

```
Uzunluk: 33
Kalan: 127
Çok uzun: False
```

**Başlangıç kodu:**

```python
limit = 160
message = "Merhaba, yarın hava nasıl olacak?"
```

**İpuçları:**

1. length = len(message) mesajdaki karakterleri sayar (boşluklar da sayılır).
2. Karşılaştırmanın sonucu True ya da False'tur: too_long = length > limit

<details><summary>Çözüm</summary>

```python
limit = 160
message = "Merhaba, yarın hava nasıl olacak?"
length = len(message)
left = limit - length
too_long = length > limit
print("Uzunluk:", length)
print("Kalan:", left)
print("Çok uzun:", too_long)
```

</details>

### Okul Not Defteri: Sınav ortalaması

Matematikten üç yazılı sınava girdin: `exam1`, `exam2` ve `exam3`.

- `total`: üç notun toplamı
- `average`: ortalama (`total / 3`), `round()` ile **1 basamağa** yuvarla
- `passed`: ortalama 50 veya üstü mü? (`average >= 50`, sonucu `True` ya da `False`)

Sonra şöyle yazdır:

```
Toplam: 245
Ortalama: 81.7
Geçti mi: True
```

**Başlangıç kodu:**

```python
exam1 = 70
exam2 = 85
exam3 = 90
```

**İpuçları:**

1. total = exam1 + exam2 + exam3
2. average = round(total / 3, 1) ve passed = average >= 50

<details><summary>Çözüm</summary>

```python
exam1 = 70
exam2 = 85
exam3 = 90
total = exam1 + exam2 + exam3
average = round(total / 3, 1)
passed = average >= 50
print("Toplam:", total)
print("Ortalama:", average)
print("Geçti mi:", passed)
```

</details>
