# Gün 8: Dictionary

**Kurs:** 30 Günde Python  ·  **Bölge:** Veri Ormanı  ·  **Maskot:** Piko

**Bugünün hedefi:** Anahtar-değer yapısını öğrenmek

> Ormanda yaşayan her canlının bir kimlik kartı var: adı, canı, gücü... Bugün oyundaki karakterlerin bilgilerini saklamayı öğreneceğiz. Bunun için Python'ın **sözlüklerini** (dictionary) kullanacağız.

![Veri Ormanı](../../gorseller/python/harita/orman.webp)

## Konu anlatımı

### Sözlük nedir?

Gerçek bir sözlükte kelimeye bakıp anlamını bulursun. Python sözlüğünde de **anahtara** bakıp **değeri** bulursun.

```python
player = {"name": "Piko", "hp": 100, "gold": 50}
print(player["name"])  # Piko
```

Listede elemanlara sıra numarasıyla (0, 1, 2) ulaşırız, sözlükte ise isimle (`"name"`, `"hp"`).

### Ekle, değiştir, sil

```python
player["level"] = 1                # yeni anahtar ekle
player["hp"] = player["hp"] - 10   # değiştir
del player["gold"]                 # sil
```

### Güvenli bakış: get()

Olmayan bir anahtarı `player["shield"]` diye sorarsan Python `KeyError` hatası verir. `get()` ise hata vermez, senin belirlediğin yedek değeri döndürür:

```python
shield = player.get("shield", 0)  # yoksa 0
```

### Sözlüğü incelemek

- `player.keys()` tüm anahtarlar
- `player.values()` tüm değerler
- `"hp" in player` bu anahtar var mı?
- `len(player)` kaç anahtar var?

Değer olarak liste bile koyabilirsin: `{"inventory": ["kılıç", "iksir"]}`

## Örnekler

### Kimlik kartı

```python
player = {"name": "Piko", "hp": 100, "gold": 50}
print(player["name"])
player["level"] = 1
print(player)
print(player.keys())
```

### Düşmana saldır

```python
enemy = {"name": "Goblin", "hp": 30}
enemy["hp"] -= 12
print(enemy["name"], "canı:", enemy["hp"])
print(enemy.get("shield", "Kalkanı yok!"))
```

### İç içe

```python
hero = {"name": "Piko", "inventory": ["kılıç", "iksir"]}
hero["inventory"].append("harita")
print(hero["inventory"])
print(len(hero["inventory"]), "eşya")
```

## Görevler

### Görev 1: Altın ekle

Oyuncunun sözlüğüne `"gold"` anahtarını `50` değeriyle ekle.

**Başlangıç kodu:**

```python
player = {"name": "Piko", "hp": 100}

# "gold" anahtarını 50 değeriyle ekle

print(player)
```

**İpuçları:**

1. Yeni anahtar eklemek: sozluk[anahtar] = deger
2. player["gold"] = 50

<details><summary>Çözüm</summary>

```python
player = {"name": "Piko", "hp": 100}

player["gold"] = 50

print(player)
```

</details>

### Görev 2: Hasar al

Goblin 12 hasar aldı. Canını 12 azalt. Yeni sayıyı elle yazma, `enemy["hp"]` değerini değiştir.

**Başlangıç kodu:**

```python
enemy = {"name": "Goblin", "hp": 30}

# Goblin 12 hasar aldı

print(enemy["name"], "canı:", enemy["hp"])
```

**İpuçları:**

1. enemy["hp"] ile değere ulaşırsın.
2. enemy["hp"] -= 12

<details><summary>Çözüm</summary>

```python
enemy = {"name": "Goblin", "hp": 30}

enemy["hp"] -= 12

print(enemy["name"], "canı:", enemy["hp"])
```

</details>

### Görev 3: Güvenli bakış

`get()` kullanarak oyuncunun kalkanını oku. Sözlükte `"shield"` yoksa sonuç `0` olsun.

**Başlangıç kodu:**

```python
player = {"name": "Piko", "hp": 100}

shield = None  # get() ile oku
print("Kalkan:", shield)
```

**İpuçları:**

1. get() iki şey alır: anahtar ve yedek değer.
2. shield = player.get("shield", 0)

<details><summary>Çözüm</summary>

```python
player = {"name": "Piko", "hp": 100}

shield = player.get("shield", 0)
print("Kalkan:", shield)
```

</details>

## Challenge: Market hesabı

Sepetteki eşyaların toplam fiyatını `prices` sözlüğünü kullanarak hesapla ve `total`'a koy. Fiyatları elle yazmak yok! İpucu: `prices[cart[0]]` ilk eşyanın fiyatını verir.

**Başlangıç kodu:**

```python
prices = {"iksir": 25, "kılıç": 120, "kalkan": 80}
cart = ["iksir", "iksir", "kalkan"]

total = 0
print("Toplam:", total)
```

**İpuçları:**

1. cart[0] ilk eşyanın adı.
2. O adı prices sözlüğünde anahtar olarak kullan.

<details><summary>Çözüm</summary>

```python
prices = {"iksir": 25, "kılıç": 120, "kalkan": 80}
cart = ["iksir", "iksir", "kalkan"]

total = prices[cart[0]] + prices[cart[1]] + prices[cart[2]]
print("Toplam:", total)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Kahraman kaydı**

### Piko'nun Macerası: Kahraman kaydı

Önceki günlerde kahramanın bilgilerini ayrı değişkenlerde tutmuştuk. Şimdi hepsini tek bir `hero` sözlüğünde toplayalım:

- `"name"`: kahramanın adı
- `"hp"`: 100
- `"gold"`: 0
- `"inventory"`: içinde `"fener"` olan bir liste

Sonra `Piko - Can: 100` biçiminde bir satır yazdır. Ad ve can sözlükten gelsin.

**Başlangıç kodu:**

```python
# Kahramanın tüm bilgileri tek bir sözlükte
hero = {
    "name": "Piko",
}
```

**İpuçları:**

1. Anahtar-değer çiftlerini virgülle ayır.
2. "inventory": ["fener"]
3. print(hero["name"], "- Can:", hero["hp"])

<details><summary>Çözüm</summary>

```python
hero = {
    "name": "Piko",
    "hp": 100,
    "gold": 0,
    "inventory": ["fener"],
}

print(f"{hero['name']} - Can: {hero['hp']}")
```

</details>

### Harcama Defteri: Kategori limitleri

Her kategori için bir harcama sınırı koyalım. `limits` sözlüğü kategori -> limit.

- `"eğlence"` için `300` limitini ekle.
- `"market"` limitini `1600`'e çıkar.
- Sonra `total_limit`: tüm limitlerin toplamı (`sum(limits.values())`)
- `Market limiti: 1600 TL` ve `Toplam limit: 4400 TL` yazdır.

**Başlangıç kodu:**

```python
limits = {"kira": 2000, "market": 1500, "ulaşım": 500}
```

**İpuçları:**

1. Yeni anahtar eklemek ve değeri değiştirmek aynı yazılır: limits["eğlence"] = 300
2. sum(limits.values()) tüm değerleri toplar.

<details><summary>Çözüm</summary>

```python
limits = {"kira": 2000, "market": 1500, "ulaşım": 500}
limits["eğlence"] = 300
limits["market"] = 1600
total_limit = sum(limits.values())
print(f"Market limiti: {limits['market']} TL")
print(f"Toplam limit: {total_limit} TL")
```

</details>

### Görev Asistanı: Görev kartı

Her görevi bir sözlükle tutalım: `task`.

- Göreve `"priority"` anahtarıyla `"yüksek"` önceliğini ekle.
- Görevi bitmiş işaretle: `"done"` değeri `True` olsun.
- Sonra `Rapor yaz [yüksek] - bitti: True` yazdır (değerler sözlükten gelsin).

**Başlangıç kodu:**

```python
task = {"title": "Rapor yaz", "done": False}
```

**İpuçları:**

1. task["priority"] = "yüksek" yeni anahtar ekler.
2. Değer değiştirmek de aynı: task["done"] = True

<details><summary>Çözüm</summary>

```python
task = {"title": "Rapor yaz", "done": False}
task["priority"] = "yüksek"
task["done"] = True
print(f"{task['title']} [{task['priority']}] - bitti: {task['done']}")
```

</details>

### Kişisel Web Sitem: Yazı sözlüğü

Bir yazının bütün bilgilerini tek bir sözlükte tutalım.

- `"tags"` anahtarıyla `["python", "blog"]` listesini ekle.
- `"words"` değerini `420` yap (yazıyı uzattın).
- `draft`: yazının `"draft"` değeri; sözlükte yoksa `False` olsun (`get()` ile).
- Sonra şöyle yazdır:

```
Merhaba Dünya - 420 kelime
Taslak mı: False
```

**Başlangıç kodu:**

```python
post = {"title": "Merhaba Dünya", "slug": "merhaba-dunya", "words": 350}
```

**İpuçları:**

1. Yeni anahtar eklemek ve değeri değiştirmek aynı yazılır: post["words"] = 420
2. post.get("draft", False) anahtar yoksa False verir.

<details><summary>Çözüm</summary>

```python
post = {"title": "Merhaba Dünya", "slug": "merhaba-dunya", "words": 350}
post["tags"] = ["python", "blog"]
post["words"] = 420
draft = post.get("draft", False)
print(f"{post['title']} - {post['words']} kelime")
print("Taslak mı:", draft)
```

</details>

### Sohbet Botu: Cevap sözlüğü

Niyet -> cevap eşleşmelerini bir sözlükte tutmak çok daha kolay.

- `"veda"` niyeti için `"Görüşürüz!"` cevabını ekle.
- `"selam"` cevabını `"Selam, hoş geldin!"` olarak değiştir.
- `answer`: `intent` niyetinin cevabı; sözlükte yoksa `"Bunu anlamadım."` (`get()` ile)
- `answer`'ı ve `3 cevap biliyorum` satırını yazdır (`len()`).

**Başlangıç kodu:**

```python
replies = {"selam": "Merhaba!", "hava": "Bugün hava güneşli."}
intent = "veda"
```

**İpuçları:**

1. Eklemek ve değiştirmek aynı yazılır: replies["veda"] = "Görüşürüz!"
2. replies.get(intent, "Bunu anlamadım.") anahtar yoksa ikinci değeri verir.

<details><summary>Çözüm</summary>

```python
replies = {"selam": "Merhaba!", "hava": "Bugün hava güneşli."}
intent = "veda"
replies["veda"] = "Görüşürüz!"
replies["selam"] = "Selam, hoş geldin!"
answer = replies.get(intent, "Bunu anlamadım.")
print(answer)
print(f"{len(replies)} cevap biliyorum")
```

</details>

### Okul Not Defteri: Not sözlüğü

Her dersin notunu bir sözlükte tutalım: `grades` ders -> not.

- `"Kimya"` için `75` notunu ekle.
- Fizik sınavına itiraz ettin ve notun `70` oldu: `"Fizik"` notunu güncelle.
- `average`: tüm notların ortalaması (`sum(grades.values()) / len(grades)`), `round()` ile 1 basamağa yuvarla.
- `Fizik: 70` ve `Ortalama: 80.0` yazdır.

**Başlangıç kodu:**

```python
grades = {"Matematik": 85, "Fizik": 60, "Tarih": 90}
```

**İpuçları:**

1. Yeni anahtar eklemek ve değeri değiştirmek aynı yazılır: grades["Kimya"] = 75
2. sum(grades.values()) tüm notları toplar, len(grades) kaç ders olduğunu verir.

<details><summary>Çözüm</summary>

```python
grades = {"Matematik": 85, "Fizik": 60, "Tarih": 90}
grades["Kimya"] = 75
grades["Fizik"] = 70
average = round(sum(grades.values()) / len(grades), 1)
print(f"Fizik: {grades['Fizik']}")
print(f"Ortalama: {average}")
```

</details>
