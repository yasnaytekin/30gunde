# Video senaryosu: Gün 2, Variables and built-in functions

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~148 sn

Piko explains how to keep the hero's details in labeled boxes: variables, data types, reading input with input(), and built-in functions like len, round and max.

Ders metni: [gun-02.md](../../gunler/gun-02.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 11 sn | konusma (sag) |
| 2 | kod | 13 sn | isaret (sag) |
| 3 | anlatim | 12 sn | on (sol) |
| 4 | kod | 14 sn | konusma (sag) |
| 5 | kod | 10 sn | isaret (sag) |
| 6 | kod | 14 sn | konusma (sag) |
| 7 | kod | 12 sn | mutlu (sag) |
| 8 | hata | 14 sn | sasirma (sag) |
| 9 | soru | 8 sn | dusunme (sag) |
| 10 | cikti | 8 sn | mutlu (sag) |
| 11 | gorev | 14 sn | isaret (sol) |
| 12 | ozet | 8 sn | on (sag) |
| 13 | kapanis | 10 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 2: Variables and built-in functions! In this lesson you'll store information in labeled boxes, get to know data types, and use Python's built-in functions.

- Variables: labeled boxes
- Data types and input()
- len, round, max, min

## Sahne 1: acilis (11 sn)

**Seslendirme:** Hi, I'm Piko! We're still at Base Camp. Our game is going to have a hero. But how will the computer remember the hero's name, health and gold? Today we open labeled boxes in memory!

**Ekranda başlık:** Day 2: Variables and built-in functions

**Görsel:** `gorseller/python/harita/kamp.webp`

**Maskot:** konusma pozu, sag

## Sahne 2: kod (13 sn)

**Seslendirme:** A variable is a labeled box you put information in. The equals sign here isn't the one from math: it means put the value on the right into the box on the left. Then you use what's inside by writing the box's name.

**Ekranda başlık:** A variable: a labeled box

**Kod** (vurgulanan satırlar: 1, 2):

```python
name = "Piko"
hp = 100
print(name)
print(hp)
```

**Çıktı:**

```text
Piko
100
```

**Maskot:** isaret pozu, sag

## Sahne 3: anlatim (12 sn)

**Seslendirme:** There are a few rules for naming boxes. A name starts with a letter or an underscore and has no spaces. Uppercase and lowercase are different. Most importantly, pick names that make sense.

**Ekranda başlık:** Naming rules

**Ekranda maddeler:**

- Start with a letter or _: score
- No spaces, use _: player_name
- Score and score are different boxes
- Pick clear names: gold, not x

**Maskot:** on pozu, sol

## Sahne 4: kod (14 sn)

**Seslendirme:** Different kinds of information go in boxes. Text is a string, whole numbers are int, decimals are float, and True or False is a bool. If you wonder what type a value is, just ask the type function.

**Ekranda başlık:** Data types

**Kod** (vurgulanan satırlar: 6, 7):

```python
name = "Piko"
hp = 100
speed = 2.5
is_alive = True
print(name, hp, speed, is_alive)
print(type(name))
print(type(hp))
```

**Çıktı:**

```text
Piko 100 2.5 True
<class 'str'>
<class 'int'>
```

**Maskot:** konusma pozu, sag

## Sahne 5: kod (10 sn)

**Seslendirme:** Put a new value in a box and it replaces the old one. The third line says: take the current gold, add twenty-five, and put the result back in the same box.

**Ekranda başlık:** Changing what's inside

**Kod** (vurgulanan satırlar: 3):

```python
gold = 10
print("At first:", gold)
gold = gold + 25
print("After the treasure:", gold)
```

**Çıktı:**

```text
At first: 10
After the treasure: 35
```

**Maskot:** isaret pozu, sag

## Sahne 6: kod (14 sn)

**Seslendirme:** With input you ask the user a question. The answer always comes back as text. If you need a number, convert it with int. On this site you type your answers in the Input box under the editor, one answer per line.

**Ekranda başlık:** Getting input from the user

**Kod** (vurgulanan satırlar: 1, 3):

```python
name = input("What's your name? ")
print("Hello", name)
age = int(input("How old are you? "))
```

**Çıktı:**

```text
What's your name? Ece
Hello Ece
How old are you? 12
```

**Maskot:** konusma pozu, sag

## Sahne 7: kod (12 sn)

**Seslendirme:** Python comes with ready-to-use functions. len measures length, float turns text into a decimal number, round rounds, and max and min find the biggest and the smallest.

**Ekranda başlık:** Built-in functions

**Kod**:

```python
name = "Piko"
print(len(name))
print(float("2.5") + 1)
print(round(7.6))
print(max(3, 9, 4), min(3, 9, 4))
```

**Çıktı:**

```text
4
3.5
8
9 3
```

**Maskot:** mutlu pozu, sag

## Sahne 8: hata (14 sn)

**Seslendirme:** The most common mistake: trying to add text and a number. Twelve in quotes is text, but one is a number. Python says TypeError: you can only add text to text. You'll figure out how to fix it yourself in the Type detective task.

**Ekranda başlık:** Text + number = error

**Kod** (vurgulanan satırlar: 2):

```python
age = "12"
print(age + 1)
```

**Çıktı:**

```text
TypeError: can only concatenate str (not "int") to str
```

**Maskot:** sasirma pozu, sag

## Sahne 9: soru (8 sn)

**Seslendirme:** Let's see. What do you think this code prints? Ten, five, or something else?

**Ekranda başlık:** What will it print?

**Kod**:

```python
gold = 10
gold = gold + 5
print(gold)
```

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (8 sn)

**Seslendirme:** Fifteen! First the box held ten. The second line added five and put the result back into the same box.

**Ekranda başlık:** The answer

**Kod** (vurgulanan satırlar: 2):

```python
gold = 10
gold = gold + 5
print(gold)
```

**Çıktı:**

```text
15
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (14 sn)

**Seslendirme:** Task time! First you'll put your own name in a box. Then you'll make a hero card with three variables. In the Type detective task you'll rescue a broken piece of code. And in the challenge you'll swap what's inside two boxes.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Fill the box
- Task 2: Hero card
- Task 3: Type detective
- Stage task: Variable army
- Challenge: Swap the boxes

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (8 sn)

**Seslendirme:** Today we opened boxes and put different types of information in them. We got input from the user and put built-in functions to work.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- Variable = labeled box; = puts the right side on the left
- Types: str, int, float, bool; check with type()
- input() always gives text; convert with int()

**Maskot:** on pozu, sag

## Sahne 13: kapanis (10 sn)

**Seslendirme:** Your training at camp is done, congratulations! Tomorrow we head to Python Village. At the village market we'll do math with operators and ask true or false questions.

**Ekranda başlık:** Tomorrow: Operators

**Görsel:** `gorseller/python/harita/koy.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
