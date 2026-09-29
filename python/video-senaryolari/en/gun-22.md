# Video senaryosu: Gün 22, Web scraping

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~155 sn

Starting from the notice board of Knowledge Harbor, Piko explains the structure of HTML and how to collect titles, links and text with BeautifulSoup.

Ders metni: [gun-22.md](../../gunler/gun-22.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | sasirma (sag) |
| 2 | anlatim | 15 sn | isaret (sol) |
| 3 | kod | 17 sn | isaret (sag) |
| 4 | kod | 12 sn | isaret (sol) |
| 5 | kod | 15 sn | konusma (sag) |
| 6 | hata | 13 sn | uzgun (sol) |
| 7 | soru | 9 sn | dusunme (sag) |
| 8 | cikti | 9 sn | mutlu (sol) |
| 9 | anlatim | 15 sn | dusunme (sag) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 12 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 22: Web scraping! In this lesson you'll learn how HTML is built, and collect titles, links and text from pages with BeautifulSoup.

- HTML tags
- find and find_all
- Being a polite scraper

## Sahne 1: acilis (14 sn)

**Seslendirme:** Hi, I'm Piko! The notice board at Knowledge Harbor is full of notices: ship times, prices, lost items. Copying them all into a notebook by hand would take hours. Web pages are boards like this too. Today we learn to collect information from pages: web scraping!

**Ekranda başlık:** Day 22: Web scraping

**Ekranda maddeler:**

- Knowledge Harbor
- HTML and BeautifulSoup

**Maskot:** sasirma pozu, sag

## Sahne 2: anlatim (15 sn)

**Seslendirme:** Web pages are written in HTML. Content is marked with tags: h1 is a heading, p is a paragraph, and a is a link. class and href are the tag's attributes, and the words between the tags are the text.

**Ekranda başlık:** A quick look at HTML

**Kod** (vurgulanan satırlar: 2, 3):

```html
<h1>Title</h1>
<p class="price">25 gold</p>
<a href="/map">Go to the map</a>
```

**Maskot:** isaret pozu, sol

## Sahne 3: kod (17 sn)

**Seslendirme:** BeautifulSoup reads HTML and lets us search inside it. soup.title gets the title, find gets the first matching tag, and find_all brings them all back as a list. The .text at the end gives the words inside the tag.

**Ekranda başlık:** The title and paragraphs

**Kod** (vurgulanan satırlar: 8, 11):

```python
from bs4 import BeautifulSoup

html = """<title>Harbor Board</title>
<h1>Today's ships</h1>
<p>Seagull leaves at 10:00.</p>
<p>Dolphin arrives at 14:30.</p>"""

soup = BeautifulSoup(html, "html.parser")
print(soup.title.text)
print(soup.find("h1").text)
for p in soup.find_all("p"):
    print("-", p.text)
```

**Çıktı:**

```text
Harbor Board
Today's ships
- Seagull leaves at 10:00.
- Dolphin arrives at 14:30.
```

**Maskot:** isaret pozu, sag

## Sahne 4: kod (12 sn)

**Seslendirme:** To get an attribute's value, I treat the tag like a dictionary: href inside square brackets. Each link's text and address come out side by side.

**Ekranda başlık:** Links

**Kod** (vurgulanan satırlar: 6):

```python
from bs4 import BeautifulSoup

html = '<a href="/map">Map</a> <a href="/ships">Ships</a>'
soup = BeautifulSoup(html, "html.parser")
for a in soup.find_all("a"):
    print(a.text, "->", a["href"])
```

**Çıktı:**

```text
Map -> /map
Ships -> /ships
```

**Maskot:** isaret pozu, sol

## Sahne 5: kod (15 sn)

**Seslendirme:** I only want the prices. Since class is a special word in Python, I put an underscore after it. I turn the text I find into numbers with int and add them up.

**Ekranda başlık:** Find by class: class_

**Kod** (vurgulanan satırlar: 6):

```python
from bs4 import BeautifulSoup

html = """<li>Rope <span class="price">5</span></li>
<li>Lantern <span class="price">40</span></li>"""
soup = BeautifulSoup(html, "html.parser")
spans = soup.find_all("span", class_="price")
prices = [int(s.text) for s in spans]
print(prices, "total:", sum(prices))
```

**Çıktı:**

```text
[5, 40] total: 45
```

**Maskot:** konusma pozu, sag

## Sahne 6: hata (13 sn)

**Seslendirme:** A common mistake: searching for a tag that isn't on the page. If find doesn't find anything, it returns None. Since None has no text, you get an AttributeError. Check whether the result is None first.

**Ekranda başlık:** Common mistake: a tag that isn't there

**Kod** (vurgulanan satırlar: 4):

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup("<p>Hello</p>", "html.parser")
print(soup.find("h1").text)
```

**Çıktı:**

```text
AttributeError: 'NoneType' object has no attribute 'text'
```

**Maskot:** uzgun pozu, sol

## Sahne 7: soru (9 sn)

**Seslendirme:** Mini question! There are three paragraphs. What do you think find brings back, and how long is find_all's list?

**Ekranda başlık:** What will it print?

**Kod**:

```python
from bs4 import BeautifulSoup

html = "<p>Rope</p><p>Lantern</p><p>Map</p>"
soup = BeautifulSoup(html, "html.parser")
print(soup.find("p").text)
print(len(soup.find_all("p")))
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (9 sn)

**Seslendirme:** find brought back only the first paragraph: Rope. find_all found all three.

**Ekranda başlık:** The answer

**Kod**:

```python
from bs4 import BeautifulSoup

html = "<p>Rope</p><p>Lantern</p><p>Map</p>"
soup = BeautifulSoup(html, "html.parser")
print(soup.find("p").text)
print(len(soup.find_all("p")))
```

**Çıktı:**

```text
Rope
3
```

**Maskot:** mutlu pozu, sol

## Sahne 9: anlatim (15 sn)

**Seslendirme:** On a real site, the HTML is first downloaded from the internet with requests. But be a polite scraper: check whether the site allows it, don't flood the server with requests, and don't collect personal information. If the site offers an API, use that.

**Ekranda başlık:** Be a polite scraper

**Ekranda maddeler:**

- In real life: html = requests.get(address).text
- Terms of use and robots.txt
- Don't send requests too fast
- Don't collect personal information
- If there's an API, use it

**Maskot:** dusunme pozu, sag

## Sahne 10: gorev (13 sn)

**Seslendirme:** In the tasks you'll find a page's title, collect all its links, and add up the prices. In the project you're sorting real treasure clues from traps on an old page.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Page title
- Task 2: All the links
- Task 3: Add up the prices
- Challenge: Read the table
- Project: Treasure clues

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** In short: give the HTML to BeautifulSoup, find one with find and all with find_all, then take the text and the attributes.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- HTML: tags, attributes, text
- find, find_all, class_
- .text and tag["href"]

**Maskot:** on pozu, sag

## Sahne 12: kapanis (12 sn)

**Seslendirme:** You learned to read the board, bravo! Tomorrow we'll get our projects in order. We'll meet virtual environments, which give every project its own package cupboard. See you!

**Ekranda başlık:** Tomorrow: Virtual environments

**Ekranda maddeler:**

- venv
- Project structure

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
