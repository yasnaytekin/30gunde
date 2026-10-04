# Video senaryosu: Gün 10, Loops

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~125 sn

In the tower of Logic Castle, Piko explains while and for loops: range(), looping over lists, enumerate, break, continue, and the infinite loop trap.

Ders metni: [gun-10.md](../../gunler/gun-10.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | konusma (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 12 sn | konusma (sag) |
| 4 | kod | 12 sn | mutlu (sag) |
| 5 | kod | 12 sn | isaret (sag) |
| 6 | soru | 10 sn | dusunme (sag) |
| 7 | cikti | 10 sn | mutlu (sag) |
| 8 | hata | 12 sn | uzgun (sag) |
| 9 | gorev | 14 sn | isaret (sol) |
| 10 | ozet | 8 sn | on (sag) |
| 11 | kapanis | 9 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 10: Loops! In this lesson you'll let the computer do repeating work with while and for loops, and use range, break and continue.

- while and for
- range() and enumerate
- break, continue, infinite loops

## Sahne 1: acilis (12 sn)

**Seslendirme:** Hi, I'm Piko! The tower of Logic Castle has a hundred steps. If we wrote a separate print for every step, our fingers would get tired! Computers do repeating work without ever getting bored. Today we learn loops.

**Ekranda başlık:** Day 10: Loops

**Görsel:** `gorseller/python/harita/kale.webp`

**Maskot:** konusma pozu, sag

## Sahne 2: kod (14 sn)

**Seslendirme:** while runs the code inside it again and again as long as the condition is true. Each round, the number goes down by one. Five, four, three, two, one... and at zero the condition turns false and the loop ends.

**Ekranda başlık:** while: as long as it's true

**Kod** (vurgulanan satırlar: 2, 4):

```python
count = 5
while count > 0:
    print(count)
    count -= 1
print("Liftoff!")
```

**Çıktı:**

```text
5
4
3
2
1
Liftoff!
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (12 sn)

**Seslendirme:** For a set number of repeats, we use for and range. When you say range one to four, four isn't included. The third number is the step: it counts by twos.

**Ekranda başlık:** for and range()

**Kod** (vurgulanan satırlar: 1, 3):

```python
for i in range(1, 4):
    print("Round", i)
print(list(range(0, 10, 2)))
```

**Çıktı:**

```text
Round 1
Round 2
Round 3
[0, 2, 4, 6, 8]
```

**Maskot:** konusma pozu, sag

## Sahne 4: kod (12 sn)

**Seslendirme:** How long would it take to add up the numbers from one to a hundred by hand? Python adds each number to the total, round by round, and finishes in the blink of an eye.

**Ekranda başlık:** The adding machine

**Kod** (vurgulanan satırlar: 3):

```python
total = 0
for n in range(1, 101):
    total += n
print("Sum from 1 to 100:", total)
```

**Çıktı:**

```text
Sum from 1 to 100: 5050
```

**Maskot:** mutlu pozu, sag

## Sahne 5: kod (12 sn)

**Seslendirme:** for hands you each item of a list in order. enumerate adds a position number too. And break leaves the loop right away: once the map was found, the key was never checked.

**Ekranda başlık:** Looping over a list and break

**Kod** (vurgulanan satırlar: 2, 6):

```python
bag = ["sword", "potion", "map", "key"]
for i, item in enumerate(bag, 1):
    print(f"{i}. {item}")
    if item == "map":
        print("Found the map, I'll stop searching.")
        break
```

**Çıktı:**

```text
1. sword
2. potion
3. map
Found the map, I'll stop searching.
```

**Maskot:** isaret pozu, sag

## Sahne 6: soru (10 sn)

**Seslendirme:** continue skips this round and moves on to the next one. So with break and continue together, which numbers does this code print?

**Ekranda başlık:** What will it print?

**Kod**:

```python
for n in range(1, 10):
    if n == 5:
        break
    if n % 2 == 0:
        continue
    print(n)
```

**Maskot:** dusunme pozu, sag

## Sahne 7: cikti (10 sn)

**Seslendirme:** One and three! On even numbers, continue skipped the round. And when we got to five, break ended the loop, so five wasn't even printed.

**Ekranda başlık:** The answer

**Kod** (vurgulanan satırlar: 3, 5):

```python
for n in range(1, 10):
    if n == 5:
        break
    if n % 2 == 0:
        continue
    print(n)
```

**Çıktı:**

```text
1
3
```

**Maskot:** mutlu pozu, sag

## Sahne 8: hata (12 sn)

**Seslendirme:** The most common mistake: forgetting to change the condition. count stays at three, the condition stays true, and the loop never ends. This is called an infinite loop; on our site it's stopped after six seconds.

**Ekranda başlık:** The infinite loop

**Kod** (vurgulanan satırlar: 2):

```python
count = 3
while count > 0:
    print(count)
```

**Çıktı:**

```text
3
3
3
3
...
```

**Maskot:** uzgun pozu, sag

## Sahne 9: gorev (14 sn)

**Seslendirme:** In the tasks you'll count down with while, print a number's times table, and add up gold without using sum. In the stage task you'll build a Piko pyramid. And in the challenge you'll give special names to numbers divisible by three and five.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Countdown
- Task 2: Times table
- Task 3: Add up the gold
- Stage task: Piko pyramid
- Challenge: PiKo numbers

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (8 sn)

**Seslendirme:** Today we let loops do the repeating work. A hundred steps or a thousand, now a single loop is enough.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- while: as long as it's true; remember to change the condition
- for + range(start, stop, step)
- enumerate gives positions; break exits, continue skips

**Maskot:** on pozu, sag

## Sahne 11: kapanis (9 sn)

**Seslendirme:** You've conquered the tower, congratulations! Tomorrow we head to the Tool Workshop. You'll build your own tools, called functions, that you write once and use as often as you like.

**Ekranda başlık:** Tomorrow: Functions

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
