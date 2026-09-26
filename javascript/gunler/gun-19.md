# Gün 19: CSS'i kodla kontrol etmek

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Olay Kuşağı  ·  **Maskot:** Kodi

**Bugünün hedefi:** style, classList, CSS değişkenleri ve data-* özellikleriyle görünüşü JavaScript'ten değiştirmek

> Gemin artık hareket ediyor ve zamanı ölçüyor; şimdi sıra görünüşte! Bugün JavaScript ile **CSS'i kontrol edip** temalar, efektler ve renk seçiciler yapacaksın.

![Olay Kuşağı](../../gorseller/javascript/bolgeler/kusak.webp)

## Konu anlatımı

### element.style: tek tek özellikler

Her elemanın bir `style` nesnesi var. CSS'teki tireli adlar burada **camelCase** yazılır (`background-color` → `backgroundColor`) ve değerler metindir; birimi unutma:

```js
const box = document.querySelector("#box");
box.style.backgroundColor = "#f7df1e";
box.style.width = "150px"; // 150 değil, "150px"
```

`box.style` yalnızca elemanın üstüne yazılanı gösterir. CSS kurallarından gelen son hâli görmek için `getComputedStyle(box).width` kullanılır.

### classList ile durumlar

Çok sayıda stili tek tek yazmak yerine görünüşü CSS'te bir **sınıfa** yaz, JavaScript'te yalnızca sınıfı ekle ya da çıkar:

```
.shield.active { border-color: #26c6da; background: #e0f7fa; }
```

```js
shield.classList.add("active");      // ekle
shield.classList.remove("active");   // çıkar
shield.classList.toggle("active");   // varsa çıkar, yoksa ekle
shield.classList.contains("active"); // true / false
btn.classList.toggle("active", color === "#f7df1e"); // koşul doğruysa ekle, değilse çıkar
```

### CSS değişkenleri

CSS'te `--` ile başlayan adlar **değişkendir**. Bir kez tanımlanır, `var(...)` ile her yerde kullanılır:

```
:root { --accent: #f7df1e; }
h2 { border-bottom: 4px solid var(--accent); }
button.active { outline: 3px solid var(--accent); }
```

JavaScript'le tek satırda değiştirirsin; değişkeni kullanan **her şey** birden güncellenir:

```js
const root = document.documentElement; // :root yani <html>
root.style.setProperty("--accent", "#b388ff");
const now = getComputedStyle(root).getPropertyValue("--accent").trim();
```

### data-* özellikleri

HTML'de `data-` ile başlayan özellikler, elemana kendi bilgini eklemenin yoludur. JavaScript'te `dataset` ile okunur ve yazılır:

```js
// <button data-color="#e53935">Kızıl</button>
btn.dataset.color;              // "#e53935"
document.body.dataset.mode = "gece"; // <body data-mode="gece">
```

CSS de bu özelliklere göre seçim yapabilir: `body[data-mode="gece"] #panel { ... }`. Böylece bir değer değişince bütün görünüş değişir.

## Örnekler

### Gece modu

Sayfa:

```html
<div id="card"><h3>Kaptan Günlüğü</h3><p>Bugün Olay Kuşağı gezildi.</p></div>
<button id="toggle">Gece modu</button>
```

```js
const btn = document.querySelector("#toggle");
btn.addEventListener("click", () => {
  document.body.classList.toggle("night");
  const night = document.body.classList.contains("night");
  btn.textContent = night ? "Gündüz modu" : "Gece modu";
});
```

*Bütün renkler CSS'te; JavaScript yalnızca sınıfı değiştiriyor.*

### Boyut kaydırıcısı

Sayfa:

```html
<input type="range" id="size" min="20" max="120" value="60"> <span id="label">60px</span>
<div id="star"></div>
```

```js
const slider = document.querySelector("#size");
slider.addEventListener("input", () => {
  const value = slider.value + "px";
  document.documentElement.style.setProperty("--size", value);
  document.querySelector("#label").textContent = value;
});
```

*Kaydırıcıyı oynat: yıldızın boyutu CSS değişkeniyle değişiyor.*

## Görevler

### Görev 1: Kutuyu boya

`#paint` düğmesine tıklanınca `#box` kutusunun `style`'ını değiştir:

- arka plan rengi `#f7df1e` olsun (`backgroundColor`),
- genişliği `150px` olsun.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<div id="box">Kargo</div>
<button id="paint">Boya</button>
```

**CSS:**

```css
#box{width:80px;height:50px;background:#ccc;display:grid;place-items:center;margin-bottom:8px}
```

**Başlangıç kodu:**

```js
const box = document.querySelector("#box");

// #paint tıklanınca box.style ile boya
```

**İpuçları:**

1. box.style.backgroundColor = "#f7df1e";
2. Birimi unutma: box.style.width = "150px";

<details><summary>Çözüm</summary>

```js
const box = document.querySelector("#box");

// #paint tıklanınca box.style ile boya
document.querySelector("#paint").addEventListener("click", () => {
  box.style.backgroundColor = "#f7df1e";
  box.style.width = "150px";
});
```

</details>

### Görev 2: Kalkan

`#shield-btn` her tıklandığında `#shield`'daki `active` sınıfını aç/kapat (`classList.toggle`).

`#status` kalkan açıkken `Kalkan: AÇIK`, kapalıyken `Kalkan: KAPALI` yazsın (durumu `classList.contains` ile öğren).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<div id="shield">Kalkan</div>
<button id="shield-btn">Kalkanı aç/kapat</button>
<p id="status">Kalkan: KAPALI</p>
```

**CSS:**

```css
#shield{padding:10px;border:3px solid #999;border-radius:8px;margin-bottom:8px}#shield.active{border-color:#26c6da;background:#e0f7fa}
```

**Başlangıç kodu:**

```js
const shield = document.querySelector("#shield");

// tıklanınca active sınıfını aç/kapat ve #status'u güncelle
```

**İpuçları:**

1. shield.classList.toggle("active");
2. const on = shield.classList.contains("active");

<details><summary>Çözüm</summary>

```js
const shield = document.querySelector("#shield");

// tıklanınca active sınıfını aç/kapat ve #status'u güncelle
document.querySelector("#shield-btn").addEventListener("click", () => {
  shield.classList.toggle("active");
  const on = shield.classList.contains("active");
  document.querySelector("#status").textContent = on ? "Kalkan: AÇIK" : "Kalkan: KAPALI";
});
```

</details>

### Görev 3: Gezegen rengi

Gezegenin rengi CSS değişkeni `--planet`'ten geliyor. `data-color` özelliği olan her düğmeye tıklanınca:

- `document.documentElement.style.setProperty("--planet", ...)` ile rengi düğmenin `dataset.color` değeri yap,
- `#current`'e değişkenin yeni değerini `Renk: #1e88e5` biçiminde yaz (`getComputedStyle(...).getPropertyValue("--planet")` ile oku, `trim()` et).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<div id="planet"></div>
<button data-color="#e53935">Kızıl</button> <button data-color="#1e88e5">Mavi</button> <button data-color="#43a047">Yeşil</button>
<p id="current">Renk: #f7df1e</p>
```

**CSS:**

```css
:root{--planet:#f7df1e}#planet{width:60px;height:60px;border-radius:50%;background:var(--planet);margin-bottom:8px}
```

**Başlangıç kodu:**

```js
const root = document.documentElement;
const colorButtons = document.querySelectorAll("[data-color]");

// her düğmeye click dinleyicisi ekle
```

**İpuçları:**

1. root.style.setProperty("--planet", btn.dataset.color);
2. getComputedStyle(root).getPropertyValue("--planet").trim()

<details><summary>Çözüm</summary>

```js
const root = document.documentElement;
const colorButtons = document.querySelectorAll("[data-color]");

// her düğmeye click dinleyicisi ekle
colorButtons.forEach((btn) => {
  btn.addEventListener("click", () => {
    root.style.setProperty("--planet", btn.dataset.color);
    const value = getComputedStyle(root).getPropertyValue("--planet").trim();
    document.querySelector("#current").textContent = `Renk: ${value}`;
  });
});
```

</details>

## Challenge: Panel modu

`setMode(mode)` fonksiyonunu yaz:

- `document.body.dataset.mode`'u `mode` yapsın (CSS panelin rengini buna göre değiştiriyor),
- `data-mode`'u `mode`'a eşit olan düğmeye `selected` sınıfını eklesin, diğerlerinden kaldırsın,
- `#mode-label`'a `Mod: gece` biçiminde yazsın.

Her `[data-mode]` düğmesi tıklanınca kendi moduyla `setMode` çağırsın. Sayfa açılınca `setMode("gunduz")` çalışsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<div id="panel">Kontrol paneli</div>
<button data-mode="gunduz">Gündüz</button> <button data-mode="gece">Gece</button> <button data-mode="alarm">Alarm</button>
<p id="mode-label"></p>
```

**CSS:**

```css
#panel{padding:12px;border-radius:8px;background:#fff8d6;color:#1b1f33;margin-bottom:8px}body[data-mode="gece"] #panel{background:#0b1026;color:#eef1ff}body[data-mode="alarm"] #panel{background:#c62828;color:#fff}button.selected{outline:3px solid #f7df1e}
```

**Başlangıç kodu:**

```js
const modeButtons = document.querySelectorAll("[data-mode]");

function setMode(mode) {
  // body.dataset.mode, selected sınıfı, #mode-label
}

// düğmeleri dinle ve başlangıç modunu ayarla
```

**İpuçları:**

1. document.body.dataset.mode = mode;
2. btn.classList.toggle("selected", btn.dataset.mode === mode);

<details><summary>Çözüm</summary>

```js
const modeButtons = document.querySelectorAll("[data-mode]");

function setMode(mode) {
  // body.dataset.mode, selected sınıfı, #mode-label
  document.body.dataset.mode = mode;
  modeButtons.forEach((btn) => {
    btn.classList.toggle("selected", btn.dataset.mode === mode);
  });
  document.querySelector("#mode-label").textContent = `Mod: ${mode}`;
}

// düğmeleri dinle ve başlangıç modunu ayarla
modeButtons.forEach((btn) => {
  btn.addEventListener("click", () => setMode(btn.dataset.mode));
});
setMode("gunduz");
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Tema ve efektler**

### Yıldız Avcısı: Tema ve efektler

Oyuna renk ve efekt ekleyelim. Geminin rengi CSS değişkeni `--ship-color`'dan geliyor.

- `setShipColor(color)`: `--ship-color`'ı `color` yapsın (`document.documentElement.style.setProperty`).
- `#colors` içindeki her `[data-color]` düğmesi tıklanınca kendi `dataset.color` değeriyle `setShipColor` çağırsın.
- `flashHit()`: gemi vurulunca oyun alanı (`#field`) kızarsın: `hit` sınıfını eklesin ve **150 ms sonra** kaldırsın (`setTimeout`).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 id="title">Yıldız Avcısı</h2>
<form id="pilot-form"><input id="pilot-name" placeholder="Pilot adı" autocomplete="off"> <button>Başla</button></form>
<p id="info">Pilot adını yaz ve başla.</p>
<p id="hud">Skor: <span id="score">0</span> · Süre: <span id="time">10</span> · En yüksek: <span id="best">0</span></p>
<div id="field"><div id="ship"></div></div>
<div id="colors"><button data-color="#f7df1e">Sarı</button> <button data-color="#4dd0e1">Turkuaz</button> <button data-color="#ff6b6b">Kırmızı</button></div>
```

**CSS:**

```css
:root{--ship-color:#f7df1e}#title{margin:0 0 6px;color:#0b1026}#info.error{color:#c0392b;font-weight:600}#hud{margin:4px 0}#field{position:relative;width:300px;height:70px;background:#0b1026;border-radius:8px;overflow:hidden}#field.hit{background:#8e1b2b}#ship{position:absolute;left:0;bottom:10px;width:30px;height:30px;border-radius:50% 50% 6px 6px;background:var(--ship-color)}#colors{margin-top:8px}
```

**Başlangıç kodu:**

```js
const field = document.querySelector("#field");

function setShipColor(color) {
  // --ship-color değişkenini değiştir
}

function flashHit() {
  // hit sınıfını ekle, 150 ms sonra kaldır
}

// renk düğmelerini dinle
```

**İpuçları:**

1. document.documentElement.style.setProperty("--ship-color", color);
2. field.classList.add("hit"); setTimeout(() => field.classList.remove("hit"), 150);

<details><summary>Çözüm</summary>

```js
const field = document.querySelector("#field");

function setShipColor(color) {
  // --ship-color değişkenini değiştir
  document.documentElement.style.setProperty("--ship-color", color);
}

function flashHit() {
  // hit sınıfını ekle, 150 ms sonra kaldır
  field.classList.add("hit");
  setTimeout(() => {
    field.classList.remove("hit");
  }, 150);
}

// renk düğmelerini dinle
document.querySelectorAll("#colors [data-color]").forEach((btn) => {
  btn.addEventListener("click", () => setShipColor(btn.dataset.color));
});
```

</details>

### Kişisel Web Sitem: Tema rengi

Ziyaretçi sitenin vurgu rengini seçebilsin. Başlığın alt çizgisi CSS değişkeni `--accent`'ten geliyor.

`setAccent(color)` fonksiyonunu yaz:

- `--accent`'i `color` yapsın,
- `#accents` içinde `data-accent`'i `color`'a eşit olan düğmeye `active` sınıfını eklesin, diğerlerinden kaldırsın.

Her `[data-accent]` düğmesi tıklanınca kendi rengiyle `setAccent` çağırsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<header id="top"><h2 id="site-title">Deniz Yıldız</h2> <input id="search" placeholder="Sitede ara ( / )" autocomplete="off"> <span id="clock">--:--:--</span></header>
<nav id="accents"><button data-accent="#f7df1e">Sarı</button> <button data-accent="#26c6da">Turkuaz</button> <button data-accent="#b388ff">Mor</button> <button id="theme-btn">Tema değiştir</button></nav>
<form id="contact"><input id="c-name" placeholder="Adın" autocomplete="off"> <input id="c-email" placeholder="E-posta adresin" autocomplete="off"> <button>Gönder</button></form>
<p id="form-msg"></p>
```

**CSS:**

```css
:root{--accent:#f7df1e}body.dark{background:#0b1026;color:#eef1ff}#site-title{display:inline-block;margin:0 8px 6px 0;border-bottom:4px solid var(--accent)}#clock{font-family:monospace;margin-left:8px}nav{margin:6px 0}nav button.active{outline:3px solid var(--accent)}#contact input{margin:4px 4px 4px 0}#form-msg.error{color:#c0392b;font-weight:600}
```

**Başlangıç kodu:**

```js
const accentButtons = document.querySelectorAll("#accents [data-accent]");

function setAccent(color) {
  // --accent ve active sınıfı
}

// düğmeleri dinle
```

**İpuçları:**

1. document.documentElement.style.setProperty("--accent", color);
2. btn.classList.toggle("active", btn.dataset.accent === color);

<details><summary>Çözüm</summary>

```js
const accentButtons = document.querySelectorAll("#accents [data-accent]");

function setAccent(color) {
  // --accent ve active sınıfı
  document.documentElement.style.setProperty("--accent", color);
  accentButtons.forEach((btn) => {
    btn.classList.toggle("active", btn.dataset.accent === color);
  });
}

// düğmeleri dinle
accentButtons.forEach((btn) => {
  btn.addEventListener("click", () => setAccent(btn.dataset.accent));
});
```

</details>

### Çalışma Asistanım: Tamamlanan görevler

Görevlere tıklayınca tamamlandı olarak işaretlensin ve ilerleme çubuğu dolsun.

- `addTask` içinde her `li`'ye tıklanınca `done` sınıfı aç/kapansın ve `updateProgress()` çağrılsın.
- `updateProgress()`: biten (`li.done`) ve toplam görev sayısını bulsun, `#progress-text`'e `1 / 3` yazsın ve yüzdeyi (`Math.round`) `#progress` elemanında `--progress` değişkenine `33%` biçiminde koysun (`style.setProperty`). Görev yoksa yüzde 0 olsun.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 id="app-title">Çalışma Asistanım</h2>
<form id="task-form"><input id="task-input" placeholder="Yeni görev" autocomplete="off"> <button>Ekle</button></form>
<p id="task-msg"></p>
<ul id="task-list"></ul>
<div id="progress"><div id="progress-bar"></div></div> <span id="progress-text">0 / 0</span>
<p id="focus"><strong id="focus-time">25:00</strong> <button id="focus-start">Başlat</button> <button id="focus-pause">Duraklat</button> <span id="focus-msg"></span></p>
```

**CSS:**

```css
#app-title{margin:0 0 6px}#task-msg.error{color:#c0392b;font-weight:600}#task-list li{cursor:pointer;padding:2px 0}#task-list li.done{text-decoration:line-through;opacity:.55}#progress{display:inline-block;vertical-align:middle;width:200px;height:10px;background:#e3e6f0;border-radius:5px;overflow:hidden}#progress-bar{width:var(--progress,0%);height:100%;background:#43a047}#focus-time{font-family:monospace;font-size:20px}
```

**Başlangıç kodu:**

```js
const list = document.querySelector("#task-list");

function updateProgress() {
  // biten / toplam → #progress-text ve --progress
}

function addTask(text) {
  const li = document.createElement("li");
  li.textContent = text;
  // tıklanınca done sınıfını aç/kapat ve ilerlemeyi güncelle
  list.append(li);
  updateProgress();
}

addTask("Matematik ödevi");
addTask("Fizik tekrarı");
addTask("İngilizce kelimeler");
```

**İpuçları:**

1. list.querySelectorAll("li.done").length biten görev sayısıdır.
2. document.querySelector("#progress").style.setProperty("--progress", percent + "%");

<details><summary>Çözüm</summary>

```js
const list = document.querySelector("#task-list");

function updateProgress() {
  // biten / toplam → #progress-text ve --progress
  const total = list.querySelectorAll("li").length;
  const done = list.querySelectorAll("li.done").length;
  const percent = total === 0 ? 0 : Math.round((done / total) * 100);
  document.querySelector("#progress").style.setProperty("--progress", percent + "%");
  document.querySelector("#progress-text").textContent = `${done} / ${total}`;
}

function addTask(text) {
  const li = document.createElement("li");
  li.textContent = text;
  // tıklanınca done sınıfını aç/kapat ve ilerlemeyi güncelle
  li.addEventListener("click", () => {
    li.classList.toggle("done");
    updateProgress();
  });
  list.append(li);
  updateProgress();
}

addTask("Matematik ödevi");
addTask("Fizik tekrarı");
addTask("İngilizce kelimeler");
```

</details>

### Bilgi Yarışması: Doğru ve yanlış renkleri

Cevap verilince seçenekler renklensin (CSS hazır: `.correct` yeşil, `.wrong` kırmızı).

- `answer(index)` içinde doğru seçeneğin düğmesine (`buttons[question.correct]`) **her zaman** `correct` sınıfını ekle. Cevap yanlışsa seçilen düğmeye `wrong` sınıfını da ekle.
- `resetOptions()`: bütün düğmelerden `correct` ve `wrong` sınıflarını kaldırsın, `answered`'ı `false` yapsın ve `#feedback`'i boşaltsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 id="quiz-title">Bilgi Yarışması</h2>
<form id="player-form"><input id="player-name" placeholder="Yarışmacı adı" autocomplete="off"> <button>Katıl</button></form>
<p id="welcome"></p>
<p id="question">Ay, hangi gezegenin uydusudur?</p>
<div id="options"><button class="option">1) Mars</button> <button class="option">2) Dünya</button> <button class="option">3) Jüpiter</button></div>
<p id="feedback"></p>
<p id="status">Puan: <span id="score">0</span> · Süre: <span id="time">10</span> · Rekor: <span id="best">0</span></p>
```

**CSS:**

```css
#quiz-title{margin:0 0 6px}#welcome.error{color:#c0392b;font-weight:600}.option{margin:2px;padding:6px 10px;border:1px solid #9aa3c0;border-radius:6px;background:#f4f6fb;color:#1b1f33}.option.correct{background:#2e7d32;color:#fff}.option.wrong{background:#c62828;color:#fff}
```

**Başlangıç kodu:**

```js
const question = { text: "Ay, hangi gezegenin uydusudur?", options: ["Mars", "Dünya", "Jüpiter"], correct: 1 };
const buttons = document.querySelectorAll(".option");
const feedback = document.querySelector("#feedback");
let score = 0;
let answered = false;

function answer(index) {
  if (answered) return;
  answered = true;
  // doğru düğmeye correct, yanlış seçilene wrong
  if (index === question.correct) {
    score += 10;
    document.querySelector("#score").textContent = score;
    feedback.textContent = "Doğru!";
  } else {
    feedback.textContent = `Yanlış! Doğru cevap: ${question.options[question.correct]}`;
  }
}

function resetOptions() {
  // sınıfları kaldır, answered = false, #feedback boş
}

buttons.forEach((btn, i) => btn.addEventListener("click", () => answer(i)));
```

**İpuçları:**

1. buttons[question.correct].classList.add("correct");
2. classList.remove("correct", "wrong") iki sınıfı birden kaldırır.

<details><summary>Çözüm</summary>

```js
const question = { text: "Ay, hangi gezegenin uydusudur?", options: ["Mars", "Dünya", "Jüpiter"], correct: 1 };
const buttons = document.querySelectorAll(".option");
const feedback = document.querySelector("#feedback");
let score = 0;
let answered = false;

function answer(index) {
  if (answered) return;
  answered = true;
  // doğru düğmeye correct, yanlış seçilene wrong
  buttons[question.correct].classList.add("correct");
  if (index === question.correct) {
    score += 10;
    document.querySelector("#score").textContent = score;
    feedback.textContent = "Doğru!";
  } else {
    buttons[index].classList.add("wrong");
    feedback.textContent = `Yanlış! Doğru cevap: ${question.options[question.correct]}`;
  }
}

function resetOptions() {
  // sınıfları kaldır, answered = false, #feedback boş
  buttons.forEach((btn) => btn.classList.remove("correct", "wrong"));
  answered = false;
  feedback.textContent = "";
}

buttons.forEach((btn, i) => btn.addEventListener("click", () => answer(i)));
```

</details>
