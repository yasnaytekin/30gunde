# Gün 18: Zamanlayıcılar

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Olay Kuşağı  ·  **Maskot:** Kodi

**Bugünün hedefi:** setTimeout, setInterval ve clearInterval ile zamanlanmış işler yapmak, üst üste binen sayaçları önlemek

> Olay Kuşağı'nda zaman da bir olaydır: her saniye bir tık! Bugün **zamanlayıcılarla** geri sayımlar, saatler ve kronometreler kuracaksın.

![Olay Kuşağı](../../gorseller/javascript/bolgeler/kusak.webp)

## Konu anlatımı

### setTimeout: biraz sonra

`setTimeout(fonksiyon, ms)` fonksiyonu **bir kez**, belirttiğin milisaniye sonra çalıştırır (1000 ms = 1 saniye):

```js
console.log("Geri sayım başladı");
setTimeout(() => {
  console.log("Kalkış!");
}, 1000);
console.log("Bu satır önce yazılır!");
```

`setTimeout` beklemez: fonksiyonu "sonra çalıştır" diye bir kenara koyar ve kod hemen devam eder. Bu yüzden son satır `Kalkış!`'tan önce yazılır.

### setInterval ve clearInterval

`setInterval(fonksiyon, ms)` fonksiyonu her `ms` milisaniyede **bir kez daha** çalıştırır, ta ki sen durdurana kadar:

```js
let count = 0;
const timer = setInterval(() => {
  count++;
  console.log("Tık", count);
  if (count === 5) clearInterval(timer);
}, 200);
```

`setInterval` bir **kimlik numarası** döndürür; sayacı durdurmak için bunu `clearInterval`'a verirsin. `setTimeout`'u da `clearTimeout` ile iptal edebilirsin.

### Üst üste binen sayaçlar

Başlat düğmesine iki kez basılırsa **iki ayrı** sayaç çalışır ve süre iki kat hızlı akar! Çözüm: sayaç zaten çalışıyorsa yenisini kurma (ya da önce eskisini durdur):

```js
let timer = null;
function start() {
  if (timer !== null) return; // zaten çalışıyor
  timer = setInterval(tick, 1000);
}
function stop() {
  clearInterval(timer);
  timer = null;
}
```

Her adımı `tick()` gibi ayrı bir fonksiyona koymak iyi bir fikir: onu elle çağırıp tek adımı deneyebilirsin. Denerken aralığı kısa tut (ör. `100` ms), iş bitince gerçek değeri (`1000`) yazarsın.

### Tarih ve saat: Date

`new Date()` şu anı verir. İçinden saat, dakika ve saniyeyi alabilirsin:

```js
const now = new Date();
const h = String(now.getHours()).padStart(2, "0");
const m = String(now.getMinutes()).padStart(2, "0");
console.log(`${h}:${m}`); // ör. 09:05
```

- `padStart(2, "0")` metni 2 karakter olana kadar başına 0 ekler: `"5"` → `"05"`.
- Belli bir anı da oluşturabilirsin: `new Date(2026, 0, 5, 9, 7, 3)` → 5 Ocak 2026, 09:07:03. Aylar **0'dan** başlar (Ocak = 0).

## Örnekler

### Gecikmeli sinyal

Sayfa:

```html
<button id="send">Sinyal gönder</button>
<p id="info">Hazır.</p>
```

```js
document.querySelector("#send").addEventListener("click", () => {
  const info = document.querySelector("#info");
  info.textContent = "Sinyal yolda...";
  setTimeout(() => {
    info.textContent = "Sinyal Mars üssüne ulaştı!";
  }, 1000);
});
```

*Düğmeye bas ve 1 saniye bekle.*

### Canlı saat

Sayfa:

```html
<p>Üs saati: <strong id="clock"></strong></p>
```

```js
const clock = document.querySelector("#clock");

function showTime() {
  clock.textContent = new Date().toLocaleTimeString("tr-TR");
}

showTime(); // hemen göster
setInterval(showTime, 1000); // sonra her saniye güncelle
```

*showTime() satırını silersen saat ilk saniye boş kalır.*

## Görevler

### Görev 1: Gecikmeli kalkış

`#launch` düğmesine tıklanınca:

- `#info` hemen `Hazırlanıyor...` olsun,
- **200 ms sonra** (`setTimeout`) `Kalkış!` olsun.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<button id="launch">Kalkış</button>
<p id="info">Beklemede</p>
```

**Başlangıç kodu:**

```js
const info = document.querySelector("#info");

// click olayını dinle, içinde setTimeout kullan
```

**İpuçları:**

1. setTimeout(() => { ... }, 200);
2. İlk metni setTimeout'un dışında, hemen yaz.

<details><summary>Çözüm</summary>

```js
const info = document.querySelector("#info");

// click olayını dinle, içinde setTimeout kullan
document.querySelector("#launch").addEventListener("click", () => {
  info.textContent = "Hazırlanıyor...";
  setTimeout(() => {
    info.textContent = "Kalkış!";
  }, 200);
});
```

</details>

### Görev 2: Uçuş süresi

Sayfa açılınca `count` her **100 ms'de** 1 artsın ve `#count`'ta görünsün (`setInterval`).

`#stop` düğmesine tıklanınca sayaç dursun (`clearInterval`).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<p>Uçuş süresi: <span id="count">0</span></p>
<button id="stop">Dur</button>
```

**Başlangıç kodu:**

```js
let count = 0;
const countEl = document.querySelector("#count");

// her 100 ms'de count'u artır

// Dur düğmesi sayacı durdursun
```

**İpuçları:**

1. const timer = setInterval(() => { ... }, 100);
2. Tıklayınca: clearInterval(timer);

<details><summary>Çözüm</summary>

```js
let count = 0;
const countEl = document.querySelector("#count");

// her 100 ms'de count'u artır
const timer = setInterval(() => {
  count++;
  countEl.textContent = count;
}, 100);

// Dur düğmesi sayacı durdursun
document.querySelector("#stop").addEventListener("click", () => {
  clearInterval(timer);
});
```

</details>

### Görev 3: Yanıp sönen işaret

İşaret ışığı `#light` her **100 ms'de** yanıp sönsün: `on` sınıfını aç/kapat (`classList.toggle`) ve `blinks` sayısını 1 artır.

6 kez değiştikten sonra (`blinks === 6`) sayaç dursun. `#blinks`'te değişim sayısı görünsün.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<div id="light"></div>
<p>Değişim: <span id="blinks">0</span></p>
```

**CSS:**

```css
#light{width:40px;height:40px;border-radius:50%;background:#333}#light.on{background:#f7df1e}
```

**Başlangıç kodu:**

```js
const light = document.querySelector("#light");
let blinks = 0;

// setInterval ile yak/söndür, 6 değişimde durdur
```

**İpuçları:**

1. light.classList.toggle("on");
2. if (blinks === 6) clearInterval(timer);

<details><summary>Çözüm</summary>

```js
const light = document.querySelector("#light");
let blinks = 0;

// setInterval ile yak/söndür, 6 değişimde durdur
const timer = setInterval(() => {
  light.classList.toggle("on");
  blinks++;
  document.querySelector("#blinks").textContent = blinks;
  if (blinks === 6) clearInterval(timer);
}, 100);
```

</details>

## Challenge: Kronometre

Bir kronometre yap. `tenths` saniyenin onda birini sayar; `#watch` onu `2.3` biçiminde göstersin (`(tenths / 10).toFixed(1)`).

- `#start`: her 100 ms'de `tenths`'i artırmaya başlasın. **Zaten çalışıyorsa** yeni sayaç kurmasın!
- `#stop`: sayacı durdursun (`timer` yeniden `null` olsun ki tekrar başlatılabilsin).
- `#reset`: durdursun, `tenths`'i 0 yapsın ve `0.0` göstersin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<p id="watch">0.0</p>
<button id="start">Başlat</button> <button id="stop">Durdur</button> <button id="reset">Sıfırla</button>
```

**CSS:**

```css
#watch{font-family:monospace;font-size:28px;margin:4px 0}
```

**Başlangıç kodu:**

```js
let tenths = 0;
let timer = null;
const watch = document.querySelector("#watch");

function show() {
  watch.textContent = (tenths / 10).toFixed(1);
}

// Başlat, Durdur ve Sıfırla düğmelerini dinle
```

**İpuçları:**

1. if (timer !== null) return; iki kez başlatmayı engeller.
2. Durdururken: clearInterval(timer); timer = null;

<details><summary>Çözüm</summary>

```js
let tenths = 0;
let timer = null;
const watch = document.querySelector("#watch");

function show() {
  watch.textContent = (tenths / 10).toFixed(1);
}

function stop() {
  clearInterval(timer);
  timer = null;
}

// Başlat, Durdur ve Sıfırla düğmelerini dinle
document.querySelector("#start").addEventListener("click", () => {
  if (timer !== null) return; // zaten çalışıyor
  timer = setInterval(() => {
    tenths++;
    show();
  }, 100);
});
document.querySelector("#stop").addEventListener("click", stop);
document.querySelector("#reset").addEventListener("click", () => {
  stop();
  tenths = 0;
  show();
});
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Süre sayacı**

### Yıldız Avcısı: Süre sayacı

Oyunun 10 saniyelik süresi olsun. İki fonksiyon yaz:

- `tick()`: `timeLeft`'i 1 azaltsın (0'ın altına inmesin) ve `#time`'a yazsın. 0 olunca sayacı durdursun (`clearInterval`) ve `#info`'ya `Süre doldu!` yazsın.
- `startTimer()`: önce eski sayacı durdursun, `timeLeft`'i 10 yapıp `#time`'a yazsın, sonra `setInterval(tick, TICK_MS)` ile sayacı başlatsın.

Form gönderilince `startTimer()` zaten çağrılıyor. Denemesi kolay olsun diye `TICK_MS` şimdilik 100 ms; gerçek oyunda 1000 yaparsın.

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
const TICK_MS = 100; // gerçek oyunda 1000 (1 saniye)
let timeLeft = 10;
let timer = null;
const timeEl = document.querySelector("#time");
const info = document.querySelector("#info");

function tick() {
  // 1 azalt (0'ın altına inme), #time'a yaz; 0 olunca durdur ve "Süre doldu!" yaz
}

function startTimer() {
  // eski sayacı durdur, süreyi 10 yap, setInterval ile başlat
}

document.querySelector("#pilot-form").addEventListener("submit", (e) => {
  e.preventDefault();
  startTimer();
});
```

**İpuçları:**

1. if (timeLeft > 0) timeLeft--;
2. startTimer'ın ilk satırı: clearInterval(timer);
3. timer = setInterval(tick, TICK_MS);

<details><summary>Çözüm</summary>

```js
const TICK_MS = 100; // gerçek oyunda 1000 (1 saniye)
let timeLeft = 10;
let timer = null;
const timeEl = document.querySelector("#time");
const info = document.querySelector("#info");

function tick() {
  // 1 azalt (0'ın altına inme), #time'a yaz; 0 olunca durdur ve "Süre doldu!" yaz
  if (timeLeft > 0) timeLeft--;
  timeEl.textContent = timeLeft;
  if (timeLeft === 0) {
    clearInterval(timer);
    timer = null;
    info.textContent = "Süre doldu!";
  }
}

function startTimer() {
  // eski sayacı durdur, süreyi 10 yap, setInterval ile başlat
  clearInterval(timer);
  timeLeft = 10;
  timeEl.textContent = timeLeft;
  info.textContent = "Yıldızları topla!";
  timer = setInterval(tick, TICK_MS);
}

document.querySelector("#pilot-form").addEventListener("submit", (e) => {
  e.preventDefault();
  startTimer();
});
```

</details>

### Kişisel Web Sitem: Canlı saat

Sitenin başlığında canlı bir saat olsun.

- `formatTime(date)`: verilen `Date`'i `"09:07:03"` biçiminde (saat:dakika:saniye, her biri 2 haneli) döndürsün.
- `updateClock()`: `#clock`'a `formatTime(new Date())` yazsın.
- Sayfa açılınca `updateClock()` hemen çalışsın, sonra `setInterval` ile her saniye tekrarlansın.

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
const clock = document.querySelector("#clock");

function formatTime(date) {
  // saat, dakika, saniye → "HH:MM:SS" (padStart ile)
}

function updateClock() {
  // #clock'a şimdiki saati yaz
}

// hemen göster ve her saniye güncelle
```

**İpuçları:**

1. String(date.getHours()).padStart(2, "0")
2. return `${h}:${m}:${s}`;
3. updateClock(); setInterval(updateClock, 1000);

<details><summary>Çözüm</summary>

```js
const clock = document.querySelector("#clock");

function formatTime(date) {
  // saat, dakika, saniye → "HH:MM:SS" (padStart ile)
  const h = String(date.getHours()).padStart(2, "0");
  const m = String(date.getMinutes()).padStart(2, "0");
  const s = String(date.getSeconds()).padStart(2, "0");
  return `${h}:${m}:${s}`;
}

function updateClock() {
  // #clock'a şimdiki saati yaz
  clock.textContent = formatTime(new Date());
}

// hemen göster ve her saniye güncelle
updateClock();
setInterval(updateClock, 1000);
```

</details>

### Çalışma Asistanım: Odak zamanlayıcısı

25 dakikalık odak zamanlayıcısı yapalım. `render()` hazır. Üç fonksiyon yaz:

- `tick()`: `secondsLeft`'i 1 azaltsın (0'ın altına inmesin) ve `render()` çağırsın. 0 olunca `pause()` çağırsın ve `#focus-msg`'ye `Mola zamanı!` yazsın.
- `start()`: sayaç **zaten çalışıyorsa hiçbir şey yapmasın**; değilse `setInterval(tick, TICK_MS)` ile başlasın.
- `pause()`: sayacı durdursun ve `timer`'ı `null` yapsın.

`TICK_MS` denemek için 100 ms; gerçekte 1000 olur.

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
const TICK_MS = 100; // gerçekte 1000 (1 saniye)
let secondsLeft = 25 * 60;
let timer = null;

function render() {
  const m = String(Math.floor(secondsLeft / 60)).padStart(2, "0");
  const s = String(secondsLeft % 60).padStart(2, "0");
  document.querySelector("#focus-time").textContent = `${m}:${s}`;
}

function tick() {
  // 1 azalt, render(); 0 olunca pause() ve "Mola zamanı!"
}

function start() {
  // zaten çalışıyorsa çık; değilse setInterval ile başlat
}

function pause() {
  // sayacı durdur
}

document.querySelector("#focus-start").addEventListener("click", start);
document.querySelector("#focus-pause").addEventListener("click", pause);
render();
```

**İpuçları:**

1. if (timer !== null) return;
2. timer = setInterval(tick, TICK_MS);
3. pause: clearInterval(timer); timer = null;

<details><summary>Çözüm</summary>

```js
const TICK_MS = 100; // gerçekte 1000 (1 saniye)
let secondsLeft = 25 * 60;
let timer = null;

function render() {
  const m = String(Math.floor(secondsLeft / 60)).padStart(2, "0");
  const s = String(secondsLeft % 60).padStart(2, "0");
  document.querySelector("#focus-time").textContent = `${m}:${s}`;
}

function tick() {
  // 1 azalt, render(); 0 olunca pause() ve "Mola zamanı!"
  if (secondsLeft > 0) secondsLeft--;
  render();
  if (secondsLeft === 0) {
    pause();
    document.querySelector("#focus-msg").textContent = "Mola zamanı!";
  }
}

function start() {
  // zaten çalışıyorsa çık; değilse setInterval ile başlat
  if (timer !== null) return;
  timer = setInterval(tick, TICK_MS);
}

function pause() {
  // sayacı durdur
  clearInterval(timer);
  timer = null;
}

document.querySelector("#focus-start").addEventListener("click", start);
document.querySelector("#focus-pause").addEventListener("click", pause);
render();
```

</details>

### Bilgi Yarışması: Süreli soru

Her soru için 10 saniye var! İki fonksiyon yaz ve `answer`'a bir satır ekle:

- `tick()`: `timeLeft`'i 1 azaltsın (0'ın altına inmesin), `#time`'a yazsın. 0 olunca sayacı durdursun, `answered = true` yapsın, `#feedback`'e `Süre doldu!` yazsın ve bütün seçenek düğmelerini kapatsın (`btn.disabled = true`).
- `startQuestion()`: eski sayacı durdursun; `timeLeft = 10`, `answered = false`, `#feedback` boş, düğmeler açık (`disabled = false`) olsun; sonra `setInterval(tick, TICK_MS)` ile başlasın.
- `answer(index)` içinde cevap verilince sayaç dursun (`clearInterval(timer)`).

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
const TICK_MS = 100; // gerçekte 1000 (1 saniye)
let timeLeft = 10;
let timer = null;
const timeEl = document.querySelector("#time");

function answer(index) {
  if (answered) return;
  answered = true;
  // sayacı durdur
  if (index === question.correct) {
    score += 10;
    document.querySelector("#score").textContent = score;
    feedback.textContent = "Doğru!";
  } else {
    feedback.textContent = `Yanlış! Doğru cevap: ${question.options[question.correct]}`;
  }
}
buttons.forEach((btn, i) => btn.addEventListener("click", () => answer(i)));

function tick() {
  // süreyi azalt; 0 olunca durdur, "Süre doldu!", düğmeleri kapat
}

function startQuestion() {
  // her şeyi sıfırla ve sayacı başlat
}

document.querySelector("#player-form").addEventListener("submit", (e) => {
  e.preventDefault();
  startQuestion();
});
```

**İpuçları:**

1. buttons.forEach((btn) => (btn.disabled = true));
2. startQuestion'ın ilk satırı: clearInterval(timer);
3. answer içinde: clearInterval(timer);

<details><summary>Çözüm</summary>

```js
const question = { text: "Ay, hangi gezegenin uydusudur?", options: ["Mars", "Dünya", "Jüpiter"], correct: 1 };
const buttons = document.querySelectorAll(".option");
const feedback = document.querySelector("#feedback");
let score = 0;
let answered = false;
const TICK_MS = 100; // gerçekte 1000 (1 saniye)
let timeLeft = 10;
let timer = null;
const timeEl = document.querySelector("#time");

function answer(index) {
  if (answered) return;
  answered = true;
  // sayacı durdur
  clearInterval(timer);
  if (index === question.correct) {
    score += 10;
    document.querySelector("#score").textContent = score;
    feedback.textContent = "Doğru!";
  } else {
    feedback.textContent = `Yanlış! Doğru cevap: ${question.options[question.correct]}`;
  }
}
buttons.forEach((btn, i) => btn.addEventListener("click", () => answer(i)));

function tick() {
  // süreyi azalt; 0 olunca durdur, "Süre doldu!", düğmeleri kapat
  if (timeLeft > 0) timeLeft--;
  timeEl.textContent = timeLeft;
  if (timeLeft === 0) {
    clearInterval(timer);
    answered = true;
    feedback.textContent = "Süre doldu!";
    buttons.forEach((btn) => (btn.disabled = true));
  }
}

function startQuestion() {
  // her şeyi sıfırla ve sayacı başlat
  clearInterval(timer);
  timeLeft = 10;
  answered = false;
  feedback.textContent = "";
  timeEl.textContent = timeLeft;
  buttons.forEach((btn) => (btn.disabled = false));
  timer = setInterval(tick, TICK_MS);
}

document.querySelector("#player-form").addEventListener("submit", (e) => {
  e.preventDefault();
  startQuestion();
});
```

</details>
