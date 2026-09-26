# Gün 13: DOM'a giriş

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** DOM Gezegeni  ·  **Maskot:** Kodi

**Bugünün hedefi:** querySelector ile sayfadaki elemanları bulmak; metnini, sınıfını, stilini ve niteliklerini değiştirmek

> DOM Gezegeni'ne iniş yaptın! Buradaki her şey bir web sayfası: başlıklar, paragraflar, düğmeler. Bugün JavaScript ile sayfaya dokunmayı, yani **DOM**'u değiştirmeyi öğreneceksin.

![DOM Gezegeni](../../gorseller/javascript/bolgeler/dom.webp)

## Konu anlatımı

### DOM nedir?

Tarayıcı bir HTML sayfasını açınca onu okuyup bir **ağaca** dönüştürür: her etiket (`h1`, `p`, `button`...) bir **nesne** olur. Bu ağaca **DOM** (Document Object Model, Belge Nesne Modeli) denir. JavaScript bu nesnelere ulaşıp onları değiştirebilir; değiştirdiğin anda sayfa da değişir.

Ağacın kökü `document` nesnesidir. Sayfadaki her şeye oradan ulaşırız.

**Bugünden itibaren görevlerde bir sayfa var.** Sayfanın HTML'i görevle birlikte hazır gelir; sen yalnızca JavaScript yazarsın. Editörün yanındaki **önizleme** paneli sayfayı gösterir. Kodun sayfa yüklendikten sonra çalışır, yani bütün elemanlar hazırdır. `console.log` da çalışmaya devam eder; çıktısı yine Çıktı alanında görünür.

### querySelector ile eleman bulmak

`document.querySelector("seçici")` CSS seçicisine uyan **ilk** elemanı verir:

```js
const title = document.querySelector("#title");    // id="title" olan
const note = document.querySelector(".note");      // class="note" olan ilk eleman
const firstItem = document.querySelector("ul li"); // ul içindeki ilk li
```

Uyan **hepsini** almak için `querySelectorAll` kullanılır. Bir liste döner; `for...of` ya da `forEach` ile gezebilirsin:

```js
const planets = document.querySelectorAll(".planet");
console.log(planets.length);
for (const p of planets) {
  console.log(p.textContent);
}
```

Seçiciye uyan eleman yoksa `querySelector` `null` döndürür. `Cannot set properties of null` hatası görürsen seçiciyi kontrol et: id için `#`, sınıf için `.` koydun mu?

### textContent ve innerHTML

`textContent` bir elemanın içindeki **metni** okur ya da değiştirir:

```js
const status = document.querySelector("#status");
console.log(status.textContent);    // eski metin
status.textContent = "İniş tamam!"; // yeni metin
```

`innerHTML` ise verdiğin metni **HTML olarak** yorumlar: `box.innerHTML = "<b>Kalın</b>"` gerçekten kalın yazı üretir.

**Güvenlik notu:** Kullanıcının yazdığı bir metni asla `innerHTML` ile sayfaya koyma; biri metnin içine zararlı HTML ya da kod gizleyebilir. Metin göstermek için `textContent` kullan. Bu kursta da hep onu tercih edeceğiz.

### classList, style ve nitelikler

Görünümü değiştirmenin en temiz yolu **sınıf** (class) eklemek ya da çıkarmaktır; sınıfın nasıl görüneceğini CSS söyler:

```js
const panel = document.querySelector("#panel");
panel.classList.add("active");      // ekle
panel.classList.remove("hidden");   // çıkar
panel.classList.toggle("dark");     // varsa çıkar, yoksa ekle
panel.classList.contains("active"); // true
```

Tek bir stili doğrudan da verebilirsin. CSS'teki tireli adlar burada camelCase olur (`background-color` → `backgroundColor`):

```js
panel.style.color = "#d63384";
panel.style.backgroundColor = "#0b1026";
```

`href`, `src`, `disabled`, `data-...` gibi HTML **nitelikleri** (attribute) için:

```js
const link = document.querySelector("#docs");
link.getAttribute("href");                                // oku
link.setAttribute("href", "https://developer.mozilla.org"); // değiştir
const btn = document.querySelector("#launch");
btn.removeAttribute("disabled");                          // kaldır
```

## Örnekler

### Başlığı değiştir

Sayfa:

```html
<h1 id="title">Merhaba</h1>
<p class="note">Bu metin JavaScript ile değişecek.</p>
```

```js
const title = document.querySelector("#title");
title.textContent = "Merhaba, DOM Gezegeni!";
title.style.color = "#d63384";

const note = document.querySelector(".note");
note.textContent = "Bu satırı JavaScript yazdı.";
note.classList.add("big");

console.log("Başlık:", title.textContent);
```

*Kodu değiştirip Çalıştır'a bas; önizleme her çalıştırmada sayfayı baştan kurar.*

### Hepsini işaretle

Sayfa:

```html
<ul>
  <li class="planet">Merkür</li>
  <li class="planet">Venüs</li>
  <li class="planet">Mars</li>
</ul>
<a id="link" href="#">Belgeler</a>
```

```js
const planets = document.querySelectorAll(".planet");
console.log("Gezegen sayısı:", planets.length);

for (const p of planets) {
  p.classList.add("visited");
  p.textContent = p.textContent + " (ziyaret edildi)";
}

const link = document.querySelector("#link");
link.setAttribute("href", "https://developer.mozilla.org");
console.log("Bağlantı:", link.getAttribute("href"));
```

*querySelectorAll bir liste verir; for...of ile her elemana tek tek dokunuruz.*

## Görevler

### Görev 1: İlk dokunuş

Sayfadaki başlığın (`#title`) metnini `DOM Gezegeni`, durum paragrafının (`#status`) metnini `İniş tamam!` yap. `textContent` kullan.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1 id="title">Görev Merkezi</h1>
<p id="status">Bekleniyor...</p>
<div id="panel" class="box hidden">Gizli panel: rota hazır.</div>
<ul id="planets">
  <li class="planet">Merkür</li>
  <li class="planet">Venüs</li>
  <li class="planet">Mars</li>
  <li class="planet">Jüpiter</li>
</ul>
<p><a id="docs" href="#">Belgeler</a> <button id="launch" data-fuel="80" disabled>Kalkış</button></p>
```

**CSS:**

```css
.hidden{display:none}.box{padding:8px;border:2px dashed #7a86b8;border-radius:8px}.active{color:#1a7f37;font-weight:bold}.visited{color:#7a86b8;text-decoration:line-through}
```

**Başlangıç kodu:**

```js
const title = document.querySelector("#title");

// title'ın ve #status'un metnini değiştir
```

**İpuçları:**

1. title.textContent = "DOM Gezegeni";
2. #status için de document.querySelector("#status") kullan.

<details><summary>Çözüm</summary>

```js
const title = document.querySelector("#title");

// title'ın ve #status'un metnini değiştir
title.textContent = "DOM Gezegeni";
document.querySelector("#status").textContent = "İniş tamam!";
```

</details>

### Görev 2: Sınıf ve stil

Paneli hazırla:

1. `#status`'a `active` sınıfını ekle.
2. `#panel`'den `hidden` sınıfını kaldır (panel görünsün).
3. `#title`'ın yazı rengini `style` ile `#d63384` yap.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1 id="title">Görev Merkezi</h1>
<p id="status">Bekleniyor...</p>
<div id="panel" class="box hidden">Gizli panel: rota hazır.</div>
<ul id="planets">
  <li class="planet">Merkür</li>
  <li class="planet">Venüs</li>
  <li class="planet">Mars</li>
  <li class="planet">Jüpiter</li>
</ul>
<p><a id="docs" href="#">Belgeler</a> <button id="launch" data-fuel="80" disabled>Kalkış</button></p>
```

**CSS:**

```css
.hidden{display:none}.box{padding:8px;border:2px dashed #7a86b8;border-radius:8px}.active{color:#1a7f37;font-weight:bold}.visited{color:#7a86b8;text-decoration:line-through}
```

**Başlangıç kodu:**

```js
const status = document.querySelector("#status");
const panel = document.querySelector("#panel");
const title = document.querySelector("#title");

// sınıf ekle, sınıf kaldır, rengi değiştir
```

**İpuçları:**

1. status.classList.add("active");
2. panel.classList.remove("hidden");
3. title.style.color = "#d63384";

<details><summary>Çözüm</summary>

```js
const status = document.querySelector("#status");
const panel = document.querySelector("#panel");
const title = document.querySelector("#title");

// sınıf ekle, sınıf kaldır, rengi değiştir
status.classList.add("active");
panel.classList.remove("hidden");
title.style.color = "#d63384";
```

</details>

### Görev 3: Bütün gezegenler

`querySelectorAll` ile bütün `.planet` elemanlarını al ve bir döngüyle her birine `visited` sınıfını ekle.

Sonra `#status`'a kaç gezegen olduğunu yaz: `4 gezegen ziyaret edildi`. Sayıyı elle yazma; listenin `length`'ini kullan.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1 id="title">Görev Merkezi</h1>
<p id="status">Bekleniyor...</p>
<div id="panel" class="box hidden">Gizli panel: rota hazır.</div>
<ul id="planets">
  <li class="planet">Merkür</li>
  <li class="planet">Venüs</li>
  <li class="planet">Mars</li>
  <li class="planet">Jüpiter</li>
</ul>
<p><a id="docs" href="#">Belgeler</a> <button id="launch" data-fuel="80" disabled>Kalkış</button></p>
```

**CSS:**

```css
.hidden{display:none}.box{padding:8px;border:2px dashed #7a86b8;border-radius:8px}.active{color:#1a7f37;font-weight:bold}.visited{color:#7a86b8;text-decoration:line-through}
```

**Başlangıç kodu:**

```js
const planets = document.querySelectorAll(".planet");

// her gezegene visited ekle

// #status'a gezegen sayısını yaz
```

**İpuçları:**

1. for (const p of planets) { p.classList.add("visited"); }
2. planets.length gezegen sayısını verir.
3. `${planets.length} gezegen ziyaret edildi`

<details><summary>Çözüm</summary>

```js
const planets = document.querySelectorAll(".planet");

// her gezegene visited ekle
for (const p of planets) {
  p.classList.add("visited");
}

// #status'a gezegen sayısını yaz
document.querySelector("#status").textContent = `${planets.length} gezegen ziyaret edildi`;
```

</details>

## Challenge: Kalkış izni

Kalkış düğmesinin (`#launch`) yakıt bilgisi `data-fuel` niteliğinde. `updateLaunch()` fonksiyonunu yaz:

- `getAttribute` ile `data-fuel`'i oku ve sayıya çevir.
- Yakıt 50 ya da fazlaysa: düğmenin `disabled` niteliğini kaldır, `#status`'a `Kalkışa hazır (yakıt 80)` yaz.
- Azsa: düğmeye `disabled` niteliğini koy (`setAttribute("disabled", "")`), `#status`'a `Yakıt yetersiz (yakıt 30)` yaz.

Ayrıca `#docs` bağlantısının `href` niteliğini `https://developer.mozilla.org` yap.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1 id="title">Görev Merkezi</h1>
<p id="status">Bekleniyor...</p>
<div id="panel" class="box hidden">Gizli panel: rota hazır.</div>
<ul id="planets">
  <li class="planet">Merkür</li>
  <li class="planet">Venüs</li>
  <li class="planet">Mars</li>
  <li class="planet">Jüpiter</li>
</ul>
<p><a id="docs" href="#">Belgeler</a> <button id="launch" data-fuel="80" disabled>Kalkış</button></p>
```

**CSS:**

```css
.hidden{display:none}.box{padding:8px;border:2px dashed #7a86b8;border-radius:8px}.active{color:#1a7f37;font-weight:bold}.visited{color:#7a86b8;text-decoration:line-through}
```

**Başlangıç kodu:**

```js
const launch = document.querySelector("#launch");
const status = document.querySelector("#status");

function updateLaunch() {
  // data-fuel'i oku, sayıya çevir, düğmeyi ve #status'u güncelle
}

updateLaunch();

// #docs bağlantısının href niteliğini değiştir
```

**İpuçları:**

1. const fuel = Number(launch.getAttribute("data-fuel"));
2. launch.removeAttribute("disabled");
3. Metinde yakıtı değişkenden yaz: `Kalkışa hazır (yakıt ${fuel})`

<details><summary>Çözüm</summary>

```js
const launch = document.querySelector("#launch");
const status = document.querySelector("#status");

function updateLaunch() {
  // data-fuel'i oku, sayıya çevir, düğmeyi ve #status'u güncelle
  const fuel = Number(launch.getAttribute("data-fuel"));
  if (fuel >= 50) {
    launch.removeAttribute("disabled");
    status.textContent = `Kalkışa hazır (yakıt ${fuel})`;
  } else {
    launch.setAttribute("disabled", "");
    status.textContent = `Yakıt yetersiz (yakıt ${fuel})`;
  }
}

updateLaunch();

// #docs bağlantısının href niteliğini değiştir
document.querySelector("#docs").setAttribute("href", "https://developer.mozilla.org");
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Başlangıç ekranı**

### Yıldız Avcısı: Başlangıç ekranı

Oyunun başlangıç ekranını doldur. `showStart(g)` fonksiyonunu yaz:

- `g.title`'ı `#game-title`'a, `g.pilot`'u `#pilot`'a, `g.level`'ı `#level`'a yazsın (`textContent`).
- Başla düğmesine (`#start-btn`) `ready` sınıfını eklesin.

Metinleri elle yazma; hep `g` nesnesinden al.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<div id="start-screen" class="screen">
  <h1 id="game-title">Oyun</h1>
  <p>Pilot: <span id="pilot">?</span></p>
  <p>Seviye: <span id="level">?</span></p>
  <button id="start-btn">Başla</button>
</div>
<div id="game-panel" class="screen hidden">
  <p id="hud">Skor: 0</p>
  <h2>Envanter</h2>
  <ul id="inventory"></ul>
</div>
```

**CSS:**

```css
html,body{background:#0b1026;color:#e8ecff}.screen{padding:12px;border:1px solid #2c3566;border-radius:10px}.hidden{display:none}#game-title{color:#f7df1e;margin-top:0}#start-btn{padding:6px 14px;border-radius:6px;border:1px solid #7a86b8}.ready{background:#f7df1e;color:#0b1026;font-weight:bold}.item{margin:4px 0}
```

**Başlangıç kodu:**

```js
const game = { title: "Yıldız Avcısı", pilot: "Ada", level: 1 };

function showStart(g) {
  // elemanları bul ve g'deki bilgilerle doldur
}

showStart(game);
```

**İpuçları:**

1. document.querySelector("#game-title").textContent = g.title;
2. #pilot ve #level için de aynısını yap.
3. classList.add("ready")

<details><summary>Çözüm</summary>

```js
const game = { title: "Yıldız Avcısı", pilot: "Ada", level: 1 };

function showStart(g) {
  // elemanları bul ve g'deki bilgilerle doldur
  document.querySelector("#game-title").textContent = g.title;
  document.querySelector("#pilot").textContent = g.pilot;
  document.querySelector("#level").textContent = g.level;
  document.querySelector("#start-btn").classList.add("ready");
}

showStart(game);
```

</details>

### Kişisel Web Sitem: Sitenin başlığı

Sitenin başlık bölümünü doldur. `fillHeader(profile)` fonksiyonunu yaz:

- `profile.name`'i `#site-name`'e, `profile.tagline`'ı `#tagline`'a yazsın.
- `#site-header`'a `filled` sınıfını eklesin (alt çizgisi sarı olur).

Sonra kendi bilgilerinle çağır.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<header id="site-header">
  <h1 id="site-name">Adın</h1>
  <p id="tagline">Kısa bir cümle</p>
  <button id="theme-btn">Koyu tema</button>
</header>
<main>
  <h2>Projelerim</h2>
  <div id="projects"></div>
</main>
```

**CSS:**

```css
html:has(body.dark){background:#0b1026}body.dark{background:#0b1026;color:#e8ecff}#site-header{padding:10px 0;border-bottom:3px solid #c9cfe8}#site-header.filled{border-bottom-color:#f7df1e}#site-name{margin:0}.card{border:1px solid #c9cfe8;border-radius:8px;padding:6px 10px;margin:6px 0}.card h3{margin:0}.tag{margin:2px 0 0;font-size:13px;color:#7a86b8}
```

**Başlangıç kodu:**

```js
const me = { name: "Deniz Yıldız", tagline: "Kod yazan, oyun tasarlayan bir kaşif" };

function fillHeader(profile) {
  // #site-name, #tagline ve #site-header
}

fillHeader(me);
```

**İpuçları:**

1. document.querySelector("#site-name").textContent = profile.name;
2. classList.add("filled")

<details><summary>Çözüm</summary>

```js
const me = { name: "Deniz Yıldız", tagline: "Kod yazan, oyun tasarlayan bir kaşif" };

function fillHeader(profile) {
  // #site-name, #tagline ve #site-header
  document.querySelector("#site-name").textContent = profile.name;
  document.querySelector("#tagline").textContent = profile.tagline;
  document.querySelector("#site-header").classList.add("filled");
}

fillHeader(me);
```

</details>

### Çalışma Asistanım: Günün özeti

Görev listesi sayfada hazır. `updateSummary()` fonksiyonunu yaz: sayfadaki görevleri say ve `#summary`'ye `1/4 görev tamamlandı` biçiminde yaz.

- Bütün görevler: `.task` elemanları
- Tamamlananlar: hem `task` hem `done` sınıfı olanlar (seçici: `.task.done`)

Sayıları elle yazma; `querySelectorAll(...).length` ile say.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1>Çalışma Asistanım</h1>
<p id="summary">...</p>
<ul id="task-list">
  <li class="task done"><span class="name">Matematik ödevi</span> <button class="done-btn">Geri al</button></li>
  <li class="task"><span class="name">Fizik tekrarı</span> <button class="done-btn">Tamamla</button></li>
  <li class="task"><span class="name">İngilizce kelimeler</span> <button class="done-btn">Tamamla</button></li>
  <li class="task"><span class="name">Kitap okuma</span> <button class="done-btn">Tamamla</button></li>
</ul>
<p><input id="new-task" placeholder="Yeni görev"> <button id="add-btn">Ekle</button></p>
```

**CSS:**

```css
#summary{font-weight:bold}.task{margin:4px 0}.done .name{text-decoration:line-through;color:#7a86b8}.done-btn{font-size:13px;margin-left:6px}
```

**Başlangıç kodu:**

```js
function updateSummary() {
  // görevleri say, #summary'ye yaz
}

updateSummary();
```

**İpuçları:**

1. document.querySelectorAll(".task").length
2. Tamamlananlar: document.querySelectorAll(".task.done").length
3. `${done}/${all} görev tamamlandı`

<details><summary>Çözüm</summary>

```js
function updateSummary() {
  // görevleri say, #summary'ye yaz
  const all = document.querySelectorAll(".task").length;
  const done = document.querySelectorAll(".task.done").length;
  document.querySelector("#summary").textContent = `${done}/${all} görev tamamlandı`;
}

updateSummary();
```

</details>

### Bilgi Yarışması: Soruyu göster

Soru artık sayfada görünecek. `showQuestion(q)` fonksiyonunu yaz:

- `q.text`'i `#question`'a yazsın.
- `querySelectorAll(".option")` ile üç düğmeyi alsın ve her düğmeye sırasıyla `q.options` dizisindeki seçeneği yazsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1>Bilgi Yarışması</h1>
<p id="question">Soru yükleniyor...</p>
<div id="options">
  <button class="option">?</button>
  <button class="option">?</button>
  <button class="option">?</button>
</div>
<p id="feedback"></p>
<p id="score">Puan: 0</p>
```

**CSS:**

```css
#question{font-size:18px;font-weight:bold}.option{display:block;margin:6px 0;padding:6px 12px;min-width:180px;text-align:left}#feedback{font-weight:bold}
```

**Başlangıç kodu:**

```js
const question = { text: "Kızıl gezegen hangisi?", options: ["Mars", "Venüs", "Merkür"], answer: 0 };

function showQuestion(q) {
  // #question ve .option düğmeleri
}

showQuestion(question);
```

**İpuçları:**

1. document.querySelector("#question").textContent = q.text;
2. buttons.forEach((btn, i) => { btn.textContent = q.options[i]; });

<details><summary>Çözüm</summary>

```js
const question = { text: "Kızıl gezegen hangisi?", options: ["Mars", "Venüs", "Merkür"], answer: 0 };

function showQuestion(q) {
  // #question ve .option düğmeleri
  document.querySelector("#question").textContent = q.text;
  const buttons = document.querySelectorAll(".option");
  buttons.forEach((btn, i) => {
    btn.textContent = q.options[i];
  });
}

showQuestion(question);
```

</details>
