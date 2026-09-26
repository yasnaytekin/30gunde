# Gün 25: Pandas

**Kurs:** 30 Günde Python  ·  **Bölge:** Bilgi Limanı  ·  **Maskot:** Piko

**Bugünün hedefi:** pandas ile tablo verisi oluşturmak, incelemek, filtrelemek ve özetlemek

> Liman başkanının masasında dev bir defter var: her satırda bir gemi, her sütunda bir bilgi. Satır satır okumak yerine "en çok yük taşıyan kim?" diye sorup anında cevap almak istiyor. Bugün tablolar için süper güçlü bir alet olan **pandas** ile tanışıyoruz.

![Bilgi Limanı](../../gorseller/python/harita/liman.webp)

## Konu anlatımı

### DataFrame: Python'da tablo

pandas'ın kalbi **DataFrame** denen tablodur. Bir sözlükten kolayca oluşturulur; anahtarlar sütun adları, listeler sütunların değerleri olur:

```python
import pandas as pd

data = {"isim": ["Piko", "Ece", "Can"], "skor": [300, 250, 120]}
df = pd.DataFrame(data)
print(df)
```

İlk çalıştırmada pandas yükleneceği için biraz bekleyebilirsin.

### Tabloyu tanımak

- `df.head()` ilk 5 satır
- `df.shape` (satır sayısı, sütun sayısı)
- `df.columns` sütun adları
- `df.describe()` sayısal sütunların özeti

Tek bir sütun `df["skor"]` şeklinde alınır. Buna **Series** denir ve `.mean()`, `.max()`, `.sum()` gibi metotları vardır.

### Filtrelemek ve sıralamak

```python
winners = df[df["skor"] >= 200]           # koşula uyan satırlar
top = df.sort_values("skor", ascending=False)
best = top.iloc[0]["isim"]                # ilk satırın isim hücresi
names = df["isim"].tolist()               # sütunu listeye çevir
```

Yeni sütun eklemek de kolay: `df["bonus"] = df["skor"] * 2`

### CSV ve gruplama

Gerçek veriler çoğu zaman **CSV** dosyasında gelir: virgülle ayrılmış satırlar. `pd.read_csv("dosya.csv")` onu tabloya çevirir. Elimizde yazı olarak varsa `io.StringIO` ile dosya gibi okutabiliriz.

Aynı değere sahip satırları toplamak için `groupby` kullanılır:

```python
totals = df.groupby("oyuncu")["skor"].sum()
print(totals.idxmax())   # toplamı en yüksek oyuncu
```

## Örnekler

### İlk tablo

```python
import pandas as pd

data = {"isim": ["Piko", "Ece", "Can"], "skor": [300, 250, 120]}
df = pd.DataFrame(data)
print(df)
print("Boyut:", df.shape)
print("Ortalama skor:", df["skor"].mean())
```

### Filtre ve sıralama

```python
import pandas as pd

df = pd.DataFrame({"isim": ["Piko", "Ece", "Can", "Ada"], "skor": [300, 250, 120, 280]})
print(df[df["skor"] >= 250])
print(df.sort_values("skor", ascending=False)["isim"].tolist())
```

### CSV ve gruplama

```python
import io
import pandas as pd

csv = """oyuncu,skor
Piko,50
Ece,70
Piko,40
Ece,10
"""
df = pd.read_csv(io.StringIO(csv))
totals = df.groupby("oyuncu")["skor"].sum()
print(totals)
print("Kazanan:", totals.idxmax())
```

## Görevler

### Görev 1: İlk tablom

`data` sözlüğünden `df` adında bir DataFrame oluştur. Sonra satır sayısını `rows` değişkenine koy.

**Başlangıç kodu:**

```python
import pandas as pd

data = {"gemi": ["Martı", "Yunus", "Kartal"], "yük": [12, 30, 7]}

df = None
rows = 0

print(df)
print("Satır:", rows)
```

**İpuçları:**

1. df = pd.DataFrame(data)
2. df.shape (satır, sütun) verir; satır sayısı df.shape[0] ya da len(df)

<details><summary>Çözüm</summary>

```python
import pandas as pd

data = {"gemi": ["Martı", "Yunus", "Kartal"], "yük": [12, 30, 7]}

df = pd.DataFrame(data)
rows = df.shape[0]

print(df)
print("Satır:", rows)
```

</details>

### Görev 2: Ortalama yük

`df` tablosundaki `yük` sütununun ortalamasını `avg` değişkenine koy.

**Başlangıç kodu:**

```python
import pandas as pd

data = {"gemi": ["Martı", "Yunus", "Kartal"], "yük": [12, 30, 6]}
df = pd.DataFrame(data)

avg = 0

print("Ortalama yük:", avg)
```

**İpuçları:**

1. Sütun: df["yük"]
2. Ortalama: .mean()

<details><summary>Çözüm</summary>

```python
import pandas as pd

data = {"gemi": ["Martı", "Yunus", "Kartal"], "yük": [12, 30, 6]}
df = pd.DataFrame(data)

avg = df["yük"].mean()

print("Ortalama yük:", avg)
```

</details>

### Görev 3: Ağır gemiler

Yükü 10 veya daha fazla olan gemilerin isimlerini **liste** olarak `heavy` değişkenine koy.

**Başlangıç kodu:**

```python
import pandas as pd

data = {"gemi": ["Martı", "Yunus", "Kartal", "Balina"], "yük": [12, 30, 7, 10]}
df = pd.DataFrame(data)

heavy = []

print(heavy)
```

**İpuçları:**

1. Önce satırları filtrele: df[df["yük"] >= 10]
2. Sonra gemi sütununu listeye çevir: ["gemi"].tolist()

<details><summary>Çözüm</summary>

```python
import pandas as pd

data = {"gemi": ["Martı", "Yunus", "Kartal", "Balina"], "yük": [12, 30, 7, 10]}
df = pd.DataFrame(data)

heavy = df[df["yük"] >= 10]["gemi"].tolist()

print(heavy)
```

</details>

## Challenge: En iyi oyuncu

Tabloyu `skor`'a göre büyükten küçüğe sırala ve en yüksek skorlu oyuncunun ismini `best` değişkenine koy.

**Başlangıç kodu:**

```python
import pandas as pd

data = {"isim": ["Ali", "Piko", "Ece"], "skor": [120, 300, 250]}
df = pd.DataFrame(data)

best = ""

print("En iyi:", best)
```

**İpuçları:**

1. df.sort_values("skor", ascending=False)
2. İlk satırın ismi: top.iloc[0]["isim"]

<details><summary>Çözüm</summary>

```python
import pandas as pd

data = {"isim": ["Ali", "Piko", "Ece"], "skor": [120, 300, 250]}
df = pd.DataFrame(data)

top = df.sort_values("skor", ascending=False)
best = top.iloc[0]["isim"]

print("En iyi:", best)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Skor analizi**

### Piko'nun Macerası: Skor analizi

Piko'nun Macerası'nda oynanan oyunların skorları CSV olarak geldi. Aynı oyuncu birden çok kez oynamış olabilir.

- CSV'yi `df` tablosuna oku.
- `totals`: her oyuncunun toplam skoru (`groupby`)
- `winner`: toplamı en yüksek oyuncu
- `Kazanan: Ece` gibi yazdır.

**Başlangıç kodu:**

```python
import io
import pandas as pd

csv = """oyuncu,skor
Piko,50
Ece,70
Piko,40
Ece,30
Can,80
"""

df = None
totals = None
winner = ""

print(f"Kazanan: {winner}")
```

**İpuçları:**

1. pd.read_csv(io.StringIO(csv))
2. df.groupby("oyuncu")["skor"].sum()
3. En büyük toplamın sahibi: totals.idxmax()

<details><summary>Çözüm</summary>

```python
import io
import pandas as pd

csv = """oyuncu,skor
Piko,50
Ece,70
Piko,40
Ece,30
Can,80
"""

df = pd.read_csv(io.StringIO(csv))
totals = df.groupby("oyuncu")["skor"].sum()
winner = totals.idxmax()

print(f"Kazanan: {winner}")
```

</details>

### Harcama Defteri: Kategori analizi

Bankadan indirdiğin harcamalar CSV olarak `csv` değişkeninde (`kategori,tutar`). Aynı kategoride birden çok harcama olabilir.

- CSV'yi `df` tablosuna oku (`pd.read_csv(io.StringIO(csv))`).
- `by_category`: her kategorinin toplam harcaması (`groupby` ve `sum`)
- `top`: toplamı en yüksek kategori (`idxmax()`)
- `En çok harcama: market` gibi yazdır.

**Başlangıç kodu:**

```python
import io
import pandas as pd

csv = """kategori,tutar
market,120
kahve,35
market,300
ulaşım,150
"""
```

**İpuçları:**

1. df.groupby("kategori")["tutar"].sum()
2. by_category.idxmax() en büyük değerin etiketini verir.

<details><summary>Çözüm</summary>

```python
import io
import pandas as pd

csv = """kategori,tutar
market,120
kahve,35
market,300
ulaşım,150
"""
df = pd.read_csv(io.StringIO(csv))
by_category = df.groupby("kategori")["tutar"].sum()
top = by_category.idxmax()
print(by_category)
print("En çok harcama:", top)
```

</details>

### Görev Asistanı: Kim ne kadar çalıştı?

Bir proje ekibinin görev kayıtları CSV olarak `csv` değişkeninde (`kisi,gorev,sure`).

- CSV'yi `df` tablosuna oku.
- `per_person`: her kişinin toplam süresi (`groupby` ve `sum`)
- `busiest`: en çok çalışan kişi (`idxmax()`)
- `En yoğun: Ece` gibi yazdır.

**Başlangıç kodu:**

```python
import io
import pandas as pd

csv = """kisi,gorev,sure
Ece,rapor,90
Can,sunum,60
Ece,e-posta,20
Can,toplantı,30
"""
```

**İpuçları:**

1. pd.read_csv(io.StringIO(csv))
2. df.groupby("kisi")["sure"].sum() ve .idxmax()

<details><summary>Çözüm</summary>

```python
import io
import pandas as pd

csv = """kisi,gorev,sure
Ece,rapor,90
Can,sunum,60
Ece,e-posta,20
Can,toplantı,30
"""
df = pd.read_csv(io.StringIO(csv))
per_person = df.groupby("kisi")["sure"].sum()
busiest = per_person.idxmax()
print(per_person)
print("En yoğun:", busiest)
```

</details>

### Kişisel Web Sitem: Popüler sayfalar

Sitenin ziyaret kayıtları CSV olarak `csv` değişkeninde (`sayfa,goruntulenme`). Aynı sayfa birden çok kez geçebilir.

- CSV'yi `df` tablosuna oku (`pd.read_csv(io.StringIO(csv))`).
- `total_views`: toplam görüntülenme (tam sayı: `int(...)`)
- `by_page`: her sayfanın toplam görüntülenmesi (`groupby` ve `sum`)
- `popular`: en çok görüntülenen sayfa (`idxmax()`)

Sonra şöyle yazdır:

```
Toplam görüntülenme: 475
En popüler sayfa: /blog.html
```

**Başlangıç kodu:**

```python
import io
import pandas as pd

csv = """sayfa,goruntulenme
/index.html,120
/blog.html,80
/index.html,95
/hakkimda.html,30
/blog.html,150
"""
```

**İpuçları:**

1. df["goruntulenme"].sum() bütün sütunu toplar.
2. df.groupby("sayfa")["goruntulenme"].sum() ve by_page.idxmax()

<details><summary>Çözüm</summary>

```python
import io
import pandas as pd

csv = """sayfa,goruntulenme
/index.html,120
/blog.html,80
/index.html,95
/hakkimda.html,30
/blog.html,150
"""
df = pd.read_csv(io.StringIO(csv))
total_views = int(df["goruntulenme"].sum())
by_page = df.groupby("sayfa")["goruntulenme"].sum()
popular = by_page.idxmax()
print("Toplam görüntülenme:", total_views)
print("En popüler sayfa:", popular)
```

</details>

### Sohbet Botu: Sohbet kaydı analizi

Kullanıcılar botun her cevabına 1-5 arası puan verdi. Kayıtlar CSV olarak `csv` değişkeninde (`niyet,puan`).

- CSV'yi `df` tablosuna oku (`pd.read_csv(io.StringIO(csv))`).
- `by_intent`: her niyetin ortalama puanı (`groupby` ve `mean`)
- `worst`: ortalaması en düşük niyet (`idxmin()`, `idxmax()`'ın tersi)
- `low_count`: puanı 2 veya daha düşük kaç cevap var (tabloyu filtreleyip `len()`)

Sonra şöyle yazdır:

```
En zayıf niyet: hava
Düşük puanlı cevap: 2
```

**Başlangıç kodu:**

```python
import io
import pandas as pd

csv = """niyet,puan
selam,5
hava,2
selam,4
hava,3
saat,4
saat,2
"""
```

**İpuçları:**

1. df.groupby("niyet")["puan"].mean() ve by_intent.idxmin()
2. df[df["puan"] <= 2] sadece düşük puanlı satırları seçer.

<details><summary>Çözüm</summary>

```python
import io
import pandas as pd

csv = """niyet,puan
selam,5
hava,2
selam,4
hava,3
saat,4
saat,2
"""
df = pd.read_csv(io.StringIO(csv))
by_intent = df.groupby("niyet")["puan"].mean()
worst = by_intent.idxmin()
low_count = len(df[df["puan"] <= 2])
print(by_intent)
print("En zayıf niyet:", worst)
print("Düşük puanlı cevap:", low_count)
```

</details>

### Okul Not Defteri: Sınav sonuçları analizi

Dönemin sınav sonuçları CSV olarak `csv` değişkeninde (`ders,sinav,puan`). Her dersten birden çok sınav var.

- CSV'yi `df` tablosuna oku (`pd.read_csv(io.StringIO(csv))`).
- `averages`: her dersin ortalama puanı (`groupby` ve `mean`)
- `weakest`: ortalaması en düşük ders (`idxmin()`)
- `low_count`: puanı 50'nin altında olan sınav sayısı (filtreleyip `len`)
- `Daha çok çalış: Fizik` ve `50 altı sınav: 1` yazdır.

**Başlangıç kodu:**

```python
import io
import pandas as pd

csv = """ders,sinav,puan
Matematik,1,80
Fizik,1,55
Matematik,2,90
Fizik,2,45
Tarih,1,75
"""
```

**İpuçları:**

1. df.groupby("ders")["puan"].mean() ve .idxmin()
2. df[df["puan"] < 50] sadece 50 altı satırları verir.

<details><summary>Çözüm</summary>

```python
import io
import pandas as pd

csv = """ders,sinav,puan
Matematik,1,80
Fizik,1,55
Matematik,2,90
Fizik,2,45
Tarih,1,75
"""
df = pd.read_csv(io.StringIO(csv))
averages = df.groupby("ders")["puan"].mean()
weakest = averages.idxmin()
low_count = len(df[df["puan"] < 50])
print(averages)
print("Daha çok çalış:", weakest)
print("50 altı sınav:", low_count)
```

</details>
