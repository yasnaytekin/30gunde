# Video senaryosu: Gün 4, Stringler

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~122 sn

Piko, Python Köyü'nün tabelaları üzerinden stringleri birleştirmeyi, indeks ve dilimlemeyi, string metotlarını ve f-string ile biçimlendirmeyi anlatıyor.

Ders metni: [gun-04.md](../gunler/gun-04.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | mutlu (sag) |
| 2 | kod | 12 sn | isaret (sag) |
| 3 | kod | 14 sn | isaret (sag) |
| 4 | kod | 14 sn | konusma (sag) |
| 5 | kod | 11 sn | mutlu (sag) |
| 6 | hata | 11 sn | sasirma (sag) |
| 7 | soru | 10 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 13 sn | isaret (sol) |
| 10 | ozet | 7 sn | on (sag) |
| 11 | kapanis | 8 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Piko! Python Köyü'nde her yerde tabelalar, konuşmalar, mektuplar var. Oyunlarda da karakterler konuşur, isimler ekranda parlar. Bugün yazılarla, yani stringlerle oynuyoruz. Bir kelimeyi tersten yazdırmak ister misin?

**Ekranda başlık:** Gün 4: Stringler

**Görsel:** `gorseller/python/harita/koy.webp`

**Maskot:** mutlu pozu, sag

## Sahne 2: kod (12 sn)

**Seslendirme:** String, tırnak içindeki karakterler dizisi. Artı ile birleştirirsin, yıldız ile tekrarlarsın, len ile kaç karakter olduğunu ölçersin. Boşluk ve kesme işareti de sayılır!

**Ekranda başlık:** Birleştir ve tekrarla

**Kod**:

```python
first = "Pi"
second = "ko"
print(first + second)
print("ha" * 3)
print(len("Piko'nun Macerası"))
```

**Çıktı:**

```text
Piko
hahaha
17
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (14 sn)

**Seslendirme:** Her harfin bir sıra numarası var ve sayma sıfırdan başlar. Eksi bir sondaki harfi verir. Sıfırdan üçe dilim alırsan üç dahil olmaz. Eksi birlik adımla da kelime tersine döner!

**Ekranda başlık:** İndeks ve dilimleme

**Kod** (vurgulanan satırlar: 3, 4):

```python
word = "Python"
print(word[0], word[-1])
print(word[0:3])
print(word[::-1])
```

**Çıktı:**

```text
P n
Pyt
nohtyP
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: P-y-t-h-o-n harflerinin altında 0'dan 5'e indeks numaraları belirir.*

## Sahne 4: kod (14 sn)

**Seslendirme:** Stringlerin kendi aletleri var, bunlara metot deriz. strip kenardaki boşlukları siler, upper büyütür, title kelimelerin baş harfini büyütür, count sayar. Dikkat: upper İngilizce kuralını kullanır, İstanbul noktasız I ile çıkar.

**Ekranda başlık:** String metotları

**Kod** (vurgulanan satırlar: 5):

```python
name = "  piko  "
print(name.strip().upper())
print("python köyü".title())
print("ananas".count("a"))
print("istanbul".upper())
```

**Çıktı:**

```text
PIKO
Python Köyü
3
ISTANBUL
```

**Maskot:** konusma pozu, sag

## Sahne 5: kod (11 sn)

**Seslendirme:** En sevdiğim alet: f-string! Tırnağın başına f koyarsın, süslü parantez içindeki değişkenler değerleriyle yer değiştirir. Parantezin içine metot bile yazabilirsin.

**Ekranda başlık:** f-string

**Kod** (vurgulanan satırlar: 3, 4):

```python
name = "Piko"
gold = 42
print(f"{name} cebinde {gold} altın taşıyor.")
print(f"{name.upper()} geliyor!")
```

**Çıktı:**

```text
Piko cebinde 42 altın taşıyor.
PIKO geliyor!
```

**Maskot:** mutlu pozu, sag

## Sahne 6: hata (11 sn)

**Seslendirme:** Yazıyla sayıyı artıyla birleştirmeye çalışırsan Python yine TypeError verir: yazıya sadece yazı eklenebilir. Kurtarıcın hazır: f-string ya da str fonksiyonu.

**Ekranda başlık:** Yazı + sayı = TypeError

**Kod** (vurgulanan satırlar: 3):

```python
name = "Piko"
level = 3
print(name + " seviye " + level)
```

**Çıktı:**

```text
TypeError: can only concatenate str (not "int") to str
```

**Maskot:** sasirma pozu, sag

## Sahne 7: soru (10 sn)

**Seslendirme:** Bir ipucu: in, bir yazının içinde başka bir yazı var mı diye sorar. Şimdi söyle: bu kod ne yazdırır?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```python
word = "Python"
print(word[1:4])
print("th" in word)
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Birden dörde kadar dilim: y, t, h. Dört dahil değil! Ve evet, t h kelimenin içinde geçiyor, bu yüzden in True diyor.

**Ekranda başlık:** Cevap

**Kod**:

```python
word = "Python"
print(word[1:4])
print("th" in word)
```

**Çıktı:**

```text
yth
True
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (13 sn)

**Seslendirme:** Görevlerde bir tabelayı bağıran harflerle yazacak, bir ismin ilk ve son harfini yakalayacak, f-string ile seviye mesajı hazırlayacaksın. Challenge'da kabak gibi tersten de aynı okunan kelimeleri avlayacaksın!

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Tabela
- Görev 2: İlk ve son harf
- Görev 3: Seviye mesajı
- Sahne görevi: Piko kalede
- Challenge: Palindrom avcısı

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (7 sn)

**Seslendirme:** Bugün yazıları birleştirdik, harf harf dilimledik, metotlarla değiştirdik ve f-string ile süsledik.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- + birleştirir, * tekrarlar, len() ölçer
- İndeks 0'dan başlar; [0:3] dilim, [::-1] ters
- upper, title, strip, count ve f-string

**Maskot:** on pozu, sag

## Sahne 11: kapanis (8 sn)

**Seslendirme:** Köyün yazı ustası sensin! Yarın Veri Ormanı'na giriyoruz. Kahramanın çantasındaki bütün eşyaları tek bir listede toplayacağız.

**Ekranda başlık:** Yarın: Listeler

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** tebrik pozu, orta

*Yönetmen notu: Harita köyden ormana doğru kayar.*
