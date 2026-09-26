# Gün 19: Dosya işlemleri

**Kurs:** 30 Günde Python  ·  **Bölge:** Keşif Adası  ·  **Maskot:** Piko

**Bugünün hedefi:** Dosyaya yazmak, dosyadan okumak ve JSON ile veriyi kaydetmek

> Adanın deniz fenerinde bir kaptan günlüğü bulduk. Kaptan her akşam olanları deftere yazmış, böylece yüzlerce yıl sonra biz okuyabiliyoruz. Programların da bir defteri olabilir: **dosyalar**. Program kapansa bile dosyadaki bilgi kalır. Bugün oyunumuzu kaydetmeyi öğreneceğiz.

![Keşif Adası](../../gorseller/python/harita/ada.webp)

## Konu anlatımı

### Dosya açmak

`open(dosya_adı, mod)` bir dosyayı açar. Mod, ne yapmak istediğini söyler:

- `"r"` okumak için (varsayılan)
- `"w"` yazmak için: dosya yoksa oluşturur, **varsa içini siler**
- `"a"` sonuna eklemek için

Dosyayı işimiz bitince kapatmak gerekir. `with` bunu bizim için otomatik yapar:

```python
with open("gunluk.txt", "w") as f:
    f.write("Bugün Python öğrendim\n")
```

`\n` yeni satır demektir. `write` kendisi alt satıra geçmez.

### Okumak

```python
with open("gunluk.txt") as f:
    text = f.read()          # tüm dosya tek bir yazı

with open("gunluk.txt") as f:
    for line in f:           # satır satır
        print(line.strip())
```

`strip()` satır sonundaki `\n` karakterini temizler.

### JSON ile kaydetmek

Listeleri ve sözlükleri dosyaya kaydetmenin en kolay yolu **JSON** biçimidir:

```python
import json

hero = {"name": "Piko", "hp": 80}
with open("kayit.json", "w") as f:
    json.dump(hero, f)

with open("kayit.json") as f:
    loaded = json.load(f)
```

Dosya var mı diye bakmak için: `import os` ve `os.path.exists("kayit.json")`

### Bu sitede dosyalar

Burada yazdığın dosyalar tarayıcının hafızasında, **sadece o çalıştırma boyunca** yaşar. Bir sonraki çalıştırmada her şey temiz başlar. Bu yüzden görevlerde önce yazıp sonra aynı kodda okuyacağız.

Kendi bilgisayarında Python kurduğunda dosyalar gerçekten diske yazılır ve kalıcı olur.

## Örnekler

### Yaz ve oku

```python
with open("gunluk.txt", "w") as f:
    f.write("1. gün: Kampa vardık\n")
    f.write("2. gün: Köyü gezdik\n")

with open("gunluk.txt") as f:
    print(f.read())
```

### Sonuna ekle

```python
with open("liste.txt", "w") as f:
    f.write("kılıç\n")

with open("liste.txt", "a") as f:
    f.write("iksir\n")

with open("liste.txt") as f:
    for i, line in enumerate(f, 1):
        print(i, line.strip())
```

### JSON kaydı

```python
import json, os

hero = {"name": "Piko", "hp": 80, "bag": ["harita"]}
with open("kayit.json", "w") as f:
    json.dump(hero, f)

print("Dosya var mı?", os.path.exists("kayit.json"))
with open("kayit.json") as f:
    print(json.load(f))
```

## Görevler

### Görev 1: Günlük yaz

`entry` yazısını `gunluk.txt` dosyasına yaz, sonra dosyayı okuyup içeriğini yazdır.

**Başlangıç kodu:**

```python
entry = "Bugün Python öğrendim"

# gunluk.txt dosyasına yaz

# Dosyayı oku ve yazdır
```

**İpuçları:**

1. Yazmak için: with open("gunluk.txt", "w") as f:
2. Okumak için: with open("gunluk.txt") as f: print(f.read())

<details><summary>Çözüm</summary>

```python
entry = "Bugün Python öğrendim"

with open("gunluk.txt", "w") as f:
    f.write(entry)

with open("gunluk.txt") as f:
    print(f.read())
```

</details>

### Görev 2: Satırları say

`lines` listesindeki her eşyayı ayrı satır olarak `canta.txt` dosyasına yaz. Sonra dosyayı okuyup kaç satır olduğunu `count` değişkenine koy.

**Başlangıç kodu:**

```python
lines = ["kılıç", "kalkan", "iksir"]

# Her eşyayı ayrı satıra yaz

count = 0

print(count, "satır")
```

**İpuçları:**

1. Her eşyanın sonuna "\n" ekle.
2. Okurken for line in f: ile say.

<details><summary>Çözüm</summary>

```python
lines = ["kılıç", "kalkan", "iksir"]

with open("canta.txt", "w") as f:
    for item in lines:
        f.write(item + "\n")

count = 0
with open("canta.txt") as f:
    for line in f:
        count += 1

print(count, "satır")
```

</details>

### Görev 3: Sonuna ekle

`skorlar.txt` dosyasına önce `100` yaz. Sonra dosyayı **ekleme modunda** açıp `new_score`'u ekle. En sonda dosyayı okuyup yazdır.

**Başlangıç kodu:**

```python
new_score = 250

with open("skorlar.txt", "w") as f:
    f.write("100\n")

# new_score'u dosyanın sonuna ekle

with open("skorlar.txt") as f:
    print(f.read())
```

**İpuçları:**

1. Ekleme modu: open("skorlar.txt", "a")
2. Sayıyı yazmadan önce str() ile yazıya çevir.

<details><summary>Çözüm</summary>

```python
new_score = 250

with open("skorlar.txt", "w") as f:
    f.write("100\n")

with open("skorlar.txt", "a") as f:
    f.write(str(new_score) + "\n")

with open("skorlar.txt") as f:
    print(f.read())
```

</details>

## Challenge: JSON kaydet ve yükle

`hero` sözlüğünü `hero.json` dosyasına **json.dump** ile kaydet. Sonra **json.load** ile okuyup `loaded` değişkenine koy.

**Başlangıç kodu:**

```python
import json

hero = {"name": "Piko", "hp": 80, "bag": ["harita", "anahtar"]}

loaded = None

print(loaded)
```

**İpuçları:**

1. Kaydet: with open("hero.json", "w") as f: json.dump(hero, f)
2. Yükle: with open("hero.json") as f: loaded = json.load(f)

<details><summary>Çözüm</summary>

```python
import json

hero = {"name": "Piko", "hp": 80, "bag": ["harita", "anahtar"]}

with open("hero.json", "w") as f:
    json.dump(hero, f)

with open("hero.json") as f:
    loaded = json.load(f)

print(loaded)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Oyunu kaydetme**

### Piko'nun Macerası: Oyunu kaydetme

Piko'nun Macerası artık kaydedilebilsin!

- `save_game(state)` sözlüğü `kayit.json` dosyasına JSON olarak yazsın.
- `load_game()` dosya varsa içindeki sözlüğü döndürsün, **yoksa `None`** döndürsün.

**Başlangıç kodu:**

```python
import json
import os

def save_game(state):
    pass

def load_game():
    pass

print(load_game())
save_game({"hp": 50, "place": "fener"})
print(load_game())
```

**İpuçları:**

1. save_game içinde json.dump kullan.
2. load_game içinde önce os.path.exists("kayit.json") ile bak.

<details><summary>Çözüm</summary>

```python
import json
import os

def save_game(state):
    with open("kayit.json", "w") as f:
        json.dump(state, f)

def load_game():
    if not os.path.exists("kayit.json"):
        return None
    with open("kayit.json") as f:
        return json.load(f)

print(load_game())
save_game({"hp": 50, "place": "fener"})
print(load_game())
```

</details>

### Harcama Defteri: Harcamaları kaydetme

Program kapanınca harcamalar kaybolmasın!

- `save_expenses(records)`: listeyi `harcamalar.json` dosyasına JSON olarak yazsın.
- `load_expenses()`: dosya varsa içindeki listeyi döndürsün, **yoksa boş liste** `[]` döndürsün.

**Başlangıç kodu:**

```python
import json
import os


def save_expenses(records):
    pass


def load_expenses():
    pass
```

**İpuçları:**

1. json.dump(veri, dosya) yazar, json.load(dosya) okur.
2. os.path.exists("harcamalar.json") dosya var mı diye bakar.

<details><summary>Çözüm</summary>

```python
import json
import os


def save_expenses(records):
    with open("harcamalar.json", "w") as f:
        json.dump(records, f)


def load_expenses():
    if not os.path.exists("harcamalar.json"):
        return []
    with open("harcamalar.json") as f:
        return json.load(f)
```

</details>

### Görev Asistanı: Görevleri dosyaya kaydetme

Asistan kapanınca görevler kaybolmasın!

- `save_tasks(tasks)`: her görevi **ayrı bir satıra** yazarak `gorevler.txt` dosyasına kaydetsin.
- `load_tasks()`: dosya varsa satırları liste olarak döndürsün (satır sonlarını at), **yoksa boş liste** döndürsün.

**Başlangıç kodu:**

```python
import os


def save_tasks(tasks):
    pass


def load_tasks():
    pass
```

**İpuçları:**

1. f.write(task + "\n") her görevi ayrı satıra yazar.
2. Okurken line.strip() satır sonunu atar.

<details><summary>Çözüm</summary>

```python
import os


def save_tasks(tasks):
    with open("gorevler.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")


def load_tasks():
    if not os.path.exists("gorevler.txt"):
        return []
    with open("gorevler.txt") as f:
        return [line.strip() for line in f if line.strip()]
```

</details>

### Kişisel Web Sitem: Yazıları kaydetme

Yazıların program kapanınca kaybolmasın!

- `save_posts(posts)`: listeyi `yazilar.json` dosyasına JSON olarak yazsın.
- `load_posts()`: dosya varsa içindeki listeyi döndürsün, **yoksa boş liste** `[]` döndürsün.
- `add_post(post)`: kayıtlı yazıları yükleyip yeni yazıyı sona eklesin, listeyi tekrar kaydetsin ve toplam yazı sayısını döndürsün.

**Başlangıç kodu:**

```python
import json
import os


def save_posts(posts):
    pass


def load_posts():
    pass


def add_post(post):
    pass
```

**İpuçları:**

1. json.dump(veri, dosya) yazar, json.load(dosya) okur.
2. add_post içinde: posts = load_posts(), posts.append(post), save_posts(posts), return len(posts)

<details><summary>Çözüm</summary>

```python
import json
import os


def save_posts(posts):
    with open("yazilar.json", "w") as f:
        json.dump(posts, f)


def load_posts():
    if not os.path.exists("yazilar.json"):
        return []
    with open("yazilar.json") as f:
        return json.load(f)


def add_post(post):
    posts = load_posts()
    posts.append(post)
    save_posts(posts)
    return len(posts)
```

</details>

### Sohbet Botu: Sohbet geçmişi

Bot kapanınca konuşmaları unutmasın!

- `load_history()`: `sohbet.json` dosyası varsa içindeki listeyi döndürsün, **yoksa boş liste** `[]` döndürsün.
- `log_message(sender, text)`: geçmişi yüklesin, sonuna `{"sender": sender, "text": text}` sözlüğünü eklesin, listeyi `sohbet.json` dosyasına JSON olarak geri yazsın ve geçmişteki mesaj sayısını döndürsün.

**Başlangıç kodu:**

```python
import json
import os


def load_history():
    pass


def log_message(sender, text):
    pass
```

**İpuçları:**

1. os.path.exists("sohbet.json") dosya var mı diye bakar; json.load(dosya) okur.
2. log_message içinde: yükle, append ile ekle, json.dump(history, dosya) ile yaz, len(history) döndür.

<details><summary>Çözüm</summary>

```python
import json
import os


def load_history():
    if not os.path.exists("sohbet.json"):
        return []
    with open("sohbet.json") as f:
        return json.load(f)


def log_message(sender, text):
    history = load_history()
    history.append({"sender": sender, "text": text})
    with open("sohbet.json", "w") as f:
        json.dump(history, f)
    return len(history)
```

</details>

### Okul Not Defteri: Notları kaydetme

Program kapanınca notların kaybolmasın!

- `save_grades(grades)`: sözlüğü `notlar.json` dosyasına JSON olarak yazsın.
- `load_grades()`: dosya varsa içindeki sözlüğü döndürsün, **yoksa boş sözlük** `{}` döndürsün.
- `add_grade(lesson, grade)`: kayıtlı notları yüklesin, yeni notu ekleyip tekrar kaydetsin.

**Başlangıç kodu:**

```python
import json
import os


def save_grades(grades):
    pass


def load_grades():
    pass


def add_grade(lesson, grade):
    pass
```

**İpuçları:**

1. json.dump(veri, dosya) yazar, json.load(dosya) okur. os.path.exists("notlar.json") dosya var mı diye bakar.
2. add_grade içinde: önce load_grades(), sonra grades[lesson] = grade, en son save_grades(grades).

<details><summary>Çözüm</summary>

```python
import json
import os


def save_grades(grades):
    with open("notlar.json", "w") as f:
        json.dump(grades, f)


def load_grades():
    if not os.path.exists("notlar.json"):
        return {}
    with open("notlar.json") as f:
        return json.load(f)


def add_grade(lesson, grade):
    grades = load_grades()
    grades[lesson] = grade
    save_grades(grades)
```

</details>
