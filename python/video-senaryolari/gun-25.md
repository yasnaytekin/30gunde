# Video senaryosu: Gün 25, Pandas

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~143 sn

Piko, Bilgi Limanı başkanının dev defterinden yola çıkarak pandas ile tablo kurmayı, filtrelemeyi, sıralamayı ve CSV verisini gruplayarak özetlemeyi anlatıyor.

Ders metni: [gun-25.md](../gunler/gun-25.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | mutlu (sag) |
| 2 | kod | 16 sn | isaret (sag) |
| 3 | anlatim | 13 sn | konusma (sol) |
| 4 | kod | 14 sn | isaret (sag) |
| 5 | soru | 10 sn | dusunme (sag) |
| 6 | cikti | 10 sn | mutlu (sol) |
| 7 | kod | 17 sn | isaret (sag) |
| 8 | hata | 12 sn | sasirma (sol) |
| 9 | gorev | 13 sn | konusma (sag) |
| 10 | ozet | 11 sn | on (sag) |
| 11 | kapanis | 13 sn | tebrik (orta) |

## Sahne 1: acilis (14 sn)

**Seslendirme:** Selam, ben Piko! Liman başkanının masasında dev bir defter var: her satırda bir gemi, her sütunda bir bilgi. Satır satır okumak yerine, en çok yükü kim taşıyor diye sorup anında cevap almak istiyor. Bugün pandas ile tanışıyoruz!

**Ekranda başlık:** Gün 25: Pandas

**Ekranda maddeler:**

- Bilgi Limanı
- Tablo verisi: DataFrame

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Arka plan: Bilgi Limanı bölge görseli (gorseller/python/harita/liman.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Liman başkanının masasında satır ve sütunlarla dolu dev bir defter.*

## Sahne 2: kod (16 sn)

**Seslendirme:** pandas'ın kalbi DataFrame denen tablo. Onu bir sözlükten kuruyorum: anahtarlar sütun adları, listeler de sütunların değerleri oluyor. Soldaki sıfır, bir, iki satır numaraları. shape satır ve sütun sayısını veriyor.

**Ekranda başlık:** İlk tablo: DataFrame

**Kod** (vurgulanan satırlar: 4, 6):

```python
import pandas as pd

data = {"isim": ["Piko", "Ece", "Can"], "skor": [300, 250, 120]}
df = pd.DataFrame(data)
print(df)
print("Boyut:", df.shape)
print("Ortalama skor:", df["skor"].mean())
```

**Çıktı:**

```text
   isim  skor
0  Piko   300
1   Ece   250
2   Can   120
Boyut: (3, 2)
Ortalama skor: 223.33333333333334
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: Kod pandas paketini kullanır; doğrulayıcının Python ortamında kurulu olmalı.*

## Sahne 3: anlatim (13 sn)

**Seslendirme:** Tabloyu tanımak için birkaç kısayol var. Tek bir sütunu köşeli parantezle alırsın, buna Series denir. Series'in mean, max ve sum gibi hazır metotları vardır.

**Ekranda başlık:** Tabloyu tanımak

**Ekranda maddeler:**

- df.head(): ilk 5 satır
- df.shape, df.columns
- df.describe(): sayısal özet
- df["skor"]: bir sütun (Series)

**Maskot:** konusma pozu, sol

## Sahne 4: kod (14 sn)

**Seslendirme:** Filtrelemek için tablonun içine bir koşul yazıyorum. Skoru iki yüz elli ve üstü olan satırlar kalıyor. Satır numaralarının korunduğuna dikkat et: Can'ın satırı olan iki numara aradan çıktı.

**Ekranda başlık:** Filtrele

**Kod** (vurgulanan satırlar: 5):

```python
import pandas as pd

df = pd.DataFrame({"isim": ["Piko", "Ece", "Can", "Ada"],
                   "skor": [300, 250, 120, 280]})
print(df[df["skor"] >= 250])
```

**Çıktı:**

```text
   isim  skor
0  Piko   300
1   Ece   250
3   Ada   280
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: Kod pandas paketini kullanır; doğrulayıcının Python ortamında kurulu olmalı.*

## Sahne 5: soru (10 sn)

**Seslendirme:** Şimdi sıra sende! Tabloyu skora göre büyükten küçüğe sıralayıp isimleri listeye çeviriyorum. Sence listede sıra nasıl olur?

**Ekranda başlık:** Sence ne yazdırır?

**Kod** (vurgulanan satırlar: 5):

```python
import pandas as pd

df = pd.DataFrame({"isim": ["Piko", "Ece", "Can", "Ada"],
                   "skor": [300, 250, 120, 280]})
top = df.sort_values("skor", ascending=False)
print(top["isim"].tolist())
```

**Maskot:** dusunme pozu, sag

## Sahne 6: cikti (10 sn)

**Seslendirme:** Piko en üstte, sonra Ada, Ece ve Can. ascending False büyükten küçüğe demek, tolist de sütunu düz bir listeye çeviriyor.

**Ekranda başlık:** Cevap

**Kod**:

```python
import pandas as pd

df = pd.DataFrame({"isim": ["Piko", "Ece", "Can", "Ada"],
                   "skor": [300, 250, 120, 280]})
top = df.sort_values("skor", ascending=False)
print(top["isim"].tolist())
```

**Çıktı:**

```text
['Piko', 'Ada', 'Ece', 'Can']
```

**Maskot:** mutlu pozu, sol

*Yönetmen notu: Kod pandas paketini kullanır; doğrulayıcının Python ortamında kurulu olmalı.*

## Sahne 7: kod (17 sn)

**Seslendirme:** Gerçek veriler çoğunlukla CSV dosyasında, virgülle ayrılmış satırlar olarak gelir. read_csv onu tabloya çevirir; burada yazıyı StringIO ile dosya gibi okutuyorum. groupby aynı oyuncunun skorlarını topluyor, idxmax da kazananı buluyor.

**Ekranda başlık:** CSV ve gruplama

**Kod** (vurgulanan satırlar: 5, 6, 8):

```python
import io
import pandas as pd

csv = "oyuncu,skor\nPiko,50\nEce,70\nPiko,40\nEce,10\n"
df = pd.read_csv(io.StringIO(csv))
totals = df.groupby("oyuncu")["skor"].sum()
print(totals)
print("Kazanan:", totals.idxmax())
```

**Çıktı:**

```text
oyuncu
Ece     80
Piko    90
Name: skor, dtype: int64
Kazanan: Piko
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: Kod pandas paketini kullanır; doğrulayıcının Python ortamında kurulu olmalı.*

## Sahne 8: hata (12 sn)

**Seslendirme:** Sık hata: sütun adını yanlış yazmak. Tabloda isim var ama ben ad istedim. pandas bu sütunu bulamayınca KeyError veriyor. Emin değilsen df.columns ile adlara bak.

**Ekranda başlık:** Sık hata: olmayan sütun

**Kod** (vurgulanan satırlar: 4):

```python
import pandas as pd

df = pd.DataFrame({"isim": ["Piko"], "skor": [300]})
print(df["ad"])
```

**Çıktı:**

```text
KeyError: 'ad'
```

**Maskot:** sasirma pozu, sol

*Yönetmen notu: Kod pandas paketini kullanır; doğrulayıcının Python ortamında kurulu olmalı.*

## Sahne 9: gorev (13 sn)

**Seslendirme:** Görevlerde ilk tablonu kurup satırlarını sayacak, gemilerin ortalama yükünü bulacak ve ağır gemileri listeleyeceksin. Projede de oyun skorlarını analiz edip kazananı seçiyorsun.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: İlk tablom
- Görev 2: Ortalama yük
- Görev 3: Ağır gemiler
- Challenge: En iyi oyuncu
- Proje: Skor analizi

**Maskot:** konusma pozu, sag

## Sahne 10: ozet (11 sn)

**Seslendirme:** Özetle: sözlükten ya da CSV'den tablo kur, koşulla süz, sırala, groupby ile özetle.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- pd.DataFrame ve pd.read_csv
- df[koşul], sort_values, tolist
- groupby ile toplama

**Maskot:** on pozu, sag

## Sahne 11: kapanis (13 sn)

**Seslendirme:** Bilgi Limanı'nı da bitirdik, muhteşemsin! Yarın son bölgeye, Python Dağı'na tırmanıyoruz. İlk durak: web'in istek ve yanıtla nasıl çalıştığı ve Python ile web sayfası üretmek. Görüşürüz!

**Ekranda başlık:** Yarın: Python ile web

**Ekranda maddeler:**

- Yeni bölge: Python Dağı
- İstek, yanıt, yönlendirme

**Maskot:** tebrik pozu, orta
