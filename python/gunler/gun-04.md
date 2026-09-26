# Gün 4: Stringler

**Kurs:** 30 Günde Python  ·  **Bölge:** Python Köyü  ·  **Maskot:** Piko

**Bugünün hedefi:** Stringleri birleştirmek, parçalamak ve f-string ile biçimlendirmek

> Köyde her yerde tabelalar, konuşmalar, mektuplar var. Oyunlarda da karakterler konuşur, isimler ekranda parlar. Bugün yazılarla, yani **string**'lerle oynayacağız!

![Python Köyü](../../gorseller/python/harita/koy.webp)

## Konu anlatımı

### String nedir?

String, tırnak içindeki karakterler dizisidir. Tek tırnak da çift tırnak da olur: `'Piko'` ya da `"Piko"`.

- `+` ile birleştir: `"Pi" + "ko"` sonucu `"Piko"`
- `*` ile tekrarla: `"ha" * 3` sonucu `"hahaha"`
- `len()` ile uzunluğunu ölç: `len("Piko")` sonucu `4`

### Harflere tek tek ulaşmak

Her harfin bir sıra numarası (indeks) vardır ve sayma **0'dan başlar**.

```python
word = "Python"
print(word[0])    # P
print(word[-1])   # n (sondan birinci)
print(word[0:3])  # Pyt (0, 1 ve 2)
print(word[::-1]) # nohtyP (ters çevir)
```

### String metotları

- `upper()` hepsi büyük, `lower()` hepsi küçük
- `title()` Kelimelerin Baş Harfi Büyük
- `replace("a", "e")` harf değiştir
- `strip()` baştaki ve sondaki boşlukları sil
- `count("a")` kaç tane var say

Küçük bir not: `upper()` İngilizce kurallarını kullanır, yani `"istanbul".upper()` sonucu `ISTANBUL` olur, `İSTANBUL` değil.

### f-string: yazının içine değişken koy

Başına `f` koyduğun bir yazıda süslü parantez içindeki değişkenler değerleriyle yer değiştirir:

```python
name = "Piko"
level = 3
print(f"{name} seviye {level} oldu!")
```

Oyunlarda mesaj yazmanın en kolay yolu budur.

### İçinde var mı?

`in` ile bir yazının içinde başka bir yazı var mı diye bakabilirsin: `"ko" in "Piko"` sonucu `True`.

İki şeyin aynı olup olmadığını da `==` ile sorarsın: `"ada" == "ada"` sonucu `True`.

## Örnekler

### Birleştir ve tekrarla

```python
first = "Pi"
second = "ko"
print(first + second)
print("ha" * 3)
print(len("Piko'nun Macerası"))
```

### Dilimleme

```python
word = "Python"
print(word[0], word[-1])
print(word[0:3])
print(word[::-1])
```

### f-string

```python
name = "Piko"
gold = 42
print(f"{name} cebinde {gold} altın taşıyor.")
print(f"{name.upper()} geliyor!")
```

## Görevler

### Görev 1: Tabela

`word` içindeki yazıyı büyük harfe çevir, sonuna `!` ekle ve `shout` değişkenine koy. Sonuç `PYTHON!` olmalı.

**Başlangıç kodu:**

```python
word = "python"

shout = ""  # word'ün büyük harfli hali + "!"
print(shout)
```

**İpuçları:**

1. word.upper() büyük harfli halini verir.
2. + "!" ile sonuna ünlem eklenir.

<details><summary>Çözüm</summary>

```python
word = "python"

shout = word.upper() + "!"
print(shout)
```

</details>

### Görev 2: İlk ve son harf

`name` değişkeninin ilk harfini `first`, son harfini `last` değişkenine koy. Son harf için negatif indeks kullan.

**Başlangıç kodu:**

```python
name = "Piko"

first = ""
last = ""
print(first, last)
```

**İpuçları:**

1. İlk harf: name[0]
2. Son harf: name[-1]

<details><summary>Çözüm</summary>

```python
name = "Piko"

first = name[0]
last = name[-1]
print(first, last)
```

</details>

### Görev 3: Seviye mesajı

f-string kullanarak `message` değişkenini oluştur. Sonuç tam olarak `Ayla seviye 7!` olmalı, ama isim ve sayı değişkenlerden gelsin.

**Başlangıç kodu:**

```python
name = "Ayla"
level = 7

message = ""
print(message)
```

**İpuçları:**

1. f-string'in başında f olur: f"..."
2. Değişkenleri süslü paranteze koy: {name}

<details><summary>Çözüm</summary>

```python
name = "Ayla"
level = 7

message = f"{name} seviye {level}!"
print(message)
```

</details>

### Sahne görevi: Piko kalede

Piko'yu duvarlarla çevrili bir odaya koyalım. `bosluk`, Piko'nun iki yanındaki boş kare sayısı.

- `duvar`: `"#"` işaretini `bosluk * 2 + 3` kez tekrarla
- `oda`: `"#"` + `bosluk` kadar boşluk + `"*"` + `bosluk` kadar boşluk + `"#"`
- Sonra `duvar`, `oda`, `duvar` yazdır.

`bosluk = 3` olunca oda kendiliğinden büyümeli.

**Başlangıç kodu:**

```python
bosluk = 2
duvar = "#" * 7
oda = ""

print(duvar)
```

**İpuçları:**

1. Boşluk da bir yazıdır: " " * bosluk
2. oda = "#" + " " * bosluk + "*" + " " * bosluk + "#"

<details><summary>Çözüm</summary>

```python
bosluk = 2
duvar = "#" * (bosluk * 2 + 3)
oda = "#" + " " * bosluk + "*" + " " * bosluk + "#"

print(duvar)
print(oda)
print(duvar)
```

</details>

## Challenge: Palindrom avcısı

Tersten okunuşu da aynı olan kelimelere palindrom denir: kabak, ada, kek. `word` bir palindromsa `is_palindrome` değişkeni `True`, değilse `False` olsun. `True` yazmak yok; karşılaştırarak bul!

**Başlangıç kodu:**

```python
word = "kabak"

is_palindrome = False
print(is_palindrome)
```

**İpuçları:**

1. Kelimenin tersi: word[::-1]
2. İki şey aynı mı? == ile sor.

<details><summary>Çözüm</summary>

```python
word = "kabak"

is_palindrome = word == word[::-1]
print(is_palindrome)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Karakter konuşmaları**

### Piko'nun Macerası: Karakter konuşması

Oyunun açılışında kahraman kendini tanıtsın.

- Önce 30 tane `=` işaretinden oluşan bir çizgi yazdır
- Sonra f-string ile `intro` değişkenini oluştur: `Ben Piko, macera başlıyor!` (Piko yerine `player_name` kullan)
- `intro`'yu yazdır

**Başlangıç kodu:**

```python
player_name = "Piko"

# 1) 30 tane "=" işaretinden oluşan bir çizgi yazdır

# 2) f-string ile tanıtım cümlesi oluştur
intro = ""
print(intro)
```

**İpuçları:**

1. Çizgi için: print("=" * 30)
2. intro = f"Ben {player_name}, macera başlıyor!"

<details><summary>Çözüm</summary>

```python
player_name = "Piko"

print("=" * 30)

intro = f"Ben {player_name}, macera başlıyor!"
print(intro)
```

</details>

### Harcama Defteri: Kategori etiketi

Harcamaları girerken kategori adları dağınık yazılabiliyor: `"  MARKET "` gibi. Bunu düzeltelim:

- `clean`: baştaki ve sondaki boşlukları at, sadece ilk harfi büyük yap (`strip()` ve `capitalize()`)
- `label`: f-string ile `Market: 120 TL` biçiminde bir yazı (tutar `amount` değişkeninden)
- `label`'ı yazdır.

**Başlangıç kodu:**

```python
category = "  MARKET "
amount = 120
```

**İpuçları:**

1. category.strip() boşlukları atar, .capitalize() ilk harfi büyük yapar.
2. label = f"{clean}: {amount} TL"

<details><summary>Çözüm</summary>

```python
category = "  MARKET "
amount = 120
clean = category.strip().capitalize()
label = f"{clean}: {amount} TL"
print(label)
```

</details>

### Görev Asistanı: Görev başlığı düzeltme

Görevler aceleyle yazılınca dağınık oluyor: `"  rapor YAZ "`. Asistan bunu düzeltsin:

- `title`: boşlukları at, ilk harfi büyük yap (`strip()`, `capitalize()`)
- `slug`: başlığı küçük harfe çevir, boşlukları `-` yap (dosya adı için)
- `Görev: Rapor yaz (rapor-yaz)` gibi yazdır (f-string).

**Başlangıç kodu:**

```python
raw = "  rapor YAZ "
```

**İpuçları:**

1. raw.strip().capitalize()
2. title.lower().replace(" ", "-")

<details><summary>Çözüm</summary>

```python
raw = "  rapor YAZ "
title = raw.strip().capitalize()
slug = title.lower().replace(" ", "-")
print(f"Görev: {title} ({slug})")
```

</details>

### Kişisel Web Sitem: Başlıktan bağlantı

Yazı başlıkları bazen boşluklarla geliyor: `"  Merhaba Dünya  "`. Bundan yazının bağlantısını üretelim:

- `title`: baştaki ve sondaki boşlukları at (`strip()`)
- `slug`: başlığı küçük harfe çevir, boşlukları `-` yap (`lower()` ve `replace()`)
- `link`: f-string ile şu biçimde bir yazı: `<a href="/blog/merhaba-dünya.html">Merhaba Dünya</a>`
- `link`'i yazdır.

**Başlangıç kodu:**

```python
raw = "  Merhaba Dünya  "
```

**İpuçları:**

1. title.lower().replace(" ", "-") küçük harf yapar ve boşlukları - ile değiştirir.
2. Yazının içinde " olacağı için f-string'i tek tırnakla aç: f'<a href="/blog/{slug}.html">{title}</a>'

<details><summary>Çözüm</summary>

```python
raw = "  Merhaba Dünya  "
title = raw.strip()
slug = title.lower().replace(" ", "-")
link = f'<a href="/blog/{slug}.html">{title}</a>'
print(link)
```

</details>

### Sohbet Botu: Mesaj temizleme

Kullanıcılar bazen büyük harfle ve fazla boşlukla yazar: `"   MERHABA BOT   "`. Bot anlamaya çalışmadan önce mesajı temizleyelim:

- `clean`: baştaki ve sondaki boşlukları at, hepsini küçük harf yap (`strip()` ve `lower()`)
- `has_greeting`: `clean` içinde `"merhaba"` geçiyor mu? (`in`)
- `reply`: f-string ile `Bilge: 'merhaba bot' mesajını aldım.` biçiminde bir yazı (botun adı `bot_name`'den)

Sonra `reply`'ı ve `Selam var mı: True` satırını yazdır.

**Başlangıç kodu:**

```python
bot_name = "Bilge"
message = "   MERHABA BOT   "
```

**İpuçları:**

1. message.strip() boşlukları atar, .lower() hepsini küçük harf yapar: message.strip().lower()
2. reply = f"{bot_name}: '{clean}' mesajını aldım."

<details><summary>Çözüm</summary>

```python
bot_name = "Bilge"
message = "   MERHABA BOT   "
clean = message.strip().lower()
has_greeting = "merhaba" in clean
reply = f"{bot_name}: '{clean}' mesajını aldım."
print(reply)
print("Selam var mı:", has_greeting)
```

</details>

### Okul Not Defteri: Ders etiketi

Ders adları bazen dağınık kaydediliyor: `"  Türk_Dili  "` gibi. Bunu düzeltelim:

- `clean`: baştaki ve sondaki boşlukları at (`strip()`), alt çizgileri boşluğa çevir (`replace()`)
- `label`: f-string ile `Türk Dili: 88 puan` biçiminde bir yazı (not `grade` değişkeninden)
- `label`'ı yazdır.

**Başlangıç kodu:**

```python
lesson = "  Türk_Dili  "
grade = 88
```

**İpuçları:**

1. lesson.strip() boşlukları atar, .replace("_", " ") alt çizgiyi boşluk yapar.
2. label = f"{clean}: {grade} puan"

<details><summary>Çözüm</summary>

```python
lesson = "  Türk_Dili  "
grade = 88
clean = lesson.strip().replace("_", " ")
label = f"{clean}: {grade} puan"
print(label)
```

</details>
