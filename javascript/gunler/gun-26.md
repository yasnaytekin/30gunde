# Gün 26: fetch ve API

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Async İstasyonu  ·  **Maskot:** Kodi

**Bugünün hedefi:** fetch ile bir API'den JSON veri almak, hataları yönetmek ve gelen veriyi sayfada göstermek

> Async İstasyonu'nun dev anteni açıldı, kaptan! Artık uzaktaki sunuculardan veri isteyebiliriz. Bugün **fetch** ile bir **API**'ye soru soracak, gelen cevabı sayfaya dökeceğiz.

![Async İstasyonu](../../gorseller/javascript/bolgeler/istasyon.webp)

## Konu anlatımı

### API nedir?

**API**, bir programın başka programlara açtığı kapıdır. Belli bir adrese istek gönderirsin, sunucu sana veri döndürür. Hava durumu uygulaması sıcaklığı, harita uygulaması konumları böyle alır.

Çoğu API cevabı **JSON** biçiminde verir (12. günü hatırla). Bu kursta önizleme gerçek internete çıkmaz; senin için hazırlanmış bir deneme API'si var:

| Adres | Ne döndürür? |
| --- | --- |
| `/demo-api/sehirler` | 8 şehir: `ad`, `bolge`, `nufus`, `sicaklik` |
| `/demo-api/sorular` | 5 soru: `soru`, `secenekler`, `dogru` |
| `/demo-api/seviyeler/1` (2, 3) | Bir oyun seviyesi: `seviye`, `yildiz`, `dusman`, `hiz` |
| `/demo-api/gorevler` | 4 görev: `id`, `baslik`, `bitti` |
| `/demo-api/yazilar` | 3 blog yazısı: `id`, `baslik`, `ozet` |
| `/demo-api/hata` | Her zaman hata (500) verir: denemek için |

### fetch ve res.json()

```js
async function loadCities() {
  const res = await fetch("/demo-api/sehirler");
  const cities = await res.json();
  console.log(cities.length, "şehir geldi");
}
loadCities();
```

- `fetch(adres)` isteği gönderir ve bir **Promise** döndürür (25. gün!). `await` ile cevabı bekleriz.
- Gelen cevap (`res`) bir zarf gibidir. İçindeki veriyi okumak için bir kez daha bekleriz: `await res.json()`.
- İki `await` var, çünkü önce cevabın başlığı, sonra gövdesi gelir.

### res.ok ve durum kodları

Her cevabın bir **durum kodu** (status) vardır:

| Kod | Anlamı |
| --- | --- |
| `200` | Tamam |
| `404` | Bulunamadı (adres yanlış) |
| `500` | Sunucuda bir sorun var |

Dikkat: `fetch`, 404 ya da 500 gelince hata **fırlatmaz**! Kontrol etmek senin işin:

```js
const res = await fetch("/demo-api/hata");
if (!res.ok) {
  console.log("Olmadı, durum kodu:", res.status);
  return;
}
```

`res.ok`, kod 200 ile 299 arasındaysa `true` olur. Bağlantı hiç kurulamazsa `fetch` gerçekten hata fırlatır; onu `try/catch` ile yakalarsın (24. gün).

### Sorgu metni ve yükleniyor durumu

Adresin sonuna `?anahtar=değer` ekleyerek sunucudan süzülmüş veri isteyebilirsin: `/demo-api/sehirler?bolge=Ege` yalnızca Ege'deki şehirleri getirir. Değerde boşluk ya da Türkçe harf varsa `encodeURIComponent` ile güvenli hale getir:

```js
const region = "İç Anadolu";
const url = `/demo-api/sehirler?bolge=${encodeURIComponent(region)}`;
```

İyi bir sayfa kullanıcıyı bekletirken bilgilendirir. Her istekte üç durumu düşün:

- **Yükleniyor**: istekten önce `Yükleniyor...` yaz.
- **Başarılı**: veriyi sayfada göster.
- **Hata**: anlaşılır bir mesaj ver, sayfayı boş bırakma.

## Örnekler

### Şehirleri getir

Sayfa:

```html
<p id="info">Yükleniyor...</p>
<ul id="list"></ul>
```

```js
const info = document.querySelector("#info");
const list = document.querySelector("#list");

async function loadCities() {
  const res = await fetch("/demo-api/sehirler");
  const cities = await res.json();
  for (const city of cities) {
    const li = document.createElement("li");
    li.textContent = `${city.ad}: ${city.sicaklik}°C`;
    list.append(li);
  }
  info.textContent = `${cities.length} şehir geldi.`;
}

loadCities();
```

*Önce 'Yükleniyor...' görünür, kısa bir süre sonra liste gelir.*

### Hata durumunu yakala

Sayfa:

```html
<button id="good">Doğru adres</button> <button id="bad">Hatalı adres</button>
<p id="info">Bir düğmeye bas.</p>
```

```js
const info = document.querySelector("#info");

async function load(url) {
  info.textContent = "Yükleniyor...";
  try {
    const res = await fetch(url);
    if (!res.ok) {
      info.textContent = `Hata! Durum kodu: ${res.status}`;
      return;
    }
    const posts = await res.json();
    info.textContent = `Başarılı: ${posts.length} yazı geldi.`;
  } catch (err) {
    info.textContent = "Bağlantı kurulamadı.";
  }
}

document.querySelector("#good").addEventListener("click", () => load("/demo-api/yazilar"));
document.querySelector("#bad").addEventListener("click", () => load("/demo-api/hata"));
```

*İki düğmeyi de dene: hatalı adres 500 durum kodunu gösterir.*

## Görevler

### Görev 1: Şehir listesi

`loadCities()` fonksiyonunu tamamla:

- `/demo-api/sehirler` adresinden şehirleri `fetch` ile al.
- Her şehir için `#list`'e `İstanbul (19°C)` biçiminde bir `<li>` ekle.
- Sonunda `#info`'ya kaç şehir geldiğini yaz: `8 şehir yüklendi` (sayı veriden gelsin).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2>Şehir İstasyonu</h2>
<p id="info">Hazır.</p>
<ul id="list"></ul>
```

**CSS:**

```css
#list li{padding:2px 0}#regions button{margin:4px}
```

**Başlangıç kodu:**

```js
const list = document.querySelector("#list");
const info = document.querySelector("#info");

async function loadCities() {
  // 1) fetch ile iste  2) res.json() ile oku  3) her şehir için <li> ekle
}

loadCities();
```

**İpuçları:**

1. const res = await fetch("/demo-api/sehirler");
2. const cities = await res.json(); sonra for...of ile dolaş.
3. Sayı için cities.length kullan.

<details><summary>Çözüm</summary>

```js
const list = document.querySelector("#list");
const info = document.querySelector("#info");

async function loadCities() {
  // 1) fetch ile iste  2) res.json() ile oku  3) her şehir için <li> ekle
  const res = await fetch("/demo-api/sehirler");
  const cities = await res.json();
  for (const city of cities) {
    const li = document.createElement("li");
    li.textContent = `${city.ad} (${city.sicaklik}°C)`;
    list.append(li);
  }
  info.textContent = `${cities.length} şehir yüklendi`;
}

loadCities();
```

</details>

### Görev 2: Bölge filtresi

Düğmeler hazır: her biri `loadRegion(bölge)` fonksiyonunu çağırıyor. Fonksiyonu sen yaz:

- Adrese sorgu metni ekleyerek iste: `/demo-api/sehirler?bolge=...` (değeri `encodeURIComponent` ile ver).
- Önce `#list`'i temizle, sonra her şehrin **adını** bir `<li>` olarak ekle.
- `#info`'ya `İç Anadolu: 2 şehir` biçiminde özet yaz.

Süzmeyi sunucu yapsın: `?bolge=Anadolu` adında Anadolu geçen 4 şehri getirir.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2>Şehir İstasyonu</h2>
<p id="info">Hazır.</p>
<ul id="list"></ul>

<div id="regions"><button data-region="Ege">Ege</button><button data-region="İç Anadolu">İç Anadolu</button><button data-region="Karadeniz">Karadeniz</button></div>
```

**CSS:**

```css
#list li{padding:2px 0}#regions button{margin:4px}
```

**Başlangıç kodu:**

```js
const list = document.querySelector("#list");
const info = document.querySelector("#info");

async function loadRegion(region) {
  // sorgu metniyle iste, listeyi temizle, adları ekle, özeti yaz
}

for (const btn of document.querySelectorAll("#regions button")) {
  btn.addEventListener("click", () => loadRegion(btn.dataset.region));
}
```

**İpuçları:**

1. fetch(`/demo-api/sehirler?bolge=${encodeURIComponent(region)}`)
2. Listeyi temizlemek için: list.innerHTML = "";

<details><summary>Çözüm</summary>

```js
const list = document.querySelector("#list");
const info = document.querySelector("#info");

async function loadRegion(region) {
  // sorgu metniyle iste, listeyi temizle, adları ekle, özeti yaz
  const res = await fetch(`/demo-api/sehirler?bolge=${encodeURIComponent(region)}`);
  const cities = await res.json();
  list.innerHTML = "";
  for (const city of cities) {
    const li = document.createElement("li");
    li.textContent = city.ad;
    list.append(li);
  }
  info.textContent = `${region}: ${cities.length} şehir`;
}

for (const btn of document.querySelectorAll("#regions button")) {
  btn.addEventListener("click", () => loadRegion(btn.dataset.region));
}
```

</details>

### Görev 3: Yükleniyor ve hata

`loadData(url)` üç durumu da göstersin (`#info`'da):

- İstekten önce: `Yükleniyor...` (bu satır hazır)
- Cevap başarılıysa: `Tamam: 4 kayıt` (gelen dizinin uzunluğu)
- `res.ok` değilse: `Hata: 404` (durum kodu `res.status`'tan gelsin)
- Bağlantı hiç kurulamazsa (`catch`): `Bağlantı kurulamadı`

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2>Veri İstasyonu</h2>
<p id="info">Hazır.</p>
```

**Başlangıç kodu:**

```js
const info = document.querySelector("#info");

async function loadData(url) {
  info.textContent = "Yükleniyor...";
  // try içinde fetch et; res.ok değilse durum kodunu, başarılıysa kayıt sayısını yaz
  // catch içinde bağlantı hatasını yaz
}

loadData("/demo-api/gorevler");
```

**İpuçları:**

1. if (!res.ok) { info.textContent = `Hata: ${res.status}`; return; }
2. Bütün isteği try { ... } catch (err) { ... } içine al.

<details><summary>Çözüm</summary>

```js
const info = document.querySelector("#info");

async function loadData(url) {
  info.textContent = "Yükleniyor...";
  // try içinde fetch et; res.ok değilse durum kodunu, başarılıysa kayıt sayısını yaz
  // catch içinde bağlantı hatasını yaz
  try {
    const res = await fetch(url);
    if (!res.ok) {
      info.textContent = `Hata: ${res.status}`;
      return;
    }
    const data = await res.json();
    info.textContent = `Tamam: ${data.length} kayıt`;
  } catch (err) {
    info.textContent = "Bağlantı kurulamadı";
  }
}

loadData("/demo-api/gorevler");
```

</details>

## Challenge: En sıcak şehir

`showHottest(region)` bir bölgedeki **en sıcak** şehri bulsun:

- `/demo-api/sehirler?bolge=...` ile şehirleri iste (boş bölge `""` bütün şehirleri getirir).
- En yüksek `sicaklik`'lı şehri bul (`reduce` ya da döngüyle).
- `#info`'ya `En sıcak: Antalya (26°C)` yaz. Hiç şehir gelmezse `Şehir bulunamadı` yaz.

Şehir adını elle yazma: sonuç veriden gelsin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2>Şehir İstasyonu</h2>
<p id="info">Hazır.</p>
<ul id="list"></ul>
```

**CSS:**

```css
#list li{padding:2px 0}#regions button{margin:4px}
```

**Başlangıç kodu:**

```js
const info = document.querySelector("#info");

async function showHottest(region) {
  // iste, en sıcak şehri bul, yaz
}

showHottest("");
```

**İpuçları:**

1. cities.reduce((best, city) => (city.sicaklik > best.sicaklik ? city : best))
2. Boş diziyle reduce hata verir: önce cities.length === 0 durumunu kontrol et.

<details><summary>Çözüm</summary>

```js
const info = document.querySelector("#info");

async function showHottest(region) {
  // iste, en sıcak şehri bul, yaz
  const res = await fetch(`/demo-api/sehirler?bolge=${encodeURIComponent(region)}`);
  const cities = await res.json();
  if (cities.length === 0) {
    info.textContent = "Şehir bulunamadı";
    return;
  }
  const hottest = cities.reduce((best, city) => (city.sicaklik > best.sicaklik ? city : best));
  info.textContent = `En sıcak: ${hottest.ad} (${hottest.sicaklik}°C)`;
}

showHottest("");
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Seviyeleri sunucudan almak**

### Yıldız Avcısı: Seviyeleri sunucudan al

Oyunun seviyeleri artık sunucuda! Seviye düğmeleri hazır; `loadLevel(n)` fonksiyonunu yaz:

- `/demo-api/seviyeler/` adresinin sonuna `n` ekleyerek iste.
- Başarılıysa seviyeyi `currentLevel`'a kaydet ve `#info`'ya yaz: `Seviye 2: 8 yıldız, 3 düşman, hız 3`
- `res.ok` değilse (4. seviye henüz yok, 404 gelir): `Seviye 4 henüz hazır değil.` yaz; `currentLevel` değişmesin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1 id="title">Yıldız Avcısı</h1>
<p id="info">Bir seviye seç.</p>
<div id="levels"><button data-level="1">Seviye 1</button><button data-level="2">Seviye 2</button><button data-level="3">Seviye 3</button><button data-level="4">Seviye 4</button></div>
```

**CSS:**

```css
#title{color:#0b1026}canvas{background:#0b1026;display:block;max-width:100%;border-radius:6px}#levels button{margin:4px}.controls button{font-size:22px;min-width:56px;min-height:48px;margin:4px}section h1,section h2{color:#0b1026}
```

**Başlangıç kodu:**

```js
let currentLevel = null;
const info = document.querySelector("#info");

async function loadLevel(n) {
  info.textContent = "Yükleniyor...";
  // /demo-api/seviyeler/n adresini iste
  // res.ok değilse: Seviye n henüz hazır değil.
  // başarılıysa: currentLevel = seviye; bilgiyi yaz
}

for (const btn of document.querySelectorAll("#levels button")) {
  btn.addEventListener("click", () => loadLevel(Number(btn.dataset.level)));
}
```

**İpuçları:**

1. const res = await fetch(`/demo-api/seviyeler/${n}`);
2. if (!res.ok) { ...; return; } ile hatalı seviyeyi erkenden ele.
3. const level = await res.json(); sonra level.yildiz, level.dusman, level.hiz

<details><summary>Çözüm</summary>

```js
let currentLevel = null;
const info = document.querySelector("#info");

async function loadLevel(n) {
  info.textContent = "Yükleniyor...";
  const res = await fetch(`/demo-api/seviyeler/${n}`);
  if (!res.ok) {
    info.textContent = `Seviye ${n} henüz hazır değil.`;
    return;
  }
  const level = await res.json();
  currentLevel = level;
  info.textContent = `Seviye ${level.seviye}: ${level.yildiz} yıldız, ${level.dusman} düşman, hız ${level.hiz}`;
}

for (const btn of document.querySelectorAll("#levels button")) {
  btn.addEventListener("click", () => loadLevel(Number(btn.dataset.level)));
}
```

</details>

### Kişisel Web Sitem: Blog yazılarını getir

Sitenin blog bölümü yazıları sunucudan alsın. `loadPosts(url)` fonksiyonunu tamamla:

- `url` adresinden yazıları iste (varsayılan: `/demo-api/yazilar`).
- Başarılıysa `#posts`'u temizle ve her yazı için bir kart ekle: `<article class="card">` içinde `<h3>` (başlık) ve `<p>` (özet).
- Cevap başarısızsa ya da bağlantı kurulamazsa `#posts`'a `Yazılar yüklenemedi.` yaz.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<header><h1 id="site-title">Kod Günlüğüm</h1></header>
<main><h2>Blog</h2>
<div id="posts"></div></main>
```

**CSS:**

```css
header{display:flex;align-items:center;gap:12px;flex-wrap:wrap}header h1{margin:0;font-size:22px}nav a{margin-right:10px}.card{border:1px solid #ccd;border-radius:8px;padding:8px 12px;margin:8px 0}.card h3{margin:0 0 4px}.tech{color:#556;font-size:14px}body.dark{background:#0b1026;color:#eef}body.dark a{color:#9cf}form{display:grid;gap:6px;max-width:320px}
```

**Başlangıç kodu:**

```js
const posts = document.querySelector("#posts");

async function loadPosts(url = "/demo-api/yazilar") {
  posts.textContent = "Yükleniyor...";
  // iste; başarılıysa kartları çiz, değilse hata mesajı yaz
}

loadPosts();
```

**İpuçları:**

1. if (!res.ok) throw new Error(...) yazarsan hatalı cevap da catch'e düşer.
2. Kart: document.createElement("article"), card.className = "card"
3. card.append(title, summary); posts.append(card);

<details><summary>Çözüm</summary>

```js
const posts = document.querySelector("#posts");

async function loadPosts(url = "/demo-api/yazilar") {
  posts.textContent = "Yükleniyor...";
  try {
    const res = await fetch(url);
    if (!res.ok) throw new Error(`Durum kodu ${res.status}`);
    const data = await res.json();
    posts.textContent = "";
    for (const post of data) {
      const card = document.createElement("article");
      card.className = "card";
      const title = document.createElement("h3");
      title.textContent = post.baslik;
      const summary = document.createElement("p");
      summary.textContent = post.ozet;
      card.append(title, summary);
      posts.append(card);
    }
  } catch (err) {
    posts.textContent = "Yazılar yüklenemedi.";
  }
}

loadPosts();
```

</details>

### Çalışma Asistanım: Görevleri getir

Asistan görevleri sunucudan alsın. İki fonksiyonu tamamla:

- `renderTasks(tasks)`: `#tasks` listesini temizlesin, her görev için `baslik`'ı yazan bir `<li>` eklesin; `bitti` olanlara `done` sınıfı versin. `#count`'a kalan görev sayısını yazsın: `2 görev kaldı`.
- `loadTasks()`: `/demo-api/gorevler` adresinden görevleri alıp `renderTasks`'e versin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1>Çalışma Asistanım</h1>
<p id="count"></p>
<ul id="tasks"></ul>
```

**CSS:**

```css
li{padding:6px;cursor:pointer}li.done{text-decoration:line-through;color:#889}li.selected{outline:2px solid #3b6ef5;border-radius:4px}.big{font-size:20px;min-width:64px;min-height:48px;margin:4px}#stats,#count{font-weight:bold}form{display:flex;gap:6px}
```

**Başlangıç kodu:**

```js
const list = document.querySelector("#tasks");
const count = document.querySelector("#count");

function renderTasks(tasks) {
  // listeyi temizle, her görev için <li> ekle (bitti ise done sınıfı), kalanı yaz
}

async function loadTasks() {
  // /demo-api/gorevler adresinden al, renderTasks'e ver
}

loadTasks();
```

**İpuçları:**

1. if (task.bitti) li.classList.add("done");
2. Kalan: tasks.filter((t) => !t.bitti).length
3. loadTasks içinde: const tasks = await res.json(); renderTasks(tasks);

<details><summary>Çözüm</summary>

```js
const list = document.querySelector("#tasks");
const count = document.querySelector("#count");

function renderTasks(tasks) {
  list.innerHTML = "";
  for (const task of tasks) {
    const li = document.createElement("li");
    li.textContent = task.baslik;
    if (task.bitti) li.classList.add("done");
    list.append(li);
  }
  const left = tasks.filter((t) => !t.bitti).length;
  count.textContent = `${left} görev kaldı`;
}

async function loadTasks() {
  count.textContent = "Yükleniyor...";
  const res = await fetch("/demo-api/gorevler");
  if (!res.ok) {
    count.textContent = "Görevler alınamadı.";
    return;
  }
  const tasks = await res.json();
  renderTasks(tasks);
}

loadTasks();
```

</details>

### Bilgi Yarışması: Soruları getir

Sorular artık sunucuda. İki fonksiyonu tamamla:

- `loadQuestions()`: `/demo-api/sorular` adresinden soruları alıp `questions` değişkenine koysun, sonra `showQuestion(0)` çağırsın.
- `showQuestion(index)`: `#question`'a `Soru 1: Ay, hangi gezegenin uydusudur?` biçiminde soruyu yazsın; `#options`'ı temizleyip her seçenek için bir `<button>` eklesin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1>Bilgi Yarışması</h1>
<p id="question">Sorular yükleniyor...</p>
<div id="options"></div>
<p id="feedback"></p>
```

**CSS:**

```css
#options button{display:block;width:100%;max-width:320px;margin:6px 0;padding:10px;font-size:18px}#feedback{font-weight:bold}
```

**Başlangıç kodu:**

```js
let questions = [];
const questionEl = document.querySelector("#question");
const options = document.querySelector("#options");

function showQuestion(index) {
  // soruyu yaz, seçenek düğmelerini ekle
}

async function loadQuestions() {
  // soruları al, questions'a koy, ilk soruyu göster
}

loadQuestions();
```

**İpuçları:**

1. questions = await res.json(); (let ile tanımlı olduğu için yeniden atanabilir)
2. Soru metni: `Soru ${index + 1}: ${q.soru}`
3. Her seçenek için document.createElement("button")

<details><summary>Çözüm</summary>

```js
let questions = [];
const questionEl = document.querySelector("#question");
const options = document.querySelector("#options");

function showQuestion(index) {
  const q = questions[index];
  questionEl.textContent = `Soru ${index + 1}: ${q.soru}`;
  options.innerHTML = "";
  q.secenekler.forEach((text) => {
    const btn = document.createElement("button");
    btn.textContent = text;
    options.append(btn);
  });
}

async function loadQuestions() {
  const res = await fetch("/demo-api/sorular");
  if (!res.ok) {
    questionEl.textContent = "Sorular yüklenemedi.";
    return;
  }
  questions = await res.json();
  showQuestion(0);
}

loadQuestions();
```

</details>
