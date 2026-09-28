# Video senaryosu: Gün 16, Dates and times

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~159 sn

In front of the sundial on Discovery Island, Piko explains the datetime module: creating dates, formatting them with strftime, and counting days between dates.

Ders metni: [gun-16.md](../../gunler/gun-16.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 15 sn | mutlu (sag) |
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

## Giriş (konu tanıtımı)

**Seslendirme:** Day 16: Dates and times! In this lesson you'll create dates with the datetime module, format them, and count the days between dates.

- date and datetime
- Formatting with strftime
- Counting days with timedelta

## Sahne 1: acilis (15 sn)

**Seslendirme:** Hi, I'm Piko! We've set foot on Discovery Island. In the middle of the island there's a giant sundial, and on it is written: whoever reads the time solves the island's secret. How do you think daily streaks in games are counted? Today we read time with Python!

**Ekranda başlık:** Day 16: Dates and times

**Ekranda maddeler:**

- Discovery Island
- The datetime module

**Maskot:** mutlu pozu, sag

## Sahne 2: anlatim (12 sn)

**Seslendirme:** For dates and times we use the datetime module. Three parts do the job: date holds a date, datetime holds a date and a time together, and timedelta is the length of time between two moments.

**Ekranda başlık:** The datetime module

**Kod** (vurgulanan satırlar: 1):

```python
from datetime import date, datetime, timedelta

today = date.today()      # today's date
now = datetime.now()      # the current date and time
```

**Maskot:** isaret pozu, sag

## Sahne 3: anlatim (9 sn)

**Seslendirme:** Careful: date.today gives a different result every day. So in the examples we'll use fixed dates, and the outputs will always stay the same.

**Ekranda başlık:** Why a fixed date?

**Ekranda maddeler:**

- date.today() changes every day
- Fixed date in the examples: date(2026, 9, 23)

**Maskot:** dusunme pozu, sol

## Sahne 4: kod (14 sn)

**Seslendirme:** To make a date, I write the year, the month and the day, in that order. Then I take its parts one by one with year, month and day. On the last line, strftime turns the date into familiar-looking text.

**Ekranda başlık:** The parts of a date

**Kod** (vurgulanan satırlar: 3, 7):

```python
from datetime import date

d = date(2026, 9, 23)
print("Year:", d.year)
print("Month:", d.month)
print("Day:", d.day)
print(d.strftime("%d.%m.%Y"))
```

**Çıktı:**

```text
Year: 2026
Month: 9
Day: 23
23.09.2026
```

**Maskot:** isaret pozu, sag

## Sahne 5: anlatim (14 sn)

**Seslendirme:** The letters with percent signs inside strftime are placeholders: percent d is the day, percent m the month, and capital Y the four-digit year. strptime does the opposite: it reads text and makes a real date out of it.

**Ekranda başlık:** Formatting: strftime and strptime

**Ekranda maddeler:**

- %d day, %m month, %Y year
- %H hour, %M minute

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

**Seslendirme:** Now it's time to count. When I subtract today from New Year's Day, I get the time in between. The .days at the end turns that into a number of days. Exactly one hundred days!

**Ekranda başlık:** How many days are left?

**Kod** (vurgulanan satırlar: 5):

```python
from datetime import date

today = date(2026, 9, 23)
new_year = date(2027, 1, 1)
left = (new_year - today).days
print(f"{left} days until the new year.")
```

**Çıktı:**

```text
100 days until the new year.
```

**Maskot:** mutlu pozu, sag

## Sahne 7: kod (14 sn)

**Seslendirme:** To add days to a date, I use timedelta. Each round, the loop adds seven, fourteen and twenty-one days. When the month runs out, Python moves on to the next month by itself.

**Ekranda başlık:** A week later

**Kod** (vurgulanan satırlar: 5):

```python
from datetime import date, timedelta

start = date(2026, 9, 23)
for week in range(1, 4):
    later = start + timedelta(days=7 * week)
    print(f"Week {week}:", later.strftime("%d.%m.%Y"))
```

**Çıktı:**

```text
Week 1: 30.09.2026
Week 2: 07.10.2026
Week 3: 14.10.2026
```

**Maskot:** isaret pozu, sol

## Sahne 8: hata (12 sn)

**Seslendirme:** The most common mistake is writing a date that isn't on the calendar. There's no February thirtieth! Python gives a ValueError and says the day is out of range for the month.

**Ekranda başlık:** Common mistake: a date that doesn't exist

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

**Seslendirme:** Now it's your turn. I'm subtracting two dates, but I forgot to write .days. What do you think this code prints?

**Ekranda başlık:** What will it print?

**Kod**:

```python
from datetime import date

print(date(2026, 9, 30) - date(2026, 9, 1))
```

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (10 sn)

**Seslendirme:** The result isn't a number, it's a length of time: twenty-nine days and zero hours. If you only need the number of days, don't forget to add .days at the end.

**Ekranda başlık:** The answer

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

**Seslendirme:** Task time! First you'll print a date as day, month and year. Then you'll find how many days are left until your birthday, and finally you'll add weeks to a date. In the project, you're building the daily streak system.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Format a date
- Task 2: How many days left?
- Task 3: A week later
- Challenge: Day of the week
- Project: Daily streak

**Maskot:** konusma pozu, sag

## Sahne 12: ozet (11 sn)

**Seslendirme:** In short: build a date with date, write it nicely with strftime, and subtract two dates to do math with timedelta.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- Make a date with date(year, month, day)
- Turn it into text with strftime, back into a date with strptime
- Date difference with .days, add days with timedelta

**Maskot:** on pozu, sag

## Sahne 13: kapanis (12 sn)

**Seslendirme:** You were great! Tomorrow we'll cross the island's rotten bridges. Instead of crashing when something goes wrong, our program will learn to hold on to the rope: error handling with try and except. See you!

**Ekranda başlık:** Tomorrow: Error handling

**Ekranda maddeler:**

- try, except, else, finally
- Your own errors with raise

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
