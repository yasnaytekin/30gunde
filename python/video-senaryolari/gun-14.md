# Video senaryosu: Gün 14, Üst düzey fonksiyonlar

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~124 sn

Piko, fonksiyonları değer gibi kullanmayı anlatıyor: fonksiyonu fonksiyona vermek, map, filter, sorted ile key, ve fonksiyon döndüren fonksiyonlar (closure).

Ders metni: [gun-14.md](../gunler/gun-14.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | konusma (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 11 sn | konusma (sag) |
| 4 | hata | 10 sn | uzgun (sag) |
| 5 | kod | 14 sn | isaret (sag) |
| 6 | kod | 14 sn | mutlu (sag) |
| 7 | soru | 9 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 13 sn | isaret (sol) |
| 10 | ozet | 8 sn | on (sag) |
| 11 | kapanis | 9 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Piko! Atölyenin ustası bana bir sır verdi: aletleri başka aletlere de takabilirsin! Matkabın ucunu değiştirmek gibi, bir fonksiyona başka bir fonksiyonu verebilirsin. Bugün üst düzey fonksiyonları öğreniyoruz.

**Ekranda başlık:** Gün 14: Üst düzey fonksiyonlar

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** konusma pozu, sag

*Yönetmen notu: Bir matkaba farklı uçlar takılıp çıkarılır.*

## Sahne 2: kod (14 sn)

**Seslendirme:** Fonksiyonu parantezsiz yazarsan onu çağırmazsın, kendisini alırsın. use_twice, verdiğin fonksiyonu iki kez uygular. hey, önce büyük harf ve ünlem alıyor, sonra bir ünlem daha. lambda da verilebilir!

**Ekranda başlık:** Fonksiyonlar da değerdir

**Kod** (vurgulanan satırlar: 5, 7):

```python
def shout(text):
    return text.upper() + "!"

def use_twice(func, value):
    return func(func(value))

print(use_twice(shout, "hey"))
print(use_twice(lambda n: n * 10, 3))
```

**Çıktı:**

```text
HEY!!
300
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (11 sn)

**Seslendirme:** map her elemana fonksiyonu uygular: bütün skorlar iki katına çıktı. filter ise fonksiyonun True dediği elemanları tutar: burada altmışın altındakiler.

**Ekranda başlık:** map ve filter

**Kod** (vurgulanan satırlar: 2, 3):

```python
scores = [40, 75, 90, 55]
print(list(map(lambda s: s * 2, scores)))
print(list(filter(lambda s: s < 60, scores)))
```

**Çıktı:**

```text
[80, 150, 180, 110]
[40, 55]
```

**Maskot:** konusma pozu, sag

## Sahne 4: hata (10 sn)

**Seslendirme:** list'i unutursan Python sonucu değil, bir map nesnesi gösterir. Hata vermez ama işine de yaramaz. Sonuçları görmek için list içine al.

**Ekranda başlık:** list() unutulunca

**Kod** (vurgulanan satırlar: 2):

```python
scores = [40, 75, 90]
print(map(lambda s: s * 2, scores))
```

**Çıktı:**

```text
<map object at 0x7f3a2c1b5e10>
```

**Maskot:** uzgun pozu, sag

*Yönetmen notu: Adres her çalıştırmada farklıdır; ekranda örnek bir adres gösterilir.*

## Sahne 5: kod (14 sn)

**Seslendirme:** sorted'a key ile neye göre sıralayacağını söylersin. Burada her oyuncunun skoruna bakıyoruz, reverse True da büyükten küçüğe dizer. key olarak len verirsen kısa isimler öne geçer.

**Ekranda başlık:** sorted ve key

**Kod** (vurgulanan satırlar: 2, 4):

```python
players = [("Ali", 120), ("Piko", 300), ("Ece", 250)]
for name, score in sorted(players, key=lambda p: p[1], reverse=True):
    print(name, score)
print("Kısa isim önce:", sorted(["Zeynep", "Can", "Ece"], key=len))
```

**Çıktı:**

```text
Piko 300
Ece 250
Ali 120
Kısa isim önce: ['Can', 'Ece', 'Zeynep']
```

**Maskot:** isaret pozu, sag

## Sahne 6: kod (14 sn)

**Seslendirme:** Bir fonksiyon, içinde yeni bir fonksiyon yapıp onu döndürebilir. İçteki fonksiyon dıştakinin değerini hatırlar; buna closure denir. plus5 artık her sayıya beş ekleyen yepyeni bir alet.

**Ekranda başlık:** Fonksiyon üreten fonksiyon

**Kod** (vurgulanan satırlar: 4, 7):

```python
def make_adder(n):
    def add(x):
        return x + n
    return add

plus5 = make_adder(5)
print(plus5(10))
print(plus5(1))
```

**Çıktı:**

```text
15
6
```

**Maskot:** mutlu pozu, sag

## Sahne 7: soru (9 sn)

**Seslendirme:** max da key alır, map'e de hazır bir fonksiyon verebilirsin. Sence bu iki satır ne yazdırır?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```python
names = ["Piko", "Al", "Ece"]
print(max(names, key=len))
print(list(map(len, names)))
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Piko ve dört, iki, üç! max en uzun ismi seçti. map ise len fonksiyonunu her isme uygulayıp uzunlukları bir listeye koydu.

**Ekranda başlık:** Cevap

**Kod**:

```python
names = ["Piko", "Al", "Ece"]
print(max(names, key=len))
print(list(map(len, names)))
```

**Çıktı:**

```text
Piko
[4, 2, 3]
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (13 sn)

**Seslendirme:** Görevlerde bir fonksiyonu başka bir fonksiyona verecek, map ile skorlara bonus ekleyecek ve filter ile geçenleri ayıracaksın. Challenge'da fonksiyon üreten bir fonksiyon, yani çarpan üretici yazacaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Uygula
- Görev 2: Bonus puan
- Görev 3: Geçenler
- Challenge: Çarpan üretici

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (8 sn)

**Seslendirme:** Bugün fonksiyonları bir değer gibi elden ele verdik, listelere uyguladık ve yeni fonksiyonlar ürettik.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- Parantezsiz fonksiyon = fonksiyonun kendisi
- map uygular, filter süzer; list() ile gör
- sorted/max key alır; closure değer hatırlar

**Maskot:** on pozu, sag

## Sahne 11: kapanis (9 sn)

**Seslendirme:** Artık alet ustasısın! Yarın atölyenin son odasına giriyoruz: bir dedektif bürosu. Kırmızı hata mesajlarını okuyup hata tiplerini tanıyacağız.

**Ekranda başlık:** Yarın: Hata tipleri

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** tebrik pozu, orta
