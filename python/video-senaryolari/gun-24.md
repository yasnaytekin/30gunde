# Video senaryosu: Gün 24, İstatistik ve NumPy

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~143 sn

Piko, Bilgi Limanı'nın kayıt ofisinde statistics modülüyle ortalama, ortanca ve tepe değeri; NumPy dizileriyle toplu işlem ve koşulla seçimi anlatıyor.

Ders metni: [gun-24.md](../gunler/gun-24.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | dusunme (sag) |
| 2 | anlatim | 17 sn | isaret (sol) |
| 3 | kod | 16 sn | isaret (sag) |
| 4 | anlatim | 11 sn | konusma (sag) |
| 5 | soru | 10 sn | dusunme (sag) |
| 6 | cikti | 12 sn | sasirma (sol) |
| 7 | kod | 16 sn | isaret (sag) |
| 8 | hata | 11 sn | uzgun (sol) |
| 9 | gorev | 13 sn | konusma (sag) |
| 10 | ozet | 11 sn | on (sag) |
| 11 | kapanis | 12 sn | tebrik (orta) |

## Sahne 1: acilis (14 sn)

**Seslendirme:** Selam, ben Piko! Bilgi Limanı'nın kayıt ofisinde yüzlerce geminin varış süresi yazılı. Liman başkanı soruyor: Gemiler ortalama kaç saatte geliyor, en sık hangi süre görülüyor? Bugün Python'la sayıları konuşturacağız!

**Ekranda başlık:** Gün 24: İstatistik ve NumPy

**Ekranda maddeler:**

- Bilgi Limanı
- statistics ve NumPy

**Maskot:** dusunme pozu, sag

*Yönetmen notu: Arka plan: Bilgi Limanı bölge görseli (gorseller/python/harita/liman.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Kayıt ofisinde üst üste yığılmış defterler, sayılar havada uçuşur.*

## Sahne 2: anlatim (17 sn)

**Seslendirme:** Dört temel ölçü var. Ortalama: hepsini topla, sayısına böl. Ortanca: sıralayınca tam ortadaki değer. Tepe değer: en sık görülen. Standart sapma ise sayıların ortalamadan ne kadar uzağa dağıldığını söyler.

**Ekranda başlık:** Temel ölçüler

**Ekranda maddeler:**

- Ortalama (mean)
- Ortanca (median)
- Tepe değer (mode)
- Standart sapma (stdev)

**Maskot:** isaret pozu, sol

## Sahne 3: kod (16 sn)

**Seslendirme:** statistics modülü Python'la birlikte gelir ve bu ölçüleri hazır hesaplar. Bak, on iki saatlik tek bir geç gemi ortalamayı altıya çekti ama ortanca beşte kaldı. Ortanca uç değerlerden pek etkilenmez.

**Ekranda başlık:** Varış süreleri: statistics

**Kod** (vurgulanan satırlar: 4, 5, 6):

```python
import statistics

times = [3, 5, 5, 6, 12]
print("Ortalama:", statistics.mean(times))
print("Ortanca:", statistics.median(times))
print("En sık:", statistics.mode(times))
print("Sapma:", round(statistics.stdev(times), 2))
```

**Çıktı:**

```text
Ortalama: 6.2
Ortanca: 5
En sık: 5
Sapma: 3.42
```

**Maskot:** isaret pozu, sag

## Sahne 4: anlatim (11 sn)

**Seslendirme:** NumPy, bilim insanlarının en sevdiği paket. array yapısı listeye benzer ama bir işlemi tüm elemanlara birden uygular.

**Ekranda başlık:** NumPy dizileri

**Ekranda maddeler:**

- import numpy as np
- np.array([10, 20, 30])
- İşlem tüm elemanlara birden

**Maskot:** konusma pozu, sag

## Sahne 5: soru (10 sn)

**Seslendirme:** Aynı listeyi bir kez olduğu gibi, bir kez de NumPy dizisi yapıp iki ile çarpıyorum. Sence iki satırda ne görürüz?

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```python
import numpy as np

nums = [10, 20, 30]
print("Liste * 2:", nums * 2)
print("Dizi * 2:", np.array(nums) * 2)
```

**Maskot:** dusunme pozu, sag

## Sahne 6: cikti (12 sn)

**Seslendirme:** Aynı işlem, çok farklı sonuç! Liste iki kez yan yana eklendi. Dizi ise her elemanı iki katına çıkardı. Dizinin virgülsüz yazıldığına da dikkat et.

**Ekranda başlık:** Cevap: liste mi dizi mi?

**Kod**:

```python
import numpy as np

nums = [10, 20, 30]
print("Liste * 2:", nums * 2)
print("Dizi * 2:", np.array(nums) * 2)
```

**Çıktı:**

```text
Liste * 2: [10, 20, 30, 10, 20, 30]
Dizi * 2: [20 40 60]
```

**Maskot:** sasirma pozu, sol

*Yönetmen notu: Kod numpy paketini kullanır; doğrulayıcının Python ortamında kurulu olmalı.*

## Sahne 7: kod (16 sn)

**Seslendirme:** Dizilerde köşeli parantezin içine koşul yazarak seçim yapabilirsin. Elli ve üstü olanlar süzülüyor. Koşulun sonucunu sum ile toplarsan kaç kişinin geçtiğini bulursun. mean de ortalamayı veriyor.

**Ekranda başlık:** Koşulla seçmek

**Kod** (vurgulanan satırlar: 4, 5):

```python
import numpy as np

scores = np.array([45, 90, 12, 77, 60])
print("Geçenler:", scores[scores >= 50])
print("Kaç kişi:", (scores >= 50).sum())
print("Ortalama:", scores.mean())
```

**Çıktı:**

```text
Geçenler: [90 77 60]
Kaç kişi: 3
Ortalama: 56.8
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: Kod numpy paketini kullanır; doğrulayıcının Python ortamında kurulu olmalı.*

## Sahne 8: hata (11 sn)

**Seslendirme:** Sık hata: boş bir listenin ortalamasını istemek. Hiç sayı yoksa ortalama da olmaz, Python StatisticsError verir. Hesaplamadan önce listenin boş olmadığına bak.

**Ekranda başlık:** Sık hata: boş liste

**Kod** (vurgulanan satırlar: 4):

```python
import statistics

scores = []
print(statistics.mean(scores))
```

**Çıktı:**

```text
statistics.StatisticsError: mean requires at least one data point
```

**Maskot:** uzgun pozu, sol

## Sahne 9: gorev (13 sn)

**Seslendirme:** Görevlerde ortalama ve ortancayı hesaplayacak, en sık gelen zarı bulacak ve döngü kullanmadan skorları iki katına çıkaracaksın. Projede de oyuncuların oyun sürelerini özetliyorsun.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Ortalama ve ortanca
- Görev 2: En sık zar
- Görev 3: NumPy ile iki katı
- Challenge: Kaç kişi geçti?
- Proje: Oyun istatistikleri

**Maskot:** konusma pozu, sag

## Sahne 10: ozet (11 sn)

**Seslendirme:** Özetle: statistics ile ölçüleri hesapla, NumPy ile tüm diziye birden işlem yap, koşulla da süz.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- mean, median, mode, stdev
- np.array: işlem tüm elemanlara
- dizi[koşul] ile seçim

**Maskot:** on pozu, sag

## Sahne 11: kapanis (12 sn)

**Seslendirme:** Sayılar konuştu, harikasın! Yarın bu sayıları tablolara dizeceğiz. pandas ile satır ve sütunları filtreleyip özetlemeyi öğreneceğiz. Görüşürüz!

**Ekranda başlık:** Yarın: Pandas

**Ekranda maddeler:**

- DataFrame
- Filtrele ve özetle

**Maskot:** tebrik pozu, orta
