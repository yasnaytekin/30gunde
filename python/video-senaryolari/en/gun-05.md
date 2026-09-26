# Video senaryosu: Gün 5, Lists

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~119 sn

In the Data Forest, Piko organizes the hero's bag with a list: making a list, adding, removing and changing items, and exploring it with sum, max and sorted.

Ders metni: [gun-05.md](../../gunler/gun-05.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | mutlu (sag) |
| 2 | kod | 13 sn | isaret (sag) |
| 3 | kod | 14 sn | konusma (sag) |
| 4 | kod | 10 sn | isaret (sag) |
| 5 | kod | 12 sn | konusma (sag) |
| 6 | hata | 12 sn | sasirma (sag) |
| 7 | soru | 8 sn | dusunme (sag) |
| 8 | cikti | 8 sn | mutlu (sag) |
| 9 | gorev | 14 sn | isaret (sol) |
| 10 | ozet | 7 sn | on (sag) |
| 11 | kapanis | 9 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 5: Lists! In this lesson you'll organize the hero's bag with a list: adding items, removing them, and exploring the list.

- Making a list and indexes
- append, remove, pop
- sum, max, sorted

## Sahne 1: acilis (12 sn)

**Seslendirme:** Hi, I'm Piko! Welcome to the Data Forest. Every hero on an adventure carries a bag: a sword, a potion, a map. Keeping dozens of items in separate variables would be hard. The solution? A list!

**Ekranda başlık:** Day 5: Lists

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** mutlu pozu, sag

## Sahne 2: kod (13 sn)

**Seslendirme:** A list is values separated by commas inside square brackets. append adds a new item to the end. Just like with strings, indexes start at zero, and len tells you how many items there are.

**Ekranda başlık:** The bag: making a list

**Kod** (vurgulanan satırlar: 1, 2):

```python
inventory = ["sword", "potion"]
inventory.append("map")
print(inventory)
print("First item:", inventory[0])
print("Item count:", len(inventory))
```

**Çıktı:**

```text
['sword', 'potion', 'map']
First item: sword
Item count: 3
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (14 sn)

**Seslendirme:** remove throws the first matching stone out of the bag. With in you ask whether an item is there. pop removes the last item and hands it back to you, so you can catch it in a variable.

**Ekranda başlık:** Remove and check

**Kod** (vurgulanan satırlar: 2, 5):

```python
inventory = ["sword", "potion", "stone"]
inventory.remove("stone")
print(inventory)
print("potion" in inventory)
last = inventory.pop()
print("Removed:", last, "Left:", inventory)
```

**Çıktı:**

```text
['sword', 'potion']
True
Removed: potion Left: ['sword']
```

**Maskot:** konusma pozu, sag

## Sahne 4: kod (10 sn)

**Seslendirme:** To change an item, write its position number and put in the new value. insert adds at any position you like; say zero, and it goes to the very front.

**Ekranda başlık:** Change and insert

**Kod** (vurgulanan satırlar: 2, 3):

```python
inventory = ["sword", "potion"]
inventory[1] = "shield"
inventory.insert(0, "map")
print(inventory)
```

**Çıktı:**

```text
['map', 'sword', 'shield']
```

**Maskot:** isaret pozu, sag

## Sahne 5: kod (12 sn)

**Seslendirme:** For lists of numbers, sum gives the total, max the biggest and min the smallest. sorted returns a new sorted list and leaves the original alone. Slicing works just like with strings.

**Ekranda başlık:** Exploring a list

**Kod**:

```python
scores = [40, 85, 60, 95]
print(sum(scores), max(scores), min(scores))
print(sorted(scores))
print(scores[0:2])
```

**Çıktı:**

```text
280 95 40
[40, 60, 85, 95]
[40, 85]
```

**Maskot:** konusma pozu, sag

## Sahne 6: hata (12 sn)

**Seslendirme:** A list with three items has no item number three! Counting starts at zero, so the last item is number two. Python says IndexError: that position is outside the list. For the last item, minus one is always safe.

**Ekranda başlık:** IndexError

**Kod** (vurgulanan satırlar: 2):

```python
inventory = ["sword", "potion", "map"]
print(inventory[3])
```

**Çıktı:**

```text
IndexError: list index out of range
```

**Düzeltilmiş kod:**

```python
inventory = ["sword", "potion", "map"]
print(inventory[-1])
```

**Düzeltilmiş çıktı:**

```text
map
```

**Maskot:** sasirma pozu, sag

## Sahne 7: soru (8 sn)

**Seslendirme:** Take a guess! Which two numbers does this code print?

**Ekranda başlık:** What will it print?

**Kod**:

```python
nums = [3, 1, 2]
nums.append(5)
print(len(nums), nums[-1])
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (8 sn)

**Seslendirme:** Four and five! append added five to the end, so the list has four items. And minus one gave the last item, which is five.

**Ekranda başlık:** The answer

**Kod**:

```python
nums = [3, 1, 2]
nums.append(5)
print(len(nums), nums[-1])
```

**Çıktı:**

```text
4 5
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (14 sn)

**Seslendirme:** Your turn! You'll add a potion to the bag, throw out the useless stone, and work out a score table with built-in functions. In the stage task you'll place Piko in the middle of a room. And in the challenge you'll sort names alphabetically.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Add to the bag
- Task 2: Throw out the stone
- Task 3: Score table
- Stage task: Put Piko in the room
- Challenge: Alphabetical order

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (7 sn)

**Seslendirme:** Today we gathered items in a list, added and removed them, and explored the list with built-in functions.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- List: values in [ ], indexes start at 0
- Change it with append, insert, remove, pop
- Explore with in, len, sum, max, min, sorted

**Maskot:** on pozu, sag

## Sahne 11: kapanis (9 sn)

**Seslendirme:** Your bag is tidy now! Tomorrow we'll find coordinates that old explorers carved into the forest's trees: sealed boxes nobody can change, called tuples.

**Ekranda başlık:** Tomorrow: Tuples

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
