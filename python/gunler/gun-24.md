# Gün 24: İstatistik ve NumPy

**Kurs:** 30 Günde Python  ·  **Bölge:** Bilgi Limanı  ·  **Maskot:** Piko

**Bugünün hedefi:** statistics modülü ve NumPy ile ortalama, ortanca, tepe değer ve dizi işlemleri yapmak

> Limanın kayıt ofisinde yüzlerce geminin varış süreleri yazılı. Liman başkanı soruyor: "Gemiler ortalama kaç saatte geliyor? En çok hangi süre görülüyor?" Sayı yığınlarından anlam çıkarmaya **istatistik** denir. Bugün Python'la sayıları konuşturacağız.

![Bilgi Limanı](../../gorseller/python/harita/liman.webp)

## Konu anlatımı

### Temel ölçüler

- **Ortalama** (mean): hepsini topla, kaç tane olduğuna böl
- **Ortanca** (median): sıraladığında tam ortadaki değer
- **Tepe değer** (mode): en sık görülen değer
- **Standart sapma** (stdev): sayılar ortalamadan ne kadar uzağa dağılıyor?

Ortanca, çok büyük ya da çok küçük tek bir sayıdan ortalama kadar etkilenmez.

### statistics modülü

Python'ın içinde gelen `statistics` modülü bu ölçüleri hazır hesaplar:

```python
import statistics

times = [3, 5, 5, 6, 12]
print(statistics.mean(times))     # 6.2
print(statistics.median(times))   # 5
print(statistics.mode(times))     # 5
print(round(statistics.stdev(times), 2))
```

### NumPy dizileri

**NumPy**, bilim insanlarının en çok kullandığı pakettir. Onun `array` yapısı listeye benzer ama matematik işlemlerini **tüm elemanlara birden** uygular:

```python
import numpy as np

a = np.array([10, 20, 30])
print(a * 2)        # [20 40 60]
print(a + a)        # [20 40 60]
print(a.mean(), a.max(), a.sum())
```

Normal bir listeyle `[10, 20] * 2` yazsan liste iki kez yan yana eklenirdi!

İlk çalıştırmada NumPy paketi yükleneceği için birkaç saniye bekleyebilirsin.

### Koşulla seçmek

NumPy dizilerinde köşeli parantezin içine koşul yazarak eleman seçebilirsin:

```python
scores = np.array([45, 90, 12, 77])
print(scores[scores >= 50])   # [90 77]
print((scores >= 50).sum())   # 2 kişi geçti
```

## Örnekler

### Varış süreleri

```python
import statistics

times = [3, 5, 5, 6, 12]
print("Ortalama:", statistics.mean(times))
print("Ortanca:", statistics.median(times))
print("En sık:", statistics.mode(times))
print("Sapma:", round(statistics.stdev(times), 2))
```

### Liste mi dizi mi?

```python
import numpy as np

nums = [10, 20, 30]
print("Liste * 2:", nums * 2)
print("Dizi * 2:", np.array(nums) * 2)
```

*Aynı işlem, çok farklı sonuç!*

### Filtre

```python
import numpy as np

scores = np.array([45, 90, 12, 77, 60])
print("Geçenler:", scores[scores >= 50])
print("Kaç kişi:", (scores >= 50).sum())
print("Ortalama:", scores.mean())
```

## Görevler

### Görev 1: Ortalama ve ortanca

`statistics` modülüyle `scores` listesinin ortalamasını `avg`, ortancasını `mid` değişkenine koy.

**Başlangıç kodu:**

```python
import statistics

scores = [70, 85, 85, 90, 40]

avg = 0
mid = 0

print(avg, mid)
```

**İpuçları:**

1. statistics.mean(scores)
2. statistics.median(scores)

<details><summary>Çözüm</summary>

```python
import statistics

scores = [70, 85, 85, 90, 40]

avg = statistics.mean(scores)
mid = statistics.median(scores)

print(avg, mid)
```

</details>

### Görev 2: En sık zar

`rolls` listesinde en çok gelen zarı `most` değişkenine koy.

**Başlangıç kodu:**

```python
import statistics

rolls = [3, 6, 2, 6, 1, 6, 3]

most = 0

print("En sık gelen:", most)
```

**İpuçları:**

1. Tepe değer için statistics.mode(rolls)

<details><summary>Çözüm</summary>

```python
import statistics

rolls = [3, 6, 2, 6, 1, 6, 3]

most = statistics.mode(rolls)

print("En sık gelen:", most)
```

</details>

### Görev 3: NumPy ile iki katı

`scores` listesini bir NumPy dizisine çevir ve tüm skorları iki katına çıkaran `doubled` dizisini oluştur. Döngü kullanma!

**Başlangıç kodu:**

```python
import numpy as np

scores = [10, 25, 40]

doubled = scores

print(doubled)
```

**İpuçları:**

1. np.array(scores) ile diziye çevir.
2. Diziyi doğrudan 2 ile çarp.

<details><summary>Çözüm</summary>

```python
import numpy as np

scores = [10, 25, 40]

doubled = np.array(scores) * 2

print(doubled)
```

</details>

## Challenge: Kaç kişi geçti?

NumPy ile `scores` içinde 50 ve üstü olanları `passed` dizisine, bunların sayısını `count` değişkenine koy.

**Başlangıç kodu:**

```python
import numpy as np

scores = np.array([45, 90, 12, 77, 50])

passed = scores
count = 0

print(passed, count)
```

**İpuçları:**

1. Koşulla seçim: scores[scores >= 50]
2. Sayısı için len(passed)

<details><summary>Çözüm</summary>

```python
import numpy as np

scores = np.array([45, 90, 12, 77, 50])

passed = scores[scores >= 50]
count = len(passed)

print(passed, count)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Oyun istatistikleri**

### Piko'nun Macerası: Oyun istatistikleri

Oyuncuların günlük oyun süreleri (dakika) `play_times` listesinde. Şunları yazdır:

```
Ortalama: 31.4
En uzun: 55
En kısa: 12
Toplam: 157
```

Ortalamayı 1 basamağa yuvarla.

**Başlangıç kodu:**

```python
import statistics

play_times = [25, 40, 12, 55, 25]

# Dört satırı yazdır
```

**İpuçları:**

1. round(statistics.mean(play_times), 1)
2. max, min ve sum hazır fonksiyonlarını kullan.

<details><summary>Çözüm</summary>

```python
import statistics

play_times = [25, 40, 12, 55, 25]

print("Ortalama:", round(statistics.mean(play_times), 1))
print("En uzun:", max(play_times))
print("En kısa:", min(play_times))
print("Toplam:", sum(play_times))
```

</details>

### Harcama Defteri: Harcama istatistikleri

`amounts` listesindeki harcamaların istatistiklerini `statistics` modülüyle çıkaralım. Şunları yazdır:

```
Ortalama: 184.2
Ortanca: 120
En büyük: 450
```

Ortalamayı 1 basamağa yuvarla (`round`).

**Başlangıç kodu:**

```python
import statistics

amounts = [120, 45, 450, 90, 216]
```

**İpuçları:**

1. statistics.mean() ortalama, statistics.median() ortanca verir.
2. round(x, 1) bir basamağa yuvarlar.

<details><summary>Çözüm</summary>

```python
import statistics

amounts = [120, 45, 450, 90, 216]
print("Ortalama:", round(statistics.mean(amounts), 1))
print("Ortanca:", statistics.median(amounts))
print("En büyük:", max(amounts))
```

</details>

### Görev Asistanı: Görev süreleri

Geçen haftaki görevlerin süreleri (dakika) `durations` listesinde. `statistics` modülüyle şunları yazdır:

```
Ortalama: 38.6 dk
Ortanca: 30 dk
Uzun görev sayısı: 2
```

Ortalamayı 1 basamağa yuvarla. Uzun görev: ortalamadan uzun sürenler.

**Başlangıç kodu:**

```python
import statistics

durations = [25, 30, 90, 18, 30]
```

**İpuçları:**

1. statistics.mean() ve statistics.median()
2. Uzun görevler: [d for d in durations if d > mean]

<details><summary>Çözüm</summary>

```python
import statistics

durations = [25, 30, 90, 18, 30]
mean = statistics.mean(durations)
print(f"Ortalama: {round(mean, 1)} dk")
print(f"Ortanca: {statistics.median(durations)} dk")
long_tasks = [d for d in durations if d > mean]
print(f"Uzun görev sayısı: {len(long_tasks)}")
```

</details>

### Kişisel Web Sitem: Ziyaretçi istatistikleri

Son bir haftada sitene her gün kaç kişinin geldiği `visits` listesinde.

- `mean`: ortalama ziyaret (`statistics.mean`, 1 basamağa yuvarla: `round`)
- `median`: ortanca (`statistics.median`)
- `busy_days`: ortalamanın **üstünde** ziyaret alan gün sayısı. Listeyi NumPy dizisine çevir (`np.array`), `>` ile koşul yaz ve `.sum()` ile say.

Sonra şöyle yazdır:

```
Ortalama: 185.1
Ortanca: 131
Yoğun gün: 2
```

**Başlangıç kodu:**

```python
import statistics
import numpy as np

visits = [120, 95, 310, 150, 88, 402, 131]
```

**İpuçları:**

1. statistics.mean() ortalama, statistics.median() ortanca verir.
2. arr > mean her gün için True/False verir; (arr > mean).sum() True'ları sayar.

<details><summary>Çözüm</summary>

```python
import statistics
import numpy as np

visits = [120, 95, 310, 150, 88, 402, 131]
mean = round(statistics.mean(visits), 1)
median = statistics.median(visits)
arr = np.array(visits)
busy_days = int((arr > mean).sum())
print("Ortalama:", mean)
print("Ortanca:", median)
print("Yoğun gün:", busy_days)
```

</details>

### Sohbet Botu: Mesaj uzunlukları

Kullanıcılar bota kısa mı, uzun mu yazıyor? `messages` listesindeki mesajlar için:

- `lengths`: her mesajın **kelime** sayısı (list comprehension ve `split()`)
- `statistics` ile ortalamayı (1 basamağa yuvarla) ve ortancayı yazdır.
- `arr = np.array(lengths)` ile bir NumPy dizisi yap ve 2 kelime ya da daha kısa mesajların sayısını bul (`arr[arr <= 2]`).

```
Ortalama: 2.6
Ortanca: 2
Kısa mesaj: 3
```

**Başlangıç kodu:**

```python
import statistics
import numpy as np

messages = ["merhaba", "yarın hava nasıl olacak", "teşekkürler", "saat kaç", "bana bir fıkra anlatır mısın"]
```

**İpuçları:**

1. lengths = [len(m.split()) for m in messages]
2. arr[arr <= 2] sadece 2 ve altındaki değerleri seçer; len() ile say.

<details><summary>Çözüm</summary>

```python
import statistics
import numpy as np

messages = ["merhaba", "yarın hava nasıl olacak", "teşekkürler", "saat kaç", "bana bir fıkra anlatır mısın"]
lengths = [len(m.split()) for m in messages]
print("Ortalama:", round(statistics.mean(lengths), 1))
print("Ortanca:", statistics.median(lengths))
arr = np.array(lengths)
short = arr[arr <= 2]
print("Kısa mesaj:", len(short))
```

</details>

### Okul Not Defteri: Sınıfta neredesin?

Öğretmen sınıfın sınav notlarını paylaştı: `class_scores`. Senin notun `my_score`.

- `statistics` modülüyle sınıf ortalamasını (1 basamağa yuvarla) ve ortancayı yazdır.
- Notları `np.array` ile NumPy dizisine çevir ve **koşulla seçerek** senden yüksek alan kaç kişi olduğunu bul.

```
Sınıf ortalaması: 68.3
Ortanca: 66.0
Senden yüksek: 2 kişi
```

**Başlangıç kodu:**

```python
import statistics
import numpy as np

class_scores = [45, 90, 72, 60, 88, 55]
my_score = 72
```

**İpuçları:**

1. statistics.mean() ortalama, statistics.median() ortanca verir.
2. scores[scores > my_score] senden yüksek notları seçer; len() ile say.

<details><summary>Çözüm</summary>

```python
import statistics
import numpy as np

class_scores = [45, 90, 72, 60, 88, 55]
my_score = 72
print("Sınıf ortalaması:", round(statistics.mean(class_scores), 1))
print("Ortanca:", statistics.median(class_scores))
scores = np.array(class_scores)
higher = scores[scores > my_score]
print(f"Senden yüksek: {len(higher)} kişi")
```

</details>
