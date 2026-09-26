# Video senaryosu: Gün 13, List comprehension

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~116 sn

Piko, atölyenin sihirli kalıbıyla list comprehension'ı anlatıyor: tek satırda liste üretmek, if ile süzmek, if-else ile dönüştürmek ve lambda ile isimsiz mini fonksiyonlar.

Ders metni: [gun-13.md](../gunler/gun-13.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | mutlu (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 9 sn | konusma (sag) |
| 4 | kod | 12 sn | isaret (sag) |
| 5 | kod | 13 sn | konusma (sag) |
| 6 | hata | 10 sn | uzgun (sag) |
| 7 | soru | 8 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 11 sn | isaret (sol) |
| 10 | ozet | 7 sn | on (sag) |
| 11 | kapanis | 10 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Piko! Atölyenin köşesinde sihirli bir kalıp var: bir tarafından malzemeleri atıyorsun, öbür tarafından hazır ürünler çıkıyor. Python'da buna list comprehension denir. Dört satırlık döngüleri tek satıra sığdırır!

**Ekranda başlık:** Gün 13: List comprehension

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Kalıba sayılar girer, iki katı büyümüş halleri çıkar.*

## Sahne 2: kod (14 sn)

**Seslendirme:** Bir listeden yeni liste yapmanın uzun yolu: boş liste, döngü, append. Kısa yolu tek satır! Şöyle oku: nums'taki her n için n çarpı onu al. İki yol da aynı sonucu veriyor.

**Ekranda başlık:** Uzun yol, kısa yol

**Kod** (vurgulanan satırlar: 8):

```python
nums = [1, 2, 3, 4, 5]

tens = []
for n in nums:
    tens.append(n * 10)
print(tens)

print([n * 10 for n in nums])
```

**Çıktı:**

```text
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (9 sn)

**Seslendirme:** Sona bir if eklersen sadece istediğin elemanları alırsın. Kalıp, altmışın altındaki skorları süzgeçten geçirmiyor.

**Ekranda başlık:** if ile süz

**Kod** (vurgulanan satırlar: 2):

```python
scores = [45, 90, 12, 77, 100, 63]
passed = [s for s in scores if s >= 60]
print("Geçenler:", passed)
```

**Çıktı:**

```text
Geçenler: [90, 77, 100, 63]
```

**Maskot:** konusma pozu, sag

## Sahne 4: kod (12 sn)

**Seslendirme:** Her eleman için iki sonuçtan birini seçmek istersen if ve else başa yazılır. Süzmek için if sonda, dönüştürmek için if else başta. Bunu aklında tut!

**Ekranda başlık:** if ve else ile dönüştür

**Kod** (vurgulanan satırlar: 2):

```python
scores = [45, 90, 12, 77]
print(["geçti" if s >= 60 else "kaldı" for s in scores])
```

**Çıktı:**

```text
['kaldı', 'geçti', 'kaldı', 'geçti']
```

**Maskot:** isaret pozu, sag

## Sahne 5: kod (13 sn)

**Seslendirme:** Tek satırlık küçük fonksiyonları lambda ile yazabilirsin. İki noktanın solu parametre, sağı döndürülen sonuç. Aynı kalıp fikri sözlükte de çalışır: süslü parantezle bir kareler sözlüğü!

**Ekranda başlık:** lambda: isimsiz mini fonksiyon

**Kod** (vurgulanan satırlar: 1, 2):

```python
square = lambda x: x * x
add = lambda a, b: a + b
print(square(6))
print(add(2, 3))
print({n: square(n) for n in range(1, 5)})
```

**Çıktı:**

```text
36
5
{1: 1, 2: 4, 3: 9, 4: 16}
```

**Maskot:** konusma pozu, sag

## Sahne 6: hata (10 sn)

**Seslendirme:** else'i sona koyarsan Python SyntaxError verir. Hatırla: sadece if varsa sona, if ile else birlikteyse başa yazılır.

**Ekranda başlık:** else yanlış yerde

**Kod** (vurgulanan satırlar: 2):

```python
nums = [1, 2, 3]
print([n for n in nums if n > 1 else 0])
```

**Çıktı:**

```text
SyntaxError: invalid syntax
```

**Maskot:** uzgun pozu, sag

## Sahne 7: soru (8 sn)

**Seslendirme:** Bu kalıp hem süzüyor hem dönüştürüyor. Sence ekrana hangi liste çıkar?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```python
words = ["kılıç", "iksir", "ok"]
print([len(w) for w in words if len(w) > 2])
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Beş ve beş! Ok kelimesi iki harfli olduğu için süzgeçte kaldı. Kalan iki kelimenin yerine de uzunlukları yazıldı.

**Ekranda başlık:** Cevap

**Kod**:

```python
words = ["kılıç", "iksir", "ok"]
print([len(w) for w in words if len(w) > 2])
```

**Çıktı:**

```text
[5, 5]
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (11 sn)

**Seslendirme:** Görevlerde sayıların iki katını, isimlerin büyük harfli halini ve sadece değerli ganimetleri tek satırda üreteceksin. Challenge'da bir lambda yazıp kareler listesi hazırlayacaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: İki katı
- Görev 2: Büyük harfle
- Görev 3: Değerli ganimet
- Challenge: lambda ile

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (7 sn)

**Seslendirme:** Bugün uzun döngüleri tek satırlık kalıplara çevirdik ve isimsiz mini fonksiyonlarla tanıştık.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- [ifade for x in liste]
- Süzmek: if sonda; dönüştürmek: if-else başta
- lambda x: x * x ile mini fonksiyon

**Maskot:** on pozu, sag

## Sahne 11: kapanis (10 sn)

**Seslendirme:** Sihirli kalıbın ustası oldun! Yarın atölyenin ustası bir sır verecek: aletleri başka aletlere takmak. map, filter ve sorted ile fonksiyonlarla oynayacağız.

**Ekranda başlık:** Yarın: Üst düzey fonksiyonlar

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** tebrik pozu, orta
