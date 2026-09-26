# Gün 25: Promise ve async/await

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Async İstasyonu  ·  **Maskot:** Kodi

**Bugünün hedefi:** Promise oluşturmak, then/catch ve async/await ile beklemek, hataları yakalamak ve Promise.all ile işleri birlikte yürütmek

> İstasyonda hiçbir iş anında bitmiyor: yakıt dolumu sürüyor, sinyaller gecikiyor. Bugün JavaScript'e **beklemeyi** öğreteceksin: Promise ve async/await ile iş bitince kaldığı yerden devam eden kod yazacaksın.

![Async İstasyonu](../../gorseller/javascript/bolgeler/istasyon.webp)

## Konu anlatımı

### Neden bekleme gerekir?

Bazı işler zaman alır: sunucudan veri gelmesi, bir dosyanın okunması, bir zamanlayıcı. JavaScript bu sırada **durup beklemez**; diğer işlere devam eder, uzun iş bitince haber alır:

```js
console.log("1. Sinyal gönderildi");
setTimeout(() => console.log("3. Cevap geldi"), 100);
console.log("2. Beklerken başka işler");
```

Çıktı sırası 1, 2, 3'tür. Bu tür işlere **asenkron** (eşzamansız) denir. Sayfa donmaz ama "bitince şunu yap" demenin düzenli bir yoluna ihtiyacımız var: **Promise**.

### Promise: bir söz

Promise, "iş bitince sana sonucu vereceğim" sözüdür. Üç hali vardır: *bekliyor* (pending), *tamamlandı* (fulfilled), *reddedildi* (rejected).

```js
function wait(ms) {
  return new Promise((resolve) => {
    setTimeout(() => resolve("hazır"), ms);
  });
}

wait(100)
  .then((result) => console.log("Sonuç:", result))
  .catch((error) => console.log("Hata:", error.message));
```

- `resolve(değer)` sözü tutar; `.then` içindeki fonksiyon o değerle çalışır.
- `reject(new Error("..."))` sözü bozar; `.catch` içindeki fonksiyon hatayla çalışır.

### async ve await

`.then` zincirleri uzayınca okumak zorlaşır. `async` bir fonksiyonun içinde `await`, Promise bitene kadar **bekler** ve sonucunu verir. Kod yukarıdan aşağı okunur:

```js
async function countdown() {
  console.log("Geri sayım...");
  await wait(100);
  console.log("Kalkış!");
  return "yörüngede";
}

const result = await countdown(); // async fonksiyon da bir Promise döndürür
```

Reddedilen bir Promise'i `await` edersen hata fırlatılır; dün öğrendiğin `try/catch` ile yakalarsın:

```js
try {
  const level = await loadLevel(7);
} catch (error) {
  console.log("Sorun:", error.message);
}
```

`await` yalnızca `async` fonksiyonların içinde (ve bu editördeki gibi en üst seviyede) kullanılabilir.

### Promise.all: birlikte bekle

Birbirini beklemesi gerekmeyen işleri sırayla beklemek zaman kaybıdır:

```js
// Sırayla: 100 + 150 = yaklaşık 250 ms
const a = await wait(100);
const b = await wait(150);

// Birlikte: yaklaşık 150 ms (en uzunu kadar)
const [x, y] = await Promise.all([wait(100), wait(150)]);
```

`Promise.all` bir Promise dizisi alır; hepsi bitince sonuçları **aynı sırayla** bir dizi olarak verir. İçlerinden biri bile reddedilirse bütünü reddedilir.

## Örnekler

### Sıra kimde?

```js
function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}


console.log("1. Sinyal gönderildi");
wait(100).then(() => console.log("3. Cevap geldi"));
console.log("2. Beklerken başka işler");
await wait(150);
console.log("4. Hepsi bitti");
```

*wait(100) satırı ikinci sırada ama çıktısı üçüncü geliyor.*

### Birlikte yükle

```js
function loadPart(name, ms) {
  return new Promise((resolve) => setTimeout(() => resolve(name + " hazır"), ms));
}

const start = Date.now();
const parts = await Promise.all([loadPart("Motor", 150), loadPart("Kanat", 100), loadPart("Kokpit", 120)]);
console.log(parts);
console.log("Süre (ms):", Date.now() - start);
```

*Toplam süre 370 değil, yaklaşık 150 ms: parçalar aynı anda yüklendi.*

## Görevler

### Görev 1: Bekleme sözü

`wait(ms)` fonksiyonunu yaz: `ms` milisaniye sonra tamamlanan bir **Promise** döndürsün (`new Promise` ve `setTimeout`).

Sonra `wait(100).then(...)` ile, bekleme bitince `Motorlar ısındı` yazdır.

**Başlangıç kodu:**

```js
function wait(ms) {
  // new Promise döndür
}

// wait(100).then(...) ile mesaj yazdır
```

**İpuçları:**

1. return new Promise((resolve) => { ... });
2. İçeride: setTimeout(resolve, ms);
3. wait(100).then(() => console.log("Motorlar ısındı"));

<details><summary>Çözüm</summary>

```js
function wait(ms) {
  // new Promise döndür
  return new Promise((resolve) => {
    setTimeout(resolve, ms);
  });
}

// wait(100).then(...) ile mesaj yazdır
wait(100).then(() => console.log("Motorlar ısındı"));
```

</details>

### Görev 2: Yakıt dolumu

`refuel()` adında bir `async` fonksiyon yaz:

1. `Dolum başladı` yazdırsın,
2. `await wait(100)` ile beklesin,
3. `Dolum bitti` yazdırsın ve `100` döndürsün (depo yüzdesi).

Sonra en altta `const fuel = await refuel();` ile çağır ve `Yakıt: 100` yazdır.

**Başlangıç kodu:**

```js
function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}


// async function refuel() { ... }

// const fuel = await refuel();
```

**İpuçları:**

1. async function refuel() { ... }
2. İçeride: await wait(100);
3. Çağırırken de bekle: const fuel = await refuel();

<details><summary>Çözüm</summary>

```js
function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}


async function refuel() {
  console.log("Dolum başladı");
  await wait(100);
  console.log("Dolum bitti");
  return 100;
}

const fuel = await refuel();
console.log("Yakıt:", fuel);
```

</details>

### Görev 3: Motor kontrolü

`checkEngine(temp)` hazır: 50 ms sonra, sıcaklık 90'dan büyükse `Motor çok sıcak!` hatasıyla **reddedilir**, değilse `Motor hazır` ile tamamlanır.

`preflight(temp)` adında bir `async` fonksiyon yaz:

- `await checkEngine(temp)` sonucunu döndürsün.
- Hata olursa `try/catch` ile yakalayıp `"Uyarı: " + error.message` döndürsün (`Uyarı: Motor çok sıcak!`).

**Başlangıç kodu:**

```js
function checkEngine(temp) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (temp > 90) reject(new Error("Motor çok sıcak!"));
      else resolve("Motor hazır");
    }, 50);
  });
}

async function preflight(temp) {
  // try / catch ile await checkEngine(temp)
}

console.log(await preflight(60));
console.log(await preflight(120));
```

**İpuçları:**

1. try { return await checkEngine(temp); } catch (error) { ... }
2. catch içinde: return "Uyarı: " + error.message;

<details><summary>Çözüm</summary>

```js
function checkEngine(temp) {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (temp > 90) reject(new Error("Motor çok sıcak!"));
      else resolve("Motor hazır");
    }, 50);
  });
}

async function preflight(temp) {
  // try / catch ile await checkEngine(temp)
  try {
    return await checkEngine(temp);
  } catch (error) {
    return "Uyarı: " + error.message;
  }
}

console.log(await preflight(60));
console.log(await preflight(120));
```

</details>

## Challenge: Paralel yükleme

`loadPart(name, ms)` hazır. `loadAll()` adında bir `async` fonksiyon yaz:

- `Motor` (150 ms), `Kanat` (100 ms) ve `Kokpit` (120 ms) parçalarını `Promise.all` ile **aynı anda** yüklesin,
- sonuç dizisini (`["Motor", "Kanat", "Kokpit"]`) döndürsün.

Sırayla beklersen 370 ms sürer; birlikte yüklersen 150 ms civarı.

**Başlangıç kodu:**

```js
function loadPart(name, ms) {
  return new Promise((resolve) => setTimeout(() => resolve(name), ms));
}

async function loadAll() {
  // Promise.all ile üç parçayı birlikte yükle
  return [];
}

const start = Date.now();
console.log(await loadAll());
console.log("Süre:", Date.now() - start, "ms");
```

**İpuçları:**

1. Promise.all bir dizi alır: Promise.all([loadPart("Motor", 150), ...])
2. const parts = await Promise.all([...]); return parts;

<details><summary>Çözüm</summary>

```js
function loadPart(name, ms) {
  return new Promise((resolve) => setTimeout(() => resolve(name), ms));
}

async function loadAll() {
  // Promise.all ile üç parçayı birlikte yükle
  const parts = await Promise.all([
    loadPart("Motor", 150),
    loadPart("Kanat", 100),
    loadPart("Kokpit", 120),
  ]);
  return parts;
}

const start = Date.now();
console.log(await loadAll());
console.log("Süre:", Date.now() - start, "ms");
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Seviye yükleme**

### Yıldız Avcısı: Seviye yükleme

Seviyeler bir sunucudan geliyormuş gibi biraz gecikmeyle yüklenecek.

- `loadLevel(n)`: bir **Promise** döndürsün. 100 ms sonra `LEVELS[n]` ile tamamlansın; böyle bir seviye yoksa `new Error("Seviye bulunamadı: 7")` ile reddedilsin (sayı `n` olsun).
- `startLevel(n)`: `async` bir fonksiyon. Önce `#info`'ya `Seviye yükleniyor…` yazsın, `await loadLevel(n)` ile beklesin, sonra `Seviye 2: 8 yıldız, hız 3` biçiminde bilgiyi yazsın. Hata olursa `#info`'ya `Hata: Seviye bulunamadı: 7` yazsın.

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
const LEVELS = {
  1: { seviye: 1, yildiz: 5, hiz: 2 },
  2: { seviye: 2, yildiz: 8, hiz: 3 },
  3: { seviye: 3, yildiz: 12, hiz: 4 },
};

function loadLevel(n) {
  // 100 ms sonra LEVELS[n] ile tamamlanan (yoksa reddedilen) bir Promise döndür
}

async function startLevel(n) {
  const info = document.querySelector("#info");
  // yükleniyor yaz, await loadLevel(n), bilgiyi yaz; hatayı yakala
}

startLevel(1);
```

**İpuçları:**

1. return new Promise((resolve, reject) => { setTimeout(() => { ... }, 100); });
2. if (LEVELS[n]) resolve(LEVELS[n]); else reject(new Error(`Seviye bulunamadı: ${n}`));
3. startLevel içinde try { const level = await loadLevel(n); ... } catch (error) { ... }

<details><summary>Çözüm</summary>

```js
const LEVELS = {
  1: { seviye: 1, yildiz: 5, hiz: 2 },
  2: { seviye: 2, yildiz: 8, hiz: 3 },
  3: { seviye: 3, yildiz: 12, hiz: 4 },
};

function loadLevel(n) {
  // 100 ms sonra LEVELS[n] ile tamamlanan (yoksa reddedilen) bir Promise döndür
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (LEVELS[n]) resolve(LEVELS[n]);
      else reject(new Error(`Seviye bulunamadı: ${n}`));
    }, 100);
  });
}

async function startLevel(n) {
  const info = document.querySelector("#info");
  // yükleniyor yaz, await loadLevel(n), bilgiyi yaz; hatayı yakala
  info.textContent = "Seviye yükleniyor…";
  try {
    const level = await loadLevel(n);
    info.textContent = `Seviye ${level.seviye}: ${level.yildiz} yıldız, hız ${level.hiz}`;
  } catch (error) {
    info.textContent = `Hata: ${error.message}`;
  }
}

startLevel(1);
```

</details>

### Kişisel Web Sitem: Yükleniyor ekranı

Site açılırken kısa bir yükleniyor ekranı göster.

- `wait(ms)`: `ms` milisaniye sonra tamamlanan bir Promise döndürsün.
- `showPage()`: `async` bir fonksiyon. Önce `#content`'i boşaltsın ve `#loader`'dan `hidden` sınıfını kaldırsın; `await wait(150)` ile beklesin; sonra `posts` dizisindeki her başlık için `#content`'e bir `<h3>` eklesin ve `#loader`'a tekrar `hidden` sınıfı versin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<header><h1 id="site-title">Ada'nın Sitesi</h1><nav><a href="#">Ana sayfa</a> · <a href="#">Galeri</a> · <a href="#">İletişim</a></nav></header>
<div id="loader" class="hidden">Yükleniyor…</div>
<main id="content"></main>
```

**CSS:**

```css
header{border-bottom:3px solid #7e57c2;margin-bottom:10px;padding-bottom:4px}#site-title{margin:0;color:#4a2f8a;font-size:22px}nav a{color:#7e57c2}.hidden{display:none}#loader{padding:12px;background:#ede7f6;border-radius:6px}#content h3{margin:6px 0}
```

**Başlangıç kodu:**

```js
const posts = ["İlk kodum", "Döngüler neden harika?", "Sitemi yayınladım"];

function wait(ms) {
  // Promise döndür
}

async function showPage() {
  // boşalt, yükleniyor göster, bekle, yazıları ekle, yükleniyor gizle
}

showPage();
```

**İpuçları:**

1. wait: return new Promise((resolve) => setTimeout(resolve, ms));
2. loader.classList.remove("hidden"); await wait(150);
3. Her başlık için document.createElement("h3") ve content.append(h3)

<details><summary>Çözüm</summary>

```js
const posts = ["İlk kodum", "Döngüler neden harika?", "Sitemi yayınladım"];

function wait(ms) {
  // Promise döndür
  return new Promise((resolve) => setTimeout(resolve, ms));
}

async function showPage() {
  // boşalt, yükleniyor göster, bekle, yazıları ekle, yükleniyor gizle
  const loader = document.querySelector("#loader");
  const content = document.querySelector("#content");
  content.innerHTML = "";
  loader.classList.remove("hidden");
  await wait(150);
  for (const title of posts) {
    const h3 = document.createElement("h3");
    h3.textContent = title;
    content.append(h3);
  }
  loader.classList.add("hidden");
}

showPage();
```

</details>

### Çalışma Asistanım: Kaydediliyor…

Kaydetme biraz zaman alıyormuş gibi davranalım.

- `saveTasks(tasks)`: bir Promise döndürsün; 100 ms sonra `tasks`'ı JSON olarak `localStorage`'da `tasks` anahtarına yazıp tamamlansın.
- `#save` tıklanınca `async` bir fonksiyon çalışsın: görevleri listedeki `<li>`'lerin metninden topla; `#status` `Kaydediliyor…` olsun ve düğme devre dışı kalsın (`disabled = true`); `await saveTasks(...)` bitince `#status` `Kaydedildi` olsun ve düğme tekrar açılsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 class="app-title">Çalışma Asistanım</h2>
<ul id="list"><li>Fizik tekrarı</li><li>Kitap okuma</li></ul>
<button id="save">Kaydet</button>
<p id="status"></p>
```

**CSS:**

```css
.app-title{margin:0 0 8px;color:#2e7d32}
```

**Başlangıç kodu:**

```js
const saveBtn = document.querySelector("#save");
const statusText = document.querySelector("#status");

function saveTasks(tasks) {
  // 100 ms sonra localStorage'a yazan bir Promise döndür
}

// #save tıklanınca: topla, Kaydediliyor…, await, Kaydedildi
```

**İpuçları:**

1. return new Promise((resolve) => { setTimeout(() => { localStorage.setItem(...); resolve(); }, 100); });
2. Dinleyici async olabilir: saveBtn.addEventListener("click", async () => { ... });
3. Görevler: Array.from(document.querySelectorAll("#list li")).map((li) => li.textContent)

<details><summary>Çözüm</summary>

```js
const saveBtn = document.querySelector("#save");
const statusText = document.querySelector("#status");

function saveTasks(tasks) {
  // 100 ms sonra localStorage'a yazan bir Promise döndür
  return new Promise((resolve) => {
    setTimeout(() => {
      localStorage.setItem("tasks", JSON.stringify(tasks));
      resolve();
    }, 100);
  });
}

// #save tıklanınca: topla, Kaydediliyor…, await, Kaydedildi
saveBtn.addEventListener("click", async () => {
  const tasks = Array.from(document.querySelectorAll("#list li")).map((li) => li.textContent);
  statusText.textContent = "Kaydediliyor…";
  saveBtn.disabled = true;
  await saveTasks(tasks);
  statusText.textContent = "Kaydedildi";
  saveBtn.disabled = false;
});
```

</details>

### Bilgi Yarışması: Sorular yükleniyor

Sorular bir sunucudan geliyormuş gibi gecikmeyle yüklensin.

- `loadQuestions()`: bir Promise döndürsün; 150 ms sonra `QUESTIONS` dizisiyle tamamlansın.
- `start()`: `async` bir fonksiyon. `#question`'a `Sorular yükleniyor…` yazsın ve `#start` düğmesini gizlesin (`hidden = true`); soruları `await` ile alsın; sonra `#question`'a ilk sorunun metnini (`soru`), `#count`'a `3 soru` biçiminde soru sayısını yazsın.
- `#start` düğmesi `start()`'ı çalıştırsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 class="quiz-title">Bilgi Yarışması</h2>
<p id="question">Hazır olduğunda başlat.</p>
<p id="count"></p>
<button id="start">Yarışmayı başlat</button>
```

**CSS:**

```css
.quiz-title{margin:0 0 8px;color:#5e35b1}#question{font-weight:600}
```

**Başlangıç kodu:**

```js
const QUESTIONS = [
  { soru: "Ay, hangi gezegenin uydusudur?", secenekler: ["Mars", "Dünya", "Jüpiter"], dogru: 1 },
  { soru: "Kızıl gezegen hangisidir?", secenekler: ["Venüs", "Mars", "Merkür"], dogru: 1 },
  { soru: "Halkalarıyla ünlü gezegen hangisidir?", secenekler: ["Satürn", "Mars", "Uranüs"], dogru: 0 },
];

function loadQuestions() {
  // 150 ms sonra QUESTIONS ile tamamlanan bir Promise döndür
}

async function start() {
  // yükleniyor yaz, düğmeyi gizle, await, ilk soruyu ve sayıyı yaz
}

// #start düğmesini bağla
```

**İpuçları:**

1. return new Promise((resolve) => { setTimeout(() => resolve(QUESTIONS), 150); });
2. const questions = await loadQuestions();
3. Sayı: `${questions.length} soru`

<details><summary>Çözüm</summary>

```js
const QUESTIONS = [
  { soru: "Ay, hangi gezegenin uydusudur?", secenekler: ["Mars", "Dünya", "Jüpiter"], dogru: 1 },
  { soru: "Kızıl gezegen hangisidir?", secenekler: ["Venüs", "Mars", "Merkür"], dogru: 1 },
  { soru: "Halkalarıyla ünlü gezegen hangisidir?", secenekler: ["Satürn", "Mars", "Uranüs"], dogru: 0 },
];

function loadQuestions() {
  // 150 ms sonra QUESTIONS ile tamamlanan bir Promise döndür
  return new Promise((resolve) => {
    setTimeout(() => resolve(QUESTIONS), 150);
  });
}

async function start() {
  // yükleniyor yaz, düğmeyi gizle, await, ilk soruyu ve sayıyı yaz
  const question = document.querySelector("#question");
  question.textContent = "Sorular yükleniyor…";
  document.querySelector("#start").hidden = true;
  const questions = await loadQuestions();
  question.textContent = questions[0].soru;
  document.querySelector("#count").textContent = `${questions.length} soru`;
}

// #start düğmesini bağla
document.querySelector("#start").addEventListener("click", start);
```

</details>
