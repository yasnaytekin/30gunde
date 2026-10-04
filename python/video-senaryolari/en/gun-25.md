# Video senaryosu: Gün 25, Pandas

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~145 sn

Starting from the harbor master's giant logbook, Piko explains building tables with pandas, filtering, sorting, and summarizing CSV data with groups.

Ders metni: [gun-25.md](../../gunler/gun-25.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 16 sn | mutlu (sag) |
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

## Giriş (konu tanıtımı)

**Seslendirme:** Day 25: Pandas! In this lesson you'll build tables with pandas, filter and sort them, and summarize CSV data with groupby.

- DataFrame: your first table
- Filter and sort
- CSV and groupby

## Sahne 1: acilis (16 sn)

**Seslendirme:** Hi, I'm Piko! There's a giant logbook on the harbor master's desk: a ship on every row, a piece of information in every column. Instead of reading it row by row, the harbor master wants to ask who carries the most cargo and get an answer right away. Today we meet pandas!

**Ekranda başlık:** Day 25: Pandas

**Ekranda maddeler:**

- Knowledge Harbor
- Table data: the DataFrame

**Maskot:** mutlu pozu, sag

## Sahne 2: kod (16 sn)

**Seslendirme:** The heart of pandas is a table called a DataFrame. I build it from a dictionary: the keys become the column names, and the lists become the column values. The zero, one, two on the left are the row numbers. shape gives the number of rows and columns.

**Ekranda başlık:** Your first table: DataFrame

**Kod** (vurgulanan satırlar: 4, 6):

```python
import pandas as pd

data = {"name": ["Piko", "Ece", "Can"], "score": [300, 250, 120]}
df = pd.DataFrame(data)
print(df)
print("Size:", df.shape)
print("Average score:", df["score"].mean())
```

**Çıktı:**

```text
   name  score
0  Piko    300
1   Ece    250
2   Can    120
Size: (3, 2)
Average score: 223.33333333333334
```

**Maskot:** isaret pozu, sag

## Sahne 3: anlatim (13 sn)

**Seslendirme:** There are a few shortcuts for getting to know a table. You take a single column with square brackets; that's called a Series. A Series has ready-made methods like mean, max and sum.

**Ekranda başlık:** Getting to know the table

**Ekranda maddeler:**

- df.head(): the first 5 rows
- df.shape, df.columns
- df.describe(): a numeric summary
- df["score"]: one column (a Series)

**Maskot:** konusma pozu, sol

## Sahne 4: kod (14 sn)

**Seslendirme:** To filter, I write a condition inside the table. The rows with a score of two hundred fifty or more stay. Notice the row numbers are kept: row two, which was Can's, dropped out.

**Ekranda başlık:** Filter

**Kod** (vurgulanan satırlar: 5):

```python
import pandas as pd

df = pd.DataFrame({"name": ["Piko", "Ece", "Can", "Ada"],
                   "score": [300, 250, 120, 280]})
print(df[df["score"] >= 250])
```

**Çıktı:**

```text
   name  score
0  Piko    300
1   Ece    250
3   Ada    280
```

**Maskot:** isaret pozu, sag

## Sahne 5: soru (10 sn)

**Seslendirme:** Now it's your turn! I sort the table by score from biggest to smallest and turn the names into a list. What order do you think the list will be in?

**Ekranda başlık:** What will it print?

**Kod** (vurgulanan satırlar: 5):

```python
import pandas as pd

df = pd.DataFrame({"name": ["Piko", "Ece", "Can", "Ada"],
                   "score": [300, 250, 120, 280]})
top = df.sort_values("score", ascending=False)
print(top["name"].tolist())
```

**Maskot:** dusunme pozu, sag

## Sahne 6: cikti (10 sn)

**Seslendirme:** Piko is on top, then Ada, Ece and Can. ascending False means biggest to smallest, and tolist turns the column into a plain list.

**Ekranda başlık:** The answer

**Kod**:

```python
import pandas as pd

df = pd.DataFrame({"name": ["Piko", "Ece", "Can", "Ada"],
                   "score": [300, 250, 120, 280]})
top = df.sort_values("score", ascending=False)
print(top["name"].tolist())
```

**Çıktı:**

```text
['Piko', 'Ada', 'Ece', 'Can']
```

**Maskot:** mutlu pozu, sol

## Sahne 7: kod (17 sn)

**Seslendirme:** Real data usually comes in a CSV file, as lines separated by commas. read_csv turns it into a table; here I read the text like a file with StringIO. groupby adds up each player's scores, and idxmax finds the winner.

**Ekranda başlık:** CSV and grouping

**Kod** (vurgulanan satırlar: 5, 6, 8):

```python
import io
import pandas as pd

csv = "player,score\nPiko,50\nEce,70\nPiko,40\nEce,10\n"
df = pd.read_csv(io.StringIO(csv))
totals = df.groupby("player")["score"].sum()
print(totals)
print("Winner:", totals.idxmax())
```

**Çıktı:**

```text
player
Ece     80
Piko    90
Name: score, dtype: int64
Winner: Piko
```

**Maskot:** isaret pozu, sag

## Sahne 8: hata (12 sn)

**Seslendirme:** A common mistake: writing a column name wrong. The table has name, but I asked for username. When pandas can't find the column, it gives a KeyError. If you're not sure, look at the names with df.columns.

**Ekranda başlık:** Common mistake: a column that doesn't exist

**Kod** (vurgulanan satırlar: 4):

```python
import pandas as pd

df = pd.DataFrame({"name": ["Piko"], "score": [300]})
print(df["username"])
```

**Çıktı:**

```text
KeyError: 'username'
```

**Maskot:** sasirma pozu, sol

## Sahne 9: gorev (13 sn)

**Seslendirme:** In the tasks you'll build your first table and count its rows, find the ships' average cargo, and list the heavy ships. In the project you're analyzing game scores and picking the winner.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: My first table
- Task 2: Average cargo
- Task 3: Heavy ships
- Challenge: The best player
- Project: Score analysis

**Maskot:** konusma pozu, sag

## Sahne 10: ozet (11 sn)

**Seslendirme:** In short: build a table from a dictionary or a CSV, filter it with conditions, sort it, and summarize it with groupby.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- pd.DataFrame and pd.read_csv
- df[condition], sort_values, tolist
- Adding up with groupby

**Maskot:** on pozu, sag

## Sahne 11: kapanis (13 sn)

**Seslendirme:** We've finished Knowledge Harbor too, you're fantastic! Tomorrow we climb the last region, Python Mountain. First stop: how the web works with requests and responses, and making web pages with Python. See you!

**Ekranda başlık:** Tomorrow: The web with Python

**Ekranda maddeler:**

- New region: Python Mountain
- Requests, responses, routing

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
