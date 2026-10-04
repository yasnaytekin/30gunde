# Video senaryosu: Gün 1, Meet Python

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~135 sn

At Base Camp, Piko explains how to print text with print(), use Python as a calculator, write comments and read your first error message.

Ders metni: [gun-01.md](../../gunler/gun-01.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | mutlu (sag) |
| 2 | anlatim | 10 sn | on (sol) |
| 3 | kod | 12 sn | isaret (sag) |
| 4 | kod | 12 sn | mutlu (sag) |
| 5 | kod | 12 sn | isaret (sag) |
| 6 | kod | 10 sn | mutlu (alt-sag) |
| 7 | hata | 14 sn | sasirma (sag) |
| 8 | soru | 8 sn | dusunme (sag) |
| 9 | cikti | 10 sn | mutlu (sag) |
| 10 | gorev | 16 sn | isaret (sol) |
| 11 | ozet | 10 sn | on (sag) |
| 12 | kapanis | 9 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 1: Meet Python! In this lesson you'll print text on the screen, make Python do math for you, and read your very first error message.

- Print text with print()
- Do math with Python
- Read your first error

## Sahne 1: acilis (12 sn)

**Seslendirme:** Hi, I'm Piko! Welcome to Base Camp. Computers are super fast, but they don't know what to do on their own. You're the one who tells them. Ready? Today we talk to a computer for the very first time!

**Ekranda başlık:** Day 1: Meet Python

**Görsel:** `gorseller/python/harita/kamp.webp`

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Zoom into the camp on the map; Piko peeks out from beside the campfire.*

## Sahne 2: anlatim (10 sn)

**Seslendirme:** Code is a list of instructions you give a computer. Python reads them from top to bottom, line by line, and does them in order. Games, websites, artificial intelligence: Python is everywhere.

**Ekranda başlık:** What is code?

**Ekranda maddeler:**

- Code: instructions for the computer
- Python reads top to bottom, line by line
- Games, websites, AI

**Maskot:** on pozu, sol

## Sahne 3: kod (12 sn)

**Seslendirme:** Our first magic word is print. Whatever you put inside the parentheses shows up on the screen. Text goes inside quotes, numbers don't. Press Run, and two lines appear.

**Ekranda başlık:** Talk with print()

**Kod** (vurgulanan satırlar: 1, 2):

```python
print("Hello World!")
print(42)
```

**Çıktı:**

```text
Hello World!
42
```

**Maskot:** isaret pozu, sag

## Sahne 4: kod (12 sn)

**Seslendirme:** Python is also a giant calculator. Plus adds, a star multiplies, and two stars raise to a power. Two to the power of ten is exactly one thousand twenty-four!

**Ekranda başlık:** Python is a calculator

**Kod** (vurgulanan satırlar: 3):

```python
print(3 + 4)
print(10 * 5)
print(2 ** 10)
```

**Çıktı:**

```text
7
50
1024
```

**Maskot:** mutlu pozu, sag

## Sahne 5: kod (12 sn)

**Seslendirme:** A line that starts with a hash sign is a comment. Python skips it, so you can leave notes for yourself. With commas you can print several things side by side, and Python puts a space between them.

**Ekranda başlık:** Comments and commas

**Kod** (vurgulanan satırlar: 1, 2):

```python
# This is a comment, Python skips it
print("Piko", "says:", "Hi!")
print("My age:", 12)
```

**Çıktı:**

```text
Piko says: Hi!
My age: 12
```

**Maskot:** isaret pozu, sag

## Sahne 6: kod (10 sn)

**Seslendirme:** In some tasks, what you print turns into a picture on the stage. Every star becomes a Piko, and every hash sign becomes a wall. Here are five Pikos with five walls below them!

**Ekranda başlık:** Drawing on the stage

**Kod**:

```python
print("*****")
print("#####")
```

**Çıktı:**

```text
*****
#####
```

**Maskot:** mutlu pozu, alt-sag

*Yönetmen notu: Next to the output, a stage grid: stars turn into Piko figures, # signs into wall tiles.*

## Sahne 7: hata (14 sn)

**Seslendirme:** Now let's forget one letter. Python answers in red: NameError, I don't know anything called prin. It even asks: did you mean print? Don't worry, the error message shows you where the problem is. Fix the letter and run it again.

**Ekranda başlık:** Our first error

**Kod** (vurgulanan satırlar: 1):

```python
prin("Hello!")
```

**Çıktı:**

```text
NameError: name 'prin' is not defined. Did you mean: 'print'?
```

**Düzeltilmiş kod:**

```python
print("Hello!")
```

**Düzeltilmiş çıktı:**

```text
Hello!
```

**Maskot:** sasirma pozu, sag

*Yönetmen notu: The error line flashes red; the missing 't' drops into place and it turns green.*

## Sahne 8: soru (8 sn)

**Seslendirme:** Your turn. Do you think these two lines print the same thing? Think for a second...

**Ekranda başlık:** What will it print?

**Kod**:

```python
print(3 + 4)
print("3 + 4")
```

**Maskot:** dusunme pozu, sag

*Yönetmen notu: A 3-second countdown on screen.*

## Sahne 9: cikti (10 sn)

**Seslendirme:** Nope! The first line does the math and prints seven. In the second line the math is inside quotes, so it's just text. Python doesn't calculate it, it prints it exactly as it is.

**Ekranda başlık:** The answer

**Kod** (vurgulanan satırlar: 2):

```python
print(3 + 4)
print("3 + 4")
```

**Çıktı:**

```text
7
3 + 4
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (16 sn)

**Seslendirme:** Now the stage is yours! First you'll print your very first words, then introduce yourself. You'll also find out how many hours there are in a year, but don't do the math yourself, let Python do it. And in the stage task, you'll line up your own Piko army.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Your first words
- Task 2: Introduce yourself
- Task 3: Hours in a year?
- Stage task: Piko army
- Challenge: Starry banner

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (10 sn)

**Seslendirme:** Today we printed on the screen with print, made Python do math, left a comment, and read our first error message. Not bad, right?

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- print() writes to the screen; text goes in quotes
- Do math with + - * / **
- # starts a comment; errors show the way

**Maskot:** on pozu, sag

## Sahne 12: kapanis (9 sn)

**Seslendirme:** You wrote your first code, congratulations! Tomorrow we'll open labeled boxes in the computer's memory, and keep our hero's name and health in them. See you!

**Ekranda başlık:** Tomorrow: Variables

**Görsel:** `gorseller/python/rozetler/ilk-kod.webp`

**Maskot:** tebrik pozu, orta

*Yönetmen notu: The First Code badge floats onto the screen, then the camp map slowly fades out.*

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
