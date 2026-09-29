# Video senaryosu: Gün 26, The web with Python

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~157 sn

From the watchtower on Python Mountain, Piko explains how the web runs on requests and responses, status codes, generating HTML with Python, and routing with a dictionary.

Ders metni: [gun-26.md](../../gunler/gun-26.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 15 sn | mutlu (sag) |
| 2 | anlatim | 16 sn | isaret (sol) |
| 3 | kod | 12 sn | mutlu (sag) |
| 4 | anlatim | 17 sn | konusma (sag) |
| 5 | kod | 16 sn | isaret (sol) |
| 6 | anlatim | 12 sn | konusma (sag) |
| 7 | soru | 10 sn | dusunme (sag) |
| 8 | cikti | 11 sn | mutlu (sol) |
| 9 | hata | 12 sn | uzgun (sag) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 12 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 26: The web with Python! In this lesson you'll learn how the web works with requests and responses, status codes, generating HTML with Python, and routing.

- Request, response, status code
- Generating HTML with Python
- Routing with a dictionary

## Sahne 1: acilis (15 sn)

**Seslendirme:** Hi, I'm Piko! We've reached the last region, the foot of Python Mountain! At the top stands a giant watchtower, and it receives messages from all over the world. Every message is a request, and every answer from the tower is a response. Websites work exactly like this!

**Ekranda başlık:** Day 26: The web with Python

**Ekranda maddeler:**

- New region: Python Mountain
- Requests, responses, generating HTML

**Maskot:** mutlu pozu, sag

## Sahne 2: anlatim (16 sn)

**Seslendirme:** When you type an address into your browser, the browser sends a request to the server: give me the profile page. The server prepares the page and sends back a response. The response has HTML and a status code.

**Ekranda başlık:** Requests and responses

**Ekranda maddeler:**

- Browser → request: GET /profile
- Server → response: HTML + status code
- 200 OK, 404 not found, 500 server error

**Maskot:** isaret pozu, sol

## Sahne 3: kod (12 sn)

**Seslendirme:** I keep the status codes in a dictionary. When I ask with get, if a code isn't in the dictionary, it says Unknown. Four hundred eighteen really exists: it means I'm a teapot!

**Ekranda başlık:** Status codes

**Kod** (vurgulanan satırlar: 3):

```python
codes = {200: "OK", 404: "Not found", 500: "Server error"}
for code in [200, 404, 500, 418]:
    print(code, codes.get(code, "Unknown"))
```

**Çıktı:**

```text
200 OK
404 Not found
500 Server error
418 Unknown
```

**Maskot:** mutlu pozu, sag

## Sahne 4: anlatim (17 sn)

**Seslendirme:** One of the favorite ways to build a website in Python is Flask. The route line says: if someone asks for the main address, run the home function. We can't start a server on our site, so we'll try the same idea with plain Python.

**Ekranda başlık:** A site with Flask (on your computer)

**Kod** (vurgulanan satırlar: 4):

```python
from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Piko's site!</h1>"

app.run()
```

**Maskot:** konusma pozu, sag

## Sahne 5: kod (16 sn)

**Seslendirme:** A server's real job is to produce HTML text from data. I build the heading with an f-string. Then I turn each item in the list into an li tag and join them together. Here's the page that will go to the browser!

**Ekranda başlık:** Generating HTML

**Kod** (vurgulanan satırlar: 4, 5):

```python
name = "Piko"
items = ["sword", "potion", "map"]

page = f"<h1>{name}'s bag</h1>"
page += "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
print(page)
```

**Çıktı:**

```text
<h1>Piko's bag</h1><ul><li>sword</li><li>potion</li><li>map</li></ul>
```

**Maskot:** isaret pozu, sol

## Sahne 6: anlatim (12 sn)

**Seslendirme:** Deciding which address goes to which function is called routing. We can set it up with a dictionary: the key is the address, and the value is the function that makes that page.

**Ekranda başlık:** Routing

**Kod** (vurgulanan satırlar: 7):

```python
def home():
    return "<h1>Home</h1>"

def about():
    return "<h1>About</h1>"

routes = {"/": home, "/about": about}
```

**Maskot:** konusma pozu, sag

## Sahne 7: soru (10 sn)

**Seslendirme:** I try three addresses: home, about and secret. What happens when an address that isn't in the dictionary comes in? What do you think we'll see on the screen?

**Ekranda başlık:** What will it print?

**Kod** (vurgulanan satırlar: 10, 11):

```python
def home():
    return "<h1>Home</h1>"

def about():
    return "<h1>About</h1>"

routes = {"/": home, "/about": about}

for path in ["/", "/about", "/secret"]:
    view = routes.get(path)
    print(path, "->", view() if view else "404 Not found")
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (11 sn)

**Seslendirme:** The first two addresses brought back their own pages. Secret isn't in the dictionary, so get gave None, and we showed four hundred four, Not found. Flask does this for you.

**Ekranda başlık:** The answer: mini routing

**Kod**:

```python
def home():
    return "<h1>Home</h1>"

def about():
    return "<h1>About</h1>"

routes = {"/": home, "/about": about}

for path in ["/", "/about", "/secret"]:
    view = routes.get(path)
    print(path, "->", view() if view else "404 Not found")
```

**Çıktı:**

```text
/ -> <h1>Home</h1>
/about -> <h1>About</h1>
/secret -> 404 Not found
```

**Maskot:** mutlu pozu, sol

## Sahne 9: hata (12 sn)

**Seslendirme:** A common mistake: asking for an address that isn't in the dictionary directly with square brackets. Python gives a KeyError and the server crashes. Use get, and return four hundred four for addresses that don't exist.

**Ekranda başlık:** Common mistake: an address that doesn't exist

**Kod** (vurgulanan satırlar: 2):

```python
routes = {"/": "Home"}
print(routes["/secret"])
```

**Çıktı:**

```text
KeyError: '/secret'
```

**Maskot:** uzgun pozu, sag

## Sahne 10: gorev (13 sn)

**Seslendirme:** In the tasks you'll produce a welcome page and a list page, and write a function that turns status codes into words. In the project you're building Piko's profile page.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Welcome page
- Task 2: List page
- Task 3: Status code
- Challenge: Mini server
- Project: The game's web page

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** In short: the web runs on requests and responses, the server turns data into HTML, and routing sends each address to the right function.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- Requests, responses and status codes
- HTML with f-strings and join
- Routing with a dictionary, otherwise 404

**Maskot:** on pozu, sag

## Sahne 12: kapanis (12 sn)

**Seslendirme:** You answered the tower's first messages, congratulations! Tomorrow we go down to the mountain's archive. We'll explore MongoDB, a document database, and the insert, find and update operations. See you!

**Ekranda başlık:** Tomorrow: Python and MongoDB

**Ekranda maddeler:**

- A document database
- insert, find, update

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
