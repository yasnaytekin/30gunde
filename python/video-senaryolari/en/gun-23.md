# Video senaryosu: Gün 23, Virtual environments

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~163 sn

With two ships' separate cargo holds in Knowledge Harbor, Piko explains why virtual environments are needed, the venv commands, and sharing a package list.

Ders metni: [gun-23.md](../../gunler/gun-23.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | konusma (sag) |
| 2 | anlatim | 16 sn | dusunme (sol) |
| 3 | anlatim | 17 sn | isaret (sag) |
| 4 | anlatim | 10 sn | mutlu (sol) |
| 5 | hata | 13 sn | uzgun (sag) |
| 6 | anlatim | 14 sn | konusma (sag) |
| 7 | soru | 10 sn | dusunme (sag) |
| 8 | cikti | 10 sn | sasirma (sol) |
| 9 | kod | 12 sn | isaret (sag) |
| 10 | kod | 11 sn | isaret (sol) |
| 11 | gorev | 13 sn | konusma (sag) |
| 12 | ozet | 11 sn | on (sag) |
| 13 | kapanis | 12 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 23: Virtual environments! In this lesson you'll learn why virtual environments matter, the venv commands, and how to share your package list.

- The version clash problem
- venv commands
- Sharing with requirements.txt

## Sahne 1: acilis (14 sn)

**Seslendirme:** Hi, I'm Piko! Two ships sit side by side at Knowledge Harbor: one carries fish, the other carries flowers. Imagine if the cargo got mixed up! Each ship has its own hold. Python projects should have their own hold too. It's called a virtual environment.

**Ekranda başlık:** Day 23: Virtual environments

**Ekranda maddeler:**

- Knowledge Harbor
- Project structure with venv

**Maskot:** konusma pozu, sag

## Sahne 2: anlatim (16 sn)

**Seslendirme:** Let's see the problem. Your game project needs pygame 2.5, and an old project needs 2.1. If the computer has only one box of packages, both can't be installed at once; update one and the other breaks. A virtual environment gives each project its own box.

**Ekranda başlık:** The problem: a version clash

**Ekranda maddeler:**

- game → pygame 2.5
- old-game → pygame 2.1
- One box: one of them breaks
- Virtual environment: a box for each project

**Maskot:** dusunme pozu, sol

## Sahne 3: anlatim (17 sn)

**Seslendirme:** These commands are typed into the terminal while you're in the project folder. The first sets up an environment called dot venv. Then you activate it: activate in the Scripts folder on Windows, or the source command on macOS and Linux. To close it, deactivate is enough.

**Ekranda başlık:** Create and activate (in the terminal)

**Ekranda maddeler:**

- python -m venv .venv
- Windows: .venv\Scripts\activate
- macOS/Linux: source .venv/bin/activate
- Close it: deactivate

**Maskot:** isaret pozu, sag

## Sahne 4: anlatim (10 sn)

**Seslendirme:** If you see .venv in parentheses at the start of the terminal line, the environment is open. Now every package you install with pip install goes only into this project.

**Ekranda başlık:** Is the environment open?

**Ekranda maddeler:**

- (.venv) ~/game $
- pip install pygame → only for this project

**Maskot:** mutlu pozu, sol

## Sahne 5: hata (13 sn)

**Seslendirme:** A common mistake: installing a package in one environment and running the program in another, or forgetting to activate the environment. Python can't find the package and gives a ModuleNotFoundError. Open the environment first, then run it.

**Ekranda başlık:** Common mistake: the wrong environment

**Kod** (vurgulanan satırlar: 1):

```python
import pygame
```

**Çıktı:**

```text
ModuleNotFoundError: No module named 'pygame'
```

**Maskot:** uzgun pozu, sag

## Sahne 6: anlatim (14 sn)

**Seslendirme:** The environment folder is big and isn't shared. Instead, we share the package list: pip freeze writes the list into a requirements file. Your friend sets up their own environment and installs the same packages. The .venv folder also goes into gitignore.

**Ekranda başlık:** Sharing an environment

**Ekranda maddeler:**

- pip freeze > requirements.txt
- pip install -r requirements.txt
- Put the .venv folder in .gitignore

**Maskot:** konusma pozu, sag

## Sahne 7: soru (10 sn)

**Seslendirme:** There's a similar trap in code. I assigned the list to the site variable and added flask to site. What do you think happens to the game list?

**Ekranda başlık:** What will it print?

**Kod**:

```python
game = ["pygame"]
site = game
site.append("flask")
print("Game:", game)
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Game changed too! Because both names point to the same box. Just like two projects sharing a single box of packages.

**Ekranda başlık:** The answer: a shared box

**Kod**:

```python
game = ["pygame"]
site = game
site.append("flask")
print("Game:", game)
```

**Çıktı:**

```text
Game: ['pygame', 'flask']
```

**Maskot:** sasirma pozu, sol

## Sahne 9: kod (12 sn)

**Seslendirme:** The fix is to take a separate copy. With copy, site gets its own box, and game stays as it was. A virtual environment does exactly this for projects.

**Ekranda başlık:** A separate copy: copy()

**Kod** (vurgulanan satırlar: 2):

```python
game = ["pygame"]
site = game.copy()
site.append("flask")
print("Game:", game)
print("Site:", site)
```

**Çıktı:**

```text
Game: ['pygame']
Site: ['pygame', 'flask']
```

**Maskot:** isaret pozu, sag

## Sahne 10: kod (11 sn)

**Seslendirme:** Let's imitate environments with a dictionary. Different versions of the same package live in two projects without ever getting mixed up.

**Ekranda başlık:** Imitating environments

**Kod** (vurgulanan satırlar: 2, 3):

```python
envs = {
    "game": {"pygame": "2.5.2"},
    "old-game": {"pygame": "2.1.0"},
}
for name, packages in envs.items():
    print(name, "->", packages)
```

**Çıktı:**

```text
game -> {'pygame': '2.5.2'}
old-game -> {'pygame': '2.1.0'}
```

**Maskot:** isaret pozu, sol

## Sahne 11: gorev (13 sn)

**Seslendirme:** In the tasks you'll produce the environment commands, take a separate copy of a list, and find version clashes between two projects. In the project you're choosing which files to share.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Prepare the commands
- Task 2: A separate copy
- Task 3: Find the clash
- Challenge: Install into the environment
- Project: Project structure

**Maskot:** konusma pozu, sag

## Sahne 12: ozet (11 sn)

**Seslendirme:** In short: set up a virtual environment for each project, activate it, install packages inside it, and share only the list.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- Virtual environment = a package box just for the project
- python -m venv .venv, activate, deactivate
- Share requirements.txt, not .venv

**Maskot:** on pozu, sag

## Sahne 13: kapanis (12 sn)

**Seslendirme:** The holds are spotless, well done! Tomorrow we stop by the harbor's records office. We'll make numbers talk with the mean, the median and NumPy arrays. See you!

**Ekranda başlık:** Tomorrow: Statistics and NumPy

**Ekranda maddeler:**

- The statistics module
- NumPy arrays

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
