# Gün 7: Set'ler

**Kurs:** 30 Günde Python  ·  **Bölge:** Veri Ormanı  ·  **Maskot:** Piko

**Bugünün hedefi:** Tekrarsız koleksiyonlar olan set'leri kullanmak ve küme işlemleri yapmak

> Piko ormanda dolaşırken aynı yerlerden defalarca geçti. Haritasına her geçişi yazarsa sayfa dolacak! Aslında ona sadece **hangi yerleri gördüğü** lazım, kaç kez gördüğü değil. Bugün tekrarları kendiliğinden atan **set**'lerle tanışıyoruz.

![Veri Ormanı](../../gorseller/python/harita/orman.webp)

## Konu anlatımı

### Set nedir?

Set, **süslü parantezle** yazılan ve içinde **aynı eleman iki kez bulunamayan** bir koleksiyondur. Elemanların bir sırası yoktur.

```python
places = {"kamp", "köy", "kamp"}
print(places)       # {'kamp', 'köy'}  (sıra değişebilir)
print(len(places))  # 2
```

Boş set oluşturmak için `set()` yazılır. `{}` yazarsan boş bir sözlük (dictionary) olur.

### Listeden tekrarları atmak

Bir listeyi `set()` içine koyarsan tekrarlar kaybolur:

```python
visits = ["orman", "köy", "orman", "kamp"]
unique = set(visits)
print(len(unique))  # 3
```

Sonucu sıralı görmek istersen `sorted(unique)` kullan; sana alfabetik bir liste verir.

### Ekle ve çıkar

- `places.add("liman")` bir eleman ekler (zaten varsa bir şey olmaz)
- `places.remove("kamp")` siler, eleman yoksa hata verir
- `places.discard("kamp")` siler, eleman yoksa sessizce geçer
- `"köy" in places` var mı diye sorar ve çok hızlıdır

### Küme işlemleri

Matematikteki kümeler gibi iki set'i karşılaştırabilirsin:

- `a | b` birleşim: ikisindeki her şey
- `a & b` kesişim: ikisinde de olanlar
- `a - b` fark: a'da olup b'de olmayanlar
- `a <= b` a'nın her elemanı b'de var mı?

Aynı işlemlerin kelime halleri de var: `a.union(b)`, `a.intersection(b)`, `a.difference(b)`.

## Örnekler

### Tekrarlar gitti

```python
visits = ["orman", "köy", "orman", "kamp", "köy"]
unique = set(visits)
print(len(visits), "ziyaret")
print(len(unique), "farklı yer")
print(sorted(unique))
```

### Ekle ve çıkar

```python
bag = {"kılıç", "iksir"}
bag.add("harita")
bag.add("iksir")
bag.discard("kılıç")
print(sorted(bag))
print("iksir" in bag)
```

*İksiri iki kez eklemeye çalıştık ama set'te bir tane var.*

### Arkadaşların oyunları

```python
ali = {"satranç", "saklambaç", "futbol"}
ece = {"futbol", "satranç", "yüzme"}
print("İkisi de:", sorted(ali & ece))
print("Hepsi:", sorted(ali | ece))
print("Sadece Ali:", sorted(ali - ece))
```

## Görevler

### Görev 1: Tekrarları sil

`visits` listesinden tekrarsız bir set yap ve adını `unique` koy. Sonra kaç farklı yer olduğunu yazdır: `3 farklı yer`

**Başlangıç kodu:**

```python
visits = ["orman", "köy", "orman", "kamp", "köy"]

# unique adında bir set oluştur

# Kaç farklı yer olduğunu yazdır
```

**İpuçları:**

1. set(visits) tekrarları atar.
2. print(f"{len(unique)} farklı yer")

<details><summary>Çözüm</summary>

```python
visits = ["orman", "köy", "orman", "kamp", "köy"]

unique = set(visits)

print(f"{len(unique)} farklı yer")
```

</details>

### Görev 2: Yeni yer keşfet

`explored` set'ine `"orman"` ekle ve `"kamp"` yerini çıkar. Sonra sıralı halini yazdır.

**Başlangıç kodu:**

```python
explored = {"kamp", "köy"}

# "orman" ekle, "kamp" çıkar

print(sorted(explored))
```

**İpuçları:**

1. Eklemek için add(), çıkarmak için discard() ya da remove()

<details><summary>Çözüm</summary>

```python
explored = {"kamp", "köy"}

explored.add("orman")
explored.discard("kamp")

print(sorted(explored))
```

</details>

### Görev 3: Ortak oyunlar

`both` iki arkadaşın **ortak** oyunları, `all_games` ise ikisinin **tüm** oyunları olsun.

**Başlangıç kodu:**

```python
ali = {"satranç", "saklambaç", "futbol"}
ece = {"futbol", "satranç", "yüzme"}

both = set()        # ortak oyunlar
all_games = set()   # tüm oyunlar

print(sorted(both))
print(sorted(all_games))
```

**İpuçları:**

1. Kesişim için &, birleşim için | kullan.

<details><summary>Çözüm</summary>

```python
ali = {"satranç", "saklambaç", "futbol"}
ece = {"futbol", "satranç", "yüzme"}

both = ali & ece
all_games = ali | ece

print(sorted(both))
print(sorted(all_games))
```

</details>

## Challenge: Eksik rozetler

`missing` henüz kazanılmamış rozetler olsun. Sonra `Eksik: [...]` şeklinde sıralı yazdır. Hepsi kazanıldıysa `Hepsi tamam!` yazdır.

**Başlangıç kodu:**

```python
all_badges = {"İlk Adım", "İlk Kod", "5 Gün", "Python Dostu"}
earned = {"İlk Adım", "İlk Kod"}

# missing = ?

# missing boşsa "Hepsi tamam!", değilse "Eksik: [...]"
```

**İpuçları:**

1. Fark için - kullan: all_badges - earned
2. Boş mu diye len(missing) == 0 ile bakabilirsin.

<details><summary>Çözüm</summary>

```python
all_badges = {"İlk Adım", "İlk Kod", "5 Gün", "Python Dostu"}
earned = {"İlk Adım", "İlk Kod"}

missing = all_badges - earned

if len(missing) == 0:
    print("Hepsi tamam!")
else:
    print(f"Eksik: {sorted(missing)}")
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Keşfedilen yerler**

### Piko'nun Macerası: Keşfedilen yerler

Piko'nun gezdiği yerler `route` listesinde, daha önce bildiği yerler `known` set'inde.

- `visited`: gezdiği farklı yerler (set)
- `new_places`: gezdiği ama daha önce bilmediği yerler

Sonra şöyle yazdır:

```
4 farklı yer gezildi
Yeni keşifler: ['liman', 'mağara']
```

**Başlangıç kodu:**

```python
route = ["kamp", "köy", "mağara", "köy", "liman", "kamp"]
known = {"kamp", "köy"}

# visited ve new_places

# İki satırı yazdır
```

**İpuçları:**

1. visited = set(route)
2. Yeni yerler için fark: visited - known

<details><summary>Çözüm</summary>

```python
route = ["kamp", "köy", "mağara", "köy", "liman", "kamp"]
known = {"kamp", "köy"}

visited = set(route)
new_places = visited - known

print(f"{len(visited)} farklı yer gezildi")
print(f"Yeni keşifler: {sorted(new_places)}")
```

</details>

### Harcama Defteri: Farklı kategoriler

Bu ayki harcamaların kategorileri `month` listesinde, geçen ay kullandıkların `known` set'inde.

- `categories`: bu ayki farklı kategoriler (set)
- `new_categories`: bu ay ilk kez harcama yaptığın kategoriler

Sonra şöyle yazdır:

```
4 farklı kategori
Yeni: ['kitap', 'sinema']
```

Yeni kategorileri `sorted()` ile alfabetik yazdır.

**Başlangıç kodu:**

```python
month = ["market", "kira", "market", "sinema", "kitap", "kira"]
known = {"market", "kira", "ulaşım"}
```

**İpuçları:**

1. set(month) tekrarları atar.
2. Fark için: categories - known

<details><summary>Çözüm</summary>

```python
month = ["market", "kira", "market", "sinema", "kitap", "kira"]
known = {"market", "kira", "ulaşım"}
categories = set(month)
new_categories = categories - known
print(len(categories), "farklı kategori")
print("Yeni:", sorted(new_categories))
```

</details>

### Görev Asistanı: Kalan görevler

Bütün görevler `all_tasks`, bugün bitirdiklerin `done` set'inde.

- `remaining`: henüz bitmemiş görevler (set farkı)
- `extra`: `done` içinde olup listede olmayan (planda olmayan ama yaptığın) işler

Sonra şöyle yazdır (alfabetik, `sorted()` ile):

```
2 görev kaldı: ['Rapor yaz', 'Spor']
Plan dışı: ['Bulaşık']
```

**Başlangıç kodu:**

```python
all_tasks = {"Kahve", "Rapor yaz", "Spor", "E-postaları oku"}
done = {"Kahve", "E-postaları oku", "Bulaşık"}
```

**İpuçları:**

1. Fark: all_tasks - done
2. Plan dışı işler için tersi: done - all_tasks

<details><summary>Çözüm</summary>

```python
all_tasks = {"Kahve", "Rapor yaz", "Spor", "E-postaları oku"}
done = {"Kahve", "E-postaları oku", "Bulaşık"}
remaining = all_tasks - done
extra = done - all_tasks
print(f"{len(remaining)} görev kaldı: {sorted(remaining)}")
print(f"Plan dışı: {sorted(extra)}")
```

</details>

### Kişisel Web Sitem: Etiket bulutu

Yazılarına etiketler koyuyorsun: hepsi `post_tags` listesinde (tekrarlı). Menüde görünen etiketler `menu_tags` set'inde.

- `tags`: farklı etiketler (set)
- `missing`: yazılarda olan ama menüde olmayan etiketler
- `empty`: menüde olan ama hiçbir yazıda kullanılmayan etiketler

Sonra şöyle yazdır (set'leri `sorted()` ile alfabetik):

```
4 farklı etiket
Menüye ekle: ['notlar', 'oyun']
Boş etiket: ['müzik']
```

**Başlangıç kodu:**

```python
post_tags = ["python", "oyun", "python", "web", "notlar", "web"]
menu_tags = {"python", "web", "müzik"}
```

**İpuçları:**

1. set(post_tags) tekrarları atar.
2. Fark için: tags - menu_tags ve menu_tags - tags

<details><summary>Çözüm</summary>

```python
post_tags = ["python", "oyun", "python", "web", "notlar", "web"]
menu_tags = {"python", "web", "müzik"}
tags = set(post_tags)
missing = tags - menu_tags
empty = menu_tags - tags
print(len(tags), "farklı etiket")
print("Menüye ekle:", sorted(missing))
print("Boş etiket:", sorted(empty))
```

</details>

### Sohbet Botu: Bilinmeyen kelimeler

Bot bazı kelimeleri tanıyor (`known` set'i). Kullanıcının mesajındaki kelimelerden hangilerini tanıyor, hangilerini tanımıyor?

- `words`: mesajdaki farklı kelimeler (`set(message.split())`)
- `matched`: botun tanıdığı kelimeler (kesişim)
- `unknown`: botun tanımadığı kelimeler (fark)

Sonra şöyle yazdır (set'leri `sorted()` ile sıralayarak):

```
5 farklı kelime
Tanıdık: ['hava', 'merhaba']
Bilinmeyen: ['mı', 'sıcak', 'yarın']
```

**Başlangıç kodu:**

```python
known = {"merhaba", "selam", "hava", "saat", "görüşürüz"}
message = "merhaba yarın hava sıcak mı sıcak"
```

**İpuçları:**

1. set() tekrar eden kelimeleri atar.
2. Kesişim: words & known, fark: words - known

<details><summary>Çözüm</summary>

```python
known = {"merhaba", "selam", "hava", "saat", "görüşürüz"}
message = "merhaba yarın hava sıcak mı sıcak"
words = set(message.split())
matched = words & known
unknown = words - known
print(len(words), "farklı kelime")
print("Tanıdık:", sorted(matched))
print("Bilinmeyen:", sorted(unknown))
```

</details>

### Okul Not Defteri: Sınavı olan dersler

Bu dönemki derslerin `lessons` set'inde. Bu haftaki sınavlar `exams` listesinde (bir dersten iki sınav olabilir).

- `exam_lessons`: bu hafta sınavı olan farklı dersler (set)
- `free`: bu hafta sınavı **olmayan** dersler

Sonra şöyle yazdır:

```
3 derste sınav var
Sınavsız: ['Müzik', 'Tarih']
```

Sınavsız dersleri `sorted()` ile alfabetik yazdır.

**Başlangıç kodu:**

```python
lessons = {"Matematik", "Fizik", "Kimya", "Tarih", "Müzik"}
exams = ["Matematik", "Fizik", "Matematik", "Kimya"]
```

**İpuçları:**

1. set(exams) tekrarları atar.
2. Fark için: lessons - exam_lessons

<details><summary>Çözüm</summary>

```python
lessons = {"Matematik", "Fizik", "Kimya", "Tarih", "Müzik"}
exams = ["Matematik", "Fizik", "Matematik", "Kimya"]
exam_lessons = set(exams)
free = lessons - exam_lessons
print(len(exam_lessons), "derste sınav var")
print("Sınavsız:", sorted(free))
```

</details>
