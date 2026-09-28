# Video senaryosu: Gün 9, Conditions

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~124 sn

At the gate of Logic Castle, Piko teaches the program to make decisions: if, elif, else, indentation rules, and combining conditions with and, or and in.

Ders metni: [gun-09.md](../../gunler/gun-09.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | konusma (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 14 sn | konusma (sag) |
| 4 | anlatim | 10 sn | on (sol) |
| 5 | kod | 14 sn | konusma (sag) |
| 6 | hata | 12 sn | sasirma (sag) |
| 7 | soru | 9 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 13 sn | isaret (sol) |
| 10 | ozet | 8 sn | on (sag) |
| 11 | kapanis | 8 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 9: Conditions! In this lesson you'll teach your program to make decisions with if, elif and else, learn the indentation rules, and combine conditions.

- if, elif, else
- Colons and indentation
- Conditions with and, or, in

## Sahne 1: acilis (12 sn)

**Seslendirme:** Hi, I'm Piko! We've reached Logic Castle. Its gate only opens for those who have the key! In games everything runs on rules: when your health runs out, the game is over. Today we write those rules in Python.

**Ekranda başlık:** Day 9: Conditions

**Görsel:** `gorseller/python/harita/kale.webp`

**Maskot:** konusma pozu, sag

## Sahne 2: kod (14 sn)

**Seslendirme:** if means if. When the condition is True, the line under it runs. else means otherwise. Watch out for two things: the colon at the end of the line, and the four-space indent. What if there were no key? The gate would stay locked.

**Ekranda başlık:** if and else

**Kod** (vurgulanan satırlar: 2, 4):

```python
has_key = True
if has_key:
    print("The gate opened!")
else:
    print("The gate is locked.")
```

**Çıktı:**

```text
The gate opened!
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (14 sn)

**Seslendirme:** When there are more than two cases, we use elif: else if. Python checks from top to bottom and runs the first block that's true. Forty-five isn't more than seventy, but it is more than thirty.

**Ekranda başlık:** elif: else if

**Kod** (vurgulanan satırlar: 4, 5):

```python
hp = 45
if hp > 70:
    print("You're strong")
elif hp > 30:
    print("Be careful")
else:
    print("Drink a potion!")
```

**Çıktı:**

```text
Be careful
```

**Maskot:** konusma pozu, sag

## Sahne 4: anlatim (10 sn)

**Seslendirme:** Indentation matters a lot in Python. It looks at the spaces to know which lines belong to the if. In most editors, type a colon and press Enter, and the indent appears by itself.

**Ekranda başlık:** Block rules

**Ekranda maddeler:**

- A condition line ends with :
- The block is 4 spaces in
- The first true block runs, the rest are skipped

**Maskot:** on pozu, sol

## Sahne 5: kod (14 sn)

**Seslendirme:** You can combine conditions with and, or and not. Here both must be true: the age is thirteen or more, and less than twenty. Try it with different ages.

**Ekranda başlık:** Combining conditions

**Kod** (vurgulanan satırlar: 2):

```python
age = int(input("How old are you? "))
if age >= 13 and age < 20:
    print("You're a teen!")
else:
    print("Your age:", age)
```

**Çıktı:**

```text
How old are you? 15
You're a teen!
```

**Maskot:** konusma pozu, sag

## Sahne 6: hata (12 sn)

**Seslendirme:** Forgetting the colon is the most common mistake. Python says SyntaxError and even tells you what it expected: a colon! If you forget the indent, you'll get an IndentationError too.

**Ekranda başlık:** The forgotten colon

**Kod** (vurgulanan satırlar: 2):

```python
hp = 45
if hp > 30
    print("Be careful")
```

**Çıktı:**

```text
SyntaxError: expected ':'
```

**Maskot:** sasirma pozu, sag

## Sahne 7: soru (9 sn)

**Seslendirme:** You can write conditions with lists too. There's no key in the bag, but there is a sword. What do you think this code prints?

**Ekranda başlık:** What will it print?

**Kod**:

```python
inventory = ["sword", "potion"]
if "key" in inventory:
    print("Open the gate")
elif "sword" in inventory:
    print("Ready for battle")
else:
    print("Empty-handed")
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Ready for battle! The first condition was false, because there's no key. The second condition was true, and Python never even looked at the else.

**Ekranda başlık:** The answer

**Kod** (vurgulanan satırlar: 4, 5):

```python
inventory = ["sword", "potion"]
if "key" in inventory:
    print("Open the gate")
elif "sword" in inventory:
    print("Ready for battle")
else:
    print("Empty-handed")
```

**Çıktı:**

```text
Ready for battle
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (13 sn)

**Seslendirme:** In the tasks you'll open the castle gate, build a health meter, and combine two conditions for a treasure chest. In the stage task, health shows up as hearts. And in the challenge you'll pick a game mode based on age.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: The castle gate
- Task 2: Health meter
- Task 3: Treasure chest
- Stage task: Health meter
- Challenge: Game mode

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (8 sn)

**Seslendirme:** Today we taught our program to make decisions. Now it can take different paths based on rules, just like a game.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- if, elif, else: the first true block runs
- : at the end of the line, block 4 spaces in
- Combine conditions with and, or, not and in

**Maskot:** on pozu, sag

## Sahne 11: kapanis (8 sn)

**Seslendirme:** The castle gate is open! Tomorrow we'll climb the castle's hundred-step tower. We'll learn loops, which let the computer do repeating work for us.

**Ekranda başlık:** Tomorrow: Loops

**Görsel:** `gorseller/python/harita/kale.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
