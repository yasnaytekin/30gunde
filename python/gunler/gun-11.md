# Gün 11: Fonksiyonlar

**Kurs:** 30 Günde Python  ·  **Bölge:** Alet Atölyesi  ·  **Maskot:** Piko

**Bugünün hedefi:** Kendi fonksiyonlarını yazmak, parametre almak ve sonuç döndürmek

> Alet Atölyesi'ne hoş geldin! Burada her aletin bir işi var: çekiç çakar, testere keser. Bir kere yapılan alet defalarca kullanılır. Kodda da aynısı mümkün: bir işi bir kez yazıp istediğin kadar çağırabilirsin. Bu aletlere **fonksiyon** diyoruz.

![Alet Atölyesi](../../gorseller/python/harita/atolye.webp)

## Konu anlatımı

### Fonksiyon tanımlamak

`def` ile kendi fonksiyonunu yaparsın. Fonksiyonun içindeki satırlar girintili yazılır ve fonksiyon **çağrılana kadar** çalışmaz:

```python
def greet():
    print("Merhaba!")

greet()
greet()
```

Fonksiyonlara ne yaptıklarını anlatan isimler ver: `greet`, `attack`, `calculate_score`.

### Parametreler

Parantezin içine yazdığın isimler **parametredir**. Fonksiyonu çağırırken bu kutulara değer koyarsın:

```python
def greet(name):
    print(f"Merhaba {name}!")

greet("Piko")
greet("Ece")
```

Birden fazla parametre virgülle ayrılır: `def add(a, b):`

### return: sonucu geri ver

`print` sonucu sadece ekrana yazar. `return` ise sonucu **çağıran yere geri verir**, böylece onu bir değişkene koyup kullanabilirsin:

```python
def add(a, b):
    return a + b

total = add(3, 4)
print(total * 2)   # 14
```

`return` çalışınca fonksiyon orada biter; altındaki satırlar çalışmaz.

### Varsayılan değerler

Bir parametreye varsayılan değer verirsen, çağırırken o değeri yazmak zorunda kalmazsın:

```python
def attack(hp, damage=10):
    return hp - damage

print(attack(50))       # 40
print(attack(50, 25))   # 25
print(attack(hp=50, damage=5))  # isimle de verebilirsin
```

İstediğin kadar değer alan fonksiyonlar için `*args` kullanılır: `def total(*numbers):`

## Örnekler

### İlk fonksiyon

```python
def greet(name):
    print(f"Merhaba {name}, atölyeye hoş geldin!")

greet("Piko")
greet("Deniz")
```

### return ile hesap

```python
def area(width, height):
    return width * height

room = area(4, 5)
garden = area(10, 3)
print("Oda:", room)
print("Bahçe:", garden)
print("Toplam:", room + garden)
```

### Varsayılan ve *args

```python
def attack(hp, damage=10):
    return hp - damage

print(attack(50))
print(attack(50, 25))

def total(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result

print(total(1, 2, 3, 4))
```

## Görevler

### Görev 1: Selam fonksiyonu

`greet` adında, `name` parametresi alan ve `Merhaba Piko!` gibi selam yazdıran bir fonksiyon yaz. Sonra `greet("Piko")` ile çağır.

**Başlangıç kodu:**

```python
# greet fonksiyonunu yaz


# Fonksiyonu çağır
```

**İpuçları:**

1. def greet(name): ile başla.
2. İçinde print(f"Merhaba {name}!") yaz.
3. En altta greet("Piko") ile çağır.

<details><summary>Çözüm</summary>

```python
def greet(name):
    print(f"Merhaba {name}!")

greet("Piko")
```

</details>

### Görev 2: Alan hesaplayıcı

`area(width, height)` fonksiyonu dikdörtgenin alanını **return** ile döndürsün (yazdırmasın).

**Başlangıç kodu:**

```python
def area(width, height):
    # alanı döndür
    pass

print(area(4, 5))
```

**İpuçları:**

1. Alan = genişlik x yükseklik
2. print yerine return width * height

<details><summary>Çözüm</summary>

```python
def area(width, height):
    return width * height

print(area(4, 5))
```

</details>

### Görev 3: Varsayılan hasar

`attack(hp, damage)` fonksiyonu kalan canı döndürsün. `damage` verilmezse 10 olsun.

**Başlangıç kodu:**

```python
def attack(hp, damage):
    return hp - damage

print(attack(50, 25))
print(attack(50))
```

**İpuçları:**

1. Varsayılan değer parametrenin yanına yazılır: damage=10

<details><summary>Çözüm</summary>

```python
def attack(hp, damage=10):
    return hp - damage

print(attack(50, 25))
print(attack(50))
```

</details>

### Sahne görevi: Ordu fabrikası

`ordu(satir, sutun)` fonksiyonu `satir` kadar satır yazdırsın, her satırda `sutun` kadar Piko olsun. Sonra fonksiyonu `ordu(2, 5)` diye çağır.

Fonksiyonun farklı sayılarla da denenecek.

**Başlangıç kodu:**

```python
def ordu(satir, sutun):
    pass

ordu(2, 5)
```

**İpuçları:**

1. Fonksiyonun içinde for i in range(satir):
2. Döngüde print("*" * sutun)

<details><summary>Çözüm</summary>

```python
def ordu(satir, sutun):
    for i in range(satir):
        print("*" * sutun)

ordu(2, 5)
```

</details>

## Challenge: En büyük skor

`biggest(numbers)` listedeki en büyük sayıyı döndürsün. `max()` kullanmadan, bir döngüyle bul.

**Başlangıç kodu:**

```python
def biggest(numbers):
    # max() kullanmadan en büyüğü bul
    pass

print(biggest([3, 17, 8]))
```

**İpuçları:**

1. İlk elemanı en büyük kabul et: best = numbers[0]
2. Döngüde daha büyüğünü görünce best'i güncelle.

<details><summary>Çözüm</summary>

```python
def biggest(numbers):
    best = numbers[0]
    for n in numbers:
        if n > best:
            best = n
    return best

print(biggest([3, 17, 8]))
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Hareket etme**

### Piko'nun Macerası: Hareket etme

Piko'yu yönlerle hareket ettirelim. `move(pos, direction)` yeni konumu **tuple** olarak döndürsün:

- `"kuzey"`: y bir artar
- `"güney"`: y bir azalır
- `"doğu"`: x bir artar
- `"batı"`: x bir azalır
- Başka bir yön gelirse konum değişmez.

**Başlangıç kodu:**

```python
def move(pos, direction):
    x, y = pos
    # yöne göre x veya y'yi değiştir
    return (x, y)

print(move((0, 0), "kuzey"))
```

**İpuçları:**

1. Önce konumu aç: x, y = pos
2. if/elif ile her yönü kontrol et.
3. Sonunda return (x, y)

<details><summary>Çözüm</summary>

```python
def move(pos, direction):
    x, y = pos
    if direction == "kuzey":
        y += 1
    elif direction == "güney":
        y -= 1
    elif direction == "doğu":
        x += 1
    elif direction == "batı":
        x -= 1
    return (x, y)

print(move((0, 0), "kuzey"))
```

</details>

### Harcama Defteri: Hesap fonksiyonları

Hesapları fonksiyonlara taşıyalım:

- `total(amounts)`: listedeki tutarların toplamını **döndürsün**.
- `remaining(budget, amounts)`: bütçeden toplamı çıkarıp kalanı döndürsün. İçinde `total()`'ı kullan.

**Başlangıç kodu:**

```python
def total(amounts):
    pass


def remaining(budget, amounts):
    pass
```

**İpuçları:**

1. Fonksiyonun sonucu return ile döner: return result
2. remaining içinde: return budget - total(amounts)

<details><summary>Çözüm</summary>

```python
def total(amounts):
    result = 0
    for amount in amounts:
        result += amount
    return result


def remaining(budget, amounts):
    return budget - total(amounts)
```

</details>

### Görev Asistanı: Ekle ve tamamla

Görev işlerini fonksiyonlara taşıyalım:

- `add_task(tasks, title)`: görev listede yoksa ekleyip `True`, zaten varsa eklemeden `False` döndürsün.
- `complete_task(tasks, title)`: görev listedeyse çıkarıp `True`, yoksa `False` döndürsün.

**Başlangıç kodu:**

```python
def add_task(tasks, title):
    pass


def complete_task(tasks, title):
    pass
```

**İpuçları:**

1. title in tasks listede olup olmadığını söyler.
2. tasks.remove(title) görevi çıkarır.

<details><summary>Çözüm</summary>

```python
def add_task(tasks, title):
    if title in tasks:
        return False
    tasks.append(title)
    return True


def complete_task(tasks, title):
    if title not in tasks:
        return False
    tasks.remove(title)
    return True
```

</details>

### Kişisel Web Sitem: Slug fonksiyonları

Slug ve adres üretmeyi fonksiyonlara taşıyalım:

- `make_slug(title)`: başlığın baştaki ve sondaki boşluklarını at, küçük harfe çevir, boşlukları `-` yap ve sonucu **döndür**.
- `post_url(title, folder="blog")`: `/blog/kodla-oyna.html` gibi bir adres döndürsün. İçinde `make_slug()`'ı kullan; `folder` verilmezse `"blog"` olsun.

**Başlangıç kodu:**

```python
def make_slug(title):
    pass


def post_url(title, folder="blog"):
    pass
```

**İpuçları:**

1. return title.strip().lower().replace(" ", "-")
2. post_url içinde: return f"/{folder}/{make_slug(title)}.html"

<details><summary>Çözüm</summary>

```python
def make_slug(title):
    return title.strip().lower().replace(" ", "-")


def post_url(title, folder="blog"):
    return f"/{folder}/{make_slug(title)}.html"
```

</details>

### Sohbet Botu: Cevap fonksiyonu

Cevap verme işini fonksiyonlara taşıyalım:

- `clean(message)`: mesajın baştaki ve sondaki boşlukları atılmış, küçük harfe çevrilmiş hâlini **döndürsün**.
- `get_reply(message, bot_name="Bilge")`: mesajı önce `clean()` ile temizlesin, sonra:
  - içinde `"merhaba"` varsa `Merhaba, ben Bilge!` (ad `bot_name`'den)
  - içinde `"hava"` varsa `Bugün hava güneşli.`
  - hiçbiri yoksa `Bunu anlamadım.` döndürsün.

**Başlangıç kodu:**

```python
def clean(message):
    pass


def get_reply(message, bot_name="Bilge"):
    pass
```

**İpuçları:**

1. clean içinde: return message.strip().lower()
2. get_reply içinde önce text = clean(message), sonra if / elif / else ile return.

<details><summary>Çözüm</summary>

```python
def clean(message):
    return message.strip().lower()


def get_reply(message, bot_name="Bilge"):
    text = clean(message)
    if "merhaba" in text:
        return f"Merhaba, ben {bot_name}!"
    elif "hava" in text:
        return "Bugün hava güneşli."
    else:
        return "Bunu anlamadım."
```

</details>

### Okul Not Defteri: Ortalama fonksiyonları

Hesapları fonksiyonlara taşıyalım:

- `average(grades)`: notların ortalamasını 2 basamağa yuvarlayıp **döndürsün** (`round(..., 2)`). Liste boşsa `0` döndürsün.
- `passed(grades, pass_mark=50)`: ortalama `pass_mark` veya üstüyse `True`, değilse `False` döndürsün. İçinde `average()`'ı kullan.

**Başlangıç kodu:**

```python
def average(grades):
    pass


def passed(grades, pass_mark=50):
    pass
```

**İpuçları:**

1. Önce boş liste mi diye bak: if len(grades) == 0: return 0
2. passed içinde: return average(grades) >= pass_mark

<details><summary>Çözüm</summary>

```python
def average(grades):
    if len(grades) == 0:
        return 0
    return round(sum(grades) / len(grades), 2)


def passed(grades, pass_mark=50):
    return average(grades) >= pass_mark
```

</details>
