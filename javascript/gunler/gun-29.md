# Gün 29: Projeyi toparlama

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** JavaScript Yıldızı  ·  **Maskot:** Kodi

**Bugünün hedefi:** Düğme ve klavyeyi aynı fonksiyona bağlamak, erişilebilir kontroller yapmak ve kodu init/render/update ile düzenlemek

> Projen neredeyse hazır, kaptan! Ama arkadaşın onu telefonda açınca klavye yok, ekran küçük. Bugün projeni **herkes için** kullanışlı yapıyoruz: dokunmatik kontroller, küçük ekranlar ve **erişilebilirlik**.

![JavaScript Yıldızı](../../gorseller/javascript/bolgeler/yildiz.webp)

## Konu anlatımı

### Telefonda klavye yok

Oyununu yalnızca ok tuşlarıyla yönetiyorsan telefondaki arkadaşın oynayamaz. Çözüm: ekrana ◀ ▶ gibi düğmeler koy ve **hem tuşlar hem düğmeler aynı fonksiyonu** çağırsın:

```js
function move(dx) { /* hareketin TEK yeri */ }

leftBtn.addEventListener("click", () => move(-10));
document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowLeft") move(-10);
});
```

- `click` hem fareyle hem dokunmayla çalışır.
- Basılı tutmayı algılamak istersen `pointerdown` (basıldı) ve `pointerup` (bırakıldı) olaylarını kullan; fare, parmak ve kalemin hepsinde çalışırlar.
- Parmak fare imlecinden büyüktür: dokunulacak düğmeler en az 44–48 piksel olsun.

### Küçük ekranlar ve matchMedia

Düzeni çoğunlukla CSS ayarlar: `@media (max-width: 600px) { ... }` küçük ekranlar için ayrı kurallar yazmanı sağlar. JavaScript'te de ekranı sorabilirsin:

```js
const isSmall = window.matchMedia("(max-width: 600px)").matches;
if (isSmall) {
  console.log("Küçük ekran: dokunmatik düğmeleri göster");
}
```

`matches` o anki durumu `true`/`false` olarak verir. Tuvale CSS'te `max-width: 100%` verirsen küçük ekrana sığar.

### Erişilebilirlik: herkes kullanabilsin

Bazı kullanıcılar ekranı göremez ve **ekran okuyucu** kullanır; bazıları fare kullanamaz ve yalnızca klavyeyle gezinir. Birkaç alışkanlık büyük fark yaratır:

- Tıklanan şey için `<div>` değil `<button>` kullan: düğme Tab ile seçilir, Enter ve Boşluk ile kendiliğinden çalışır.
- Yalnızca simgeden oluşan düğmeye `aria-label` ver: `btn.setAttribute("aria-label", "Sola git")`. Ekran okuyucu ◀ yerine bunu okur.
- Açılıp kapanan bir menünün düğmesinde `aria-expanded` değeri `"true"` ya da `"false"` olsun.
- Kendiliğinden değişen mesajlar (`Doğru!`, `Kaydedildi`) için kutuya `aria-live="polite"` ekle; ekran okuyucu değişikliği okur.
- `element.focus()` klavye odağını bir elemana taşır. Bir menü kapanınca odağı onu açan düğmeye geri ver.

### init, update, render

Proje büyüdükçe kod dağılır. Üç parçalı bir düzen işini kolaylaştırır:

```js
const state = { score: 0 };   // bütün veriler tek yerde

function update(action) {     // veriyi değiştirir
  if (action === "star") state.score += 10;
}

function render() {           // veriyi ekrana çizer
  scoreEl.textContent = `Skor: ${state.score}`;
}

function init() {             // olayları bağlar, ilk çizimi yapar
  starBtn.addEventListener("click", () => {
    update("star");
    render();
  });
  render();
}

init();
```

Kural basit: **ekrana yalnızca render dokunur, veriyi yalnızca update değiştirir.** Bir hata olunca nereye bakacağını hemen bilirsin.

## Örnekler

### Düğme ve tuş, tek fonksiyon

Sayfa:

```html
<p id="pos">Konum: 5</p>
<div class="controls"><button id="left" aria-label="Sola git">◀</button> <button id="right" aria-label="Sağa git">▶</button></div>
```

```js
let x = 5;
const pos = document.querySelector("#pos");

function move(dx) {
  x = Math.min(10, Math.max(0, x + dx));
  pos.textContent = `Konum: ${x}`;
}

document.querySelector("#left").addEventListener("click", () => move(-1));
document.querySelector("#right").addEventListener("click", () => move(1));
document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowLeft") move(-1);
  if (e.key === "ArrowRight") move(1);
});
```

*Düğmelere tıkla ya da önizlemeye tıklayıp ok tuşlarını kullan: ikisi de aynı move fonksiyonunu çağırır.*

### Açılır menü

Sayfa:

```html
<button id="menu-btn" aria-expanded="false" aria-label="Menüyü aç">☰</button>
<nav id="nav" hidden><a href="#a">Ana sayfa</a> <a href="#b">Blog</a></nav>
```

```js
const btn = document.querySelector("#menu-btn");
const nav = document.querySelector("#nav");

btn.addEventListener("click", () => {
  const open = nav.hidden; // gizliyse şimdi açılacak
  nav.hidden = !open;
  btn.setAttribute("aria-expanded", String(open));
  btn.setAttribute("aria-label", open ? "Menüyü kapat" : "Menüyü aç");
});
```

*Ekran okuyucu düğmeyi 'Menüyü aç, daraltılmış' diye okur; açınca 'genişletilmiş' olur.*

## Görevler

### Görev 1: Tek fonksiyon, iki yol

`move(dx)` fonksiyonunu yaz ve hem düğmelere hem ok tuşlarına bağla:

- `move(dx)`: `x`'i `dx` kadar değiştirsin; `x` 0 ile 100 arasında kalsın. `#pos`'a `Konum: 60` yazsın.
- `#left` ve `#right` düğmeleri tıklanınca `move(-10)` / `move(10)` çağrılsın.
- `ArrowLeft` ve `ArrowRight` tuşları da **aynı** fonksiyonu çağırsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<p id="pos">Konum: 50</p>
<div class="controls"><button id="left" aria-label="Sola git">◀</button> <button id="right" aria-label="Sağa git">▶</button></div>
```

**CSS:**

```css
#title{color:#0b1026}canvas{background:#0b1026;display:block;max-width:100%;border-radius:6px}#levels button{margin:4px}.controls button{font-size:22px;min-width:56px;min-height:48px;margin:4px}section h1,section h2{color:#0b1026}
```

**Başlangıç kodu:**

```js
let x = 50;
const pos = document.querySelector("#pos");

function move(dx) {
  // x'i değiştir (0 ile 100 arasında), #pos'u güncelle
}

// düğmeler ve ok tuşları aynı move fonksiyonunu çağırsın
```

**İpuçları:**

1. x = Math.min(100, Math.max(0, x + dx));
2. document.querySelector("#right").addEventListener("click", () => move(10));
3. Klavye: if (e.key === "ArrowLeft") move(-10);

<details><summary>Çözüm</summary>

```js
let x = 50;
const pos = document.querySelector("#pos");

function move(dx) {
  x = Math.min(100, Math.max(0, x + dx));
  pos.textContent = `Konum: ${x}`;
}

// düğmeler ve ok tuşları aynı move fonksiyonunu çağırsın
document.querySelector("#left").addEventListener("click", () => move(-10));
document.querySelector("#right").addEventListener("click", () => move(10));
document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowLeft") move(-10);
  if (e.key === "ArrowRight") move(10);
});
```

</details>

### Görev 2: Etiket ve odak

▶ ve ■ düğmeleri yalnızca simgeden oluşuyor; ekran okuyucu ne yaptıklarını bilemez. Düzelt:

- `#play`'e `aria-label` olarak `Başlat`, `#stop`'a `Durdur` ver (`setAttribute`).
- `#play` tıklanınca `#status` `Çalışıyor` olsun ve klavye odağı `#stop`'a geçsin (`focus()`).
- `#stop` tıklanınca `#status` `Durdu` olsun ve odak `#play`'e dönsün.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<div class="controls"><button id="play">▶</button><button id="stop">■</button></div>
<p id="status">Hazır</p>
```

**CSS:**

```css
.controls button{font-size:22px;min-width:56px;min-height:48px;margin:4px}
```

**Başlangıç kodu:**

```js
const play = document.querySelector("#play");
const stop = document.querySelector("#stop");
const status = document.querySelector("#status");

// aria-label ver

// tıklamaları bağla
```

**İpuçları:**

1. play.setAttribute("aria-label", "Başlat");
2. Odak taşımak: stop.focus();

<details><summary>Çözüm</summary>

```js
const play = document.querySelector("#play");
const stop = document.querySelector("#stop");
const status = document.querySelector("#status");

// aria-label ver
play.setAttribute("aria-label", "Başlat");
stop.setAttribute("aria-label", "Durdur");

// tıklamaları bağla
play.addEventListener("click", () => {
  status.textContent = "Çalışıyor";
  stop.focus();
});
stop.addEventListener("click", () => {
  status.textContent = "Durdu";
  play.focus();
});
```

</details>

### Görev 3: init, update, render

Yakıt göstergesini üç parçalı düzenle yaz (`state` hazır):

- `update(action)`: `"burn"` gelirse yakıt 20 azalsın (0'ın altına inmesin), `"refill"` gelirse 100 olsun. Ekrana dokunmasın.
- `render()`: `#fuel`'e `Yakıt: 80` yazsın; yakıt 20 ya da daha azsa `#fuel`'e `low` sınıfı eklesin, değilse kaldırsın.
- `init()`: `#burn` ve `#refill` düğmelerini bağlasın (tıklanınca `update` sonra `render`) ve bir kez `render` çağırsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<p id="fuel">Yakıt: ?</p>
<button id="burn">Motoru ateşle</button><button id="refill">Yakıt doldur</button>
```

**CSS:**

```css
#fuel{font-weight:bold}#fuel.low{color:#c62828}button{margin:4px;min-height:44px}
```

**Başlangıç kodu:**

```js
const state = { fuel: 100 };
const fuelEl = document.querySelector("#fuel");

function update(action) {
  // "burn" ve "refill"
}

function render() {
  // metin ve low sınıfı
}

function init() {
  // düğmeleri bağla, ilk çizim
}

init();
```

**İpuçları:**

1. if (action === "burn") state.fuel = Math.max(0, state.fuel - 20);
2. classList.toggle("low", state.fuel <= 20) sınıfı koşula göre ekler ya da kaldırır.
3. init'in sonunda render(); çağırmayı unutma.

<details><summary>Çözüm</summary>

```js
const state = { fuel: 100 };
const fuelEl = document.querySelector("#fuel");

function update(action) {
  if (action === "burn") state.fuel = Math.max(0, state.fuel - 20);
  if (action === "refill") state.fuel = 100;
}

function render() {
  fuelEl.textContent = `Yakıt: ${state.fuel}`;
  fuelEl.classList.toggle("low", state.fuel <= 20);
}

function init() {
  document.querySelector("#burn").addEventListener("click", () => {
    update("burn");
    render();
  });
  document.querySelector("#refill").addEventListener("click", () => {
    update("refill");
    render();
  });
  render();
}

init();
```

</details>

## Challenge: Klavyeyle menü

Menüdeki düğmeler arasında ok tuşlarıyla gezilebilsin:

- `#menu` içindeyken `ArrowDown` odağı bir sonraki düğmeye, `ArrowUp` bir öncekine taşısın (`focus()`).
- Uçlarda başa sarsın: sondan aşağı inince ilke, ilkten yukarı çıkınca sona.
- Bir düğmeye tıklanınca `#info`'ya `Seçildi: Ayarlar` yazılsın.

İpucu: olayın geldiği düğmeyi `e.target`, sırasını `items.indexOf(e.target)` verir.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<div id="menu"><button>Oyna</button><button>Ayarlar</button><button>Skorlar</button><button>Çıkış</button></div>
<p id="info"></p>
```

**CSS:**

```css
#menu{display:flex;flex-direction:column;gap:4px;max-width:200px}#menu button{min-height:44px}#menu button:focus{outline:3px solid #3b6ef5}
```

**Başlangıç kodu:**

```js
const items = [...document.querySelectorAll("#menu button")];
const info = document.querySelector("#info");

function focusItem(index) {
  // index dışarı taşarsa başa/sona sar, o düğmeye odaklan
}

// #menu'de keydown dinle; düğmelere click bağla
```

**İpuçları:**

1. Başa sarmak için kalan işlemi: (index + count) % count
2. const current = items.indexOf(e.target);

<details><summary>Çözüm</summary>

```js
const items = [...document.querySelectorAll("#menu button")];
const info = document.querySelector("#info");

function focusItem(index) {
  const count = items.length;
  items[(index + count) % count].focus();
}

// #menu'de keydown dinle; düğmelere click bağla
document.querySelector("#menu").addEventListener("keydown", (e) => {
  const current = items.indexOf(e.target);
  if (e.key === "ArrowDown") focusItem(current + 1);
  if (e.key === "ArrowUp") focusItem(current - 1);
});

items.forEach((item) => {
  item.addEventListener("click", () => {
    info.textContent = `Seçildi: ${item.textContent}`;
  });
});
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Mobil kontroller**

### Yıldız Avcısı: Mobil kontroller

Telefonda da oynanabilsin! Eski kodda hareket yalnızca klavyede ve mantık olayın içine gömülü. Düzenle:

- `moveShip(dx)`: `ship.x`'i değiştirsin, gemi tuvalden çıkmasın (0 ile `canvas.width - SHIP_SIZE`), sonra `draw()` çağırsın.
- Klavye (`ArrowLeft` / `ArrowRight`) ve ekrandaki `#btn-left` / `#btn-right` düğmeleri **aynı** `moveShip`'i çağırsın (adım: `STEP`).
- Simge düğmelerine `aria-label` ver: `Sola` ve `Sağa`.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1 id="title">Yıldız Avcısı</h1>
<canvas id="game" width="300" height="150"></canvas>
<div class="controls"><button id="btn-left">◀</button><button id="btn-right">▶</button></div>
```

**CSS:**

```css
#title{color:#0b1026}canvas{background:#0b1026;display:block;max-width:100%;border-radius:6px}#levels button{margin:4px}.controls button{font-size:22px;min-width:56px;min-height:48px;margin:4px}section h1,section h2{color:#0b1026}
```

**Başlangıç kodu:**

```js
const canvas = document.querySelector("#game");
const ctx = canvas.getContext("2d");
const SHIP_SIZE = 30;
const STEP = 10;
const ship = { x: 135, y: 110 };

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#f7df1e";
  ctx.fillRect(ship.x, ship.y, SHIP_SIZE, SHIP_SIZE);
}

// Eski kod: hareket yalnızca klavyede ve mantık burada gömülü
document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowLeft") ship.x -= STEP;
  if (e.key === "ArrowRight") ship.x += STEP;
  draw();
});

// 1) moveShip(dx) yaz  2) klavye ve düğmeler onu çağırsın  3) aria-label ver

draw();
```

**İpuçları:**

1. function moveShip(dx) { ship.x = Math.min(maxX, Math.max(0, ship.x + dx)); draw(); }
2. Eski keydown kodunu moveShip(-STEP) / moveShip(STEP) çağıracak şekilde değiştir.
3. rightBtn.addEventListener("click", () => moveShip(STEP));

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#game");
const ctx = canvas.getContext("2d");
const SHIP_SIZE = 30;
const STEP = 10;
const ship = { x: 135, y: 110 };

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#f7df1e";
  ctx.fillRect(ship.x, ship.y, SHIP_SIZE, SHIP_SIZE);
}

function moveShip(dx) {
  const maxX = canvas.width - SHIP_SIZE;
  ship.x = Math.min(maxX, Math.max(0, ship.x + dx));
  draw();
}

document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowLeft") moveShip(-STEP);
  if (e.key === "ArrowRight") moveShip(STEP);
});

const leftBtn = document.querySelector("#btn-left");
const rightBtn = document.querySelector("#btn-right");
leftBtn.setAttribute("aria-label", "Sola");
rightBtn.setAttribute("aria-label", "Sağa");
leftBtn.addEventListener("click", () => moveShip(-STEP));
rightBtn.addEventListener("click", () => moveShip(STEP));

draw();
```

</details>

### Kişisel Web Sitem: Erişilebilir menü

Küçük ekranda menü bir ☰ düğmesinin arkasına saklanıyor. Herkesin kullanabileceği biçimde yaz:

- `setMenu(open)`: `open` true ise menüyü göstersin (`nav.hidden = false`), değilse gizlesin. Düğmenin `aria-expanded`'ını `"true"`/`"false"`, `aria-label`'ını `Menüyü kapat` / `Menüyü aç` yapsın.
- Açılışta `setMenu(false)` çağır.
- Düğmeye tıklanınca menü açılıp kapansın.
- `Escape` tuşuna basılınca menü kapansın ve odak ☰ düğmesine dönsün.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<header><h1 id="site-title">Kod Günlüğüm</h1><button id="menu-btn" aria-controls="nav">☰</button>
<nav id="nav"><a href="#home">Ana sayfa</a><a href="#blog">Blog</a><a href="#projects">Projeler</a></nav></header>
```

**CSS:**

```css
header{display:flex;align-items:center;gap:12px;flex-wrap:wrap}header h1{margin:0;font-size:22px}nav a{margin-right:10px}.card{border:1px solid #ccd;border-radius:8px;padding:8px 12px;margin:8px 0}.card h3{margin:0 0 4px}.tech{color:#556;font-size:14px}body.dark{background:#0b1026;color:#eef}body.dark a{color:#9cf}form{display:grid;gap:6px;max-width:320px}
```

**Başlangıç kodu:**

```js
const btn = document.querySelector("#menu-btn");
const nav = document.querySelector("#nav");

function setMenu(open) {
  // hidden, aria-expanded ve aria-label
}

// açılışta kapalı; tıklama ve Escape
```

**İpuçları:**

1. btn.setAttribute("aria-expanded", String(open));
2. Tıklayınca: setMenu(nav.hidden) (gizliyse aç, açıksa kapat)
3. if (e.key === "Escape") { setMenu(false); btn.focus(); }

<details><summary>Çözüm</summary>

```js
const btn = document.querySelector("#menu-btn");
const nav = document.querySelector("#nav");

function setMenu(open) {
  nav.hidden = !open;
  btn.setAttribute("aria-expanded", String(open));
  btn.setAttribute("aria-label", open ? "Menüyü kapat" : "Menüyü aç");
}

// açılışta kapalı; tıklama ve Escape
setMenu(false);
btn.addEventListener("click", () => setMenu(nav.hidden));
document.addEventListener("keydown", (e) => {
  if (e.key === "Escape" && !nav.hidden) {
    setMenu(false);
    btn.focus();
  }
});
```

</details>

### Çalışma Asistanım: Büyük düğmeler

Asistan telefonda da kolay kullanılsın. Görev listesi ve büyük düğmeler hazır; yönetim kodunu yaz:

- `select(delta)`: `selected`'ı `delta` kadar değiştirsin (0 ile son görev arasında kalsın), sonra `render()`.
- `toggleSelected()`: seçili görevin `done`'ını tersine çevirsin, sonra `render()`.
- `#up` / `#down` / `#toggle` düğmeleri ve `ArrowUp` / `ArrowDown` / `x` tuşları **aynı** fonksiyonları çağırsın.
- ▲ ▼ düğmelerine `aria-label` ver: `Yukarı`, `Aşağı`.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1>Çalışma Asistanım</h1>
<ul id="tasks"></ul>
<div class="bar"><button id="up" class="big">▲</button><button id="down" class="big">▼</button><button id="toggle" class="big">Tamamla</button></div>
```

**CSS:**

```css
li{padding:6px;cursor:pointer}li.done{text-decoration:line-through;color:#889}li.selected{outline:2px solid #3b6ef5;border-radius:4px}.big{font-size:20px;min-width:64px;min-height:48px;margin:4px}#stats,#count{font-weight:bold}form{display:flex;gap:6px}
```

**Başlangıç kodu:**

```js
const tasks = [
  { title: "Matematik ödevi", done: false },
  { title: "Fizik tekrarı", done: false },
  { title: "Kitap okuma", done: false },
];
let selected = 0;
const list = document.querySelector("#tasks");

function render() {
  list.innerHTML = "";
  tasks.forEach((task, i) => {
    const li = document.createElement("li");
    li.textContent = task.title;
    li.classList.toggle("done", task.done);
    li.classList.toggle("selected", i === selected);
    list.append(li);
  });
}

function select(delta) {
  // selected'ı değiştir (sınırlar içinde), render
}

function toggleSelected() {
  // seçili görevi değiştir, render
}

// aria-label'lar; düğmeler ve tuşlar (ArrowUp, ArrowDown, x)

render();
```

**İpuçları:**

1. selected = Math.min(tasks.length - 1, Math.max(0, selected + delta));
2. upBtn.addEventListener("click", () => select(-1));
3. Klavyede: if (e.key === "x") toggleSelected();

<details><summary>Çözüm</summary>

```js
const tasks = [
  { title: "Matematik ödevi", done: false },
  { title: "Fizik tekrarı", done: false },
  { title: "Kitap okuma", done: false },
];
let selected = 0;
const list = document.querySelector("#tasks");

function render() {
  list.innerHTML = "";
  tasks.forEach((task, i) => {
    const li = document.createElement("li");
    li.textContent = task.title;
    li.classList.toggle("done", task.done);
    li.classList.toggle("selected", i === selected);
    list.append(li);
  });
}

function select(delta) {
  selected = Math.min(tasks.length - 1, Math.max(0, selected + delta));
  render();
}

function toggleSelected() {
  tasks[selected].done = !tasks[selected].done;
  render();
}

// aria-label'lar; düğmeler ve tuşlar (ArrowUp, ArrowDown, x)
const upBtn = document.querySelector("#up");
const downBtn = document.querySelector("#down");
upBtn.setAttribute("aria-label", "Yukarı");
downBtn.setAttribute("aria-label", "Aşağı");
upBtn.addEventListener("click", () => select(-1));
downBtn.addEventListener("click", () => select(1));
document.querySelector("#toggle").addEventListener("click", toggleSelected);
document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowUp") select(-1);
  if (e.key === "ArrowDown") select(1);
  if (e.key === "x") toggleSelected();
});

render();
```

</details>

### Bilgi Yarışması: Tıkla ya da tuşla

Yarışma hem dokunarak hem klavyeyle oynanabilsin. Tek bir `choose(i)` fonksiyonu yaz ve her yere bağla:

- `choose(i)`: soru zaten cevaplandıysa hiçbir şey yapmasın (erken dönüş). Değilse `answered = true`; doğruysa `score` 10 artsın ve `#feedback` `Doğru!` olsun, yanlışsa `Yanlış! Doğru cevap: Dünya`. `#score`'a `Puan: 10` yaz.
- Seçenek düğmelerine tıklama (`data-i` sırası) ve `1`, `2`, `3` tuşları `choose`'u çağırsın.
- `#feedback`'e `aria-live="polite"` ekle: ekran okuyucu sonucu okusun.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1>Bilgi Yarışması</h1>
<p id="question"></p>
<div id="options"><button data-i="0"></button><button data-i="1"></button><button data-i="2"></button></div>
<p id="feedback"></p>
<p id="score">Puan: 0</p>
<button id="next">Sonraki soru</button>
```

**CSS:**

```css
#options button{display:block;width:100%;max-width:320px;margin:6px 0;padding:10px;font-size:18px}#feedback{font-weight:bold}
```

**Başlangıç kodu:**

```js
const questions = [
  { soru: "Ay, hangi gezegenin uydusudur?", secenekler: ["Mars", "Dünya", "Jüpiter"], dogru: 1 },
  { soru: "Güneş sistemindeki en büyük gezegen hangisidir?", secenekler: ["Satürn", "Jüpiter", "Neptün"], dogru: 1 },
];
let current = 0;
let score = 0;
let answered = false;
const optionButtons = document.querySelectorAll("#options button");
const feedback = document.querySelector("#feedback");

function showQuestion() {
  const q = questions[current];
  document.querySelector("#question").textContent = q.soru;
  optionButtons.forEach((btn, i) => {
    btn.textContent = `${i + 1}) ${q.secenekler[i]}`;
  });
  feedback.textContent = "";
  answered = false;
}

function choose(i) {
  // cevaplandıysa çık; değilse değerlendir, #feedback ve #score
}

document.querySelector("#next").addEventListener("click", () => {
  current = (current + 1) % questions.length;
  showQuestion();
});

// aria-live; seçenek tıklamaları; 1, 2, 3 tuşları

showQuestion();
```

**İpuçları:**

1. if (answered) return; ile başla.
2. Düğmenin sırası: Number(btn.dataset.i)
3. Tuşlar: if (["1", "2", "3"].includes(e.key)) choose(Number(e.key) - 1);

<details><summary>Çözüm</summary>

```js
const questions = [
  { soru: "Ay, hangi gezegenin uydusudur?", secenekler: ["Mars", "Dünya", "Jüpiter"], dogru: 1 },
  { soru: "Güneş sistemindeki en büyük gezegen hangisidir?", secenekler: ["Satürn", "Jüpiter", "Neptün"], dogru: 1 },
];
let current = 0;
let score = 0;
let answered = false;
const optionButtons = document.querySelectorAll("#options button");
const feedback = document.querySelector("#feedback");

function showQuestion() {
  const q = questions[current];
  document.querySelector("#question").textContent = q.soru;
  optionButtons.forEach((btn, i) => {
    btn.textContent = `${i + 1}) ${q.secenekler[i]}`;
  });
  feedback.textContent = "";
  answered = false;
}

function choose(i) {
  if (answered) return;
  answered = true;
  const q = questions[current];
  if (i === q.dogru) {
    score += 10;
    feedback.textContent = "Doğru!";
  } else {
    feedback.textContent = `Yanlış! Doğru cevap: ${q.secenekler[q.dogru]}`;
  }
  document.querySelector("#score").textContent = `Puan: ${score}`;
}

document.querySelector("#next").addEventListener("click", () => {
  current = (current + 1) % questions.length;
  showQuestion();
});

// aria-live; seçenek tıklamaları; 1, 2, 3 tuşları
feedback.setAttribute("aria-live", "polite");
optionButtons.forEach((btn) => {
  btn.addEventListener("click", () => choose(Number(btn.dataset.i)));
});
document.addEventListener("keydown", (e) => {
  if (["1", "2", "3"].includes(e.key)) choose(Number(e.key) - 1);
});

showQuestion();
```

</details>
