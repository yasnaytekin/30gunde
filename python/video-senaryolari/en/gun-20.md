# Video senaryosu: Gün 20, The pip package manager

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~154 sn

With the crates landing at the harbor of Discovery Island, Piko explains packages, pip commands, the requirements.txt file, and the version comparison trap.

Ders metni: [gun-20.md](../../gunler/gun-20.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 13 sn | mutlu (sag) |
| 2 | anlatim | 14 sn | konusma (sag) |
| 3 | anlatim | 16 sn | isaret (sol) |
| 4 | hata | 12 sn | uzgun (sag) |
| 5 | anlatim | 15 sn | konusma (sag) |
| 6 | kod | 12 sn | isaret (sol) |
| 7 | anlatim | 9 sn | dusunme (sag) |
| 8 | soru | 9 sn | dusunme (sag) |
| 9 | cikti | 16 sn | sasirma (sol) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 12 sn | on (sag) |
| 12 | kapanis | 13 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 20: The pip package manager! In this lesson you'll learn about packages, pip commands, the requirements.txt file, and the version comparison trap.

- Packages and PyPI
- pip commands
- requirements.txt and versions

## Sahne 1: acilis (13 sn)

**Seslendirme:** Hi, I'm Piko! Every day ships dock at the harbor of Discovery Island, and crates from all over the world are unloaded. Inside are ready-made tools built by other programmers. We call these crates packages, and the ship that brings them is pip!

**Ekranda başlık:** Day 20: The pip package manager

**Ekranda maddeler:**

- Discovery Island
- Packages, pip, requirements.txt

**Maskot:** mutlu pozu, sag

## Sahne 2: anlatim (14 sn)

**Seslendirme:** A package is a collection of modules someone wrote and shared with everyone. Hundreds of thousands of packages live in a giant store called PyPI. requests gets data from the internet, pygame makes games, and pandas works with tables.

**Ekranda başlık:** What is a package?

**Ekranda maddeler:**

- PyPI: the Python Package Index
- requests: data from the internet
- pygame: games
- pandas: tables

**Maskot:** konusma pozu, sag

## Sahne 3: anlatim (16 sn)

**Seslendirme:** pip is the program that installs packages. These commands don't go inside your Python code; they're typed into the terminal on your computer. install installs, and with two equals signs you pick a specific version. list and freeze show the installed packages, and uninstall removes one.

**Ekranda başlık:** pip commands (in the terminal)

**Ekranda maddeler:**

- pip install requests
- pip install pygame==2.5.2
- pip list  /  pip freeze
- pip uninstall requests

**Maskot:** isaret pozu, sol

## Sahne 4: hata (12 sn)

**Seslendirme:** Here's the most common mistake: writing a pip command inside a Python file. Python thinks it's code and gives a SyntaxError. pip install always runs in the terminal.

**Ekranda başlık:** Common mistake: pip inside the code

**Kod** (vurgulanan satırlar: 1):

```python
pip install requests
```

**Çıktı:**

```text
SyntaxError: invalid syntax
```

**Maskot:** uzgun pozu, sag

## Sahne 5: anlatim (15 sn)

**Seslendirme:** The packages a project needs are written in a requirements.txt file, with a package and its version on each line. Anyone who downloads your project installs them all with one command: pip install dash r requirements.txt.

**Ekranda başlık:** requirements.txt

**Ekranda maddeler:**

- requests==2.31.0
- pygame==2.5.2
- Install them all: pip install -r requirements.txt

**Maskot:** konusma pozu, sag

## Sahne 6: kod (12 sn)

**Seslendirme:** Reading a line like that with Python is easy. I split it at the two equals signs with split, and unpack both parts into two variables at once.

**Ekranda başlık:** Split the line

**Kod** (vurgulanan satırlar: 2):

```python
line = "requests==2.31.0"
name, version = line.split("==")
print("Package:", name)
print("Version:", version)
```

**Çıktı:**

```text
Package: requests
Version: 2.31.0
```

**Maskot:** isaret pozu, sol

## Sahne 7: anlatim (9 sn)

**Seslendirme:** Version numbers have three parts: major, minor and patch. There's a trap when you compare them, so let's see it right away.

**Ekranda başlık:** Version numbers

**Ekranda maddeler:**

- 2.31.0 = major.minor.patch
- Which is newer: 2.4.1 or 2.31.0?

**Maskot:** dusunme pozu, sag

## Sahne 8: soru (9 sn)

**Seslendirme:** If you compare the versions as text, do you think 2.4.1 comes out bigger? Does it print True or False?

**Ekranda başlık:** What will it print?

**Kod**:

```python
a = "2.4.1"
b = "2.31.0"
print("As text:", a > b)
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (16 sn)

**Seslendirme:** It printed True, but that's wrong! Text is compared letter by letter, and four is bigger than three. The right way is to turn the parts into numbers and make a tuple. Then thirty-one is bigger than four, and 2.31.0 comes out newer.

**Ekranda başlık:** The version trap

**Kod** (vurgulanan satırlar: 4, 6):

```python
a = "2.4.1"
b = "2.31.0"
print("As text:", a > b)
va = tuple(int(p) for p in a.split("."))
vb = tuple(int(p) for p in b.split("."))
print("As numbers:", va > vb)
```

**Çıktı:**

```text
As text: True
As numbers: False
```

**Maskot:** sasirma pozu, sol

## Sahne 10: gorev (13 sn)

**Seslendirme:** In the tasks you'll split a line, turn a whole requirements text into a dictionary, and find which of two versions is newer. In the project you're preparing our game's package list.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Split the line
- Task 2: requirements reader
- Task 3: Which is newer?
- Challenge: Missing packages
- Project: Package list

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (12 sn)

**Seslendirme:** In short: packages live on PyPI, pip installs them from the terminal, and requirements.txt keeps the list. A surprise: type import this and run it!

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- Package = shared ready-made modules
- pip install, list, freeze, uninstall
- Compare versions as numbers

**Maskot:** on pozu, sag

## Sahne 12: kapanis (13 sn)

**Seslendirme:** We've finished Discovery Island, congratulations! Tomorrow we set sail for Knowledge Harbor. There we'll build our own data types with class: classes and objects. See you!

**Ekranda başlık:** Tomorrow: Classes and objects

**Ekranda maddeler:**

- New region: Knowledge Harbor
- class, __init__, self

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
