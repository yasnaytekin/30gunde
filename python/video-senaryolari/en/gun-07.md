# Video senaryosu: Gün 7, Sets

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~122 sn

In the Data Forest, Piko uses sets to keep the places he visits free of repeats: removing duplicates, adding and removing items, and union, intersection and difference.

Ders metni: [gun-07.md](../../gunler/gun-07.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 15 sn | konusma (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 10 sn | mutlu (sag) |
| 4 | kod | 14 sn | konusma (sag) |
| 5 | hata | 12 sn | uzgun (sag) |
| 6 | kod | 13 sn | isaret (sag) |
| 7 | soru | 8 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 12 sn | isaret (sol) |
| 10 | ozet | 7 sn | on (sag) |
| 11 | kapanis | 7 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 7: Sets! In this lesson you'll meet sets, which throw away repeats on their own, learn to add and remove items, and use union, intersection and difference.

- Sets: no repeats
- add, discard, remove
- Union, intersection, difference

## Sahne 1: acilis (15 sn)

**Seslendirme:** Hi, I'm Piko! Walking around the forest, I passed the same places again and again. If I write down every visit, my map will fill up! Really, I only need to know which places I've seen. Today we meet sets, which throw away repeats on their own.

**Ekranda başlık:** Day 7: Sets

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** konusma pozu, sag

## Sahne 2: kod (14 sn)

**Seslendirme:** A set is written with curly braces, and the same item can't be in it twice. We wrote camp twice, but the set kept only one. A set has no order; if you want to see it neatly, use sorted.

**Ekranda başlık:** What is a set?

**Kod** (vurgulanan satırlar: 1):

```python
places = {"camp", "village", "camp"}
print(len(places))
print(sorted(places))
```

**Çıktı:**

```text
2
['camp', 'village']
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (10 sn)

**Seslendirme:** Put a list inside a set and the repeats disappear. Five colors were written, but there are really only three different ones.

**Ekranda başlık:** Removing repeats from a list

**Kod** (vurgulanan satırlar: 2):

```python
colors = ["blue", "yellow", "blue", "green", "yellow"]
unique = set(colors)
print(len(colors), "colors written")
print(len(unique), "different colors")
print(sorted(unique))
```

**Çıktı:**

```text
5 colors written
3 different colors
['blue', 'green', 'yellow']
```

**Maskot:** mutlu pozu, sag

## Sahne 4: kod (14 sn)

**Seslendirme:** add puts in an item. We tried to add the potion twice, but the set still has just one. discard removes an item, and if it isn't there, it quietly moves on. Asking with in is very fast with sets.

**Ekranda başlık:** Add and remove

**Kod** (vurgulanan satırlar: 2, 3, 4):

```python
bag = {"sword", "potion"}
bag.add("map")
bag.add("potion")
bag.discard("sword")
print(sorted(bag))
print("potion" in bag)
```

**Çıktı:**

```text
['map', 'potion']
True
```

**Maskot:** konusma pozu, sag

## Sahne 5: hata (12 sn)

**Seslendirme:** remove deletes too, but if you try to remove an item that isn't there, you get a KeyError: there's no shield in the bag! If you're not sure, use discard; it never complains.

**Ekranda başlık:** remove and KeyError

**Kod** (vurgulanan satırlar: 2):

```python
bag = {"sword", "potion"}
bag.remove("shield")
```

**Çıktı:**

```text
KeyError: 'shield'
```

**Maskot:** uzgun pozu, sag

## Sahne 6: kod (13 sn)

**Seslendirme:** Just like sets in math, you can compare two sets. The vertical bar gives the union, the ampersand gives the intersection, and minus gives the difference. The places both Ece and I visited are the castle and the village.

**Ekranda başlık:** Set operations

**Kod** (vurgulanan satırlar: 3, 4, 5):

```python
piko = {"forest", "village", "castle"}
ece = {"village", "castle", "harbor"}
print("Both:", sorted(piko & ece))
print("All:", sorted(piko | ece))
print("Only Piko:", sorted(piko - ece))
```

**Çıktı:**

```text
Both: ['castle', 'village']
All: ['castle', 'forest', 'harbor', 'village']
Only Piko: ['forest']
```

**Maskot:** isaret pozu, sag

## Sahne 7: soru (8 sn)

**Seslendirme:** We want to make an empty set. We tried two ways. What do you think the type of each one is?

**Ekranda başlık:** What will it print?

**Kod**:

```python
a = {}
b = set()
print(type(a))
print(type(b))
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Empty curly braces aren't a set, they're an empty dictionary! For an empty set you have to write set. We'll meet dictionaries tomorrow.

**Ekranda başlık:** The answer

**Kod** (vurgulanan satırlar: 2):

```python
a = {}
b = set()
print(type(a))
print(type(b))
```

**Çıktı:**

```text
<class 'dict'>
<class 'set'>
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (12 sn)

**Seslendirme:** In the tasks you'll remove the repeats from a visit list, add a new place to your map, and find the games two friends have in common. In the challenge you'll go after the badges nobody has earned yet.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Remove repeats
- Task 2: Discover a new place
- Task 3: Games in common
- Challenge: Missing badges

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (7 sn)

**Seslendirme:** Today we learned about collections that throw away repeats on their own, and set operations that compare two sets.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- Set: no repeats, no order; empty set = set()
- add, discard, remove and a fast in
- | union, & intersection, - difference

**Maskot:** on pozu, sag

## Sahne 11: kapanis (7 sn)

**Seslendirme:** Your map is spotless! Tomorrow we'll make ID cards for the creatures of the forest with dictionaries, which work with keys and values.

**Ekranda başlık:** Tomorrow: Dictionaries

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
