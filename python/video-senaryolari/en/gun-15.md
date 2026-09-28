# Video senaryosu: Gün 15, Error types

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~142 sn

In the workshop's detective office, Piko explains how to read error messages: line, type and description; common errors like NameError, ValueError, AttributeError and TypeError; and tracing with print.

Ders metni: [gun-15.md](../../gunler/gun-15.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | konusma (sag) |
| 2 | anlatim | 12 sn | on (sol) |
| 3 | hata | 12 sn | sasirma (sag) |
| 4 | hata | 10 sn | sasirma (sag) |
| 5 | hata | 10 sn | sasirma (sag) |
| 6 | anlatim | 13 sn | dusunme (sol) |
| 7 | kod | 12 sn | isaret (sag) |
| 8 | kod | 14 sn | dusunme (sag) |
| 9 | soru | 8 sn | dusunme (sag) |
| 10 | hata | 9 sn | mutlu (sag) |
| 11 | gorev | 12 sn | isaret (sol) |
| 12 | ozet | 7 sn | on (sag) |
| 13 | kapanis | 11 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 15: Error types! In this lesson you'll learn to read error messages, recognize the most common error types, and track bugs down with print.

- How to read an error message
- NameError, ValueError, AttributeError
- Tracing with print

## Sahne 1: acilis (12 sn)

**Seslendirme:** Hi, I'm Piko! The workshop's last room is a detective office. The desk is covered with broken code, and all of it gives red error messages. But error messages aren't our enemies, they're clues. Today we become error detectives!

**Ekranda başlık:** Day 15: Error types

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** konusma pozu, sag

## Sahne 2: anlatim (12 sn)

**Seslendirme:** An error message has three clues: the line number, the error type, and a short description. Go to the line first, then look at the type. The problem is usually on that line or right above it.

**Ekranda başlık:** How to read an error message

**Ekranda maddeler:**

- Line number: where is the problem?
- Error type: NameError, TypeError...
- Description: the short sentence next to the type

**Maskot:** on pozu, sol

## Sahne 3: hata (12 sn)

**Seslendirme:** NameError means a name that was never defined. Most of the time it's a typo. Python is a good detective partner: it even asks, did you mean score?

**Ekranda başlık:** NameError

**Kod** (vurgulanan satırlar: 2):

```python
score = 10
print(scroe)
```

**Çıktı:**

```text
NameError: name 'scroe' is not defined. Did you mean: 'score'?
```

**Maskot:** sasirma pozu, sag

## Sahne 4: hata (10 sn)

**Seslendirme:** With a ValueError the type is right, but the value doesn't fit. int can turn text into a number, but it can't understand twelve written out in letters.

**Ekranda başlık:** ValueError

**Kod** (vurgulanan satırlar: 2):

```python
text = "twelve"
print(int(text))
```

**Çıktı:**

```text
ValueError: invalid literal for int() with base 10: 'twelve'
```

**Maskot:** sasirma pozu, sag

## Sahne 5: hata (10 sn)

**Seslendirme:** AttributeError means you called a method that type doesn't have. upper is a tool that belongs to text; a number has no such tool.

**Ekranda başlık:** AttributeError

**Kod** (vurgulanan satırlar: 2):

```python
level = 5
print(level.upper())
```

**Çıktı:**

```text
AttributeError: 'int' object has no attribute 'upper'
```

**Maskot:** sasirma pozu, sag

## Sahne 6: anlatim (13 sn)

**Seslendirme:** Let's add a few more suspects to the detective's notebook. A forgotten colon gives a SyntaxError, and broken indentation gives an IndentationError. A missing position gives an IndexError, a missing key gives a KeyError, and dividing by zero gives a ZeroDivisionError.

**Ekranda başlık:** The suspect list

**Ekranda maddeler:**

- SyntaxError: a grammar rule is broken
- IndentationError: bad indentation
- TypeError: the wrong types together
- IndexError: a position that isn't in the list
- KeyError: a key that isn't in the dictionary
- ZeroDivisionError: dividing by zero

**Maskot:** dusunme pozu, sol

## Sahne 7: kod (12 sn)

**Seslendirme:** Many errors come from mixed-up types. They all look like three, but their types are completely different! Three in quotes is text, and three in square brackets is a list.

**Ekranda başlık:** Check the type

**Kod**:

```python
values = [3, "3", 3.0, True, [3]]
for v in values:
    print(repr(v), "->", type(v).__name__)
```

**Çıktı:**

```text
3 -> int
'3' -> str
3.0 -> float
True -> bool
[3] -> list
```

**Maskot:** isaret pozu, sag

## Sahne 8: kod (14 sn)

**Seslendirme:** Some errors don't even give a message! The total should have been sixty, but it came out thirty. The detective's trick: put prints in between. The running total never builds up, so an equals sign must have been written instead of plus equals.

**Ekranda başlık:** Trace it with print

**Kod** (vurgulanan satırlar: 4, 5):

```python
prices = [10, 20, 30]
total = 0
for p in prices:
    total = p
    print("running total:", total)
print("Total:", total)
```

**Çıktı:**

```text
running total: 10
running total: 20
running total: 30
Total: 30
```

**Maskot:** dusunme pozu, sag

## Sahne 9: soru (8 sn)

**Seslendirme:** Now you're the detective! Which error type does this code give? A KeyError, or a TypeError?

**Ekranda başlık:** Which error?

**Kod**:

```python
hero = {"name": "Piko"}
print(hero["name"] + 5)
```

**Maskot:** dusunme pozu, sag

## Sahne 10: hata (9 sn)

**Seslendirme:** TypeError! The key exists, so it's not a KeyError. But the value that comes back is text, and you can't add a number to text.

**Ekranda başlık:** The answer: TypeError

**Kod** (vurgulanan satırlar: 2):

```python
hero = {"name": "Piko"}
print(hero["name"] + 5)
```

**Çıktı:**

```text
TypeError: can only concatenate str (not "int") to str
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (12 sn)

**Seslendirme:** Your detective tasks are ready! You'll repair three broken pieces of code by reading their error messages: a TypeError, an IndexError and a KeyError. In the challenge you'll rescue an average function that crashes on an empty list.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Fix the TypeError
- Task 2: Fix the IndexError
- Task 3: Fix the KeyError
- Challenge: Dividing by zero

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (7 sn)

**Seslendirme:** Today we learned to read error messages like clues and to recognize the suspects one by one.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- First the line, then the error type, then the description
- Common errors: NameError, TypeError, ValueError...
- Check the type with type(), trace with print()

**Maskot:** on pozu, sag

## Sahne 13: kapanis (11 sn)

**Seslendirme:** You've finished the Tool Workshop, congratulations, detective! Tomorrow we set sail for Discovery Island, where we'll do math with dates and times. On the island we'll also learn to catch errors before the program crashes.

**Ekranda başlık:** Tomorrow: Dates and times

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
