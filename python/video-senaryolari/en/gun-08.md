# Video senaryosu: Gün 8, Dictionaries

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~122 sn

Piko keeps ID cards for the creatures of the Data Forest in dictionaries: reaching values by key, adding, changing and deleting, reading safely with get(), and nested data.

Ders metni: [gun-08.md](../../gunler/gun-08.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | konusma (sag) |
| 2 | kod | 12 sn | isaret (sag) |
| 3 | kod | 12 sn | konusma (sag) |
| 4 | hata | 9 sn | sasirma (sag) |
| 5 | kod | 11 sn | mutlu (sag) |
| 6 | kod | 11 sn | isaret (sag) |
| 7 | kod | 10 sn | konusma (sag) |
| 8 | soru | 10 sn | dusunme (sag) |
| 9 | cikti | 9 sn | mutlu (sag) |
| 10 | gorev | 11 sn | isaret (sol) |
| 11 | ozet | 6 sn | on (sag) |
| 12 | kapanis | 9 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 8: Dictionaries! In this lesson you'll store information with keys and values, update it, and read it safely with get.

- Keys and values
- Add, change, delete
- get() and nested data

## Sahne 1: acilis (12 sn)

**Seslendirme:** Hi, I'm Piko! Every creature living in the Data Forest has an ID card: its name, its health, its strength. If we keep them in a list, we'll mix up which is which. Today we meet Python's dictionaries!

**Ekranda başlık:** Day 8: Dictionaries

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** konusma pozu, sag

## Sahne 2: kod (12 sn)

**Seslendirme:** In a real dictionary you look up a word to find its meaning. In a Python dictionary you look up a key to find its value. With lists we used position numbers; with dictionaries we use names.

**Ekranda başlık:** Keys and values

**Kod** (vurgulanan satırlar: 1):

```python
player = {"name": "Piko", "hp": 100, "gold": 50}
print(player["name"])
print(player["gold"])
```

**Çıktı:**

```text
Piko
50
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (12 sn)

**Seslendirme:** To add a new key, write its name in square brackets and put in a value. You change a value the same way. And del deletes a key together with its value.

**Ekranda başlık:** Add, change, delete

**Kod** (vurgulanan satırlar: 2, 3, 4):

```python
player = {"name": "Piko", "hp": 100, "gold": 50}
player["level"] = 1
player["hp"] = player["hp"] - 10
del player["gold"]
print(player)
```

**Çıktı:**

```text
{'name': 'Piko', 'hp': 90, 'level': 1}
```

**Maskot:** konusma pozu, sag

## Sahne 4: hata (9 sn)

**Seslendirme:** Ask for a key that doesn't exist and Python gives you a KeyError. The message is very clear: there's no key called shield in the dictionary.

**Ekranda başlık:** KeyError

**Kod** (vurgulanan satırlar: 2):

```python
player = {"name": "Piko", "hp": 100}
print(player["shield"])
```

**Çıktı:**

```text
KeyError: 'shield'
```

**Maskot:** sasirma pozu, sag

## Sahne 5: kod (11 sn)

**Seslendirme:** Here comes our rescuer, get! It never gives an error. If the key exists it returns its value; if not, it returns the backup value you chose. The goblin has a name but no shield.

**Ekranda başlık:** Safe lookup: get()

**Kod** (vurgulanan satırlar: 3):

```python
enemy = {"name": "Goblin", "hp": 30}
print(enemy.get("name"))
print(enemy.get("shield", "No shield!"))
```

**Çıktı:**

```text
Goblin
No shield!
```

**Maskot:** mutlu pozu, sag

## Sahne 6: kod (11 sn)

**Seslendirme:** keys gives all the keys, and values gives all the values. in asks whether a key is there, and len tells you how many keys there are.

**Ekranda başlık:** Exploring a dictionary

**Kod**:

```python
player = {"name": "Piko", "hp": 100}
print(player.keys())
print(player.values())
print("hp" in player, len(player))
```

**Çıktı:**

```text
dict_keys(['name', 'hp'])
dict_values(['Piko', 100])
True 2
```

**Maskot:** isaret pozu, sag

## Sahne 7: kod (10 sn)

**Seslendirme:** You can even use a list as a value. The hero's bag is now inside the ID card! We add a new item to the bag with append.

**Ekranda başlık:** Nested data

**Kod** (vurgulanan satırlar: 2):

```python
hero = {"name": "Piko", "inventory": ["sword", "potion"]}
hero["inventory"].append("map")
print(hero["inventory"])
print(len(hero["inventory"]), "items")
```

**Çıktı:**

```text
['sword', 'potion', 'map']
3 items
```

**Maskot:** konusma pozu, sag

## Sahne 8: soru (10 sn)

**Seslendirme:** Look carefully! Does the second line add a new key, or does it do something else? What does this code print?

**Ekranda başlık:** What will it print?

**Kod**:

```python
hero = {"name": "Piko", "hp": 100}
hero["hp"] = 80
print(len(hero), hero["hp"])
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (9 sn)

**Seslendirme:** Two and eighty! The hp key was already there, so no new key was added. Only its value changed.

**Ekranda başlık:** The answer

**Kod** (vurgulanan satırlar: 2):

```python
hero = {"name": "Piko", "hp": 100}
hero["hp"] = 80
print(len(hero), hero["hp"])
```

**Çıktı:**

```text
2 80
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (11 sn)

**Seslendirme:** In the tasks you'll give the player gold, lower the goblin's health, and read the shield safely. In the challenge you'll work out a shopping bill with a price dictionary. No typing the prices by hand!

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Add gold
- Task 2: Take damage
- Task 3: Safe lookup
- Challenge: Shopping bill

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (6 sn)

**Seslendirme:** Today we stored information by name, updated it, and learned to read it safely without errors.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- Dictionary: {key: value}, reached by name
- d[key] = value adds or changes
- get() looks without errors; keys, values, in

**Maskot:** on pozu, sag

## Sahne 12: kapanis (9 sn)

**Seslendirme:** You've finished the Data Forest, congratulations! Tomorrow we reach Logic Castle, whose gate only opens for those with a key. There we'll teach our program to make decisions.

**Ekranda başlık:** Tomorrow: Conditions

**Görsel:** `gorseller/python/harita/kale.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
