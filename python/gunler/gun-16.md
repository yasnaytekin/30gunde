# Gün 16: Tarih ve saat

**Kurs:** 30 Günde Python  ·  **Bölge:** Keşif Adası  ·  **Maskot:** Piko

**Bugünün hedefi:** datetime modülüyle tarih oluşturmak, biçimlendirmek ve tarihler arasında hesap yapmak

> Keşif Adası'na ayak bastık! Adanın ortasında dev bir güneş saati var ve üzerinde bir yazı: "Zamanı okuyan, adanın sırrını çözer." Oyunlardaki günlük ödüller, seriler ve geri sayımlar hep tarih hesabıyla çalışır. Bugün Python'la zamanı okuyoruz.

![Keşif Adası](../../gorseller/python/harita/ada.webp)

## Konu anlatımı

### datetime modülü

Tarih ve saat için `datetime` modülünü kullanırız. En çok üç parçasını kullanacağız:

```python
from datetime import date, datetime, timedelta

today = date.today()      # bugünün tarihi
now = datetime.now()      # şu anki tarih ve saat
```

`date.today()` her gün farklı sonuç verir. Bu yüzden görevlerde sabit tarihlerle çalışacağız.

### Tarih oluşturmak

```python
birthday = date(2014, 5, 19)   # yıl, ay, gün
print(birthday.year)    # 2014
print(birthday.month)   # 5
print(birthday.day)     # 19
print(birthday.weekday())  # 0 pazartesi ... 6 pazar
```

Saat de lazımsa `datetime(2026, 9, 23, 14, 30)` yazılır: 14.30.

### Biçimlendirmek

`strftime` tarihi istediğin biçimde yazıya çevirir:

- `%d` gün, `%m` ay, `%Y` dört haneli yıl
- `%H` saat, `%M` dakika

```python
d = date(2026, 9, 23)
print(d.strftime("%d.%m.%Y"))   # 23.09.2026
```

Tersini `datetime.strptime("23.09.2026", "%d.%m.%Y")` yapar: yazıdan tarih üretir.

### Tarihlerle hesap

İki tarihi çıkarırsan aradaki süreyi verir. `.days` ile gün sayısını alırsın:

```python
start = date(2026, 9, 1)
end = date(2026, 9, 30)
print((end - start).days)   # 29
```

Bir tarihe gün eklemek için `timedelta` kullanılır:

```python
print(start + timedelta(days=7))   # bir hafta sonrası
```

## Örnekler

### Tarihin parçaları

```python
from datetime import date

d = date(2026, 9, 23)
print("Yıl:", d.year)
print("Ay:", d.month)
print("Gün:", d.day)
print(d.strftime("%d.%m.%Y"))
```

### Kaç gün kaldı?

```python
from datetime import date

today = date(2026, 9, 23)
new_year = date(2027, 1, 1)
left = (new_year - today).days
print(f"Yeni yıla {left} gün var.")
```

### Bir hafta sonra

```python
from datetime import date, timedelta

start = date(2026, 9, 23)
for week in range(1, 4):
    print(f"{week}. hafta:", (start + timedelta(days=7 * week)).strftime("%d.%m.%Y"))
```

## Görevler

### Görev 1: Tarihi biçimle

`year`, `month` ve `day` ile bir tarih oluştur ve `23.09.2026` biçiminde yazdır.

**Başlangıç kodu:**

```python
from datetime import date

year = 2026
month = 9
day = 23

# Tarihi oluştur ve gün.ay.yıl biçiminde yazdır
```

**İpuçları:**

1. d = date(year, month, day)
2. Biçim: d.strftime("%d.%m.%Y")

<details><summary>Çözüm</summary>

```python
from datetime import date

year = 2026
month = 9
day = 23

d = date(year, month, day)
print(d.strftime("%d.%m.%Y"))
```

</details>

### Görev 2: Kaç gün kaldı?

`today` ile doğum günü (`birthday`) arasında kaç gün olduğunu `days_left` değişkenine koy ve `Doğum gününe 12 gün var.` gibi yazdır.

**Başlangıç kodu:**

```python
from datetime import date

today = date(2026, 9, 23)
birthday_day = 5
birthday = date(2026, 10, birthday_day)

days_left = 0

print(f"Doğum gününe {days_left} gün var.")
```

**İpuçları:**

1. İki tarihi çıkar: birthday - today
2. Gün sayısı için sonuna .days ekle.

<details><summary>Çözüm</summary>

```python
from datetime import date

today = date(2026, 9, 23)
birthday_day = 5
birthday = date(2026, 10, birthday_day)

days_left = (birthday - today).days

print(f"Doğum gününe {days_left} gün var.")
```

</details>

### Görev 3: Bir hafta sonra

`start` tarihine `weeks` hafta ekle ve sonucu `gün.ay.yıl` biçiminde yazdır.

**Başlangıç kodu:**

```python
from datetime import date, timedelta

start = date(2026, 9, 23)
weeks = 1

# start + weeks hafta
```

**İpuçları:**

1. timedelta(weeks=weeks) ya da timedelta(days=7 * weeks)
2. Biçim için strftime("%d.%m.%Y")

<details><summary>Çözüm</summary>

```python
from datetime import date, timedelta

start = date(2026, 9, 23)
weeks = 1

later = start + timedelta(weeks=weeks)
print(later.strftime("%d.%m.%Y"))
```

</details>

## Challenge: Haftanın günü

`weekday()` 0 (pazartesi) ile 6 (pazar) arasında sayı verir. Bu sayıyı `names` listesinde kullanarak tarihin hangi gün olduğunu yazdır: `23.09.2026 Çarşamba`

**Başlangıç kodu:**

```python
from datetime import date

names = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
year, month, day = 2026, 9, 23
d = date(year, month, day)

# Tarihi ve gün adını yazdır
```

**İpuçları:**

1. Gün adı: names[d.weekday()]

<details><summary>Çözüm</summary>

```python
from datetime import date

names = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
year, month, day = 2026, 9, 23
d = date(year, month, day)

print(d.strftime("%d.%m.%Y"), names[d.weekday()])
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Günlük seri**

### Piko'nun Macerası: Günlük seri

Oyunlarda her gün girersen serin büyür. `last_play` son oynanan gün, `today` bugün.

- Aradaki fark 0 günse: `Bugün zaten oynadın.`
- 1 günse: `Seri devam ediyor!`
- Daha fazlaysa: `Seri bozuldu, yeniden başla!`

**Başlangıç kodu:**

```python
from datetime import date

today = date(2026, 9, 23)
last_day = 22
last_play = date(2026, 9, last_day)

# Farkı hesapla ve mesajı yazdır
```

**İpuçları:**

1. gap = (today - last_play).days
2. if gap == 0 ... elif gap == 1 ... else

<details><summary>Çözüm</summary>

```python
from datetime import date

today = date(2026, 9, 23)
last_day = 22
last_play = date(2026, 9, last_day)

gap = (today - last_play).days
if gap == 0:
    print("Bugün zaten oynadın.")
elif gap == 1:
    print("Seri devam ediyor!")
else:
    print("Seri bozuldu, yeniden başla!")
```

</details>

### Harcama Defteri: Kira hatırlatıcı

Kira her ay ödeniyor. Bugün `today`, bir sonraki ödeme günü `due` (Ekim'in `due_day`'inci günü).

- `days_left`: iki tarih arasındaki gün farkı (`(due - today).days`)
- 0'dan büyükse: `Kiraya 7 gün kaldı` gibi yazdır.
- 0 ise: `Kira bugün!`
- 0'dan küçükse: `Kira gecikti!`

**Başlangıç kodu:**

```python
from datetime import date

today = date(2026, 9, 24)
due_day = 1
due = date(2026, 10, due_day)
```

**İpuçları:**

1. İki tarihi çıkarınca timedelta çıkar; .days gün sayısını verir.
2. days_left > 0, == 0 ve kalan durum için if / elif / else.

<details><summary>Çözüm</summary>

```python
from datetime import date

today = date(2026, 9, 24)
due_day = 1
due = date(2026, 10, due_day)
days_left = (due - today).days
if days_left > 0:
    print(f"Kiraya {days_left} gün kaldı")
elif days_left == 0:
    print("Kira bugün!")
else:
    print("Kira gecikti!")
```

</details>

### Görev Asistanı: Toplantı hatırlatıcı

Toplantı `start` zamanında başlıyor. Asistan `minutes_before` dakika önce hatırlatsın.

- `reminder`: `start - timedelta(minutes=minutes_before)`
- `Hatırlatma: 13:45` biçiminde yazdır (`strftime("%H:%M")`).
- `Toplantı: 24.09.2026 14:00` biçiminde de yazdır (`%d.%m.%Y %H:%M`).

**Başlangıç kodu:**

```python
from datetime import datetime, timedelta

start = datetime(2026, 9, 24, 14, 0)
minutes_before = 15
```

**İpuçları:**

1. timedelta(minutes=15) 15 dakikalık bir süre.
2. reminder.strftime("%H:%M") saati 13:45 biçiminde verir.

<details><summary>Çözüm</summary>

```python
from datetime import datetime, timedelta

start = datetime(2026, 9, 24, 14, 0)
minutes_before = 15
reminder = start - timedelta(minutes=minutes_before)
print("Hatırlatma:", reminder.strftime("%H:%M"))
print("Toplantı:", start.strftime("%d.%m.%Y %H:%M"))
```

</details>

### Kişisel Web Sitem: Yayın tarihi

Her yazının altında yayın tarihi görünsün.

- `pretty`: `published` tarihini `01.09.2026` biçiminde yazıya çevir (`strftime("%d.%m.%Y")`)
- `days_ago`: yayından bu yana geçen gün (`(today - published).days`)
- `Yayın tarihi: 01.09.2026` yazdır.
- `days_ago` 7 veya daha azsa `Yeni yazı!`, değilse `23 gün önce yayınlandı` gibi yazdır.

**Başlangıç kodu:**

```python
from datetime import date

today = date(2026, 9, 24)
published = date(2026, 9, 1)
```

**İpuçları:**

1. published.strftime("%d.%m.%Y") gün.ay.yıl biçiminde yazı verir.
2. İki tarihi çıkarınca timedelta çıkar; .days gün sayısını verir.

<details><summary>Çözüm</summary>

```python
from datetime import date

today = date(2026, 9, 24)
published = date(2026, 9, 1)
pretty = published.strftime("%d.%m.%Y")
days_ago = (today - published).days
print(f"Yayın tarihi: {pretty}")
if days_ago <= 7:
    print("Yeni yazı!")
else:
    print(f"{days_ago} gün önce yayınlandı")
```

</details>

### Sohbet Botu: Saate göre selam

Bot saati bilsin! Şu an `now`, seninle en son konuştuğu an `last_seen`.

- `hour`: şu anki saat (`now.hour` saati sayı olarak verir)
- Saat 12'den küçükse `Günaydın!`, 18'den küçükse `İyi günler!`, değilse `İyi akşamlar!` selamını seç ve yanına saati ekleyerek yazdır: `Günaydın! Saat 09:30.` (`strftime("%H:%M")`)
- `days_away`: iki an arasındaki gün farkı (`(now - last_seen).days`)
- `days_away` 1 veya daha fazlaysa `Seni 2 gündür görmedim!` gibi yazdır.

**Başlangıç kodu:**

```python
import datetime

now = datetime.datetime(2026, 9, 24, 9, 30)
last_seen = datetime.datetime(2026, 9, 21, 20, 0)
```

**İpuçları:**

1. now.strftime("%H:%M") saati 09:30 biçiminde verir.
2. İki zamanı çıkarınca timedelta çıkar; .days gün sayısını verir.

<details><summary>Çözüm</summary>

```python
import datetime

now = datetime.datetime(2026, 9, 24, 9, 30)
last_seen = datetime.datetime(2026, 9, 21, 20, 0)
hour = now.hour
if hour < 12:
    greeting = "Günaydın!"
elif hour < 18:
    greeting = "İyi günler!"
else:
    greeting = "İyi akşamlar!"
print(f"{greeting} Saat {now.strftime('%H:%M')}.")
days_away = (now - last_seen).days
if days_away >= 1:
    print(f"Seni {days_away} gündür görmedim!")
```

</details>

### Okul Not Defteri: Sınav geri sayımı

Bugün `today`, sınav günü `exam`.

- `days_left`: iki tarih arasındaki gün farkı (`(exam - today).days`)
- Önce sınav tarihini `Sınav tarihi: 05.10.2026` biçiminde yazdır (`strftime("%d.%m.%Y")`).
- Sonra:
  - 7'den fazla gün varsa: `Sınava 11 gün var`
  - 1 ile 7 gün arasıysa: `Sınav yaklaşıyor: 3 gün kaldı!`
  - 0 ise: `Sınav bugün, başarılar!`
  - 0'dan küçükse: `Sınav geçti.`

**Başlangıç kodu:**

```python
from datetime import date

today = date(2026, 9, 24)
exam = date(2026, 10, 5)
```

**İpuçları:**

1. İki tarihi çıkarınca timedelta çıkar; .days gün sayısını verir.
2. Sıra önemli: önce > 7, sonra > 0, sonra == 0, en son else.

<details><summary>Çözüm</summary>

```python
from datetime import date

today = date(2026, 9, 24)
exam = date(2026, 10, 5)
days_left = (exam - today).days
print("Sınav tarihi:", exam.strftime("%d.%m.%Y"))
if days_left > 7:
    print(f"Sınava {days_left} gün var")
elif days_left > 0:
    print(f"Sınav yaklaşıyor: {days_left} gün kaldı!")
elif days_left == 0:
    print("Sınav bugün, başarılar!")
else:
    print("Sınav geçti.")
```

</details>
