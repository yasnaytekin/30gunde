# Video senaryosu: Gün 3, Operatörler

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~137 sn

Piko, Python Köyü'nün pazarında bölmenin üç halini, işlem önceliğini, += kısayolunu, karşılaştırma ve mantık operatörlerini anlatıyor.

Ders metni: [gun-03.md](../gunler/gun-03.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | konusma (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 12 sn | konusma (sag) |
| 4 | kod | 12 sn | mutlu (sag) |
| 5 | kod | 14 sn | isaret (sag) |
| 6 | kod | 12 sn | konusma (sag) |
| 7 | hata | 12 sn | uzgun (sag) |
| 8 | soru | 8 sn | dusunme (sag) |
| 9 | cikti | 10 sn | mutlu (sag) |
| 10 | gorev | 14 sn | isaret (sol) |
| 11 | ozet | 8 sn | on (sag) |
| 12 | kapanis | 9 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Gün 3: Operatörler! Bu derste bölmenin üç halini, işlem önceliğini, karşılaştırma ve mantık operatörlerini öğreneceksin.

- /, // ve % ile bölme
- İşlem önceliği ve +=
- Karşılaştırma: and, or, not

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Piko! Python Köyü'ne hoş geldin. Oyunlarda her şey sayılarla döner: skor, can, altın. Bugün köyün pazarında hesapları sen yapacaksın. İlk soru: yedi elmayı iki kişiye nasıl bölersin?

**Ekranda başlık:** Gün 3: Operatörler

**Görsel:** `gorseller/python/harita/koy.webp`

**Maskot:** konusma pozu, sag

## Sahne 2: kod (14 sn)

**Seslendirme:** Bölmenin üç hali var. Tek eğik çizgi sonucu ondalıklı verir. Çift eğik çizgi tam bölmedir, yüzde işareti ise kalanı verir. Yani herkese üç elma düşer, bir tane artar.

**Ekranda başlık:** Bölmenin üç hali

**Kod** (vurgulanan satırlar: 2, 3):

```python
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(2 ** 10)
```

**Çıktı:**

```text
3.5
3
1
1024
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: Yedi elma iki sepete dağılır, bir elma ortada kalır.*

## Sahne 3: kod (12 sn)

**Seslendirme:** Python matematikteki sırayı izler: önce parantez, sonra üs, sonra çarpma ve bölme, en son toplama ve çıkarma. Parantez ekleyince sonuç on dörtten yirmiye çıkıyor.

**Ekranda başlık:** İşlem önceliği

**Kod** (vurgulanan satırlar: 2):

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
```

**Çıktı:**

```text
14
20
```

**Maskot:** konusma pozu, sag

## Sahne 4: kod (12 sn)

**Seslendirme:** Skor eşittir skor artı on yazmak yerine kısaca artı eşittir yazabilirsin. Aynı hile eksi, çarpı ve bölü için de çalışır. Skor önce yirmi oluyor, sonra ikiyle çarpılıyor.

**Ekranda başlık:** Kısayollar: += ve *=

**Kod** (vurgulanan satırlar: 2, 4):

```python
score = 0
score += 10
score += 10
score *= 2
print("Skor:", score)
```

**Çıktı:**

```text
Skor: 40
```

**Maskot:** mutlu pozu, sag

## Sahne 5: kod (14 sn)

**Seslendirme:** İki değeri karşılaştırınca Python True ya da False der. Dikkat: tek eşittir kutuya değer koyar, çift eşittir soru sorar. Ünlem eşittir de eşit değil mi diye sorar.

**Ekranda başlık:** Karşılaştırma operatörleri

**Kod** (vurgulanan satırlar: 5, 6):

```python
hp = 40
gold = 120
print(hp > 50)
print(gold >= 100)
print(hp == 40)
print(hp != 40)
```

**Çıktı:**

```text
False
True
True
False
```

**Maskot:** isaret pozu, sag

## Sahne 6: kod (12 sn)

**Seslendirme:** Soruları birleştirmek için mantık operatörleri var. and ikisi de doğruysa, or en az biri doğruysa True verir. not ise cevabı tersine çevirir.

**Ekranda başlık:** and, or, not

**Kod** (vurgulanan satırlar: 3, 4, 5):

```python
hp = 40
gold = 120
print(hp > 20 and gold > 100)
print(hp > 50 or gold > 100)
print(not hp > 50)
```

**Çıktı:**

```text
True
True
True
```

**Maskot:** konusma pozu, sag

## Sahne 7: hata (12 sn)

**Seslendirme:** Bu hata mesaj bile vermez, o yüzden sinsidir! Python'da ondalık için nokta kullanılır. Virgül koyarsan Python iki ayrı sayı görür: üç ve altı yazar. Üç buçuk için 3.5 yaz.

**Ekranda başlık:** Virgül değil, nokta!

**Kod** (vurgulanan satırlar: 1):

```python
print(3,5 + 1)
```

**Çıktı:**

```text
3 6
```

**Düzeltilmiş kod:**

```python
print(3.5 + 1)
```

**Düzeltilmiş çıktı:**

```text
4.5
```

**Maskot:** uzgun pozu, sag

## Sahne 8: soru (8 sn)

**Seslendirme:** Şimdi sen söyle: dokuz çift bir sayı mı? Sence bu kod ne yazdırır?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```python
x = 9
print(x % 2 == 0)
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (10 sn)

**Seslendirme:** False! Dokuzun ikiye bölümünden kalan bir. Bir, sıfıra eşit olmadığı için cevap False; yani dokuz tek sayı. Yüzde işareti çift ve tek bulmanın en kolay yolu.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 2):

```python
x = 9
print(x % 2 == 0)
```

**Çıktı:**

```text
False
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (14 sn)

**Seslendirme:** Pazar senin! On yedi dilim pizzayı beş arkadaşa paylaştıracak, kahramanına can iksiri içirecek ve üç skorun ortalamasını bulacaksın. Challenge'da saniyeleri saate ve dakikaya çevireceksin. İpucu: bölmenin üç halini hatırla.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Pizza paylaşımı
- Görev 2: Can iksiri
- Görev 3: Ortalama
- Sahne görevi: Eşit sıralar
- Challenge: Saniye çevirici

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (8 sn)

**Seslendirme:** Bugün bölmenin üç halini, kısayolları ve Python'a doğru mu yanlış mı diye soru sormayı öğrendik.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- / ondalıklı, // tam bölme, % kalan
- += ile kısa güncelleme; parantez önceliği değiştirir
- Karşılaştırma ve and, or, not: True ya da False

**Maskot:** on pozu, sag

## Sahne 12: kapanis (9 sn)

**Seslendirme:** Artık pazarın hesap ustası sensin! Yarın köyde kalıyoruz ama bu kez yazılarla oynayacağız: stringleri birleştirecek, parçalayacak ve süsleyeceğiz.

**Ekranda başlık:** Yarın: Stringler

**Görsel:** `gorseller/python/harita/koy.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** Bu dersin interaktif hâli 30gunde.com.tr'de seni bekliyor. Kodunu tarayıcıda yaz, hemen çalıştır ve görevleri tamamla!

**Ekranda:** İnteraktif dersler için **30gunde.com.tr**

- Kodunu tarayıcıda yaz ve çalıştır
- Görevleri tamamla, rozet kazan
- 30 günde adım adım Python
