# Video senaryosu: Gün 30, The finale and beyond

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~172 sn

At the top of Python Mountain, Piko sums up the 30-day journey region by region, combines everything into a single game, introduces the final tasks, and closes the course with a celebration.

Ders metni: [gun-30.md](../../gunler/gun-30.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | tebrik (sag) |
| 2 | anlatim | 17 sn | mutlu (sol) |
| 3 | anlatim | 16 sn | isaret (sag) |
| 4 | kod | 16 sn | isaret (sol) |
| 5 | soru | 12 sn | dusunme (sag) |
| 6 | cikti | 12 sn | mutlu (sol) |
| 7 | hata | 11 sn | sasirma (sag) |
| 8 | anlatim | 14 sn | konusma (sag) |
| 9 | anlatim | 16 sn | isaret (sol) |
| 10 | gorev | 16 sn | konusma (sag) |
| 11 | ozet | 12 sn | on (sag) |
| 12 | kapanis | 16 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 30: The finale and beyond! In this lesson you'll look back on the whole 30-day journey, combine everything you learned into a single game, and see what comes next.

- The 30 days in review
- All together: the final adventure
- What can you do next?

## Sahne 1: acilis (14 sn)

**Seslendirme:** Hi, I'm Piko! You made it, we're at the top of Python Mountain! Look back from here: from your first print to your very own API, you've walked a long way. I'm so proud. One last adventure is left: putting everything together in a single game!

**Ekranda başlık:** Day 30: The finale and beyond

**Ekranda maddeler:**

- Python Mountain: the summit
- Time to put it all together

**Maskot:** tebrik pozu, sag

## Sahne 2: anlatim (17 sn)

**Seslendirme:** Let's remember the path. At Base Camp you learned print and variables, and in the Village, operators and strings. In the Data Forest, lists, tuples, sets and dictionaries, and at Logic Castle, conditions and loops. And in the Tool Workshop there were functions and modules.

**Ekranda başlık:** The first half of the journey

**Ekranda maddeler:**

- Camp: print, variables
- Village: operators, strings
- Forest: lists, tuples, sets, dictionaries
- Castle: conditions, loops
- Workshop: functions, modules, lambda, errors

**Görsel:** `gorseller/python/harita/kamp.webp`

**Maskot:** mutlu pozu, sol

## Sahne 3: anlatim (16 sn)

**Seslendirme:** On Discovery Island you learned dates, try and except, regular expressions and files. At Knowledge Harbor, classes, web scraping, NumPy and pandas. And on Python Mountain, the web, databases and APIs. That's a real programmer's toolbox!

**Ekranda başlık:** The second half of the journey

**Ekranda maddeler:**

- Island: dates, try/except, regex, files, pip
- Harbor: classes, web scraping, venv, NumPy, pandas
- Mountain: the web, MongoDB, using and building APIs

**Maskot:** isaret pozu, sag

## Sahne 4: kod (16 sn)

**Seslendirme:** Here it all is together: a class, a set for items without repeats, a loop, and an f-string. The map was picked up twice, but thanks to the set there's only one in the bag. And sorted puts the bag in alphabetical order.

**Ekranda başlık:** All together

**Kod** (vurgulanan satırlar: 4, 7, 13):

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.bag = set()

    def pick(self, item):
        self.bag.add(item)
        return f"{self.name} picked up the {item}."

piko = Hero("Piko")
for item in ["map", "key", "map"]:
    print(piko.pick(item))
print("Bag:", sorted(piko.bag))
```

**Çıktı:**

```text
Piko picked up the map.
Piko picked up the key.
Piko picked up the map.
Bag: ['key', 'map']
```

**Maskot:** isaret pozu, sol

## Sahne 5: soru (12 sn)

**Seslendirme:** The heart of the final adventure is a map of rooms: nested dictionaries. Piko starts at the camp and tries to go north, east, and north. Where do you think Piko stops?

**Ekranda başlık:** What will it print?

**Kod** (vurgulanan satırlar: 7, 8):

```python
rooms = {
    "camp": {"north": "forest"},
    "forest": {"south": "camp", "east": "cave"},
    "cave": {"west": "forest"},
}
place = "camp"
for step in ["north", "east", "north"]:
    if step in rooms[place]:
        place = rooms[place][step]
        print("You are now in the", place)
    else:
        print("You can't go that way!")
```

**Maskot:** dusunme pozu, sag

## Sahne 6: cikti (12 sn)

**Seslendirme:** First to the forest, then to the cave. There's no exit north of the cave, so it said you can't go that way. Dictionaries, loops and conditions, hand in hand!

**Ekranda başlık:** The answer

**Kod**:

```python
rooms = {
    "camp": {"north": "forest"},
    "forest": {"south": "camp", "east": "cave"},
    "cave": {"west": "forest"},
}
place = "camp"
for step in ["north", "east", "north"]:
    if step in rooms[place]:
        place = rooms[place][step]
        print("You are now in the", place)
    else:
        print("You can't go that way!")
```

**Çıktı:**

```text
You are now in the forest
You are now in the cave
You can't go that way!
```

**Maskot:** mutlu pozu, sol

## Sahne 7: hata (11 sn)

**Seslendirme:** Error messages are still your best teacher. Here I wrote scroe instead of score, and Python gives a NameError and tells you which name it doesn't know. Read the error, fix it, keep going!

**Ekranda başlık:** Read the errors

**Kod** (vurgulanan satırlar: 2):

```python
score = 100
print(scroe)
```

**Çıktı:**

```text
NameError: name 'scroe' is not defined. Did you mean: 'score'?
```

**Maskot:** sasirma pozu, sag

## Sahne 8: anlatim (14 sn)

**Seslendirme:** Habits that will keep helping you from now on: move in small steps, pick meaningful names, turn repeated code into functions, and don't be shy about asking when you're stuck.

**Ekranda başlık:** Good programmer habits

**Ekranda maddeler:**

- Move in small steps
- score instead of x, move_player instead of f
- Read the error messages
- Turn repeated code into functions
- Ask when you're stuck

**Maskot:** konusma pozu, sag

## Sahne 9: anlatim (16 sn)

**Seslendirme:** So what now? Graphical games with pygame, your own website with Flask, data stories with pandas, automations that do the boring jobs, even artificial intelligence. Install Python on your own computer and run your projects there too.

**Ekranda başlık:** What can you do next?

**Ekranda maddeler:**

- Games: pygame
- Web: Flask
- Data: pandas and charts
- Automation
- Artificial intelligence
- Install Python: python.org

**Maskot:** isaret pozu, sol

## Sahne 10: gorev (16 sn)

**Seslendirme:** In the last tasks you'll write a vowel counter, a word counter and a counter class. In the final project, Piko will wander between rooms, collect items, and open the treasure door with a key. Then press Play my game on the Project page!

**Ekranda başlık:** The last tasks

**Ekranda maddeler:**

- Task 1: Vowel counter
- Task 2: Word counter
- Task 3: Counter class
- Challenge: Command engine
- Project: The final adventure
- Then: play your game and get your certificate

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (12 sn)

**Seslendirme:** The thirty days in a nutshell: you built the basics, organized your data, taught your program to make decisions, and connected it to the real world.

**Ekranda başlık:** The 30 days in review

**Ekranda maddeler:**

- The basics and data structures
- Conditions, loops, functions, classes
- Files, packages, data, the web and APIs

**Maskot:** on pozu, sag

## Sahne 12: kapanis (16 sn)

**Seslendirme:** That's it! You've finished thirty days, and now you're a Python programmer. All the pieces came together in a single game. Walking this path with you was wonderful. Get your certificate, keep coding, and see you on new adventures!

**Ekranda başlık:** Congratulations, Python programmer!

**Ekranda maddeler:**

- 30 days complete
- Final project badge

**Görsel:** `gorseller/python/rozetler/final-projesi.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
