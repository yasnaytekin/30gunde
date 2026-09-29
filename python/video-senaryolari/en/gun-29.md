# Video senaryosu: Gün 29, Building APIs

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~159 sn

At a station near the top of Python Mountain, Piko explains building our own API: HTTP methods, addresses, status codes, and functions that return (code, response).

Ders metni: [gun-29.md](../../gunler/gun-29.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | mutlu (sag) |
| 2 | anlatim | 16 sn | isaret (sol) |
| 3 | kod | 14 sn | isaret (sag) |
| 4 | anlatim | 16 sn | konusma (sag) |
| 5 | anlatim | 14 sn | dusunme (sol) |
| 6 | kod | 15 sn | isaret (sag) |
| 7 | soru | 9 sn | dusunme (sag) |
| 8 | cikti | 11 sn | mutlu (sol) |
| 9 | hata | 12 sn | uzgun (sag) |
| 10 | gorev | 14 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 13 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 29: Building APIs! In this lesson you'll build your own API and learn the GET, POST, PUT and DELETE methods and the right status codes.

- GET, POST, PUT, DELETE
- Splitting the address
- The right status code

## Sahne 1: acilis (14 sn)

**Seslendirme:** Hi, I'm Piko! We're very close to the top! Yesterday we asked other stations questions. Today we become the station that answers them. Your friends' games will read scores from the API you write. Ready?

**Ekranda başlık:** Day 29: Building APIs

**Ekranda maddeler:**

- Python Mountain
- GET, POST, PUT, DELETE

**Maskot:** mutlu pozu, sag

## Sahne 2: anlatim (16 sn)

**Seslendirme:** Every request that comes to an API has a method, which says what's being asked for. GET fetches data, POST adds new data, PUT updates, and DELETE removes. These four operations are called CRUD for short.

**Ekranda başlık:** HTTP methods

**Ekranda maddeler:**

- GET: read
- POST: add
- PUT: update
- DELETE: remove
- CRUD: Create, Read, Update, Delete

**Maskot:** isaret pozu, sol

## Sahne 3: kod (14 sn)

**Seslendirme:** Addresses are neat and tidy: players is all players, and players slash two is player number two. When I split the address into parts with strip and split, I can read which resource and which ID is being asked for.

**Ekranda başlık:** Split the address

**Kod** (vurgulanan satırlar: 2):

```python
for path in ["/players", "/players/2", "/scores/10"]:
    parts = path.strip("/").split("/")
    print(path, "->", parts)
```

**Çıktı:**

```text
/players -> ['players']
/players/2 -> ['players', '2']
/scores/10 -> ['scores', '10']
```

**Maskot:** isaret pozu, sag

## Sahne 4: anlatim (16 sn)

**Seslendirme:** You write a real API with Flask. route picks the address and the method, jsonify turns the answer into JSON, and a status code comes along with it. Since we can't run a server here, each function will return a status code and an answer.

**Ekranda başlık:** A real API with Flask

**Kod** (vurgulanan satırlar: 5, 9):

```python
from flask import Flask, jsonify, request
app = Flask(__name__)
players = []

@app.route("/players", methods=["POST"])
def create_player():
    data = request.get_json()
    players.append(data)
    return jsonify(data), 201
```

**Maskot:** konusma pozu, sag

## Sahne 5: anlatim (14 sn)

**Seslendirme:** A good API always returns a clear status code. Two hundred one means a new record was created, two hundred four means something was deleted but there's nothing to show, and four hundred means your request was incomplete or wrong.

**Ekranda başlık:** The right status code

**Ekranda maddeler:**

- 200 OK (GET, PUT)
- 201 Created (POST)
- 204 No content (DELETE)
- 400 Bad request
- 404 Not found

**Maskot:** dusunme pozu, sol

## Sahne 6: kod (15 sn)

**Seslendirme:** Here's the POST part of our mini API. First it checks whether the body has a name; if not, it sends it back with four hundred. If it does, it gives the player a new ID, adds them, and returns two hundred one.

**Ekranda başlık:** Mini API: POST

**Kod** (vurgulanan satırlar: 4, 5, 8):

```python
players = [{"id": 1, "name": "Piko"}]

def create_player(body):
    if "name" not in body:
        return 400, {"error": "name required"}
    player = {"id": len(players) + 1, "name": body["name"]}
    players.append(player)
    return 201, player
```

**Maskot:** isaret pozu, sag

## Sahne 7: soru (9 sn)

**Seslendirme:** I send this API two requests: one with a name, and one completely empty. What do you think comes back for each?

**Ekranda başlık:** What will it print?

**Kod** (vurgulanan satırlar: 10, 11):

```python
players = [{"id": 1, "name": "Piko"}]

def create_player(body):
    if "name" not in body:
        return 400, {"error": "name required"}
    player = {"id": len(players) + 1, "name": body["name"]}
    players.append(player)
    return 201, player

print(create_player({"name": "Ece"}))
print(create_player({}))
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (11 sn)

**Seslendirme:** Ece was added with ID number two, and we got two hundred one. The empty request got four hundred, with a message saying what was missing.

**Ekranda başlık:** The answer

**Kod**:

```python
players = [{"id": 1, "name": "Piko"}]

def create_player(body):
    if "name" not in body:
        return 400, {"error": "name required"}
    player = {"id": len(players) + 1, "name": body["name"]}
    players.append(player)
    return 201, player

print(create_player({"name": "Ece"}))
print(create_player({}))
```

**Çıktı:**

```text
(201, {'id': 2, 'name': 'Ece'})
(400, {'error': 'name required'})
```

**Maskot:** mutlu pozu, sol

## Sahne 9: hata (12 sn)

**Seslendirme:** A common mistake: reading the name field directly without checking the body. If the request has no name, you get a KeyError and the API crashes. Check with in first, and return four hundred if it's missing.

**Ekranda başlık:** Common mistake: an unchecked body

**Kod** (vurgulanan satırlar: 2):

```python
def create_player(body):
    return 201, {"name": body["name"]}

print(create_player({}))
```

**Çıktı:**

```text
KeyError: 'name'
```

**Maskot:** uzgun pozu, sag

## Sahne 10: gorev (14 sn)

**Seslendirme:** In the tasks you'll write a GET that fetches one player, a POST that adds a new player, and a DELETE that removes a player. In the project you're building the score API for Piko's Adventure!

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: GET: one player
- Task 2: POST: a new player
- Task 3: DELETE: remove a player
- Challenge: Router
- Project: Game API

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** In short: the method says what to do, the address says what's wanted, and a good API answers every request with the right status code.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- GET, POST, PUT, DELETE = CRUD
- Split the address with split
- 200, 201, 204, 400, 404

**Maskot:** on pozu, sag

## Sahne 12: kapanis (13 sn)

**Seslendirme:** Now you can write your own API, incredible! Tomorrow we reach the top. We'll combine everything you learned in thirty days and write the final version of Piko's Adventure. Don't miss it!

**Ekranda başlık:** Tomorrow: The finale and beyond

**Ekranda maddeler:**

- The summit!
- The final adventure

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
