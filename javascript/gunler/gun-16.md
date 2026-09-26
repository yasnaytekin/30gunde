# Gün 16: Formlar

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** DOM Gezegeni  ·  **Maskot:** Kodi

**Bugünün hedefi:** Formdan değer okumak (metin, sayı, onay kutusu, seçim listesi), doğrulamak ve hataları sayfada göstermek

> DOM Gezegeni'nin son durağındasın! Kontrol kulesi, uçuşa çıkacak her pilotun bilgilerini istiyor. Bugün **formlardan** veri almayı ve yanlış girilen bilgileri yakalamayı öğreneceksin.

![DOM Gezegeni](../../gorseller/javascript/bolgeler/dom.webp)

## Konu anlatımı

### submit olayı ve preventDefault

Formun içindeki düğmeye basınca (ya da kutudayken Enter'a basınca) form **gönderilir** ve `submit` olayı olur. Tarayıcı normalde bu anda sayfayı yeniler; yazdığın her şey kaybolur. `e.preventDefault()` bu varsayılan davranışı durdurur:

```js
const form = document.querySelector("#pilot-form");
form.addEventListener("submit", (e) => {
  e.preventDefault(); // sayfa yenilenmesin
  console.log("Form gönderildi!");
});
```

Olayı düğmeye (`click`) değil **forma** (`submit`) bağla. Böylece Enter tuşu da çalışır.

### Kutudaki değeri okumak

Bir `input`'un içindeki yazı `.value` özelliğindedir ve **her zaman metindir**, içine sayı yazılmış olsa bile:

```js
const raw = document.querySelector("#fuel").value; // "150"
const fuel = Number(raw);                          // 150
if (Number.isNaN(fuel)) {
  console.log("Bu bir sayı değil!");
}
```

- `.value.trim()` baştaki ve sondaki boşlukları siler: `"  Ada "` → `"Ada"`
- `Number("abc")` sonucu `NaN` olur; `Number.isNaN(...)` ile anlarsın.
- `Number("")` ise `0` verir. Boş kutuyu ayrıca kontrol etmeyi unutma!

### Onay kutusu ve seçim listesi

Onay kutusunda (`type="checkbox"`) önemli olan yazı değil, işaretli olup olmadığıdır: `.checked` bize `true` ya da `false` verir. Seçim listesinde (`select`) `.value`, seçili `option`'ın `value` değeridir:

```js
const ready = document.querySelector("#ready").checked;      // true / false
const crew = Number(document.querySelector("#crew").value);  // "3" → 3
```

### Doğrulama, hata mesajı ve sıfırlama

Formu kabul etmeden önce değerleri kontrol etmeye **doğrulama** denir. Hata mesajını sayfanın içinde göster ki kullanıcı neyi düzelteceğini görsün:

```js
if (name === "") {
  info.textContent = "Önce pilot adını yaz!";
  info.classList.add("error");
  return; // gerisini çalıştırma
}
info.classList.remove("error");
form.reset(); // bütün kutuları boşaltır
```

`return` olay fonksiyonundan hemen çıkar; hata varsa gerisi çalışmaz.

İpucu: Doğrulamayı `validate(...)` gibi ayrı bir fonksiyona koy. Hata varsa mesajı, yoksa boş metni `""` döndürsün. Böylece onu farklı değerlerle tek tek deneyebilirsin.

## Örnekler

### Pilot kaydı

Sayfa:

```html
<form id="f"><input id="name" placeholder="Adın"> <button>Kaydet</button></form>
<p id="info">Adını yaz, sonra Kaydet düğmesine bas.</p>
```

```js
const form = document.querySelector("#f");
const info = document.querySelector("#info");

form.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.querySelector("#name").value.trim();
  if (name === "") {
    info.textContent = "Adını yazmayı unuttun!";
    return;
  }
  info.textContent = `Hoş geldin, Kaptan ${name}!`;
  form.reset();
});
```

*Kutuyu boş bırakıp da dene.*

### Onay kutusu ve seçim listesi

Sayfa:

```html
<form id="f"><label><input type="checkbox" id="shield"> Kalkan açık</label> 
<select id="speed"><option value="1">Yavaş</option><option value="2">Normal</option><option value="3">Hızlı</option></select> <button>Uygula</button></form>
<p id="info"></p>
```

```js
const form = document.querySelector("#f");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const shield = document.querySelector("#shield").checked;
  const speed = Number(document.querySelector("#speed").value);
  console.log("Kalkan:", shield, "Hız:", speed);
  document.querySelector("#info").textContent = `Kalkan ${shield ? "açık" : "kapalı"}, hız ${speed * 100} km/sn`;
});
```

*Onay kutusunu işaretle, hızı değiştir ve Uygula'ya bas.*

## Görevler

### Görev 1: Görev kaydı

Form gönderilince:

- sayfa yenilenmesin (`preventDefault`),
- `#mission` kutusundaki görev adı boşlukları temizlenerek `#out`'a `Görev kaydedildi: Mars keşfi` biçiminde yazılsın,
- form sıfırlansın (`form.reset()`).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<form id="mission-form"><input id="mission" placeholder="Görev adı"> <button>Kaydet</button></form>
<p id="out">Henüz görev yok.</p>
```

**Başlangıç kodu:**

```js
const form = document.querySelector("#mission-form");

// submit olayını dinle
```

**İpuçları:**

1. form.addEventListener("submit", (e) => { e.preventDefault(); ... })
2. document.querySelector("#mission").value.trim()

<details><summary>Çözüm</summary>

```js
const form = document.querySelector("#mission-form");

// submit olayını dinle
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const mission = document.querySelector("#mission").value.trim();
  document.querySelector("#out").textContent = `Görev kaydedildi: ${mission}`;
  form.reset();
});
```

</details>

### Görev 2: Yakıt hesaplayıcı

Form gönderilince toplam yakıtı hesapla: `#fuel` kutusundaki sayı × `#tanks` listesinde seçilen depo sayısı.

- Sonucu `#out`'a `Toplam yakıt: 300 litre` biçiminde yaz.
- Yakıt bir sayı değilse ya da 0 veya daha küçükse `Lütfen geçerli bir sayı yaz.` yaz.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<form id="fuel-form"><label>Depo başına yakıt <input id="fuel" placeholder="ör. 150"></label> 
<label>Depo sayısı <select id="tanks"><option value="1">1</option><option value="2">2</option><option value="3">3</option></select></label> <button>Hesapla</button></form>
<p id="out"></p>
```

**Başlangıç kodu:**

```js
const form = document.querySelector("#fuel-form");
const result = document.querySelector("#out");

// submit olayını dinle, sayıları Number ile çevir
```

**İpuçları:**

1. const fuel = Number(document.querySelector("#fuel").value);
2. Number.isNaN(fuel) || fuel <= 0 ise hata mesajı yaz ve return ile çık.

<details><summary>Çözüm</summary>

```js
const form = document.querySelector("#fuel-form");
const result = document.querySelector("#out");

// submit olayını dinle, sayıları Number ile çevir
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const fuel = Number(document.querySelector("#fuel").value);
  const tanks = Number(document.querySelector("#tanks").value);
  if (Number.isNaN(fuel) || fuel <= 0) {
    result.textContent = "Lütfen geçerli bir sayı yaz.";
    return;
  }
  result.textContent = `Toplam yakıt: ${fuel * tanks} litre`;
});
```

</details>

### Görev 3: Kalkış onayı

Form gönderilince:

- `#ready` onay kutusu işaretli **değilse** `#out`'a `Önce güvenlik kontrolünü onayla!` yaz ve `#out`'a `error` sınıfını ekle.
- İşaretliyse `Kalkış onaylandı: 3 kişilik ekip` yaz (sayı `#crew` listesinden gelsin) ve `error` sınıfını kaldır.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<form id="launch-form"><label><input type="checkbox" id="ready"> Güvenlik kontrolü tamam</label><br>
<label>Ekip: <select id="crew"><option value="2">2 kişi</option><option value="3">3 kişi</option><option value="4">4 kişi</option></select></label> <button>Kalkış</button></form>
<p id="out"></p>
```

**CSS:**

```css
.error{color:#c0392b;font-weight:600}
```

**Başlangıç kodu:**

```js
const form = document.querySelector("#launch-form");
const result = document.querySelector("#out");

// submit olayını dinle; onay kutusu için .checked
```

**İpuçları:**

1. document.querySelector("#ready").checked true ya da false verir.
2. if (!ready) { ... return; }

<details><summary>Çözüm</summary>

```js
const form = document.querySelector("#launch-form");
const result = document.querySelector("#out");

// submit olayını dinle; onay kutusu için .checked
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const ready = document.querySelector("#ready").checked;
  const crew = document.querySelector("#crew").value;
  if (!ready) {
    result.textContent = "Önce güvenlik kontrolünü onayla!";
    result.classList.add("error");
    return;
  }
  result.textContent = `Kalkış onaylandı: ${crew} kişilik ekip`;
  result.classList.remove("error");
});
```

</details>

## Challenge: Kayıt formu

Kayıt formunu doğrula. Form gönderilince bütün hataları bul ve her birini `#errors` listesine ayrı bir `<li>` olarak ekle (önce listeyi temizle):

- Kullanıcı adı (boşlukları temizlenmiş) 3 ile 12 harf arasında değilse: `Kullanıcı adı 3-12 harf olmalı.`
- Yaş 10 ile 99 arasında tam sayı değilse: `Yaş 10 ile 99 arasında bir sayı olmalı.`

Hata yoksa `#out`'a `Kayıt tamam, Ada!` yaz ve formu sıfırla. Hata varsa `#out` boş kalsın.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<form id="signup"><input id="username" placeholder="Kullanıcı adı"> <input id="age" placeholder="Yaş"> <button>Kaydol</button></form>
<ul id="errors"></ul>
<p id="out"></p>
```

**CSS:**

```css
#errors{color:#c0392b}
```

**Başlangıç kodu:**

```js
const form = document.querySelector("#signup");
const errorList = document.querySelector("#errors");
const result = document.querySelector("#out");

// submit olayını dinle: hataları bir diziye topla, sonra listede göster
```

**İpuçları:**

1. const errors = []; hata buldukça errors.push("...")
2. Listeyi temizlemek için: errorList.innerHTML = "";
3. Tam sayı mı? Number.isInteger(age)

<details><summary>Çözüm</summary>

```js
const form = document.querySelector("#signup");
const errorList = document.querySelector("#errors");
const result = document.querySelector("#out");

// submit olayını dinle: hataları bir diziye topla, sonra listede göster
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const username = document.querySelector("#username").value.trim();
  const age = Number(document.querySelector("#age").value);
  const errors = [];
  if (username.length < 3 || username.length > 12) {
    errors.push("Kullanıcı adı 3-12 harf olmalı.");
  }
  if (!Number.isInteger(age) || age < 10 || age > 99) {
    errors.push("Yaş 10 ile 99 arasında bir sayı olmalı.");
  }
  errorList.innerHTML = "";
  for (const error of errors) {
    const li = document.createElement("li");
    li.textContent = error;
    errorList.append(li);
  }
  if (errors.length === 0) {
    result.textContent = `Kayıt tamam, ${username}!`;
    form.reset();
  } else {
    result.textContent = "";
  }
});
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Pilot adı formu**

### Yıldız Avcısı: Pilot adı formu

Oyun başlamadan önce pilotun adını alalım. `#pilot-form` gönderilince:

- Sayfa yenilenmesin.
- Ad (boşlukları temizlenmiş) boşsa `#info`'ya `Önce pilot adını yaz!` yaz ve `error` sınıfını ekle.
- Değilse adı `pilotName` değişkenine koy, `#info`'ya `Hazır ol, Kaptan Ada!` yaz, `error` sınıfını kaldır ve formu sıfırla.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 id="title">Yıldız Avcısı</h2>
<form id="pilot-form"><input id="pilot-name" placeholder="Pilot adı" autocomplete="off"> <button>Başla</button></form>
<p id="info">Pilot adını yaz ve başla.</p>
<p id="hud">Skor: <span id="score">0</span> · Süre: <span id="time">10</span> · En yüksek: <span id="best">0</span></p>
<div id="field"><div id="ship"></div></div>
<div id="colors"><button data-color="#f7df1e">Sarı</button> <button data-color="#4dd0e1">Turkuaz</button> <button data-color="#ff6b6b">Kırmızı</button></div>
```

**CSS:**

```css
:root{--ship-color:#f7df1e}#title{margin:0 0 6px;color:#0b1026}#info.error{color:#c0392b;font-weight:600}#hud{margin:4px 0}#field{position:relative;width:300px;height:70px;background:#0b1026;border-radius:8px;overflow:hidden}#field.hit{background:#8e1b2b}#ship{position:absolute;left:0;bottom:10px;width:30px;height:30px;border-radius:50% 50% 6px 6px;background:var(--ship-color)}#colors{margin-top:8px}
```

**Başlangıç kodu:**

```js
const form = document.querySelector("#pilot-form");
const info = document.querySelector("#info");
let pilotName = "";

// submit olayını dinle
```

**İpuçları:**

1. const name = document.querySelector("#pilot-name").value.trim();
2. Boşsa: info.classList.add("error"); return;
3. Başarılıysa: pilotName = name; ... form.reset();

<details><summary>Çözüm</summary>

```js
const form = document.querySelector("#pilot-form");
const info = document.querySelector("#info");
let pilotName = "";

// submit olayını dinle
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.querySelector("#pilot-name").value.trim();
  if (name === "") {
    info.textContent = "Önce pilot adını yaz!";
    info.classList.add("error");
    return;
  }
  pilotName = name;
  info.textContent = `Hazır ol, Kaptan ${pilotName}!`;
  info.classList.remove("error");
  form.reset();
});
```

</details>

### Kişisel Web Sitem: İletişim formu

Sitene bir iletişim formu ekliyoruz. Önce `validateContact(name, email)` fonksiyonunu yaz:

- `name` boşsa `"Adını yazmalısın."` döndürsün,
- `email` içinde `@` ya da `.` yoksa `"Geçerli bir e-posta yaz."` döndürsün,
- sorun yoksa `""` (boş metin) döndürsün.

Sonra `#contact` gönderilince ad ve e-postayı (boşlukları temizleyerek) oku. Hata varsa mesajı `#form-msg`'ye yaz ve `error` sınıfını ekle. Yoksa `Teşekkürler, Ada! Mesajın alındı.` yaz, `error`'u kaldır ve formu sıfırla.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<header id="top"><h2 id="site-title">Deniz Yıldız</h2> <input id="search" placeholder="Sitede ara ( / )" autocomplete="off"> <span id="clock">--:--:--</span></header>
<nav id="accents"><button data-accent="#f7df1e">Sarı</button> <button data-accent="#26c6da">Turkuaz</button> <button data-accent="#b388ff">Mor</button> <button id="theme-btn">Tema değiştir</button></nav>
<form id="contact"><input id="c-name" placeholder="Adın" autocomplete="off"> <input id="c-email" placeholder="E-posta adresin" autocomplete="off"> <button>Gönder</button></form>
<p id="form-msg"></p>
```

**CSS:**

```css
:root{--accent:#f7df1e}body.dark{background:#0b1026;color:#eef1ff}#site-title{display:inline-block;margin:0 8px 6px 0;border-bottom:4px solid var(--accent)}#clock{font-family:monospace;margin-left:8px}nav{margin:6px 0}nav button.active{outline:3px solid var(--accent)}#contact input{margin:4px 4px 4px 0}#form-msg.error{color:#c0392b;font-weight:600}
```

**Başlangıç kodu:**

```js
const form = document.querySelector("#contact");
const msg = document.querySelector("#form-msg");

function validateContact(name, email) {
  // Hata varsa mesajı, yoksa "" döndür
}

// submit olayını dinle
```

**İpuçları:**

1. if (name === "") return "Adını yazmalısın.";
2. email.includes("@") içinde @ var mı diye bakar.
3. Olayda: const error = validateContact(name, email);

<details><summary>Çözüm</summary>

```js
const form = document.querySelector("#contact");
const msg = document.querySelector("#form-msg");

function validateContact(name, email) {
  // Hata varsa mesajı, yoksa "" döndür
  if (name === "") return "Adını yazmalısın.";
  if (!email.includes("@") || !email.includes(".")) return "Geçerli bir e-posta yaz.";
  return "";
}

// submit olayını dinle
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.querySelector("#c-name").value.trim();
  const email = document.querySelector("#c-email").value.trim();
  const error = validateContact(name, email);
  if (error !== "") {
    msg.textContent = error;
    msg.classList.add("error");
    return;
  }
  msg.textContent = `Teşekkürler, ${name}! Mesajın alındı.`;
  msg.classList.remove("error");
  form.reset();
});
```

</details>

### Çalışma Asistanım: Yeni görev formu

Boş ya da çok uzun görevler listeye girmesin. Önce `validateTask(text)` fonksiyonunu yaz:

- `text` boşsa `"Görev boş olamaz."`
- 40 karakterden uzunsa `"Görev en fazla 40 karakter olabilir."`
- sorun yoksa `""`

Sonra `#task-form` gönderilince kutudaki metni (boşlukları temizleyerek) doğrula. Hata varsa `#task-msg`'ye yaz ve `error` sınıfını ekle. Yoksa mesajı temizle, `error`'u kaldır, `addTask(text)` ile görevi ekle ve formu sıfırla.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 id="app-title">Çalışma Asistanım</h2>
<form id="task-form"><input id="task-input" placeholder="Yeni görev" autocomplete="off"> <button>Ekle</button></form>
<p id="task-msg"></p>
<ul id="task-list"></ul>
<div id="progress"><div id="progress-bar"></div></div> <span id="progress-text">0 / 0</span>
<p id="focus"><strong id="focus-time">25:00</strong> <button id="focus-start">Başlat</button> <button id="focus-pause">Duraklat</button> <span id="focus-msg"></span></p>
```

**CSS:**

```css
#app-title{margin:0 0 6px}#task-msg.error{color:#c0392b;font-weight:600}#task-list li{cursor:pointer;padding:2px 0}#task-list li.done{text-decoration:line-through;opacity:.55}#progress{display:inline-block;vertical-align:middle;width:200px;height:10px;background:#e3e6f0;border-radius:5px;overflow:hidden}#progress-bar{width:var(--progress,0%);height:100%;background:#43a047}#focus-time{font-family:monospace;font-size:20px}
```

**Başlangıç kodu:**

```js
const form = document.querySelector("#task-form");
const input = document.querySelector("#task-input");
const msg = document.querySelector("#task-msg");
const list = document.querySelector("#task-list");

function addTask(text) {
  const li = document.createElement("li");
  li.textContent = text;
  list.append(li);
}

function validateTask(text) {
  // Hata varsa mesajı, yoksa "" döndür
}

// submit olayını dinle
```

**İpuçları:**

1. if (text.length > 40) return "Görev en fazla 40 karakter olabilir.";
2. Olayda: const error = validateTask(input.value.trim());

<details><summary>Çözüm</summary>

```js
const form = document.querySelector("#task-form");
const input = document.querySelector("#task-input");
const msg = document.querySelector("#task-msg");
const list = document.querySelector("#task-list");

function addTask(text) {
  const li = document.createElement("li");
  li.textContent = text;
  list.append(li);
}

function validateTask(text) {
  // Hata varsa mesajı, yoksa "" döndür
  if (text === "") return "Görev boş olamaz.";
  if (text.length > 40) return "Görev en fazla 40 karakter olabilir.";
  return "";
}

// submit olayını dinle
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const text = input.value.trim();
  const error = validateTask(text);
  if (error !== "") {
    msg.textContent = error;
    msg.classList.add("error");
    return;
  }
  msg.textContent = "";
  msg.classList.remove("error");
  addTask(text);
  form.reset();
});
```

</details>

### Bilgi Yarışması: Yarışmacı formu

Yarışmaya katılan herkes adını yazsın. `#player-form` gönderilince:

- Ad (boşlukları temizlenmiş) 2 harften kısaysa `#welcome`'a `İsim en az 2 harf olmalı.` yaz ve `error` sınıfını ekle.
- Değilse adı `playerName`'e koy, `#welcome`'a `Hoş geldin, Ada! Bol şans.` yaz, `error`'u kaldır ve formu gizle (`form.hidden = true`).

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 id="quiz-title">Bilgi Yarışması</h2>
<form id="player-form"><input id="player-name" placeholder="Yarışmacı adı" autocomplete="off"> <button>Katıl</button></form>
<p id="welcome"></p>
<p id="question">Ay, hangi gezegenin uydusudur?</p>
<div id="options"><button class="option">1) Mars</button> <button class="option">2) Dünya</button> <button class="option">3) Jüpiter</button></div>
<p id="feedback"></p>
<p id="status">Puan: <span id="score">0</span> · Süre: <span id="time">10</span> · Rekor: <span id="best">0</span></p>
```

**CSS:**

```css
#quiz-title{margin:0 0 6px}#welcome.error{color:#c0392b;font-weight:600}.option{margin:2px;padding:6px 10px;border:1px solid #9aa3c0;border-radius:6px;background:#f4f6fb;color:#1b1f33}.option.correct{background:#2e7d32;color:#fff}.option.wrong{background:#c62828;color:#fff}
```

**Başlangıç kodu:**

```js
const form = document.querySelector("#player-form");
const welcome = document.querySelector("#welcome");
let playerName = "";

// submit olayını dinle
```

**İpuçları:**

1. if (name.length < 2) { ... return; }
2. form.hidden = true; formu gizler.

<details><summary>Çözüm</summary>

```js
const form = document.querySelector("#player-form");
const welcome = document.querySelector("#welcome");
let playerName = "";

// submit olayını dinle
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.querySelector("#player-name").value.trim();
  if (name.length < 2) {
    welcome.textContent = "İsim en az 2 harf olmalı.";
    welcome.classList.add("error");
    return;
  }
  playerName = name;
  welcome.textContent = `Hoş geldin, ${playerName}! Bol şans.`;
  welcome.classList.remove("error");
  form.hidden = true;
});
```

</details>
