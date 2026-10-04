# Video senaryosu: Gün 27, Python and MongoDB

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~160 sn

Starting from the library on Python Mountain, Piko explains the idea of a document database, MongoDB's insert, find and update operations, and bringing them to life with Python dictionaries.

Ders metni: [gun-27.md](../../gunler/gun-27.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 15 sn | konusma (sag) |
| 2 | anlatim | 16 sn | isaret (sol) |
| 3 | anlatim | 17 sn | konusma (sag) |
| 4 | kod | 14 sn | isaret (sag) |
| 5 | anlatim | 15 sn | dusunme (sol) |
| 6 | soru | 10 sn | dusunme (sag) |
| 7 | cikti | 12 sn | mutlu (sol) |
| 8 | kod | 13 sn | isaret (sag) |
| 9 | hata | 12 sn | uzgun (sol) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 12 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 27: Python and MongoDB! In this lesson you'll learn the idea of a document database, MongoDB's insert, find and update operations, and how to act them out in Python.

- Documents and collections
- insert, find, update
- Matching a query

## Sahne 1: acilis (15 sn)

**Seslendirme:** Hi, I'm Piko! In the library on the slopes of Python Mountain, every player has a file. When the librarian hears a name, they find the right file in seconds, open new files, and update levels. In the computer world, this librarian is called a database!

**Ekranda başlık:** Day 27: Python and MongoDB

**Ekranda maddeler:**

- Python Mountain
- Documents, collections, queries

**Maskot:** konusma pozu, sag

## Sahne 2: anlatim (16 sn)

**Seslendirme:** When a program closes, its variables are lost. To search thousands of players' data quickly and keep it safe, we use a database. MongoDB is a document database: every record is a document that looks like a dictionary, and documents are gathered in collections.

**Ekranda başlık:** What is a database?

**Ekranda maddeler:**

- Document: {"name": "Piko", "level": 3}
- Collection: where documents are gathered
- MongoDB = a document database

**Maskot:** isaret pozu, sol

## Sahne 3: anlatim (17 sn)

**Seslendirme:** On your own computer, you connect to a real MongoDB with the pymongo package. insert_one adds, find searches, update_one updates, and delete_one deletes. We can't connect to a database on our site, so we'll act out the collection with a list of dictionaries.

**Ekranda başlık:** Real MongoDB with pymongo

**Kod** (vurgulanan satırlar: 5, 6, 8):

```python
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["game"]

db.players.insert_one({"name": "Piko", "level": 3})
for p in db.players.find({"level": 3}):
    print(p["name"])
db.players.update_one({"name": "Piko"}, {"$set": {"level": 4}})
```

**Maskot:** konusma pozu, sag

## Sahne 4: kod (14 sn)

**Seslendirme:** Here's our collection: a list made of dictionaries. Adding a new document is as easy as append, which is exactly what insert does. And I go through all the documents with a loop.

**Ekranda başlık:** Collections and documents

**Kod** (vurgulanan satırlar: 5):

```python
players = [
    {"name": "Piko", "level": 3},
    {"name": "Ece", "level": 5},
]
players.append({"name": "Can", "level": 1})
for p in players:
    print(p["name"], "level", p["level"])
```

**Çıktı:**

```text
Piko level 3
Ece level 5
Can level 1
```

**Maskot:** isaret pozu, sag

## Sahne 5: anlatim (15 sn)

**Seslendirme:** The query inside find is a dictionary too. If it says level three, it brings back every document whose level is three. A document has to match every field in the query. The all function answers the question are they all true in a single line.

**Ekranda başlık:** What is a query?

**Ekranda maddeler:**

- find({"level": 3})
- Every field in the query must match
- all(): are they all true?
- any(): is at least one true?

**Maskot:** dusunme pozu, sol

## Sahne 6: soru (10 sn)

**Seslendirme:** I'm trying one document against four different queries. The last one is an empty query. Which ones do you think come out True, and which False?

**Ekranda başlık:** What will it print?

**Kod** (vurgulanan satırlar: 3):

```python
doc = {"name": "Piko", "level": 3, "club": "blue"}
for query in [{"level": 3}, {"level": 3, "club": "blue"}, {"level": 4}, {}]:
    ok = all(doc.get(k) == v for k, v in query.items())
    print(query, "->", ok)
```

**Maskot:** dusunme pozu, sag

## Sahne 7: cikti (12 sn)

**Seslendirme:** Level four didn't match, so it's False. The empty query has no fields to check, and all gives True when it's empty. So an empty query matches every document and brings them all back.

**Ekranda başlık:** The answer

**Kod**:

```python
doc = {"name": "Piko", "level": 3, "club": "blue"}
for query in [{"level": 3}, {"level": 3, "club": "blue"}, {"level": 4}, {}]:
    ok = all(doc.get(k) == v for k, v in query.items())
    print(query, "->", ok)
```

**Çıktı:**

```text
{'level': 3} -> True
{'level': 3, 'club': 'blue'} -> True
{'level': 4} -> False
{} -> True
```

**Maskot:** mutlu pozu, sol

## Sahne 8: kod (13 sn)

**Seslendirme:** To update, I find Piko and write the new values with update. And break ends the search after the first match, just like update_one.

**Ekranda başlık:** Updating

**Kod** (vurgulanan satırlar: 4, 5):

```python
players = [{"name": "Piko", "level": 3}, {"name": "Ece", "level": 5}]
for p in players:
    if p["name"] == "Piko":
        p.update({"level": 4})
        break
print(players)
```

**Çıktı:**

```text
[{'name': 'Piko', 'level': 4}, {'name': 'Ece', 'level': 5}]
```

**Maskot:** isaret pozu, sag

## Sahne 9: hata (12 sn)

**Seslendirme:** A common mistake: reading a field some documents don't have with square brackets. Documents can have different fields, and Python gives a KeyError. Use get to read safely.

**Ekranda başlık:** Common mistake: a missing field

**Kod** (vurgulanan satırlar: 3):

```python
players = [{"name": "Piko", "level": 3}, {"name": "Can"}]
for p in players:
    print(p["name"], p["level"])
```

**Çıktı:**

```text
Piko 3
KeyError: 'level'
```

**Maskot:** uzgun pozu, sol

## Sahne 10: gorev (13 sn)

**Seslendirme:** In the tasks you'll write your own insert_one, find and update_one functions. That means you're building the inside of MongoDB yourself! In the project you're adding players and leveling them up.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: insert_one
- Task 2: find
- Task 3: update_one
- Challenge: The $gt sign
- Project: Player database

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** In short: in MongoDB, documents are like dictionaries and are gathered in collections. You find them with queries, update them with update, and delete them with delete.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- Documents and collections
- insert, find, update, delete
- Matching a query: all()

**Maskot:** on pozu, sag

## Sahne 12: kapanis (12 sn)

**Seslendirme:** You're the library's new master! Tomorrow we move to the radio in the camp house. We'll learn about APIs, where programs talk to each other, and how to read JSON responses. See you!

**Ekranda başlık:** Tomorrow: Using APIs

**Ekranda maddeler:**

- What is an API?
- JSON and status codes

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
