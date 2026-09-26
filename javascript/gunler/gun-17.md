# Gün 17: Klavye ve ses

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Olay Kuşağı  ·  **Maskot:** Kodi

**Bugünün hedefi:** keydown/keyup ile tuşlara tepki vermek, bir elemanı klavyeyle hareket ettirmek ve Web Audio ile bip sesi çalmak

> Olay Kuşağı'na girdin! Burada her şey bir sinyale tepki veriyor. Bugün gemini **klavyeyle** yöneteceksin, üstüne bir de ses ekleyeceksin.

![Olay Kuşağı](../../gorseller/javascript/bolgeler/kusak.webp)

## Konu anlatımı

### keydown ve keyup

Bir tuşa bastığın an `keydown`, bıraktığın an `keyup` olayı olur. Tuşları bütün sayfada dinlemek için olayı `document`'a bağlarız. Hangi tuşa basıldığı `e.key`'dedir:

```js
document.addEventListener("keydown", (e) => {
  console.log("Basıldı:", e.key);
});
```

| Tuş | e.key |
|---|---|
| Sol / sağ ok | `"ArrowLeft"` / `"ArrowRight"` |
| Yukarı / aşağı ok | `"ArrowUp"` / `"ArrowDown"` |
| Enter | `"Enter"` |
| Boşluk | `" "` (içinde tek boşluk olan metin) |
| Esc | `"Escape"` |
| Harf ve rakamlar | `"a"`, `"A"`, `"1"` |

Önizleme tuşları duysun diye önce önizlemenin içine bir kez tıkla.

### Bir elemanı hareket ettirmek

Bir elemanın yerini değiştirmek için konumunu bir değişkende tut; değişince CSS'ini güncelle. Eleman `position: absolute` ise `style.left` kullanılabilir, `transform` ise her elemanda çalışır:

```js
let x = 0;
function move(dx) {
  x = Math.max(0, Math.min(260, x + dx)); // 0 ile 260 arasında tut
  rocket.style.left = x + "px";
  // ya da: rocket.style.transform = `translateX(${x}px)`;
}
```

`Math.min(260, ...)` 260'tan büyük sayıyı 260 yapar, `Math.max(0, ...)` sıfırdan küçüğünü 0 yapar. Böylece roket alanın dışına kaçmaz. Buna **sınırlamak** denir.

### Varsayılan davranışı durdurmak

Ok tuşları ve boşluk normalde sayfayı kaydırır. Oyunda bunu istemeyiz: yalnızca **kendi kullandığın** tuşlar için `e.preventDefault()` çağır.

Kullanıcı bir kutuya yazı yazıyorsa kısayollar çalışmamalı. Olayın hangi elemanda olduğunu `e.target` söyler:

```js
document.addEventListener("keydown", (e) => {
  if (e.target.tagName === "INPUT") return; // kutuya yazılıyor
  if (e.key === "ArrowLeft" || e.key === "ArrowRight") {
    e.preventDefault(); // sayfa kaymasın
  }
});
```

### Ses: Web Audio ile bip

Tarayıcı kendi başına ses üretebilir! `AudioContext` küçük bir ses stüdyosu, `oscillator` ise ton üreten bir hoparlör gibidir:

```js
function beep(freq = 440) {
  try {
    const audio = new AudioContext();
    const osc = audio.createOscillator();
    osc.frequency.value = freq; // büyüdükçe ses incelir
    osc.connect(audio.destination);
    osc.start();
    osc.stop(audio.currentTime + 0.15); // 0,15 saniye çal
  } catch (err) {
    console.log("Ses çalınamadı.");
  }
}
```

`try { ... } catch (err) { ... }`: içerideki kod hata verirse program durmaz, `catch` kısmı çalışır (24. günde ayrıntısıyla göreceğiz).

Tarayıcılar sesi ancak kullanıcı bir yere tıkladıktan ya da bir tuşa bastıktan sonra çalar. Ses her cihazda çalışmayabilir; bu yüzden oyunun geri kalanı sese **bağlı olmamalı**.

## Örnekler

### Ok tuşlarıyla nokta

Sayfa:

```html
<div id="area"><div id="dot"></div></div>
<p id="info">Önizlemeye tıkla, sonra ok tuşlarına bas.</p>
```

```js
const dot = document.querySelector("#dot");
let x = 0;
let y = 0;
document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowRight") x += 20;
  else if (e.key === "ArrowLeft") x -= 20;
  else if (e.key === "ArrowDown") y += 20;
  else if (e.key === "ArrowUp") y -= 20;
  else return;
  e.preventDefault();
  x = Math.max(0, Math.min(220, x));
  y = Math.max(0, Math.min(100, y));
  dot.style.left = x + "px";
  dot.style.top = y + "px";
  document.querySelector("#info").textContent = `${e.key} → x: ${x}, y: ${y}`;
});
```

*Nokta alanın kenarından dışarı çıkabiliyor mu? Dene.*

### Bip sesi

Sayfa:

```html
<button id="beep">Bip!</button>
<p>Ya da önizlemeye tıklayıp <b>b</b> tuşuna bas.</p>
```

```js
let audio = null;
function beep(freq = 440) {
  try {
    audio = audio || new AudioContext();
    const osc = audio.createOscillator();
    const gain = audio.createGain();
    osc.frequency.value = freq;
    gain.gain.value = 0.1; // ses düzeyi
    osc.connect(gain);
    gain.connect(audio.destination);
    osc.start();
    osc.stop(audio.currentTime + 0.15);
  } catch (err) {
    console.log("Ses çalınamadı:", err.message);
  }
}

document.querySelector("#beep").addEventListener("click", () => beep());
document.addEventListener("keydown", (e) => {
  if (e.key === "b") beep(660);
});
```

*Sesin açık olsun. Ses çalmazsa sorun değil; görevlerde ses gerekmiyor.*

## Görevler

### Görev 1: Tuş dedektörü

Bir tuşa basılınca (`keydown`) `#key` paragrafına `Basılan tuş: a` biçiminde tuşun adını yaz.

Boşluk tuşunun `e.key` değeri görünmez bir `" "` olduğu için onun yerine `Boşluk` yaz: `Basılan tuş: Boşluk`.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<p id="key">Önizlemeye tıkla ve bir tuşa bas.</p>
```

**Başlangıç kodu:**

```js
// keydown olayını document üzerinde dinle
```

**İpuçları:**

1. document.addEventListener("keydown", (e) => { ... })
2. const name = e.key === " " ? "Boşluk" : e.key;

<details><summary>Çözüm</summary>

```js
// keydown olayını document üzerinde dinle
document.addEventListener("keydown", (e) => {
  const name = e.key === " " ? "Boşluk" : e.key;
  document.querySelector("#key").textContent = `Basılan tuş: ${name}`;
});
```

</details>

### Görev 2: Roketi kaydır

Sağ ok (`ArrowRight`) `x`'i 20 artırsın, sol ok (`ArrowLeft`) 20 azaltsın. `x` hep **0 ile 260 arasında** kalsın.

Her hareketten sonra:

- roketi `transform` ile taşı: `rocket.style.transform` değeri `translateX(40px)` biçiminde olsun,
- `#pos`'a `x: 40` yaz.

Oklarda `e.preventDefault()` çağır; başka tuşlar hiçbir şeyi değiştirmesin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<div id="track"><div id="rocket"></div></div>
<p id="pos">x: 0</p>
```

**CSS:**

```css
#track{width:300px;height:50px;background:#0b1026;border-radius:8px}#rocket{width:40px;height:40px;margin-top:5px;background:#f7df1e;border-radius:50%}
```

**Başlangıç kodu:**

```js
const rocket = document.querySelector("#rocket");
let x = 0;

// keydown dinle
```

**İpuçları:**

1. x = Math.max(0, Math.min(260, x)); x'i sınırlar.
2. rocket.style.transform = `translateX(${x}px)`;

<details><summary>Çözüm</summary>

```js
const rocket = document.querySelector("#rocket");
let x = 0;

// keydown dinle
document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowRight") x += 20;
  else if (e.key === "ArrowLeft") x -= 20;
  else return;
  e.preventDefault();
  x = Math.max(0, Math.min(260, x));
  rocket.style.transform = `translateX(${x}px)`;
  document.querySelector("#pos").textContent = `x: ${x}`;
});
```

</details>

### Görev 3: Motor düğmesi

Boşluk tuşu basılı tutulduğu sürece motor çalışsın:

- Boşluk basılınca (`keydown`): `#engine` metni `Motor: AÇIK` olsun ve `on` sınıfı eklensin.
- Boşluk bırakılınca (`keyup`): `Motor: KAPALI` olsun ve `on` sınıfı kaldırılsın.

Boşlukta `e.preventDefault()` çağırmayı unutma; diğer tuşlar motoru etkilemesin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<p id="engine">Motor: KAPALI</p><p>Önizlemeye tıkla, sonra boşluk tuşunu basılı tut.</p>
```

**CSS:**

```css
#engine{font-size:20px}#engine.on{color:#e65100;font-weight:700}
```

**Başlangıç kodu:**

```js
const engine = document.querySelector("#engine");

// keydown ve keyup dinle
```

**İpuçları:**

1. if (e.key !== " ") return; diğer tuşları atlar.
2. İki ayrı dinleyici yaz: biri keydown, biri keyup.

<details><summary>Çözüm</summary>

```js
const engine = document.querySelector("#engine");

// keydown ve keyup dinle
document.addEventListener("keydown", (e) => {
  if (e.key !== " ") return;
  e.preventDefault();
  engine.textContent = "Motor: AÇIK";
  engine.classList.add("on");
});

document.addEventListener("keyup", (e) => {
  if (e.key !== " ") return;
  engine.textContent = "Motor: KAPALI";
  engine.classList.remove("on");
});
```

</details>

## Challenge: Gizli kod

Oyunlarda gizli kodlar vardır! Basılan tuşları `pressed` dizisinde tut, ama dizide hep **en son 4 tuş** kalsın (`slice(-4)`).

Son 4 tuş sırasıyla `ArrowUp`, `ArrowUp`, `ArrowDown`, `ArrowDown` olunca `#secret`'e `Gizli mod açıldı!` yaz.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<p id="secret">Kodu gir...</p>
```

**Başlangıç kodu:**

```js
const CODE = ["ArrowUp", "ArrowUp", "ArrowDown", "ArrowDown"];
let pressed = [];

// keydown dinle: tuşu ekle, son 4 tuşu tut, kodla karşılaştır
```

**İpuçları:**

1. pressed.push(e.key); sonra pressed = pressed.slice(-4);
2. İki diziyi karşılaştırmak için metne çevir: pressed.join(",") === CODE.join(",")

<details><summary>Çözüm</summary>

```js
const CODE = ["ArrowUp", "ArrowUp", "ArrowDown", "ArrowDown"];
let pressed = [];

// keydown dinle: tuşu ekle, son 4 tuşu tut, kodla karşılaştır
document.addEventListener("keydown", (e) => {
  pressed.push(e.key);
  pressed = pressed.slice(-4);
  if (pressed.join(",") === CODE.join(",")) {
    document.querySelector("#secret").textContent = "Gizli mod açıldı!";
  }
});
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Klavye kontrolü ve sesler**

### Yıldız Avcısı: Klavye kontrolü

Gemiyi ok tuşlarıyla yönetelim. `moveShip(dx)` fonksiyonunu yaz:

- `x`'i `dx` kadar değiştirsin ve **0 ile `MAX_X` (270) arasında** tutsun,
- gemiyi yerleştirsin: `ship.style.left = x + "px"`,
- istersen gemi duvara çarpınca hazır `beep()` fonksiyonuyla ses çalsın (zorunlu değil).

Sonra `keydown` dinle: sol ok `moveShip(-STEP)`, sağ ok `moveShip(STEP)` çağırsın ve `e.preventDefault()` ile sayfa kaymasın. Pilot adı kutusuna yazı yazılırken oklar gemiyi oynatmasın.

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
const ship = document.querySelector("#ship");
const STEP = 20;
const MAX_X = 270; // alan 300px, gemi 30px genişliğinde
let x = 0;

// Bip sesi (hazır): ses çalamazsa oyun sessizce devam eder
let audio = null;
function beep(freq = 440) {
  try {
    audio = audio || new AudioContext();
    const osc = audio.createOscillator();
    const gain = audio.createGain();
    osc.frequency.value = freq;
    gain.gain.value = 0.05;
    osc.connect(gain);
    gain.connect(audio.destination);
    osc.start();
    osc.stop(audio.currentTime + 0.1);
  } catch (err) {
    // ses yoksa sorun değil
  }
}

function moveShip(dx) {
  // x'i değiştir, 0 ile MAX_X arasında tut, gemiyi yerleştir
}

// keydown dinle
```

**İpuçları:**

1. x = Math.max(0, Math.min(MAX_X, x));
2. ship.style.left = x + "px";
3. Kutuya yazılıyorsa çık: if (e.target.tagName === "INPUT") return;

<details><summary>Çözüm</summary>

```js
const ship = document.querySelector("#ship");
const STEP = 20;
const MAX_X = 270; // alan 300px, gemi 30px genişliğinde
let x = 0;

// Bip sesi (hazır): ses çalamazsa oyun sessizce devam eder
let audio = null;
function beep(freq = 440) {
  try {
    audio = audio || new AudioContext();
    const osc = audio.createOscillator();
    const gain = audio.createGain();
    osc.frequency.value = freq;
    gain.gain.value = 0.05;
    osc.connect(gain);
    gain.connect(audio.destination);
    osc.start();
    osc.stop(audio.currentTime + 0.1);
  } catch (err) {
    // ses yoksa sorun değil
  }
}

function moveShip(dx) {
  // x'i değiştir, 0 ile MAX_X arasında tut, gemiyi yerleştir
  x = x + dx;
  if (x < 0 || x > MAX_X) beep(220); // duvara çarptı
  x = Math.max(0, Math.min(MAX_X, x));
  ship.style.left = x + "px";
}

// keydown dinle
document.addEventListener("keydown", (e) => {
  if (e.target.tagName === "INPUT") return;
  if (e.key === "ArrowLeft") {
    e.preventDefault();
    moveShip(-STEP);
  } else if (e.key === "ArrowRight") {
    e.preventDefault();
    moveShip(STEP);
  }
});
```

</details>

### Kişisel Web Sitem: Klavye kısayolları

Sitene klavye kısayolları ekle:

- `t`: `body`'deki `dark` sınıfını aç/kapat (tema değişsin).
- `/`: arama kutusuna (`#search`) odaklan (`search.focus()`). `/` kutuya yazılmasın diye `e.preventDefault()` çağır.
- Arama kutusundayken `Escape`: kutuyu boşalt ve odaktan çıkar (`search.blur()`).

Bir kutuya yazı yazılırken (`e.target.tagName === "INPUT"`) `t` ve `/` kısayolları çalışmasın.

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
const search = document.querySelector("#search");

// keydown dinle
```

**İpuçları:**

1. document.body.classList.toggle("dark");
2. if (e.target.tagName === "INPUT") return;
3. Escape kontrolünü INPUT kontrolünden ÖNCE yaz; yoksa kutudayken hiç çalışmaz.

<details><summary>Çözüm</summary>

```js
const search = document.querySelector("#search");

// keydown dinle
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && e.target === search) {
    search.value = "";
    search.blur();
    return;
  }
  if (e.target.tagName === "INPUT") return; // yazı yazılıyor
  if (e.key === "t") {
    document.body.classList.toggle("dark");
  } else if (e.key === "/") {
    e.preventDefault();
    search.focus();
  }
});
```

</details>

### Çalışma Asistanım: Kısayollar

Asistanını klavyeyle hızlı kullanmak için kısayollar ekle (Enter'a basınca form zaten gönderiliyor):

- `Escape`: görev kutusunu (`input`) ve `#task-msg`'yi boşalt. Bu kısayol kutudayken de çalışsın.
- `n`: görev kutusuna odaklan (`input.focus()`) ve `e.preventDefault()` çağır.
- `Delete`: listedeki **son** görevi sil (`list.lastElementChild`); liste boşsa hiçbir şey yapma.

Kutuya yazı yazılırken (`e.target === input`) `n` ve `Delete` çalışmasın.

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
const form = document.querySelector("#task-form");
const input = document.querySelector("#task-input");
const msg = document.querySelector("#task-msg");
const list = document.querySelector("#task-list");

function addTask(text) {
  const li = document.createElement("li");
  li.textContent = text;
  list.append(li);
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (text === "") {
    msg.textContent = "Görev boş olamaz.";
    return;
  }
  msg.textContent = "";
  addTask(text);
  form.reset();
});

addTask("Matematik ödevi");
addTask("Fizik tekrarı");

// Kısayollar: keydown dinle
```

**İpuçları:**

1. if (e.key === "Escape") { input.value = ""; ... }
2. const last = list.lastElementChild; if (last) last.remove();
3. if (e.target === input) return;

<details><summary>Çözüm</summary>

```js
const form = document.querySelector("#task-form");
const input = document.querySelector("#task-input");
const msg = document.querySelector("#task-msg");
const list = document.querySelector("#task-list");

function addTask(text) {
  const li = document.createElement("li");
  li.textContent = text;
  list.append(li);
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (text === "") {
    msg.textContent = "Görev boş olamaz.";
    return;
  }
  msg.textContent = "";
  addTask(text);
  form.reset();
});

addTask("Matematik ödevi");
addTask("Fizik tekrarı");

// Kısayollar: keydown dinle
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape") {
    input.value = "";
    msg.textContent = "";
    return;
  }
  if (e.target === input) return; // yazı yazılıyor
  if (e.key === "n") {
    e.preventDefault();
    input.focus();
  } else if (e.key === "Delete") {
    const last = list.lastElementChild;
    if (last) last.remove();
  }
});
```

</details>

### Bilgi Yarışması: Tuşlarla cevap

Yarışmacılar fareye uzanmadan cevap versin: `1`, `2`, `3` tuşları sırasıyla 1., 2. ve 3. seçeneği seçsin. Bunun için hazır `answer(index)` fonksiyonunu çağır (index 0'dan başlar: `1` tuşu → `answer(0)`).

- Başka tuşlar hiçbir şey yapmasın.
- Yarışmacı adı kutusuna yazı yazılırken rakam tuşları cevap vermesin.
- Tuşu sayıya çevirmek için `Number(e.key)` kullan; her rakam için ayrı `if` yazma.

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
  if (index === question.correct) {
    score += 10;
    document.querySelector("#score").textContent = score;
    feedback.textContent = "Doğru!";
  } else {
    feedback.textContent = `Yanlış! Doğru cevap: ${question.options[question.correct]}`;
  }
}
buttons.forEach((btn, i) => btn.addEventListener("click", () => answer(i)));

// keydown dinle: 1, 2, 3 tuşları
```

**İpuçları:**

1. ["1", "2", "3"].includes(e.key) doğru tuş mu diye bakar.
2. answer(Number(e.key) - 1);

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
  if (index === question.correct) {
    score += 10;
    document.querySelector("#score").textContent = score;
    feedback.textContent = "Doğru!";
  } else {
    feedback.textContent = `Yanlış! Doğru cevap: ${question.options[question.correct]}`;
  }
}
buttons.forEach((btn, i) => btn.addEventListener("click", () => answer(i)));

// keydown dinle: 1, 2, 3 tuşları
document.addEventListener("keydown", (e) => {
  if (e.target.tagName === "INPUT") return;
  if (["1", "2", "3"].includes(e.key)) {
    answer(Number(e.key) - 1);
  }
});
```

</details>
