# Gün 14: Olaylar

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** DOM Gezegeni  ·  **Maskot:** Kodi

**Bugünün hedefi:** addEventListener ile tıklama ve yazma olaylarını dinlemek, e.target ve olay yetkilendirmeyi kullanmak

> DOM Gezegeni'nde her şey sana tepki vermeyi bekliyor. Bir düğmeye basılması, bir kutuya harf yazılması: bunların hepsi birer **olay**. Bugün sayfanı olaylara kulak veren canlı bir kontrol paneline çeviriyorsun.

![DOM Gezegeni](../../gorseller/javascript/bolgeler/dom.webp)

## Konu anlatımı

### addEventListener: olayı dinle

Tıklama, tuşa basma, bir kutuya yazma... Sayfada olan her şey bir **olaydır** (event). `addEventListener` bir elemana "bu olay olunca şu fonksiyonu çalıştır" der:

```js
const btn = document.querySelector("#start");
btn.addEventListener("click", () => {
  console.log("Tıklandı!");
});
```

Fonksiyon hemen çalışmaz; olay **her olduğunda** çalışır. Kodu çalıştırdıktan sonra önizlemedeki düğmeye kendin tıklayıp dene.

Dikkat: adı olan bir fonksiyon verirken parantez koyma. `btn.addEventListener("click", launch)` doğru; `launch()` yazarsan fonksiyon hemen bir kez çalışır ve tıklamayı dinlemez.

### Olay nesnesi ve e.target

Dinleyici fonksiyona tarayıcı bir **olay nesnesi** verir; genelde `e` diye adlandırılır. En çok kullanılan özelliği `e.target`: olayın olduğu eleman.

```js
const buttons = document.querySelectorAll(".planet-btn");
for (const b of buttons) {
  b.addEventListener("click", (e) => {
    console.log("Seçilen:", e.target.textContent);
  });
}
```

`e.type` olayın adını (`"click"`) verir. Aynı fonksiyonu birçok düğmeye bağlayıp hangisine tıklandığını `e.target` ile anlayabilirsin.

### input olayı ve durum

Bir `<input>` kutusuna her harf yazıldığında `input` olayı olur. Kutudaki metin `value` özelliğindedir:

```js
const nameBox = document.querySelector("#name");
nameBox.addEventListener("input", () => {
  document.querySelector("#hello").textContent = "Merhaba, " + nameBox.value;
});
```

Etkileşimli sayfalarda veriyi bir değişkende tutarız; buna **durum** (state) denir. Olay durumu değiştirir, sonra ekranı durumdan güncelleriz:

```js
let lives = 3;
hitBtn.addEventListener("click", () => {
  lives--;                                  // 1) durumu değiştir
  livesText.textContent = "Can: " + lives; // 2) ekranı güncelle
});
```

### Dinleyiciyi kaldırmak ve olay yetkilendirme

Bir dinleyiciyi kaldırmak için `removeEventListener` aynı olay adı ve **aynı fonksiyonla** çağrılır; bu yüzden fonksiyona bir ad veririz:

```js
function onLaunch() {
  console.log("Kalkış!");
  btn.removeEventListener("click", onLaunch); // bir daha çalışmaz
}
btn.addEventListener("click", onLaunch);
```

Kısa yolu: `btn.addEventListener("click", onLaunch, { once: true })`.

**Olay yetkilendirme** (event delegation): tıklama olayı tıklanan elemandan başlayıp onu kapsayan elemanlara doğru **kabarcık gibi yükselir**. Bu yüzden her düğmeye ayrı dinleyici eklemek yerine, onları kapsayan elemana **tek** dinleyici ekleyebilirsin:

```js
const menu = document.querySelector("#menu");
menu.addEventListener("click", (e) => {
  if (e.target.tagName !== "BUTTON") return; // düğme değilse boş ver
  console.log("Rota:", e.target.textContent);
});
```

Güzel yanı: menüye **sonradan eklenen** düğmeler de çalışır. Yarın elemanları kodla oluştururken çok işine yarayacak.

## Örnekler

### Sayaç düğmesi

Sayfa:

```html
<button id="btn">Tıkla</button>
<p id="info">0 tıklama</p>
```

```js
let count = 0;
const btn = document.querySelector("#btn");

btn.addEventListener("click", (e) => {
  count++;
  document.querySelector("#info").textContent = `${count} tıklama`;
  console.log("Tıklanan:", e.target.textContent);
});
```

*Çalıştır'a bastıktan sonra önizlemedeki düğmeye birkaç kez tıkla.*

### Canlı önizleme ve renkler

Sayfa:

```html
<input id="name" placeholder="Adını yaz">
<p id="hello">Merhaba!</p>
<div id="colors"><button>kırmızı</button> <button>mavi</button> <button>yeşil</button></div>
```

```js
const input = document.querySelector("#name");
const hello = document.querySelector("#hello");

input.addEventListener("input", () => {
  hello.textContent = "Merhaba, " + input.value + "!";
});

const colors = { "kırmızı": "#d1242f", "mavi": "#1f6feb", "yeşil": "#1a7f37" };
document.querySelector("#colors").addEventListener("click", (e) => {
  if (e.target.tagName !== "BUTTON") return;
  hello.style.color = colors[e.target.textContent];
});
```

*Kutuya yaz, sonra renk düğmelerine tıkla. Renk düğmelerinin hepsini tek dinleyici yönetiyor.*

## Görevler

### Görev 1: Hız kontrolü

`speed` durumunu düğmelerle yönet:

- `#boost` (Hızlan) tıklanınca `speed` 10 artsın.
- `#brake` (Yavaşla) tıklanınca 10 azalsın ama **0'ın altına inmesin**.
- Her tıklamadan sonra `#speed` yeni hızı göstersin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1 id="title">Kontrol Paneli</h1>
<p id="info">Hazır.</p>
<p>Hız: <span id="speed">0</span></p>
<p><button id="boost">Hızlan</button> <button id="brake">Yavaşla</button> <button id="launch">Kalkış</button></p>
<p><input id="call-sign" placeholder="Çağrı adın"></p>
<p id="preview"></p>
<ul id="menu">
  <li><button>Mars</button></li>
  <li><button>Venüs</button></li>
  <li><button>Jüpiter</button></li>
</ul>
```

**CSS:**

```css
#menu{list-style:none;padding:0;display:flex;gap:6px}.selected{background:#f7df1e;font-weight:bold}#info{font-weight:bold}
```

**Başlangıç kodu:**

```js
let speed = 0;
const speedText = document.querySelector("#speed");

// #boost ve #brake düğmelerini dinle
```

**İpuçları:**

1. document.querySelector("#boost").addEventListener("click", () => { ... })
2. 0'ın altına inmemek için: if (speed > 0) speed -= 10;
3. Sonra speedText.textContent = speed;

<details><summary>Çözüm</summary>

```js
let speed = 0;
const speedText = document.querySelector("#speed");

// #boost ve #brake düğmelerini dinle
document.querySelector("#boost").addEventListener("click", () => {
  speed += 10;
  speedText.textContent = speed;
});

document.querySelector("#brake").addEventListener("click", () => {
  speed = Math.max(0, speed - 10);
  speedText.textContent = speed;
});
```

</details>

### Görev 2: Çağrı adı

`#call-sign` kutusuna her yazıldığında (`input` olayı) `#preview` paragrafı çağrı adını **büyük harflerle** göstersin:

`kartal` yazılınca → `Çağrı adı: KARTAL`

İpucu: metni büyük harfe çeviren `toUpperCase()` metodunu 3. günden hatırla.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1 id="title">Kontrol Paneli</h1>
<p id="info">Hazır.</p>
<p>Hız: <span id="speed">0</span></p>
<p><button id="boost">Hızlan</button> <button id="brake">Yavaşla</button> <button id="launch">Kalkış</button></p>
<p><input id="call-sign" placeholder="Çağrı adın"></p>
<p id="preview"></p>
<ul id="menu">
  <li><button>Mars</button></li>
  <li><button>Venüs</button></li>
  <li><button>Jüpiter</button></li>
</ul>
```

**CSS:**

```css
#menu{list-style:none;padding:0;display:flex;gap:6px}.selected{background:#f7df1e;font-weight:bold}#info{font-weight:bold}
```

**Başlangıç kodu:**

```js
const callSign = document.querySelector("#call-sign");
const preview = document.querySelector("#preview");

// input olayını dinle
```

**İpuçları:**

1. callSign.addEventListener("input", () => { ... })
2. Kutudaki metin: callSign.value
3. callSign.value.toUpperCase()

<details><summary>Çözüm</summary>

```js
const callSign = document.querySelector("#call-sign");
const preview = document.querySelector("#preview");

// input olayını dinle
callSign.addEventListener("input", () => {
  preview.textContent = "Çağrı adı: " + callSign.value.toUpperCase();
});
```

</details>

### Görev 3: Tek seferlik kalkış

Kalkış yalnızca **bir kez** yapılabilir. `onLaunch` fonksiyonunu tamamla:

- `launches` 1 artsın ve `#info`'ya `Kalkış! Motorlar çalıştı.` yazsın.
- Sonra `removeEventListener` ile kendini kaldırsın; ikinci tıklama hiçbir şey yapmasın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1 id="title">Kontrol Paneli</h1>
<p id="info">Hazır.</p>
<p>Hız: <span id="speed">0</span></p>
<p><button id="boost">Hızlan</button> <button id="brake">Yavaşla</button> <button id="launch">Kalkış</button></p>
<p><input id="call-sign" placeholder="Çağrı adın"></p>
<p id="preview"></p>
<ul id="menu">
  <li><button>Mars</button></li>
  <li><button>Venüs</button></li>
  <li><button>Jüpiter</button></li>
</ul>
```

**CSS:**

```css
#menu{list-style:none;padding:0;display:flex;gap:6px}.selected{background:#f7df1e;font-weight:bold}#info{font-weight:bold}
```

**Başlangıç kodu:**

```js
let launches = 0;
const launchBtn = document.querySelector("#launch");

function onLaunch() {
  // launches'ı artır, #info'ya yaz, dinleyiciyi kaldır
}

launchBtn.addEventListener("click", onLaunch);
```

**İpuçları:**

1. launches++;
2. launchBtn.removeEventListener("click", onLaunch);

<details><summary>Çözüm</summary>

```js
let launches = 0;
const launchBtn = document.querySelector("#launch");

function onLaunch() {
  // launches'ı artır, #info'ya yaz, dinleyiciyi kaldır
  launches++;
  document.querySelector("#info").textContent = "Kalkış! Motorlar çalıştı.";
  launchBtn.removeEventListener("click", onLaunch);
}

launchBtn.addEventListener("click", onLaunch);
```

</details>

## Challenge: Tek dinleyici

Rota menüsü (`#menu`) için **olay yetkilendirme** kullan: düğmelere değil, `#menu`'ye **tek** bir `click` dinleyicisi ekle.

- Tıklanan bir düğmeyse `#info`'ya `Rota: Mars` biçiminde yaz (düğmenin metninden).
- Tıklanan düğmeye `selected` sınıfını ekle, menüdeki diğer düğmelerden kaldır.
- Düğme dışında bir yere tıklanırsa hiçbir şey yapma.

Kontrol, menüye sonradan yeni bir düğme ekleyip ona da tıklayacak!

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1 id="title">Kontrol Paneli</h1>
<p id="info">Hazır.</p>
<p>Hız: <span id="speed">0</span></p>
<p><button id="boost">Hızlan</button> <button id="brake">Yavaşla</button> <button id="launch">Kalkış</button></p>
<p><input id="call-sign" placeholder="Çağrı adın"></p>
<p id="preview"></p>
<ul id="menu">
  <li><button>Mars</button></li>
  <li><button>Venüs</button></li>
  <li><button>Jüpiter</button></li>
</ul>
```

**CSS:**

```css
#menu{list-style:none;padding:0;display:flex;gap:6px}.selected{background:#f7df1e;font-weight:bold}#info{font-weight:bold}
```

**Başlangıç kodu:**

```js
const menu = document.querySelector("#menu");

// menu'ye TEK bir click dinleyicisi ekle; e.target ile tıklanan düğmeyi bul
```

**İpuçları:**

1. menu.addEventListener("click", (e) => { ... })
2. if (e.target.tagName !== "BUTTON") return;
3. Önce bütün düğmelerden selected'ı kaldır, sonra e.target'a ekle.

<details><summary>Çözüm</summary>

```js
const menu = document.querySelector("#menu");

// menu'ye TEK bir click dinleyicisi ekle; e.target ile tıklanan düğmeyi bul
menu.addEventListener("click", (e) => {
  if (e.target.tagName !== "BUTTON") return;
  for (const b of menu.querySelectorAll("button")) {
    b.classList.remove("selected");
  }
  e.target.classList.add("selected");
  document.querySelector("#info").textContent = `Rota: ${e.target.textContent}`;
});
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Başla düğmesi**

### Yıldız Avcısı: Başla düğmesi

Başla düğmesi (`#start-btn`) artık çalışsın. Tıklanınca:

- `#start-screen`'e `hidden` sınıfı eklensin (başlangıç ekranı kaybolsun),
- `#game-panel`'den `hidden` sınıfı kaldırılsın (oyun paneli görünsün),
- `#hud`'a `Skor: 0 | Pilot: Ada` yazılsın (pilot adı `game.pilot`'tan gelsin).

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
  document.querySelector("#game-title").textContent = g.title;
  document.querySelector("#pilot").textContent = g.pilot;
  document.querySelector("#level").textContent = g.level;
  document.querySelector("#start-btn").classList.add("ready");
}
showStart(game);

// Başla düğmesine tıklanınca ekranları değiştir
```

**İpuçları:**

1. document.querySelector("#start-btn").addEventListener("click", () => { ... })
2. classList.add("hidden") ve classList.remove("hidden")
3. `Skor: 0 | Pilot: ${game.pilot}`

<details><summary>Çözüm</summary>

```js
const game = { title: "Yıldız Avcısı", pilot: "Ada", level: 1 };

function showStart(g) {
  document.querySelector("#game-title").textContent = g.title;
  document.querySelector("#pilot").textContent = g.pilot;
  document.querySelector("#level").textContent = g.level;
  document.querySelector("#start-btn").classList.add("ready");
}
showStart(game);

// Başla düğmesine tıklanınca ekranları değiştir
document.querySelector("#start-btn").addEventListener("click", () => {
  document.querySelector("#start-screen").classList.add("hidden");
  document.querySelector("#game-panel").classList.remove("hidden");
  document.querySelector("#hud").textContent = `Skor: 0 | Pilot: ${game.pilot}`;
});
```

</details>

### Kişisel Web Sitem: Tema düğmesi

Siteye koyu tema ekle. `#theme-btn` tıklanınca:

- `body`'deki `dark` sınıfı `toggle` ile açılıp kapansın,
- Düğmenin yazısı koyu temadayken `Açık tema`, açık temadayken `Koyu tema` olsun.

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
document.querySelector("#site-name").textContent = "Deniz Yıldız";
document.querySelector("#tagline").textContent = "Kod yazan, oyun tasarlayan bir kaşif";

const themeBtn = document.querySelector("#theme-btn");

// tıklanınca body'de dark sınıfını aç/kapat, düğme yazısını güncelle
```

**İpuçları:**

1. body elemanına document.body ile ulaşılır.
2. document.body.classList.toggle("dark");
3. classList.contains("dark") ? "Açık tema" : "Koyu tema"

<details><summary>Çözüm</summary>

```js
document.querySelector("#site-name").textContent = "Deniz Yıldız";
document.querySelector("#tagline").textContent = "Kod yazan, oyun tasarlayan bir kaşif";

const themeBtn = document.querySelector("#theme-btn");

// tıklanınca body'de dark sınıfını aç/kapat, düğme yazısını güncelle
themeBtn.addEventListener("click", () => {
  document.body.classList.toggle("dark");
  const isDark = document.body.classList.contains("dark");
  themeBtn.textContent = isDark ? "Açık tema" : "Koyu tema";
});
```

</details>

### Çalışma Asistanım: Tamamla düğmeleri

Her görevin yanındaki `.done-btn` düğmesi çalışsın. Bir döngüyle her düğmeye `click` dinleyicisi ekle. Tıklanınca:

- Düğmenin içinde olduğu `<li>`'de (`btn.parentElement`) `done` sınıfı `toggle` ile açılıp kapansın,
- Düğme yazısı görev tamamlandıysa `Geri al`, değilse `Tamamla` olsun,
- `updateSummary()` çağrılsın.

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
  const all = document.querySelectorAll(".task").length;
  const done = document.querySelectorAll(".task.done").length;
  document.querySelector("#summary").textContent = `${done}/${all} görev tamamlandı`;
}
updateSummary();

// her .done-btn düğmesine click dinleyicisi ekle
```

**İpuçları:**

1. for (const btn of document.querySelectorAll(".done-btn")) { ... }
2. const li = btn.parentElement; li.classList.toggle("done");
3. Sonunda updateSummary(); çağır.

<details><summary>Çözüm</summary>

```js
function updateSummary() {
  const all = document.querySelectorAll(".task").length;
  const done = document.querySelectorAll(".task.done").length;
  document.querySelector("#summary").textContent = `${done}/${all} görev tamamlandı`;
}
updateSummary();

// her .done-btn düğmesine click dinleyicisi ekle
for (const btn of document.querySelectorAll(".done-btn")) {
  btn.addEventListener("click", () => {
    const li = btn.parentElement;
    li.classList.toggle("done");
    btn.textContent = li.classList.contains("done") ? "Geri al" : "Tamamla";
    updateSummary();
  });
}
```

</details>

### Bilgi Yarışması: Seçeneğe tıklama

Seçenek düğmelerine tıklanabilsin. `forEach((btn, i) => ...)` ile her düğmeye `click` dinleyicisi ekle. Tıklanınca:

- Düğmenin sırası `i`, `question.answer`'a eşitse `#feedback`'e `Doğru!` yaz, `score`'u 10 artır.
- Değilse `#feedback`'e `Yanlış` yaz.
- `#score` her seferinde `Puan: 10` biçiminde güncellensin.

Doğru cevabı tıklama anında `question.answer`'dan oku.

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
let score = 0;

function showQuestion(q) {
  document.querySelector("#question").textContent = q.text;
  document.querySelectorAll(".option").forEach((btn, i) => {
    btn.textContent = q.options[i];
  });
}
showQuestion(question);

// seçenek düğmelerine click dinleyicisi ekle
```

**İpuçları:**

1. document.querySelectorAll(".option").forEach((btn, i) => { btn.addEventListener("click", () => { ... }); });
2. if (i === question.answer) { ... }
3. `Puan: ${score}`

<details><summary>Çözüm</summary>

```js
const question = { text: "Kızıl gezegen hangisi?", options: ["Mars", "Venüs", "Merkür"], answer: 0 };
let score = 0;

function showQuestion(q) {
  document.querySelector("#question").textContent = q.text;
  document.querySelectorAll(".option").forEach((btn, i) => {
    btn.textContent = q.options[i];
  });
}
showQuestion(question);

// seçenek düğmelerine click dinleyicisi ekle
const feedback = document.querySelector("#feedback");
document.querySelectorAll(".option").forEach((btn, i) => {
  btn.addEventListener("click", () => {
    if (i === question.answer) {
      feedback.textContent = "Doğru!";
      score += 10;
    } else {
      feedback.textContent = "Yanlış";
    }
    document.querySelector("#score").textContent = `Puan: ${score}`;
  });
});
```

</details>
