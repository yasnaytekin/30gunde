# Gün 9: Koşullar

**Kurs:** 30 Günde Python  ·  **Bölge:** Mantık Kalesi  ·  **Maskot:** Piko

**Bugünün hedefi:** if, elif ve else ile programın karar vermesini sağlamak

> Mantık Kalesi'nin kapısı sadece anahtarı olanlara açılır! Oyunlarda her şey kurallarla çalışır: can biterse oyun biter, anahtar varsa kapı açılır. Bugün bu kuralları Python'a yazmayı öğreneceğiz.

![Mantık Kalesi](../../gorseller/python/harita/kale.webp)

## Konu anlatımı

### True ve False

Python'a soru sorabilirsin, cevabı `True` (doğru) ya da `False` (yanlış) olur:

- `==` eşit mi? Tek `=` kutuya koymaktır, iki `==` sormaktır!
- `!=` eşit değil mi?
- `>` ve `<` büyük mü, küçük mü?
- `>=` ve `<=` büyük eşit, küçük eşit

```python
hp = 30
print(hp > 50)   # False
print(hp == 30)  # True
```

### if: eğer

```python
if has_key:
    print("Kapı açıldı!")
```

İki şeye dikkat: satırın sonunda **iki nokta** (`:`) var ve alttaki satır **4 boşluk içeride**. Bu boşluğa **girinti** denir; Python hangi satırların if'e ait olduğunu girintiye bakarak anlar. Editörde `:` yazıp Enter'a basınca girinti kendiliğinden gelir.

### else ve elif

`else` "değilse" demektir. Birden fazla durum varsa `elif` ("değilse eğer") kullanırız. Python yukarıdan aşağı bakar ve **ilk doğru olan** bloğu çalıştırır:

```python
if hp > 70:
    print("Güçlüsün")
elif hp > 30:
    print("Dikkatli ol")
else:
    print("İksir iç!")
```

### and, or, not

- `and`: ikisi de doğruysa doğru
- `or`: biri doğruysa doğru
- `not`: tersine çevirir

```python
if has_key and gold >= 10:
    print("Sandık açıldı")
```

Listelerle de koşul yazabilirsin: `if "anahtar" in inventory:`

## Örnekler

### Kapı

```python
has_key = True
if has_key:
    print("Kapı açıldı!")
else:
    print("Kapı kilitli.")
```

*has_key'i False yapıp tekrar çalıştır.*

### Can durumu

```python
hp = 45
if hp > 70:
    print("Güçlüsün")
elif hp > 30:
    print("Dikkatli ol")
else:
    print("İksir iç!")
```

### Yaş sorusu

```python
age = int(input("Kaç yaşındasın? "))
if age >= 13 and age < 20:
    print("Sen bir gençsin!")
else:
    print("Yaşın:", age)
```

*Girdi kutusuna farklı yaşlar yazıp dene.*

## Görevler

### Görev 1: Kalenin kapısı

`has_key` True ise `Kapı açıldı!`, değilse `Kapı kilitli.` yazdır.

**Başlangıç kodu:**

```python
has_key = True

# has_key True ise "Kapı açıldı!", değilse "Kapı kilitli." yazdır
```

**İpuçları:**

1. if has_key: yazıp Enter'a bas.
2. else: bloğu if ile aynı hizada olmalı.

<details><summary>Çözüm</summary>

```python
has_key = True

if has_key:
    print("Kapı açıldı!")
else:
    print("Kapı kilitli.")
```

</details>

### Görev 2: Can göstergesi

`hp` 70'ten büyükse `Güçlüsün`, 30'dan büyükse `Dikkatli ol`, değilse `İksir iç!` yazdır.

**Başlangıç kodu:**

```python
hp = 25

# hp 70'ten büyükse "Güçlüsün"
# 30'dan büyükse "Dikkatli ol"
# değilse "İksir iç!"
```

**İpuçları:**

1. Üç durum var: if, elif ve else.
2. Büyükten küçüğe doğru kontrol et.

<details><summary>Çözüm</summary>

```python
hp = 25

if hp > 70:
    print("Güçlüsün")
elif hp > 30:
    print("Dikkatli ol")
else:
    print("İksir iç!")
```

</details>

### Görev 3: Hazine sandığı

Anahtar varsa **ve** en az 10 altın varsa `Sandık açıldı!`, yoksa `Sandık açılmadı.` yazdır.

**Başlangıç kodu:**

```python
has_key = True
gold = 15

# Anahtar varsa VE en az 10 altın varsa "Sandık açıldı!"
# yoksa "Sandık açılmadı."
```

**İpuçları:**

1. İki koşulu and ile bağla.
2. En az 10: gold >= 10

<details><summary>Çözüm</summary>

```python
has_key = True
gold = 15

if has_key and gold >= 10:
    print("Sandık açıldı!")
else:
    print("Sandık açılmadı.")
```

</details>

### Sahne görevi: Can göstergesi

Oyunlarda can kalplerle gösterilir. Sahnede her `H` bir kalp. `can` değişkenine göre:

- 3 veya fazlaysa `HHH`
- 2 ise `HH`
- 1 ise `H`
- 0 veya daha azsa `Oyun bitti!`

yazdır. Kodun farklı can değerleriyle denenecek.

**Başlangıç kodu:**

```python
can = 3

print("HHH")
```

**İpuçları:**

1. if can >= 3: ile başla
2. Ardından elif can == 2: ve elif can == 1:
3. Geri kalan her şey için else:

<details><summary>Çözüm</summary>

```python
can = 3

if can >= 3:
    print("HHH")
elif can == 2:
    print("HH")
elif can == 1:
    print("H")
else:
    print("Oyun bitti!")
```

</details>

## Challenge: Oyun modu

Kullanıcının yaşını sor. 13 veya daha büyükse `Macera modu açık!`, değilse `Çocuk modu açık!` yazdır. Cevabı editörün altındaki **Girdi** kutusuna yaz.

**Başlangıç kodu:**

```python
age = int(input("Kaç yaşındasın? "))

# 13 veya daha büyükse "Macera modu açık!", değilse "Çocuk modu açık!"
```

**İpuçları:**

1. 13 veya daha büyük: age >= 13
2. if ve else yeterli.

<details><summary>Çözüm</summary>

```python
age = int(input("Kaç yaşındasın? "))

if age >= 13:
    print("Macera modu açık!")
else:
    print("Çocuk modu açık!")
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Oyun kuralları**

### Piko'nun Macerası: Oyun kuralları

Oyunumuzun kurallarını yazalım. `hero` sözlüğüne bak:

- Can 0 veya altındaysa `Oyun bitti!`
- Değilse ve altın 100 veya fazlaysa `Kazandın!`
- İkisi de değilse `Maceraya devam!`

**Başlangıç kodu:**

```python
hero = {"name": "Piko", "hp": 100, "gold": 40}

# Kurallar:
# can 0 veya altındaysa  -> "Oyun bitti!"
# altın 100 veya fazlaysa -> "Kazandın!"
# yoksa                   -> "Maceraya devam!"
```

**İpuçları:**

1. Can: hero["hp"], altın: hero["gold"]
2. Önce canı kontrol et: if hero["hp"] <= 0:

<details><summary>Çözüm</summary>

```python
hero = {"name": "Piko", "hp": 100, "gold": 40}

if hero["hp"] <= 0:
    print("Oyun bitti!")
elif hero["gold"] >= 100:
    print("Kazandın!")
else:
    print("Maceraya devam!")
```

</details>

### Harcama Defteri: Bütçe uyarısı

Programımız bütçe durumunu söylesin:

- `spent`, `budget`'tan büyükse: `Bütçe aşıldı!`
- Değilse ve `spent`, bütçenin %80'i veya fazlasıysa: `Dikkat: bütçenin %80'i harcandı.`
- İkisi de değilse: `Bütçe yolunda.`

**Başlangıç kodu:**

```python
budget = 5000
spent = 4200
```

**İpuçları:**

1. Bütçenin %80'i: budget * 0.8
2. Sıra önemli: önce aşıldı mı diye bak, sonra %80'e.

<details><summary>Çözüm</summary>

```python
budget = 5000
spent = 4200
if spent > budget:
    print("Bütçe aşıldı!")
elif spent >= budget * 0.8:
    print("Dikkat: bütçenin %80'i harcandı.")
else:
    print("Bütçe yolunda.")
```

</details>

### Görev Asistanı: Akıllı selam

Asistan saate göre selam versin (`hour`, 0-23):

- 12'den küçükse `Günaydın!`
- 18'den küçükse `İyi günler!`
- Değilse `İyi akşamlar!`

Sonra `pending` (kalan görev) 0 ise `Bugünlük bu kadar, dinlen.`, değilse `3 görev seni bekliyor.` gibi yazdır.

**Başlangıç kodu:**

```python
hour = 9
pending = 3
```

**İpuçları:**

1. İlk koşul hour < 12, sonra elif hour < 18.
2. İkinci bir if bloğu kalan görevlere baksın.

<details><summary>Çözüm</summary>

```python
hour = 9
pending = 3
if hour < 12:
    print("Günaydın!")
elif hour < 18:
    print("İyi günler!")
else:
    print("İyi akşamlar!")
if pending == 0:
    print("Bugünlük bu kadar, dinlen.")
else:
    print(f"{pending} görev seni bekliyor.")
```

</details>

### Kişisel Web Sitem: Yayına hazır mı?

Bir yazı ancak kurallara uyarsa yayına girsin. Sırayla kontrol et:

- `title` boşsa (`""`): `Başlık eksik!`
- Değilse ve `draft` True ise: `Taslak, yayınlanmadı.`
- Değilse ve `words` 300'den azsa: `Çok kısa: en az 300 kelime olmalı.`
- Hiçbiri değilse: `Yayına hazır!`

Her durumda yalnızca bir satır yazdır.

**Başlangıç kodu:**

```python
title = "Merhaba Dünya"
draft = False
words = 450
```

**İpuçları:**

1. if / elif / elif / else: ilk doğru olan dal çalışır, diğerleri atlanır.
2. Boş başlık için title == "" ya da not title yazabilirsin.

<details><summary>Çözüm</summary>

```python
title = "Merhaba Dünya"
draft = False
words = 450
if title == "":
    print("Başlık eksik!")
elif draft:
    print("Taslak, yayınlanmadı.")
elif words < 300:
    print("Çok kısa: en az 300 kelime olmalı.")
else:
    print("Yayına hazır!")
```

</details>

### Sohbet Botu: Cevap seçimi

Bot artık mesaja bakıp karar versin. `message` içinde:

- `"merhaba"` **ya da** `"selam"` geçiyorsa: `Merhaba! Nasıl yardımcı olabilirim?`
- Değilse, `"hava"` geçiyorsa: `Bugün hava güneşli.`
- Değilse, `"görüşürüz"` geçiyorsa: `Hoşça kal!`
- Hiçbiri değilse: `Bunu anlamadım, başka türlü sorar mısın?`

Sadece bir cevap yazdırılmalı.

**Başlangıç kodu:**

```python
message = "selam, bugün hava nasıl?"
```

**İpuçları:**

1. İlk koşul: if "merhaba" in message or "selam" in message:
2. Sıra önemli: bir koşul doğru olunca alttakilere bakılmaz.

<details><summary>Çözüm</summary>

```python
message = "selam, bugün hava nasıl?"
if "merhaba" in message or "selam" in message:
    print("Merhaba! Nasıl yardımcı olabilirim?")
elif "hava" in message:
    print("Bugün hava güneşli.")
elif "görüşürüz" in message:
    print("Hoşça kal!")
else:
    print("Bunu anlamadım, başka türlü sorar mısın?")
```

</details>

### Okul Not Defteri: Not derecesi

Programımız notun derecesini söylesin. `grade`'e göre:

- 85 ve üstü: `Derece: Pekiyi`
- 70 ve üstü: `Derece: İyi`
- 60 ve üstü: `Derece: Orta`
- 50 ve üstü: `Derece: Geçer`
- 50'nin altı: `Derece: Geçmez`

Sadece tek bir satır yazdırmalı.

**Başlangıç kodu:**

```python
grade = 72
```

**İpuçları:**

1. En yüksek sınırdan başla: if grade >= 85: sonra elif grade >= 70: ...
2. Hiçbiri tutmazsa else: Geçmez.

<details><summary>Çözüm</summary>

```python
grade = 72
if grade >= 85:
    print("Derece: Pekiyi")
elif grade >= 70:
    print("Derece: İyi")
elif grade >= 60:
    print("Derece: Orta")
elif grade >= 50:
    print("Derece: Geçer")
else:
    print("Derece: Geçmez")
```

</details>
