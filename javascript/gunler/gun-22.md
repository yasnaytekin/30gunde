# Gün 22: Animasyon

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Piksel Gezegeni  ·  **Maskot:** Kodi

**Bugünün hedefi:** requestAnimationFrame ile animasyon döngüsü kurmak, update ve draw'u ayırmak, hız ve sekme hesaplamak

> Piksel Gezegeni'nde resimler kıpırdamaya başladı! Çizgi filmler gibi oyunlar da saniyede onlarca resmi art arda çizer. Bugün bir **animasyon döngüsü** kuracak ve gemini hareket ettireceksin.

![Piksel Gezegeni](../../gorseller/javascript/bolgeler/piksel.webp)

## Konu anlatımı

### Animasyon nasıl çalışır?

Ekrandaki her hareket aslında hızla değişen resimlerdir. Her **karede** (frame) üç şey olur:

1. Nesnelerin yerini biraz değiştir.
2. Eski resmi sil.
3. Yeni resmi çiz.

Tarayıcı bunun için bize `requestAnimationFrame` (kısaca rAF) verir. Anlamı: "bir sonraki resmi çizmeden hemen önce bu fonksiyonu çalıştır". Fonksiyon her seferinde kendini yeniden isterse tarayıcıyı dondurmayan bir döngü olur (genellikle saniyede 60 kare):

```js
function loop() {
  update();                    // hesapla
  draw();                      // çiz
  requestAnimationFrame(loop); // bir sonraki kareyi iste
}
requestAnimationFrame(loop);
```

`while (true)` ile animasyon yapılmaz: tarayıcı çizim yapmaya fırsat bulamaz ve sayfa donar.

### update ve draw'u ayır

İyi bir alışkanlık: **hesaplamayı** ve **çizimi** ayrı fonksiyonlarda tut.

```js
const ball = { x: 20, y: 60, r: 10, vx: 2 };

function update() {
  ball.x += ball.vx;  // yalnızca sayıları değiştirir
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.r, 0, Math.PI * 2);
  ctx.fill();         // yalnızca çizer
}
```

Böylece `update()`'i tek başına çağırıp sonucunu kontrol edebilir, oyunu durdurduğunda yalnızca `draw()` çağırabilirsin. Bu kurstaki kontroller de fonksiyonlarını tek tek çağırarak sınar.

### Hız ve kenardan sekme

**Hız** (`vx`, `vy`), her karede konumun ne kadar değişeceğidir. `vx = 3` ise nesne her karede 3 piksel sağa gider, `vx = -3` ise sola.

Kenara çarpınca geri dönmesi için hızın işaretini çeviririz:

```js
if (ball.x + ball.r > canvas.width || ball.x - ball.r < 0) {
  ball.vx = -ball.vx;
}
```

Nesne kenarın biraz dışına taştıysa onu kenara geri koymak (**sınırlamak**) da iyi olur. `Math.max` ve `Math.min` bunun kısa yoludur: `x = Math.max(0, Math.min(x, canvas.width - w));`

### Zaman farkı (delta) ve durdurmak

Bazı ekranlar saniyede 60, bazıları 120 kare çizer. Hızı "kare başına" yazarsan oyun hızlı ekranda iki kat hızlı oynar! Çözüm: hızı **saniye başına** yaz ve iki kare arasında geçen süreyle (`dt`) çarp. rAF, fonksiyona milisaniye cinsinden zamanı verir:

```js
let last = 0;
function loop(time) {
  if (!last) last = time;            // ilk kare
  const dt = (time - last) / 1000;   // saniye
  last = time;
  rocket.x += rocket.speed * dt;     // speed: piksel/saniye
  draw();
  frameId = requestAnimationFrame(loop);
}
```

`requestAnimationFrame` bir numara döndürür. `cancelAnimationFrame(frameId)` bu numaralı kareyi iptal eder ve döngü durur.

## Örnekler

### Kayan kare

Sayfa:

```html
<canvas id="c" width="200" height="120"></canvas>
```

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const box = { x: 0, y: 50, size: 20, vx: 2 };

function update() {
  box.x += box.vx;
  if (box.x > canvas.width) box.x = -box.size; // sağdan çıkınca soldan gir
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#4fc3f7";
  ctx.fillRect(box.x, box.y, box.size, box.size);
}

function loop() {
  update();
  draw();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

*vx'i 5 yap: kare daha hızlı kayar. Negatif yaparsan ne olur?*

### Seken top

Sayfa:

```html
<canvas id="c" width="200" height="120"></canvas>
```

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const ball = { x: 50, y: 40, r: 10, vx: 2.5, vy: 1.5 };

function update() {
  ball.x += ball.vx;
  ball.y += ball.vy;
  if (ball.x + ball.r > canvas.width || ball.x - ball.r < 0) ball.vx = -ball.vx;
  if (ball.y + ball.r > canvas.height || ball.y - ball.r < 0) ball.vy = -ball.vy;
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.r, 0, Math.PI * 2);
  ctx.fillStyle = "#ff9800";
  ctx.fill();
}

function loop() {
  update();
  draw();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

*draw içindeki clearRect satırını silersen top arkasında iz bırakır.*

## Görevler

### Görev 1: İlk hareket

Döngü hazır; sen iki fonksiyonu yaz:

- `update()`: `box.x`'e `box.vx` eklesin.
- `draw()`: tuvali `clearRect` ile silip kutuyu mavi (`#4fc3f7`), `size` × `size` boyutunda bir kare olarak `(box.x, box.y)` noktasına çizsin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<canvas id="c" width="200" height="120"></canvas>
```

**CSS:**

```css
canvas{background:#e8ebf3;border-radius:8px;max-width:100%;display:block}
```

**Başlangıç kodu:**

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const box = { x: 10, y: 50, size: 20, vx: 1 };

function update() {
  // box.x'i vx kadar artır
}

function draw() {
  // temizle ve kutuyu çiz
}

function loop() {
  update();
  draw();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

**İpuçları:**

1. box.x += box.vx;
2. draw: ctx.clearRect(0, 0, canvas.width, canvas.height); sonra fillStyle ve fillRect(box.x, box.y, box.size, box.size)

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const box = { x: 10, y: 50, size: 20, vx: 1 };

function update() {
  // box.x'i vx kadar artır
  box.x += box.vx;
}

function draw() {
  // temizle ve kutuyu çiz
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#4fc3f7";
  ctx.fillRect(box.x, box.y, box.size, box.size);
}

function loop() {
  update();
  draw();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

</details>

### Görev 2: Duvardan sek

Top dört duvardan da seksin. `update()` içinde konum zaten değişiyor; altına şunları ekle:

- Top sağ ya da sol kenarı geçtiyse (`ball.x + ball.r > canvas.width` veya `ball.x - ball.r < 0`) `vx`'in işaretini çevir.
- Üst ya da alt kenar için aynısını `vy` ve `canvas.height` ile yap.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<canvas id="c" width="200" height="120"></canvas>
```

**CSS:**

```css
canvas{background:#e8ebf3;border-radius:8px;max-width:100%;display:block}
```

**Başlangıç kodu:**

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const ball = { x: 100, y: 60, r: 10, vx: 3, vy: 2 };

function update() {
  ball.x += ball.vx;
  ball.y += ball.vy;
  // kenarlardan sek
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.r, 0, Math.PI * 2);
  ctx.fillStyle = "#ff9800";
  ctx.fill();
}


function loop() {
  update();
  draw();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

**İpuçları:**

1. if (ball.x + ball.r > canvas.width || ball.x - ball.r < 0) { ball.vx = -ball.vx; }
2. Aynısını y, vy ve canvas.height ile yaz.

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const ball = { x: 100, y: 60, r: 10, vx: 3, vy: 2 };

function update() {
  ball.x += ball.vx;
  ball.y += ball.vy;
  // kenarlardan sek
  if (ball.x + ball.r > canvas.width || ball.x - ball.r < 0) {
    ball.vx = -ball.vx;
  }
  if (ball.y + ball.r > canvas.height || ball.y - ball.r < 0) {
    ball.vy = -ball.vy;
  }
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.r, 0, Math.PI * 2);
  ctx.fillStyle = "#ff9800";
  ctx.fill();
}


function loop() {
  update();
  draw();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

</details>

### Görev 3: Saniyede 120 piksel

Roketin hızı artık **saniye başına** piksel: `speed: 120`.

- `update(dt)` fonksiyonunu yaz: `dt` saniye cinsinden geçen süre; roket `speed * dt` kadar ilerlesin.
- `loop(time)` içinde `dt`'yi hesapla: `(time - last) / 1000`. Sonra `last = time` yap ve `update(dt)`'yi çağır.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<canvas id="c" width="200" height="120"></canvas>
```

**CSS:**

```css
canvas{background:#e8ebf3;border-radius:8px;max-width:100%;display:block}
```

**Başlangıç kodu:**

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const rocket = { x: 0, y: 50, speed: 120 };
let last = 0;

function update(dt) {
  // speed * dt kadar ilerle
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#e53935";
  ctx.fillRect(rocket.x, rocket.y, 24, 12);
}

function loop(time) {
  if (!last) last = time;
  // dt'yi hesapla, last'ı güncelle, update(dt) çağır
  if (rocket.x > canvas.width) rocket.x = -24;
  draw();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

**İpuçları:**

1. rocket.x += rocket.speed * dt;
2. const dt = (time - last) / 1000; last = time; update(dt);

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const rocket = { x: 0, y: 50, speed: 120 };
let last = 0;

function update(dt) {
  // speed * dt kadar ilerle
  rocket.x += rocket.speed * dt;
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#e53935";
  ctx.fillRect(rocket.x, rocket.y, 24, 12);
}

function loop(time) {
  if (!last) last = time;
  // dt'yi hesapla, last'ı güncelle, update(dt) çağır
  const dt = (time - last) / 1000;
  last = time;
  update(dt);
  if (rocket.x > canvas.width) rocket.x = -24;
  draw();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

</details>

## Challenge: Durdur / Başlat

Düğmeyle animasyonu durdur ve yeniden başlat. `requestAnimationFrame`'in döndürdüğü numara `frameId`'de saklanıyor.

- `running` true iken düğmeye tıklanırsa: `cancelAnimationFrame(frameId)` ile durdur, `running = false` yap, düğmenin metni `Başlat` olsun.
- `running` false iken tıklanırsa: `running = true` yap, döngüyü `requestAnimationFrame(loop)` ile yeniden başlat, düğmenin metni `Durdur` olsun.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<canvas id="c" width="200" height="120"></canvas>
<p><button id="toggle">Durdur</button></p>
```

**CSS:**

```css
canvas{background:#e8ebf3;border-radius:8px;max-width:100%;display:block}
```

**Başlangıç kodu:**

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const btn = document.querySelector("#toggle");
let angle = 0;
let running = true;
let frameId = 0;

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const x = 100 + Math.cos(angle) * 40;
  const y = 60 + Math.sin(angle) * 40;
  ctx.beginPath();
  ctx.arc(x, y, 8, 0, Math.PI * 2);
  ctx.fillStyle = "#4fc3f7";
  ctx.fill();
}

function loop() {
  angle += 0.05;
  draw();
  frameId = requestAnimationFrame(loop);
}
frameId = requestAnimationFrame(loop);

btn.addEventListener("click", () => {
  // running'e göre durdur ya da başlat
});
```

**İpuçları:**

1. if (running) { ... } else { ... }
2. Durdurmak: cancelAnimationFrame(frameId);
3. Başlatmak: frameId = requestAnimationFrame(loop);

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const btn = document.querySelector("#toggle");
let angle = 0;
let running = true;
let frameId = 0;

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const x = 100 + Math.cos(angle) * 40;
  const y = 60 + Math.sin(angle) * 40;
  ctx.beginPath();
  ctx.arc(x, y, 8, 0, Math.PI * 2);
  ctx.fillStyle = "#4fc3f7";
  ctx.fill();
}

function loop() {
  angle += 0.05;
  draw();
  frameId = requestAnimationFrame(loop);
}
frameId = requestAnimationFrame(loop);

btn.addEventListener("click", () => {
  // running'e göre durdur ya da başlat
  if (running) {
    cancelAnimationFrame(frameId);
    running = false;
    btn.textContent = "Başlat";
  } else {
    running = true;
    frameId = requestAnimationFrame(loop);
    btn.textContent = "Durdur";
  }
});
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Gemi hareketi**

### Yıldız Avcısı: Gemi hareketi

Gemi artık kendi kendine yatay gidip gelsin.

- `update()`: `ship.x`'e `ship.vx` ekle. Gemi sol kenarı geçerse (`ship.x < 0`) onu `0`'a koy; sağ kenarı geçerse (`ship.x + ship.w > canvas.width`) `canvas.width - ship.w`'ye koy. İki durumda da `vx`'in işaretini çevir.
- `draw()` hazır: zemini, gemiyi ve yıldızları çiziyor.
- `loop()`: `update()` ve `draw()`'u çağırıp kendini `requestAnimationFrame` ile yeniden istesin. Döngüyü başlatmayı unutma.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<canvas id="game" width="300" height="200"></canvas>
<p id="info">Skor: 0</p>
```

**CSS:**

```css
canvas{background:#0b1026;display:block;max-width:100%;border-radius:8px}#info{font-weight:600;margin:8px 0 0}
```

**Başlangıç kodu:**

```js
const canvas = document.querySelector("#game");
const ctx = canvas.getContext("2d");

const ship = { x: 20, y: 150, w: 30, h: 20, vx: 3 };
const stars = [
  { x: 120, y: 40 },
  { x: 200, y: 60 },
  { x: 260, y: 110 },
];

function draw() {
  ctx.fillStyle = "#0b1026";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#4fc3f7";
  ctx.fillRect(ship.x, ship.y, ship.w, ship.h);
  ctx.fillStyle = "#f7df1e";
  for (const star of stars) {
    ctx.beginPath();
    ctx.arc(star.x, star.y, 6, 0, Math.PI * 2);
    ctx.fill();
  }
}

function update() {
  // ilerle, kenarda dur ve geri dön
}

// loop fonksiyonunu yaz ve başlat

draw();
```

**İpuçları:**

1. ship.x += ship.vx;
2. if (ship.x + ship.w > canvas.width) { ship.x = canvas.width - ship.w; ship.vx = -ship.vx; }
3. function loop() { update(); draw(); requestAnimationFrame(loop); }

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#game");
const ctx = canvas.getContext("2d");

const ship = { x: 20, y: 150, w: 30, h: 20, vx: 3 };
const stars = [
  { x: 120, y: 40 },
  { x: 200, y: 60 },
  { x: 260, y: 110 },
];

function draw() {
  ctx.fillStyle = "#0b1026";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#4fc3f7";
  ctx.fillRect(ship.x, ship.y, ship.w, ship.h);
  ctx.fillStyle = "#f7df1e";
  for (const star of stars) {
    ctx.beginPath();
    ctx.arc(star.x, star.y, 6, 0, Math.PI * 2);
    ctx.fill();
  }
}

function update() {
  // ilerle, kenarda dur ve geri dön
  ship.x += ship.vx;
  if (ship.x < 0) {
    ship.x = 0;
    ship.vx = -ship.vx;
  } else if (ship.x + ship.w > canvas.width) {
    ship.x = canvas.width - ship.w;
    ship.vx = -ship.vx;
  }
}

// loop fonksiyonunu yaz ve başlat
function loop() {
  update();
  draw();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);

draw();
```

</details>

### Kişisel Web Sitem: Kayan duyuru bandı

Sitenin üstünde sağdan sola kayan bir duyuru bandı olsun. `step()` fonksiyonunu yaz:

- `offset`'i `speed` kadar azalt.
- `offset`, `-200`'den küçük olursa `300` yap (yazı sağdan yeniden girsin).
- `#ticker`'ın `style.transform` değerini `translateX(...px)` yap; `...` yerine `offset` gelsin.

Sonra `loop()` ile `step()`'i her karede çağır (`requestAnimationFrame`).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<header><h1 id="site-title">Ada'nın Sitesi</h1><nav><a href="#">Ana sayfa</a> · <a href="#">Galeri</a> · <a href="#">İletişim</a></nav></header>
<div id="ticker-box"><p id="ticker">Yeni yazım yayında: Döngüler neden harika?</p></div>
```

**CSS:**

```css
header{border-bottom:3px solid #7e57c2;margin-bottom:10px;padding-bottom:4px}#site-title{margin:0;color:#4a2f8a;font-size:22px}nav a{color:#7e57c2}#ticker-box{overflow:hidden;background:#1b1f33;color:#fff;border-radius:6px;height:34px;position:relative}#ticker{position:absolute;left:0;top:6px;margin:0;white-space:nowrap}
```

**Başlangıç kodu:**

```js
const ticker = document.querySelector("#ticker");
let offset = 300;
let speed = 1;

function step() {
  // offset'i azalt, gerekirse başa sar, transform'u ayarla
}

// loop: step() ve requestAnimationFrame
```

**İpuçları:**

1. offset -= speed;
2. if (offset < -200) offset = 300;
3. ticker.style.transform = `translateX(${offset}px)`;

<details><summary>Çözüm</summary>

```js
const ticker = document.querySelector("#ticker");
let offset = 300;
let speed = 1;

function step() {
  // offset'i azalt, gerekirse başa sar, transform'u ayarla
  offset -= speed;
  if (offset < -200) offset = 300;
  ticker.style.transform = `translateX(${offset}px)`;
}

// loop: step() ve requestAnimationFrame
function loop() {
  step();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

</details>

### Çalışma Asistanım: Yumuşak ilerleme çubuğu

Hedef yüzdesi değişince çubuk birden zıplamasın, yavaşça ilerlesin. `step()` fonksiyonunu yaz:

- `progress`, `target`'tan küçükse `2` artsın, büyükse `2` azalsın; ama `target`'ı **geçmesin**, tam `target`'ta dursun.
- `#bar`'ın genişliğini `progress + "%"` yap ve `#percent`'e `%42` biçiminde yaz.

`animateTo(value)` fonksiyonunu da yaz: `target = value` yapsın ve `progress` hedefe varana kadar `step()`'i her karede çağıran bir döngü başlatsın (`requestAnimationFrame`).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 class="app-title">Çalışma Asistanım</h2>
<p>Bugünkü hedef</p>
<div id="track"><div id="bar"></div></div>
<p id="percent">%0</p>
```

**CSS:**

```css
.app-title{margin:0 0 8px;color:#2e7d32}#track{background:#e0e0e0;border-radius:8px;height:18px;overflow:hidden}#bar{background:#4caf50;height:100%;width:0}
```

**Başlangıç kodu:**

```js
const bar = document.querySelector("#bar");
const percent = document.querySelector("#percent");
let progress = 0;
let target = 0;

function step() {
  // progress'i hedefe doğru 2 yaklaştır, çubuğu ve yazıyı güncelle
}

function animateTo(value) {
  // target'ı ayarla, döngüyü başlat
}

animateTo(60);
```

**İpuçları:**

1. Artarken hedefi geçmemek için: progress = Math.min(progress + 2, target);
2. Azalırken: progress = Math.max(progress - 2, target);
3. animateTo içinde step() çağıran küçük bir tick fonksiyonu yaz ve requestAnimationFrame(tick) ile başlat.

<details><summary>Çözüm</summary>

```js
const bar = document.querySelector("#bar");
const percent = document.querySelector("#percent");
let progress = 0;
let target = 0;

function step() {
  // progress'i hedefe doğru 2 yaklaştır, çubuğu ve yazıyı güncelle
  if (progress < target) {
    progress = Math.min(progress + 2, target);
  } else if (progress > target) {
    progress = Math.max(progress - 2, target);
  }
  bar.style.width = progress + "%";
  percent.textContent = "%" + progress;
}

function animateTo(value) {
  // target'ı ayarla, döngüyü başlat
  target = value;
  function tick() {
    step();
    if (progress !== target) requestAnimationFrame(tick);
  }
  requestAnimationFrame(tick);
}

animateTo(60);
```

</details>

### Bilgi Yarışması: Süre çubuğu

Her soru için 10 saniye var; süre azaldıkça çubuk daralsın. Döngü hazır, `step(dt)` fonksiyonunu yaz (`dt`: geçen süre, saniye):

- `timeLeft`'ten `dt` çıkar; `0`'ın altına inmesin.
- `#time-bar`'ın genişliği kalan sürenin yüzdesi olsun: `timeLeft * 100 / TOTAL` ve sonuna `%`.
- `#info`'ya `Süre: 7 sn` yaz (saniyeyi yukarı yuvarla: `Math.ceil`).
- Süre `0` olunca `#info` `Süre doldu!` yazsın ve çubuğa `empty` sınıfı eklensin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 class="quiz-title">Bilgi Yarışması</h2>
<p id="question">Ay, hangi gezegenin uydusudur?</p>
<div id="timer"><div id="time-bar"></div></div>
<p id="info">Süre: 10 sn</p>
```

**CSS:**

```css
.quiz-title{margin:0 0 8px;color:#5e35b1}#timer{background:#eee;height:14px;border-radius:7px;overflow:hidden}#time-bar{background:#7e57c2;height:100%;width:100%}#time-bar.empty{background:#e53935}
```

**Başlangıç kodu:**

```js
const TOTAL = 10;
let timeLeft = 10;
const bar = document.querySelector("#time-bar");
const info = document.querySelector("#info");

function step(dt) {
  // süreyi azalt, çubuğu ve yazıyı güncelle
}

let last = 0;
function loop(time) {
  if (!last) last = time;
  step((time - last) / 1000);
  last = time;
  if (timeLeft > 0) requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

**İpuçları:**

1. timeLeft = Math.max(0, timeLeft - dt);
2. bar.style.width = timeLeft * 100 / TOTAL + "%";
3. if (timeLeft === 0) { ... } else { info.textContent = `Süre: ${Math.ceil(timeLeft)} sn`; }

<details><summary>Çözüm</summary>

```js
const TOTAL = 10;
let timeLeft = 10;
const bar = document.querySelector("#time-bar");
const info = document.querySelector("#info");

function step(dt) {
  // süreyi azalt, çubuğu ve yazıyı güncelle
  timeLeft = Math.max(0, timeLeft - dt);
  bar.style.width = timeLeft * 100 / TOTAL + "%";
  if (timeLeft === 0) {
    info.textContent = "Süre doldu!";
    bar.classList.add("empty");
  } else {
    info.textContent = `Süre: ${Math.ceil(timeLeft)} sn`;
  }
}

let last = 0;
function loop(time) {
  if (!last) last = time;
  step((time - last) / 1000);
  last = time;
  if (timeLeft > 0) requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

</details>
