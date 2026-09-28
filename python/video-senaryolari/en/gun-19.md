# Video senaryosu: Gün 19, Working with files

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~155 sn

Starting from a captain's logbook found in the lighthouse of Discovery Island, Piko explains writing to files, reading from files, and saving the game with JSON.

Ders metni: [gun-19.md](../../gunler/gun-19.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | mutlu (sag) |
| 2 | anlatim | 15 sn | isaret (sol) |
| 3 | kod | 16 sn | isaret (sag) |
| 4 | kod | 16 sn | isaret (sol) |
| 5 | kod | 17 sn | konusma (sag) |
| 6 | anlatim | 10 sn | dusunme (sag) |
| 7 | hata | 11 sn | sasirma (sol) |
| 8 | soru | 10 sn | dusunme (sag) |
| 9 | cikti | 10 sn | uzgun (sol) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 12 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 19: Working with files! In this lesson you'll write to files, read from them, and save your game with JSON.

- open and file modes
- Write, read, append
- Saving with JSON

## Sahne 1: acilis (14 sn)

**Seslendirme:** Hi, I'm Piko! In the lighthouse of Discovery Island we found an old captain's logbook. The captain wrote down what happened every evening, and years later we can still read it. Programs have a notebook like that too: files. Today we learn to save our game!

**Ekranda başlık:** Day 19: Working with files

**Ekranda maddeler:**

- Discovery Island
- Write, read, save with JSON

**Maskot:** mutlu pozu, sag

## Sahne 2: anlatim (15 sn)

**Seslendirme:** The open function opens a file. The second piece of information is the mode: r for reading, and a for append, which adds to the end. w is for writing, but careful, if the file exists, it wipes it! And with closes the file for us when we're done.

**Ekranda başlık:** Opening a file: open and modes

**Ekranda maddeler:**

- "r" read (the default)
- "w" write: wipes the file if it exists
- "a" add to the end
- with closes the file automatically

**Maskot:** isaret pozu, sol

## Sahne 3: kod (16 sn)

**Seslendirme:** First I write two lines in w mode. The backslash n at the end of each line means a new line, because write doesn't move to the next line by itself. Then I open the file and read it all with read.

**Ekranda başlık:** Write and read

**Kod** (vurgulanan satırlar: 1, 5):

```python
with open("diary.txt", "w") as f:
    f.write("Day 1: We reached camp\n")
    f.write("Day 2: We explored the village\n")

with open("diary.txt") as f:
    print(f.read())
```

**Çıktı:**

```text
Day 1: We reached camp
Day 2: We explored the village
```

**Maskot:** isaret pozu, sag

## Sahne 4: kod (16 sn)

**Seslendirme:** When you open a file in append mode, the old lines aren't wiped; the new one goes at the end. When reading, I go through the file line by line. strip cleans the extra bit at the end of each line, and enumerate gives the numbers.

**Ekranda başlık:** Add to the end

**Kod** (vurgulanan satırlar: 4, 8):

```python
with open("list.txt", "w") as f:
    f.write("sword\n")

with open("list.txt", "a") as f:
    f.write("potion\n")

with open("list.txt") as f:
    for i, line in enumerate(f, 1):
        print(i, line.strip())
```

**Çıktı:**

```text
1 sword
2 potion
```

**Maskot:** isaret pozu, sol

## Sahne 5: kod (17 sn)

**Seslendirme:** The easiest way to save dictionaries and lists is JSON. json.dump writes the dictionary to a file, and json.load reads it back as a dictionary. You can also check whether a file exists with os.path.exists.

**Ekranda başlık:** Saving with JSON

**Kod** (vurgulanan satırlar: 5, 9):

```python
import json, os

hero = {"name": "Piko", "hp": 80, "bag": ["map"]}
with open("save.json", "w") as f:
    json.dump(hero, f)

print("Does the file exist?", os.path.exists("save.json"))
with open("save.json") as f:
    print(json.load(f))
```

**Çıktı:**

```text
Does the file exist? True
{'name': 'Piko', 'hp': 80, 'bag': ['map']}
```

**Maskot:** konusma pozu, sag

## Sahne 6: anlatim (10 sn)

**Seslendirme:** On our site, the files you write only live during that run. On your own computer, they're written to disk and stay even after the program closes.

**Ekranda başlık:** Files on our site

**Ekranda maddeler:**

- On the site: only during that run
- On your computer: permanent
- In the tasks, write first, then read in the same code

**Maskot:** dusunme pozu, sag

## Sahne 7: hata (11 sn)

**Seslendirme:** A common mistake: trying to read a file that doesn't exist. Python gives a FileNotFoundError. Check the file name, or look first with os.path.exists.

**Ekranda başlık:** Common mistake: no such file

**Kod** (vurgulanan satırlar: 1):

```python
with open("lost-map.txt") as f:
    print(f.read())
```

**Çıktı:**

```text
FileNotFoundError: [Errno 2] No such file or directory: 'lost-map.txt'
```

**Maskot:** sasirma pozu, sol

## Sahne 8: soru (10 sn)

**Seslendirme:** Mini question! I open the same file twice in w mode, writing sword first and then potion. What do you think is in the file at the end?

**Ekranda başlık:** What will it print?

**Kod**:

```python
with open("bag.txt", "w") as f:
    f.write("sword\n")

with open("bag.txt", "w") as f:
    f.write("potion\n")

with open("bag.txt") as f:
    print(f.read())
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (10 sn)

**Seslendirme:** Only potion! w mode resets the file every time it opens, so the sword was wiped. If you want both to stay, open it the second time in append mode.

**Ekranda başlık:** The answer

**Kod**:

```python
with open("bag.txt", "w") as f:
    f.write("sword\n")

with open("bag.txt", "w") as f:
    f.write("potion\n")

with open("bag.txt") as f:
    print(f.read())
```

**Çıktı:**

```text
potion
```

**Maskot:** uzgun pozu, sol

## Sahne 10: gorev (13 sn)

**Seslendirme:** In the tasks you'll write a diary and read it, write the items in your bag to a file and count the lines, and add a score to the end. In the project you're saving the game with JSON and loading it back.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Write a diary
- Task 2: Count the lines
- Task 3: Add to the end
- Challenge: Save and load JSON
- Project: Saving the game

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** In short: open the file with with open, pick the right mode, and keep your dictionaries in JSON.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- with open(name, mode): "r", "w", "a"
- write writes, read and for line read
- json.dump saves, json.load loads

**Maskot:** on pozu, sag

## Sahne 12: kapanis (12 sn)

**Seslendirme:** Our game can be saved now, great! Tomorrow ships dock at the harbor. We'll meet ready-made packages written by others, and pip, which brings them to us. See you!

**Ekranda başlık:** Tomorrow: The pip package manager

**Ekranda maddeler:**

- Packages and PyPI
- requirements.txt

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
