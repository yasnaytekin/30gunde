# Gün 27: Sınıflar ve modüller

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Async İstasyonu  ·  **Maskot:** Kodi

**Bugünün hedefi:** class ile nesne kalıpları yazmak; constructor, metot, getter, extends kullanmak ve modül fikrini anlamak

> İstasyonda onlarca gemi var ve hepsinin adı, hızı, yakıtı var. Her birini tek tek yazmak yerine bir kalıp yapalım: bugün **sınıflarla (class)** bir gemi fabrikası kuruyoruz.

![Async İstasyonu](../../gorseller/javascript/bolgeler/istasyon.webp)

## Konu anlatımı

### Sınıf: nesne kalıbı

10. günde nesneleri elle yazdık. Aynı biçimde çok sayıda nesne gerekiyorsa **sınıf** (class) bir kalıp gibi çalışır:

```js
class Ship {
  constructor(name, speed) {
    this.name = name;
    this.speed = speed;
  }
}
const a = new Ship("Kartal", 10);
const b = new Ship("Şahin", 12);
console.log(a.name, b.speed);  // Kartal 12
```

- `new Ship(...)` kalıptan yeni bir nesne üretir. Bu nesneye sınıfın bir **örneği** denir.
- `constructor`, nesne üretilirken bir kez çalışır.
- `this` "şu anki nesne" demektir: `this.name = name` yeni nesneye bir özellik ekler.
- Sınıf adları büyük harfle başlar: `Ship`, `Planet`.

### Metotlar ve getter

Sınıfın içine fonksiyonlar yazarsın; başlarına `function` yazılmaz. Bunlara **metot** denir:

```js
class Ship {
  constructor(name) {
    this.name = name;
    this.fuel = 100;
  }
  fly(km) {
    this.fuel -= km / 10;
  }
  get isEmpty() {
    return this.fuel <= 0;
  }
}
const s = new Ship("Kartal");
s.fly(300);
console.log(s.fuel, s.isEmpty);  // 70 false
```

`get` ile yazılan **getter** bir özellik gibi okunur (`s.isEmpty`, parantez yok) ama her okunuşta yeniden hesaplanır.

### extends ve super

Bir sınıfı genişletip yeni bir sınıf yapabilirsin. Yeni sınıf eskisinin her şeyini **miras** alır:

```js
class CargoShip extends Ship {
  constructor(name, cargo) {
    super(name);         // önce Ship'in constructor'ı çalışır
    this.cargo = cargo;
  }
}
const c = new CargoShip("Yük-1", 40);
c.fly(100);             // Ship'ten gelen metot
```

- `super(...)` üst sınıfın constructor'ını çağırır; `this`'ten önce yazılmalı.
- `super.metot()` üst sınıftaki metodu çağırır; alt sınıfta aynı adlı bir metot yazıp onu genişletebilirsin.
- `static` ile yazılan özellik ve metotlar örneklere değil **sınıfın kendisine** aittir: `Math.max` gibi `Ship.count` diye kullanılır.

### Modüller: kodu dosyalara bölmek

Büyük projelerde her şeyi tek dosyaya yazmayız; kodu **modüllere** böleriz. Bir dosya `export` ile paylaşır, diğeri `import` ile alır:

```js
// ship.js
export class Ship { /* ... */ }
export const MAX_SPEED = 20;

// main.js
import { Ship, MAX_SPEED } from "./ship.js";
const s = new Ship("Kartal");
```

HTML'de ana dosya `<script type="module" src="main.js"></script>` ile yüklenir. Bu kursun editörü her görevde tek bir betik çalıştırdığı için görevlerde `import` kullanamayız; bütün kod tek kutuda. Ama gerçek projelerde dosyalara böleriz ve sınıflar buna çok uygundur: her sınıf kendi dosyasında yaşar.

## Örnekler

### Robot sınıfı

```js
class Robot {
  constructor(name, battery) {
    this.name = name;
    this.battery = battery;
  }

  work(hours) {
    this.battery -= hours * 10;
  }

  get status() {
    return this.battery > 20 ? "hazır" : "şarj gerekli";
  }
}

const r1 = new Robot("Tekno", 100);
const r2 = new Robot("Bip", 30);
r2.work(2);
console.log(r1.name, r1.status);
console.log(r2.name, r2.battery, r2.status);
```

*status bir getter: parantezsiz okunur ama her seferinde yeniden hesaplanır.*

### extends ve super

```js
class Ship {
  constructor(name) {
    this.name = name;
  }
  describe() {
    return `${this.name} gemisi`;
  }
}

class Explorer extends Ship {
  constructor(name, planet) {
    super(name);
    this.planet = planet;
  }
  describe() {
    return `${super.describe()}, hedef: ${this.planet}`;
  }
}

const e = new Explorer("Kaşif", "Mars");
console.log(e.describe());
console.log(e instanceof Ship);
```

*instanceof bir nesnenin hangi sınıftan geldiğini söyler. Explorer da bir Ship'tir.*

## Görevler

### Görev 1: Gezegen sınıfı

`Planet` sınıfını tamamla:

- `constructor(name, moons)`: `name` ve `moons` özelliklerini kaydetsin.
- `describe()`: `Mars: 2 uydu` biçiminde bir metin **döndürsün**.

**Başlangıç kodu:**

```js
class Planet {
  constructor(name, moons) {
    // özellikleri kaydet
  }

  describe() {
    // metni döndür
  }
}

const mars = new Planet("Mars", 2);
console.log(mars.describe());
```

**İpuçları:**

1. this.name = name;
2. return `${this.name}: ${this.moons} uydu`;

<details><summary>Çözüm</summary>

```js
class Planet {
  constructor(name, moons) {
    // özellikleri kaydet
    this.name = name;
    this.moons = moons;
  }

  describe() {
    // metni döndür
    return `${this.name}: ${this.moons} uydu`;
  }
}

const mars = new Planet("Mars", 2);
console.log(mars.describe());
```

</details>

### Görev 2: Yakıt deposu

`FuelTank` sınıfına iki şey ekle:

- `use(liters)`: istenen yakıt depoda varsa `amount`'tan düşsün ve `true` döndürsün; yoksa hiçbir şeyi değiştirmeden `false` döndürsün.
- `get percent`: deponun yüzde kaçının dolu olduğunu (`Math.round` ile tam sayı) veren bir **getter**.

**Başlangıç kodu:**

```js
class FuelTank {
  constructor(capacity) {
    this.capacity = capacity;
    this.amount = capacity;
  }

  use(liters) {
    // yeterliyse düş ve true, değilse false
  }

  get percent() {
    // yüzde kaç dolu?
  }
}

const tank = new FuelTank(200);
tank.use(50);
console.log("Doluluk: %" + tank.percent);
```

**İpuçları:**

1. use(liters) { if (liters > this.amount) return false; ... }
2. get percent() { return Math.round(...); }

<details><summary>Çözüm</summary>

```js
class FuelTank {
  constructor(capacity) {
    this.capacity = capacity;
    this.amount = capacity;
  }

  use(liters) {
    // yeterliyse düş ve true, değilse false
    if (liters > this.amount) return false;
    this.amount -= liters;
    return true;
  }

  get percent() {
    // yüzde kaç dolu?
    return Math.round((this.amount / this.capacity) * 100);
  }
}

const tank = new FuelTank(200);
tank.use(50);
console.log("Doluluk: %" + tank.percent);
```

</details>

### Görev 3: Kargo gemisi

`Ship` sınıfı hazır. Onu genişleten bir `CargoShip` sınıfı yaz:

- `constructor(name, cargo)`: `super(name)` ile `Ship`'in kurulumunu yapsın, sonra `cargo`'yu kaydetsin.
- `info()`: `Ship`'in `info()`'sunu (`super.info()`) kullanıp sonuna yükü eklesin: `Yük-1 (hız 0) - yük: 40 ton`

**Başlangıç kodu:**

```js
class Ship {
  constructor(name) {
    this.name = name;
    this.speed = 0;
  }
  info() {
    return `${this.name} (hız ${this.speed})`;
  }
}

// CargoShip sınıfını yaz
```

**İpuçları:**

1. class CargoShip extends Ship { ... }
2. constructor içinde ilk satır: super(name);
3. return `${super.info()} - yük: ${this.cargo} ton`;

<details><summary>Çözüm</summary>

```js
class Ship {
  constructor(name) {
    this.name = name;
    this.speed = 0;
  }
  info() {
    return `${this.name} (hız ${this.speed})`;
  }
}

// CargoShip sınıfını yaz
class CargoShip extends Ship {
  constructor(name, cargo) {
    super(name);
    this.cargo = cargo;
  }
  info() {
    return `${super.info()} - yük: ${this.cargo} ton`;
  }
}

const cargo = new CargoShip("Yük-1", 40);
console.log(cargo.info());
```

</details>

## Challenge: Astronot kayıtları

`Astronaut` sınıfı her yeni astronota sırayla bir numara versin:

- `static count = 0`: şimdiye kadar kaç astronot üretildiği (sınıfa ait).
- `constructor(name)`: `Astronaut.count`'u 1 artırsın, `this.id`'yi bu sayı yapsın, `name`'i kaydetsin.
- `badge()`: `#2 Can` biçiminde döndürsün.
- `static fromList(names)`: bir ad dizisinden astronot dizisi üretsin (`map`).

**Başlangıç kodu:**

```js
class Astronaut {
  // static count

  constructor(name) {
    // sayacı artır, id ve name
  }

  badge() {
    // #1 Ada
  }

  static fromList(names) {
    return [];
  }
}

const crew = Astronaut.fromList(["Ada", "Can", "Ece"]);
crew.forEach((a) => console.log(a.badge()));
```

**İpuçları:**

1. static count = 0; sınıfın içinde, metotların dışında yazılır.
2. Sayaca sınıfın adıyla ulaşılır: Astronaut.count += 1;
3. return names.map((name) => new Astronaut(name));

<details><summary>Çözüm</summary>

```js
class Astronaut {
  // static count
  static count = 0;

  constructor(name) {
    // sayacı artır, id ve name
    Astronaut.count += 1;
    this.id = Astronaut.count;
    this.name = name;
  }

  badge() {
    // #1 Ada
    return `#${this.id} ${this.name}`;
  }

  static fromList(names) {
    return names.map((name) => new Astronaut(name));
  }
}

const crew = Astronaut.fromList(["Ada", "Can", "Ece"]);
crew.forEach((a) => console.log(a.badge()));
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Gemi sınıfı**

### Yıldız Avcısı: Gemi sınıfı

Geminin bütün davranışı bir sınıfta toplansın. `Ship` sınıfını tamamla (çizim ve klavye kodu hazır):

- `constructor(x, y)`: konumu kaydetsin.
- `move(dx)`: `x`'i `dx` kadar değiştirsin ama gemi tuvalden çıkmasın: `x` en az `0`, en çok `canvas.width - SHIP_SIZE` olsun.
- `hits(star)`: yıldızın noktası (`star.x`, `star.y`) geminin karesinin içindeyse (kenarlar dahil) `true` döndürsün.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1 id="title">Yıldız Avcısı</h1>
<canvas id="game" width="300" height="150"></canvas>
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

class Ship {
  constructor(x, y) {
    // x ve y'yi sakla
  }

  move(dx) {
    // x'i değiştir, 0 ile canvas.width - SHIP_SIZE arasında tut
  }

  hits(star) {
    // yıldız karenin içinde mi?
    return false;
  }

  draw() {
    ctx.fillStyle = "#f7df1e";
    ctx.fillRect(this.x, this.y, SHIP_SIZE, SHIP_SIZE);
  }
}

const ship = new Ship(135, 110);

function render() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ship.draw();
}

document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowLeft") ship.move(-10);
  if (e.key === "ArrowRight") ship.move(10);
  render();
});

render();
```

**İpuçları:**

1. this.x = x; this.y = y;
2. Sınırlamak için: Math.min(maxX, Math.max(0, this.x + dx))
3. hits: star.x >= this.x && star.x <= this.x + SHIP_SIZE (y için de aynısı)

<details><summary>Çözüm</summary>

```js
const canvas = document.querySelector("#game");
const ctx = canvas.getContext("2d");
const SHIP_SIZE = 30;

class Ship {
  constructor(x, y) {
    this.x = x;
    this.y = y;
  }

  move(dx) {
    const maxX = canvas.width - SHIP_SIZE;
    this.x = Math.min(maxX, Math.max(0, this.x + dx));
  }

  hits(star) {
    const insideX = star.x >= this.x && star.x <= this.x + SHIP_SIZE;
    const insideY = star.y >= this.y && star.y <= this.y + SHIP_SIZE;
    return insideX && insideY;
  }

  draw() {
    ctx.fillStyle = "#f7df1e";
    ctx.fillRect(this.x, this.y, SHIP_SIZE, SHIP_SIZE);
  }
}

const ship = new Ship(135, 110);

function render() {
  ctx.clearRect(0, 0, canvas.width, canvas.height);
  ship.draw();
}

document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowLeft") ship.move(-10);
  if (e.key === "ArrowRight") ship.move(10);
  render();
});

render();
```

</details>

### Kişisel Web Sitem: ProjectCard sınıfı

Projelerin kartlarını bir sınıf üretsin. `ProjectCard` sınıfının `render()` metodunu yaz ve kartları sayfaya ekle:

- `render()` bir `<article class="card">` oluşturup **döndürsün**. İçinde: `<h3>` (başlık), `<p class="tech">` (teknolojiler virgül ve boşlukla: `Canvas, JavaScript`) ve `<a>` (`href` = `url`, metni `İncele`).
- En altta `myProjects` içindeki her kartın `render()` sonucunu `#projects`'e ekle.

Metinleri `textContent` ile yaz.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<header><h1 id="site-title">Kod Günlüğüm</h1></header>
<main><h2>Projelerim</h2>
<div id="projects"></div></main>
```

**CSS:**

```css
header{display:flex;align-items:center;gap:12px;flex-wrap:wrap}header h1{margin:0;font-size:22px}nav a{margin-right:10px}.card{border:1px solid #ccd;border-radius:8px;padding:8px 12px;margin:8px 0}.card h3{margin:0 0 4px}.tech{color:#556;font-size:14px}body.dark{background:#0b1026;color:#eef}body.dark a{color:#9cf}form{display:grid;gap:6px;max-width:320px}
```

**Başlangıç kodu:**

```js
class ProjectCard {
  constructor(title, tech, url) {
    this.title = title;
    this.tech = tech;
    this.url = url;
  }

  render() {
    // article.card oluştur; içine h3, p.tech ve a ekle; article'ı döndür
  }
}

const myProjects = [
  new ProjectCard("Yıldız Avcısı", ["Canvas", "JavaScript"], "#oyun"),
  new ProjectCard("Hava Durumu", ["fetch", "JSON"], "#hava"),
  new ProjectCard("Not Defteri", ["localStorage"], "#notlar"),
];

const box = document.querySelector("#projects");
// her kartın render() sonucunu box'a ekle
```

**İpuçları:**

1. const card = document.createElement("article"); card.className = "card";
2. Teknolojiler: this.tech.join(", ")
3. render() en sonda return card; demeli. Ekleme: box.append(project.render())

<details><summary>Çözüm</summary>

```js
class ProjectCard {
  constructor(title, tech, url) {
    this.title = title;
    this.tech = tech;
    this.url = url;
  }

  render() {
    const card = document.createElement("article");
    card.className = "card";
    const h3 = document.createElement("h3");
    h3.textContent = this.title;
    const tech = document.createElement("p");
    tech.className = "tech";
    tech.textContent = this.tech.join(", ");
    const link = document.createElement("a");
    link.href = this.url;
    link.textContent = "İncele";
    card.append(h3, tech, link);
    return card;
  }
}

const myProjects = [
  new ProjectCard("Yıldız Avcısı", ["Canvas", "JavaScript"], "#oyun"),
  new ProjectCard("Hava Durumu", ["fetch", "JSON"], "#hava"),
  new ProjectCard("Not Defteri", ["localStorage"], "#notlar"),
];

const box = document.querySelector("#projects");
// her kartın render() sonucunu box'a ekle
myProjects.forEach((project) => box.append(project.render()));
```

</details>

### Çalışma Asistanım: Task sınıfı

Görevleri bir sınıfla tutalım. Listeyi çizen kod hazır; `Task` sınıfını tamamla:

- `constructor(title)`: `title`'ı kaydetsin, `done` başlangıçta `false` olsun.
- `toggle()`: `done`'ı tersine çevirsin.
- `get label`: bitmişse `[x] Fizik tekrarı`, bitmemişse `[ ] Fizik tekrarı` döndürsün.

Sonra önizlemede bir göreve tıklayıp dene.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1>Çalışma Asistanım</h1>
<p id="count"></p>
<ul id="tasks"></ul>
```

**CSS:**

```css
li{padding:6px;cursor:pointer}li.done{text-decoration:line-through;color:#889}li.selected{outline:2px solid #3b6ef5;border-radius:4px}.big{font-size:20px;min-width:64px;min-height:48px;margin:4px}#stats,#count{font-weight:bold}form{display:flex;gap:6px}
```

**Başlangıç kodu:**

```js
class Task {
  constructor(title) {
    // title ve done
  }

  toggle() {
    // done'ı tersine çevir
  }

  get label() {
    // [x] ya da [ ] ile başlığı döndür
  }
}

const tasks = [new Task("Matematik ödevi"), new Task("Fizik tekrarı"), new Task("Kitap okuma")];
const list = document.querySelector("#tasks");

function render() {
  list.innerHTML = "";
  tasks.forEach((task) => {
    const li = document.createElement("li");
    li.textContent = task.label;
    li.classList.toggle("done", task.done === true);
    li.addEventListener("click", () => {
      task.toggle();
      render();
    });
    list.append(li);
  });
  const left = tasks.filter((t) => !t.done).length;
  document.querySelector("#count").textContent = `${left} görev kaldı`;
}

render();
```

**İpuçları:**

1. this.done = false;
2. toggle() { this.done = !this.done; }
3. get label() { const box = this.done ? "[x]" : "[ ]"; return ...; }

<details><summary>Çözüm</summary>

```js
class Task {
  constructor(title) {
    this.title = title;
    this.done = false;
  }

  toggle() {
    this.done = !this.done;
  }

  get label() {
    const box = this.done ? "[x]" : "[ ]";
    return `${box} ${this.title}`;
  }
}

const tasks = [new Task("Matematik ödevi"), new Task("Fizik tekrarı"), new Task("Kitap okuma")];
const list = document.querySelector("#tasks");

function render() {
  list.innerHTML = "";
  tasks.forEach((task) => {
    const li = document.createElement("li");
    li.textContent = task.label;
    li.classList.toggle("done", task.done === true);
    li.addEventListener("click", () => {
      task.toggle();
      render();
    });
    list.append(li);
  });
  const left = tasks.filter((t) => !t.done).length;
  document.querySelector("#count").textContent = `${left} görev kaldı`;
}

render();
```

</details>

### Bilgi Yarışması: Quiz sınıfı

Yarışmanın bütün kuralları bir sınıfta toplansın. `Quiz` sınıfında eksik üç parçayı yaz:

- `answer(index)`: seçilen şık sorunun `dogru` değerine eşitse `score`'a 10 ekleyip `true`, değilse `false` döndürsün.
- `next()`: bir sonraki soruya geçsin (`current` 1 artsın).
- `get isOver`: bütün sorular bittiyse (`current`, soru sayısına ulaştıysa) `true` döndürsün.

**Başlangıç kodu:**

```js
const questions = [
  { soru: "Ay, hangi gezegenin uydusudur?", secenekler: ["Mars", "Dünya", "Jüpiter"], dogru: 1 },
  { soru: "Kızıl gezegen olarak bilinen gezegen hangisidir?", secenekler: ["Mars", "Venüs", "Merkür"], dogru: 0 },
];

class Quiz {
  constructor(questions) {
    this.questions = questions;
    this.current = 0;
    this.score = 0;
  }

  get question() {
    return this.questions[this.current];
  }

  answer(index) {
    // doğruysa score'a 10 ekle ve true döndür, değilse false
  }

  next() {
    // sonraki soru
  }

  get isOver() {
    // sorular bitti mi?
  }
}

const quiz = new Quiz(questions);
console.log(quiz.question.soru, quiz.answer(1));
quiz.next();
console.log(quiz.question.soru, quiz.answer(2));
quiz.next();
console.log("Bitti mi?", quiz.isOver, "| Puan:", quiz.score);
```

**İpuçları:**

1. const correct = index === this.question.dogru;
2. if (correct) this.score += 10; return correct;
3. get isOver() { return this.current >= this.questions.length; }

<details><summary>Çözüm</summary>

```js
const questions = [
  { soru: "Ay, hangi gezegenin uydusudur?", secenekler: ["Mars", "Dünya", "Jüpiter"], dogru: 1 },
  { soru: "Kızıl gezegen olarak bilinen gezegen hangisidir?", secenekler: ["Mars", "Venüs", "Merkür"], dogru: 0 },
];

class Quiz {
  constructor(questions) {
    this.questions = questions;
    this.current = 0;
    this.score = 0;
  }

  get question() {
    return this.questions[this.current];
  }

  answer(index) {
    const correct = index === this.question.dogru;
    if (correct) this.score += 10;
    return correct;
  }

  next() {
    this.current += 1;
  }

  get isOver() {
    return this.current >= this.questions.length;
  }
}

const quiz = new Quiz(questions);
console.log(quiz.question.soru, quiz.answer(1));
quiz.next();
console.log(quiz.question.soru, quiz.answer(2));
quiz.next();
console.log("Bitti mi?", quiz.isOver, "| Puan:", quiz.score);
```

</details>
