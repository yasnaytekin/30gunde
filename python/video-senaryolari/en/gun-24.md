# Video senaryosu: Gün 24, Statistics and NumPy

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~144 sn

In the records office of Knowledge Harbor, Piko explains mean, median and mode with the statistics module, and whole-array math and filtering with NumPy arrays.

Ders metni: [gun-24.md](../../gunler/gun-24.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 15 sn | dusunme (sag) |
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

## Giriş (konu tanıtımı)

**Seslendirme:** Day 24: Statistics and NumPy! In this lesson you'll calculate the mean, median and mode, and work with whole arrays and filters in NumPy.

- mean, median, mode
- NumPy arrays
- Filtering with conditions

## Sahne 1: acilis (15 sn)

**Seslendirme:** Hi, I'm Piko! In the records office of Knowledge Harbor, the arrival times of hundreds of ships are written down. The harbor master asks: on average, how many hours do ships take to arrive, and which time shows up most often? Today we make numbers talk with Python!

**Ekranda başlık:** Day 24: Statistics and NumPy

**Ekranda maddeler:**

- Knowledge Harbor
- statistics and NumPy

**Maskot:** dusunme pozu, sag

## Sahne 2: anlatim (17 sn)

**Seslendirme:** There are four basic measures. The mean: add them all up and divide by how many there are. The median: the value right in the middle when you sort them. The mode: the most common value. And the standard deviation tells you how far the numbers spread from the mean.

**Ekranda başlık:** The basic measures

**Ekranda maddeler:**

- Mean
- Median
- Mode
- Standard deviation (stdev)

**Maskot:** isaret pozu, sol

## Sahne 3: kod (16 sn)

**Seslendirme:** The statistics module comes with Python and calculates these measures for you. Look, one late ship taking twelve hours pulled the mean up to six, but the median stayed at five. The median isn't bothered much by extreme values.

**Ekranda başlık:** Arrival times: statistics

**Kod** (vurgulanan satırlar: 4, 5, 6):

```python
import statistics

times = [3, 5, 5, 6, 12]
print("Mean:", statistics.mean(times))
print("Median:", statistics.median(times))
print("Most common:", statistics.mode(times))
print("Spread:", round(statistics.stdev(times), 2))
```

**Çıktı:**

```text
Mean: 6.2
Median: 5
Most common: 5
Spread: 3.42
```

**Maskot:** isaret pozu, sag

## Sahne 4: anlatim (11 sn)

**Seslendirme:** NumPy is scientists' favorite package. Its array looks like a list, but it applies an operation to every item at once.

**Ekranda başlık:** NumPy arrays

**Ekranda maddeler:**

- import numpy as np
- np.array([10, 20, 30])
- Operations apply to every item at once

**Maskot:** konusma pozu, sag

## Sahne 5: soru (10 sn)

**Seslendirme:** I multiply the same list by two once as it is, and once as a NumPy array. What do you think we'll see on the two lines?

**Ekranda başlık:** What will it print?

**Kod**:

```python
import numpy as np

nums = [10, 20, 30]
print("List * 2:", nums * 2)
print("Array * 2:", np.array(nums) * 2)
```

**Maskot:** dusunme pozu, sag

## Sahne 6: cikti (12 sn)

**Seslendirme:** Same operation, very different results! The list got stuck onto itself twice. The array doubled every item. Also notice the array is printed without commas.

**Ekranda başlık:** The answer: list or array?

**Kod**:

```python
import numpy as np

nums = [10, 20, 30]
print("List * 2:", nums * 2)
print("Array * 2:", np.array(nums) * 2)
```

**Çıktı:**

```text
List * 2: [10, 20, 30, 10, 20, 30]
Array * 2: [20 40 60]
```

**Maskot:** sasirma pozu, sol

## Sahne 7: kod (16 sn)

**Seslendirme:** With arrays, you can pick items by writing a condition inside the square brackets. The ones fifty and above get through. Add up the condition's result with sum, and you find how many people passed. And mean gives the average.

**Ekranda başlık:** Picking with a condition

**Kod** (vurgulanan satırlar: 4, 5):

```python
import numpy as np

scores = np.array([45, 90, 12, 77, 60])
print("Passed:", scores[scores >= 50])
print("How many:", (scores >= 50).sum())
print("Average:", scores.mean())
```

**Çıktı:**

```text
Passed: [90 77 60]
How many: 3
Average: 56.8
```

**Maskot:** isaret pozu, sag

## Sahne 8: hata (11 sn)

**Seslendirme:** A common mistake: asking for the average of an empty list. If there are no numbers, there's no average either, and Python gives a StatisticsError. Before calculating, check that the list isn't empty.

**Ekranda başlık:** Common mistake: an empty list

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

**Seslendirme:** In the tasks you'll calculate the mean and the median, find the most common dice roll, and double scores without a loop. In the project you're summarizing how long the players played.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Mean and median
- Task 2: The most common roll
- Task 3: Double it with NumPy
- Challenge: How many passed?
- Project: Game statistics

**Maskot:** konusma pozu, sag

## Sahne 10: ozet (11 sn)

**Seslendirme:** In short: calculate measures with statistics, do math on a whole array at once with NumPy, and filter with conditions.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- mean, median, mode, stdev
- np.array: operations apply to every item
- Pick with array[condition]

**Maskot:** on pozu, sag

## Sahne 11: kapanis (12 sn)

**Seslendirme:** The numbers talked, you're amazing! Tomorrow we'll line these numbers up in tables. We'll learn to filter and summarize rows and columns with pandas. See you!

**Ekranda başlık:** Tomorrow: Pandas

**Ekranda maddeler:**

- DataFrame
- Filter and summarize

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
