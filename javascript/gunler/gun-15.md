# Gün 15: Eleman oluşturmak

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** DOM Gezegeni  ·  **Maskot:** Kodi

**Bugünün hedefi:** createElement ile yeni elemanlar oluşturmak, diziden liste çizmek (render), eleman silmek ve dataset kullanmak

> DOM Gezegeni'nde inşaat zamanı! Şimdiye kadar sayfada var olan elemanları değiştirdin; bugün JavaScript ile sıfırdan **yeni elemanlar** üretip sayfaya ekleyeceksin.

![DOM Gezegeni](../../gorseller/javascript/bolgeler/dom.webp)

## Konu anlatımı

### createElement ve append

Yeni bir eleman üç adımda eklenir: **oluştur, doldur, ekle**.

```js
const list = document.querySelector("#cargo");
const li = document.createElement("li"); // 1) oluştur
li.textContent = "Oksijen tüpü";          // 2) doldur
li.classList.add("item");
list.append(li);                           // 3) sayfaya ekle (sona)
```

`createElement` elemanı yalnızca bellekte oluşturur; bir yere eklemeden sayfada görünmez. `append` sona, `prepend` başa ekler. Bir elemanın içine başka elemanlar da koyabilirsin: `li.append(button)`.

### remove() ve temizlemek

`el.remove()` elemanı sayfadan siler. Bir kutunun içini tamamen boşaltmak için içeriğini boş metin yapmak yeter:

```js
document.querySelector("#old").remove(); // tek elemanı sil
list.textContent = "";                    // listenin içini boşalt
```

### Diziden liste: render()

Asıl güç şurada: veriyi bir dizide tutup ekranı diziden **çizmek**. Bunu yapan fonksiyona genelde `render` (çiz) denir. Her çağrıldığında listeyi temizler ve diziden baştan kurar:

```js
const items = ["Oksijen", "Su", "Yakıt"];

function render() {
  list.textContent = ""; // önce temizle
  for (const item of items) {
    const li = document.createElement("li");
    li.textContent = item;
    list.append(li);
  }
}

render();
items.push("Kalkan"); // veri değişti...
render();             // ...ekranı yeniden çiz
```

Kural basit: **önce veriyi değiştir, sonra `render()` çağır.** Temizlemeyi unutursan her çağrıda liste bir kez daha eklenir.

### dataset: data-* nitelikleri

Bir elemanda kendi bilgini `data-` ile başlayan niteliklerde saklayabilirsin. JavaScript'te bunlara `dataset` ile ulaşılır:

```js
li.dataset.id = 7;          // HTML'de: <li data-id="7">
console.log(li.dataset.id); // "7" (her zaman metin!)
```

Tireli adlar camelCase olur: `data-max-speed` → `dataset.maxSpeed`.

Olay yetkilendirmeyle birlikte çok kullanışlıdır: tıklanan düğmenin hangi kayda ait olduğunu `e.target.dataset.index` söyler. Değer metin olduğu için sayı gerekiyorsa `Number(...)` ile çevir.

## Örnekler

### Diziden liste

Sayfa:

```html
<ul id="list"></ul>
```

```js
const planets = ["Merkür", "Venüs", "Dünya", "Mars"];
const list = document.querySelector("#list");

for (const name of planets) {
  const li = document.createElement("li");
  li.textContent = name;
  list.append(li);
}

const sun = document.createElement("li");
sun.textContent = "Güneş (merkez)";
sun.classList.add("sun");
list.prepend(sun);
console.log("Eleman sayısı:", list.children.length);
```

*planets dizisine Jüpiter'i ekleyip tekrar çalıştır.*

### render() ve silme

Sayfa:

```html
<ul id="list"></ul>
<button id="add">Rastgele yıldız ekle</button>
```

```js
const stars = ["Vega", "Sirius"];
const list = document.querySelector("#list");

function render() {
  list.textContent = "";
  stars.forEach((star, i) => {
    const li = document.createElement("li");
    li.textContent = star + " ";
    const del = document.createElement("button");
    del.textContent = "Sil";
    del.dataset.index = i;
    li.append(del);
    list.append(li);
  });
}

list.addEventListener("click", (e) => {
  if (e.target.tagName !== "BUTTON") return;
  stars.splice(Number(e.target.dataset.index), 1);
  render();
});

document.querySelector("#add").addEventListener("click", () => {
  stars.push("Yıldız " + Math.floor(Math.random() * 100));
  render();
});

render();
```

*Yıldız ekle, sonra Sil düğmelerine tıkla. Her değişiklikte dizi değişiyor ve render() listeyi baştan çiziyor.*

## Görevler

### Görev 1: İlk elemanlar

`#cargo` listesine kodla iki eleman ekle:

1. `Oksijen tüpü` yazan bir `<li>` oluştur ve `append` ile ekle.
2. `Su deposu` yazan bir `<li>` oluştur ve `prepend` ile **başa** ekle.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1>Yük Listesi</h1>
<ul id="cargo"></ul>
<p id="count"></p>
<p><input id="item-name" placeholder="Yeni yük"> <button id="add">Ekle</button></p>
```

**CSS:**

```css
#cargo li{margin:4px 0;cursor:pointer}.del{margin-left:8px;font-size:13px}#count{font-weight:bold}
```

**Başlangıç kodu:**

```js
const cargo = document.querySelector("#cargo");

// 1) Oksijen tüpü: oluştur, doldur, append

// 2) Su deposu: oluştur, doldur, prepend
```

**İpuçları:**

1. const li = document.createElement("li");
2. li.textContent = "Oksijen tüpü"; cargo.append(li);
3. İkincisi için cargo.prepend(...)

<details><summary>Çözüm</summary>

```js
const cargo = document.querySelector("#cargo");

// 1) Oksijen tüpü: oluştur, doldur, append
const oxygen = document.createElement("li");
oxygen.textContent = "Oksijen tüpü";
cargo.append(oxygen);

// 2) Su deposu: oluştur, doldur, prepend
const water = document.createElement("li");
water.textContent = "Su deposu";
cargo.prepend(water);
```

</details>

### Görev 2: Diziden liste

`render()` fonksiyonunu tamamla:

- `#cargo`'yu temizlesin,
- `items` dizisindeki her yük için bir `<li>` oluşturup eklesin,
- `#count`'a `3 yük` biçiminde yük sayısını yazsın.

Kontrol, diziye yeni yük ekleyip `render()`'ı tekrar çağıracak.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1>Yük Listesi</h1>
<ul id="cargo"></ul>
<p id="count"></p>
<p><input id="item-name" placeholder="Yeni yük"> <button id="add">Ekle</button></p>
```

**CSS:**

```css
#cargo li{margin:4px 0;cursor:pointer}.del{margin-left:8px;font-size:13px}#count{font-weight:bold}
```

**Başlangıç kodu:**

```js
const items = ["Oksijen", "Su", "Yakıt"];
const cargo = document.querySelector("#cargo");

function render() {
  // temizle, her yük için <li>, sonra #count
}

render();
```

**İpuçları:**

1. Önce temizle: cargo.textContent = "";
2. for (const item of items) { ... createElement("li") ... }
3. `${items.length} yük`

<details><summary>Çözüm</summary>

```js
const items = ["Oksijen", "Su", "Yakıt"];
const cargo = document.querySelector("#cargo");

function render() {
  // temizle, her yük için <li>, sonra #count
  cargo.textContent = "";
  for (const item of items) {
    const li = document.createElement("li");
    li.textContent = item;
    cargo.append(li);
  }
  document.querySelector("#count").textContent = `${items.length} yük`;
}

render();
```

</details>

### Görev 3: Kimlik etiketleri

Her yükün bir kimliği (`id`) var. `render()` her `<li>`'ye yükün adını yazsın ve kimliğini `li.dataset.id` ile saklasın.

Sonra `#cargo`'ya **tek** bir `click` dinleyicisi ekle: tıklanan `<li>`'nin kimliğini `#count`'a `Seçilen kimlik: 12` biçiminde yazsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1>Yük Listesi</h1>
<ul id="cargo"></ul>
<p id="count"></p>
<p><input id="item-name" placeholder="Yeni yük"> <button id="add">Ekle</button></p>
```

**CSS:**

```css
#cargo li{margin:4px 0;cursor:pointer}.del{margin-left:8px;font-size:13px}#count{font-weight:bold}
```

**Başlangıç kodu:**

```js
const parts = [
  { id: 7, name: "Oksijen" },
  { id: 12, name: "Su" },
  { id: 31, name: "Yakıt" },
];
const cargo = document.querySelector("#cargo");

function render() {
  cargo.textContent = "";
  for (const part of parts) {
    // <li> oluştur: adını yaz, dataset.id'ye kimliğini koy
  }
}

render();

// #cargo'ya tıklama dinleyicisi
```

**İpuçları:**

1. li.dataset.id = part.id;
2. cargo.addEventListener("click", (e) => { ... })
3. Tıklanan li: e.target, kimliği: e.target.dataset.id

<details><summary>Çözüm</summary>

```js
const parts = [
  { id: 7, name: "Oksijen" },
  { id: 12, name: "Su" },
  { id: 31, name: "Yakıt" },
];
const cargo = document.querySelector("#cargo");

function render() {
  cargo.textContent = "";
  for (const part of parts) {
    // <li> oluştur: adını yaz, dataset.id'ye kimliğini koy
    const li = document.createElement("li");
    li.textContent = part.name;
    li.dataset.id = part.id;
    cargo.append(li);
  }
}

render();

// #cargo'ya tıklama dinleyicisi
cargo.addEventListener("click", (e) => {
  if (e.target.tagName !== "LI") return;
  document.querySelector("#count").textContent = `Seçilen kimlik: ${e.target.dataset.id}`;
});
```

</details>

## Challenge: Ekle ve sil

Yük listesini tam çalışır hâle getir:

- `render()` her `<li>`'nin içine `Sil` yazan, `del` sınıflı bir düğme koysun; düğmenin `dataset.index`'i yükün dizideki sırası olsun.
- `#add` tıklanınca `#item-name` kutusundaki metin (boşlukları `trim()` ile temizlenmiş) `items`'a eklensin, kutu temizlensin ve liste yeniden çizilsin. Boş metin eklenmesin.
- `#cargo`'ya tek bir dinleyici ekle: bir `Sil` düğmesine tıklanınca o yük `splice` ile diziden silinsin ve liste yeniden çizilsin.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1>Yük Listesi</h1>
<ul id="cargo"></ul>
<p id="count"></p>
<p><input id="item-name" placeholder="Yeni yük"> <button id="add">Ekle</button></p>
```

**CSS:**

```css
#cargo li{margin:4px 0;cursor:pointer}.del{margin-left:8px;font-size:13px}#count{font-weight:bold}
```

**Başlangıç kodu:**

```js
const items = ["Oksijen", "Su", "Yakıt"];
const cargo = document.querySelector("#cargo");
const input = document.querySelector("#item-name");

function render() {
  cargo.textContent = "";
  items.forEach((item, i) => {
    const li = document.createElement("li");
    li.textContent = item;
    // Sil düğmesi: class "del", dataset.index = i
    cargo.append(li);
  });
  document.querySelector("#count").textContent = `${items.length} yük`;
}

render();

// Ekle düğmesi

// Sil düğmeleri (olay yetkilendirme)
```

**İpuçları:**

1. const del = document.createElement("button"); del.classList.add("del"); del.dataset.index = i; li.append(del);
2. Ekle: const name = input.value.trim(); if (name === "") return;
3. Sil: items.splice(Number(e.target.dataset.index), 1); render();

<details><summary>Çözüm</summary>

```js
const items = ["Oksijen", "Su", "Yakıt"];
const cargo = document.querySelector("#cargo");
const input = document.querySelector("#item-name");

function render() {
  cargo.textContent = "";
  items.forEach((item, i) => {
    const li = document.createElement("li");
    li.textContent = item;
    // Sil düğmesi: class "del", dataset.index = i
    const del = document.createElement("button");
    del.textContent = "Sil";
    del.classList.add("del");
    del.dataset.index = i;
    li.append(del);
    cargo.append(li);
  });
  document.querySelector("#count").textContent = `${items.length} yük`;
}

render();

// Ekle düğmesi
document.querySelector("#add").addEventListener("click", () => {
  const name = input.value.trim();
  if (name === "") return;
  items.push(name);
  input.value = "";
  render();
});

// Sil düğmeleri (olay yetkilendirme)
cargo.addEventListener("click", (e) => {
  if (!e.target.classList.contains("del")) return;
  items.splice(Number(e.target.dataset.index), 1);
  render();
});
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Envanter listesi ekranda**

### Yıldız Avcısı: Envanter ekranda

Oyun panelinde envanter görünsün. `renderInventory()` fonksiyonunu tamamla:

- `#inventory` listesini temizlesin,
- `inventory` dizisindeki her eşya için `item` sınıflı bir `<li>` oluşturup eklesin.

Önizlemede Başla'ya tıklayınca envanteri görürsün. Kontrol, envantere yeni eşya ekleyip `renderInventory()`'yi tekrar çağıracak.

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
const inventory = ["kalkan", "lazer", "harita"];

// (14. gün) Başla düğmesi oyun panelini açar
document.querySelector("#start-btn").addEventListener("click", () => {
  document.querySelector("#start-screen").classList.add("hidden");
  document.querySelector("#game-panel").classList.remove("hidden");
});

function renderInventory() {
  const list = document.querySelector("#inventory");
  // temizle, her eşya için <li class="item">
}

renderInventory();
```

**İpuçları:**

1. Önce temizle: list.textContent = "";
2. const li = document.createElement("li"); li.classList.add("item");
3. list.append(li);

<details><summary>Çözüm</summary>

```js
const inventory = ["kalkan", "lazer", "harita"];

// (14. gün) Başla düğmesi oyun panelini açar
document.querySelector("#start-btn").addEventListener("click", () => {
  document.querySelector("#start-screen").classList.add("hidden");
  document.querySelector("#game-panel").classList.remove("hidden");
});

function renderInventory() {
  const list = document.querySelector("#inventory");
  // temizle, her eşya için <li class="item">
  list.textContent = "";
  for (const thing of inventory) {
    const li = document.createElement("li");
    li.textContent = thing;
    li.classList.add("item");
    list.append(li);
  }
}

renderInventory();
```

</details>

### Kişisel Web Sitem: Proje kartları

Projelerini `projects` dizisinden kart olarak çiz. `renderProjects()` fonksiyonu:

- `#projects`'i temizlesin,
- Her proje için `card` sınıflı bir `<article>` oluştursun; içine proje adını yazan bir `<h3>` ve etiketi yazan, `tag` sınıflı bir `<p>` koysun,
- Kartı `#projects`'e eklesin.

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
const projects = [
  { title: "Hesap Makinesi", tag: "js" },
  { title: "Kedi Galerisi", tag: "html" },
  { title: "Yıldız Oyunu", tag: "js" },
];

function renderProjects() {
  const box = document.querySelector("#projects");
  // temizle, her proje için article.card > h3 + p.tag
}

renderProjects();
```

**İpuçları:**

1. const card = document.createElement("article"); card.classList.add("card");
2. h3 ve p'yi de oluştur, sonra card.append(title, tag);
3. Başta box.textContent = ""; ile temizle.

<details><summary>Çözüm</summary>

```js
const projects = [
  { title: "Hesap Makinesi", tag: "js" },
  { title: "Kedi Galerisi", tag: "html" },
  { title: "Yıldız Oyunu", tag: "js" },
];

function renderProjects() {
  const box = document.querySelector("#projects");
  // temizle, her proje için article.card > h3 + p.tag
  box.textContent = "";
  for (const p of projects) {
    const card = document.createElement("article");
    card.classList.add("card");
    const title = document.createElement("h3");
    title.textContent = p.title;
    const tag = document.createElement("p");
    tag.classList.add("tag");
    tag.textContent = p.tag;
    card.append(title, tag);
    box.append(card);
  }
}

renderProjects();
```

</details>

### Çalışma Asistanım: Yeni görev ekle

Ekle düğmesi (`#add-btn`) çalışsın. Tıklanınca:

- `#new-task` kutusundaki metni `trim()` ile al; boşsa hiçbir şey yapma.
- `task` sınıflı bir `<li>` oluştur; içine metni yazan `name` sınıflı bir `<span>` ve `Tamamla` yazan `done-btn` sınıflı bir `<button>` koy.
- `<li>`'yi `#task-list`'e ekle, kutuyu temizle, `updateSummary()` çağır.

Tamamla düğmeleri olay yetkilendirmeyle çalıştığı için yeni görevlerde de işe yarar.

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
const list = document.querySelector("#task-list");
const input = document.querySelector("#new-task");

function updateSummary() {
  const all = document.querySelectorAll(".task").length;
  const done = document.querySelectorAll(".task.done").length;
  document.querySelector("#summary").textContent = `${done}/${all} görev tamamlandı`;
}
updateSummary();

// Tamamla düğmeleri (olay yetkilendirme: yeni görevlerde de çalışır)
list.addEventListener("click", (e) => {
  if (!e.target.classList.contains("done-btn")) return;
  const li = e.target.parentElement;
  li.classList.toggle("done");
  e.target.textContent = li.classList.contains("done") ? "Geri al" : "Tamamla";
  updateSummary();
});

// Ekle düğmesi: yeni görev oluştur
```

**İpuçları:**

1. const text = input.value.trim(); if (text === "") return;
2. span ve button'u oluşturup li.append(name, btn); ile ekle.
3. Sonra list.append(li); input.value = ""; updateSummary();

<details><summary>Çözüm</summary>

```js
const list = document.querySelector("#task-list");
const input = document.querySelector("#new-task");

function updateSummary() {
  const all = document.querySelectorAll(".task").length;
  const done = document.querySelectorAll(".task.done").length;
  document.querySelector("#summary").textContent = `${done}/${all} görev tamamlandı`;
}
updateSummary();

// Tamamla düğmeleri (olay yetkilendirme: yeni görevlerde de çalışır)
list.addEventListener("click", (e) => {
  if (!e.target.classList.contains("done-btn")) return;
  const li = e.target.parentElement;
  li.classList.toggle("done");
  e.target.textContent = li.classList.contains("done") ? "Geri al" : "Tamamla";
  updateSummary();
});

// Ekle düğmesi: yeni görev oluştur
document.querySelector("#add-btn").addEventListener("click", () => {
  const text = input.value.trim();
  if (text === "") return;
  const li = document.createElement("li");
  li.classList.add("task");
  const name = document.createElement("span");
  name.classList.add("name");
  name.textContent = text;
  const btn = document.createElement("button");
  btn.classList.add("done-btn");
  btn.textContent = "Tamamla";
  li.append(name, " ", btn);
  list.append(li);
  input.value = "";
  updateSummary();
});
```

</details>

### Bilgi Yarışması: Seçenekleri oluştur

Seçenek düğmeleri artık HTML'de yok; soruya göre kodla oluşturulacak (soruların 2, 3 ya da 4 seçeneği olabilir). `renderOptions(q)` fonksiyonu:

- `#question`'a `q.text`'i yazsın, `#options`'ı temizlesin,
- Her seçenek için `option` sınıflı bir `<button>` oluştursun; metni seçenek, `dataset.index`'i sırası olsun,
- Düğmeye tıklanınca sırası `q.answer`'a eşitse `#feedback`'e `Doğru!`, değilse `Yanlış` yazsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h1>Bilgi Yarışması</h1>
<p id="question">Soru yükleniyor...</p>
<div id="options"></div>
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
const feedback = document.querySelector("#feedback");

function renderOptions(q) {
  const box = document.querySelector("#options");
  // soruyu yaz, kutuyu temizle, her seçenek için düğme oluştur
}

renderOptions(question);
```

**İpuçları:**

1. q.options.forEach((option, i) => { const btn = document.createElement("button"); ... })
2. btn.dataset.index = i; btn.classList.add("option");
3. btn.addEventListener("click", () => { ... i === q.answer ... });

<details><summary>Çözüm</summary>

```js
const question = { text: "Kızıl gezegen hangisi?", options: ["Mars", "Venüs", "Merkür"], answer: 0 };
const feedback = document.querySelector("#feedback");

function renderOptions(q) {
  const box = document.querySelector("#options");
  // soruyu yaz, kutuyu temizle, her seçenek için düğme oluştur
  document.querySelector("#question").textContent = q.text;
  box.textContent = "";
  q.options.forEach((option, i) => {
    const btn = document.createElement("button");
    btn.classList.add("option");
    btn.textContent = option;
    btn.dataset.index = i;
    btn.addEventListener("click", () => {
      feedback.textContent = i === q.answer ? "Doğru!" : "Yanlış";
    });
    box.append(btn);
  });
}

renderOptions(question);
```

</details>
