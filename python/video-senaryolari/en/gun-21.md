# Video senaryosu: Gün 21, Classes and objects

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~152 sn

In the shipyard of Knowledge Harbor, Piko explains building blueprints with class, and making objects with __init__, self, methods, __str__ and inheritance.

Ders metni: [gun-21.md](../../gunler/gun-21.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 16 sn | mutlu (sag) |
| 2 | kod | 13 sn | isaret (sag) |
| 3 | kod | 16 sn | isaret (sol) |
| 4 | anlatim | 10 sn | konusma (sag) |
| 5 | soru | 10 sn | dusunme (sag) |
| 6 | cikti | 10 sn | mutlu (sol) |
| 7 | kod | 12 sn | isaret (sag) |
| 8 | kod | 17 sn | isaret (sol) |
| 9 | hata | 12 sn | sasirma (sag) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 12 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Day 21: Classes and objects! In this lesson you'll build your own data types with class, and learn __init__, self, methods and inheritance.

- class and objects
- __init__ and self
- Methods and inheritance

## Sahne 1: acilis (16 sn)

**Seslendirme:** Hi, I'm Piko! We've reached Knowledge Harbor! In the shipyard, ships are built from a single blueprint. The blueprint is drawn once, and you can build as many ships from it as you like. In Python, the blueprint is called a class, and the ships built from it are objects.

**Ekranda başlık:** Day 21: Classes and objects

**Ekranda maddeler:**

- New region: Knowledge Harbor
- class, __init__, self, methods, inheritance

**Maskot:** mutlu pozu, sag

## Sahne 2: kod (13 sn)

**Seslendirme:** You've actually been using objects all along: the text Piko is a str object. I build my own class with class, and its name starts with a capital letter. Call it with parentheses, and an object comes out of that blueprint.

**Ekranda başlık:** Classes and objects

**Kod** (vurgulanan satırlar: 1, 4):

```python
class Pet:
    pass

tost = Pet()
print(type(tost))
print(type("Piko"))
```

**Çıktı:**

```text
<class '__main__.Pet'>
<class 'str'>
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (16 sn)

**Seslendirme:** __init__ is a special method that runs by itself when an object is created. self is the object being made right then. self.name and self.happiness become that object's attributes, and every object has its own.

**Ekranda başlık:** __init__ and self

**Kod** (vurgulanan satırlar: 2, 3, 4):

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50

tost = Pet("Tost")
print(tost.name)
print(tost.happiness)
```

**Çıktı:**

```text
Tost
50
```

**Maskot:** isaret pozu, sol

## Sahne 4: anlatim (10 sn)

**Seslendirme:** Functions inside a class are called methods. Their first parameter is always self. That way, the method knows which object's attributes to change.

**Ekranda başlık:** Methods

**Kod** (vurgulanan satırlar: 6, 7):

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50

    def feed(self):
        self.happiness += 10
```

**Maskot:** konusma pozu, sag

## Sahne 5: soru (10 sn)

**Seslendirme:** I made two pets from the same blueprint and fed only Tost, twice. Which happiness values do you think show up on the screen?

**Ekranda başlık:** What will it print?

**Kod** (vurgulanan satırlar: 11, 12):

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50

    def feed(self):
        self.happiness += 10

tost = Pet("Tost")
misket = Pet("Misket")
tost.feed()
tost.feed()
print(tost.name, tost.happiness)
print(misket.name, misket.happiness)
```

**Maskot:** dusunme pozu, sag

## Sahne 6: cikti (10 sn)

**Seslendirme:** Tost went up to seventy, and Misket stayed at fifty. The two objects came from the same blueprint, but each one keeps its own attributes.

**Ekranda başlık:** The answer

**Kod**:

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50

    def feed(self):
        self.happiness += 10

tost = Pet("Tost")
misket = Pet("Misket")
tost.feed()
tost.feed()
print(tost.name, tost.happiness)
print(misket.name, misket.happiness)
```

**Çıktı:**

```text
Tost 70
Misket 50
```

**Maskot:** mutlu pozu, sol

## Sahne 7: kod (12 sn)

**Seslendirme:** The __str__ method decides what shows up when print prints an object. That way, the ship introduces itself with a nice sentence.

**Ekranda başlık:** An object that introduces itself

**Kod** (vurgulanan satırlar: 6, 7):

```python
class Ship:
    def __init__(self, name, cargo):
        self.name = name
        self.cargo = cargo

    def __str__(self):
        return f"The {self.name}, cargo: {self.cargo}"

print(Ship("Seagull", 12))
```

**Çıktı:**

```text
The Seagull, cargo: 12
```

**Maskot:** isaret pozu, sag

## Sahne 8: kod (17 sn)

**Seslendirme:** With inheritance, one class inherits everything from another class. Wizard comes from Hero; it doesn't even have its own __init__, but it knows its name. On top of that, it adds a cast method. If you write your own __init__, you call the parent's with super.

**Ekranda başlık:** Inheritance

**Ekranda maddeler:**

- If you write your own __init__: super().__init__(name)

**Kod** (vurgulanan satırlar: 5, 6):

```python
class Hero:
    def __init__(self, name):
        self.name = name

class Wizard(Hero):
    def cast(self):
        return f"{self.name} cast a spell!"

w = Wizard("Merlin")
print(w.cast())
```

**Çıktı:**

```text
Merlin cast a spell!
```

**Maskot:** isaret pozu, sol

## Sahne 9: hata (12 sn)

**Seslendirme:** The most common mistake is forgetting self in a method. Python secretly sends the object as the first piece of information, but the method doesn't expect any parameters. The result is a TypeError!

**Ekranda başlık:** Common mistake: forgetting self

**Kod** (vurgulanan satırlar: 2):

```python
class Pet:
    def feed():
        print("Ate the food")

Pet().feed()
```

**Çıktı:**

```text
TypeError: Pet.feed() takes 0 positional arguments but 1 was given
```

**Maskot:** sasirma pozu, sag

## Sahne 10: gorev (13 sn)

**Seslendirme:** In the tasks you'll write a pet class, a wallet that spends money, and a hero that introduces itself. In the project, the adventure's characters will be able to attack each other.

**Ekranda başlık:** Today's tasks

**Ekranda maddeler:**

- Task 1: Pet
- Task 2: Wallet
- Task 3: Introduce yourself
- Challenge: Wizard
- Project: Character classes

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** In short: a class is the blueprint, and an object is what comes out of it. __init__ sets it up, methods do the work, and inheritance passes everything down.

**Ekranda başlık:** What you learned today

**Ekranda maddeler:**

- class is the blueprint, Pet() makes an object
- Attributes with __init__ and self
- Methods and inheritance (super)

**Maskot:** on pozu, sag

## Sahne 12: kapanis (12 sn)

**Seslendirme:** You've mastered the shipyard! Tomorrow we go to the harbor's notice board. We'll learn to collect titles, links and text from web pages: web scraping. See you!

**Ekranda başlık:** Tomorrow: Web scraping

**Ekranda maddeler:**

- HTML tags
- BeautifulSoup

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** The interactive version of this lesson is waiting for you at 30gunde.com.tr. Write your code right in the browser, run it instantly, and finish the tasks!

**Ekranda:** Interactive lessons at **30gunde.com.tr**

- Write and run code in your browser
- Finish tasks, earn badges
- Learn Python step by step in 30 days
