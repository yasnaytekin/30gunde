# Gün 27: Python ve MongoDB

**Kurs:** 30 Günde Python  ·  **Bölge:** Python Dağı  ·  **Maskot:** Piko

**Bugünün hedefi:** Belge tabanlı veritabanı fikrini öğrenmek: MongoDB'deki insert, find ve update işlemlerini Python ile canlandırmak

> Dağın yamacındaki kütüphanede her oyuncunun bir dosyası var. Kütüphaneci bir isim söylediğinde saniyeler içinde doğru dosyayı buluyor, yeni oyuncular için dosya açıyor, seviyesi artanları güncelliyor. Bilgisayar dünyasında bu kütüphanecinin adı **veritabanı**. Bugün MongoDB'nin nasıl düşündüğünü öğreniyoruz.

![Python Dağı](../../gorseller/python/harita/dag.webp)

## Konu anlatımı

### Veritabanı nedir?

Programlar kapanınca değişkenlerdeki bilgiler kaybolur. Dosyaya yazmak küçük işler için yeter ama binlerce oyuncunun verisini hızlıca aramak, güncellemek ve güvende tutmak için **veritabanı** kullanılır.

MongoDB bir **belge veritabanıdır**. Her kayıt bir Python sözlüğüne çok benzeyen bir **belgedir** (document). Belgeler **koleksiyonlarda** (collection) toplanır:

```python
{"name": "Piko", "level": 3, "items": ["kılıç"]}
```

### pymongo ile gerçek MongoDB

Kendi bilgisayarında `pymongo` paketiyle şöyle çalışırsın:

```python
from pymongo import MongoClient
client = MongoClient("mongodb://localhost:27017")
db = client["oyun"]

db.players.insert_one({"name": "Piko", "level": 3})
for p in db.players.find({"level": 3}):
    print(p["name"])
db.players.update_one({"name": "Piko"}, {"$set": {"level": 4}})
db.players.delete_one({"name": "Piko"})
```

Bu sitede gerçek bir veritabanına bağlanamıyoruz. Onun yerine koleksiyonu bir **sözlük listesi** olarak tutup aynı işlemleri kendimiz yazacağız. Böylece MongoDB'nin içinde neler olduğunu da anlamış olacağız.

### Sorgu (query) nedir?

`find({"level": 3})` şunu der: "`level` alanı 3 olan tüm belgeleri getir." Sorgu da bir sözlüktür ve belgenin **tüm** alanları sorgudaki değerlerle eşleşmelidir.

Boş sorgu `{}` tüm belgeleri getirir. MongoDB'de `{"level": {"$gt": 3}}` gibi özel işaretler de vardır: `$gt` büyüktür, `$lt` küçüktür demektir.

### all() ile hepsi mi?

Bir koşulun **hepsi** için doğru olup olmadığını `all()` hızlıca söyler:

```python
doc = {"name": "Piko", "level": 3}
query = {"level": 3, "name": "Piko"}
print(all(doc.get(k) == v for k, v in query.items()))   # True
```

Tersine, en az birinin doğru olmasını `any()` kontrol eder.

## Örnekler

### Koleksiyon ve belgeler

```python
players = [
    {"name": "Piko", "level": 3},
    {"name": "Ece", "level": 5},
]
players.append({"name": "Can", "level": 1})
for p in players:
    print(p["name"], "seviye", p["level"])
```

### Sorguya uyuyor mu?

```python
doc = {"name": "Piko", "level": 3, "club": "mavi"}
for query in [{"level": 3}, {"level": 3, "club": "mavi"}, {"level": 4}, {}]:
    ok = all(doc.get(k) == v for k, v in query.items())
    print(query, "->", ok)
```

*Boş sorgu her belgeye uyar.*

### Güncelleme

```python
players = [{"name": "Piko", "level": 3}, {"name": "Ece", "level": 5}]
for p in players:
    if p["name"] == "Piko":
        p.update({"level": 4})
        break
print(players)
```

## Görevler

### Görev 1: insert_one

`insert_one(collection, doc)` belgeyi koleksiyonun sonuna eklesin. Sonra `players` koleksiyonuna `{"name": "Ece", "level": 5}` belgesini ekle.

**Başlangıç kodu:**

```python
def insert_one(collection, doc):
    pass

players = [{"name": "Piko", "level": 3}]

# Ece'yi ekle

print(players)
```

**İpuçları:**

1. insert_one içinde: collection.append(doc)
2. insert_one(players, {"name": "Ece", "level": 5})

<details><summary>Çözüm</summary>

```python
def insert_one(collection, doc):
    collection.append(doc)

players = [{"name": "Piko", "level": 3}]

insert_one(players, {"name": "Ece", "level": 5})

print(players)
```

</details>

### Görev 2: find

`find(collection, query)` sorgudaki **tüm** alanları eşleşen belgelerin listesini döndürsün. Boş sorgu hepsini getirsin.

**Başlangıç kodu:**

```python
def find(collection, query):
    return []

players = [
    {"name": "Piko", "level": 3, "club": "mavi"},
    {"name": "Ece", "level": 5, "club": "mavi"},
    {"name": "Can", "level": 3, "club": "sarı"},
]
print(find(players, {"level": 3}))
```

**İpuçları:**

1. Her belge için sorgunun tüm alanlarını kontrol et: all(doc.get(k) == v for k, v in query.items())
2. Uyanları bir listeye topla.

<details><summary>Çözüm</summary>

```python
def find(collection, query):
    return [doc for doc in collection if all(doc.get(k) == v for k, v in query.items())]

players = [
    {"name": "Piko", "level": 3, "club": "mavi"},
    {"name": "Ece", "level": 5, "club": "mavi"},
    {"name": "Can", "level": 3, "club": "sarı"},
]
print(find(players, {"level": 3}))
```

</details>

### Görev 3: update_one

`update_one(collection, query, changes)` sorguya uyan **ilk** belgeyi `changes` sözlüğüyle güncellesin ve `True` döndürsün. Hiç belge uymazsa `False` döndürsün.

**Başlangıç kodu:**

```python
def update_one(collection, query, changes):
    return False

players = [{"name": "Piko", "level": 3}, {"name": "Ece", "level": 5}]
print(update_one(players, {"name": "Piko"}, {"level": 4}))
print(players)
```

**İpuçları:**

1. Belgeleri dolaş, ilk uyanı bulunca doc.update(changes) yap ve return True
2. Döngü bitince return False

<details><summary>Çözüm</summary>

```python
def update_one(collection, query, changes):
    for doc in collection:
        if all(doc.get(k) == v for k, v in query.items()):
            doc.update(changes)
            return True
    return False

players = [{"name": "Piko", "level": 3}, {"name": "Ece", "level": 5}]
print(update_one(players, {"name": "Piko"}, {"level": 4}))
print(players)
```

</details>

## Challenge: $gt işareti

`find` fonksiyonunu geliştir: sorgudaki değer `{"$gt": 3}` gibi bir sözlükse, belgedeki değer ondan **büyük** olmalı. Diğer değerlerde eşitlik kontrolü devam etsin.

**Başlangıç kodu:**

```python
def matches(doc, query):
    return all(doc.get(k) == v for k, v in query.items())

def find(collection, query):
    return [doc for doc in collection if matches(doc, query)]

players = [{"name": "Piko", "level": 3}, {"name": "Ece", "level": 5}, {"name": "Can", "level": 8}]
print(find(players, {"level": {"$gt": 4}}))
```

**İpuçları:**

1. matches içinde her anahtarı tek tek kontrol et.
2. Değer sözlükse ve "$gt" içeriyorsa doc[key] > value["$gt"] olmalı.
3. Bir koşul tutmazsa hemen return False

<details><summary>Çözüm</summary>

```python
def matches(doc, query):
    for key, value in query.items():
        if isinstance(value, dict) and "$gt" in value:
            if key not in doc or not doc[key] > value["$gt"]:
                return False
        elif doc.get(key) != value:
            return False
    return True

def find(collection, query):
    return [doc for doc in collection if matches(doc, query)]

players = [{"name": "Piko", "level": 3}, {"name": "Ece", "level": 5}, {"name": "Can", "level": 8}]
print(find(players, {"level": {"$gt": 4}}))
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Oyuncu veritabanı**

### Piko'nun Macerası: Oyuncu veritabanı

Piko'nun Macerası'nın oyuncu kayıtlarını yönetelim. `players` koleksiyonu için:

- `add_player(name)`: aynı isimde oyuncu varsa `False` döndürsün. Yoksa `{"name": name, "level": 1, "xp": 0}` belgesini ekleyip `True` döndürsün.
- `level_up(name)`: oyuncunun seviyesini 1 artırıp yeni seviyeyi döndürsün. Oyuncu yoksa `None` döndürsün.

**Başlangıç kodu:**

```python
players = []

def add_player(name):
    pass

def level_up(name):
    pass

print(add_player("Piko"))
print(add_player("Piko"))
print(level_up("Piko"))
print(players)
```

**İpuçları:**

1. add_player: önce aynı isim var mı diye dolaş.
2. level_up: oyuncuyu bulunca p["level"] += 1 ve return p["level"]

<details><summary>Çözüm</summary>

```python
players = []

def add_player(name):
    for p in players:
        if p["name"] == name:
            return False
    players.append({"name": name, "level": 1, "xp": 0})
    return True

def level_up(name):
    for p in players:
        if p["name"] == name:
            p["level"] += 1
            return p["level"]
    return None

print(add_player("Piko"))
print(add_player("Piko"))
print(level_up("Piko"))
print(players)
```

</details>

### Harcama Defteri: Harcama veritabanı

Harcamaları MongoDB'deki gibi belgeler olarak `expenses` koleksiyonunda (listesinde) tutalım:

- `insert(category, amount)`: `{"id": ..., "category": ..., "amount": ...}` belgesini eklesin. `id` 1'den başlayıp her eklemede bir artsın. Eklenen belgeyi döndürsün.
- `find(category)`: o kategorideki belgelerin listesini döndürsün.
- `update_amount(id, amount)`: o `id`'li belgenin tutarını değiştirip `True`, bulamazsa `False` döndürsün.

**Başlangıç kodu:**

```python
expenses = []


def insert(category, amount):
    pass


def find(category):
    pass


def update_amount(id, amount):
    pass
```

**İpuçları:**

1. id için len(expenses) + 1 kullanabilirsin.
2. find için list comprehension: [doc for doc in expenses if doc["category"] == category]

<details><summary>Çözüm</summary>

```python
expenses = []


def insert(category, amount):
    doc = {"id": len(expenses) + 1, "category": category, "amount": amount}
    expenses.append(doc)
    return doc


def find(category):
    return [doc for doc in expenses if doc["category"] == category]


def update_amount(id, amount):
    for doc in expenses:
        if doc["id"] == id:
            doc["amount"] = amount
            return True
    return False
```

</details>

### Görev Asistanı: Hatırlatma veritabanı

Hatırlatmaları MongoDB'deki gibi belgeler olarak `reminders` koleksiyonunda tutalım:

- `add_reminder(text, hour)`: `{"text": ..., "hour": ..., "sent": False}` belgesini eklesin.
- `due(hour)`: saati `hour` veya daha erken olan ve **gönderilmemiş** hatırlatmaların metinlerini liste olarak döndürsün.
- `mark_sent(text)`: o metindeki hatırlatmanın `sent` değerini `True` yapıp `True`, bulamazsa `False` döndürsün.

**Başlangıç kodu:**

```python
reminders = []


def add_reminder(text, hour):
    pass


def due(hour):
    pass


def mark_sent(text):
    pass
```

**İpuçları:**

1. due için list comprehension: iki koşul, r["hour"] <= hour and not r["sent"]
2. mark_sent içinde döngüyle belgeyi bul.

<details><summary>Çözüm</summary>

```python
reminders = []


def add_reminder(text, hour):
    reminders.append({"text": text, "hour": hour, "sent": False})


def due(hour):
    return [r["text"] for r in reminders if r["hour"] <= hour and not r["sent"]]


def mark_sent(text):
    for r in reminders:
        if r["text"] == text:
            r["sent"] = True
            return True
    return False
```

</details>

### Kişisel Web Sitem: Yazı veritabanı

Yazıları MongoDB'deki gibi belgeler olarak `posts` koleksiyonunda (listesinde) tutalım:

- `insert_post(title, tags)`: `{"id": ..., "title": ..., "tags": ..., "views": 0}` belgesini eklesin. `id` 1'den başlayıp her eklemede bir artsın. Eklenen belgeyi döndürsün.
- `find_by_tag(tag)`: `tags` listesinde `tag` olan belgelerin listesini döndürsün.
- `add_view(id)`: o `id`'li belgenin `views` değerini 1 artırıp `True`, bulamazsa `False` döndürsün.

**Başlangıç kodu:**

```python
posts = []


def insert_post(title, tags):
    pass


def find_by_tag(tag):
    pass


def add_view(id):
    pass
```

**İpuçları:**

1. id için len(posts) + 1 kullanabilirsin.
2. find_by_tag için: [doc for doc in posts if tag in doc["tags"]]

<details><summary>Çözüm</summary>

```python
posts = []


def insert_post(title, tags):
    doc = {"id": len(posts) + 1, "title": title, "tags": tags, "views": 0}
    posts.append(doc)
    return doc


def find_by_tag(tag):
    return [doc for doc in posts if tag in doc["tags"]]


def add_view(id):
    for doc in posts:
        if doc["id"] == id:
            doc["views"] += 1
            return True
    return False
```

</details>

### Sohbet Botu: Botun hafızası

Bot, kullanıcılar hakkında öğrendiklerini hatırlasın. Bilgileri MongoDB'deki gibi belgeler olarak `memory` koleksiyonunda (listesinde) tutalım; her belge `{"user": ..., "key": ..., "value": ...}`.

- `remember(user, key, value)`: aynı `user` ve `key` ile bir belge varsa değerini güncellesin, yoksa yeni belge eklesin. Belgeyi döndürsün.
- `recall(user, key)`: o bilginin değerini döndürsün, yoksa `None`.
- `forget(user)`: o kullanıcının bütün belgelerini silsin ve kaç belge sildiğini döndürsün.

**Başlangıç kodu:**

```python
memory = []


def remember(user, key, value):
    pass


def recall(user, key):
    pass


def forget(user):
    pass
```

**İpuçları:**

1. remember ve recall aynı koşulla arar: doc["user"] == user and doc["key"] == key
2. Silerken listenin bir kopyasında dolaş: for doc in list(memory):

<details><summary>Çözüm</summary>

```python
memory = []


def remember(user, key, value):
    for doc in memory:
        if doc["user"] == user and doc["key"] == key:
            doc["value"] = value
            return doc
    doc = {"user": user, "key": key, "value": value}
    memory.append(doc)
    return doc


def recall(user, key):
    for doc in memory:
        if doc["user"] == user and doc["key"] == key:
            return doc["value"]
    return None


def forget(user):
    removed = 0
    for doc in list(memory):
        if doc["user"] == user:
            memory.remove(doc)
            removed += 1
    return removed
```

</details>

### Okul Not Defteri: Ödev veritabanı

Ödevlerini MongoDB'deki gibi belgeler olarak `homework` koleksiyonunda (listesinde) tutalım:

- `insert(lesson, title)`: `{"id": ..., "lesson": ..., "title": ..., "done": False}` belgesini eklesin. `id` 1'den başlayıp her eklemede bir artsın. Eklenen belgeyi döndürsün.
- `find(query)`: sorgu sözlüğündeki **tüm** alanları eşleşen belgelerin listesini döndürsün (`all()` kullan). `find({})` hepsini döndürür.
- `mark_done(id)`: o `id`'li ödevin `done` alanını `True` yapıp `True`, bulamazsa `False` döndürsün.

**Başlangıç kodu:**

```python
homework = []


def insert(lesson, title):
    pass


def find(query):
    pass


def mark_done(id):
    pass
```

**İpuçları:**

1. id için len(homework) + 1 kullanabilirsin.
2. find için: [doc for doc in homework if all(doc.get(k) == v for k, v in query.items())]

<details><summary>Çözüm</summary>

```python
homework = []


def insert(lesson, title):
    doc = {"id": len(homework) + 1, "lesson": lesson, "title": title, "done": False}
    homework.append(doc)
    return doc


def find(query):
    return [doc for doc in homework if all(doc.get(k) == v for k, v in query.items())]


def mark_done(id):
    for doc in homework:
        if doc["id"] == id:
            doc["done"] = True
            return True
    return False
```

</details>
