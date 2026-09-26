# Gün 21: Canvas ile çizim

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Piksel Gezegeni  ·  **Maskot:** Kodi

**Bugünün hedefi:** canvas üzerine dikdörtgen, daire ve çizgi çizmek; bir diziden döngüyle resim çizmek

> Piksel Gezegeni'ne indin! Burada her şey minicik renkli noktalardan, yani piksellerden oluşuyor. Bugün **canvas** adlı tuvale kodla çizim yapacak ve oyun alanının ilk resmini çizeceksin.

![Piksel Gezegeni](../../gorseller/javascript/bolgeler/piksel.webp)

## Konu anlatımı

### Tuval ve fırça

HTML'deki `<canvas>` etiketi boş bir resim tuvalidir. Üzerine çizmek için önce ondan bir **fırça** (çizim bağlamı) isteriz:

```js
const canvas = document.querySelector("#game");
const ctx = canvas.getContext("2d");
```

`ctx` artık bütün çizim komutlarını bilen nesnedir. Tuvalin boyutu HTML'de `width` ve `height` ile verilir: `<canvas id="game" width="300" height="200">`. Kodda bu değerleri `canvas.width` ve `canvas.height` ile okursun.

### Koordinatlar: y aşağı doğru büyür

Tuvalde her noktanın bir `(x, y)` adresi vardır. **Sol üst köşe `(0, 0)`** noktasıdır. `x` sağa gittikçe, `y` ise **aşağı** gittikçe büyür (matematik dersindekinin tersi!).

| Nokta | x | y |
|---|---|---|
| Sol üst köşe | 0 | 0 |
| Sağ üst köşe | 300 | 0 |
| Sol alt köşe | 0 | 200 |
| Orta | 150 | 100 |

Yani bir şeyi yukarı taşımak için `y`'yi **azaltırsın**.

### Dikdörtgen, çerçeve ve silgi

Önce rengi seç, sonra çiz. `fillStyle` kendisinden sonraki bütün dolgu çizimlerini etkiler:

```js
ctx.fillStyle = "#0b1026";       // dolgu rengi
ctx.fillRect(0, 0, 300, 200);    // x, y, genişlik, yükseklik

ctx.strokeStyle = "#f7df1e";     // çizgi rengi
ctx.lineWidth = 3;
ctx.strokeRect(20, 20, 60, 40);  // içi boş çerçeve

ctx.clearRect(0, 0, 300, 200);   // bölgeyi siler (şeffaf yapar)
```

Renkleri `"#f7df1e"` gibi onaltılık (hex) kodlarla ya da `"white"` gibi adlarla yazabilirsin. Dikdörtgenin `(x, y)` noktası onun **sol üst köşesidir**.

### Daire, çizgi, yazı ve veriden çizim

Daire ve çizgiler bir **yol** (path) olarak çizilir: `beginPath()` ile başla, şekli tarif et, sonra `fill()` (doldur) ya da `stroke()` (çiz) de:

```js
ctx.beginPath();
ctx.arc(150, 100, 30, 0, Math.PI * 2); // merkez x, y, yarıçap, tam tur
ctx.fillStyle = "#ff9800";
ctx.fill();

ctx.beginPath();
ctx.moveTo(10, 190);  // kalemi buraya koy
ctx.lineTo(290, 190); // buraya kadar çiz
ctx.strokeStyle = "white";
ctx.stroke();

ctx.fillStyle = "white";
ctx.font = "16px sans-serif";
ctx.fillText("Yıldız Avcısı", 10, 20);
```

Asıl güç, resmi **veriden** çizmektir: bir dizideki her eleman için aynı komutu döngüyle çalıştırırsın. Dizi değişince resim de değişir:

```js
const stars = [{ x: 40, y: 30 }, { x: 120, y: 80 }, { x: 250, y: 50 }];
ctx.fillStyle = "#f7df1e";
for (const star of stars) {
  ctx.fillRect(star.x, star.y, 6, 6);
}
```

## Örnekler

### Gece manzarası

Sayfa:

```html
<canvas id="sky" width="300" height="160"></canvas>
```

```js
const ctx = document.querySelector("#sky").getContext("2d");

// Gökyüzü
ctx.fillStyle = "#0b1026";
ctx.fillRect(0, 0, 300, 160);

// Ay
ctx.beginPath();
ctx.arc(240, 40, 22, 0, Math.PI * 2);
ctx.fillStyle = "#fff5c0";
ctx.fill();

// Yer
ctx.fillStyle = "#2e7d32";
ctx.fillRect(0, 130, 300, 30);

// Roket: dolgu ve çerçeve
ctx.fillStyle = "#e53935";
ctx.fillRect(60, 80, 16, 50);
ctx.strokeStyle = "white";
ctx.strokeRect(60, 80, 16, 50);

// Yazı
ctx.fillStyle = "white";
ctx.font = "14px sans-serif";
ctx.fillText("Piksel Gezegeni", 10, 20);
```

*Koordinatları değiştir: roketi sağa taşımak için x'i, yukarı taşımak için y'yi azalt.*

### Veriden gökyüzü

Sayfa:

```html
<canvas id="sky" width="300" height="160"></canvas>
```

```js
const canvas = document.querySelector("#sky");
const ctx = canvas.getContext("2d");
ctx.fillStyle = "#0b1026";
ctx.fillRect(0, 0, canvas.width, canvas.height);

// 40 rastgele yıldız
ctx.fillStyle = "white";
for (let i = 0; i < 40; i++) {
  const x = Math.random() * canvas.width;
  const y = Math.random() * canvas.height;
  ctx.fillRect(x, y, 2, 2);
}

// Gezegenler bir diziden
const planets = [
  { x: 60, y: 90, r: 25, color: "#ff9800" },
  { x: 150, y: 50, r: 15, color: "#4fc3f7" },
  { x: 235, y: 100, r: 35, color: "#e53935" },
];
for (const p of planets) {
  ctx.beginPath();
  ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
  ctx.fillStyle = p.color;
  ctx.fill();
}
```

*Her çalıştırmada yıldızlar başka yerde. planets dizisine yeni bir gezegen ekle.*

## Görevler

### Görev 1: Uzay zemini

`#c` tuvalinin **tamamını** koyu lacivert (`#0b1026`) boya. Sonra üstüne `(20, 30)` noktasından başlayan, 60 genişliğinde ve 40 yüksekliğinde kırmızı (`#e53935`) bir dikdörtgen çiz.

Tuvalin boyutunu elle yazma: `canvas.width` ve `canvas.height` kullan.

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

// Önce zemin, sonra kırmızı dikdörtgen
```

**İpuçları:**

1. Önce rengi seç: ctx.fillStyle = "#0b1026";
2. Bütün tuval: ctx.fillRect(0, 0, canvas.width, canvas.height);
3. Sonra rengi değiştirip ctx.fillRect(20, 30, 60, 40);

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");

// Önce zemin, sonra kırmızı dikdörtgen
ctx.fillStyle = "#0b1026";
ctx.fillRect(0, 0, canvas.width, canvas.height);
ctx.fillStyle = "#e53935";
ctx.fillRect(20, 30, 60, 40);
```

</details>

### Görev 2: Turuncu gezegen

Merkezi `(100, 60)`, yarıçapı `30` olan turuncu (`#ff9800`) bir **daire** çiz. `beginPath`, `arc` ve `fill` kullan.

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

// Daireyi çiz
```

**İpuçları:**

1. ctx.arc(x, y, yarıçap, 0, Math.PI * 2) tam bir daire tarif eder.
2. Önce ctx.beginPath(), en sonda ctx.fill().

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");

// Daireyi çiz
ctx.beginPath();
ctx.arc(100, 60, 30, 0, Math.PI * 2);
ctx.fillStyle = "#ff9800";
ctx.fill();
```

</details>

### Görev 3: Yıldızları diziden çiz

`drawStars()` fonksiyonunu yaz:

1. Önce tuvalin tamamını `clearRect` ile temizlesin.
2. Sonra `stars` dizisindeki her yıldız için `(x, y)` noktasından başlayan 10×10 sarı (`#f7df1e`) bir kare çizsin.

Dizi değişip `drawStars()` yeniden çağrılınca resim de değişmeli.

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
const stars = [
  { x: 20, y: 20 },
  { x: 90, y: 70 },
  { x: 160, y: 30 },
];

function drawStars() {
  // temizle, sonra her yıldızı çiz
}

drawStars();
```

**İpuçları:**

1. ctx.clearRect(0, 0, canvas.width, canvas.height);
2. for (const star of stars) { ctx.fillRect(star.x, star.y, 10, 10); }

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#c");
const ctx = canvas.getContext("2d");
const stars = [
  { x: 20, y: 20 },
  { x: 90, y: 70 },
  { x: 160, y: 30 },
];

function drawStars() {
  // temizle, sonra her yıldızı çiz
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#f7df1e";
  for (const star of stars) {
    ctx.fillRect(star.x, star.y, 10, 10);
  }
}

drawStars();
```

</details>

## Challenge: Satranç tahtası

`#board` tuvaline 8×8'lik bir satranç tahtası çiz. Her kare 20×20 piksel.

- Satır ve sütun numaralarının toplamı **çiftse** kare beyaz (`#ffffff`), **tekse** koyu (`#1b1f33`) olsun.
- İç içe iki `for` döngüsü kullan: biri satırlar (`row`), biri sütunlar (`col`) için.
- Bir kare `(col * 20, row * 20)` noktasından başlar.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<canvas id="board" width="160" height="160"></canvas>
```

**CSS:**

```css
canvas{border:2px solid #1b1f33}
```

**Başlangıç kodu:**

```js
const ctx = document.querySelector("#board").getContext("2d");

// İç içe iki döngüyle 64 kare
```

**İpuçları:**

1. for (let row = 0; row < 8; row++) { for (let col = 0; col < 8; col++) { ... } }
2. Çift mi? (row + col) % 2 === 0
3. ctx.fillRect(col * 20, row * 20, 20, 20);

<details><summary>Çözüm</summary>

```js
const ctx = document.querySelector("#board").getContext("2d");

// İç içe iki döngüyle 64 kare
for (let row = 0; row < 8; row++) {
  for (let col = 0; col < 8; col++) {
    ctx.fillStyle = (row + col) % 2 === 0 ? "#ffffff" : "#1b1f33";
    ctx.fillRect(col * 20, row * 20, 20, 20);
  }
}
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Oyun alanını çizmek**

### Yıldız Avcısı: Oyun alanı

Yıldız Avcısı'nın oyun alanını çizme zamanı! `drawGame()` fonksiyonunu yaz:

1. Tuvalin tamamını `#0b1026` ile boya (bu, eski resmi de siler).
2. Gemiyi `ship` nesnesindeki `x`, `y`, `w`, `h` değerleriyle mavi (`#4fc3f7`) bir dikdörtgen olarak çiz.
3. `stars` dizisindeki her yıldızı, merkezi `(x, y)` ve yarıçapı `6` olan sarı (`#f7df1e`) bir daire olarak çiz.

Gemi ya da yıldızlar değişip `drawGame()` yeniden çağrılınca resim de değişmeli.

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

const ship = { x: 20, y: 90, w: 30, h: 20 };
const stars = [
  { x: 120, y: 40 },
  { x: 200, y: 150 },
  { x: 260, y: 70 },
];

function drawGame() {
  // 1. zemin  2. gemi  3. yıldızlar
}

drawGame();
```

**İpuçları:**

1. Zemin: ctx.fillRect(0, 0, canvas.width, canvas.height);
2. Gemi: ctx.fillRect(ship.x, ship.y, ship.w, ship.h);
3. Her yıldız için beginPath, arc(star.x, star.y, 6, 0, Math.PI * 2) ve fill.

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#game");
const ctx = canvas.getContext("2d");

const ship = { x: 20, y: 90, w: 30, h: 20 };
const stars = [
  { x: 120, y: 40 },
  { x: 200, y: 150 },
  { x: 260, y: 70 },
];

function drawGame() {
  // 1. zemin  2. gemi  3. yıldızlar
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

drawGame();
```

</details>

### Kişisel Web Sitem: Canvas afişi

Sitenin en üstüne kodla çizilmiş bir afiş (banner) ekle. `drawBanner()` fonksiyonunu yaz:

1. Tuvalin tamamını `#1b1f33` ile boya.
2. `planets` dizisindeki her gezegeni kendi `x`, `y`, `r` ve `color` değerleriyle bir daire olarak çiz.
3. `(75, 58)` noktasına beyaz renkle, `bold 20px sans-serif` yazı tipiyle `siteName` metnini yaz (`fillText`).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<header><h1 id="site-title">Ada'nın Sitesi</h1><nav><a href="#">Ana sayfa</a> · <a href="#">Galeri</a> · <a href="#">İletişim</a></nav></header>
<canvas id="banner" width="300" height="100"></canvas>
```

**CSS:**

```css
header{border-bottom:3px solid #7e57c2;margin-bottom:10px;padding-bottom:4px}#site-title{margin:0;color:#4a2f8a;font-size:22px}nav a{color:#7e57c2}canvas{display:block;max-width:100%;border-radius:8px}
```

**Başlangıç kodu:**

```js
const canvas = document.querySelector("#banner");
const ctx = canvas.getContext("2d");
const siteName = "Ada'nın Sitesi";
const planets = [
  { x: 40, y: 50, r: 25, color: "#f7df1e" },
  { x: 265, y: 30, r: 18, color: "#4fc3f7" },
  { x: 215, y: 75, r: 12, color: "#e53935" },
];

function drawBanner() {
  // zemin, gezegenler, yazı
}

drawBanner();
```

**İpuçları:**

1. Her gezegen için: ctx.beginPath(); ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2); ctx.fillStyle = p.color; ctx.fill();
2. Yazı: ctx.font = "bold 20px sans-serif"; ctx.fillText(siteName, 75, 58);

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#banner");
const ctx = canvas.getContext("2d");
const siteName = "Ada'nın Sitesi";
const planets = [
  { x: 40, y: 50, r: 25, color: "#f7df1e" },
  { x: 265, y: 30, r: 18, color: "#4fc3f7" },
  { x: 215, y: 75, r: 12, color: "#e53935" },
];

function drawBanner() {
  // zemin, gezegenler, yazı
  ctx.fillStyle = "#1b1f33";
  ctx.fillRect(0, 0, canvas.width, canvas.height);

  for (const p of planets) {
    ctx.beginPath();
    ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
    ctx.fillStyle = p.color;
    ctx.fill();
  }

  ctx.fillStyle = "white";
  ctx.font = "bold 20px sans-serif";
  ctx.fillText(siteName, 75, 58);
}

drawBanner();
```

</details>

### Çalışma Asistanım: Haftalık çalışma grafiği

Asistan, haftalık çalışma dakikalarını çubuk grafikle göstersin. `drawChart()` fonksiyonunu yaz:

- Önce tuvali `clearRect` ile temizle.
- `minutes` dizisindeki her gün için yeşil (`#4caf50`) bir çubuk çiz: `i`. çubuk `x = i * 40 + 5` noktasından başlasın, genişliği `30` olsun.
- Yükseklik ölçekli olsun: en uzun gün tam `100` piksel, diğerleri orantılı: `h = m / max * 100` (`max = Math.max(...minutes)`).
- Çubuklar tuvalin altına otursun: `y = canvas.height - h`.
- Son olarak `#total` paragrafına haftalık toplamı `Toplam: 255 dk` biçiminde yaz (sayıyı hesapla).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 class="app-title">Çalışma Asistanım</h2>
<canvas id="chart" width="280" height="120"></canvas>
<p id="total"></p>
```

**CSS:**

```css
.app-title{margin:0 0 8px;color:#2e7d32}canvas{background:#f1f8e9;border-radius:8px;display:block;max-width:100%}
```

**Başlangıç kodu:**

```js
const canvas = document.querySelector("#chart");
const ctx = canvas.getContext("2d");
// Pazartesiden pazara çalışılan dakikalar
const minutes = [30, 45, 60, 20, 50, 10, 40];

function drawChart() {
  // temizle, çubukları çiz, toplamı yaz
}

drawChart();
```

**İpuçları:**

1. const max = Math.max(...minutes);
2. Döngüde: const h = minutes[i] / max * 100; ctx.fillRect(i * 40 + 5, canvas.height - h, 30, h);
3. Toplam için reduce: minutes.reduce((sum, m) => sum + m, 0)

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#chart");
const ctx = canvas.getContext("2d");
// Pazartesiden pazara çalışılan dakikalar
const minutes = [30, 45, 60, 20, 50, 10, 40];

function drawChart() {
  // temizle, çubukları çiz, toplamı yaz
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  const max = Math.max(...minutes);
  ctx.fillStyle = "#4caf50";
  for (let i = 0; i < minutes.length; i++) {
    const h = minutes[i] / max * 100;
    ctx.fillRect(i * 40 + 5, canvas.height - h, 30, h);
  }
  const total = minutes.reduce((sum, m) => sum + m, 0);
  document.querySelector("#total").textContent = `Toplam: ${total} dk`;
}

drawChart();
```

</details>

### Bilgi Yarışması: Tur skorları grafiği

Her turda kaç doğru yapıldığını (`0`–`5`) çubuk grafikle göster. `drawScores()` fonksiyonunu yaz:

- Tuvalin tamamını açık lila (`#f3effa`) ile boya.
- `roundScores` dizisindeki her tur için mor (`#7e57c2`) bir çubuk çiz: `x = 10 + i * 50`, genişlik `40`, yükseklik `puan * 20`; çubuk alttan başlasın (`y = canvas.height - yükseklik`).
- En iyi turu `#best` paragrafına `En iyi tur: 2 (5 doğru)` biçiminde yaz. Tur numarası 1'den başlar; eşitlikte ilk tur kazanır.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 class="quiz-title">Bilgi Yarışması</h2>
<canvas id="scores" width="260" height="120"></canvas>
<p id="best"></p>
```

**CSS:**

```css
.quiz-title{margin:0 0 8px;color:#5e35b1}canvas{border-radius:8px;display:block;max-width:100%}
```

**Başlangıç kodu:**

```js
const canvas = document.querySelector("#scores");
const ctx = canvas.getContext("2d");
const roundScores = [3, 5, 2, 4];

function drawScores() {
  // zemin, çubuklar, en iyi tur
}

drawScores();
```

**İpuçları:**

1. Döngüde: const h = roundScores[i] * 20; ctx.fillRect(10 + i * 50, canvas.height - h, 40, h);
2. En iyi turun sırasını bir değişkende tut: if (roundScores[i] > roundScores[best]) best = i;
3. Tur numarası = sıra + 1

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#scores");
const ctx = canvas.getContext("2d");
const roundScores = [3, 5, 2, 4];

function drawScores() {
  // zemin, çubuklar, en iyi tur
  ctx.fillStyle = "#f3effa";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#7e57c2";
  let best = 0;
  for (let i = 0; i < roundScores.length; i++) {
    const h = roundScores[i] * 20;
    ctx.fillRect(10 + i * 50, canvas.height - h, 40, h);
    if (roundScores[i] > roundScores[best]) best = i;
  }
  document.querySelector("#best").textContent = `En iyi tur: ${best + 1} (${roundScores[best]} doğru)`;
}

drawScores();
```

</details>
