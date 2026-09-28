# Video senaryosu: Gün 13, List comprehensions

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~117 sn

With the workshop's magic mold, Piko explains list comprehensions: building a list in one line, filtering with if, transforming with if-else, and tiny nameless functions with lambda.

Ders metni: [gun-13.md](../../gunler/gun-13.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 13 sn | mutlu (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 9 sn | konusma (sag) |
| 4 | kod | 12 sn | isaret (sag) |
| 5 | kod | 13 sn | konusma (sag) |
| 6 | hata | 10 sn | uzgun (sag) |
| 7 | soru | 8 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 11 sn | isaret (sol) |
| 10 | ozet | 7 sn | on (sag) |
| 11 | kapanis | 10 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 13: List comprehensions! In this lesson you'll build lists in a single line, filter them with if, and write tiny functions with lambda.

- Lists in one line
- Filter with if, transform with if-else
- lambda: a mini function

## Sahne 1: acilis (13 sn)

**Seslendirme:** Hi, I'm Piko! In the corner of the workshop there's a magic mold: you drop materials in one side, and finished products come out the other. In Python this is called a list comprehension. It squeezes four-line loops into a single line!

**Ekranda başlık:** Day 13: List comprehensions

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** mutlu pozu, sag

## Sahne 2: kod (14 sn)

**Seslendirme:** The long way to make a new list from a list: an empty list, a loop, and append. The short way is one line! Read it like this: for each n in nums, take n times ten. Both ways give the same result.

**Ekranda başlık:** The long way, the short way

**Kod** (vurgulanan satırlar: 8):

```python
nums = [1, 2, 3, 4, 5]

tens = []
for n in nums:
    tens.append(n * 10)
print(tens)

print([n * 10 for n in nums])
```

**Çıktı:**

```text
[10, 20, 30, 40, 50]
[10, 20, 30, 40, 50]
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (9 sn)

**Seslendirme:** Add an if at the end and you keep only the items you want. The mold doesn't let the scores under sixty through.

**Ekranda başlık:** Filter with if

**Kod** (vurgulanan satırlar: 2):

```python
scores = [45, 90, 12, 77, 100, 63]
passed = [s for s in scores if s >= 60]
print("Passed:", passed)
```

**Çıktı:**

```text
Passed: [90, 77, 100, 63]
```

**Maskot:** konusma pozu, sag

## Sahne 4: kod (12 sn)

**Seslendirme:** If you want to pick one of two results for every item, if and else go at the front. To filter, the if goes at the end; to transform, the if-else goes at the front. Keep that in mind!

**Ekranda başlık:** Transform with if and else

**Kod** (vurgulanan satırlar: 2):

```python
scores = [45, 90, 12, 77]
print(["pass" if s >= 60 else "fail" for s in scores])
```

**Çıktı:**

```text
['fail', 'pass', 'fail', 'pass']
```

**Maskot:** isaret pozu, sag

## Sahne 5: kod (13 sn)

**Seslendirme:** You can write tiny one-line functions with lambda. The left side of the colon is the parameter, and the right side is the result it returns. The same mold idea works for dictionaries too: a dictionary of squares with curly braces!

**Ekranda başlık:** lambda: a nameless mini function

**Kod** (vurgulanan satırlar: 1, 2):

```python
square = lambda x: x * x
add = lambda a, b: a + b
print(square(6))
print(add(2, 3))
print({n: square(n) for n in range(1, 5)})
```

**Çıktı:**

```text
36
5
{1: 1, 2: 4, 3: 9, 4: 16}
```

**Maskot:** konusma pozu, sag

## Sahne 6: hata (10 sn)

**Seslendirme:** Put the else at the end and Python gives a SyntaxError. Remember: if there's only an if, it goes at the end; if the if comes with an else, they go at the front.

**Ekranda başlık:** else in the wrong place

**Kod** (vurgulanan satırlar: 2):

```python
nums = [1, 2, 3]
print([n for n in nums if n > 1 else 0])
```

**Çıktı:**

```text
SyntaxError: invalid syntax
```

**Maskot:** uzgun pozu, sag

## Sahne 7: soru (8 sn)

**Seslendirme:** This mold filters and transforms at the same time. Which list do you think shows up on the screen?

**Ekranda başlık:** What will it print?

**Kod**:

```python
words = ["sword", "potion", "ax"]
print([len(w) for w in words if len(w) > 2])
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Five and six! Ax has only two letters, so it got stuck in the filter. The other two words were replaced by their lengths.

**Ekranda başlık:** The answer

**Kod**:

```python
words = ["sword", "potion", "ax"]
print([len(w) for w in words if len(w) > 2])
```

**Çıktı:**

```text
[5, 6]
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (11 sn)

**Seslendirme:** In the tasks you'll make, in a single line, double every number, turn names into capital letters, and keep only the valuable loot. In the challenge you'll write a lambda and build a list of squares.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Double it
- Task 2: In capitals
- Task 3: Valuable loot
- Challenge: With lambda

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (7 sn)

**Seslendirme:** Today we turned long loops into one-line molds and met tiny nameless functions.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- [expression for x in list]
- Filter: if at the end; transform: if-else at the front
- A mini function with lambda x: x * x

**Maskot:** on pozu, sag

## Sahne 11: kapanis (10 sn)

**Seslendirme:** You've mastered the magic mold! Tomorrow the workshop master shares a secret: plugging tools into other tools. We'll play with functions using map, filter and sorted.

**Ekranda başlık:** Tomorrow: Higher-order functions

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
