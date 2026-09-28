# Video senaryosu: Gün 5, Listeler

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~118 sn

Piko, Veri Ormanı'nda kahramanın çantasını bir listeyle düzenliyor: liste oluşturmak, eleman eklemek, çıkarmak, değiştirmek ve sum, max, sorted ile incelemek.

Ders metni: [gun-05.md](../gunler/gun-05.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | mutlu (sag) |
| 2 | kod | 13 sn | isaret (sag) |
| 3 | kod | 14 sn | konusma (sag) |
| 4 | kod | 10 sn | isaret (sag) |
| 5 | kod | 12 sn | konusma (sag) |
| 6 | hata | 12 sn | sasirma (sag) |
| 7 | soru | 8 sn | dusunme (sag) |
| 8 | cikti | 8 sn | mutlu (sag) |
| 9 | gorev | 13 sn | isaret (sol) |
| 10 | ozet | 7 sn | on (sag) |
| 11 | kapanis | 9 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Gün 5: Listeler! Bu derste kahramanın çantasını bir listeyle düzenlemeyi; eleman eklemeyi, çıkarmayı ve listeyi incelemeyi öğreneceksin.

- Liste oluşturmak ve indeks
- append, remove, pop
- sum, max, sorted

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Piko! Veri Ormanı'na hoş geldin. Maceraya çıkan her kahramanın bir çantası vardır: kılıç, iksir, harita. Onlarca eşyayı tek tek değişkende tutmak zor olurdu. Çözüm mü? Liste!

**Ekranda başlık:** Gün 5: Listeler

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** mutlu pozu, sag

## Sahne 2: kod (13 sn)

**Seslendirme:** Liste, köşeli parantez içinde virgülle ayrılmış değerler. append sona yeni bir eşya ekler. Stringlerdeki gibi indeks sıfırdan başlar, len de kaç eleman olduğunu söyler.

**Ekranda başlık:** Çanta: liste oluşturmak

**Kod** (vurgulanan satırlar: 1, 2):

```python
inventory = ["kılıç", "iksir"]
inventory.append("harita")
print(inventory)
print("İlk eşya:", inventory[0])
print("Eşya sayısı:", len(inventory))
```

**Çıktı:**

```text
['kılıç', 'iksir', 'harita']
İlk eşya: kılıç
Eşya sayısı: 3
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: Çantaya kılıç, iksir ve harita simgeleri sırayla düşer.*

## Sahne 3: kod (14 sn)

**Seslendirme:** remove bulduğu ilk taşı çantadan atar. in ile bir eşya var mı diye sorarsın. pop ise son elemanı çıkarır ve sana geri verir; onu bir değişkende yakalayabilirsin.

**Ekranda başlık:** Çıkar ve kontrol et

**Kod** (vurgulanan satırlar: 2, 5):

```python
inventory = ["kılıç", "iksir", "taş"]
inventory.remove("taş")
print(inventory)
print("iksir" in inventory)
last = inventory.pop()
print("Çıkan:", last, "Kalan:", inventory)
```

**Çıktı:**

```text
['kılıç', 'iksir']
True
Çıkan: iksir Kalan: ['kılıç']
```

**Maskot:** konusma pozu, sag

## Sahne 4: kod (10 sn)

**Seslendirme:** Bir elemanı değiştirmek için sıra numarasını yazıp yeni değeri koyarsın. insert ise istediğin sıraya ekler; sıfır dersen en başa.

**Ekranda başlık:** Değiştir ve araya ekle

**Kod** (vurgulanan satırlar: 2, 3):

```python
inventory = ["kılıç", "iksir"]
inventory[1] = "kalkan"
inventory.insert(0, "harita")
print(inventory)
```

**Çıktı:**

```text
['harita', 'kılıç', 'kalkan']
```

**Maskot:** isaret pozu, sag

## Sahne 5: kod (12 sn)

**Seslendirme:** Sayı listelerinde sum toplamı, max en büyüğü, min en küçüğü verir. sorted sıralanmış yeni bir liste döndürür, asıl liste bozulmaz. Dilimleme de stringlerdeki gibi çalışır.

**Ekranda başlık:** Listeyi incelemek

**Kod**:

```python
scores = [40, 85, 60, 95]
print(sum(scores), max(scores), min(scores))
print(sorted(scores))
print(scores[0:2])
```

**Çıktı:**

```text
280 95 40
[40, 60, 85, 95]
[40, 85]
```

**Maskot:** konusma pozu, sag

## Sahne 6: hata (12 sn)

**Seslendirme:** Üç eşyalı listede üç numaralı eleman yok! Sayma sıfırdan başladığı için son eleman iki numarada. Python IndexError der: bu sıra numarası listenin dışında. Son eleman için eksi bir hep güvenlidir.

**Ekranda başlık:** IndexError

**Kod** (vurgulanan satırlar: 2):

```python
inventory = ["kılıç", "iksir", "harita"]
print(inventory[3])
```

**Çıktı:**

```text
IndexError: list index out of range
```

**Düzeltilmiş kod:**

```python
inventory = ["kılıç", "iksir", "harita"]
print(inventory[-1])
```

**Düzeltilmiş çıktı:**

```text
harita
```

**Maskot:** sasirma pozu, sag

## Sahne 7: soru (8 sn)

**Seslendirme:** Hadi bir tahmin yap! Bu kod hangi iki sayıyı yazdırır?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```python
nums = [3, 1, 2]
nums.append(5)
print(len(nums), nums[-1])
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (8 sn)

**Seslendirme:** Dört ve beş! append beşi sona ekledi, liste dört elemanlı oldu. Eksi bir de son elemanı, yani beşi verdi.

**Ekranda başlık:** Cevap

**Kod**:

```python
nums = [3, 1, 2]
nums.append(5)
print(len(nums), nums[-1])
```

**Çıktı:**

```text
4 5
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (13 sn)

**Seslendirme:** Sıra sende! Çantaya iksir ekleyecek, gereksiz taşı atacak ve skor tablosunu hazır fonksiyonlarla hesaplayacaksın. Sahne görevinde bir odanın ortasına Piko yerleştireceksin. Challenge'da da isimleri alfabetik sıraya dizeceksin.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Çantaya ekle
- Görev 2: Taşı at
- Görev 3: Skor tablosu
- Sahne görevi: Odaya Piko koy
- Challenge: Alfabetik sıralama

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (7 sn)

**Seslendirme:** Bugün eşyaları bir listede topladık, ekledik, çıkardık ve listeyi hazır fonksiyonlarla inceledik.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- Liste: [ ] içinde değerler, indeks 0'dan başlar
- append, insert, remove, pop ile değiştir
- in, len, sum, max, min, sorted ile incele

**Maskot:** on pozu, sag

## Sahne 11: kapanis (9 sn)

**Seslendirme:** Çantan artık düzenli! Yarın ormanın ağaçlarında eski kaşiflerin kazıdığı koordinatları bulacağız: kimsenin değiştiremediği mühürlü kutular, yani tuple'lar.

**Ekranda başlık:** Yarın: Tuple'lar

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** Bu dersin interaktif hâli 30gunde.com.tr'de seni bekliyor. Kodunu tarayıcıda yaz, hemen çalıştır ve görevleri tamamla!

**Ekranda:** İnteraktif dersler için **30gunde.com.tr**

- Kodunu tarayıcıda yaz ve çalıştır
- Görevleri tamamla, rozet kazan
- 30 günde adım adım Python
