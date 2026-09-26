# Gün 28: Temiz kod

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** JavaScript Yıldızı  ·  **Maskot:** Kodi

**Bugünün hedefi:** Anlamlı isimler, küçük fonksiyonlar, sabitler, erken dönüş ve parçalama ile kodu düzenlemek

> JavaScript Yıldızı'nın ışığı göründü, kaptan! Usta kaptanlar kodlarını yalnızca çalışır değil, **okunur** yazar. Bugün dağınık kodu toplayıp **temiz kod** yazmayı öğreniyoruz.

![JavaScript Yıldızı](../../gorseller/javascript/bolgeler/yildiz.webp)

## Konu anlatımı

### İsimler bir şey anlatmalı

```js
// Anlaşılmıyor
const d = 7;
function c(a) { return a * 24; }

// Kendini anlatıyor
const daysLeft = 7;
function daysToHours(days) { return days * 24; }
```

- Değişken adı **ne** tuttuğunu söylesin: `score`, `playerName`.
- Doğru/yanlış tutan değişkenler soru gibi okunsun: `isReady`, `hasKey`, `canLaunch`.
- Fonksiyon adı bir **fiil** olsun: `loadTasks`, `drawShip`, `calculateScore`.
- Anlaşılmayan kısaltmalardan kaçın: `btn` herkesçe bilinir ama `plNm` bilinmez.

### Küçük fonksiyonlar, tekrarsız kod

Her fonksiyonun **tek bir işi** olsun. Bir fonksiyonu anlatırken "ve" diyorsan belki iki fonksiyondur.

Aynı kodu iki kez kopyaladıysan dur ve onu bir fonksiyona çevir. Buna **DRY** denir (Don't Repeat Yourself: kendini tekrarlama):

```js
// Tekrar
console.log("*** " + "ay".toUpperCase() + " ***");
console.log("*** " + "mars".toUpperCase() + " ***");

// Tek fonksiyon
function banner(text) {
  return `*** ${text.toUpperCase()} ***`;
}
["ay", "mars"].forEach((p) => console.log(banner(p)));
```

Artık bir değişiklik gerektiğinde tek bir yeri düzeltirsin.

### Sihirli sayılar ve erken dönüş

Kodun ortasındaki açıklamasız sayılara **sihirli sayı** denir: `if (d > 1000)` yazınca neden 1000 olduğunu kimse bilmez. Onlara isim ver. Hiç değişmeyen ayarları BÜYÜK_HARFLE yazmak yaygın bir alışkanlıktır:

```js
const MIN_FUEL = 50;
const STAR_POINTS = 10;
```

İç içe `if`'ler yerine **erken dönüş** (early return) kullan: önce sorunlu durumları eleyip fonksiyondan çık, asıl işi en sona bırak:

```js
function canLaunch(ship) {
  if (!ship) return "Gemi yok";
  if (ship.fuel < MIN_FUEL) return "Yakıt az";
  return "Kalkış!";
}
```

### Parçalama, varsayılan değer ve yorumlar

**Parçalama** (destructuring) bir nesneden ya da diziden değerleri tek satırda çıkarır:

```js
const ship = { name: "Kartal", speed: 12 };
const { name, speed } = ship;
const [first, second] = ["Ay", "Mars", "Venüs"];
```

Parametrede de kullanılır ve **varsayılan değer** alabilir:

```js
function createShip({ name = "Kaşif", speed = 10 } = {}) {
  return { name, speed };
}
createShip();              // { name: "Kaşif", speed: 10 }
createShip({ speed: 20 }); // { name: "Kaşif", speed: 20 }
```

`{ name, speed }` kısa yazımı `{ name: name, speed: speed }` demektir.

İyi bir yorum kodun **ne** yaptığını değil **neden** öyle yaptığını anlatır. `// x'i 1 artır` gereksizdir; `// 0'dan başlıyoruz çünkü ilk tur ısınma turu` işe yarar.

## Örnekler

### Önce ve sonra

```js
// Önce: ne yaptığı belli değil
function x(a, b) { return a * 10 + (b ? 50 : 0); }
console.log(x(3, true));

// Sonra: aynı iş, okunur hali
const STAR_POINTS = 10;
const BONUS_POINTS = 50;

function calculateScore(stars, hasBonus) {
  const bonus = hasBonus ? BONUS_POINTS : 0;
  return stars * STAR_POINTS + bonus;
}
console.log(calculateScore(3, true));
```

*İki satır da 80 yazar: davranış aynı, okunuş çok farklı.*

### Parçalama ve varsayılan değer

```js
const pilot = { name: "Deniz", level: 4, ship: "Kartal" };
const { name, ship } = pilot;
console.log(`${name}, ${ship} gemisinde.`);

const [gold, silver] = ["Ada", "Can", "Ece"];
console.log("Birinci:", gold, "| İkinci:", silver);

function greet({ name, level = 1 }) {
  return `Merhaba ${name}, seviye ${level}`;
}
console.log(greet(pilot));
console.log(greet({ name: "Mert" }));
```

*Mert'in seviyesi verilmediği için varsayılan değer (1) kullanıldı.*

## Görevler

### Görev 1: Sihirli sayılara isim ver

Aşağıdaki `f` çalışıyor ama ne yaptığı anlaşılmıyor: bir yolculuk için gereken yakıtı hesaplıyor. Aynı işi yapan temiz bir sürüm yaz:

- Sabitler: `FUEL_PER_KM = 3`, `LONG_TRIP_KM = 1000`, `LONG_TRIP_EXTRA = 200`
- `fuelNeeded(distanceKm)`: km başına yakıt ile çarpsın; yolculuk `LONG_TRIP_KM`'den uzunsa `LONG_TRIP_EXTRA` eklesin. İçinde 3, 1000 ya da 200 sayısı **geçmesin**; sabitleri kullan.
- Sonunda `fuelNeeded(500)` ve `fuelNeeded(2000)` sonuçlarını yazdır (1500 ve 6200).

**Başlangıç kodu:**

```js
function f(d) {
  let r = d * 3;
  if (d > 1000) {
    r = r + 200;
  }
  return r;
}

console.log(f(500));
console.log(f(2000));
```

**İpuçları:**

1. const FUEL_PER_KM = 3; gibi üç sabit yaz.
2. const extra = distanceKm > LONG_TRIP_KM ? LONG_TRIP_EXTRA : 0;

<details><summary>Çözüm</summary>

```js
const FUEL_PER_KM = 3;
const LONG_TRIP_KM = 1000;
const LONG_TRIP_EXTRA = 200;

function fuelNeeded(distanceKm) {
  const extra = distanceKm > LONG_TRIP_KM ? LONG_TRIP_EXTRA : 0;
  return distanceKm * FUEL_PER_KM + extra;
}

console.log(fuelNeeded(500));
console.log(fuelNeeded(2000));
```

</details>

### Görev 2: Tekrarı kaldır

Bu kod aynı satırı üç kez kopyalıyor. Temizle:

- `banner(name)`: `*** MARS ***` biçiminde bir metin **döndürsün** (Türkçe büyük harf: `toLocaleUpperCase("tr")`).
- Gezegenleri bir diziye koy: `const planets = ["Merkür", "Venüs", "Dünya"];`
- `forEach` ile her birini `banner` sonucuyla yazdır.

Kodda `toLocaleUpperCase` ve `console.log` yalnızca **birer kez** geçsin.

**Başlangıç kodu:**

```js
const a = "Merkür";
console.log("*** " + a.toLocaleUpperCase("tr") + " ***");
const b = "Venüs";
console.log("*** " + b.toLocaleUpperCase("tr") + " ***");
const c = "Dünya";
console.log("*** " + c.toLocaleUpperCase("tr") + " ***");
```

**İpuçları:**

1. function banner(name) { return `*** ${name.toLocaleUpperCase("tr")} ***`; }
2. planets.forEach((planet) => console.log(banner(planet)));

<details><summary>Çözüm</summary>

```js
const planets = ["Merkür", "Venüs", "Dünya"];

function banner(name) {
  return `*** ${name.toLocaleUpperCase("tr")} ***`;
}

planets.forEach((planet) => console.log(banner(planet)));
```

</details>

### Görev 3: Erken dönüş

`canLaunch` iç içe `if`'lerle dolu. Aynı sonuçları veren düz bir sürüm yaz:

- 50 için bir sabit tanımla: `MIN_FUEL`.
- Önce sorunlu durumları `return` ile ele: gemi yoksa `Gemi yok`, yakıt `MIN_FUEL`'den azsa `Yakıt az`, mürettebat yoksa (`crew` 0) `Mürettebat yok`; en sonda `Kalkış!`.
- `fuel` ve `crew`'u parçalama ile al: `const { fuel, crew } = ship;`
- Fonksiyonda hiç `else` kalmasın.

**Başlangıç kodu:**

```js
function canLaunch(ship) {
  if (ship) {
    if (ship.fuel >= 50) {
      if (ship.crew > 0) {
        return "Kalkış!";
      } else {
        return "Mürettebat yok";
      }
    } else {
      return "Yakıt az";
    }
  } else {
    return "Gemi yok";
  }
}

console.log(canLaunch({ fuel: 80, crew: 3 }));
```

**İpuçları:**

1. if (!ship) return "Gemi yok";
2. const { fuel, crew } = ship;
3. if (fuel < MIN_FUEL) return "Yakıt az";

<details><summary>Çözüm</summary>

```js
const MIN_FUEL = 50;

function canLaunch(ship) {
  if (!ship) return "Gemi yok";
  const { fuel, crew } = ship;
  if (fuel < MIN_FUEL) return "Yakıt az";
  if (crew <= 0) return "Mürettebat yok";
  return "Kalkış!";
}

console.log(canLaunch({ fuel: 80, crew: 3 }));
```

</details>

## Challenge: Varsayılan ayarlar

Bu `createShip` iki sorun taşıyor: `createShip()` hata veriyor ve `speed: 0` verince hız 10 oluyor (çünkü `0 || 10` sonucu 10!). Düzelt:

- Parametrede parçalama ve varsayılan değerler kullan: `name` için `"Kaşif"`, `speed` için `10`, `color` için `"#f7df1e"`; parametre hiç verilmezse `{}` kullanılsın.
- Kısa yazımla döndür: `return { name, speed, color };`
- Ayrıca `describeShip(ship)` yaz: parçalama ile `name` ve `speed`'i alıp `Kartal: hız 12` döndürsün.

**Başlangıç kodu:**

```js
function createShip(options) {
  const name = options.name || "Kaşif";
  const speed = options.speed || 10;
  const color = options.color || "#f7df1e";
  return { name: name, speed: speed, color: color };
}

// describeShip

console.log(createShip({ name: "Kartal" }));
```

**İpuçları:**

1. function createShip({ name = "Kaşif", speed = 10, color = "#f7df1e" } = {})
2. Sondaki = {} parametre hiç verilmezse boş nesne kullanır.
3. function describeShip({ name, speed }) { ... }

<details><summary>Çözüm</summary>

```js
function createShip({ name = "Kaşif", speed = 10, color = "#f7df1e" } = {}) {
  return { name, speed, color };
}

// describeShip
function describeShip({ name, speed }) {
  return `${name}: hız ${speed}`;
}

console.log(createShip({ name: "Kartal" }));
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Kodu düzenlemek**

### Yıldız Avcısı: Oyun kodunu düzenle

Oyunun eski puan kodu çalışıyor ama okunmuyor: `s` skor, `l` can; `"y"` yıldız, `"d"` düşman demek. Temiz bir sürüm yaz:

- Sabitler: `STAR_POINTS = 10`, `BONUS_EVERY = 50` (her 50 puanda bir can), `START_LIVES = 3`
- `collectStar(game)`: skoru `STAR_POINTS` artırsın; skor `BONUS_EVERY`'nin katı olunca bir can eklesin.
- `hitEnemy(game)`: bir can azaltsın ama can 0'ın altına inmesin.
- `isGameOver(game)`: can 0 ise `true` döndürsün.
- Fonksiyonlar dışarıdaki değişkenleri değil, aldıkları `game` nesnesini (`{ score, lives }`) değiştirsin.

En sonda `const game = { score: 0, lives: START_LIVES };` oluştur; bir yıldız topla, bir düşmana çarp ve `Skor: 10 | Can: 2` yazdır.

**Başlangıç kodu:**

```js
let s = 0;
let l = 3;
function u(t) {
  if (t == "y") {
    s = s + 10;
    if (s % 50 == 0) {
      l = l + 1;
    }
  }
  if (t == "d") {
    l = l - 1;
    if (l < 0) l = 0;
  }
}

u("y");
u("d");
console.log("Skor: " + s + " | Can: " + l);
```

**İpuçları:**

1. function collectStar(game) { game.score += STAR_POINTS; ... }
2. Can 0'ın altına inmesin: Math.max(0, game.lives - 1)
3. function isGameOver(game) { return game.lives === 0; }

<details><summary>Çözüm</summary>

```js
const STAR_POINTS = 10;
const BONUS_EVERY = 50;
const START_LIVES = 3;

function collectStar(game) {
  game.score += STAR_POINTS;
  // her BONUS_EVERY puanda bir ödül canı
  if (game.score % BONUS_EVERY === 0) game.lives += 1;
}

function hitEnemy(game) {
  game.lives = Math.max(0, game.lives - 1);
}

function isGameOver(game) {
  return game.lives === 0;
}

const game = { score: 0, lives: START_LIVES };
collectStar(game);
hitEnemy(game);
console.log(`Skor: ${game.score} | Can: ${game.lives}`);
```

</details>

### Kişisel Web Sitem: Menü kodunu düzenle

Menüyü üreten kod aynı beş satırı üç kez tekrar ediyor. Temizle:

- Bağlantıları bir diziye koy: `MENU_LINKS` (her biri `{ text, href }`).
- `createLink({ text, href })`: `link` sınıfı olan bir `<a>` oluşturup **döndürsün** (parametrede parçalama).
- `renderMenu(links)`: `#menu`'yü temizleyip her bağlantıyı eklesin.
- En sonda `renderMenu(MENU_LINKS)` çağır. Kodda `createElement` yalnızca bir kez geçsin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<header><h1 id="site-title">Kod Günlüğüm</h1><nav id="menu"></nav></header>
```

**CSS:**

```css
header{display:flex;align-items:center;gap:12px;flex-wrap:wrap}header h1{margin:0;font-size:22px}nav a{margin-right:10px}.card{border:1px solid #ccd;border-radius:8px;padding:8px 12px;margin:8px 0}.card h3{margin:0 0 4px}.tech{color:#556;font-size:14px}body.dark{background:#0b1026;color:#eef}body.dark a{color:#9cf}form{display:grid;gap:6px;max-width:320px}
```

**Başlangıç kodu:**

```js
const m = document.querySelector("#menu");
const a1 = document.createElement("a");
a1.textContent = "Ana sayfa";
a1.href = "#home";
a1.className = "link";
m.append(a1);
const a2 = document.createElement("a");
a2.textContent = "Blog";
a2.href = "#blog";
a2.className = "link";
m.append(a2);
const a3 = document.createElement("a");
a3.textContent = "Projeler";
a3.href = "#projects";
a3.className = "link";
m.append(a3);
```

**İpuçları:**

1. const MENU_LINKS = [{ text: "Ana sayfa", href: "#home" }, ...];
2. function createLink({ text, href }) { ... return link; }
3. links.forEach((link) => menu.append(createLink(link)));

<details><summary>Çözüm</summary>

```js
const MENU_LINKS = [
  { text: "Ana sayfa", href: "#home" },
  { text: "Blog", href: "#blog" },
  { text: "Projeler", href: "#projects" },
];

function createLink({ text, href }) {
  const link = document.createElement("a");
  link.textContent = text;
  link.href = href;
  link.className = "link";
  return link;
}

function renderMenu(links) {
  const menu = document.querySelector("#menu");
  menu.innerHTML = "";
  links.forEach((link) => menu.append(createLink(link)));
}

renderMenu(MENU_LINKS);
```

</details>

### Çalışma Asistanım: İstatistik kodunu düzenle

`st` fonksiyonu tamamlanan görev istatistiğini yazıyor ama okunmuyor ve boş listede `%NaN` gösteriyor. Üç küçük fonksiyona böl:

- `countDone(tasks)`: bitmiş (`done` true) görev sayısı (`filter` ile).
- `percentDone(tasks)`: yüzde (tam sayıya yuvarla). Liste boşsa erken dönüşle `0` döndürsün.
- `statsText(tasks)`: `Tamamlanan: 1/2 (%50)` metnini döndürsün (diğer iki fonksiyonu kullanarak).

**Başlangıç kodu:**

```js
function st(a) {
  let c = 0;
  for (let i = 0; i < a.length; i++) {
    if (a[i].done == true) {
      c++;
    }
  }
  return "Tamamlanan: " + c + "/" + a.length + " (%" + Math.round(c / a.length * 100) + ")";
}

const list = [{ title: "Matematik", done: true }, { title: "Fizik", done: false }];
console.log(st(list));
```

**İpuçları:**

1. tasks.filter((task) => task.done).length
2. if (tasks.length === 0) return 0;
3. Şablon metin: `Tamamlanan: ${...}/${tasks.length} (%${...})`

<details><summary>Çözüm</summary>

```js
function countDone(tasks) {
  return tasks.filter((task) => task.done).length;
}

function percentDone(tasks) {
  if (tasks.length === 0) return 0;
  return Math.round((countDone(tasks) / tasks.length) * 100);
}

function statsText(tasks) {
  return `Tamamlanan: ${countDone(tasks)}/${tasks.length} (%${percentDone(tasks)})`;
}

const list = [{ title: "Matematik", done: true }, { title: "Fizik", done: false }];
console.log(statsText(list));
```

</details>

### Bilgi Yarışması: Sonuç kodunu düzenle

Yarışmanın sonuç mesajını üreten `g` iç içe `else`'lerle dolu. Temiz bir sürüm yaz:

- Sabitler: `GREAT_PERCENT = 90`, `PASS_PERCENT = 60`
- `percent(correct, total)`: yüzdeyi tam sayı olarak döndürsün; `total` 0 ise `0`.
- `resultMessage({ correct, total })`: parçalamayla alsın, erken dönüşlerle `Harika! (%100)`, `Geçtin (%60)` ya da `Tekrar dene (%25)` döndürsün. İçinde `else` olmasın.

**Başlangıç kodu:**

```js
function g(c, t) {
  let p = Math.round(c / t * 100);
  if (p >= 90) {
    return "Harika! (%" + p + ")";
  } else {
    if (p >= 60) {
      return "Geçtin (%" + p + ")";
    } else {
      return "Tekrar dene (%" + p + ")";
    }
  }
}

console.log(g(4, 5));
```

**İpuçları:**

1. if (total === 0) return 0;
2. function resultMessage({ correct, total }) { ... }
3. if (p >= GREAT_PERCENT) return `Harika! (%${p})`;

<details><summary>Çözüm</summary>

```js
const GREAT_PERCENT = 90;
const PASS_PERCENT = 60;

function percent(correct, total) {
  if (total === 0) return 0;
  return Math.round((correct / total) * 100);
}

function resultMessage({ correct, total }) {
  const p = percent(correct, total);
  if (p >= GREAT_PERCENT) return `Harika! (%${p})`;
  if (p >= PASS_PERCENT) return `Geçtin (%${p})`;
  return `Tekrar dene (%${p})`;
}

console.log(resultMessage({ correct: 4, total: 5 }));
```

</details>
