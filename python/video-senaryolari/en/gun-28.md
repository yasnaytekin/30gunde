# Video senaryosu: Gün 28, Using APIs

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~148 sn

With the radio in the camp house on Python Mountain, Piko explains APIs: opening JSON responses with json.loads, sending with json.dumps, status codes, and nested data.

Ders metni: [gun-28.md](../../gunler/gun-28.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 15 sn | konusma (sag) |
| 2 | anlatim | 14 sn | isaret (sol) |
| 3 | kod | 16 sn | isaret (sag) |
| 4 | kod | 14 sn | isaret (sol) |
| 5 | anlatim | 17 sn | konusma (sag) |
| 6 | soru | 11 sn | dusunme (sag) |
| 7 | cikti | 12 sn | mutlu (sol) |
| 8 | hata | 12 sn | sasirma (sag) |
| 9 | gorev | 13 sn | konusma (sag) |
| 10 | ozet | 11 sn | on (sag) |
| 11 | kapanis | 13 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 28: Using APIs! In this lesson you'll learn what an API is, open JSON responses, check status codes, and find your way through nested data.

- What is an API?
- json.loads and json.dumps
- Status codes and nested data

## Sahne 1: acilis (15 sn)

**Seslendirme:** Hi, I'm Piko! In the camp house halfway up Python Mountain, there's a radio. I call the weather station: what's the weather like at the top? The station gives a short, tidy answer. Programs talk to each other like this too. These rules are called an API!

**Ekranda başlık:** Day 28: Using APIs

**Ekranda maddeler:**

- Python Mountain
- APIs, JSON, status codes

**Maskot:** konusma pozu, sag

## Sahne 2: anlatim (14 sn)

**Seslendirme:** An API is the set of rules for one program to ask another program for information. Think of a restaurant: you don't go into the kitchen, you order from the waiter, and the waiter brings your food. The API is that waiter.

**Ekranda başlık:** What is an API?

**Ekranda maddeler:**

- You → the waiter (API) → the kitchen (server)
- Weather, exchange rates, game scores

**Maskot:** isaret pozu, sol

## Sahne 3: kod (16 sn)

**Seslendirme:** APIs usually answer with JSON. JSON looks like a dictionary, but it's really text. json.loads turns it into a real dictionary. And the lowercase true in JSON becomes a capital True in Python.

**Ekranda başlık:** Open the JSON: json.loads

**Kod** (vurgulanan satırlar: 4, 7):

```python
import json

response = '{"city": "Izmir", "degrees": 27, "sunny": true}'
data = json.loads(response)
print(type(data))
print(f"{data['city']}: {data['degrees']} degrees")
print("Sunny?", data["sunny"])
```

**Çıktı:**

```text
<class 'dict'>
Izmir: 27 degrees
Sunny? True
```

**Maskot:** isaret pozu, sag

## Sahne 4: kod (14 sn)

**Seslendirme:** It works the other way too: json.dumps turns a dictionary into JSON text, which you need when sending data to an API. In the first line, the é turned into an escape code. With ensure_ascii False, accented letters stay just as they are.

**Ekranda başlık:** From a dictionary to JSON: json.dumps

**Kod** (vurgulanan satırlar: 4, 5):

```python
import json

order = {"item": "lantern", "count": 2, "note": "Café"}
print(json.dumps(order))
print(json.dumps(order, ensure_ascii=False))
```

**Çıktı:**

```text
{"item": "lantern", "count": 2, "note": "Caf\u00e9"}
{"item": "lantern", "count": 2, "note": "Café"}
```

**Maskot:** isaret pozu, sol

## Sahne 5: anlatim (17 sn)

**Seslendirme:** On your own computer, you use the requests package to get data from the internet. First you check the status code: if it's two hundred, everything is fine, and you open the answer with json. If not, you show the error. On our site we can't reach the internet, so the answers will come ready-made.

**Ekranda başlık:** A request with requests (on your computer)

**Kod** (vurgulanan satırlar: 4):

```python
import requests

r = requests.get("https://api.example.com/weather?city=izmir")
if r.status_code == 200:
    data = r.json()
    print(data["degrees"])
else:
    print("Error:", r.status_code)
```

**Çıktı:**

```text
27
```

**Maskot:** konusma pozu, sag

## Sahne 6: soru (11 sn)

**Seslendirme:** Real answers are often nested: a list inside a dictionary, a dictionary inside a list. Which number do you think this line prints?

**Ekranda başlık:** What will it print?

**Kod** (vurgulanan satırlar: 5):

```python
import json

response = '{"city": "Van", "days": [{"day": "Mon", "degrees": 18}, {"day": "Tue", "degrees": 21}]}'
data = json.loads(response)
print(data["days"][1]["degrees"])
```

**Maskot:** dusunme pozu, sag

## Sahne 7: cikti (12 sn)

**Seslendirme:** Twenty-one! We went down step by step: first the days list, then item number one, which is Tuesday, and finally the degrees. Remember, counting starts at zero.

**Ekranda başlık:** The answer: go down step by step

**Ekranda maddeler:**

- data["days"] → a list
- [1] → Tuesday
- ["degrees"] → 21

**Kod**:

```python
import json

response = '{"city": "Van", "days": [{"day": "Mon", "degrees": 18}, {"day": "Tue", "degrees": 21}]}'
data = json.loads(response)
print(data["days"][1]["degrees"])
```

**Çıktı:**

```text
21
```

**Maskot:** mutlu pozu, sol

## Sahne 8: hata (12 sn)

**Seslendirme:** A common mistake: using JSON text like a dictionary without opening it. response is still text, and you can't reach into text with a key, so you get a TypeError. Open it with json.loads first!

**Ekranda başlık:** Common mistake: unopened JSON

**Kod** (vurgulanan satırlar: 2):

```python
response = '{"city": "Izmir", "degrees": 27}'
print(response["degrees"])
```

**Çıktı:**

```text
TypeError: string indices must be integers, not 'str'
```

**Maskot:** sasirma pozu, sag

## Sahne 9: gorev (13 sn)

**Seslendirme:** In the tasks you'll open a weather response, collect the names from a country list, and print the right message based on the status code. In the project you're pulling the open tasks from the task service.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Weather
- Task 2: Country list
- Task 3: Status check
- Challenge: Send an order
- Project: Task service

**Maskot:** konusma pozu, sag

## Sahne 10: ozet (11 sn)

**Seslendirme:** In short: an API is the rulebook programs use to talk. Open the answer with json.loads, check the status code, and go down nested data step by step.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- API = the waiter between programs
- json.loads and json.dumps
- First status_code, then the data

**Maskot:** on pozu, sag

## Sahne 11: kapanis (13 sn)

**Seslendirme:** You used the radio like a pro! Tomorrow we switch roles: we'll be the station that answers the questions. We'll write our own API with GET, POST, PUT and DELETE. See you!

**Ekranda başlık:** Tomorrow: Building APIs

**Ekranda maddeler:**

- Your own API
- GET, POST, PUT, DELETE

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
