# Video senaryosu: Gün 12, Modules

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~123 sn

Piko opens the workshop's tool cabinet: using modules with import, the math and random modules, importing with from and as, and the idea of writing your own module.

Ders metni: [gun-12.md](../../gunler/gun-12.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | mutlu (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 14 sn | konusma (sag) |
| 4 | kod | 14 sn | isaret (sag) |
| 5 | anlatim | 12 sn | on (sol) |
| 6 | hata | 12 sn | sasirma (sag) |
| 7 | soru | 8 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 12 sn | isaret (sol) |
| 10 | ozet | 6 sn | on (sag) |
| 11 | kapanis | 9 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 12: Modules! In this lesson you'll use ready-made modules with import, do math with math, and add luck to your game with random.

- Using modules with import
- math and random
- from, as and seed

## Sahne 1: acilis (12 sn)

**Seslendirme:** Hi, I'm Piko! There's a giant tool cabinet on the workshop wall. Every drawer holds tools made by other makers: math tools, dice and lottery tools. In Python these drawers are called modules. Let's open them!

**Ekranda başlık:** Day 12: Modules

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** mutlu pozu, sag

## Sahne 2: kod (14 sn)

**Seslendirme:** A module is a Python file full of functions. You bring it into your project with import. Then you write the module's name, a dot, and the tool's name: square root, the number pi, rounding down and rounding up. Python comes with these modules.

**Ekranda başlık:** import math

**Kod** (vurgulanan satırlar: 1, 3):

```python
import math

print(math.sqrt(49))
print(round(math.pi, 4))
print(math.floor(4.7), math.ceil(4.2))
```

**Çıktı:**

```text
7.0
3.1416
4 5
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (14 sn)

**Seslendirme:** The surprises in games come from the random module. randint gives a random whole number between two numbers, both included. choice picks one item from a list, and shuffle mixes a list up. The result changes every time you run it!

**Ekranda başlık:** random: tools of luck

**Kod** (vurgulanan satırlar: 3, 5, 6):

```python
import random

print("Dice:", random.randint(1, 6))
friends = ["Ali", "Ece", "Can", "Zeynep"]
print("Picked:", random.choice(friends))
random.shuffle(friends)
print("Shuffled:", friends)
```

**Çıktı:**

```text
Dice: 4
Picked: Ece
Shuffled: ['Can', 'Ali', 'Zeynep', 'Ece']
```

**Maskot:** konusma pozu, sag

## Sahne 4: kod (14 sn)

**Seslendirme:** With from, you take only the tool you want out of the drawer, so you don't have to write math in front of it. With as, you shorten long names. And when the seed is fixed, the random number comes out the same every time.

**Ekranda başlık:** from, as and seed

**Kod** (vurgulanan satırlar: 1, 2, 6):

```python
from math import sqrt, pi
import random as rnd

print(sqrt(144))
print(pi)
rnd.seed(7)
print(rnd.randint(1, 100))
```

**Çıktı:**

```text
12.0
3.141592653589793
42
```

**Maskot:** isaret pozu, sag

## Sahne 5: anlatim (12 sn)

**Seslendirme:** You can write your own module too. If you make a file called tools.py on your computer, another file in the same folder can use its functions by saying import tools. That's how big projects are organized.

**Ekranda başlık:** Your own module

**Ekranda maddeler:**

- tools.py: your own functions
- In the same folder: import tools
- This is how big projects are split into parts

**Maskot:** on pozu, sol

## Sahne 6: hata (12 sn)

**Seslendirme:** We said import math, but then wrote sqrt on its own. Python gives a NameError: it doesn't know sqrt. Either write math dot sqrt, or bring sqrt in directly with from.

**Ekranda başlık:** Forgetting the module name

**Kod** (vurgulanan satırlar: 2):

```python
import math
print(sqrt(16))
```

**Çıktı:**

```text
NameError: name 'sqrt' is not defined
```

**Maskot:** sasirma pozu, sag

## Sahne 7: soru (8 sn)

**Seslendirme:** One rounds down, the other rounds up. What do you think this adds up to?

**Ekranda başlık:** What will it print?

**Kod**:

```python
import math
print(math.floor(7.9) + math.ceil(7.1))
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Fifteen! floor brought seven point nine down to seven, and ceil pushed seven point one up to eight. Seven plus eight is fifteen.

**Ekranda başlık:** The answer

**Kod**:

```python
import math
print(math.floor(7.9) + math.ceil(7.1))
```

**Çıktı:**

```text
15
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (12 sn)

**Seslendirme:** In the tasks you'll find the side of a square with math, roll a die with random, and pick a random prize from a treasure list. In the challenge you'll work out the area of a circle using pi.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Square root
- Task 2: Roll the die
- Task 3: Random treasure
- Challenge: Circle area

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (6 sn)

**Seslendirme:** Today we brought other makers' tools into our project and added some luck to our game.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- Bring it in with import module, use it with module.tool
- math: sqrt, pi, floor, ceil; random: randint, choice, shuffle
- Write less with from ... import and as; repeat with seed

**Maskot:** on pozu, sag

## Sahne 11: kapanis (9 sn)

**Seslendirme:** The tool cabinet is yours now! Tomorrow we'll fire up the magic mold in the corner of the workshop: list comprehensions, which squeeze four-line loops into a single line.

**Ekranda başlık:** Tomorrow: List comprehensions

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
