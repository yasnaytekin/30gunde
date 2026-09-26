# Gün 24: Hatalar ve hata ayıklama

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Async İstasyonu  ·  **Maskot:** Kodi

**Bugünün hedefi:** hata türlerini tanımak, try/catch/finally ile hataları yakalamak, throw ile kendi hatanı fırlatmak ve hata ayıklamak

> Async İstasyonu'na kenetlendin! İstasyonun bilgisayarı arada bir kırmızı alarmlar veriyor. Panik yok: bugün **hata mesajlarını okumayı**, hataları yakalamayı ve kendi hatalarını fırlatmayı öğreneceksin.

![Async İstasyonu](../../gorseller/javascript/bolgeler/istasyon.webp)

## Konu anlatımı

### Hata mesajını oku

Her hata mesajının üç parçası vardır: **tür**, **açıklama** ve **satır numarası**. En sık göreceğin türler:

| Tür | Ne demek? | Örnek |
|---|---|---|
| `ReferenceError` | Böyle bir isim yok (yazım hatası ya da tanımlanmamış) | `consle.log(1)` |
| `TypeError` | Değer, yapmak istediğin işe uygun değil | `undefined.length`, `5()` |
| `SyntaxError` | Kod JavaScript kurallarına uymuyor ya da metin geçerli JSON değil | `if (x > 1 {`, `JSON.parse("{")` |
| `RangeError` | Sayı izin verilen aralıkta değil | `new Array(-1)` |

Açıklama çoğu zaman İngilizcedir; kelimelere bakınca anlaşılır: *is not defined* = tanımlı değil, *cannot read properties of undefined* = tanımsız bir şeyin özelliği okunamıyor, *is not a function* = bu bir fonksiyon değil.

### try, catch, finally

Hata çıkabilecek kodu `try` bloğuna koyarsan program çökmez; JavaScript hemen `catch` bloğuna atlar:

```js
try {
  const data = JSON.parse("{bozuk");   // burada hata çıkar
  console.log("Bu satır çalışmaz");
} catch (error) {
  console.log("Yakalandı:", error.name); // SyntaxError
  console.log(error.message);
} finally {
  console.log("Bu her durumda çalışır");
}
console.log("Program devam ediyor!");
```

- `error` nesnesinin `name` (tür) ve `message` (açıklama) özellikleri vardır.
- `finally` hata olsa da olmasa da çalışır: temizlik işleri (yükleniyor yazısını kaldırmak, düğmeyi tekrar açmak) için idealdir.

`catch`'i yalnızca **beklediğin** hatalar için kullan: JSON okuma, kullanıcı girişi, ağ. Her şeyi `try` içine sarmak gerçek hataları saklar.

### throw: kendi hatanı fırlat

Bir fonksiyon hatalı veri alırsa sessizce yanlış sonuç vermek yerine açık bir mesajla durmalı:

```js
function setFuel(amount) {
  if (typeof amount !== "number") {
    throw new Error("Yakıt bir sayı olmalı");
  }
  if (amount < 0 || amount > 100) {
    throw new Error("Yakıt 0 ile 100 arasında olmalı");
  }
  return amount;
}

try {
  setFuel(150);
} catch (error) {
  console.log("Hata:", error.message); // Hata: Yakıt 0 ile 100 arasında olmalı
}
```

`throw` fonksiyonu anında durdurur ve hatayı çağıran koda gönderir. Oradaki `try/catch` onu yakalar; yakalayan yoksa program kırmızı hata mesajıyla durur.

### Hata ayıklama stratejisi

Programcılar hatayı tahminle değil, adım adım bulur:

1. **Mesajı oku**: tür, açıklama, satır numarası.
2. **Değerlere bak**: şüphelendiğin yerde `console.log("total:", total)` yaz. Diziler için `console.table(list)` işini kolaylaştırır.
3. **Sorunu küçült**: kodun bir kısmını yorum satırı yap; hata hâlâ var mı?
4. **Tek şey değiştir, tekrar çalıştır**: aynı anda birçok şeyi değiştirirsen neyin işe yaradığını bilemezsin.

`console.error(...)` mesajı hata olarak, `console.warn(...)` uyarı olarak işaretler; Çıktı alanında öne çıkarlar.

Sık görülen tuzaklar: `"5" + 3` sonucu `"53"` olur (metin birleştirme). `NaN` görürsen bir yerde sayı yerine metin ya da `undefined` vardır. Dizinin son elemanı `list[list.length - 1]`'dir; `list[list.length]` her zaman `undefined`'dır.

## Örnekler

### Bozuk kayıtlar

```js
const saves = ['{"skor": 12}', "{bozuk kayıt", '{"skor": 30}'];

for (const text of saves) {
  try {
    const data = JSON.parse(text);
    console.log("Skor:", data.skor);
  } catch (error) {
    console.log("Okunamadı:", error.name);
  } finally {
    console.log("---");
  }
}
```

*Bozuk kayıt programı durdurmadı; döngü sıradaki kayıtla devam etti.*

### Hata türleri ve console.table

```js
const tests = [
  () => undefinedVariable + 1,
  () => null.length,
  () => JSON.parse("{"),
  () => { throw new Error("Kendi hatam"); },
];

for (const test of tests) {
  try {
    test();
  } catch (error) {
    console.error(error.name + ": " + error.message);
  }
}

console.table([{ ad: "Ada", skor: 12 }, { ad: "Can", skor: 30 }]);
```

*Her testin hangi türde hata verdiğine bak.*

## Görevler

### Görev 1: Güvenli okuma

`safeParse(text)` fonksiyonunu düzelt: `JSON.parse`'ı `try/catch` içine al.

- Metin geçerli JSON ise okunan değeri döndürsün.
- Değilse program çökmesin, `null` döndürsün.

**Başlangıç kodu:**

```js
function safeParse(text) {
  // JSON.parse'ı try/catch içine al; hata olursa null döndür
  return JSON.parse(text);
}

console.log(safeParse('{"skor": 42}'));
```

**İpuçları:**

1. try { return JSON.parse(text); } catch (error) { ... }
2. catch içinde: return null;

<details><summary>Çözüm</summary>

```js
function safeParse(text) {
  // JSON.parse'ı try/catch içine al; hata olursa null döndür
  try {
    return JSON.parse(text);
  } catch (error) {
    return null;
  }
}

console.log(safeParse('{"skor": 42}'));
console.log(safeParse("{bozuk"));
```

</details>

### Görev 2: Yakıt doğrulama

`setFuel(amount)` fonksiyonunu tamamla:

- `amount` bir sayı değilse: `throw new Error("Yakıt bir sayı olmalı")`
- 0'dan küçük ya da 100'den büyükse: `throw new Error("Yakıt 0 ile 100 arasında olmalı")`
- Sorun yoksa `amount`'u döndürsün.

Alttaki `try/catch` hazır; çalıştırınca `Hata: Yakıt 0 ile 100 arasında olmalı` yazmalı.

**Başlangıç kodu:**

```js
function setFuel(amount) {
  // kontrolleri yaz; hatalıysa throw new Error(...)
  return amount;
}

try {
  setFuel(150);
  console.log("Yakıt ayarlandı");
} catch (error) {
  console.log("Hata:", error.message);
}
```

**İpuçları:**

1. Sayı mı? typeof amount !== "number"
2. Aralık: if (amount < 0 || amount > 100) { throw new Error("..."); }

<details><summary>Çözüm</summary>

```js
function setFuel(amount) {
  // kontrolleri yaz; hatalıysa throw new Error(...)
  if (typeof amount !== "number") {
    throw new Error("Yakıt bir sayı olmalı");
  }
  if (amount < 0 || amount > 100) {
    throw new Error("Yakıt 0 ile 100 arasında olmalı");
  }
  return amount;
}

try {
  setFuel(150);
  console.log("Yakıt ayarlandı");
} catch (error) {
  console.log("Hata:", error.message);
}
```

</details>

### Görev 3: finally ile kapanış

`launch(ok)` kalkış adımlarını `steps` dizisine yazıp döndürüyor. Onu `try/catch/finally` ile tamamla:

- `try` içinde: `ok` false ise `throw new Error("Motor arızası")`; değilse `steps`'e `"Kalkış başarılı"` ekle.
- `catch` içinde: `steps`'e `"Sorun: "` ile hatanın mesajını birleştirip ekle (`Sorun: Motor arızası`).
- `finally` içinde: `steps`'e `"Panel kapatıldı"` ekle.

**Başlangıç kodu:**

```js
function launch(ok) {
  const steps = [];
  // try / catch / finally
  return steps;
}

console.log(launch(true));
console.log(launch(false));
```

**İpuçları:**

1. try { if (!ok) throw new Error("Motor arızası"); steps.push("Kalkış başarılı"); }
2. catch (error) { steps.push("Sorun: " + error.message); }
3. finally { steps.push("Panel kapatıldı"); }

<details><summary>Çözüm</summary>

```js
function launch(ok) {
  const steps = [];
  // try / catch / finally
  try {
    if (!ok) throw new Error("Motor arızası");
    steps.push("Kalkış başarılı");
  } catch (error) {
    steps.push("Sorun: " + error.message);
  } finally {
    steps.push("Panel kapatıldı");
  }
  return steps;
}

console.log(launch(true));
console.log(launch(false));
```

</details>

## Challenge: Hata avı

`average(list)` bir dizinin ortalamasını hesaplamalı ama sonuç `NaN` çıkıyor! Kodda **üç** sorun var. `console.log` ile değerlere bakarak bul ve düzelt:

- `average([12, 30, 18])` → `20`
- Boş dizi için `0` döndürmeli (sıfıra bölme olmasın).

İpucu: döngünün içindeki yorum satırını aç ve çıktıyı incele.

**Başlangıç kodu:**

```js
const scores = [12, 30, 18];
console.table(scores);

function average(list) {
  let total = "0";
  for (let i = 0; i <= list.length; i++) {
    total = total + list[i];
    // console.log("i:", i, "eleman:", list[i], "total:", total);
  }
  return total / list.length;
}

console.log("Ortalama:", average(scores));
```

**İpuçları:**

1. total bir metinle başlıyor: "0" + 12 = "012". Sayıyla başlat: let total = 0;
2. Son tur list[list.length] okuyor, o da undefined. < kullan.
3. Boş dizi: if (list.length === 0) return 0;

<details><summary>Çözüm</summary>

```js
const scores = [12, 30, 18];
console.table(scores);

function average(list) {
  if (list.length === 0) return 0;
  let total = 0;
  for (let i = 0; i < list.length; i++) {
    total = total + list[i];
    // console.log("i:", i, "eleman:", list[i], "total:", total);
  }
  return total / list.length;
}

console.log("Ortalama:", average(scores));
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Hataya dayanıklı oyun**

### Yıldız Avcısı: Bozuk kayıt dosyası

Kayıt dosyası bozulursa oyun çökmesin! `loadSave()` fonksiyonunu yaz:

- `localStorage`'dan `yildizSave` anahtarını oku ve `JSON.parse` ile çöz.
- Kayıt yoksa (`null`) ya da `JSON.parse` hata verirse `{ best: 0, level: 1 }` döndür. Bozuk kayıtta ayrıca `console.warn("Kayıt bozuk, sıfırdan başlıyoruz.")` yaz.
- Kayıt sağlamsa okunan nesneyi döndür.

Önizlemedeki kayıt bilerek bozuk bırakıldı. Açılıştaki kod sonucu `#info`'ya `En iyi: 0 · Seviye: 1` biçiminde yazıyor.

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
const DEFAULT_SAVE = { best: 0, level: 1 };

function loadSave() {
  const text = localStorage.getItem("yildizSave");
  // JSON.parse'ı try/catch ile güvenli yap
  return { ...DEFAULT_SAVE };
}

const save = loadSave();
document.querySelector("#info").textContent = `En iyi: ${save.best} · Seviye: ${save.level}`;
```

**İpuçları:**

1. Kayıt yoksa getItem null döndürür: if (text === null) return { ...DEFAULT_SAVE };
2. try { return JSON.parse(text); } catch (error) { ... }
3. catch içinde console.warn(...) ve varsayılanı döndür.

<details><summary>Çözüm</summary>

```js
const DEFAULT_SAVE = { best: 0, level: 1 };

function loadSave() {
  const text = localStorage.getItem("yildizSave");
  // JSON.parse'ı try/catch ile güvenli yap
  if (text === null) return { ...DEFAULT_SAVE };
  try {
    return JSON.parse(text);
  } catch (error) {
    console.warn("Kayıt bozuk, sıfırdan başlıyoruz.");
    return { ...DEFAULT_SAVE };
  }
}

const save = loadSave();
document.querySelector("#info").textContent = `En iyi: ${save.best} · Seviye: ${save.level}`;
```

</details>

### Kişisel Web Sitem: İletişim formu hataları

İletişim formundaki hataları kullanıcıya düzgünce gösterelim. `validateContact(data)` fonksiyonunu yaz; `data` = `{ name, email, message }`:

- `name` boşsa: `throw new Error("Adını yazmalısın.")`
- `email` içinde `@` yoksa: `throw new Error("E-posta adresi geçersiz.")`
- `message` 10 karakterden kısaysa: `throw new Error("Mesaj en az 10 karakter olmalı.")`

Form gönderilince (veriyi toplayan kısım hazır) `try/catch` kullan: hata varsa mesajını `#error`'a yaz ve `#status`'u boşalt; yoksa `#error`'u boşalt ve `#status`'a `Mesajın gönderildi, teşekkürler!` yaz.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<header><h1 id="site-title">Ada'nın Sitesi</h1><nav><a href="#">Ana sayfa</a> · <a href="#">Galeri</a> · <a href="#">İletişim</a></nav></header>
<form id="contact"><input id="name" placeholder="Adın"> <input id="email" placeholder="E-posta"><br><textarea id="message" placeholder="Mesajın"></textarea><br><button>Gönder</button></form>
<p id="error"></p>
<p id="status"></p>
```

**CSS:**

```css
header{border-bottom:3px solid #7e57c2;margin-bottom:10px;padding-bottom:4px}#site-title{margin:0;color:#4a2f8a;font-size:22px}nav a{color:#7e57c2}#contact input,#contact textarea{font:inherit;margin:3px 0;padding:4px}#error{color:#c62828;font-weight:600}#status{color:#2e7d32}
```

**Başlangıç kodu:**

```js
function validateContact(data) {
  // üç kontrol; hatalıysa throw new Error(...)
}

const form = document.querySelector("#contact");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const data = {
    name: document.querySelector("#name").value.trim(),
    email: document.querySelector("#email").value.trim(),
    message: document.querySelector("#message").value.trim(),
  };
  const error = document.querySelector("#error");
  const status = document.querySelector("#status");
  // try / catch ile doğrula ve sonucu göster
});
```

**İpuçları:**

1. if (data.name === "") throw new Error("Adını yazmalısın.");
2. @ var mı? data.email.includes("@")
3. Submit içinde: try { validateContact(data); ... } catch (err) { error.textContent = err.message; }

<details><summary>Çözüm</summary>

```js
function validateContact(data) {
  // üç kontrol; hatalıysa throw new Error(...)
  if (data.name === "") throw new Error("Adını yazmalısın.");
  if (!data.email.includes("@")) throw new Error("E-posta adresi geçersiz.");
  if (data.message.length < 10) throw new Error("Mesaj en az 10 karakter olmalı.");
}

const form = document.querySelector("#contact");
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const data = {
    name: document.querySelector("#name").value.trim(),
    email: document.querySelector("#email").value.trim(),
    message: document.querySelector("#message").value.trim(),
  };
  const error = document.querySelector("#error");
  const status = document.querySelector("#status");
  // try / catch ile doğrula ve sonucu göster
  try {
    validateContact(data);
    error.textContent = "";
    status.textContent = "Mesajın gönderildi, teşekkürler!";
  } catch (err) {
    error.textContent = err.message;
    status.textContent = "";
  }
});
```

</details>

### Çalışma Asistanım: Bozuk görev kayıtları

Eski bir sürümden gelen görev kayıtlarının bazıları bozuk. `cleanTasks(rows)` fonksiyonunu yaz; `rows` JSON metinlerinden oluşan bir dizi:

- Her metni `JSON.parse` ile oku; okunamayanı atla (`try/catch`).
- Okunan görevin `title`'ı boş olmayan bir metin ve `minutes`'ı 0'dan büyük bir **sayı** değilse onu da atla.
- Geçerli görevlerin dizisini döndür. Atlananların sayısını `#warning`'e `3 kayıt atlandı` biçiminde yaz; hiç atlanmadıysa `#warning` boş olsun.

Listeyi ekrana yazan `render` hazır.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 class="app-title">Çalışma Asistanım</h2>
<ul id="list"></ul>
<p id="warning"></p>
```

**CSS:**

```css
.app-title{margin:0 0 8px;color:#2e7d32}#warning{color:#e65100;font-weight:600}
```

**Başlangıç kodu:**

```js
const rows = [
  '{"title": "Fizik tekrarı", "minutes": 30}',
  '{bozuk',
  '{"title": "", "minutes": 20}',
  '{"title": "Tarih", "minutes": -5}',
  '{"title": "Kimya", "minutes": 45}',
];

function cleanTasks(rows) {
  const tasks = [];
  // her satırı oku ve kontrol et
  return tasks;
}

function render(tasks) {
  const list = document.querySelector("#list");
  list.innerHTML = "";
  for (const t of tasks) {
    const li = document.createElement("li");
    li.textContent = `${t.title} (${t.minutes} dk)`;
    list.append(li);
  }
}

render(cleanTasks(rows));
```

**İpuçları:**

1. for (const row of rows) { try { const task = JSON.parse(row); ... } catch (error) { skipped++; } }
2. Sayı mı? typeof task.minutes === "number" && task.minutes > 0
3. #warning: skipped > 0 ? `${skipped} kayıt atlandı` : ""

<details><summary>Çözüm</summary>

```js
const rows = [
  '{"title": "Fizik tekrarı", "minutes": 30}',
  '{bozuk',
  '{"title": "", "minutes": 20}',
  '{"title": "Tarih", "minutes": -5}',
  '{"title": "Kimya", "minutes": 45}',
];

function cleanTasks(rows) {
  const tasks = [];
  // her satırı oku ve kontrol et
  let skipped = 0;
  for (const row of rows) {
    try {
      const task = JSON.parse(row);
      const titleOk = typeof task.title === "string" && task.title.trim() !== "";
      const minutesOk = typeof task.minutes === "number" && task.minutes > 0;
      if (titleOk && minutesOk) {
        tasks.push(task);
      } else {
        skipped++;
      }
    } catch (error) {
      skipped++;
    }
  }
  document.querySelector("#warning").textContent = skipped > 0 ? `${skipped} kayıt atlandı` : "";
  return tasks;
}

function render(tasks) {
  const list = document.querySelector("#list");
  list.innerHTML = "";
  for (const t of tasks) {
    const li = document.createElement("li");
    li.textContent = `${t.title} (${t.minutes} dk)`;
    list.append(li);
  }
}

render(cleanTasks(rows));
```

</details>

### Bilgi Yarışması: Hatalı soru paketi

Arkadaşların kendi soru paketlerini JSON metni olarak gönderiyor, ama her paket düzgün değil. `loadPack(text)` fonksiyonunu yaz:

- Metin `JSON.parse` ile okunamazsa `#warning`'e `Soru paketi okunamadı.` yaz ve boş dizi döndür.
- Okunduysa yalnızca geçerli soruları tut: `soru` boş olmayan bir metin, `secenekler` en az 2 elemanlı bir dizi, `dogru` da `secenekler` içinde geçerli bir sıra numarası (0'dan başlar) olmalı.
- Atlanan soru varsa `#warning`'e `2 soru atlandı` biçiminde yaz; yoksa `#warning` boş olsun.
- Geçerli soruları döndür.

**Sayfanın HTML'i** (hazır verilir, öğrenci yalnızca JavaScript yazar):

```html
<h2 class="quiz-title">Bilgi Yarışması</h2>
<p id="pack-info"></p>
<p id="warning"></p>
```

**CSS:**

```css
.quiz-title{margin:0 0 8px;color:#5e35b1}#warning{color:#c62828;font-weight:600}
```

**Başlangıç kodu:**

```js
const packText = JSON.stringify([
  { soru: "Ay, hangi gezegenin uydusudur?", secenekler: ["Mars", "Dünya", "Jüpiter"], dogru: 1 },
  { soru: "Kızıl gezegen hangisidir?", secenekler: "Mars", dogru: 0 },
  { soru: "Halkalarıyla ünlü gezegen hangisidir?", secenekler: ["Satürn", "Mars"], dogru: 0 },
  { soru: "Güneşe en yakın gezegen hangisidir?", secenekler: ["Venüs", "Merkür"], dogru: 5 },
  { soru: "En büyük gezegen hangisidir?", secenekler: ["Satürn", "Jüpiter", "Neptün"], dogru: 1 },
]);

function loadPack(text) {
  // oku (try/catch), geçerlileri süz, uyarıyı yaz
  return [];
}

const questions = loadPack(packText);
document.querySelector("#pack-info").textContent = `${questions.length} soru hazır`;
```

**İpuçları:**

1. try { data = JSON.parse(text); } catch (error) { ...; return []; }
2. Geçerlilik için ayrı bir isValid(q) fonksiyonu yaz ve data.filter(isValid) kullan.
3. dogru için: Number.isInteger(q.dogru) && q.dogru >= 0 && q.dogru < q.secenekler.length

<details><summary>Çözüm</summary>

```js
const packText = JSON.stringify([
  { soru: "Ay, hangi gezegenin uydusudur?", secenekler: ["Mars", "Dünya", "Jüpiter"], dogru: 1 },
  { soru: "Kızıl gezegen hangisidir?", secenekler: "Mars", dogru: 0 },
  { soru: "Halkalarıyla ünlü gezegen hangisidir?", secenekler: ["Satürn", "Mars"], dogru: 0 },
  { soru: "Güneşe en yakın gezegen hangisidir?", secenekler: ["Venüs", "Merkür"], dogru: 5 },
  { soru: "En büyük gezegen hangisidir?", secenekler: ["Satürn", "Jüpiter", "Neptün"], dogru: 1 },
]);

function isValid(q) {
  return typeof q.soru === "string" && q.soru.trim() !== "" &&
    Array.isArray(q.secenekler) && q.secenekler.length >= 2 &&
    Number.isInteger(q.dogru) && q.dogru >= 0 && q.dogru < q.secenekler.length;
}

function loadPack(text) {
  // oku (try/catch), geçerlileri süz, uyarıyı yaz
  const warning = document.querySelector("#warning");
  let data;
  try {
    data = JSON.parse(text);
  } catch (error) {
    warning.textContent = "Soru paketi okunamadı.";
    return [];
  }
  const valid = data.filter(isValid);
  const skipped = data.length - valid.length;
  warning.textContent = skipped > 0 ? `${skipped} soru atlandı` : "";
  return valid;
}

const questions = loadPack(packText);
document.querySelector("#pack-info").textContent = `${questions.length} soru hazır`;
```

</details>
