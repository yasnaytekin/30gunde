# Gün 30: Final

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** JavaScript Yıldızı  ·  **Maskot:** Kodi

**Bugünün hedefi:** Öğrendiklerini tek bir projede birleştirmek, projeni yayınlamayı ve sonraki adımları öğrenmek

> Karşında parıldayan ışık **JavaScript Yıldızı**, kaptan! 30 günlük yolculuğun son durağındasın. Bugün parçaları birleştirip projeni bitiriyor ve onu dünyaya göstermeye hazırlanıyorsun.

![JavaScript Yıldızı](../../gorseller/javascript/bolgeler/yildiz.webp)

## Konu anlatımı

### Neler öğrendin?

| Bölge | Öğrendiklerin |
| --- | --- |
| Kalkış Üssü | değişkenler, veri türleri, operatörler, metinler |
| Döngü Ayı | koşullar, diziler, döngüler, fonksiyonlar |
| Fonksiyon Nebulası | kapsam, nesneler, map/filter/reduce, JSON |
| DOM Gezegeni | sayfayı değiştirmek, olaylar, eleman oluşturmak, formlar |
| Olay Kuşağı | klavye, zamanlayıcılar, CSS, localStorage |
| Piksel Gezegeni | canvas, animasyon, oyun döngüsü |
| Async İstasyonu | hatalar, Promise, fetch, sınıflar |
| JavaScript Yıldızı | temiz kod, erişilebilirlik, final projesi |

Bu, bir web geliştiricisinin her gün kullandığı temel araç kutusu. Artık sıfırdan etkileşimli bir sayfa yazabilirsin!

### Projeni yayınla

Kursta kodun tek bir kutuda çalıştı. Gerçek bir sitede genelde üç dosya olur:

- `index.html`: sayfanın iskeleti (görevlerdeki HTML)
- `style.css`: görünüş
- `script.js`: davranış, yani bugüne kadar yazdığın kod

`index.html`, bu ikisini şöyle bağlar: `<link rel="stylesheet" href="style.css">` ve `<script src="script.js" defer></script>`.

Bu dosyaları bir **statik site** servisine yükleyince herkesin açabileceği bir adresin olur. Yaygın iki seçenek: **GitHub Pages** (dosyaları bir GitHub deposuna koyup ayarlardan Pages'i açarsın) ve **Netlify** (klasörü sürükleyip bırakırsın). Adımlar kabaca şöyle:

1. Bilgisayarında bir klasör aç, üç dosyayı içine koy.
2. `index.html`'i tarayıcıda açıp dene; Konsol'da kırmızı hata olmasın.
3. Bir yetişkinle birlikte servise hesap aç (çoğu servis 13 yaş ve üstünü ister).
4. Dosyaları yükle, sana verilen adresi aç ve arkadaşlarınla paylaş.

Paylaşmadan önce sayfada tam adın, okulun, adresin ya da telefonun gibi **kişisel bilgiler** olmadığından emin ol.

### Sıradaki durak

- **Daha çok proje**: En iyi öğrenme yolu yapmaktır. Bir hesap makinesi, bir çizim uygulaması, sınıfın için bir yarışma...
- **TypeScript**: JavaScript'e tür denetimi ekler; bazı hataları kod çalışmadan yakalar.
- **React, Vue, Svelte**: büyük arayüzleri bileşenlerle kurmaya yarar. `render()` fikrini hatırla: bu araçlar onu senin yerine akıllıca yapar.
- **Node.js**: JavaScript'i tarayıcının dışında, sunucuda çalıştırır. Bu kursta kullandığın `/demo-api` gibi bir API'yi kendin yazabilirsin!
- **Oyun kütüphaneleri**: Phaser gibi kütüphanelerle canvas oyunlarını daha hızlı yaparsın.
- Python kursunu da bitirdiysen artık iki dil biliyorsun: kavramlar (değişken, döngü, fonksiyon, sınıf) aynı, yalnızca yazılış farklı.

### Son kontrol listesi

Projeni paylaşmadan önce kendine sor:

- Konsolda kırmızı bir hata var mı?
- Telefonda (küçük ekranda) açılıyor ve kullanılabiliyor mu?
- Her şey klavyeyle de yapılabiliyor mu? Simge düğmelerin `aria-label`'ı var mı?
- Değişken ve fonksiyon adları anlaşılır mı? Tekrarlanan kod kaldı mı?
- Veri gelmezse (fetch hatası) kullanıcı ne görüyor?

Tebrikler, kaptan: 30 günde sıfırdan çalışan projeler yazan bir JavaScript geliştiricisi oldun. Bu bir son değil, yeni bir **kalkış**!

## Örnekler

### Hepsi bir arada: yıldız sayacı

Sayfa:

```html
<p id="count" aria-live="polite"></p>
<button id="plus">Yıldız topla</button> <button id="reset">Sıfırla</button>
```

```js
const COUNT_KEY = "stars";
const state = { stars: Number(localStorage.getItem(COUNT_KEY)) || 0 };
const countEl = document.querySelector("#count");

function update(action) {
  if (action === "plus") state.stars += 1;
  if (action === "reset") state.stars = 0;
  localStorage.setItem(COUNT_KEY, String(state.stars));
}

function render() {
  countEl.textContent = `${state.stars} yıldız`;
}

function init() {
  document.querySelector("#plus").addEventListener("click", () => {
    update("plus");
    render();
  });
  document.querySelector("#reset").addEventListener("click", () => {
    update("reset");
    render();
  });
  render();
}

init();
```

*Birkaç kez tıkla, sonra yeniden Çalıştır: sayı kaldığı yerden devam eder.*

### Sınıf ve fetch: yazı kartları

Sayfa:

```html
<div id="posts">Yükleniyor...</div>
```

```js
class PostCard {
  constructor({ baslik, ozet }) {
    this.title = baslik;
    this.summary = ozet;
  }

  render() {
    const card = document.createElement("article");
    card.className = "card";
    const h3 = document.createElement("h3");
    h3.textContent = this.title;
    const p = document.createElement("p");
    p.textContent = this.summary;
    card.append(h3, p);
    return card;
  }
}

async function init() {
  const box = document.querySelector("#posts");
  try {
    const res = await fetch("/demo-api/yazilar");
    if (!res.ok) throw new Error(`Durum kodu ${res.status}`);
    const posts = await res.json();
    box.textContent = "";
    posts.forEach((post) => box.append(new PostCard(post).render()));
  } catch (err) {
    box.textContent = "Yazılar yüklenemedi.";
  }
}

init();
```

*Sınıf, parçalama, fetch, hata yakalama ve DOM: hepsi bir arada.*

## Görevler

### Görev 1: Mezuniyet kartı

Kurs bitti, kartını oluştur! Form ve `localStorage` birlikte çalışsın:

- `showCard(name)`: `#card`'ın içine `<h2>` (`Tebrikler, Ada!`) ve `<p>` (`30 Günde JavaScript yolculuğunu tamamladı.`) koysun.
- Sayfa açılınca `localStorage`'da `graduate` anahtarı varsa kart hemen görünsün.
- Form gönderilince: sayfa yenilenmesin, ad `trim` ile temizlensin; boşsa hiçbir şey yapılmasın; değilse ad `graduate` anahtarına kaydedilsin ve kart gösterilsin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<form id="f"><input id="name" placeholder="Adın" aria-label="Adın"><button>Kartımı oluştur</button></form>
<div id="card"></div>
```

**CSS:**

```css
#card{border:2px solid #f7df1e;border-radius:10px;padding:8px 14px;margin-top:10px}#card:empty{display:none}form{display:flex;gap:6px}
```

**Başlangıç kodu:**

```js
const form = document.querySelector("#f");
const card = document.querySelector("#card");

function showCard(name) {
  // h2 ve p
}

// açılışta kayıtlı ad varsa göster

// form gönderilince
```

**İpuçları:**

1. const saved = localStorage.getItem("graduate"); if (saved) showCard(saved);
2. Formda: e.preventDefault(); sonra if (!name) return;
3. localStorage.setItem("graduate", name);

<details><summary>Çözüm</summary>

```js
const form = document.querySelector("#f");
const card = document.querySelector("#card");

function showCard(name) {
  card.innerHTML = "";
  const title = document.createElement("h2");
  title.textContent = `Tebrikler, ${name}!`;
  const text = document.createElement("p");
  text.textContent = "30 Günde JavaScript yolculuğunu tamamladı.";
  card.append(title, text);
}

// açılışta kayıtlı ad varsa göster
const saved = localStorage.getItem("graduate");
if (saved) showCard(saved);

// form gönderilince
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.querySelector("#name").value.trim();
  if (!name) return;
  localStorage.setItem("graduate", name);
  showCard(name);
});
```

</details>

### Görev 2: Canlı arama

Şehirleri bir kez getir, sonra kutuya yazıldıkça listeyi süz:

- Açılışta `/demo-api/sehirler`'i `fetch` ile al, `cities`'e koy ve hepsini göster.
- `render(list)`: `#list`'i temizleyip her şehrin adını bir `<li>` olarak eklesin; `#count`'a `8 sonuç` yazsın.
- `#search` kutusunda `input` olayı olunca adı, yazılanı içeren şehirleri göster (büyük/küçük harf fark etmesin: `toLocaleLowerCase("tr")`).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<input id="search" placeholder="Şehir ara" aria-label="Şehir ara">
<p id="count"></p>
<ul id="list"></ul>
```

**CSS:**

```css
#search{padding:6px;font-size:16px}
```

**Başlangıç kodu:**

```js
let cities = [];
const list = document.querySelector("#list");
const search = document.querySelector("#search");

function render(items) {
  // listeyi temizle, adları ekle, sonuç sayısını yaz
}

async function init() {
  // şehirleri al, cities'e koy, hepsini göster
}

// input olayında süz

init();
```

**İpuçları:**

1. cities = await res.json(); render(cities);
2. search.addEventListener("input", () => { ... })
3. cities.filter((city) => city.ad.toLocaleLowerCase("tr").includes(text))

<details><summary>Çözüm</summary>

```js
let cities = [];
const list = document.querySelector("#list");
const search = document.querySelector("#search");

function render(items) {
  list.innerHTML = "";
  items.forEach((city) => {
    const li = document.createElement("li");
    li.textContent = city.ad;
    list.append(li);
  });
  document.querySelector("#count").textContent = `${items.length} sonuç`;
}

async function init() {
  const res = await fetch("/demo-api/sehirler");
  cities = await res.json();
  render(cities);
}

// input olayında süz
search.addEventListener("input", () => {
  const text = search.value.trim().toLocaleLowerCase("tr");
  render(cities.filter((city) => city.ad.toLocaleLowerCase("tr").includes(text)));
});

init();
```

</details>

### Görev 3: Skor tablosu sınıfı

`Scoreboard` sınıfı skorları `localStorage`'da tutuyor. Eksik iki metodu yaz:

- `save()`: `this.items`'ı JSON olarak `this.key` anahtarına yazsın.
- `add(name, score)`: `{ name, score }` eklesin, listeyi büyükten küçüğe sıralasın, yalnızca ilk 3'ü tutsun, sonra `save()` çağırsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2>En iyi pilotlar</h2>
<ol id="scores"></ol>
```

**CSS:**

```css
#scores li{padding:2px 0}
```

**Başlangıç kodu:**

```js
class Scoreboard {
  constructor(key) {
    this.key = key;
    this.items = JSON.parse(localStorage.getItem(key) || "[]");
  }

  add(name, score) {
    // ekle, sırala, ilk 3, kaydet
  }

  save() {
    // JSON olarak kaydet
  }

  render(listEl) {
    listEl.innerHTML = "";
    for (const item of this.items) {
      const li = document.createElement("li");
      li.textContent = `${item.name}: ${item.score}`;
      listEl.append(li);
    }
  }
}

const board = new Scoreboard("scores");
board.render(document.querySelector("#scores"));
```

**İpuçları:**

1. Büyükten küçüğe: this.items.sort((a, b) => b.score - a.score);
2. İlk 3: this.items = this.items.slice(0, 3);
3. localStorage.setItem(this.key, JSON.stringify(this.items));

<details><summary>Çözüm</summary>

```js
class Scoreboard {
  constructor(key) {
    this.key = key;
    this.items = JSON.parse(localStorage.getItem(key) || "[]");
  }

  add(name, score) {
    this.items.push({ name, score });
    this.items.sort((a, b) => b.score - a.score);
    this.items = this.items.slice(0, 3);
    this.save();
  }

  save() {
    localStorage.setItem(this.key, JSON.stringify(this.items));
  }

  render(listEl) {
    listEl.innerHTML = "";
    for (const item of this.items) {
      const li = document.createElement("li");
      li.textContent = `${item.name}: ${item.score}`;
      listEl.append(li);
    }
  }
}

const board = new Scoreboard("scores");
board.render(document.querySelector("#scores"));
```

</details>

## Challenge: Bütün seviyeler

Üç seviyeyi **aynı anda** iste ve bir tabloda göster:

- `Promise.all` ile `/demo-api/seviyeler/1`, `2` ve `3`'ü birlikte iste (`[1, 2, 3].map(...)`).
- `#levels tbody`'ye her seviye için bir satır ekle: seviye, yıldız, düşman (üç `<td>`).
- `#total`'a toplam yıldızı yaz: `Toplam: 25 yıldız` (`reduce` ile hesapla).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<table id="levels"><thead><tr><th>Seviye</th><th>Yıldız</th><th>Düşman</th></tr></thead><tbody></tbody></table>
<p id="total"></p>
```

**CSS:**

```css
td,th{border:1px solid #ccd;padding:4px 10px}table{border-collapse:collapse}
```

**Başlangıç kodu:**

```js
const tbody = document.querySelector("#levels tbody");

async function loadAllLevels() {
  // Promise.all ile üç seviyeyi iste, satırları ekle, toplamı yaz
}

loadAllLevels();
```

**İpuçları:**

1. const levels = await Promise.all([1, 2, 3].map(getLevel));
2. Her seviye için bir tr, içine üç td.
3. levels.reduce((sum, level) => sum + level.yildiz, 0)

<details><summary>Çözüm</summary>

```js
const tbody = document.querySelector("#levels tbody");

async function getLevel(n) {
  const res = await fetch(`/demo-api/seviyeler/${n}`);
  return res.json();
}

async function loadAllLevels() {
  const levels = await Promise.all([1, 2, 3].map(getLevel));
  for (const level of levels) {
    const row = document.createElement("tr");
    for (const value of [level.seviye, level.yildiz, level.dusman]) {
      const cell = document.createElement("td");
      cell.textContent = value;
      row.append(cell);
    }
    tbody.append(row);
  }
  const total = levels.reduce((sum, level) => sum + level.yildiz, 0);
  document.querySelector("#total").textContent = `Toplam: ${total} yıldız`;
}

loadAllLevels();
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Yayınla ve paylaş**

### Yıldız Avcısı: Yıldız Avcısı: final

Oyunun son hali! Ekranlar, oyun döngüsü (`update`) ve çizim hazır. Parçaları birbirine bağla:

- `showScreen(name)`: `screens` içindeki bütün ekranları gizlesin (`hidden = true`), yalnızca `name` olanı göstersin.
- `startGame()`: `state`'i sıfırlasın (`score` 0, `time` 0, `running` true) ve `game` ekranını göstersin.
- `endGame()`: `running` false olsun, `over` ekranı görünsün; `#final-score`'a `Skor: 30` yazsın. En iyi skoru `localStorage`'daki `best` anahtarından okusun; yeni skor daha büyükse kaydetsin. `#best`'e `En iyi: 30` yazsın.
- `#start-btn` ve `#again-btn` tıklanınca `startGame()` çağrılsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<section id="start-screen"><h1>Yıldız Avcısı</h1><p>Yıldızları topla, en iyi skoru geç!</p><button id="start-btn">Başla</button></section>
<section id="game-screen" hidden><p id="hud">Skor: 0</p><canvas id="game" width="300" height="150"></canvas></section>
<section id="over-screen" hidden><h2>Oyun bitti!</h2><p id="final-score"></p><p id="best"></p><button id="again-btn">Tekrar oyna</button></section>
```

**CSS:**

```css
#title{color:#0b1026}canvas{background:#0b1026;display:block;max-width:100%;border-radius:6px}#levels button{margin:4px}.controls button{font-size:22px;min-width:56px;min-height:48px;margin:4px}section h1,section h2{color:#0b1026}
```

**Başlangıç kodu:**

```js
const BEST_KEY = "best";
const GAME_LENGTH = 100;
const canvas = document.querySelector("#game");
const ctx = canvas.getContext("2d");
const state = { score: 0, time: 0, running: false };
const screens = {
  start: document.querySelector("#start-screen"),
  game: document.querySelector("#game-screen"),
  over: document.querySelector("#over-screen"),
};

// Hazır: her karede çağrılır, süre dolunca endGame() çağırır
function update() {
  if (!state.running) return;
  state.time += 1;
  if (state.time % 10 === 0) state.score += 10; // (basitleştirilmiş) bir yıldız toplandı
  document.querySelector("#hud").textContent = `Skor: ${state.score}`;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#f7df1e";
  ctx.fillRect(135, 110, 30, 30);
  if (state.time >= GAME_LENGTH) endGame();
}

function showScreen(name) {
  // bütün ekranları gizle, yalnızca name olanı göster
}

function startGame() {
  // state'i sıfırla ve oyun ekranını göster
}

function endGame() {
  // bitiş ekranı, skor, en iyi skor (localStorage)
}

// Başla ve Tekrar oyna düğmeleri

function loop() {
  update();
  requestAnimationFrame(loop);
}
loop();
```

**İpuçları:**

1. showScreen: for (const id in screens) { screens[id].hidden = id !== name; }
2. En iyi: Math.max(Number(localStorage.getItem(BEST_KEY)) || 0, state.score)
3. document.querySelector("#start-btn").addEventListener("click", startGame);

<details><summary>Çözüm</summary>

```js
const BEST_KEY = "best";
const GAME_LENGTH = 100;
const canvas = document.querySelector("#game");
const ctx = canvas.getContext("2d");
const state = { score: 0, time: 0, running: false };
const screens = {
  start: document.querySelector("#start-screen"),
  game: document.querySelector("#game-screen"),
  over: document.querySelector("#over-screen"),
};

// Hazır: her karede çağrılır, süre dolunca endGame() çağırır
function update() {
  if (!state.running) return;
  state.time += 1;
  if (state.time % 10 === 0) state.score += 10; // (basitleştirilmiş) bir yıldız toplandı
  document.querySelector("#hud").textContent = `Skor: ${state.score}`;
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#f7df1e";
  ctx.fillRect(135, 110, 30, 30);
  if (state.time >= GAME_LENGTH) endGame();
}

function showScreen(name) {
  for (const id in screens) {
    screens[id].hidden = id !== name;
  }
}

function startGame() {
  state.score = 0;
  state.time = 0;
  state.running = true;
  showScreen("game");
}

function endGame() {
  state.running = false;
  showScreen("over");
  document.querySelector("#final-score").textContent = `Skor: ${state.score}`;
  const best = Math.max(Number(localStorage.getItem(BEST_KEY)) || 0, state.score);
  localStorage.setItem(BEST_KEY, String(best));
  document.querySelector("#best").textContent = `En iyi: ${best}`;
}

// Başla ve Tekrar oyna düğmeleri
document.querySelector("#start-btn").addEventListener("click", startGame);
document.querySelector("#again-btn").addEventListener("click", startGame);

function loop() {
  update();
  requestAnimationFrame(loop);
}
loop();
```

</details>

### Kişisel Web Sitem: Kişisel Web Sitem: final

Sitenin bütün parçaları hazır: `ProjectCard` sınıfı, `applyTheme` ve `contactMessage`. `init()` fonksiyonunda hepsini bağla:

1. Kayıtlı temayı uygula: `localStorage`'daki `theme` (yoksa `"light"`).
2. `#theme-btn` tıklanınca tema `dark` ile `light` arasında değişsin, uygulansın ve kaydedilsin.
3. `myProjects`'teki her kartın `render()` sonucunu `#projects`'e ekle.
4. `#contact` gönderilince sayfa yenilenmesin; ad ve mesajı `trim` ile alıp `contactMessage` sonucunu `#form-status`'a yaz. Mesaj başarılıysa formu temizle (`form.reset()`).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<header><h1 id="site-title">Kod Günlüğüm</h1><button id="theme-btn">Tema</button></header>
<main><h2>Projelerim</h2><div id="projects"></div>
<h2>İletişim</h2><form id="contact"><input id="c-name" placeholder="Adın" aria-label="Adın"><textarea id="c-msg" placeholder="Mesajın" aria-label="Mesajın"></textarea><button>Gönder</button></form>
<p id="form-status" aria-live="polite"></p></main>
```

**CSS:**

```css
header{display:flex;align-items:center;gap:12px;flex-wrap:wrap}header h1{margin:0;font-size:22px}nav a{margin-right:10px}.card{border:1px solid #ccd;border-radius:8px;padding:8px 12px;margin:8px 0}.card h3{margin:0 0 4px}.tech{color:#556;font-size:14px}body.dark{background:#0b1026;color:#eef}body.dark a{color:#9cf}form{display:grid;gap:6px;max-width:320px}
```

**Başlangıç kodu:**

```js
const THEME_KEY = "theme";

class ProjectCard {
  constructor(title, tech, url) {
    this.title = title;
    this.tech = tech;
    this.url = url;
  }

  render() {
    const card = document.createElement("article");
    card.className = "card";
    const h3 = document.createElement("h3");
    h3.textContent = this.title;
    const tech = document.createElement("p");
    tech.className = "tech";
    tech.textContent = this.tech.join(", ");
    const link = document.createElement("a");
    link.href = this.url;
    link.textContent = "İncele";
    card.append(h3, tech, link);
    return card;
  }
}

const myProjects = [
  new ProjectCard("Yıldız Avcısı", ["Canvas", "JavaScript"], "#oyun"),
  new ProjectCard("Hava Durumu", ["fetch", "JSON"], "#hava"),
  new ProjectCard("Not Defteri", ["localStorage"], "#notlar"),
];

function applyTheme(theme) {
  document.body.classList.toggle("dark", theme === "dark");
  document.querySelector("#theme-btn").textContent = theme === "dark" ? "Açık tema" : "Koyu tema";
}

function contactMessage(name, message) {
  if (!name || !message) return "Lütfen adını ve mesajını yaz.";
  return `Teşekkürler, ${name}! Mesajın alındı.`;
}

function init() {
  // 1) kayıtlı tema  2) tema düğmesi  3) projeler  4) iletişim formu
}

init();
```

**İpuçları:**

1. let theme = localStorage.getItem(THEME_KEY) || "light";
2. Düğmede: theme = theme === "dark" ? "light" : "dark"; sonra applyTheme ve setItem
3. Formda: e.preventDefault(); ... if (name && message) form.reset();

<details><summary>Çözüm</summary>

```js
const THEME_KEY = "theme";

class ProjectCard {
  constructor(title, tech, url) {
    this.title = title;
    this.tech = tech;
    this.url = url;
  }

  render() {
    const card = document.createElement("article");
    card.className = "card";
    const h3 = document.createElement("h3");
    h3.textContent = this.title;
    const tech = document.createElement("p");
    tech.className = "tech";
    tech.textContent = this.tech.join(", ");
    const link = document.createElement("a");
    link.href = this.url;
    link.textContent = "İncele";
    card.append(h3, tech, link);
    return card;
  }
}

const myProjects = [
  new ProjectCard("Yıldız Avcısı", ["Canvas", "JavaScript"], "#oyun"),
  new ProjectCard("Hava Durumu", ["fetch", "JSON"], "#hava"),
  new ProjectCard("Not Defteri", ["localStorage"], "#notlar"),
];

function applyTheme(theme) {
  document.body.classList.toggle("dark", theme === "dark");
  document.querySelector("#theme-btn").textContent = theme === "dark" ? "Açık tema" : "Koyu tema";
}

function contactMessage(name, message) {
  if (!name || !message) return "Lütfen adını ve mesajını yaz.";
  return `Teşekkürler, ${name}! Mesajın alındı.`;
}

function init() {
  // 1) kayıtlı tema
  let theme = localStorage.getItem(THEME_KEY) || "light";
  applyTheme(theme);

  // 2) tema düğmesi
  document.querySelector("#theme-btn").addEventListener("click", () => {
    theme = theme === "dark" ? "light" : "dark";
    applyTheme(theme);
    localStorage.setItem(THEME_KEY, theme);
  });

  // 3) projeler
  const box = document.querySelector("#projects");
  myProjects.forEach((project) => box.append(project.render()));

  // 4) iletişim formu
  const form = document.querySelector("#contact");
  form.addEventListener("submit", (e) => {
    e.preventDefault();
    const name = document.querySelector("#c-name").value.trim();
    const message = document.querySelector("#c-msg").value.trim();
    document.querySelector("#form-status").textContent = contactMessage(name, message);
    if (name && message) form.reset();
  });
}

init();
```

</details>

### Çalışma Asistanım: Çalışma Asistanım: final

Asistanın son hali! `Task` sınıfı, `load()` ve `render()` hazır. Uygulamayı çalışır hale getir:

- `save()`: `tasks`'ı JSON olarak `localStorage`'daki `tasks` anahtarına yazsın.
- `addTask(title)`: başlığı `trim` ile temizlesin; boşsa hiçbir şey yapmasın. Değilse yeni bir `Task` eklesin, kaydetsin, çizsin.
- `toggleTask(index)`: görevi değiştirsin (`toggle()`), kaydetsin, çizsin.
- `#add-form` gönderilince (sayfa yenilenmeden) `addTask` çağrılsın ve kutu temizlensin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1>Çalışma Asistanım</h1>
<form id="add-form"><input id="new-task" placeholder="Yeni görev" aria-label="Yeni görev"><button>Ekle</button></form>
<ul id="tasks"></ul>
<p id="stats"></p>
```

**CSS:**

```css
li{padding:6px;cursor:pointer}li.done{text-decoration:line-through;color:#889}li.selected{outline:2px solid #3b6ef5;border-radius:4px}.big{font-size:20px;min-width:64px;min-height:48px;margin:4px}#stats,#count{font-weight:bold}form{display:flex;gap:6px}
```

**Başlangıç kodu:**

```js
const STORAGE_KEY = "tasks";

class Task {
  constructor(title, done = false) {
    this.title = title;
    this.done = done;
  }
  toggle() {
    this.done = !this.done;
  }
}

const list = document.querySelector("#tasks");
const input = document.querySelector("#new-task");

function load() {
  const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
  return saved.map((t) => new Task(t.title, t.done));
}

let tasks = load();

function render() {
  list.innerHTML = "";
  tasks.forEach((task, i) => {
    const li = document.createElement("li");
    li.textContent = task.title;
    li.classList.toggle("done", task.done);
    li.addEventListener("click", () => toggleTask(i));
    list.append(li);
  });
  const done = tasks.filter((t) => t.done).length;
  document.querySelector("#stats").textContent = `${done}/${tasks.length} tamamlandı`;
}

function save() {
  // JSON olarak kaydet
}

function addTask(title) {
  // temizle, boşsa çık, ekle, kaydet, çiz
}

function toggleTask(index) {
  // değiştir, kaydet, çiz
}

// form gönderilince

render();
```

**İpuçları:**

1. localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
2. addTask: const clean = title.trim(); if (!clean) return; tasks.push(new Task(clean));
3. Formda: e.preventDefault(); addTask(input.value); input.value = "";

<details><summary>Çözüm</summary>

```js
const STORAGE_KEY = "tasks";

class Task {
  constructor(title, done = false) {
    this.title = title;
    this.done = done;
  }
  toggle() {
    this.done = !this.done;
  }
}

const list = document.querySelector("#tasks");
const input = document.querySelector("#new-task");

function load() {
  const saved = JSON.parse(localStorage.getItem(STORAGE_KEY) || "[]");
  return saved.map((t) => new Task(t.title, t.done));
}

let tasks = load();

function render() {
  list.innerHTML = "";
  tasks.forEach((task, i) => {
    const li = document.createElement("li");
    li.textContent = task.title;
    li.classList.toggle("done", task.done);
    li.addEventListener("click", () => toggleTask(i));
    list.append(li);
  });
  const done = tasks.filter((t) => t.done).length;
  document.querySelector("#stats").textContent = `${done}/${tasks.length} tamamlandı`;
}

function save() {
  localStorage.setItem(STORAGE_KEY, JSON.stringify(tasks));
}

function addTask(title) {
  const clean = title.trim();
  if (!clean) return;
  tasks.push(new Task(clean));
  save();
  render();
}

function toggleTask(index) {
  tasks[index].toggle();
  save();
  render();
}

// form gönderilince
document.querySelector("#add-form").addEventListener("submit", (e) => {
  e.preventDefault();
  addTask(input.value);
  input.value = "";
});

render();
```

</details>

### Bilgi Yarışması: Bilgi Yarışması: final

Yarışmanın son hali! `Quiz` sınıfı ve `showQuestion()` hazır. Oyunun akışını yaz:

- `start()`: `/demo-api/sorular`'dan soruları alsın, `quiz = new Quiz(sorular)` yapsın; `#play`'i göstersin, `#result`'ı gizlesin ve `showQuestion()` çağırsın.
- `choose(i)`: `quiz.answer(i)`, sonra `quiz.next()`. Sorular bittiyse `showResult()`, bitmediyse `showQuestion()`.
- `showResult()`: `#play`'i gizleyip `#result`'ı göstersin; `#result-text`'e `Puanın: 40 / 50` yazsın (en yüksek puan soru sayısı × 10). En iyi puanı `localStorage`'daki `quizBest` anahtarında tutsun ve `#best`'e `En iyi: 40` yazsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1>Bilgi Yarışması</h1>
<section id="play"><p id="question">Sorular yükleniyor...</p><div id="options"></div><p id="score">Puan: 0</p></section>
<section id="result" hidden><h2 id="result-text"></h2><p id="best"></p><button id="again">Tekrar oyna</button></section>
```

**CSS:**

```css
#options button{display:block;width:100%;max-width:320px;margin:6px 0;padding:10px;font-size:18px}#feedback{font-weight:bold}
```

**Başlangıç kodu:**

```js
const BEST_KEY = "quizBest";

class Quiz {
  constructor(questions) {
    this.questions = questions;
    this.current = 0;
    this.score = 0;
  }

  get question() {
    return this.questions[this.current];
  }

  answer(index) {
    const correct = index === this.question.dogru;
    if (correct) this.score += 10;
    return correct;
  }

  next() {
    this.current += 1;
  }

  get isOver() {
    return this.current >= this.questions.length;
  }
}

let quiz = null;
const options = document.querySelector("#options");
const play = document.querySelector("#play");
const result = document.querySelector("#result");

function showQuestion() {
  const q = quiz.question;
  document.querySelector("#question").textContent = `Soru ${quiz.current + 1}/${quiz.questions.length}: ${q.soru}`;
  options.innerHTML = "";
  q.secenekler.forEach((text, i) => {
    const btn = document.createElement("button");
    btn.textContent = text;
    btn.addEventListener("click", () => choose(i));
    options.append(btn);
  });
  document.querySelector("#score").textContent = `Puan: ${quiz.score}`;
}

async function start() {
  // soruları al, quiz oluştur, bölümleri ayarla, ilk soruyu göster
}

function choose(i) {
  // cevapla, ilerle; bittiyse sonuç, değilse sıradaki soru
}

function showResult() {
  // sonuç bölümü, puan, en iyi puan (localStorage)
}

document.querySelector("#again").addEventListener("click", start);

start();
```

**İpuçları:**

1. quiz = new Quiz(await res.json());
2. choose: quiz.answer(i); quiz.next(); if (quiz.isOver) { showResult(); return; } showQuestion();
3. En iyi: Math.max(Number(localStorage.getItem(BEST_KEY)) || 0, quiz.score)

<details><summary>Çözüm</summary>

```js
const BEST_KEY = "quizBest";

class Quiz {
  constructor(questions) {
    this.questions = questions;
    this.current = 0;
    this.score = 0;
  }

  get question() {
    return this.questions[this.current];
  }

  answer(index) {
    const correct = index === this.question.dogru;
    if (correct) this.score += 10;
    return correct;
  }

  next() {
    this.current += 1;
  }

  get isOver() {
    return this.current >= this.questions.length;
  }
}

let quiz = null;
const options = document.querySelector("#options");
const play = document.querySelector("#play");
const result = document.querySelector("#result");

function showQuestion() {
  const q = quiz.question;
  document.querySelector("#question").textContent = `Soru ${quiz.current + 1}/${quiz.questions.length}: ${q.soru}`;
  options.innerHTML = "";
  q.secenekler.forEach((text, i) => {
    const btn = document.createElement("button");
    btn.textContent = text;
    btn.addEventListener("click", () => choose(i));
    options.append(btn);
  });
  document.querySelector("#score").textContent = `Puan: ${quiz.score}`;
}

async function start() {
  const res = await fetch("/demo-api/sorular");
  if (!res.ok) {
    document.querySelector("#question").textContent = "Sorular yüklenemedi.";
    return;
  }
  quiz = new Quiz(await res.json());
  play.hidden = false;
  result.hidden = true;
  showQuestion();
}

function choose(i) {
  quiz.answer(i);
  quiz.next();
  if (quiz.isOver) {
    showResult();
    return;
  }
  showQuestion();
}

function showResult() {
  play.hidden = true;
  result.hidden = false;
  const max = quiz.questions.length * 10;
  document.querySelector("#result-text").textContent = `Puanın: ${quiz.score} / ${max}`;
  const best = Math.max(Number(localStorage.getItem(BEST_KEY)) || 0, quiz.score);
  localStorage.setItem(BEST_KEY, String(best));
  document.querySelector("#best").textContent = `En iyi: ${best}`;
}

document.querySelector("#again").addEventListener("click", start);

start();
```

</details>
