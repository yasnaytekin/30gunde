# Video senaryosu: Gün 3, Operators

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~138 sn

At the Python Village market, Piko explains three ways to divide, the order of operations, the += shortcut, and comparison and logical operators.

Ders metni: [gun-03.md](../../gunler/gun-03.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | konusma (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 12 sn | konusma (sag) |
| 4 | kod | 12 sn | mutlu (sag) |
| 5 | kod | 14 sn | isaret (sag) |
| 6 | kod | 12 sn | konusma (sag) |
| 7 | hata | 12 sn | uzgun (sag) |
| 8 | soru | 8 sn | dusunme (sag) |
| 9 | cikti | 11 sn | mutlu (sag) |
| 10 | gorev | 14 sn | isaret (sol) |
| 11 | ozet | 8 sn | on (sag) |
| 12 | kapanis | 9 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 3: Operators! In this lesson you'll learn three ways to divide, the order of operations, and comparison and logical operators.

- Dividing with /, // and %
- Order of operations and +=
- Comparisons: and, or, not

## Sahne 1: acilis (12 sn)

**Seslendirme:** Hi, I'm Piko! Welcome to Python Village. In games everything runs on numbers: score, health, gold. Today you're doing the math at the village market. First question: how do you share seven apples between two people?

**Ekranda başlık:** Day 3: Operators

**Görsel:** `gorseller/python/harita/koy.webp`

**Maskot:** konusma pozu, sag

## Sahne 2: kod (14 sn)

**Seslendirme:** Division comes in three flavors. A single slash gives a decimal result. A double slash is whole-number division, and the percent sign gives the remainder. So each person gets three apples, and one is left over.

**Ekranda başlık:** Three ways to divide

**Kod** (vurgulanan satırlar: 2, 3):

```python
print(7 / 2)
print(7 // 2)
print(7 % 2)
print(2 ** 10)
```

**Çıktı:**

```text
3.5
3
1
1024
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (12 sn)

**Seslendirme:** Python follows the order from math: parentheses first, then powers, then multiplication and division, and finally addition and subtraction. Add parentheses, and the result jumps from fourteen to twenty.

**Ekranda başlık:** Order of operations

**Kod** (vurgulanan satırlar: 2):

```python
print(2 + 3 * 4)
print((2 + 3) * 4)
```

**Çıktı:**

```text
14
20
```

**Maskot:** konusma pozu, sag

## Sahne 4: kod (12 sn)

**Seslendirme:** Instead of writing score equals score plus ten, you can just write plus equals. The same trick works for minus, times and divide. The score first becomes twenty, then gets multiplied by two.

**Ekranda başlık:** Shortcuts: += and *=

**Kod** (vurgulanan satırlar: 2, 4):

```python
score = 0
score += 10
score += 10
score *= 2
print("Score:", score)
```

**Çıktı:**

```text
Score: 40
```

**Maskot:** mutlu pozu, sag

## Sahne 5: kod (14 sn)

**Seslendirme:** When you compare two values, Python says True or False. Careful: a single equals sign puts a value in a box, but a double equals sign asks a question. And exclamation equals asks: are they not equal?

**Ekranda başlık:** Comparison operators

**Kod** (vurgulanan satırlar: 5, 6):

```python
hp = 40
gold = 120
print(hp > 50)
print(gold >= 100)
print(hp == 40)
print(hp != 40)
```

**Çıktı:**

```text
False
True
True
False
```

**Maskot:** isaret pozu, sag

## Sahne 6: kod (12 sn)

**Seslendirme:** To combine questions we have logical operators. and gives True if both are true, or gives True if at least one is true. And not flips the answer.

**Ekranda başlık:** and, or, not

**Kod** (vurgulanan satırlar: 3, 4, 5):

```python
hp = 40
gold = 120
print(hp > 20 and gold > 100)
print(hp > 50 or gold > 100)
print(not hp > 50)
```

**Çıktı:**

```text
True
True
True
```

**Maskot:** konusma pozu, sag

## Sahne 7: hata (12 sn)

**Seslendirme:** This bug doesn't even give an error message, which makes it sneaky! Python uses a dot for decimals. If you use a comma, Python sees two separate numbers and prints three and six. For three and a half, write 3.5.

**Ekranda başlık:** A dot, not a comma!

**Kod** (vurgulanan satırlar: 1):

```python
print(3,5 + 1)
```

**Çıktı:**

```text
3 6
```

**Düzeltilmiş kod:**

```python
print(3.5 + 1)
```

**Düzeltilmiş çıktı:**

```text
4.5
```

**Maskot:** uzgun pozu, sag

## Sahne 8: soru (8 sn)

**Seslendirme:** Now you tell me: is nine an even number? What do you think this code prints?

**Ekranda başlık:** What will it print?

**Kod**:

```python
x = 9
print(x % 2 == 0)
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (11 sn)

**Seslendirme:** False! Nine divided by two leaves a remainder of one. One isn't equal to zero, so the answer is False, which means nine is odd. The percent sign is the easiest way to tell even from odd.

**Ekranda başlık:** The answer

**Kod** (vurgulanan satırlar: 2):

```python
x = 9
print(x % 2 == 0)
```

**Çıktı:**

```text
False
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (14 sn)

**Seslendirme:** The market is yours! You'll share seventeen slices of pizza among five friends, give your hero a health potion, and find the average of three scores. In the challenge you'll turn seconds into hours and minutes. Hint: remember the three ways to divide.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Pizza sharing
- Task 2: Health potion
- Task 3: Average
- Stage task: Equal rows
- Challenge: Seconds converter

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (8 sn)

**Seslendirme:** Today we learned three ways to divide, the shortcuts, and how to ask Python true or false questions.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- / decimal, // whole division, % remainder
- += for quick updates; parentheses change the order
- Comparisons and and, or, not: True or False

**Maskot:** on pozu, sag

## Sahne 12: kapanis (9 sn)

**Seslendirme:** Now you're the market's math master! Tomorrow we stay in the village, but this time we play with text: we'll join strings, slice them up and decorate them.

**Ekranda başlık:** Tomorrow: Strings

**Görsel:** `gorseller/python/harita/koy.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
