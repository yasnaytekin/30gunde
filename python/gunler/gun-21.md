# Gün 21: Sınıflar ve nesneler

**Kurs:** 30 Günde Python  ·  **Bölge:** Bilgi Limanı  ·  **Maskot:** Piko

**Bugünün hedefi:** class ile kendi veri tiplerini oluşturmak: __init__, self, metotlar ve kalıtım

> Bilgi Limanı'na vardık! Limandaki tersanede gemiler tek bir çizime göre yapılıyor. Çizim bir kez hazırlanıyor, ondan istediğin kadar gemi üretiliyor ve her geminin kendi adı, kendi yükü oluyor. Python'da çizime **sınıf** (class), üretilen gemilere **nesne** (object) diyoruz.

![Bilgi Limanı](../../gorseller/python/harita/liman.webp)

## Konu anlatımı

### Sınıf ve nesne

Sınıf bir kalıptır; nesne o kalıptan yapılan şeydir. Aslında şimdiye kadar hep nesne kullandın: `"Piko"` bir `str` nesnesi, `[1, 2]` bir `list` nesnesi.

```python
class Pet:
    pass

tost = Pet()
print(type(tost))   # <class '__main__.Pet'>
```

Sınıf isimleri genellikle büyük harfle başlar: `Pet`, `Hero`, `Ship`.

### __init__ ve self

`__init__` nesne oluşturulurken **otomatik** çalışan özel bir metottur. `self`, o anda oluşturulan nesnenin kendisidir:

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50

tost = Pet("Tost")
print(tost.name)        # Tost
print(tost.happiness)   # 50
```

`self.name` gibi değişkenlere **özellik** (attribute) denir. Her nesnenin kendi özellikleri vardır.

### Metotlar

Sınıfın içindeki fonksiyonlara **metot** denir. İlk parametreleri her zaman `self`'tir:

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50

    def feed(self):
        self.happiness += 10

tost = Pet("Tost")
tost.feed()
print(tost.happiness)   # 60
```

### Kalıtım

Bir sınıf başka bir sınıfın her şeyini **miras alabilir** ve üstüne yenilerini ekleyebilir:

```python
class Hero:
    def __init__(self, name):
        self.name = name

class Wizard(Hero):
    def cast(self):
        return f"{self.name} büyü yaptı!"

w = Wizard("Merlin")
print(w.cast())
```

`Wizard`, `Hero`'nun `__init__` metodunu kendiliğinden kullanır. Kendi `__init__` metodunu yazarsan, üst sınıfınkini `super().__init__(name)` ile çağırabilirsin.

## Örnekler

### İlk sınıf

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

*İki nesne aynı kalıptan çıktı ama mutlulukları farklı.*

### Kendini tanıtan nesne

```python
class Ship:
    def __init__(self, name, cargo):
        self.name = name
        self.cargo = cargo

    def __str__(self):
        return f"{self.name} gemisi, yük: {self.cargo}"

print(Ship("Martı", 12))
```

*__str__ metodu, print() nesneyi yazdırırken ne görüneceğini belirler.*

### Kalıtım

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 100

class Wizard(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 30

    def cast(self):
        self.mana -= 10
        return f"{self.name} büyü yaptı, mana {self.mana}"

w = Wizard("Merlin")
print(w.hp)
print(w.cast())
```

## Görevler

### Görev 1: Evcil hayvan

`Pet` sınıfı `name` alsın ve `happiness` 50 ile başlasın. `feed()` metodu mutluluğu 10 artırsın.

**Başlangıç kodu:**

```python
class Pet:
    def __init__(self, name):
        pass

    def feed(self):
        pass

tost = Pet("Tost")
tost.feed()
print(tost.name, tost.happiness)
```

**İpuçları:**

1. __init__ içinde: self.name = name ve self.happiness = 50
2. feed içinde: self.happiness += 10

<details><summary>Çözüm</summary>

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50

    def feed(self):
        self.happiness += 10

tost = Pet("Tost")
tost.feed()
print(tost.name, tost.happiness)
```

</details>

### Görev 2: Cüzdan

`Wallet` sınıfında `balance` 0 ile başlasın. `add(amount)` parayı eklesin. `spend(amount)` yeterli para varsa harcayıp `True`, yoksa hiçbir şey değiştirmeden `False` döndürsün.

**Başlangıç kodu:**

```python
class Wallet:
    def __init__(self):
        self.balance = 0

    def add(self, amount):
        pass

    def spend(self, amount):
        pass

w = Wallet()
w.add(30)
print(w.spend(20), w.balance)
```

**İpuçları:**

1. add içinde: self.balance += amount
2. spend içinde önce yeterli para var mı bak: if amount > self.balance: return False

<details><summary>Çözüm</summary>

```python
class Wallet:
    def __init__(self):
        self.balance = 0

    def add(self, amount):
        self.balance += amount

    def spend(self, amount):
        if amount > self.balance:
            return False
        self.balance -= amount
        return True

w = Wallet()
w.add(30)
print(w.spend(20), w.balance)
```

</details>

### Görev 3: Kendini tanıt

`Hero` sınıfına `introduce()` metodu ekle. `Ben Piko, canım 100!` gibi bir yazı **döndürsün**.

**Başlangıç kodu:**

```python
class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

h = Hero("Piko", 100)
print(h.introduce())
```

**İpuçları:**

1. Metodun ilk parametresi self olmalı: def introduce(self):
2. return f"Ben {self.name}, canım {self.hp}!"

<details><summary>Çözüm</summary>

```python
class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def introduce(self):
        return f"Ben {self.name}, canım {self.hp}!"

h = Hero("Piko", 100)
print(h.introduce())
```

</details>

## Challenge: Büyücü

`Hero`'dan kalıtım alan `Wizard` sınıfı yaz. Büyücünün `mana`'sı 30 ile başlasın. `cast()` metodu yeterli mana varsa 10 mana harcayıp `True`, yoksa `False` döndürsün.

**Başlangıç kodu:**

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 100

# Wizard sınıfını yaz

w = Wizard("Merlin")
print(w.cast(), w.mana)
```

**İpuçları:**

1. class Wizard(Hero):
2. Kendi __init__ içinde önce super().__init__(name) çağır, sonra self.mana = 30

<details><summary>Çözüm</summary>

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.hp = 100

class Wizard(Hero):
    def __init__(self, name):
        super().__init__(name)
        self.mana = 30

    def cast(self):
        if self.mana < 10:
            return False
        self.mana -= 10
        return True

w = Wizard("Merlin")
print(w.cast(), w.mana)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Karakter sınıfları**

### Piko'nun Macerası: Karakter sınıfları

Maceranın karakterlerini sınıflarla yazalım. `Character` sınıfı `name`, `hp` ve `power` alsın:

- `attack(other)`: diğer karakterin canını kendi gücü kadar azaltsın.
- `is_alive()`: can 0'dan büyükse `True` döndürsün.

**Başlangıç kodu:**

```python
class Character:
    def __init__(self, name, hp, power):
        pass

    def attack(self, other):
        pass

    def is_alive(self):
        pass

piko = Character("Piko", 30, 8)
bat = Character("Yarasa", 12, 3)
piko.attack(bat)
print(bat.hp, bat.is_alive())
```

**İpuçları:**

1. __init__ içinde üç özelliği de self'e kaydet.
2. attack içinde: other.hp -= self.power
3. is_alive içinde: return self.hp > 0

<details><summary>Çözüm</summary>

```python
class Character:
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    def attack(self, other):
        other.hp -= self.power

    def is_alive(self):
        return self.hp > 0

piko = Character("Piko", 30, 8)
bat = Character("Yarasa", 12, 3)
piko.attack(bat)
print(bat.hp, bat.is_alive())
```

</details>

### Harcama Defteri: Budget sınıfı

Defteri bir sınıfla yazalım. `Budget` sınıfı `limit` alsın ve boş bir `expenses` listesiyle başlasın:

- `add(category, amount)`: `(category, amount)` tuple'ını listeye eklesin.
- `total()`: harcamaların toplamını döndürsün.
- `remaining()`: `limit - total()` döndürsün.

**Başlangıç kodu:**

```python
class Budget:
    def __init__(self, limit):
        pass
```

**İpuçları:**

1. __init__ içinde self.limit = limit ve self.expenses = []
2. total içinde: sum(amount for category, amount in self.expenses)

<details><summary>Çözüm</summary>

```python
class Budget:
    def __init__(self, limit):
        self.limit = limit
        self.expenses = []

    def add(self, category, amount):
        self.expenses.append((category, amount))

    def total(self):
        return sum(amount for category, amount in self.expenses)

    def remaining(self):
        return self.limit - self.total()
```

</details>

### Görev Asistanı: Task ve TaskList

Görevleri sınıflarla yazalım:

- `Task(title, priority=2)`: `title`, `priority` ve `False` ile başlayan `done` özellikleri olsun. `complete()` metodu `done`'ı `True` yapsın.
- `TaskList`: boş bir `tasks` listesiyle başlasın. `add(task)` görevi eklesin, `pending()` bitmemiş görevlerin **başlıklarını** liste olarak döndürsün.

**Başlangıç kodu:**

```python
class Task:
    pass


class TaskList:
    pass
```

**İpuçları:**

1. def __init__(self, title, priority=2): varsayılan değer verir.
2. pending içinde: [t.title for t in self.tasks if not t.done]

<details><summary>Çözüm</summary>

```python
class Task:
    def __init__(self, title, priority=2):
        self.title = title
        self.priority = priority
        self.done = False

    def complete(self):
        self.done = True


class TaskList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append(task)

    def pending(self):
        return [t.title for t in self.tasks if not t.done]
```

</details>

### Kişisel Web Sitem: Post ve Site sınıfları

Sitenin iki sınıfını yazalım:

- `Post(title, text)`: `title`, `text` ve `slug` (başlığın küçük harfli, boşlukları `-` olan hâli) özellikleri olsun. `word_count()` metodu yazının kelime sayısını döndürsün.
- `Site(title)`: `title` ve boş bir `posts` listesiyle başlasın. `add(post)` bir yazıyı listeye eklesin, `total_words()` bütün yazıların kelime sayılarının toplamını döndürsün.

**Başlangıç kodu:**

```python
class Post:
    def __init__(self, title, text):
        pass


class Site:
    def __init__(self, title):
        pass
```

**İpuçları:**

1. Post'un __init__'inde: self.slug = title.lower().replace(" ", "-")
2. total_words içinde: sum(post.word_count() for post in self.posts)

<details><summary>Çözüm</summary>

```python
class Post:
    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.slug = title.lower().replace(" ", "-")

    def word_count(self):
        return len(self.text.split())


class Site:
    def __init__(self, title):
        self.title = title
        self.posts = []

    def add(self, post):
        self.posts.append(post)

    def total_words(self):
        return sum(post.word_count() for post in self.posts)
```

</details>

### Sohbet Botu: Bot ve Message

Botu sınıflarla yazalım:

- `Message(sender, text)`: `sender` ve `text` özellikleri olsun. `show()` metodu `"Bilge: Merhaba!"` gibi `gönderen: metin` yazısını döndürsün.
- `Bot(name)`: `name`, boş bir `replies` sözlüğü ve boş bir `history` listesiyle başlasın.
  - `learn(keyword, reply)`: sözlüğe `keyword -> reply` eklesin.
  - `answer(text)`: `text` içinde geçen ilk anahtar kelimenin cevabını, hiçbiri geçmiyorsa `"Bunu henüz bilmiyorum."` döndürsün. Ayrıca `history` listesine önce `Message("Sen", text)`, sonra `Message(name, cevap)` eklesin.

**Başlangıç kodu:**

```python
class Message:
    pass


class Bot:
    pass
```

**İpuçları:**

1. Bot'un __init__'inde: self.name = name, self.replies = {}, self.history = []
2. answer içinde for keyword in self.replies: ile anahtar kelimelere bak, sonra iki Message ekle.

<details><summary>Çözüm</summary>

```python
class Message:
    def __init__(self, sender, text):
        self.sender = sender
        self.text = text

    def show(self):
        return f"{self.sender}: {self.text}"


class Bot:
    def __init__(self, name):
        self.name = name
        self.replies = {}
        self.history = []

    def learn(self, keyword, reply):
        self.replies[keyword] = reply

    def answer(self, text):
        reply = "Bunu henüz bilmiyorum."
        for keyword in self.replies:
            if keyword in text:
                reply = self.replies[keyword]
                break
        self.history.append(Message("Sen", text))
        self.history.append(Message(self.name, reply))
        return reply
```

</details>

### Okul Not Defteri: Course sınıfı

Dersleri bir sınıfla yazalım. `Course(name, hours)` bir ders adı ve haftalık ders saati alsın ve boş bir `grades` listesiyle başlasın:

- `add_grade(grade)`: notu listeye eklesin.
- `average()`: notların ortalamasını 2 basamağa yuvarlayıp döndürsün; hiç not yoksa `0`.
- `passed()`: ortalama 50 veya üstüyse `True` döndürsün.

**Başlangıç kodu:**

```python
class Course:
    def __init__(self, name, hours):
        pass
```

**İpuçları:**

1. __init__ içinde self.name = name, self.hours = hours ve self.grades = []
2. passed içinde: return self.average() >= 50

<details><summary>Çözüm</summary>

```python
class Course:
    def __init__(self, name, hours):
        self.name = name
        self.hours = hours
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average(self):
        if len(self.grades) == 0:
            return 0
        return round(sum(self.grades) / len(self.grades), 2)

    def passed(self):
        return self.average() >= 50
```

</details>
