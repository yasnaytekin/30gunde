# Gün 29: API yapmak

**Kurs:** 30 Günde Python  ·  **Bölge:** Python Dağı  ·  **Maskot:** Piko

**Bugünün hedefi:** Kendi API'ni tasarlamak: GET, POST, PUT ve DELETE isteklerini karşılayan fonksiyonlar yazmak

> Zirveye çok az kaldı! Dün başka istasyonlara soru sorduk; bugün soruları cevaplayan istasyon **biz** oluyoruz. Arkadaşlarının oyunları, Piko'nun Macerası'nın skorlarını senin yazacağın API'den okuyabilecek.

![Python Dağı](../../gorseller/python/harita/dag.webp)

## Konu anlatımı

### HTTP metotları

Bir API'ye gelen her isteğin bir **metodu** vardır. Metot ne yapılmak istendiğini söyler:

- `GET`: veriyi getir (oku)
- `POST`: yeni veri ekle
- `PUT`: var olan veriyi güncelle
- `DELETE`: veriyi sil

Bu dört işleme kısaca **CRUD** denir: Create, Read, Update, Delete.

### Adresler ve kimlikler

API adresleri genellikle şöyle düzenlenir:

- `GET /players` tüm oyuncular
- `GET /players/2` kimliği 2 olan oyuncu
- `POST /players` yeni oyuncu ekle
- `DELETE /players/2` 2 numaralı oyuncuyu sil

Adresi parçalamak için `split` işe yarar: `"/players/2".split("/")` sonucu `['', 'players', '2']`

### Flask ile gerçek bir API

```python
from flask import Flask, jsonify, request
app = Flask(__name__)
players = []

@app.route("/players", methods=["GET"])
def list_players():
    return jsonify(players), 200

@app.route("/players", methods=["POST"])
def create_player():
    data = request.get_json()
    players.append(data)
    return jsonify(data), 201
```

Bu sitede bir sunucu çalıştıramadığımız için aynı mantığı düz fonksiyonlarla kuracağız: her fonksiyon `(durum_kodu, cevap)` döndürecek.

### Doğru durum kodu

- `200` Tamam (GET ve PUT başarılı)
- `201` Oluşturuldu (POST başarılı)
- `204` İçerik yok (DELETE başarılı)
- `400` Hatalı istek (eksik bilgi)
- `404` Bulunamadı

İyi bir API, her zaman anlaşılır bir durum kodu ve hata mesajı döndürür.

## Örnekler

### Adresi parçala

```python
for path in ["/players", "/players/2", "/scores/10"]:
    parts = path.strip("/").split("/")
    print(path, "->", parts)
```

### Mini API

```python
players = [{"id": 1, "name": "Piko"}]

def get_players():
    return 200, players

def create_player(body):
    if "name" not in body:
        return 400, {"hata": "isim gerekli"}
    player = {"id": len(players) + 1, "name": body["name"]}
    players.append(player)
    return 201, player

print(create_player({"name": "Ece"}))
print(create_player({}))
print(get_players())
```

### Bul ya da 404

```python
players = [{"id": 1, "name": "Piko"}, {"id": 2, "name": "Ece"}]

def get_player(pid):
    for p in players:
        if p["id"] == pid:
            return 200, p
    return 404, {"hata": "oyuncu bulunamadı"}

print(get_player(2))
print(get_player(9))
```

## Görevler

### Görev 1: GET: tek oyuncu

`get_player(pid)` kimliği `pid` olan oyuncuyu bulursa `(200, oyuncu)`, bulamazsa `(404, {"hata": "bulunamadı"})` döndürsün.

**Başlangıç kodu:**

```python
players = [{"id": 1, "name": "Piko"}, {"id": 2, "name": "Ece"}]

def get_player(pid):
    pass

print(get_player(2))
print(get_player(7))
```

**İpuçları:**

1. Oyuncuları dolaş, id eşleşince return 200, p
2. Döngü bitince return 404, {"hata": "bulunamadı"}

<details><summary>Çözüm</summary>

```python
players = [{"id": 1, "name": "Piko"}, {"id": 2, "name": "Ece"}]

def get_player(pid):
    for p in players:
        if p["id"] == pid:
            return 200, p
    return 404, {"hata": "bulunamadı"}

print(get_player(2))
print(get_player(7))
```

</details>

### Görev 2: POST: yeni oyuncu

`create_player(body)`:

- `body` içinde `name` yoksa `(400, {"hata": "isim gerekli"})` döndürsün.
- Varsa yeni oyuncuyu `{"id": sıradaki_numara, "name": ...}` olarak ekleyip `(201, oyuncu)` döndürsün. Sıradaki numara, en büyük kimliğin bir fazlasıdır.

**Başlangıç kodu:**

```python
players = [{"id": 1, "name": "Piko"}, {"id": 4, "name": "Ece"}]

def create_player(body):
    pass

print(create_player({"name": "Can"}))
print(create_player({}))
```

**İpuçları:**

1. Önce kontrol: if "name" not in body:
2. En büyük kimlik: max([p["id"] for p in players])
3. Liste boşsa max hata verir; max(..., default=0) kullanabilirsin.

<details><summary>Çözüm</summary>

```python
players = [{"id": 1, "name": "Piko"}, {"id": 4, "name": "Ece"}]

def create_player(body):
    if "name" not in body:
        return 400, {"hata": "isim gerekli"}
    next_id = max([p["id"] for p in players], default=0) + 1
    player = {"id": next_id, "name": body["name"]}
    players.append(player)
    return 201, player

print(create_player({"name": "Can"}))
print(create_player({}))
```

</details>

### Görev 3: DELETE: oyuncu sil

`delete_player(pid)` oyuncuyu bulup silerse `(204, None)`, bulamazsa `(404, {"hata": "bulunamadı"})` döndürsün.

**Başlangıç kodu:**

```python
players = [{"id": 1, "name": "Piko"}, {"id": 2, "name": "Ece"}]

def delete_player(pid):
    pass

print(delete_player(1))
print(players)
```

**İpuçları:**

1. Oyuncuyu bulunca players.remove(p)
2. Sonra return 204, None

<details><summary>Çözüm</summary>

```python
players = [{"id": 1, "name": "Piko"}, {"id": 2, "name": "Ece"}]

def delete_player(pid):
    for p in players:
        if p["id"] == pid:
            players.remove(p)
            return 204, None
    return 404, {"hata": "bulunamadı"}

print(delete_player(1))
print(players)
```

</details>

## Challenge: Yönlendirici

`handle(method, path, body=None)` gelen isteği doğru fonksiyona göndersin:

- `GET /players` için `(200, players)`
- `GET /players/2` için `get_player(2)`
- `POST /players` için `create_player(body)`
- Diğer her şey için `(404, {"hata": "yol yok"})`

**Başlangıç kodu:**

```python
players = [{"id": 1, "name": "Piko"}]

def get_player(pid):
    for p in players:
        if p["id"] == pid:
            return 200, p
    return 404, {"hata": "bulunamadı"}

def create_player(body):
    player = {"id": len(players) + 1, "name": body["name"]}
    players.append(player)
    return 201, player

def handle(method, path, body=None):
    pass

print(handle("GET", "/players"))
print(handle("GET", "/players/1"))
```

**İpuçları:**

1. Adresi parçala: path.strip("/").split("/")
2. Parça sayısına ve metoda göre karar ver.
3. Kimliği int() ile sayıya çevir.

<details><summary>Çözüm</summary>

```python
players = [{"id": 1, "name": "Piko"}]

def get_player(pid):
    for p in players:
        if p["id"] == pid:
            return 200, p
    return 404, {"hata": "bulunamadı"}

def create_player(body):
    player = {"id": len(players) + 1, "name": body["name"]}
    players.append(player)
    return 201, player

def handle(method, path, body=None):
    parts = path.strip("/").split("/")
    if parts[0] != "players":
        return 404, {"hata": "yol yok"}
    if method == "GET" and len(parts) == 1:
        return 200, players
    if method == "GET" and len(parts) == 2 and parts[1].isdigit():
        return get_player(int(parts[1]))
    if method == "POST" and len(parts) == 1:
        return create_player(body)
    return 404, {"hata": "yol yok"}

print(handle("GET", "/players"))
print(handle("GET", "/players/1"))
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Oyun API'si**

### Piko'nun Macerası: Oyun API'si

Piko'nun Macerası'nın skor API'sini yazalım. `handle(method, path, body=None)`:

- `GET /scores`: skorları **büyükten küçüğe** sıralı döndürsün: `(200, liste)`
- `POST /scores`: `body`'de `name` ve `score` varsa ekleyip `(201, yeni_kayıt)` döndürsün, eksikse `(400, {"hata": "eksik bilgi"})`
- Başka her şey: `(404, {"hata": "yol yok"})`

**Başlangıç kodu:**

```python
scores = [{"name": "Piko", "score": 300}, {"name": "Ece", "score": 450}]

def handle(method, path, body=None):
    pass

print(handle("GET", "/scores"))
print(handle("POST", "/scores", {"name": "Can", "score": 120}))
```

**İpuçları:**

1. Önce yolu kontrol et: if path != "/scores":
2. GET için: sorted(scores, key=lambda s: s["score"], reverse=True)
3. POST için önce eksik bilgi var mı bak.

<details><summary>Çözüm</summary>

```python
scores = [{"name": "Piko", "score": 300}, {"name": "Ece", "score": 450}]

def handle(method, path, body=None):
    if path != "/scores":
        return 404, {"hata": "yol yok"}
    if method == "GET":
        return 200, sorted(scores, key=lambda s: s["score"], reverse=True)
    if method == "POST":
        if not body or "name" not in body or "score" not in body:
            return 400, {"hata": "eksik bilgi"}
        entry = {"name": body["name"], "score": body["score"]}
        scores.append(entry)
        return 201, entry
    return 404, {"hata": "yol yok"}

print(handle("GET", "/scores"))
print(handle("POST", "/scores", {"name": "Can", "score": 120}))
```

</details>

### Harcama Defteri: Harcama API'si

Telefonundaki bir uygulama harcama ekleyebilsin diye küçük bir API yazalım. `handle(method, path, body=None)`:

- `GET /expenses`: `(200, expenses)` döndürsün.
- `POST /expenses`: `body`'de `category` ve **0'dan büyük** bir `amount` varsa belgeyi ekleyip `(201, body)` döndürsün; yoksa `(400, {"hata": "geçersiz harcama"})`.
- Başka her istek için `(404, {"hata": "bulunamadı"})`.

**Başlangıç kodu:**

```python
expenses = []


def handle(method, path, body=None):
    pass
```

**İpuçları:**

1. Önce path'e, sonra method'a bak.
2. body.get("amount", 0) > 0 tutarın pozitif olduğunu kontrol eder.

<details><summary>Çözüm</summary>

```python
expenses = []


def handle(method, path, body=None):
    if path == "/expenses" and method == "GET":
        return (200, expenses)
    if path == "/expenses" and method == "POST":
        if body and body.get("category") and body.get("amount", 0) > 0:
            expenses.append(body)
            return (201, body)
        return (400, {"hata": "geçersiz harcama"})
    return (404, {"hata": "bulunamadı"})
```

</details>

### Görev Asistanı: Görev API'si

Asistana telefondan görev eklenebilsin diye küçük bir API yazalım. `handle(method, path, body=None)`:

- `GET /tasks`: `(200, tasks)` döndürsün.
- `POST /tasks`: `body`'de boş olmayan bir `title` varsa `{"id": ..., "title": ...}` görevini ekleyip `(201, görev)` döndürsün (`id` 1'den başlayıp artsın); yoksa `(400, {"hata": "başlık gerekli"})`.
- `DELETE /tasks/<id>`: o id'li görevi silip `(204, None)`, yoksa `(404, {"hata": "bulunamadı"})`.
- Başka her şey: `(404, {"hata": "bulunamadı"})`.

**Başlangıç kodu:**

```python
tasks = []


def handle(method, path, body=None):
    pass
```

**İpuçları:**

1. path.startswith("/tasks/") ve path.split("/")[-1] id'yi verir.
2. id'leri karşılaştırırken yazı/sayı farkına dikkat: str(task["id"])

<details><summary>Çözüm</summary>

```python
tasks = []


def handle(method, path, body=None):
    if path == "/tasks" and method == "GET":
        return (200, tasks)
    if path == "/tasks" and method == "POST":
        if body and body.get("title"):
            task = {"id": len(tasks) + 1, "title": body["title"]}
            tasks.append(task)
            return (201, task)
        return (400, {"hata": "başlık gerekli"})
    if method == "DELETE" and path.startswith("/tasks/"):
        task_id = path.split("/")[-1]
        for task in tasks:
            if str(task["id"]) == task_id:
                tasks.remove(task)
                return (204, None)
    return (404, {"hata": "bulunamadı"})
```

</details>

### Kişisel Web Sitem: Blog API'si

Sitene başka uygulamalardan da yazı eklenebilsin diye küçük bir blog API'si yazalım. `handle(method, path, body=None)`:

- `GET /posts`: `(200, posts)` döndürsün.
- `POST /posts`: `body`'de boş olmayan bir `title` varsa `{"id": ..., "title": ..., "slug": ...}` belgesini oluştursun (`id` 1'den başlar; `slug` başlığın küçük harfli, boşlukları `-` olan hâli), listeye ekleyip `(201, belge)` döndürsün. Yoksa `(400, {"hata": "başlık gerekli"})`.
- `GET /posts/2` gibi bir adres: o `id`'li yazıyı `(200, yazı)` ile döndürsün.
- Başka her istek (ya da bulunamayan yazı) için `(404, {"hata": "bulunamadı"})`.

**Başlangıç kodu:**

```python
posts = []


def handle(method, path, body=None):
    pass
```

**İpuçları:**

1. path.startswith("/posts/") ve path.split("/")[-1] adresteki id'yi verir.
2. id'leri karşılaştırırken yazı/sayı farkına dikkat: str(post["id"]) == post_id

<details><summary>Çözüm</summary>

```python
posts = []


def handle(method, path, body=None):
    if method == "GET" and path == "/posts":
        return (200, posts)
    if method == "POST" and path == "/posts":
        if body and body.get("title"):
            title = body["title"]
            post = {"id": len(posts) + 1, "title": title, "slug": title.lower().replace(" ", "-")}
            posts.append(post)
            return (201, post)
        return (400, {"hata": "başlık gerekli"})
    if method == "GET" and path.startswith("/posts/"):
        post_id = path.split("/")[-1]
        for post in posts:
            if str(post["id"]) == post_id:
                return (200, post)
    return (404, {"hata": "bulunamadı"})
```

</details>

### Sohbet Botu: Sohbet API'si

Botla bir telefon uygulaması da konuşabilsin diye küçük bir API yazalım. `handle(method, path, body=None)`:

- `POST /chat`: `body`'de boş olmayan bir `message` varsa cevabı bul: `replies` içindeki anahtar kelimelerden mesajda geçen ilkinin cevabı, hiçbiri yoksa `"Bunu anlamadım."`. `{"user": mesaj, "bot": cevap}` kaydını `history`'ye ekle ve `(200, {"reply": cevap})` döndür. Mesaj yoksa ya da boşsa `(400, {"hata": "mesaj boş"})`.
- `GET /history`: `(200, history)`
- `DELETE /history`: geçmişi temizle (`history.clear()`) ve `(204, None)` döndür.
- Başka her istek: `(404, {"hata": "bulunamadı"})`.

**Başlangıç kodu:**

```python
replies = {"merhaba": "Merhaba!", "hava": "Bugün hava güneşli."}
history = []


def handle(method, path, body=None):
    pass
```

**İpuçları:**

1. Önce path'e ve method'a bak: if path == "/chat" and method == "POST":
2. not body or not body.get("message") mesajın olmadığını ya da boş olduğunu yakalar.

<details><summary>Çözüm</summary>

```python
replies = {"merhaba": "Merhaba!", "hava": "Bugün hava güneşli."}
history = []


def handle(method, path, body=None):
    if path == "/chat" and method == "POST":
        if not body or not body.get("message"):
            return (400, {"hata": "mesaj boş"})
        message = body["message"]
        reply = "Bunu anlamadım."
        for keyword in replies:
            if keyword in message:
                reply = replies[keyword]
                break
        history.append({"user": message, "bot": reply})
        return (200, {"reply": reply})
    if path == "/history" and method == "GET":
        return (200, history)
    if path == "/history" and method == "DELETE":
        history.clear()
        return (204, None)
    return (404, {"hata": "bulunamadı"})
```

</details>

### Okul Not Defteri: Not API'si

Telefonundaki bir uygulama notlarını görebilsin ve not ekleyebilsin diye küçük bir API yazalım. Notlar `grades` sözlüğünde (ders -> not). `handle(method, path, body=None)`:

- `GET /grades`: `(200, grades)` döndürsün.
- `GET /grades/Fizik`: ders varsa `(200, {"lesson": "Fizik", "grade": 70})`, yoksa `(404, {"hata": "ders bulunamadı"})`.
- `POST /grades`: `body`'de `lesson` ve **0 ile 100 arasında** bir `grade` varsa notu kaydedip `(201, body)` döndürsün; yoksa `(400, {"hata": "geçersiz not"})`.
- Başka her istek için `(404, {"hata": "bulunamadı"})`.

**Başlangıç kodu:**

```python
grades = {}


def handle(method, path, body=None):
    pass
```

**İpuçları:**

1. "/grades/Fizik".split("/") sonucu ['', 'grades', 'Fizik'] olur.
2. 0 <= body.get("grade", -1) <= 100 notun geçerli olup olmadığını kontrol eder.

<details><summary>Çözüm</summary>

```python
grades = {}


def handle(method, path, body=None):
    parts = path.split("/")
    if path == "/grades" and method == "GET":
        return (200, grades)
    if path == "/grades" and method == "POST":
        if body and body.get("lesson") and 0 <= body.get("grade", -1) <= 100:
            grades[body["lesson"]] = body["grade"]
            return (201, body)
        return (400, {"hata": "geçersiz not"})
    if len(parts) == 3 and parts[1] == "grades" and method == "GET":
        lesson = parts[2]
        if lesson in grades:
            return (200, {"lesson": lesson, "grade": grades[lesson]})
        return (404, {"hata": "ders bulunamadı"})
    return (404, {"hata": "bulunamadı"})
```

</details>
