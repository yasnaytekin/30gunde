# Video senaryosu: Gün 6, Tuples

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~124 sn

Using the sealed coordinates of the Data Forest, Piko explains tuples: creating them, why they can't change, converting to lists, unpacking, and the one-item tuple trap.

Ders metni: [gun-06.md](../../gunler/gun-06.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | mutlu (sag) |
| 2 | kod | 12 sn | isaret (sag) |
| 3 | hata | 14 sn | sasirma (sag) |
| 4 | kod | 14 sn | konusma (sag) |
| 5 | kod | 12 sn | isaret (sag) |
| 6 | kod | 12 sn | konusma (sag) |
| 7 | soru | 10 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 14 sn | isaret (sol) |
| 10 | ozet | 6 sn | on (sag) |
| 11 | kapanis | 8 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 6: Tuples! In this lesson you'll meet sealed boxes that can't be changed, learn to unpack them, and avoid the one-item tuple trap.

- What is a tuple, and why can't it change?
- Converting with list() and tuple()
- Unpacking: x, y = pos

## Sahne 1: acilis (12 sn)

**Seslendirme:** Hi, I'm Piko! Old explorers carved marks into the trees of the Data Forest: three comma five, eight comma two. These are the coordinates of secret places, and nobody can change them. Today we open sealed boxes, called tuples!

**Ekranda başlık:** Day 6: Tuples

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** mutlu pozu, sag

## Sahne 2: kod (12 sn)

**Seslendirme:** A tuple looks a lot like a list, but it's written with parentheses. You still reach items by position number, and len works too. So what's the difference? Once it's created, it can't be changed.

**Ekranda başlık:** What is a tuple?

**Kod** (vurgulanan satırlar: 1):

```python
colors = ("blue", "yellow", "green")
print(colors[0])
print(colors[-1])
print(len(colors))
```

**Çıktı:**

```text
blue
green
3
```

**Maskot:** isaret pozu, sag

## Sahne 3: hata (14 sn)

**Seslendirme:** Let's try to break the seal. Python gives a TypeError: a tuple doesn't allow changing its items. That's a feature! It stops us from accidentally breaking things that should never change, like map coordinates or the days of the week.

**Ekranda başlık:** The seal can't be broken

**Kod** (vurgulanan satırlar: 2):

```python
colors = ("blue", "yellow", "green")
colors[0] = "red"
```

**Çıktı:**

```text
TypeError: 'tuple' object does not support item assignment
```

**Maskot:** sasirma pozu, sag

## Sahne 4: kod (14 sn)

**Seslendirme:** If you really need to change it, there's a way. Unlock it with list, change the list, then seal it again with tuple. So the only way to change a tuple is to make a new one.

**Ekranda başlık:** Unlock, change, lock

**Kod** (vurgulanan satırlar: 2, 4):

```python
colors = ("blue", "yellow")
items = list(colors)
items.append("green")
colors = tuple(items)
print(colors)
print(type(colors))
```

**Çıktı:**

```text
('blue', 'yellow', 'green')
<class 'tuple'>
```

**Maskot:** konusma pozu, sag

## Sahne 5: kod (12 sn)

**Seslendirme:** You can spread a tuple's values into separate variables in one line. This is called unpacking. The two names on the left take the two values on the right in order: x becomes three and y becomes five.

**Ekranda başlık:** Unpacking a tuple

**Kod** (vurgulanan satırlar: 2):

```python
pos = (3, 5)
x, y = pos
print("x =", x)
print("y =", y)
```

**Çıktı:**

```text
x = 3
y = 5
```

**Maskot:** isaret pozu, sag

## Sahne 6: kod (12 sn)

**Seslendirme:** Tuples have useful tools too. in asks whether something is there, and index tells you its position. Add two tuples with plus, and you get a brand new tuple.

**Ekranda başlık:** Handy operations

**Kod**:

```python
colors = ("blue", "yellow", "green")
print("yellow" in colors)
print(colors.index("yellow"))
print((1, 2) + (3, 4))
```

**Çıktı:**

```text
True
1
(1, 2, 3, 4)
```

**Maskot:** konusma pozu, sag

## Sahne 7: soru (10 sn)

**Seslendirme:** Now a little trap! Both variables look like a five in parentheses. Do you think they have the same type?

**Ekranda başlık:** What will it print?

**Kod**:

```python
a = (5)
b = (5,)
print(type(a))
print(type(b))
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** They're not the same! Without a comma, Python thinks it's just an ordinary number in parentheses. When you write a one-item tuple, don't forget the comma.

**Ekranda başlık:** The answer

**Kod** (vurgulanan satırlar: 2):

```python
a = (5)
b = (5,)
print(type(a))
print(type(b))
```

**Çıktı:**

```text
<class 'int'>
<class 'tuple'>
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (14 sn)

**Seslendirme:** Task time! You'll unpack a position into two variables, find the first and last color of a palette, and add a new item to a sealed bag. In the challenge you'll swap two variables without using a third one.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Unpack the position
- Task 2: Color palette
- Task 3: Add a new item
- Challenge: Swap them

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (6 sn)

**Seslendirme:** Today we opened sealed boxes, spread out what was inside, and learned the comma trap.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- Tuple: written with ( ), can't be changed
- Unlock with list(), reseal with tuple()
- Unpack with x, y = pos; one item: (5,)

**Maskot:** on pozu, sag

## Sahne 11: kapanis (8 sn)

**Seslendirme:** The coordinates are safe! Tomorrow we'll pass the same places in the forest again and again, and meet sets, which throw away repeats on their own.

**Ekranda başlık:** Tomorrow: Sets

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
