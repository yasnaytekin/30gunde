# Gün 18: Düzenli ifadeler

**Kurs:** 30 Günde Python  ·  **Bölge:** Keşif Adası  ·  **Maskot:** Piko

**Bugünün hedefi:** re modülüyle metinlerde desen aramak, bulmak ve değiştirmek

> Adanın mağarasında duvarlar yazılarla dolu. Bir yerlerde gizli sayılar, şifreler ve komutlar saklı. Tek tek okumak günler sürer! Neyse ki Python'ın bir büyüteci var: **düzenli ifadeler** (regex). Bir desen tarif ediyorsun, Python onu metnin içinde buluyor.

![Keşif Adası](../../gorseller/python/harita/ada.webp)

## Konu anlatımı

### Desen nedir?

Düzenli ifade, aradığın şeyin **tarifidir**. "İçinde e harfi olan kelime" ya da "yan yana rakamlar" gibi. Python'da `re` modülüyle kullanılır:

```python
import re
text = "Piko 3 elma ve 12 altın buldu"
print(re.findall(r"\d+", text))   # ['3', '12']
```

Desenlerin başına `r` koyarız (`r"..."`). Böylece ters eğik çizgiler doğru okunur.

### Özel karakterler

- `\d` bir rakam, `\w` bir harf, rakam ya da alt çizgi, `\s` bir boşluk
- `.` herhangi bir karakter
- `+` bir ya da daha fazla, `*` sıfır ya da daha fazla, `?` olabilir de olmayabilir de
- `{3}` tam 3 tane, `{2,4}` 2 ile 4 arası
- `[aeı]` köşeli parantezdekilerden biri, `[0-9]` 0 ile 9 arası
- `^` başlangıç, `$` son

### Dört temel fonksiyon

- `re.findall(desen, metin)` eşleşen tüm parçaları liste olarak verir
- `re.search(desen, metin)` ilk eşleşmeyi bulur, yoksa `None` verir
- `re.fullmatch(desen, metin)` metnin **tamamı** desene uyuyor mu?
- `re.sub(desen, yeni, metin)` eşleşenleri değiştirir

```python
print(re.sub(r"\d", "*", "Şifre 4821"))   # Şifre ****
```

### Gruplar

Parantezler deseni parçalara ayırır. Eşleşmeden sonra her parçayı `group()` ile alırsın:

```python
m = re.search(r"(\w+) (\d+) altın", "Ece 45 altın buldu")
if m:
    print(m.group(1))   # Ece
    print(m.group(2))   # 45
```

## Örnekler

### Sayıları bul

```python
import re

text = "Piko 3 elma, 12 altın ve 7 iksir buldu"
print(re.findall(r"\d+", text))
print(re.findall(r"\d", text))
```

*\d+ ile \d arasındaki farka dikkat et.*

### Ara ve değiştir

```python
import re

msg = "Şifrem 4821, telefonum 05321234567"
print(re.search(r"\d{4}", msg).group())
print(re.sub(r"\d", "*", msg))
```

### Gruplarla parçala

```python
import re

for line in ["Ece 45 altın", "Can 7 altın", "yanlış satır"]:
    m = re.search(r"(\w+) (\d+) altın", line)
    if m:
        print(m.group(1), "->", int(m.group(2)))
    else:
        print("Eşleşme yok:", line)
```

## Görevler

### Görev 1: Sayıları topla

`text` içindeki tüm sayıları `re.findall` ile bul ve `numbers` listesine koy. Sonra sayıların toplamını `total` olarak hesapla.

**Başlangıç kodu:**

```python
import re

text = "Piko 3 elma, 12 altın ve 7 iksir buldu"

numbers = []
total = 0

print(numbers, total)
```

**İpuçları:**

1. Desen: r"\d+" (bir veya daha fazla rakam)
2. findall yazı listesi verir; toplamak için int() ile çevir.

<details><summary>Çözüm</summary>

```python
import re

text = "Piko 3 elma, 12 altın ve 7 iksir buldu"

numbers = re.findall(r"\d+", text)
total = sum([int(n) for n in numbers])

print(numbers, total)
```

</details>

### Görev 2: E-posta var mı?

`text` içinde bir e-posta adresi varsa `has_email` True, yoksa False olsun. Basit bir desen yeterli: harfler, `@`, harfler, nokta, harfler.

**Başlangıç kodu:**

```python
import re

text = "Bana piko@ornek.com adresinden yaz"

has_email = False

print(has_email)
```

**İpuçları:**

1. Desen: r"\w+@\w+\.\w+"
2. re.search bulamazsa None verir: ... is not None

<details><summary>Çözüm</summary>

```python
import re

text = "Bana piko@ornek.com adresinden yaz"

has_email = re.search(r"\w+@\w+\.\w+", text) is not None

print(has_email)
```

</details>

### Görev 3: Şifreyi gizle

`re.sub` kullanarak `text` içindeki tüm rakamları `*` ile değiştir ve `hidden` değişkenine koy.

**Başlangıç kodu:**

```python
import re

text = "Kasanın şifresi 4821"

hidden = text

print(hidden)
```

**İpuçları:**

1. re.sub(r"\d", "*", text)

<details><summary>Çözüm</summary>

```python
import re

text = "Kasanın şifresi 4821"

hidden = re.sub(r"\d", "*", text)

print(hidden)
```

</details>

## Challenge: Telefon numarası

`is_phone(text)` fonksiyonu, metin tam olarak `05` ile başlayan **11 haneli** bir numaraysa True, değilse False döndürsün.

**Başlangıç kodu:**

```python
import re

def is_phone(text):
    return False

print(is_phone("05321234567"))
```

**İpuçları:**

1. 05'ten sonra 9 rakam daha gelmeli: \d{9}
2. Metnin tamamı uymalı: re.fullmatch

<details><summary>Çözüm</summary>

```python
import re

def is_phone(text):
    return re.fullmatch(r"05\d{9}", text) is not None

print(is_phone("05321234567"))
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Komut çözücü**

### Piko'nun Macerası: Komut çözücü

Oyuncu komutları yazıyla veriyor: `git kuzey 3` gibi. `parse(command)` fonksiyonu:

- Komut `git` ile başlıyor, ardından bir yön (`kuzey`, `güney`, `doğu`, `batı`) ve bir sayı geliyorsa `("kuzey", 3)` tuple'ını döndürsün (sayı int olsun).
- Uymuyorsa `None` döndürsün.

**Başlangıç kodu:**

```python
import re

def parse(command):
    return None

print(parse("git kuzey 3"))
print(parse("uç gökyüzü"))
```

**İpuçları:**

1. Seçenekler için | kullan: (kuzey|güney|doğu|batı)
2. Sayı grubu: (\d+)
3. m.group(1) yön, int(m.group(2)) adım sayısı

<details><summary>Çözüm</summary>

```python
import re

def parse(command):
    m = re.fullmatch(r"git (kuzey|güney|doğu|batı) (\d+)", command)
    if m:
        return (m.group(1), int(m.group(2)))
    return None

print(parse("git kuzey 3"))
print(parse("uç gökyüzü"))
```

</details>

### Harcama Defteri: Banka SMS'i okuyucu

Bankadan gelen SMS'ler şöyle: `Kartinizdan 245,90 TL harcama yapildi. Yer: MIGROS`

`parse_sms(text)` fonksiyonu `re` modülüyle:

- Tutarı ve yeri bulup `(245.9, "MIGROS")` tuple'ını döndürsün (tutar float olsun; virgülü noktaya çevir).
- SMS bu kalıba uymuyorsa `None` döndürsün.

**Başlangıç kodu:**

```python
import re


def parse_sms(text):
    pass
```

**İpuçları:**

1. Tutar deseni: (\d+,\d+)  Yer deseni: (\w+)
2. match.group(1) ilk parantezi verir; replace(",", ".") ile float'a çevrilebilir yap.

<details><summary>Çözüm</summary>

```python
import re


def parse_sms(text):
    match = re.search(r"(\d+,\d+) TL harcama yapildi\. Yer: (\w+)", text)
    if match is None:
        return None
    amount = float(match.group(1).replace(",", "."))
    return (amount, match.group(2))
```

</details>

### Görev Asistanı: Mesajdan bilgi çıkarma

Gelen mesajlardaki önemli bilgileri asistan bulsun. `re` modülüyle:

- `find_emails(text)`: metindeki e-posta adreslerini liste olarak döndürsün.
- `find_times(text)`: `14:30` gibi saatleri liste olarak döndürsün.

**Başlangıç kodu:**

```python
import re


def find_emails(text):
    pass


def find_times(text):
    pass
```

**İpuçları:**

1. re.findall(desen, metin) bütün eşleşmeleri liste olarak verir.
2. Saat deseni: \d{1,2}:\d{2}

<details><summary>Çözüm</summary>

```python
import re


def find_emails(text):
    return re.findall(r"[\w.]+@[\w.]+\.\w+", text)


def find_times(text):
    return re.findall(r"\d{1,2}:\d{2}", text)
```

</details>

### Kişisel Web Sitem: Bağlantılar ve e-postalar

Yazılarındaki bağlantıları ve e-posta adreslerini `re` modülüyle yakalayalım:

- `find_links(text)`: metindeki `http://` veya `https://` ile başlayan adresleri liste olarak döndürsün (`re.findall`). Adreslerden sonra hep bir boşluk ya da metnin sonu geliyor.
- `hide_emails(text)`: spam botları görmesin diye metindeki e-posta adreslerini `[gizli]` ile değiştirip yeni metni döndürsün (`re.sub`). E-postalar `ad@site.com` ya da `ad.soyad@site.org` gibi.

**Başlangıç kodu:**

```python
import re


def find_links(text):
    pass


def hide_emails(text):
    pass
```

**İpuçları:**

1. Bağlantı deseni: r"https?://\S+" (s? isteğe bağlı s, \S boşluk olmayan karakter)
2. E-posta deseni: r"[\w.]+@\w+\.\w+"

<details><summary>Çözüm</summary>

```python
import re


def find_links(text):
    return re.findall(r"https?://\S+", text)


def hide_emails(text):
    return re.sub(r"[\w.]+@\w+\.\w+", "[gizli]", text)
```

</details>

### Sohbet Botu: Ad, sayı ve e-posta

Akıllı asistanlar mesajdaki önemli bilgileri yakalar. `analyze(message)` `re` modülüyle bir **sözlük** döndürsün:

- `"name"`: mesajda `adım Ece` gibi bir kalıp varsa ad (`re.search` ve bir grup: `adım (\w+)`), yoksa `None`
- `"numbers"`: mesajdaki bütün sayılar, **int** olarak bir liste (`re.findall`)
- `"email"`: mesajdaki e-posta adresi, yoksa `None`

Örnek: `"Merhaba, benim adım Ece. 2 bilet istiyorum, mailim ece@okul.com"` için sonuç:

```
{'name': 'Ece', 'numbers': [2], 'email': 'ece@okul.com'}
```

**Başlangıç kodu:**

```python
import re


def analyze(message):
    pass
```

**İpuçları:**

1. Ad için re.search(r"adım (\w+)", message) ve .group(1); sayılar için re.findall(r"\d+", message)
2. E-posta deseni: [\w.]+@[\w.]+\w  (bulamazsa re.search None döndürür)

<details><summary>Çözüm</summary>

```python
import re


def analyze(message):
    name = re.search(r"adım (\w+)", message)
    email = re.search(r"[\w.]+@[\w.]+\w", message)
    numbers = [int(n) for n in re.findall(r"\d+", message)]
    return {
        "name": name.group(1) if name else None,
        "numbers": numbers,
        "email": email.group() if email else None,
    }
```

</details>

### Okul Not Defteri: Not mesajı okuyucu

Okul sisteminden şöyle mesajlar geliyor: `Sınav sonuçların: Matematik: 85, Fizik: 70, Tarih: 90`

`parse_grades(text)` fonksiyonu `re` modülüyle mesajdaki tüm `Ders: not` parçalarını bulsun ve bir sözlük döndürsün: `{"Matematik": 85, "Fizik": 70, "Tarih": 90}` (notlar tam sayı). Mesajda hiç not yoksa boş sözlük `{}` döndürsün.

**Başlangıç kodu:**

```python
import re


def parse_grades(text):
    pass
```

**İpuçları:**

1. Desen: (\w+): (\d+) iki grup yakalar: ders ve not.
2. Desende iki grup varsa re.findall (ders, not) ikililerinden bir liste verir.

<details><summary>Çözüm</summary>

```python
import re


def parse_grades(text):
    grades = {}
    for lesson, grade in re.findall(r"(\w+): (\d+)", text):
        grades[lesson] = int(grade)
    return grades
```

</details>
