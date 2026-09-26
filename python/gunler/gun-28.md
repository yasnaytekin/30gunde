# Gün 28: API kullanmak

**Kurs:** 30 Günde Python  ·  **Bölge:** Python Dağı  ·  **Maskot:** Piko

**Bugünün hedefi:** API'lerin ne olduğunu öğrenmek, JSON yanıtlarını okuyup işlemek ve durum kodlarını kontrol etmek

> Dağın yarısındaki kamp evinde bir telsiz var. Piko telsizle hava istasyonunu arıyor: "Zirvede hava nasıl?" İstasyon kısa ve düzenli bir cevap veriyor. Programlar da birbirleriyle böyle konuşur. Bu konuşma kurallarına **API** denir.

![Python Dağı](../../gorseller/python/harita/dag.webp)

## Konu anlatımı

### API nedir?

API (Uygulama Programlama Arayüzü), bir programın başka bir programdan bilgi istemesinin kurallarıdır. Restoranı düşün: mutfağa girmezsin, garsona sipariş verirsin, garson yemeği getirir. API o garsondur.

Hava durumu, döviz kurları, oyun skorları... Birçok hizmet verisini API ile paylaşır.

### JSON: API'lerin dili

API'ler cevaplarını çoğunlukla **JSON** biçiminde verir. JSON, Python sözlüklerine ve listelerine çok benzer ama bir **yazıdır**:

```python
import json

response = '{"sehir": "İzmir", "derece": 27, "gunesli": true}'
data = json.loads(response)    # yazı -> sözlük
print(data["derece"])          # 27

text = json.dumps(data, ensure_ascii=False)   # sözlük -> yazı
```

JSON'da `true`, `false` ve `null` yazılır; Python'da bunlar `True`, `False` ve `None` olur.

### requests ile istek

Kendi bilgisayarında internetten veri almak için `requests` paketi kullanılır:

```python
import requests

r = requests.get("https://api.ornek.com/hava?sehir=izmir")
if r.status_code == 200:
    data = r.json()
    print(data["derece"])
else:
    print("Hata:", r.status_code)
```

Bu sitede internete istek gönderemiyoruz. Görevlerde API'nin döndürdüğü JSON yazısını hazır vereceğiz; sen onu okuyup işleyeceksin.

### İç içe veriler

Gerçek API cevapları çoğu zaman iç içedir: sözlüğün içinde liste, listenin içinde sözlük...

```python
data = {"sehir": "İzmir", "gunler": [{"gun": "Pzt", "derece": 27}, {"gun": "Sal", "derece": 25}]}
print(data["gunler"][1]["derece"])   # 25
```

Adım adım in: önce `data["gunler"]`, sonra `[1]`, sonra `["derece"]`.

## Örnekler

### JSON'u aç

```python
import json

response = '{"sehir": "İzmir", "derece": 27, "gunesli": true}'
data = json.loads(response)
print(type(data))
print(f"{data['sehir']}: {data['derece']} derece")
print("Güneşli mi?", data["gunesli"])
```

### İç içe veri

```python
import json

response = '{"sehir": "Van", "gunler": [{"gun": "Pzt", "derece": 18}, {"gun": "Sal", "derece": 21}]}'
data = json.loads(response)
for day in data["gunler"]:
    print(day["gun"], day["derece"])
```

### Sözlükten JSON

```python
import json

order = {"urun": "fener", "adet": 2, "ödendi": False}
print(json.dumps(order))
print(json.dumps(order, ensure_ascii=False, indent=2))
```

*ensure_ascii=False Türkçe harflerin olduğu gibi görünmesini sağlar.*

## Görevler

### Görev 1: Hava durumu

`response` JSON yazısını sözlüğe çevir (`data`) ve `İzmir: 27 derece` gibi yazdır.

**Başlangıç kodu:**

```python
import json

response = '{"sehir": "İzmir", "derece": 27}'

data = {}

# Şehri ve dereceyi yazdır
```

**İpuçları:**

1. data = json.loads(response)
2. f-string içinde tek tırnak kullan: {data['sehir']}

<details><summary>Çözüm</summary>

```python
import json

response = '{"sehir": "İzmir", "derece": 27}'

data = json.loads(response)

print(f"{data['sehir']}: {data['derece']} derece")
```

</details>

### Görev 2: Ülke listesi

API bir ülke listesi döndürüyor. Ülke **isimlerini** sırayla `names` listesine koy.

**Başlangıç kodu:**

```python
import json

response = '[{"name": "Türkiye", "capital": "Ankara"}, {"name": "Japonya", "capital": "Tokyo"}]'

names = []

print(names)
```

**İpuçları:**

1. Önce json.loads ile listeye çevir.
2. Her ülkeden c["name"] al.

<details><summary>Çözüm</summary>

```python
import json

response = '[{"name": "Türkiye", "capital": "Ankara"}, {"name": "Japonya", "capital": "Tokyo"}]'

data = json.loads(response)
names = [c["name"] for c in data]

print(names)
```

</details>

### Görev 3: Durum kontrolü

`status` 200 ise `body` içindeki öğe sayısını `3 sonuç bulundu` gibi yazdır. Değilse `Hata: 404` gibi yazdır.

**Başlangıç kodu:**

```python
import json

status = 200
body = '{"results": ["a", "b", "c"]}'

# Durumu kontrol et
```

**İpuçları:**

1. if status == 200: ile başla.
2. Sonuçların sayısı: len(data['results'])

<details><summary>Çözüm</summary>

```python
import json

status = 200
body = '{"results": ["a", "b", "c"]}'

if status == 200:
    data = json.loads(body)
    print(f"{len(data['results'])} sonuç bulundu")
else:
    print(f"Hata: {status}")
```

</details>

## Challenge: Sipariş gönder

API'ye göndermek için `order` sözlüğünü JSON yazısına çevir ve `payload` değişkenine koy. Türkçe harfler kaçış kodu olmadan (`ş`, `ü` gibi) görünsün.

**Başlangıç kodu:**

```python
import json

order = {"ürün": "fener", "adet": 2, "şehir": "Muş"}

payload = ""

print(payload)
```

**İpuçları:**

1. json.dumps(order) sözlüğü yazıya çevirir.
2. Türkçe harfler için ensure_ascii=False ekle.

<details><summary>Çözüm</summary>

```python
import json

order = {"ürün": "fener", "adet": 2, "şehir": "Muş"}

payload = json.dumps(order, ensure_ascii=False)

print(payload)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Görev servisi**

### Piko'nun Macerası: Görev servisi

Piko'nun Macerası bir görev servisinden günün görevlerini alıyor. `response`'u aç ve:

- Tamamlanmamış (`"done": false`) görevlerin başlıklarını `open_quests` listesine koy.
- Bu görevlerin ödüllerinin toplamını `total_reward` olarak hesapla.
- `2 açık görev, toplam 150 altın` gibi yazdır.

**Başlangıç kodu:**

```python
import json

response = '{"quests": [{"title": "Fenere git", "reward": 50, "done": false}, {"title": "İksir topla", "reward": 30, "done": true}, {"title": "Ejderhayı uyandırma", "reward": 100, "done": false}]}'

open_quests = []
total_reward = 0

# Özeti yazdır
```

**İpuçları:**

1. Görevler data["quests"] içinde.
2. Açık görev: not q["done"]
3. Önce açık görevleri seç, sonra başlık ve ödülleri ayrı ayrı topla.

<details><summary>Çözüm</summary>

```python
import json

response = '{"quests": [{"title": "Fenere git", "reward": 50, "done": false}, {"title": "İksir topla", "reward": 30, "done": true}, {"title": "Ejderhayı uyandırma", "reward": 100, "done": false}]}'

data = json.loads(response)
open_list = [q for q in data["quests"] if not q["done"]]
open_quests = [q["title"] for q in open_list]
total_reward = sum([q["reward"] for q in open_list])

print(f"{len(open_quests)} açık görev, toplam {total_reward} altın")
```

</details>

### Harcama Defteri: Kur API'si

Bir kur servisinden gelen yanıt `status` (durum kodu) ve `response` (JSON yazısı) değişkenlerinde.

- `status` 200 değilse `Kur alınamadı` yazdır.
- 200 ise JSON'u aç, `rates` içindeki `USD` kurunu al ve `total_try`'ı dolara çevir: `usd = round(total_try / kur, 2)`. Sonra `Toplam: 97.5 USD` gibi yazdır.

**Başlangıç kodu:**

```python
import json

status = 200
response = '{"base": "TRY", "rates": {"USD": 32.0, "EUR": 35.0}}'
total_try = 3120
```

**İpuçları:**

1. json.loads(response) yazıyı sözlüğe çevirir.
2. Kur: data["rates"]["USD"]

<details><summary>Çözüm</summary>

```python
import json

status = 200
response = '{"base": "TRY", "rates": {"USD": 32.0, "EUR": 35.0}}'
total_try = 3120
if status != 200:
    print("Kur alınamadı")
else:
    data = json.loads(response)
    rate = data["rates"]["USD"]
    usd = round(total_try / rate, 2)
    print(f"Toplam: {usd} USD")
```

</details>

### Görev Asistanı: Hava durumu API'si

Asistan sabah hava durumuna baksın. Bir hava servisinden gelen yanıt `status` ve `response` (JSON) değişkenlerinde.

- `status` 200 değilse `Hava durumu alınamadı` yazdır.
- 200 ise JSON'u aç ve `Bugün 18 derece` gibi sıcaklığı yazdır. Yağmur olasılığı (`rain`) 50 veya fazlaysa `Şemsiyeni al!`, değilse `Şemsiyeye gerek yok.` yazdır.

**Başlangıç kodu:**

```python
import json

status = 200
response = '{"city": "İzmir", "temp": 18, "rain": 70}'
```

**İpuçları:**

1. json.loads(response)
2. data["rain"] >= 50

<details><summary>Çözüm</summary>

```python
import json

status = 200
response = '{"city": "İzmir", "temp": 18, "rain": 70}'
if status != 200:
    print("Hava durumu alınamadı")
else:
    data = json.loads(response)
    print(f"Bugün {data['temp']} derece")
    if data["rain"] >= 50:
        print("Şemsiyeni al!")
    else:
        print("Şemsiyeye gerek yok.")
```

</details>

### Kişisel Web Sitem: Yorum API'si

Yazının yorumları bir yorum servisinden geliyor. Yanıt `status` (durum kodu) ve `response` (JSON yazısı) değişkenlerinde.

- `status` 200 değilse sadece `Yorumlar yüklenemedi` yazdır.
- 200 ise JSON'u aç (`json.loads`) ve `comments` içinden sadece `approved` değeri `true` olan yorumları `approved` listesine al. Sonra onaylı yorum sayısını ve her yorumu yazdır:

```
2 yorum
can: Harika yazı!
zeynep: Devamını bekliyorum
```

**Başlangıç kodu:**

```python
import json

status = 200
response = '{"post": "merhaba-dunya", "comments": [{"user": "can", "text": "Harika yazı!", "approved": true}, {"user": "spam_bot", "text": "Ucuz ürünler!", "approved": false}, {"user": "zeynep", "text": "Devamını bekliyorum", "approved": true}]}'
```

**İpuçları:**

1. json.loads(response) yazıyı sözlüğe çevirir; JSON'daki true Python'da True olur.
2. approved = [c for c in data["comments"] if c["approved"]]

<details><summary>Çözüm</summary>

```python
import json

status = 200
response = '{"post": "merhaba-dunya", "comments": [{"user": "can", "text": "Harika yazı!", "approved": true}, {"user": "spam_bot", "text": "Ucuz ürünler!", "approved": false}, {"user": "zeynep", "text": "Devamını bekliyorum", "approved": true}]}'
if status != 200:
    print("Yorumlar yüklenemedi")
else:
    data = json.loads(response)
    approved = [c for c in data["comments"] if c["approved"]]
    print(len(approved), "yorum")
    for c in approved:
        print(f"{c['user']}: {c['text']}")
```

</details>

### Sohbet Botu: Fıkra API'si

Kullanıcı "bana fıkra anlat" deyince bot bir fıkra servisine soruyor. Yanıt `status` (durum kodu) ve `response` (JSON yazısı) değişkenlerinde.

- `status` 200 ise JSON'u aç; fıkra `joke` içinde: soru `setup`, cevap `punchline`. İkisini ayrı satırlarda yazdır:

```
Bot: Bilgisayar neden üşüdü?
Bot: Çünkü pencereleri açık kalmış!
```

- `status` 429 ise (çok fazla istek): `Bot: Çok fazla fıkra istedin, biraz bekle.`
- Başka bir kod ise: `Bot: Şu an aklıma fıkra gelmiyor.`

**Başlangıç kodu:**

```python
import json

status = 200
response = '{"id": 7, "joke": {"setup": "Bilgisayar neden üşüdü?", "punchline": "Çünkü pencereleri açık kalmış!"}}'
```

**İpuçları:**

1. json.loads(response) yazıyı sözlüğe çevirir.
2. İç içe veri: data["joke"]["setup"]

<details><summary>Çözüm</summary>

```python
import json

status = 200
response = '{"id": 7, "joke": {"setup": "Bilgisayar neden üşüdü?", "punchline": "Çünkü pencereleri açık kalmış!"}}'
if status == 200:
    data = json.loads(response)
    print(f"Bot: {data['joke']['setup']}")
    print(f"Bot: {data['joke']['punchline']}")
elif status == 429:
    print("Bot: Çok fazla fıkra istedin, biraz bekle.")
else:
    print("Bot: Şu an aklıma fıkra gelmiyor.")
```

</details>

### Okul Not Defteri: Okul API'si

Okulun not servisinden gelen yanıt `status` (durum kodu) ve `response` (JSON yazısı) değişkenlerinde. Notlar iç içe duruyor: `exams` listesindeki her sınav bir sözlük.

- `status` 200 değilse `Notlar alınamadı (404)` gibi durum koduyla yazdır.
- 200 ise JSON'u aç, notları bir listeye topla ve `average`'ı hesapla (1 basamağa yuvarla). Sonra şöyle yazdır:

```
Ece: 3 sınav, ortalama 81.7
```

**Başlangıç kodu:**

```python
import json

status = 200
response = '{"student": "Ece", "exams": [{"lesson": "Matematik", "grade": 85}, {"lesson": "Fizik", "grade": 70}, {"lesson": "Tarih", "grade": 90}]}'
```

**İpuçları:**

1. json.loads(response) yazıyı sözlüğe çevirir.
2. Notlar: [exam["grade"] for exam in data["exams"]]

<details><summary>Çözüm</summary>

```python
import json

status = 200
response = '{"student": "Ece", "exams": [{"lesson": "Matematik", "grade": 85}, {"lesson": "Fizik", "grade": 70}, {"lesson": "Tarih", "grade": 90}]}'
if status != 200:
    print(f"Notlar alınamadı ({status})")
else:
    data = json.loads(response)
    grades = [exam["grade"] for exam in data["exams"]]
    average = round(sum(grades) / len(grades), 1)
    print(f"{data['student']}: {len(grades)} sınav, ortalama {average}")
```

</details>
