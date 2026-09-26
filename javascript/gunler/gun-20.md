# Gün 20: Kalıcı veri

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Olay Kuşağı  ·  **Maskot:** Kodi

**Bugünün hedefi:** localStorage ile sayı, metin, dizi ve nesne saklamak; açılışta kayıtlı veriyi yükleyip varsayılan değer kullanmak

> Sayfayı yenileyince skorun sıfırlanıyor mu? Olay Kuşağı'nın son durağında gemine bir **hafıza** takıyoruz: localStorage sayesinde bilgiler sayfa kapansa da kalacak.

![Olay Kuşağı](../../gorseller/javascript/bolgeler/kusak.webp)

## Konu anlatımı

### localStorage: tarayıcının defteri

`localStorage` her sitenin tarayıcıda kendine ait küçük bir defteridir. Sayfa kapansa, bilgisayar yeniden açılsa da içindekiler kalır. Bilgiler **anahtar** ve **değer** çiftleri olarak saklanır:

```js
localStorage.setItem("pilot", "Ada");      // kaydet
const name = localStorage.getItem("pilot"); // oku → "Ada"
localStorage.removeItem("pilot");          // sil
localStorage.getItem("pilot");             // kayıt yoksa → null
```

Bu kursun önizlemesinde `localStorage` bir taklittir: aynı görevde çalıştırmalar arasında korunur ama gerçek tarayıcı defterine yazmaz.

### Sayılar metin olarak saklanır

`localStorage` her şeyi **metin** olarak saklar. Sayı kaydedip geri okuduğunda metin gelir; hesap yapmadan önce `Number(...)` ile çevir:

```js
localStorage.setItem("best", 42);
localStorage.getItem("best");                      // "42" (metin!)
const best = Number(localStorage.getItem("best")) || 0; // 42
```

Kayıt yoksa `getItem` `null` verir; `Number(null)` da `0` olur. Sondaki `|| 0` ise `NaN` gibi yanlış sayılan değerlerde de 0 kullanılmasını sağlar.

- `a || b`: `a` yanlış sayılıyorsa (`0`, `""`, `null`, `NaN`...) `b`'yi kullanır.
- `a ?? b`: yalnızca `a` `null` ya da `undefined` ise `b`'yi kullanır. `0` ve `""` korunur.

### Diziler ve nesneler: JSON

Dizi ya da nesneyi saklamak için önce **JSON** metnine çevirirsin (`JSON.stringify`), okurken geri çevirirsin (`JSON.parse`). 12. günden hatırlıyorsun:

```js
const items = ["kalkan", "lazer"];
localStorage.setItem("inventory", JSON.stringify(items)); // '["kalkan","lazer"]'

const back = JSON.parse(localStorage.getItem("inventory")) ?? [];
console.log(back.length); // 2
```

`JSON.parse(null)` sonucu `null` olur; `?? []` sayesinde kayıt yoksa boş bir dizi kullanırız.

### Açılışta yükle, değişince kaydet

Kalıcı veri kullanan her sayfa aynı düzeni izler:

1. Sayfa açılınca kayıtlı veriyi **yükle** (yoksa varsayılan değeri kullan).
2. Veriyi ekranda **göster**.
3. Veri her değiştiğinde yeniden **kaydet**.

Ayarlar gibi nesnelerde, eksik kalan alanları varsayılanlarla doldurmak için yayma (`...`) işe yarar:

```js
const DEFAULTS = { sound: true, volume: 5 };
const saved = JSON.parse(localStorage.getItem("settings")) ?? {};
const settings = { ...DEFAULTS, ...saved }; // kayıtlı olanlar varsayılanın üstüne yazılır
```

Yükleme işini `loadBest()` gibi bir fonksiyona koymak işini kolaylaştırır: onu farklı kayıtlarla tekrar tekrar deneyebilirsin.

## Örnekler

### Kaptan notu

Sayfa:

```html
<textarea id="note" rows="3" cols="30" placeholder="Kaptan notu..."></textarea>
<p id="info"></p>
```

```js
const note = document.querySelector("#note");
note.value = localStorage.getItem("note") ?? "";

note.addEventListener("input", () => {
  localStorage.setItem("note", note.value);
  document.querySelector("#info").textContent = "Kaydedildi.";
});
```

*Bir şey yaz ve Çalıştır'a yeniden bas: notun yerinde duruyor. Gerçek bir sitede sayfa yenilense de kalır.*

### Liste kaydetmek (JSON)

Sayfa:

```html
<p>Gezegenler: <strong id="out"></strong></p>
```

```js
const planets = ["Mars", "Venüs"];
localStorage.setItem("planets", JSON.stringify(planets));

const text = localStorage.getItem("planets");
console.log("Saklanan metin:", text);

const back = JSON.parse(text);
console.log("Geri gelen dizi:", back, "uzunluk:", back.length);

document.querySelector("#out").textContent = back.join(" ve ");
```

*Çıktı alanında saklanan metnin tırnaklı bir JSON metni olduğuna bak.*

## Görevler

### Görev 1: Ziyaret sayacı

`countVisit()` fonksiyonunu yaz:

- `visits` anahtarındaki sayıyı okusun (yoksa 0),
- 1 artırıp geri kaydetsin,
- `#info`'ya `Bu sayfayı 5. kez açtın.` biçiminde yazsın.

Sayfa açılınca `countVisit()` bir kez çalışsın. (Önizleme 4 ziyaretle başlıyor.)

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<p id="info"></p>
```

**Başlangıç kodu:**

```js
function countVisit() {
  // oku (yoksa 0), 1 artır, kaydet, göster
}

countVisit();
```

**İpuçları:**

1. const visits = (Number(localStorage.getItem("visits")) || 0) + 1;
2. localStorage.setItem("visits", String(visits));

<details><summary>Çözüm</summary>

```js
function countVisit() {
  // oku (yoksa 0), 1 artır, kaydet, göster
  const visits = (Number(localStorage.getItem("visits")) || 0) + 1;
  localStorage.setItem("visits", String(visits));
  document.querySelector("#info").textContent = `Bu sayfayı ${visits}. kez açtın.`;
}

countVisit();
```

</details>

### Görev 2: Pilotu hatırla

`showGreeting()` fonksiyonunu yaz: `pilot` anahtarında bir ad kayıtlıysa `#hello`'ya `Tekrar hoş geldin, Deniz!`, yoksa `Merhaba, yeni pilot!` yazsın. Sayfa açılınca çalışsın.

- `#name-form` gönderilince ad (boşlukları temizlenmiş, boş değilse) `pilot` anahtarına kaydedilsin ve selam güncellensin.
- `#forget` düğmesi kaydı silsin (`removeItem`) ve selamı güncellesin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<form id="name-form"><input id="name" placeholder="Pilot adı"> <button>Kaydet</button></form>
<button id="forget">Unut</button>
<p id="hello"></p>
```

**Başlangıç kodu:**

```js
const hello = document.querySelector("#hello");

function showGreeting() {
  // kayıtlı ad varsa tekrar hoş geldin, yoksa merhaba
}

// form: kaydet; Unut: sil

showGreeting();
```

**İpuçları:**

1. const name = localStorage.getItem("pilot"); kayıt yoksa null verir.
2. localStorage.removeItem("pilot");

<details><summary>Çözüm</summary>

```js
const hello = document.querySelector("#hello");

function showGreeting() {
  // kayıtlı ad varsa tekrar hoş geldin, yoksa merhaba
  const name = localStorage.getItem("pilot");
  hello.textContent = name ? `Tekrar hoş geldin, ${name}!` : "Merhaba, yeni pilot!";
}

// form: kaydet; Unut: sil
document.querySelector("#name-form").addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.querySelector("#name").value.trim();
  if (name === "") return;
  localStorage.setItem("pilot", name);
  showGreeting();
});

document.querySelector("#forget").addEventListener("click", () => {
  localStorage.removeItem("pilot");
  showGreeting();
});

showGreeting();
```

</details>

### Görev 3: Envanter kaydı

Envanter bir dizi ve `inventory` anahtarında JSON olarak saklanıyor.

- `loadItems()`: kaydı `JSON.parse` ile okuyup diziyi döndürsün; kayıt yoksa `[]` döndürsün.
- `addItem(name)`: adı `items` dizisine eklesin, diziyi `JSON.stringify` ile kaydetsin ve `render()` çağırsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<ul id="inv"></ul>
```

**Başlangıç kodu:**

```js
const inv = document.querySelector("#inv");

function loadItems() {
  // JSON.parse ile oku; kayıt yoksa []
  return [];
}

let items = loadItems();

function render() {
  inv.innerHTML = "";
  for (const item of items) {
    const li = document.createElement("li");
    li.textContent = item;
    inv.append(li);
  }
}

function addItem(name) {
  // diziye ekle, kaydet, çiz
}

render();
```

**İpuçları:**

1. JSON.parse(localStorage.getItem("inventory")) ?? []
2. localStorage.setItem("inventory", JSON.stringify(items));

<details><summary>Çözüm</summary>

```js
const inv = document.querySelector("#inv");

function loadItems() {
  // JSON.parse ile oku; kayıt yoksa []
  return JSON.parse(localStorage.getItem("inventory")) ?? [];
}

let items = loadItems();

function render() {
  inv.innerHTML = "";
  for (const item of items) {
    const li = document.createElement("li");
    li.textContent = item;
    inv.append(li);
  }
}

function addItem(name) {
  // diziye ekle, kaydet, çiz
  items.push(name);
  localStorage.setItem("inventory", JSON.stringify(items));
  render();
}

render();
```

</details>

## Challenge: Ayarları hatırla

Oyun ayarları bir nesne olarak `settings` anahtarında JSON ile saklanıyor. Varsayılanlar: `{ sound: true, volume: 5 }`.

- `loadSettings()`: kaydı okusun ve eksik alanları varsayılanlarla doldurarak döndürsün (`{ ...DEFAULTS, ...saved }`). Kayıt yoksa varsayılanlar gelsin.
- Sayfa açılınca `#sound` onay kutusu ve `#volume` listesi yüklenen ayarları göstersin.
- İkisinden biri değişince (`change`) ayar nesnesi güncellensin ve kaydedilsin. `volume` **sayı** olarak saklansın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<label><input type="checkbox" id="sound"> Ses açık</label> 
<label>Ses düzeyi <select id="volume"><option value="3">3</option><option value="5">5</option><option value="8">8</option></select></label>
```

**Başlangıç kodu:**

```js
const DEFAULTS = { sound: true, volume: 5 };
const soundBox = document.querySelector("#sound");
const volumeSelect = document.querySelector("#volume");

function loadSettings() {
  // kaydı oku, varsayılanlarla birleştir
}

// yükle, kutulara yerleştir, change olaylarında kaydet
```

**İpuçları:**

1. return { ...DEFAULTS, ...saved };
2. soundBox.checked = settings.sound; volumeSelect.value = String(settings.volume);
3. settings.volume = Number(volumeSelect.value);

<details><summary>Çözüm</summary>

```js
const DEFAULTS = { sound: true, volume: 5 };
const soundBox = document.querySelector("#sound");
const volumeSelect = document.querySelector("#volume");

function loadSettings() {
  // kaydı oku, varsayılanlarla birleştir
  const saved = JSON.parse(localStorage.getItem("settings")) ?? {};
  return { ...DEFAULTS, ...saved };
}

// yükle, kutulara yerleştir, change olaylarında kaydet
const settings = loadSettings();

function saveSettings() {
  localStorage.setItem("settings", JSON.stringify(settings));
}

soundBox.checked = settings.sound;
volumeSelect.value = String(settings.volume);

soundBox.addEventListener("change", () => {
  settings.sound = soundBox.checked;
  saveSettings();
});
volumeSelect.addEventListener("change", () => {
  settings.volume = Number(volumeSelect.value);
  saveSettings();
});
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **En yüksek skoru kaydetmek**

### Yıldız Avcısı: En yüksek skor

Oyunun rekoru sayfa kapansa da kalsın. İki fonksiyon yaz:

- `loadBest()`: `best` anahtarındaki skoru **sayı** olarak döndürsün (kayıt yoksa 0).
- `saveBest(score)`: skor rekordan büyükse kaydetsin, `#best`'i güncellesin, `#info`'ya `Yeni rekor: 50!` yazsın ve `true` döndürsün; değilse hiçbir şeyi değiştirmeden `false` döndürsün.

Sayfa açılınca rekor `#best`'te görünsün. (Önizleme 35 rekoruyla başlıyor.)

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
const bestEl = document.querySelector("#best");
const info = document.querySelector("#info");

function loadBest() {
  // kayıtlı rekoru sayı olarak döndür (yoksa 0)
  return 0;
}

function saveBest(score) {
  // rekor kırıldıysa kaydet ve true döndür, değilse false
}

// açılışta rekoru göster
```

**İpuçları:**

1. return Number(localStorage.getItem("best")) || 0;
2. if (score <= loadBest()) return false;
3. Açılışta: bestEl.textContent = loadBest();

<details><summary>Çözüm</summary>

```js
const bestEl = document.querySelector("#best");
const info = document.querySelector("#info");

function loadBest() {
  // kayıtlı rekoru sayı olarak döndür (yoksa 0)
  return Number(localStorage.getItem("best")) || 0;
}

function saveBest(score) {
  // rekor kırıldıysa kaydet ve true döndür, değilse false
  if (score <= loadBest()) return false;
  localStorage.setItem("best", String(score));
  bestEl.textContent = score;
  info.textContent = `Yeni rekor: ${score}!`;
  return true;
}

// açılışta rekoru göster
bestEl.textContent = loadBest();
```

</details>

### Kişisel Web Sitem: Temayı hatırla

Ziyaretçinin seçtiği tema bir dahaki gelişinde de dursun.

- `applySavedTheme()`: `theme` anahtarını okusun; `"dark"` ise `body`'ye `dark` sınıfını eklesin, değilse (kayıt yoksa da) kaldırsın. Sayfa açılınca çalışsın.
- `#theme-btn` tıklanınca `dark` sınıfı aç/kapansın ve yeni tema (`"dark"` ya da `"light"`) `theme` anahtarına kaydedilsin.

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
function applySavedTheme() {
  // kayıtlı temayı uygula (yoksa açık tema)
}

// tema düğmesi: değiştir ve kaydet

applySavedTheme();
```

**İpuçları:**

1. const saved = localStorage.getItem("theme") ?? "light";
2. document.body.classList.toggle("dark", saved === "dark");

<details><summary>Çözüm</summary>

```js
function applySavedTheme() {
  // kayıtlı temayı uygula (yoksa açık tema)
  const saved = localStorage.getItem("theme") ?? "light";
  document.body.classList.toggle("dark", saved === "dark");
}

// tema düğmesi: değiştir ve kaydet
document.querySelector("#theme-btn").addEventListener("click", () => {
  document.body.classList.toggle("dark");
  const theme = document.body.classList.contains("dark") ? "dark" : "light";
  localStorage.setItem("theme", theme);
});

applySavedTheme();
```

</details>

### Çalışma Asistanım: Görevleri kaydet

Görevler artık bir nesne dizisi: `{ text: "Fizik tekrarı", done: false }`. Liste `tasks` anahtarında JSON olarak saklansın. `render()` hazır.

- `loadTasks()`: kaydı `JSON.parse` ile okusun; kayıt yoksa `[]` döndürsün.
- `saveTasks()`: `tasks` dizisini `JSON.stringify` ile kaydetsin.
- `addTask(text)` içinde görevi ekledikten sonra kaydetmeyi unutma. (Göreve tıklayınca `render()` zaten `saveTasks()` çağırıyor.)

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
const list = document.querySelector("#task-list");

function loadTasks() {
  // JSON.parse ile oku; kayıt yoksa []
  return [];
}

function saveTasks() {
  // tasks dizisini JSON.stringify ile kaydet
}

let tasks = loadTasks();

function render() {
  list.innerHTML = "";
  tasks.forEach((task) => {
    const li = document.createElement("li");
    li.textContent = task.text;
    if (task.done) li.classList.add("done");
    li.addEventListener("click", () => {
      task.done = !task.done;
      saveTasks();
      render();
    });
    list.append(li);
  });
}

function addTask(text) {
  tasks.push({ text: text, done: false });
  // kaydet
  render();
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (text !== "") addTask(text);
  form.reset();
});

render();
```

**İpuçları:**

1. const saved = localStorage.getItem("tasks"); return saved ? JSON.parse(saved) : [];
2. localStorage.setItem("tasks", JSON.stringify(tasks));

<details><summary>Çözüm</summary>

```js
const form = document.querySelector("#task-form");
const input = document.querySelector("#task-input");
const list = document.querySelector("#task-list");

function loadTasks() {
  // JSON.parse ile oku; kayıt yoksa []
  const saved = localStorage.getItem("tasks");
  return saved ? JSON.parse(saved) : [];
}

function saveTasks() {
  // tasks dizisini JSON.stringify ile kaydet
  localStorage.setItem("tasks", JSON.stringify(tasks));
}

let tasks = loadTasks();

function render() {
  list.innerHTML = "";
  tasks.forEach((task) => {
    const li = document.createElement("li");
    li.textContent = task.text;
    if (task.done) li.classList.add("done");
    li.addEventListener("click", () => {
      task.done = !task.done;
      saveTasks();
      render();
    });
    list.append(li);
  });
}

function addTask(text) {
  tasks.push({ text: text, done: false });
  // kaydet
  saveTasks();
  render();
}

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const text = input.value.trim();
  if (text !== "") addTask(text);
  form.reset();
});

render();
```

</details>

### Bilgi Yarışması: Rekor tablosu

Yarışmanın rekoru, rekoru kıranın adıyla birlikte `quizRecord` anahtarında JSON olarak saklansın: `{"name":"Ada","score":40}`.

- `loadRecord()`: kaydı okuyup nesneyi döndürsün; kayıt yoksa `{ name: "-", score: 0 }`.
- `finishQuiz(name, score)`: skor rekordan büyükse `{ name, score }` nesnesini kaydetsin ve `#feedback`'e `Yeni rekor: 60!` yazsın; değilse `Rekor: 40 (Ada). Tekrar dene!` yazsın. Sonunda `showRecord()` çağrılıyor.

`showRecord()` hazır: rekoru `#best`'te `40 (Ada)` biçiminde gösterir.

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
const feedback = document.querySelector("#feedback");

function loadRecord() {
  // quizRecord kaydını JSON.parse ile oku; yoksa { name: "-", score: 0 }
  return { name: "-", score: 0 };
}

function showRecord() {
  const record = loadRecord();
  document.querySelector("#best").textContent = `${record.score} (${record.name})`;
}

function finishQuiz(name, score) {
  // rekor kırıldıysa kaydet ve "Yeni rekor: 60!", değilse "Rekor: 40 (Ada). Tekrar dene!"
  showRecord();
}

showRecord();
```

**İpuçları:**

1. const saved = localStorage.getItem("quizRecord"); return saved ? JSON.parse(saved) : { ... };
2. localStorage.setItem("quizRecord", JSON.stringify({ name: name, score: score }));

<details><summary>Çözüm</summary>

```js
const feedback = document.querySelector("#feedback");

function loadRecord() {
  // quizRecord kaydını JSON.parse ile oku; yoksa { name: "-", score: 0 }
  const saved = localStorage.getItem("quizRecord");
  return saved ? JSON.parse(saved) : { name: "-", score: 0 };
}

function showRecord() {
  const record = loadRecord();
  document.querySelector("#best").textContent = `${record.score} (${record.name})`;
}

function finishQuiz(name, score) {
  // rekor kırıldıysa kaydet ve "Yeni rekor: 60!", değilse "Rekor: 40 (Ada). Tekrar dene!"
  const record = loadRecord();
  if (score > record.score) {
    localStorage.setItem("quizRecord", JSON.stringify({ name: name, score: score }));
    feedback.textContent = `Yeni rekor: ${score}!`;
  } else {
    feedback.textContent = `Rekor: ${record.score} (${record.name}). Tekrar dene!`;
  }
  showRecord();
}

showRecord();
```

</details>
