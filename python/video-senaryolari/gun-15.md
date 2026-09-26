# Video senaryosu: Gün 15, Hata tipleri

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~141 sn

Piko, atölyenin dedektif bürosunda hata mesajlarını okumayı anlatıyor: satır, tip ve açıklama; NameError, ValueError, AttributeError, TypeError gibi sık hatalar ve print ile iz sürme.

Ders metni: [gun-15.md](../gunler/gun-15.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | konusma (sag) |
| 2 | anlatim | 12 sn | on (sol) |
| 3 | hata | 12 sn | sasirma (sag) |
| 4 | hata | 10 sn | sasirma (sag) |
| 5 | hata | 10 sn | sasirma (sag) |
| 6 | anlatim | 12 sn | dusunme (sol) |
| 7 | kod | 12 sn | isaret (sag) |
| 8 | kod | 14 sn | dusunme (sag) |
| 9 | soru | 8 sn | dusunme (sag) |
| 10 | hata | 9 sn | mutlu (sag) |
| 11 | gorev | 12 sn | isaret (sol) |
| 12 | ozet | 7 sn | on (sag) |
| 13 | kapanis | 11 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Piko! Atölyenin son odası bir dedektif bürosu. Masada bir sürü bozuk kod var ve hepsi kırmızı hata mesajları veriyor. Ama hata mesajları düşmanımız değil, ipucudur. Bugün hata dedektifi oluyoruz!

**Ekranda başlık:** Gün 15: Hata tipleri

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** konusma pozu, sag

*Yönetmen notu: Piko'nun başında bir dedektif şapkası, elinde büyüteç.*

## Sahne 2: anlatim (12 sn)

**Seslendirme:** Bir hata mesajında üç ipucu var: satır numarası, hata tipi ve kısa bir açıklama. Önce satıra git, sonra tipe bak. Sorun çoğu zaman o satırda ya da hemen bir üstündedir.

**Ekranda başlık:** Hata mesajı nasıl okunur?

**Ekranda maddeler:**

- Satır numarası: sorun nerede?
- Hata tipi: NameError, TypeError...
- Açıklama: tipin yanındaki kısa cümle

**Maskot:** on pozu, sol

## Sahne 3: hata (12 sn)

**Seslendirme:** NameError, tanımlanmamış bir isim demek. Çoğu zaman bir yazım hatasıdır. Python iyi bir dedektif ortağı: score mu demek istedin diye soruyor bile!

**Ekranda başlık:** NameError

**Kod** (vurgulanan satırlar: 2):

```python
score = 10
print(scroe)
```

**Çıktı:**

```text
NameError: name 'scroe' is not defined. Did you mean: 'score'?
```

**Maskot:** sasirma pozu, sag

## Sahne 4: hata (10 sn)

**Seslendirme:** ValueError'da tip doğru ama değer uygun değil. int yazıyı sayıya çevirebilir, ama harflerle yazılmış on ikiyi anlayamaz.

**Ekranda başlık:** ValueError

**Kod** (vurgulanan satırlar: 2):

```python
text = "on iki"
print(int(text))
```

**Çıktı:**

```text
ValueError: invalid literal for int() with base 10: 'on iki'
```

**Maskot:** sasirma pozu, sag

## Sahne 5: hata (10 sn)

**Seslendirme:** AttributeError, o tipte olmayan bir metodu çağırdın demek. upper yazılara ait bir alet; sayının böyle bir aleti yok.

**Ekranda başlık:** AttributeError

**Kod** (vurgulanan satırlar: 2):

```python
level = 5
print(level.upper())
```

**Çıktı:**

```text
AttributeError: 'int' object has no attribute 'upper'
```

**Maskot:** sasirma pozu, sag

## Sahne 6: anlatim (12 sn)

**Seslendirme:** Dedektif defterine birkaç şüpheli daha ekleyelim. Unutulan iki nokta SyntaxError, bozuk girinti IndentationError verir. Olmayan sıra numarası IndexError, olmayan anahtar KeyError, sıfıra bölmek de ZeroDivisionError.

**Ekranda başlık:** Şüpheliler listesi

**Ekranda maddeler:**

- SyntaxError: yazım kuralı bozuk
- IndentationError: girinti hatalı
- TypeError: yanlış tipler bir arada
- IndexError: listede olmayan sıra
- KeyError: sözlükte olmayan anahtar
- ZeroDivisionError: sıfıra bölme

**Maskot:** dusunme pozu, sol

## Sahne 7: kod (12 sn)

**Seslendirme:** Birçok hata tip karışıklığından çıkar. Hepsi üç gibi görünüyor ama tipleri bambaşka! Tırnaklı üç bir yazı, köşeli parantezli üç ise bir liste.

**Ekranda başlık:** Tipine bak

**Kod**:

```python
values = [3, "3", 3.0, True, [3]]
for v in values:
    print(repr(v), "->", type(v).__name__)
```

**Çıktı:**

```text
3 -> int
'3' -> str
3.0 -> float
True -> bool
[3] -> list
```

**Maskot:** isaret pozu, sag

## Sahne 8: kod (14 sn)

**Seslendirme:** Bazı hatalar mesaj bile vermez! Toplam altmış olmalıydı ama otuz çıktı. Dedektif taktiği: ara yerlere print koy. Ara toplam hiç birikmiyor; demek ki artı eşittir yerine eşittir yazılmış.

**Ekranda başlık:** print ile iz sür

**Kod** (vurgulanan satırlar: 4, 5):

```python
prices = [10, 20, 30]
total = 0
for p in prices:
    total = p
    print("ara toplam:", total)
print("Toplam:", total)
```

**Çıktı:**

```text
ara toplam: 10
ara toplam: 20
ara toplam: 30
Toplam: 30
```

**Maskot:** dusunme pozu, sag

## Sahne 9: soru (8 sn)

**Seslendirme:** Şimdi dedektif sensin! Bu kod hangi hata tipini verir? KeyError mı, TypeError mı?

**Ekranda başlık:** Hangi hata?

**Kod**:

```python
hero = {"name": "Piko"}
print(hero["name"] + 5)
```

**Maskot:** dusunme pozu, sag

## Sahne 10: hata (9 sn)

**Seslendirme:** TypeError! Anahtar var, yani KeyError değil. Ama gelen değer bir yazı ve yazıya sayı eklenemiyor.

**Ekranda başlık:** Cevap: TypeError

**Kod** (vurgulanan satırlar: 2):

```python
hero = {"name": "Piko"}
print(hero["name"] + 5)
```

**Çıktı:**

```text
TypeError: can only concatenate str (not "int") to str
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (12 sn)

**Seslendirme:** Dedektif görevlerin hazır! Üç bozuk kodu hata mesajlarına bakarak onaracaksın: bir TypeError, bir IndexError ve bir KeyError. Challenge'da boş listede çöken bir ortalama fonksiyonunu kurtaracaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: TypeError'ı düzelt
- Görev 2: IndexError'ı düzelt
- Görev 3: KeyError'ı düzelt
- Challenge: Sıfıra bölme

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (7 sn)

**Seslendirme:** Bugün hata mesajlarını birer ipucu gibi okumayı ve şüphelileri tek tek tanımayı öğrendik.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- Önce satır, sonra hata tipi, sonra açıklama
- Sık hatalar: NameError, TypeError, ValueError...
- type() ile tipe bak, print() ile iz sür

**Maskot:** on pozu, sag

## Sahne 13: kapanis (11 sn)

**Seslendirme:** Alet Atölyesi'ni bitirdin, tebrikler dedektif! Yarın Keşif Adası'na yelken açıyoruz: tarih ve saatlerle hesap yapacağız. Adada hataları program çökmeden yakalamayı da öğreneceğiz.

**Ekranda başlık:** Yarın: Tarih ve saat

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** tebrik pozu, orta

*Yönetmen notu: Piko atölyeden çıkıp iskelede bekleyen tekneye atlar; ufukta Keşif Adası görünür.*
