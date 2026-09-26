# Gün 23: Oyun döngüsü

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Piksel Gezegeni  ·  **Maskot:** Kodi

**Bugünün hedefi:** oyunun durumunu bir nesnede tutmak, dikdörtgen çarpışmasını hesaplamak, skor ve oyun bitti durumunu yönetmek

> Piksel Gezegeni'nin son durağındasın. Çizmeyi ve hareket ettirmeyi öğrendin; şimdi hepsini birleştirip gerçek bir **oyun döngüsü** kuracaksın: hareket et, çarpışmaları yakala, puan topla, gerekirse oyunu bitir.

![Piksel Gezegeni](../../gorseller/javascript/bolgeler/piksel.webp)

## Konu anlatımı

### Oyunun durumu tek yerde

Bir oyunda o anki her şey (oyuncunun yeri, yıldızlar, skor, oyun bitti mi) **durum** (state) olarak adlandırılır. Hepsini tek bir nesnede tutmak işleri çok kolaylaştırır:

```js
const game = {
  player: { x: 20, y: 150, w: 30, h: 20 },
  stars: [{ x: 120, y: 40, w: 12, h: 12 }],
  score: 0,
  over: false,
};
```

Artık `console.log(game)` bütün oyunu gösterir; kaydetmek, yeniden başlatmak ve hata aramak kolaylaşır.

### Döngünün üç adımı

Her karede aynı sıra izlenir: **güncelle → çarpışmaları kontrol et → çiz**.

```js
function step() {
  if (!game.over) {
    update();   // her şeyi hareket ettir
    collide();  // çarpışmalara bak, puanı değiştir
  }
  draw();       // durumu ekrana çiz
}

function loop() {
  step();
  requestAnimationFrame(loop);
}
```

Sıra önemli: önce hareket, sonra çarpışma, en son çizim. Böylece ekranda her zaman en güncel durum görünür. Oyun bitince `update` ve `collide` durur ama `draw` son hali göstermeye devam eder.

### Dikdörtgen çarpışması (AABB)

İki dikdörtgen, hem yatayda **hem de** dikeyde üst üste biniyorsa çarpışır. Bunu dört koşulla yazarız:

```js
function hits(a, b) {
  return a.x < b.x + b.w &&  // a, b'nin sağ kenarından önce başlıyor
         a.x + a.w > b.x &&  // a'nın sağ kenarı b'nin solunu geçiyor
         a.y < b.y + b.h &&  // dikeyde de aynısı
         a.y + a.h > b.y;
}
```

Dört koşuldan biri bile yanlışsa aralarında boşluk vardır. Tam kenar kenara değmek (`a.x + a.w === b.x`) çarpışma sayılmaz.

Oyunlarda buna **AABB** (eksenlere hizalı kutu) testi denir: çok hızlıdır ve çoğu oyuna yeter. Daire şeklindeki nesneler için bile çoğu zaman çevrelerindeki kutu kullanılır.

### Toplamak, oyun bitti, yeniden başla

Değen yıldızları çıkarıp her biri için puan vermenin güvenli yolu `filter`'dır (döngü içinde diziden eleman silmek karışıklık çıkarır):

```js
const before = game.stars.length;
game.stars = game.stars.filter((s) => !hits(game.player, s));
game.score += before - game.stars.length;
if (game.stars.length === 0) game.over = true;
```

Yeniden başlatmak için durumu sıfırdan kuran bir fonksiyon yaz:

```js
function newGame() {
  return { player: { x: 20, y: 150, w: 30, h: 20 }, stars: makeStars(), score: 0, over: false };
}
let game = newGame();
function restart() {
  game = newGame();
}
```

Her seferinde **yeni** nesne ve **yeni** dizi üretmek önemli: eski diziyi tekrar kullanırsan toplanmış yıldızlar geri gelmez.

## Örnekler

### Çarpışma dedektörü

Sayfa:

```html
<canvas id="c" width="240" height="100"></canvas>
<p id="info"></p>
```

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const wall = { x: 130, y: 30, w: 40, h: 40 };
const box = { x: 0, y: 40, w: 20, h: 20, vx: 1.5 };

function hits(a, b) {
  return a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;
}

function step() {
  box.x += box.vx;
  if (box.x > canvas.width) box.x = -box.w;
  const hit = hits(box, wall);
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = hit ? "#e53935" : "#9e9e9e";
  ctx.fillRect(wall.x, wall.y, wall.w, wall.h);
  ctx.fillStyle = "#4fc3f7";
  ctx.fillRect(box.x, box.y, box.w, box.h);
  document.querySelector("#info").textContent = hit ? "Çarpışma!" : "Yol açık";
}

function loop() {
  step();
  requestAnimationFrame(loop);
}
loop();
```

*Kutu duvara girince duvar kırmızı olur. wall.y'yi 70 yap: artık çarpışmaz.*

### Mini oyun: yıldız topla

Sayfa:

```html
<canvas id="c" width="240" height="100"></canvas>
<p id="info"></p>
```

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const info = document.querySelector("#info");

function hits(a, b) {
  return a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;
}

function newGame() {
  return {
    player: { x: 10, y: 40, w: 20, h: 20, vx: 0, vy: 0 },
    stars: [
      { x: 80, y: 20, w: 10, h: 10 },
      { x: 150, y: 70, w: 10, h: 10 },
      { x: 210, y: 30, w: 10, h: 10 },
    ],
    score: 0,
    over: false,
  };
}
let game = newGame();

document.addEventListener("keydown", (e) => {
  const p = game.player;
  if (e.key === "ArrowRight") p.vx = 2;
  if (e.key === "ArrowLeft") p.vx = -2;
  if (e.key === "ArrowUp") p.vy = -2;
  if (e.key === "ArrowDown") p.vy = 2;
  if (e.key === "r") game = newGame();
});
document.addEventListener("keyup", () => {
  game.player.vx = 0;
  game.player.vy = 0;
});

function update() {
  const p = game.player;
  p.x = Math.max(0, Math.min(p.x + p.vx, canvas.width - p.w));
  p.y = Math.max(0, Math.min(p.y + p.vy, canvas.height - p.h));
}

function collide() {
  const before = game.stars.length;
  game.stars = game.stars.filter((s) => !hits(game.player, s));
  game.score += before - game.stars.length;
  if (game.stars.length === 0) game.over = true;
}

function draw() {
  ctx.fillStyle = "#0b1026";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#f7df1e";
  for (const s of game.stars) ctx.fillRect(s.x, s.y, s.w, s.h);
  ctx.fillStyle = "#4fc3f7";
  ctx.fillRect(game.player.x, game.player.y, game.player.w, game.player.h);
  info.textContent = game.over ? "Tebrikler! Yeniden başlamak için R tuşu" : "Skor: " + game.score;
}

function loop() {
  if (!game.over) {
    update();
    collide();
  }
  draw();
  requestAnimationFrame(loop);
}
loop();
```

*Önizlemeye tıkla, sonra ok tuşlarıyla gemiyi yönet.*

## Görevler

### Görev 1: Çarpışıyor mu?

`hits(a, b)` fonksiyonunu yaz: `{ x, y, w, h }` biçimindeki iki dikdörtgen üst üste biniyorsa `true`, binmiyorsa `false` döndürsün.

Kenar kenara değmek çarpışma sayılmaz. Alttaki kod sonucu `#info`'ya yazıyor.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<canvas id="c" width="200" height="120"></canvas>
<p id="info"></p>
```

**CSS:**

```css
canvas{background:#e8ebf3;border-radius:8px;max-width:100%;display:block}
```

**Başlangıç kodu:**

```js
const ctx = document.querySelector("#c").getContext("2d");
const ship = { x: 40, y: 40, w: 40, h: 30 };
const rock = { x: 70, y: 60, w: 30, h: 30 };

function hits(a, b) {
  // dört koşul
  return false;
}

ctx.fillStyle = "#4fc3f7";
ctx.fillRect(ship.x, ship.y, ship.w, ship.h);
ctx.fillStyle = "#9e9e9e";
ctx.fillRect(rock.x, rock.y, rock.w, rock.h);
document.querySelector("#info").textContent = "Çarpışma: " + (hits(ship, rock) ? "evet" : "hayır");
```

**İpuçları:**

1. Yatayda: a.x < b.x + b.w && a.x + a.w > b.x
2. Dikeyde aynısı y ve h ile. Dördünü && ile bağla.

<details><summary>Çözüm</summary>

```js
const ctx = document.querySelector("#c").getContext("2d");
const ship = { x: 40, y: 40, w: 40, h: 30 };
const rock = { x: 70, y: 60, w: 30, h: 30 };

function hits(a, b) {
  // dört koşul
  return a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;
}

ctx.fillStyle = "#4fc3f7";
ctx.fillRect(ship.x, ship.y, ship.w, ship.h);
ctx.fillStyle = "#9e9e9e";
ctx.fillRect(rock.x, rock.y, rock.w, rock.h);
document.querySelector("#info").textContent = "Çarpışma: " + (hits(ship, rock) ? "evet" : "hayır");
```

</details>

### Görev 2: Meteor çarpınca

Oyuncuya değen meteorlar can götürsün. `collide()` fonksiyonunu yaz:

- `game.meteors` içinden oyuncuya değenleri çıkar (`filter`) ve çıkan her meteor için `game.lives`'ı 1 azalt.
- `game.lives` `0` ya da daha az olursa `game.over = true` yap ve `#info`'ya `Oyun bitti!` yaz.

`hits` fonksiyonu hazır.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<canvas id="c" width="200" height="120"></canvas>
<p id="info"></p>
```

**CSS:**

```css
canvas{background:#e8ebf3;border-radius:8px;max-width:100%;display:block}
```

**Başlangıç kodu:**

```js
function hits(a, b) {
  return a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;
}

const game = {
  player: { x: 80, y: 80, w: 30, h: 20 },
  meteors: [
    { x: 90, y: 70, w: 15, h: 15 },
    { x: 20, y: 20, w: 15, h: 15 },
  ],
  lives: 3,
  over: false,
};

function collide() {
  // değen meteorları çıkar, can azalt, gerekirse oyunu bitir
}

collide();
document.querySelector("#info").textContent = `Can: ${game.lives}`;
```

**İpuçları:**

1. const before = game.meteors.length; önce eski sayıyı sakla.
2. game.meteors = game.meteors.filter((m) => !hits(game.player, m));
3. Azalan can: before - game.meteors.length

<details><summary>Çözüm</summary>

```js
function hits(a, b) {
  return a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;
}

const game = {
  player: { x: 80, y: 80, w: 30, h: 20 },
  meteors: [
    { x: 90, y: 70, w: 15, h: 15 },
    { x: 20, y: 20, w: 15, h: 15 },
  ],
  lives: 3,
  over: false,
};

function collide() {
  // değen meteorları çıkar, can azalt, gerekirse oyunu bitir
  const before = game.meteors.length;
  game.meteors = game.meteors.filter((m) => !hits(game.player, m));
  game.lives -= before - game.meteors.length;
  if (game.lives <= 0) {
    game.over = true;
    document.querySelector("#info").textContent = "Oyun bitti!";
  }
}

collide();
document.querySelector("#info").textContent = `Can: ${game.lives}`;
```

</details>

### Görev 3: Yeniden başla

`newGame()` fonksiyonunu yaz: her çağrıldığında **yepyeni** bir durum nesnesi döndürsün:

```js
{ score: 0, over: false, stars: [ /* 3 yıldız */ ] }
```

Yıldızlar `(40, 30)`, `(100, 70)` ve `(160, 40)` noktalarında; her birinin `w` ve `h` değeri `10`.

`#restart` düğmesine tıklanınca `game = newGame()` olsun ve `#info` `Skor: 0` yazsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<p id="info">Skor: 7 · Oyun bitti</p>
<button id="restart">Yeniden başla</button>
```

**Başlangıç kodu:**

```js
let game = { score: 7, over: true, stars: [] };

function newGame() {
  // yeni bir durum nesnesi döndür
}

// #restart tıklanınca yeniden başlat
```

**İpuçları:**

1. Nesneyi fonksiyonun içinde yaz ve return et: her çağrıda yeni bir nesne oluşur.
2. Tıklama: game = newGame(); sonra #info'yu güncelle.

<details><summary>Çözüm</summary>

```js
let game = { score: 7, over: true, stars: [] };

function newGame() {
  // yeni bir durum nesnesi döndür
  return {
    score: 0,
    over: false,
    stars: [
      { x: 40, y: 30, w: 10, h: 10 },
      { x: 100, y: 70, w: 10, h: 10 },
      { x: 160, y: 40, w: 10, h: 10 },
    ],
  };
}

// #restart tıklanınca yeniden başlat
document.querySelector("#restart").addEventListener("click", () => {
  game = newGame();
  document.querySelector("#info").textContent = `Skor: ${game.score}`;
});
```

</details>

## Challenge: Düşen yıldızlar

Yıldızlar yukarıdan düşüyor. `update()` fonksiyonunu yaz:

- Oyun bittiyse (`game.over`) hiçbir şey yapma.
- Her yıldızın `y`'sini kendi `vy`'si kadar artır.
- Tuvalin altından çıkan yıldızları (`y > canvas.height`) diziden çıkar; her biri için `game.missed`'i 1 artır.
- `game.missed` `3` ya da daha fazla olunca `game.over = true` yap ve `#info`'ya `Oyun bitti! Kaçan: 3` yaz.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<canvas id="c" width="200" height="120"></canvas>
<p id="info"></p>
```

**CSS:**

```css
canvas{background:#e8ebf3;border-radius:8px;max-width:100%;display:block}
```

**Başlangıç kodu:**

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const game = {
  stars: [
    { x: 30, y: 0, vy: 1 },
    { x: 100, y: -40, vy: 1.5 },
    { x: 160, y: -10, vy: 0.8 },
  ],
  missed: 0,
  over: false,
};

function update() {
  // düşür, kaçanları say, gerekirse bitir
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#f7df1e";
  for (const s of game.stars) ctx.fillRect(s.x, s.y, 8, 8);
}

function loop() {
  update();
  draw();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

**İpuçları:**

1. En başta: if (game.over) return;
2. Kalanlar: game.stars.filter((s) => s.y <= canvas.height)
3. Kaçan sayısı: önceki uzunluk - yeni uzunluk

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const game = {
  stars: [
    { x: 30, y: 0, vy: 1 },
    { x: 100, y: -40, vy: 1.5 },
    { x: 160, y: -10, vy: 0.8 },
  ],
  missed: 0,
  over: false,
};

function update() {
  // düşür, kaçanları say, gerekirse bitir
  if (game.over) return;
  for (const s of game.stars) {
    s.y += s.vy;
  }
  const before = game.stars.length;
  game.stars = game.stars.filter((s) => s.y <= canvas.height);
  game.missed += before - game.stars.length;
  if (game.missed >= 3) {
    game.over = true;
    document.querySelector("#info").textContent = `Oyun bitti! Kaçan: ${game.missed}`;
  }
}

function draw() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#f7df1e";
  for (const s of game.stars) ctx.fillRect(s.x, s.y, 8, 8);
}

function loop() {
  update();
  draw();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Çarpışma ve yıldız toplama**

### Yıldız Avcısı: Yıldız toplama

Gemi yıldızlara değince onları toplasın! Yıldızlar artık birer kutu: `{ x, y, w, h }`. `update()` ve `draw()` hazır.

- `hits(a, b)`: iki dikdörtgen çarpışıyor mu (AABB)?
- `collect()`: `stars` içinden gemiye değenleri çıkar, her biri için `score`'u 1 artır ve `#info`'ya `Skor: 2` biçiminde yaz. Hiç yıldız kalmayınca `#info` `Tebrikler! Bütün yıldızlar toplandı.` yazsın.
- `step()`: sırayla `update()`, `collect()` ve `draw()`'u çağırsın. Döngü `step()`'i her karede çağırıyor.

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
const info = document.querySelector("#info");

const ship = { x: 20, y: 150, w: 30, h: 20, vx: 3 };
let stars = [
  { x: 120, y: 155, w: 12, h: 12 },
  { x: 200, y: 150, w: 12, h: 12 },
  { x: 260, y: 160, w: 12, h: 12 },
];
let score = 0;

function update() {
  ship.x += ship.vx;
  if (ship.x < 0 || ship.x + ship.w > canvas.width) {
    ship.x = Math.max(0, Math.min(ship.x, canvas.width - ship.w));
    ship.vx = -ship.vx;
  }
}

function draw() {
  ctx.fillStyle = "#0b1026";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#f7df1e";
  for (const s of stars) ctx.fillRect(s.x, s.y, s.w, s.h);
  ctx.fillStyle = "#4fc3f7";
  ctx.fillRect(ship.x, ship.y, ship.w, ship.h);
}

function hits(a, b) {
  // AABB: dört koşul
  return false;
}

function collect() {
  // değen yıldızları çıkar, skoru artır, #info'yu güncelle
}

function step() {
  // update → collect → draw
}

function loop() {
  step();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
draw();
```

**İpuçları:**

1. hits: a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y
2. collect: stars = stars.filter((s) => !hits(ship, s)); ve kaç tane azaldığını score'a ekle.
3. step: update(); collect(); draw();

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#game");
const ctx = canvas.getContext("2d");
const info = document.querySelector("#info");

const ship = { x: 20, y: 150, w: 30, h: 20, vx: 3 };
let stars = [
  { x: 120, y: 155, w: 12, h: 12 },
  { x: 200, y: 150, w: 12, h: 12 },
  { x: 260, y: 160, w: 12, h: 12 },
];
let score = 0;

function update() {
  ship.x += ship.vx;
  if (ship.x < 0 || ship.x + ship.w > canvas.width) {
    ship.x = Math.max(0, Math.min(ship.x, canvas.width - ship.w));
    ship.vx = -ship.vx;
  }
}

function draw() {
  ctx.fillStyle = "#0b1026";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#f7df1e";
  for (const s of stars) ctx.fillRect(s.x, s.y, s.w, s.h);
  ctx.fillStyle = "#4fc3f7";
  ctx.fillRect(ship.x, ship.y, ship.w, ship.h);
}

function hits(a, b) {
  // AABB: dört koşul
  return a.x < b.x + b.w && a.x + a.w > b.x && a.y < b.y + b.h && a.y + a.h > b.y;
}

function collect() {
  // değen yıldızları çıkar, skoru artır, #info'yu güncelle
  const before = stars.length;
  stars = stars.filter((s) => !hits(ship, s));
  score += before - stars.length;
  if (stars.length === 0) {
    info.textContent = "Tebrikler! Bütün yıldızlar toplandı.";
  } else {
    info.textContent = `Skor: ${score}`;
  }
}

function step() {
  // update → collect → draw
  update();
  collect();
  draw();
}

function loop() {
  step();
  requestAnimationFrame(loop);
}
requestAnimationFrame(loop);
draw();
```

</details>

### Kişisel Web Sitem: Galeri kaydırıcı

Galeri fotoğrafları tek tek göstersin.

- `show()`: `#slide`'a `photos[current]` yazsın ve yalnızca `current` sıradaki `.dot`'a `active` sınıfı versin (diğerlerinden kaldırsın).
- `next()`: `current`'ı 1 artırsın; sondan sonra başa dönsün. `prev()`: 1 azaltsın; baştan önce sona gitsin. İkisi de sonra `show()`'u çağırsın.
- `#next` ve `#prev` düğmeleri bu fonksiyonları çalıştırsın.

Fotoğraf sayısını elle yazma, `photos.length` kullan.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<header><h1 id="site-title">Ada'nın Sitesi</h1><nav><a href="#">Ana sayfa</a> · <a href="#">Galeri</a> · <a href="#">İletişim</a></nav></header>
<section id="gallery"><button id="prev">‹</button><div id="slide"></div><button id="next">›</button></section>
<div id="dots"><span class="dot"></span><span class="dot"></span><span class="dot"></span><span class="dot"></span></div>
```

**CSS:**

```css
header{border-bottom:3px solid #7e57c2;margin-bottom:10px;padding-bottom:4px}#site-title{margin:0;color:#4a2f8a;font-size:22px}nav a{color:#7e57c2}#gallery{display:flex;align-items:center;gap:8px}#slide{flex:1;text-align:center;padding:24px;background:#1b1f33;color:#fff;border-radius:8px;font-size:20px}#dots{text-align:center}.dot{display:inline-block;width:10px;height:10px;border-radius:50%;background:#ccc;margin:4px}.dot.active{background:#7e57c2}
```

**Başlangıç kodu:**

```js
const photos = ["Mars gün batımı", "Jüpiter fırtınası", "Satürn halkaları", "Ay yüzeyi"];
let current = 0;

function show() {
  // #slide ve .dot'ları güncelle
}

function next() {
  // 1 ileri, sondan sonra başa
}

function prev() {
  // 1 geri, baştan önce sona
}

// düğmeleri bağla

show();
```

**İpuçları:**

1. Başa dönmek için kalan (%) işlemi: current = (current + 1) % photos.length;
2. Geri giderken negatif olmasın: (current - 1 + photos.length) % photos.length
3. dot.classList.toggle("active", i === current)

<details><summary>Çözüm</summary>

```js
const photos = ["Mars gün batımı", "Jüpiter fırtınası", "Satürn halkaları", "Ay yüzeyi"];
let current = 0;

function show() {
  // #slide ve .dot'ları güncelle
  document.querySelector("#slide").textContent = photos[current];
  document.querySelectorAll(".dot").forEach((dot, i) => {
    dot.classList.toggle("active", i === current);
  });
}

function next() {
  // 1 ileri, sondan sonra başa
  current = (current + 1) % photos.length;
  show();
}

function prev() {
  // 1 geri, baştan önce sona
  current = (current - 1 + photos.length) % photos.length;
  show();
}

// düğmeleri bağla
document.querySelector("#next").addEventListener("click", next);
document.querySelector("#prev").addEventListener("click", prev);

show();
```

</details>

### Çalışma Asistanım: Çalışma / mola döngüsü

Odak zamanlayıcısı bir **durum makinesi**: her an üç durumdan birinde. `next()` fonksiyonunu yaz:

| Şimdiki durum | Koşul | Yeni durum |
|---|---|---|
| `"calisma"` | `round < totalRounds` | `"mola"` |
| `"calisma"` | son tur (`round === totalRounds`) | `"bitti"` |
| `"mola"` | | `round` 1 artar, `"calisma"` |
| `"bitti"` | | değişmez |

Her geçişten sonra hazır olan `render()`'ı çağır. `#next` düğmesi `next()`'i çalıştırsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 class="app-title">Çalışma Asistanım</h2>
<p id="status"></p>
<p id="round"></p>
<button id="next">Sonraki</button>
```

**CSS:**

```css
.app-title{margin:0 0 8px;color:#2e7d32}#status{font-size:20px;font-weight:700}
```

**Başlangıç kodu:**

```js
let state = "calisma";
let round = 1;
let totalRounds = 3;

const labels = { calisma: "Çalışma zamanı", mola: "Mola zamanı", bitti: "Bugünlük bitti!" };
function render() {
  document.querySelector("#status").textContent = labels[state];
  document.querySelector("#round").textContent = `Tur ${round}/${totalRounds}`;
}

function next() {
  // duruma göre geçiş yap, sonra render()
}

// #next düğmesini bağla

render();
```

**İpuçları:**

1. if (state === "calisma") { ... } else if (state === "mola") { ... }
2. Çalışmadan sonra: state = round < totalRounds ? "mola" : "bitti";
3. "bitti" durumunda hiçbir şey değişmez; yalnızca render() çağrılır.

<details><summary>Çözüm</summary>

```js
let state = "calisma";
let round = 1;
let totalRounds = 3;

const labels = { calisma: "Çalışma zamanı", mola: "Mola zamanı", bitti: "Bugünlük bitti!" };
function render() {
  document.querySelector("#status").textContent = labels[state];
  document.querySelector("#round").textContent = `Tur ${round}/${totalRounds}`;
}

function next() {
  // duruma göre geçiş yap, sonra render()
  if (state === "calisma") {
    state = round < totalRounds ? "mola" : "bitti";
  } else if (state === "mola") {
    round++;
    state = "calisma";
  }
  render();
}

// #next düğmesini bağla
document.querySelector("#next").addEventListener("click", next);

render();
```

</details>

### Bilgi Yarışması: Soru akışı

Yarışma döngüsü: soru göster → cevap al → puanla → sıradaki soru → bitince sonuç. `show()` ve düğmeler hazır.

- `answer(i)`: seçilen `i` doğruysa (`questions[current].dogru`) `score`'u 1 artır, sonra `nextQuestion()`'ı çağır.
- `nextQuestion()`: `current`'ı 1 artır; soru kaldıysa `show()`, kalmadıysa `finish()`.
- `finish()`: `#question`'a `Yarışma bitti!`, `#score`'a `Puan: 2/3` biçiminde sonucu yaz ve seçenek düğmelerini gizle (`hidden = true`).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 class="quiz-title">Bilgi Yarışması</h2>
<p id="question"></p>
<div id="options"><button data-i="0"></button> <button data-i="1"></button> <button data-i="2"></button></div>
<p id="score"></p>
```

**CSS:**

```css
.quiz-title{margin:0 0 8px;color:#5e35b1}#question{font-weight:600}#options button{margin:2px}
```

**Başlangıç kodu:**

```js
let questions = [
  { soru: "Ay, hangi gezegenin uydusudur?", secenekler: ["Mars", "Dünya", "Jüpiter"], dogru: 1 },
  { soru: "Kızıl gezegen hangisidir?", secenekler: ["Venüs", "Mars", "Merkür"], dogru: 1 },
  { soru: "Halkalarıyla ünlü gezegen hangisidir?", secenekler: ["Satürn", "Mars", "Uranüs"], dogru: 0 },
];
let current = 0;
let score = 0;
const buttons = document.querySelectorAll("#options button");

function show() {
  const q = questions[current];
  document.querySelector("#question").textContent = q.soru;
  buttons.forEach((btn, i) => {
    btn.textContent = q.secenekler[i];
    btn.hidden = false;
  });
  document.querySelector("#score").textContent = `Puan: ${score}`;
}

function answer(i) {
  // doğruysa puan ver, sonra sıradaki soru
}

function nextQuestion() {
  // current++; soru kaldıysa show(), yoksa finish()
}

function finish() {
  // sonuç ekranı
}

buttons.forEach((btn) => btn.addEventListener("click", () => answer(Number(btn.dataset.i))));
show();
```

**İpuçları:**

1. answer: if (i === questions[current].dogru) score++; nextQuestion();
2. nextQuestion: current++; if (current < questions.length) show(); else finish();
3. finish: `Puan: ${score}/${questions.length}`

<details><summary>Çözüm</summary>

```js
let questions = [
  { soru: "Ay, hangi gezegenin uydusudur?", secenekler: ["Mars", "Dünya", "Jüpiter"], dogru: 1 },
  { soru: "Kızıl gezegen hangisidir?", secenekler: ["Venüs", "Mars", "Merkür"], dogru: 1 },
  { soru: "Halkalarıyla ünlü gezegen hangisidir?", secenekler: ["Satürn", "Mars", "Uranüs"], dogru: 0 },
];
let current = 0;
let score = 0;
const buttons = document.querySelectorAll("#options button");

function show() {
  const q = questions[current];
  document.querySelector("#question").textContent = q.soru;
  buttons.forEach((btn, i) => {
    btn.textContent = q.secenekler[i];
    btn.hidden = false;
  });
  document.querySelector("#score").textContent = `Puan: ${score}`;
}

function answer(i) {
  // doğruysa puan ver, sonra sıradaki soru
  if (i === questions[current].dogru) score++;
  nextQuestion();
}

function nextQuestion() {
  // current++; soru kaldıysa show(), yoksa finish()
  current++;
  if (current < questions.length) {
    show();
  } else {
    finish();
  }
}

function finish() {
  // sonuç ekranı
  document.querySelector("#question").textContent = "Yarışma bitti!";
  document.querySelector("#score").textContent = `Puan: ${score}/${questions.length}`;
  buttons.forEach((btn) => {
    btn.hidden = true;
  });
}

buttons.forEach((btn) => btn.addEventListener("click", () => answer(Number(btn.dataset.i))));
show();
```

</details>
