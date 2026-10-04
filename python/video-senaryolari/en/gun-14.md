# Video senaryosu: Gün 14, Higher-order functions

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~124 sn

Piko shows how to use functions as values: passing a function to a function, map, filter, sorted with key, and functions that return functions (closures).

Ders metni: [gun-14.md](../../gunler/gun-14.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | konusma (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 11 sn | konusma (sag) |
| 4 | hata | 10 sn | uzgun (sag) |
| 5 | kod | 14 sn | isaret (sag) |
| 6 | kod | 14 sn | mutlu (sag) |
| 7 | soru | 9 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 13 sn | isaret (sol) |
| 10 | ozet | 8 sn | on (sag) |
| 11 | kapanis | 9 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 14: Higher-order functions! In this lesson you'll use functions as values, work with map, filter and sorted, and write functions that make functions.

- Functions are values
- map, filter, sorted and key
- Functions that make functions

## Sahne 1: acilis (12 sn)

**Seslendirme:** Hi, I'm Piko! The workshop master told me a secret: you can plug tools into other tools! Like swapping the bit on a drill, you can hand one function to another. Today we learn higher-order functions.

**Ekranda başlık:** Day 14: Higher-order functions

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** konusma pozu, sag

## Sahne 2: kod (14 sn)

**Seslendirme:** Write a function without parentheses and you don't call it, you get the function itself. use_twice applies the function you give it two times. hey first gets capital letters and an exclamation mark, then one more. You can pass a lambda too!

**Ekranda başlık:** Functions are values

**Kod** (vurgulanan satırlar: 5, 7):

```python
def shout(text):
    return text.upper() + "!"

def use_twice(func, value):
    return func(func(value))

print(use_twice(shout, "hey"))
print(use_twice(lambda n: n * 10, 3))
```

**Çıktı:**

```text
HEY!!
300
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (11 sn)

**Seslendirme:** map applies the function to every item: all the scores doubled. filter keeps the items the function says True to: here, the ones under sixty.

**Ekranda başlık:** map and filter

**Kod** (vurgulanan satırlar: 2, 3):

```python
scores = [40, 75, 90, 55]
print(list(map(lambda s: s * 2, scores)))
print(list(filter(lambda s: s < 60, scores)))
```

**Çıktı:**

```text
[80, 150, 180, 110]
[40, 55]
```

**Maskot:** konusma pozu, sag

## Sahne 4: hata (10 sn)

**Seslendirme:** Forget list, and Python shows a map object instead of the results. It's not an error, but it's no help either. To see the results, wrap it in list.

**Ekranda başlık:** Forgetting list()

**Kod** (vurgulanan satırlar: 2):

```python
scores = [40, 75, 90]
print(map(lambda s: s * 2, scores))
```

**Çıktı:**

```text
<map object at 0x7f3a2c1b5e10>
```

**Maskot:** uzgun pozu, sag

## Sahne 5: kod (14 sn)

**Seslendirme:** With key, you tell sorted what to sort by. Here we look at each player's score, and reverse True puts them from biggest to smallest. Give len as the key, and short names come first.

**Ekranda başlık:** sorted and key

**Kod** (vurgulanan satırlar: 2, 4):

```python
players = [("Ali", 120), ("Piko", 300), ("Ece", 250)]
for name, score in sorted(players, key=lambda p: p[1], reverse=True):
    print(name, score)
print("Short names first:", sorted(["Zeynep", "Can", "Ece"], key=len))
```

**Çıktı:**

```text
Piko 300
Ece 250
Ali 120
Short names first: ['Can', 'Ece', 'Zeynep']
```

**Maskot:** isaret pozu, sag

## Sahne 6: kod (14 sn)

**Seslendirme:** A function can make a new function inside it and return it. The inner function remembers the outer one's value; this is called a closure. plus5 is now a brand new tool that adds five to any number.

**Ekranda başlık:** A function that makes functions

**Kod** (vurgulanan satırlar: 4, 7):

```python
def make_adder(n):
    def add(x):
        return x + n
    return add

plus5 = make_adder(5)
print(plus5(10))
print(plus5(1))
```

**Çıktı:**

```text
15
6
```

**Maskot:** mutlu pozu, sag

## Sahne 7: soru (9 sn)

**Seslendirme:** max takes a key too, and you can give map a ready-made function. What do you think these two lines print?

**Ekranda başlık:** What will it print?

**Kod**:

```python
names = ["Piko", "Al", "Ece"]
print(max(names, key=len))
print(list(map(len, names)))
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Piko, and four, two, three! max picked the longest name. And map applied the len function to each name and put the lengths in a list.

**Ekranda başlık:** The answer

**Kod**:

```python
names = ["Piko", "Al", "Ece"]
print(max(names, key=len))
print(list(map(len, names)))
```

**Çıktı:**

```text
Piko
[4, 2, 3]
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (13 sn)

**Seslendirme:** In the tasks you'll hand a function to another function, add bonus points to scores with map, and pick out who passed with filter. In the challenge you'll write a function that makes functions: a multiplier maker.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Apply it
- Task 2: Bonus points
- Task 3: Who passed
- Challenge: Multiplier maker

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (8 sn)

**Seslendirme:** Today we passed functions around like values, applied them to lists, and made new functions.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- A function without parentheses = the function itself
- map applies, filter sifts; see it with list()
- sorted/max take a key; a closure remembers values

**Maskot:** on pozu, sag

## Sahne 11: kapanis (9 sn)

**Seslendirme:** You're a tool master now! Tomorrow we enter the workshop's last room: a detective office. We'll read red error messages and get to know the types of errors.

**Ekranda başlık:** Tomorrow: Error types

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
