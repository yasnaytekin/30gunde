# Gün 30: Final ve sonrası

**Kurs:** 30 Günde Python  ·  **Bölge:** Python Dağı  ·  **Maskot:** Piko

**Bugünün hedefi:** 30 günde öğrendiklerini birleştirip Piko'nun Macerası'nın final sürümünü yazmak

> Python Dağı'nın zirvesindesin! Buradan geriye baktığında yol ne kadar uzun görünüyor: ilk print'ten API yazmaya kadar geldin. Piko çok gururlu. Son bir macera kaldı: bugüne kadar öğrendiğin her şeyi tek bir oyunda birleştirmek.

![Python Dağı](../../gorseller/python/harita/dag.webp)

## Konu anlatımı

### 30 günde neler öğrendin?

- **Temeller:** print, değişkenler, operatörler, stringler
- **Veri yapıları:** liste, tuple, set, sözlük
- **Akış:** koşullar ve döngüler
- **Aletler:** fonksiyonlar, modüller, list comprehension, üst düzey fonksiyonlar
- **Sağlamlık:** hata tipleri, try/except, düzenli ifadeler, dosyalar
- **Dünya:** paketler, sanal ortam, sınıflar, web kazıma, istatistik, pandas, web, veritabanı, API

Bu, gerçek programcıların her gün kullandığı bir alet çantası!

### İyi programcı alışkanlıkları

- **Küçük adımlarla ilerle:** biraz yaz, çalıştır, sonra devam et
- **İsimlere özen göster:** `x` yerine `score`, `f` yerine `move_player`
- **Hataları oku:** hata mesajı en iyi öğretmenindir
- **Tekrar eden kodu fonksiyona çevir**
- **Takıldığında sor:** arkadaşına, öğretmenine ya da belgelere

### Bundan sonra ne yapabilirsin?

- **Oyun:** `pygame` ile pencereli, grafikli oyunlar
- **Web:** `Flask` ile kendi siteni yayınla
- **Veri:** `pandas` ve grafik paketleriyle veri hikâyeleri anlat
- **Otomasyon:** tekrar eden bilgisayar işlerini Python'a yaptır
- **Yapay zekâ:** makine öğrenmesinin temelleri de Python ile öğrenilir

Kendi bilgisayarına Python kur (python.org) ve bu sitede yazdığın projeleri orada da çalıştır.

### Final macerası

Bugünkü proje görevinde oyunun kalbini yazacaksın: odalar arasında dolaşan, eşya toplayan ve anahtarla hazine kapısını açan bir Piko. Sözlükler, döngüler, koşullar ve fonksiyonlar bir arada!

Bu parçayı da ekleyince **Proje** sayfasına git ve **Oyunumu oyna**'ya bas. 30 gün boyunca yazdığın bütün parçalar tek bir oyunda birleşir: karşılama ekranın, kahramanının bilgileri, skor hesabın, hareket fonksiyonun, savaş kuralların... Yön tuşlarıyla oynarsın ve hangi parçanın ne yaptığını oyunun günlüğünde görürsün.

Görevleri bitirince 30. günü tamamla ve sertifikanı al. Tebrikler, artık bir Python programcısısın!

## Örnekler

### Hepsi bir arada

```python
class Hero:
    def __init__(self, name):
        self.name = name
        self.bag = set()

    def pick(self, item):
        self.bag.add(item)
        return f"{self.name} {item} aldı."

piko = Hero("Piko")
for item in ["harita", "anahtar", "harita"]:
    print(piko.pick(item))
print("Çanta:", sorted(piko.bag))
```

### Kelime sayacı

```python
text = "piko kod yazar piko oyun yapar piko mutlu"
counts = {}
for word in text.split():
    counts[word] = counts.get(word, 0) + 1
for word, n in sorted(counts.items(), key=lambda p: p[1], reverse=True):
    print(word, n)
```

### Oda haritası

```python
rooms = {
    "kamp": {"kuzey": "orman"},
    "orman": {"güney": "kamp", "doğu": "mağara"},
    "mağara": {"batı": "orman"},
}
place = "kamp"
for step in ["kuzey", "doğu", "kuzey"]:
    if step in rooms[place]:
        place = rooms[place][step]
        print("Şimdi buradasın:", place)
    else:
        print("Oraya gidemezsin!")
```

## Görevler

### Görev 1: Sesli harf sayacı

`count_vowels(text)` fonksiyonu yazıdaki Türkçe sesli harflerin (`aeıioöuü`) sayısını döndürsün. Büyük harfler de sayılsın.

**Başlangıç kodu:**

```python
def count_vowels(text):
    return 0

print(count_vowels("Piko Python öğreniyor"))
```

**İpuçları:**

1. Sesli harfleri bir set'e koy: set("aeıioöuü")
2. Harfleri döngüyle gez ve say.
3. Büyük harfler için .lower(), ama Türkçe I ve İ için önce replace kullan.

<details><summary>Çözüm</summary>

```python
def count_vowels(text):
    vowels = set("aeıioöuü")
    count = 0
    for ch in text.replace("I", "ı").replace("İ", "i").lower():
        if ch in vowels:
            count += 1
    return count

print(count_vowels("Piko Python öğreniyor"))
```

</details>

### Görev 2: Kelime sayacı

`word_counts(text)` fonksiyonu, yazıdaki her kelimenin kaç kez geçtiğini bir sözlük olarak döndürsün.

**Başlangıç kodu:**

```python
def word_counts(text):
    return {}

print(word_counts("piko kod yazar piko oyun yapar"))
```

**İpuçları:**

1. Kelimeler: text.split()
2. counts[word] = counts.get(word, 0) + 1

<details><summary>Çözüm</summary>

```python
def word_counts(text):
    counts = {}
    for word in text.split():
        counts[word] = counts.get(word, 0) + 1
    return counts

print(word_counts("piko kod yazar piko oyun yapar"))
```

</details>

### Görev 3: Sayaç sınıfı

`Counter` sınıfı 0'dan başlasın. `increment()` sayacı 1 artırıp yeni değeri döndürsün, `reset()` sayacı sıfırlasın. Değer `value` özelliğinde dursun.

**Başlangıç kodu:**

```python
class Counter:
    pass

c = Counter()
c.increment()
print(c.increment())
```

**İpuçları:**

1. __init__ içinde self.value = 0
2. increment içinde self.value += 1 ve return self.value

<details><summary>Çözüm</summary>

```python
class Counter:
    def __init__(self):
        self.value = 0

    def increment(self):
        self.value += 1
        return self.value

    def reset(self):
        self.value = 0

c = Counter()
c.increment()
print(c.increment())
```

</details>

## Challenge: Komut motoru

Bir kahramanın durumunu komut listesiyle değiştiren `run(commands)` fonksiyonu yaz. Başlangıç: `{"hp": 10, "gold": 0}`.

- `"kazı 5"`: altın 5 artar
- `"savaş 3"`: can 3 azalır
- `"iksir"`: can 5 artar ama 10'u geçemez
- Başka komutlar görmezden gelinir. Can 0 veya altına inerse kalan komutlar çalıştırılmaz.

Fonksiyon son durumu sözlük olarak döndürsün.

**Başlangıç kodu:**

```python
def run(commands):
    state = {"hp": 10, "gold": 0}
    return state

print(run(["kazı 5", "savaş 3", "iksir"]))
```

**İpuçları:**

1. Komutu parçala: parts = command.split()
2. İksir için min(10, hp + 5)
3. Her komuttan sonra canı kontrol et, 0 veya altındaysa break

<details><summary>Çözüm</summary>

```python
def run(commands):
    state = {"hp": 10, "gold": 0}
    for command in commands:
        parts = command.split()
        if parts[0] == "kazı" and len(parts) == 2:
            state["gold"] += int(parts[1])
        elif parts[0] == "savaş" and len(parts) == 2:
            state["hp"] -= int(parts[1])
        elif parts[0] == "iksir":
            state["hp"] = min(10, state["hp"] + 5)
        if state["hp"] <= 0:
            break
    return state

print(run(["kazı 5", "savaş 3", "iksir"]))
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Final macerası**

### Piko'nun Macerası: Final macerası

Piko'nun Macerası'nın final sürümü! `rooms` sözlüğü odaları, çıkışları ve odadaki eşyayı tutuyor. `play(commands)` fonksiyonu Piko'yu `"kamp"`tan başlatsın ve komutları sırayla uygulasın:

- `"git <yön>"`: o yönde çıkış varsa oraya git, yoksa `Oraya gidemezsin!` yazdır.
- `"al"`: odada eşya varsa çantaya koy ve odadan kaldır.
- Piko `"hazine"` odasına **anahtarla** girerse `Tebrikler! Hazineyi buldun.` yazdır ve oyunu bitir. Anahtarsız girerse `Kapı kilitli!` yazdır ve olduğu yerde kalsın.

Fonksiyon sonunda `(bulunduğu_oda, sıralı_çanta_listesi)` döndürsün.

**Başlangıç kodu:**

```python
rooms = {
    "kamp": {"exits": {"kuzey": "orman"}, "item": None},
    "orman": {"exits": {"güney": "kamp", "doğu": "mağara", "kuzey": "hazine"}, "item": "harita"},
    "mağara": {"exits": {"batı": "orman"}, "item": "anahtar"},
    "hazine": {"exits": {}, "item": None},
}

def play(commands):
    place = "kamp"
    bag = set()
    # Komutları uygula
    return place, sorted(bag)

print(play(["git kuzey", "al", "git doğu", "al", "git batı", "git kuzey"]))
```

**İpuçları:**

1. Komutu parçala: parts = command.split()
2. Çıkışlar: rooms[place]["exits"]
3. Hazineye girmeden önce "anahtar" in bag kontrolü yap.
4. Oyun bitince break ile döngüden çık.

<details><summary>Çözüm</summary>

```python
rooms = {
    "kamp": {"exits": {"kuzey": "orman"}, "item": None},
    "orman": {"exits": {"güney": "kamp", "doğu": "mağara", "kuzey": "hazine"}, "item": "harita"},
    "mağara": {"exits": {"batı": "orman"}, "item": "anahtar"},
    "hazine": {"exits": {}, "item": None},
}

def play(commands):
    place = "kamp"
    bag = set()
    for command in commands:
        parts = command.split()
        if parts[0] == "git" and len(parts) == 2:
            exits = rooms[place]["exits"]
            if parts[1] not in exits:
                print("Oraya gidemezsin!")
                continue
            target = exits[parts[1]]
            if target == "hazine":
                if "anahtar" in bag:
                    place = target
                    print("Tebrikler! Hazineyi buldun.")
                    break
                print("Kapı kilitli!")
                continue
            place = target
        elif parts[0] == "al":
            item = rooms[place]["item"]
            if item:
                bag.add(item)
                rooms[place]["item"] = None
    return place, sorted(bag)

print(play(["git kuzey", "al", "git doğu", "al", "git batı", "git kuzey"]))
```

</details>

### Harcama Defteri: Final: aylık rapor

Harcama Defteri'nin final sürümü! `monthly_report(records, budget)` fonksiyonu `(kategori, tutar)` kayıtlarını ve bütçeyi alsın ve bir **sözlük** döndürsün:

- `"total"`: toplam harcama
- `"remaining"`: `budget - total`
- `"top_category"`: toplamı en yüksek kategori (kayıt yoksa `None`)
- `"status"`: toplam bütçeden büyükse `"aşıldı"`, değilse `"yolunda"`

Ayrıca raporu şöyle yazdırsın:

```
Toplam: 2450 TL
Kalan: 2550 TL
En çok: kira
Durum: yolunda
```

**Başlangıç kodu:**

```python
def monthly_report(records, budget):
    pass


monthly_report([("kira", 2000), ("market", 450)], 5000)
```

**İpuçları:**

1. Kategorileri toplamak için bir sözlük: totals[category] = totals.get(category, 0) + amount
2. En yüksek kategori: max(totals, key=totals.get)

<details><summary>Çözüm</summary>

```python
def monthly_report(records, budget):
    totals = {}
    for category, amount in records:
        totals[category] = totals.get(category, 0) + amount
    total = sum(totals.values())
    top = max(totals, key=totals.get) if totals else None
    report = {
        "total": total,
        "remaining": budget - total,
        "top_category": top,
        "status": "aşıldı" if total > budget else "yolunda",
    }
    print(f"Toplam: {total} TL")
    print(f"Kalan: {report['remaining']} TL")
    print(f"En çok: {top}")
    print(f"Durum: {report['status']}")
    return report


monthly_report([("kira", 2000), ("market", 450)], 5000)
```

</details>

### Görev Asistanı: Final: asistan komutları

Görev Asistanı'nın final sürümü! `run_assistant(commands)` yazılı komutları sırayla işlesin ve en sonda kalan görevlerin listesini döndürsün:

- `"ekle <görev>"`: görevi ekle, `Eklendi: <görev>` yazdır. Zaten varsa `Zaten listede: <görev>`.
- `"bitir <görev>"`: görevi çıkar, `Bitti: <görev>` yazdır. Yoksa `Bulunamadı: <görev>`.
- `"liste"`: kalan görevleri `1. Spor` gibi numaralı yazdır; hiç yoksa `Liste boş`.
- Başka bir komut: `Anlaşılmadı: <komut>`.

**Başlangıç kodu:**

```python
def run_assistant(commands):
    tasks = []
    return tasks


run_assistant(["ekle Spor", "ekle Rapor yaz", "bitir Spor", "liste"])
```

**İpuçları:**

1. command.startswith("ekle ") ve command[5:] görevin adını verir.
2. Numaralı liste için enumerate(tasks, 1)

<details><summary>Çözüm</summary>

```python
def run_assistant(commands):
    tasks = []
    for command in commands:
        if command.startswith("ekle "):
            title = command[5:]
            if title in tasks:
                print(f"Zaten listede: {title}")
            else:
                tasks.append(title)
                print(f"Eklendi: {title}")
        elif command.startswith("bitir "):
            title = command[6:]
            if title in tasks:
                tasks.remove(title)
                print(f"Bitti: {title}")
            else:
                print(f"Bulunamadı: {title}")
        elif command == "liste":
            if not tasks:
                print("Liste boş")
            for number, title in enumerate(tasks, 1):
                print(f"{number}. {title}")
        else:
            print(f"Anlaşılmadı: {command}")
    return tasks


run_assistant(["ekle Spor", "ekle Rapor yaz", "bitir Spor", "liste"])
```

</details>

### Kişisel Web Sitem: Final: siteyi oluştur

Kişisel Web Sitem'in final sürümü! `build_site(site_title, posts)` bütün siteyi üretsin. `posts`, sözlüklerden oluşan bir liste (`title`, `text`, `draft`).

- Taslak **olmayan** her yazı için `slug.html` adında bir sayfa: `<h1>başlık</h1><p>metin</p>` (slug: başlığın küçük harfli, boşlukları `-` olan hâli)
- `index.html`: `<h1>site adı</h1>` ve bir `<ul>` içinde yayındaki her yazı için `<li><a href="slug.html">başlık</a></li>`
- Fonksiyon **dosya adı -> HTML** sözlüğünü döndürsün ve şu özeti yazdırsın (dosya adları alfabetik):

```
Site: Kod Günlüğüm
Yayında: 2 yazı, taslak: 1
Dosyalar: index.html, kodla-oyna.html, merhaba-dünya.html
```

**Başlangıç kodu:**

```python
def build_site(site_title, posts):
    pass


posts = [
    {"title": "Merhaba Dünya", "text": "Bu benim ilk yazım.", "draft": False},
    {"title": "Kodla Oyna", "text": "Python ile küçük bir oyun yaptım.", "draft": False},
    {"title": "Robot Kolu", "text": "Henüz bitmedi.", "draft": True},
]
build_site("Kod Günlüğüm", posts)
```

**İpuçları:**

1. Önce boş bir files sözlüğü aç; her yayındaki yazı için files[slug + ".html"] = ... yaz, bağlantıları da bir yazıda biriktir.
2. Taslakları if post["draft"]: ile say ve continue ile atla. Özet için ", ".join(sorted(files))

<details><summary>Çözüm</summary>

```python
def build_site(site_title, posts):
    files = {}
    links = ""
    drafts = 0
    for post in posts:
        if post["draft"]:
            drafts += 1
            continue
        slug = post["title"].lower().replace(" ", "-")
        files[slug + ".html"] = f"<h1>{post['title']}</h1><p>{post['text']}</p>"
        links += f'<li><a href="{slug}.html">{post["title"]}</a></li>'
    files["index.html"] = f"<h1>{site_title}</h1><ul>{links}</ul>"
    print(f"Site: {site_title}")
    print(f"Yayında: {len(files) - 1} yazı, taslak: {drafts}")
    print("Dosyalar: " + ", ".join(sorted(files)))
    return files


posts = [
    {"title": "Merhaba Dünya", "text": "Bu benim ilk yazım.", "draft": False},
    {"title": "Kodla Oyna", "text": "Python ile küçük bir oyun yaptım.", "draft": False},
    {"title": "Robot Kolu", "text": "Henüz bitmedi.", "draft": True},
]
build_site("Kod Günlüğüm", posts)
```

</details>

### Sohbet Botu: Final: sohbet botu

Sohbet Botu'nun final sürümü! `rules` sözlüğünde her niyetin `(anahtar kelimeler, cevap)` ikilisi var. `chat(messages)` bir mesaj listesi alsın, her mesaja cevap versin, konuşmayı yazdırsın ve **cevapların listesini** döndürsün. Her mesaj için:

1. `text`: mesajın temizlenmiş hâli (`strip()` ve `lower()`)
2. `text` boşsa cevap: `Bir şey yazmadın.`
3. Mesajda `adım Ece` gibi bir kalıp varsa (`re.search(r"adım (\w+)", message)`; adın büyük harfi kalsın diye asıl mesajda ara): `Memnun oldum, Ece!`
4. Yoksa `text` içindeki kelimeleri bul (`re.findall(r"\w+", text)` noktalama işaretlerini atar) ve her niyete puan ver: kaç kelime o niyetin anahtar kelimeleri arasında? **En yüksek puanlı** niyetin cevabını seç (eşitlikte önce gelen). Hiçbir niyet puan alamazsa: `Bunu anlamadım.`

Her mesaj için iki satır yazdır:

```
Sen: merhaba
Bot: Merhaba! Ben Bilge.
```

**Başlangıç kodu:**

```python
import re

rules = {
    "selam": (["merhaba", "selam", "hey"], "Merhaba! Ben Bilge."),
    "hava": (["hava", "yağmur", "güneş"], "Bugün hava güneşli."),
    "veda": (["görüşürüz", "hoşça", "bay"], "Görüşürüz!"),
}


def chat(messages):
    replies = []
    return replies


chat(["merhaba", "benim adım Ece", "yarın yağmur var mı", "görüşürüz"])
```

**İpuçları:**

1. Her niyetin puanı: len([w for w in words if w in keywords])
2. En iyiyi bulmak için best_score = 0 ile başla; daha büyük bir puan görünce hem best_score'u hem cevabı güncelle.

<details><summary>Çözüm</summary>

```python
import re

rules = {
    "selam": (["merhaba", "selam", "hey"], "Merhaba! Ben Bilge."),
    "hava": (["hava", "yağmur", "güneş"], "Bugün hava güneşli."),
    "veda": (["görüşürüz", "hoşça", "bay"], "Görüşürüz!"),
}


def chat(messages):
    replies = []
    for message in messages:
        text = message.strip().lower()
        name = re.search(r"adım (\w+)", message)
        if not text:
            reply = "Bir şey yazmadın."
        elif name:
            reply = f"Memnun oldum, {name.group(1)}!"
        else:
            words = re.findall(r"\w+", text)
            reply = "Bunu anlamadım."
            best_score = 0
            for keywords, answer in rules.values():
                score = len([w for w in words if w in keywords])
                if score > best_score:
                    best_score = score
                    reply = answer
        print(f"Sen: {message}")
        print(f"Bot: {reply}")
        replies.append(reply)
    return replies


chat(["merhaba", "benim adım Ece", "yarın yağmur var mı", "görüşürüz"])
```

</details>

### Okul Not Defteri: Final: dönem karnesi

Okul Not Defteri'nin final sürümü! `report_card(records)` fonksiyonu `(ders, not, haftalık_saat)` kayıtlarını alsın ve bir **sözlük** döndürsün:

- `"average"`: **ağırlıklı** ortalama: her not kendi haftalık saatiyle çarpılır, toplam saate bölünür (`sum(not * saat) / sum(saat)`), 2 basamağa yuvarlanır. Kayıt yoksa `0`.
- `"passed"`: notu 50 veya üstü olan derslerin adları (liste)
- `"failed"`: notu 50'nin altındaki derslerin adları (liste)
- `"best"`: notu en yüksek ders (kayıt yoksa `None`)
- `"status"`: kalınan ders varsa `"kaldı"`, yoksa `"geçti"`

Ayrıca karneyi şöyle yazdırsın:

```
Ağırlıklı ortalama: 79.0
Geçilen ders: 3
Kalan ders: 0
En iyi ders: Tarih
Durum: geçti
```

**Başlangıç kodu:**

```python
def report_card(records):
    pass


report_card([("Matematik", 80, 6), ("Fizik", 65, 2), ("Tarih", 90, 2)])
```

**İpuçları:**

1. Döngüde iki toplam tut: total_points += grade * hours ve total_hours += hours
2. En iyi ders için şimdiye kadarki en yüksek notu bir değişkende tut ya da max(records, key=lambda r: r[1]) kullan.

<details><summary>Çözüm</summary>

```python
def report_card(records):
    total_points = 0
    total_hours = 0
    passed = []
    failed = []
    best = None
    best_grade = -1
    for lesson, grade, hours in records:
        total_points += grade * hours
        total_hours += hours
        if grade >= 50:
            passed.append(lesson)
        else:
            failed.append(lesson)
        if grade > best_grade:
            best = lesson
            best_grade = grade
    average = round(total_points / total_hours, 2) if total_hours else 0
    report = {
        "average": average,
        "passed": passed,
        "failed": failed,
        "best": best,
        "status": "kaldı" if failed else "geçti",
    }
    print(f"Ağırlıklı ortalama: {average}")
    print(f"Geçilen ders: {len(passed)}")
    print(f"Kalan ders: {len(failed)}")
    print(f"En iyi ders: {best}")
    print(f"Durum: {report['status']}")
    return report


report_card([("Matematik", 80, 6), ("Fizik", 65, 2), ("Tarih", 90, 2)])
```

</details>
