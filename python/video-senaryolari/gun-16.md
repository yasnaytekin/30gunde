# Video senaryosu: Gün 16, Tarih ve saat

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~157 sn

Piko, Keşif Adası'ndaki güneş saatinin önünde datetime modülünü anlatıyor: tarih oluşturmak, strftime ile biçimlendirmek ve tarihler arasında gün hesabı yapmak.

Ders metni: [gun-16.md](../gunler/gun-16.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 13 sn | mutlu (sag) |
| 2 | anlatim | 12 sn | isaret (sag) |
| 3 | anlatim | 9 sn | dusunme (sol) |
| 4 | kod | 14 sn | isaret (sag) |
| 5 | anlatim | 14 sn | konusma (sag) |
| 6 | kod | 14 sn | mutlu (sag) |
| 7 | kod | 14 sn | isaret (sol) |
| 8 | hata | 12 sn | sasirma (sag) |
| 9 | soru | 9 sn | dusunme (sag) |
| 10 | cikti | 10 sn | isaret (sol) |
| 11 | gorev | 13 sn | konusma (sag) |
| 12 | ozet | 11 sn | on (sag) |
| 13 | kapanis | 12 sn | tebrik (orta) |

## Sahne 1: acilis (13 sn)

**Seslendirme:** Selam, ben Piko! Keşif Adası'na ayak bastık. Adanın ortasında dev bir güneş saati var ve üstünde şöyle yazıyor: Zamanı okuyan, adanın sırrını çözer. Oyunlardaki günlük seriler nasıl sayılıyor dersin? Bugün Python'la zamanı okuyoruz!

**Ekranda başlık:** Gün 16: Tarih ve saat

**Ekranda maddeler:**

- Keşif Adası
- datetime modülü

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Arka plan: Keşif Adası bölge görseli (gorseller/python/harita/ada.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Güneş saatinin gölgesi yavaşça döner.*

## Sahne 2: anlatim (12 sn)

**Seslendirme:** Tarih ve saat için datetime modülünü kullanırız. Üç parçası işimizi görür: date bir tarih tutar, datetime tarih ve saati birlikte tutar, timedelta ise iki an arasındaki süredir.

**Ekranda başlık:** datetime modülü

**Kod** (vurgulanan satırlar: 1):

```python
from datetime import date, datetime, timedelta

today = date.today()      # bugünün tarihi
now = datetime.now()      # şu anki tarih ve saat
```

**Maskot:** isaret pozu, sag

## Sahne 3: anlatim (9 sn)

**Seslendirme:** Dikkat: date.today her gün başka sonuç verir. O yüzden örneklerde sabit tarihler kullanacağız, çıktılar hep aynı kalsın.

**Ekranda başlık:** Neden sabit tarih?

**Ekranda maddeler:**

- date.today() her gün değişir
- Örneklerde sabit tarih: date(2026, 9, 23)

**Maskot:** dusunme pozu, sol

## Sahne 4: kod (14 sn)

**Seslendirme:** Bir tarih oluşturmak için sırayla yıl, ay ve gün yazıyorum. Sonra year, month ve day ile tarihin parçalarını tek tek alıyorum. Son satırda strftime tarihi tanıdık biçimde yazıya çeviriyor.

**Ekranda başlık:** Tarihin parçaları

**Kod** (vurgulanan satırlar: 3, 7):

```python
from datetime import date

d = date(2026, 9, 23)
print("Yıl:", d.year)
print("Ay:", d.month)
print("Gün:", d.day)
print(d.strftime("%d.%m.%Y"))
```

**Çıktı:**

```text
Yıl: 2026
Ay: 9
Gün: 23
23.09.2026
```

**Maskot:** isaret pozu, sag

## Sahne 5: anlatim (14 sn)

**Seslendirme:** strftime içindeki yüzde işaretli harfler birer yer tutucu: yüzde d gün, yüzde m ay, büyük Y dört haneli yıl. Tersini strptime yapar: yazıyı okuyup ondan gerçek bir tarih üretir.

**Ekranda başlık:** Biçimlendirmek: strftime ve strptime

**Ekranda maddeler:**

- %d gün, %m ay, %Y yıl
- %H saat, %M dakika

**Kod** (vurgulanan satırlar: 3):

```python
from datetime import datetime

t = datetime.strptime("23.09.2026", "%d.%m.%Y")
print(t)
print(t.strftime("%d/%m/%Y"))
```

**Çıktı:**

```text
2026-09-23 00:00:00
23/09/2026
```

**Maskot:** konusma pozu, sag

## Sahne 6: kod (14 sn)

**Seslendirme:** Şimdi hesap zamanı. Yeni yıl tarihinden bugünü çıkarınca aradaki süreyi buluyorum. Sonundaki .days bu süreyi gün sayısına çeviriyor. Tam yüz gün varmış!

**Ekranda başlık:** Kaç gün kaldı?

**Kod** (vurgulanan satırlar: 5):

```python
from datetime import date

today = date(2026, 9, 23)
new_year = date(2027, 1, 1)
left = (new_year - today).days
print(f"Yeni yıla {left} gün var.")
```

**Çıktı:**

```text
Yeni yıla 100 gün var.
```

**Maskot:** mutlu pozu, sag

## Sahne 7: kod (14 sn)

**Seslendirme:** Bir tarihe gün eklemek için timedelta kullanıyorum. Döngü her turda yedi, on dört ve yirmi bir gün ekliyor. Ay bitince Python kendisi bir sonraki aya geçiyor.

**Ekranda başlık:** Bir hafta sonra

**Kod** (vurgulanan satırlar: 5):

```python
from datetime import date, timedelta

start = date(2026, 9, 23)
for week in range(1, 4):
    later = start + timedelta(days=7 * week)
    print(f"{week}. hafta:", later.strftime("%d.%m.%Y"))
```

**Çıktı:**

```text
1. hafta: 30.09.2026
2. hafta: 07.10.2026
3. hafta: 14.10.2026
```

**Maskot:** isaret pozu, sol

## Sahne 8: hata (12 sn)

**Seslendirme:** En sık hata, takvimde olmayan bir tarih yazmak. Şubat otuz diye bir gün yok! Python da ValueError verip, gün bu ay için aralık dışında diyor.

**Ekranda başlık:** Sık hata: olmayan tarih

**Kod** (vurgulanan satırlar: 3):

```python
from datetime import date

d = date(2026, 2, 30)
```

**Çıktı:**

```text
ValueError: day is out of range for month
```

**Maskot:** sasirma pozu, sag

## Sahne 9: soru (9 sn)

**Seslendirme:** Şimdi sıra sende. İki tarihi çıkarıyorum ama .days yazmayı unuttum. Sence bu kod ne yazdırır?

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```python
from datetime import date

print(date(2026, 9, 30) - date(2026, 9, 1))
```

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (10 sn)

**Seslendirme:** Sonuç bir sayı değil, bir süre nesnesi: yirmi dokuz gün ve sıfır saat. Sadece gün sayısı lazımsa sonuna .days eklemeyi unutma.

**Ekranda başlık:** Cevap

**Kod**:

```python
from datetime import date

print(date(2026, 9, 30) - date(2026, 9, 1))
```

**Çıktı:**

```text
29 days, 0:00:00
```

**Maskot:** isaret pozu, sol

## Sahne 11: gorev (13 sn)

**Seslendirme:** Görev zamanı! Önce bir tarihi gün, ay, yıl biçiminde yazdıracaksın. Sonra doğum gününe kaç gün kaldığını bulacaksın, en son da bir tarihe hafta ekleyeceksin. Projede de günlük seri sistemini kuruyorsun.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Tarihi biçimle
- Görev 2: Kaç gün kaldı?
- Görev 3: Bir hafta sonra
- Challenge: Haftanın günü
- Proje: Günlük seri

**Maskot:** konusma pozu, sag

## Sahne 12: ozet (11 sn)

**Seslendirme:** Kısaca: date ile tarih kur, strftime ile güzelce yaz, iki tarihi çıkarıp timedelta ile hesap yap.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- date(yıl, ay, gün) ile tarih oluştur
- strftime ile yazıya, strptime ile tarihe çevir
- Tarih farkı .days, gün eklemek timedelta

**Maskot:** on pozu, sag

## Sahne 13: kapanis (12 sn)

**Seslendirme:** Harikaydın! Yarın adanın çürük köprülerinden geçeceğiz. Program hata verince çökmek yerine ipe tutunmayı, yani try ve except ile hata yönetimini öğreneceğiz. Görüşürüz!

**Ekranda başlık:** Yarın: Hata yönetimi

**Ekranda maddeler:**

- try, except, else, finally
- raise ile kendi hatan

**Maskot:** tebrik pozu, orta
