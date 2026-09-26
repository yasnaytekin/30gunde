# Gün 12: Set, Map ve JSON

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Fonksiyon Nebulası  ·  **Maskot:** Kodi

**Bugünün hedefi:** Set ile tekrarları ayıklamak, Map ile anahtar-değer tutmak, spread ile kopyalamak ve veriyi JSON'a çevirmek

> Nebulanın ucundaki bir istasyona kenetlendin. İstasyon bilgisayarı verileri saklamak ve başka gemilere göndermek için ortak bir dil kullanıyor: **JSON**. Ayrıca bugün **Set** ve **Map** adlı iki yeni kutu tanıyacaksın.

![Fonksiyon Nebulası](../../gorseller/javascript/bolgeler/nebula.webp)

## Konu anlatımı

### Set: tekrarsız kutu

`Set` her değeri **yalnızca bir kez** tutan bir koleksiyondur. Aynı değeri ikinci kez eklersen görmezden gelir:

```js
const visited = new Set();
visited.add("Mars");
visited.add("Venüs");
visited.add("Mars");              // zaten var, eklenmez
console.log(visited.size);        // 2
console.log(visited.has("Mars")); // true
visited.delete("Venüs");
```

En sık kullanımı: bir diziden tekrarları atmak. `new Set(dizi)` tekrarları siler, `[...set]` onu yeniden diziye çevirir:

```js
const logs = ["Mars", "Ay", "Mars", "Ay", "Venüs"];
const unique = [...new Set(logs)]; // ['Mars', 'Ay', 'Venüs']
```

### Map: anahtar → değer

`Map` de nesne gibi anahtar-değer çiftleri tutar ama kendi metotlarıyla çalışır: `set`, `get`, `has`, `delete` ve `size`.

```js
const cargo = new Map();
cargo.set("su", 40);
cargo.set("yakıt", 25);
console.log(cargo.get("su")); // 40
console.log(cargo.size);      // 2
cargo.set("su", 35);          // aynı anahtar: değeri günceller

for (const [item, amount] of cargo) {
  console.log(item, amount);
}
```

Ne zaman hangisi? Alanları belli bir şey (oyuncu, gemi) için **nesne**; sürekli eklenip silinen, sayılan şeyler (kelime sayacı, envanter adetleri) için **Map** rahattır.

### Spread (...): aç ve kopyala

Üç nokta `...` bir diziyi ya da nesneyi **açıp** içindekileri başka bir yere döker. Böylece kopya çıkarabilir, birleştirebilirsin:

```js
const crew = ["Ada", "Can"];
const bigger = [...crew, "Ece"];     // ['Ada', 'Can', 'Ece']

const ship = { name: "Kartal", fuel: 50 };
const full = { ...ship, fuel: 100 }; // fuel'in üzerine yazıldı
console.log(ship.fuel, full.fuel);   // 50 100
```

Neden kopya? `const b = a;` yazınca yeni bir dizi oluşmaz: `a` ile `b` **aynı** diziyi gösterir, birini değiştirirsen öbürü de değişir. `[...a]` ise yeni bir dizi verir.

### JSON: verinin ortak dili

**JSON** (JavaScript Object Notation), veriyi **metne** çevirmenin standart yoludur. Programlar veriyi kaydederken ya da internetten gönderirken JSON kullanır; bir API'den gelen veri neredeyse her zaman JSON'dır.

```js
const player = { name: "Ada", level: 3, items: ["kalkan", "lazer"] };

const text = JSON.stringify(player);
console.log(text); // {"name":"Ada","level":3,"items":["kalkan","lazer"]}

const pretty = JSON.stringify(player, null, 2); // 2 boşluk girintili, okunaklı
const back = JSON.parse(text);                  // metinden yeniden nesne
console.log(back.items[1]);                     // lazer
```

- `JSON.stringify(veri)`: nesne ya da dizi → metin. `JSON.stringify(veri, null, 2)` satırlara bölüp girintili yazar.
- `JSON.parse(metin)`: metin → nesne ya da dizi.
- JSON'da anahtarlar ve metinler **çift tırnaklı** yazılır. Fonksiyonlar ve `undefined` JSON'a girmez.
- Bozuk bir metni `JSON.parse` ile çözmeye çalışırsan `SyntaxError` alırsın.

İleride `localStorage` ile kayıt yaparken ve `fetch` ile sunucudan veri alırken hep JSON kullanacaksın.

## Örnekler

### Tekrarsız ziyaretler

```js
const logs = ["Mars", "Ay", "Mars", "Venüs", "Ay", "Mars"];

const planets = new Set(logs);
console.log(planets);
console.log("Farklı gezegen:", planets.size);

const visits = new Map();
for (const p of logs) {
  visits.set(p, (visits.get(p) || 0) + 1);
}
console.log(visits);
console.log("Mars ziyareti:", visits.get("Mars"));
```

*visits.get(p) || 0: gezegen henüz yoksa 0'dan başla.*

### JSON'a çevir, geri al

```js
const save = { pilot: "Ada", level: 3, items: ["kalkan", "lazer"] };

const text = JSON.stringify(save, null, 2);
console.log(text);
console.log(typeof text);

const loaded = JSON.parse(text);
const next = { ...loaded, level: loaded.level + 1 };
console.log(loaded.level, "→", next.level);
```

*stringify'daki 2'yi silip tekrar çalıştır: metin tek satıra iner.*

## Görevler

### Görev 1: Tekrarsız yıldızlar

Seyir defterinde bazı yıldızlar birden çok kez yazılmış. `Set` ve spread (`...`) kullanarak tekrarsız bir `unique` **dizisi** oluştur.

Sonra `unique.length` ile `4 farklı yıldız` yazdır (sayıyı elle yazma).

**Başlangıç kodu:**

```js
const visited = ["Vega", "Sirius", "Vega", "Altair", "Sirius", "Deneb"];

// unique dizisini oluştur

// kaç farklı yıldız olduğunu yazdır
```

**İpuçları:**

1. new Set(visited) tekrarları atar.
2. [...new Set(visited)] onu diziye çevirir.
3. console.log(`${unique.length} farklı yıldız`);

<details><summary>Çözüm</summary>

```js
const visited = ["Vega", "Sirius", "Vega", "Altair", "Sirius", "Deneb"];

// unique dizisini oluştur
const unique = [...new Set(visited)];

// kaç farklı yıldız olduğunu yazdır
console.log(`${unique.length} farklı yıldız`);
```

</details>

### Görev 2: Kargo haritası

`cargo` bir `Map`. Şunları yap:

1. `"yemek"` → `15` ve `"oksijen"` → `30` ekle.
2. `"su"` miktarını `35` yap.
3. `for...of` ile bütün miktarları `total`'a topla.

**Başlangıç kodu:**

```js
const cargo = new Map();
cargo.set("su", 40);
cargo.set("yakıt", 25);

// 1) yemek ve oksijen ekle  2) suyu 35 yap

let total = 0;
// 3) for...of ile bütün miktarları topla

console.log(cargo);
console.log("Toplam yük:", total);
```

**İpuçları:**

1. cargo.set("yemek", 15);
2. Aynı anahtarla set: değeri günceller.
3. for (const [item, amount] of cargo) { total += amount; }

<details><summary>Çözüm</summary>

```js
const cargo = new Map();
cargo.set("su", 40);
cargo.set("yakıt", 25);

// 1) yemek ve oksijen ekle  2) suyu 35 yap
cargo.set("yemek", 15);
cargo.set("oksijen", 30);
cargo.set("su", 35);

let total = 0;
// 3) for...of ile bütün miktarları topla
for (const [item, amount] of cargo) {
  total += amount;
}

console.log(cargo);
console.log("Toplam yük:", total);
```

</details>

### Görev 3: Seyir defteri

Seyir defterini JSON'a çevirip geri al:

1. `text`: `log`'un JSON metni (`JSON.stringify`).
2. `loaded`: `text`'ten geri çevrilen nesne (`JSON.parse`).
3. `nextDay`: `loaded`'ın spread ile kopyası, ama `day` değeri `13`. `loaded` değişmesin.

**Başlangıç kodu:**

```js
const log = { ship: "Kartal", day: 12, planets: ["Mars", "Ay"] };

// text, loaded, nextDay

console.log(text);
console.log(nextDay);
```

**İpuçları:**

1. const text = JSON.stringify(log);
2. const loaded = JSON.parse(text);
3. const nextDay = { ...loaded, day: 13 };

<details><summary>Çözüm</summary>

```js
const log = { ship: "Kartal", day: 12, planets: ["Mars", "Ay"] };

// text, loaded, nextDay
const text = JSON.stringify(log);
const loaded = JSON.parse(text);
const nextDay = { ...loaded, day: 13 };

console.log(text);
console.log(nextDay);
```

</details>

## Challenge: Sinyal sayacı

İki fonksiyon yaz:

- `countWords(list)`: her kelimenin kaç kez geçtiğini tutan bir `Map` döndürsün (ör. `"bip"` → `3`).
- `mostCommon(list)`: en çok geçen kelimeyi döndürsün (`countWords`'ü kullanabilirsin).

**Başlangıç kodu:**

```js
const signals = ["bip", "vuu", "bip", "tık", "bip", "vuu"];

function countWords(list) {
  const counts = new Map();
  // her kelimeyi say
  return counts;
}

function mostCommon(list) {
  // en çok geçen kelime
}

console.log(countWords(signals));
console.log("En sık:", mostCommon(signals));
```

**İpuçları:**

1. counts.set(word, (counts.get(word) || 0) + 1);
2. Map'i for (const [word, count] of ...) ile gez.
3. En büyüğü bulmak için bestCount değişkeni tut.

<details><summary>Çözüm</summary>

```js
const signals = ["bip", "vuu", "bip", "tık", "bip", "vuu"];

function countWords(list) {
  const counts = new Map();
  // her kelimeyi say
  for (const word of list) {
    counts.set(word, (counts.get(word) || 0) + 1);
  }
  return counts;
}

function mostCommon(list) {
  // en çok geçen kelime
  let best = null;
  let bestCount = 0;
  for (const [word, count] of countWords(list)) {
    if (count > bestCount) {
      best = word;
      bestCount = count;
    }
  }
  return best;
}

console.log(countWords(signals));
console.log("En sık:", mostCommon(signals));
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Kayıt dosyası**

### Yıldız Avcısı: Kayıt dosyası

Oyunun kayıt dosyasını hazırla:

- `saveGame(p)`: oyuncunun kopyasını alsın, envanterdeki **tekrarları** `Set` ile atsın ve 2 boşluk girintili JSON metni döndürsün. Asıl oyuncu nesnesi değişmesin.
- `loadGame(text)`: JSON metnini yeniden nesneye çevirip döndürsün.

**Başlangıç kodu:**

```js
const player = {
  name: "Ada",
  level: 3,
  score: 450,
  inventory: ["kalkan", "lazer", "lazer", "harita"],
};

function saveGame(p) {
  // kopya + tekrarsız envanter, sonra JSON.stringify(..., null, 2)
}

function loadGame(text) {
  // JSON.parse
}

const file = saveGame(player);
console.log(file);
console.log(loadGame(file));
```

**İpuçları:**

1. const clean = { ...p, inventory: [...new Set(p.inventory)] };
2. return JSON.stringify(clean, null, 2);
3. return JSON.parse(text);

<details><summary>Çözüm</summary>

```js
const player = {
  name: "Ada",
  level: 3,
  score: 450,
  inventory: ["kalkan", "lazer", "lazer", "harita"],
};

function saveGame(p) {
  // kopya + tekrarsız envanter, sonra JSON.stringify(..., null, 2)
  const clean = { ...p, inventory: [...new Set(p.inventory)] };
  return JSON.stringify(clean, null, 2);
}

function loadGame(text) {
  // JSON.parse
  return JSON.parse(text);
}

const file = saveGame(player);
console.log(file);
console.log(loadGame(file));
```

</details>

### Kişisel Web Sitem: Ayarlar dosyası

Siten ziyaretçinin ayarlarını JSON olarak saklayacak:

- `loadSettings(text)`: JSON metnini çözsün ve `defaults` ile birleştirsin: `{ ...defaults, ...kayıtlı }`. Metinde olmayan ayarlar varsayılandan gelsin. `defaults` değişmesin.
- `saveSettings(settings)`: ayarları JSON metnine çevirip döndürsün.

**Başlangıç kodu:**

```js
const defaults = { theme: "light", fontSize: 16, lang: "tr" };
const savedText = '{"theme":"dark","fontSize":18}';

function loadSettings(text) {
  // JSON'u çöz, varsayılanlarla birleştir
}

function saveSettings(settings) {
  // JSON metnine çevir
}

const settings = loadSettings(savedText);
console.log(settings);
console.log(saveSettings(settings));
```

**İpuçları:**

1. JSON.parse(text) kayıtlı ayarları nesneye çevirir.
2. return { ...defaults, ...JSON.parse(text) };
3. Sonra gelen spread öncekinin üzerine yazar.

<details><summary>Çözüm</summary>

```js
const defaults = { theme: "light", fontSize: 16, lang: "tr" };
const savedText = '{"theme":"dark","fontSize":18}';

function loadSettings(text) {
  // JSON'u çöz, varsayılanlarla birleştir
  return { ...defaults, ...JSON.parse(text) };
}

function saveSettings(settings) {
  // JSON metnine çevir
  return JSON.stringify(settings);
}

const settings = loadSettings(savedText);
console.log(settings);
console.log(saveSettings(settings));
```

</details>

### Çalışma Asistanım: Kaydet ve yükle

Asistan görev listesini kaydedip geri yükleyebilsin:

- `saveTasks(list)`: diziyi JSON metnine çevirip döndürsün.
- `loadTasks(text)`: metin boşsa (`""` ya da `null`) boş dizi `[]`, değilse `JSON.parse` sonucunu döndürsün.

**Başlangıç kodu:**

```js
const tasks = [
  { title: "Matematik ödevi", done: true },
  { title: "Fizik tekrarı", done: false },
];

function saveTasks(list) {
  // JSON metnine çevir
}

function loadTasks(text) {
  // boşsa [], değilse JSON.parse
}

const saved = saveTasks(tasks);
console.log(saved);
console.log(loadTasks(saved));
console.log(loadTasks(""));
```

**İpuçları:**

1. return JSON.stringify(list);
2. Boş metin ve null yanlış sayılır: if (!text) return [];

<details><summary>Çözüm</summary>

```js
const tasks = [
  { title: "Matematik ödevi", done: true },
  { title: "Fizik tekrarı", done: false },
];

function saveTasks(list) {
  // JSON metnine çevir
  return JSON.stringify(list);
}

function loadTasks(text) {
  // boşsa [], değilse JSON.parse
  if (!text) return [];
  return JSON.parse(text);
}

const saved = saveTasks(tasks);
console.log(saved);
console.log(loadTasks(saved));
console.log(loadTasks(""));
```

</details>

### Bilgi Yarışması: Soru paketi

Soru paketleri JSON metni olarak geliyor. İki fonksiyon yaz:

- `describePack(text)`: `"Gezegenler: 3 soru"` biçiminde paketin adını ve soru sayısını döndürsün.
- `correctAnswers(text)`: her sorunun doğru seçeneğinin **metnini** dizi olarak döndürsün (`answer` doğru seçeneğin sırası). `map` kullan.

**Başlangıç kodu:**

```js
const packText = '{"name":"Gezegenler","questions":[' +
  '{"text":"Kızıl gezegen hangisi?","options":["Mars","Venüs","Merkür"],"answer":0},' +
  '{"text":"En büyük gezegen hangisi?","options":["Satürn","Jüpiter","Neptün"],"answer":1},' +
  '{"text":"Halkalı gezegen hangisi?","options":["Uranüs","Mars","Satürn"],"answer":2}]}';

function describePack(text) {
  // JSON.parse ile paketi aç
}

function correctAnswers(text) {
  // her sorunun doğru seçeneği
}

console.log(describePack(packText));
console.log(correctAnswers(packText));
```

**İpuçları:**

1. const pack = JSON.parse(text);
2. pack.questions.length soru sayısını verir.
3. pack.questions.map((q) => q.options[q.answer])

<details><summary>Çözüm</summary>

```js
const packText = '{"name":"Gezegenler","questions":[' +
  '{"text":"Kızıl gezegen hangisi?","options":["Mars","Venüs","Merkür"],"answer":0},' +
  '{"text":"En büyük gezegen hangisi?","options":["Satürn","Jüpiter","Neptün"],"answer":1},' +
  '{"text":"Halkalı gezegen hangisi?","options":["Uranüs","Mars","Satürn"],"answer":2}]}';

function describePack(text) {
  // JSON.parse ile paketi aç
  const pack = JSON.parse(text);
  return `${pack.name}: ${pack.questions.length} soru`;
}

function correctAnswers(text) {
  // her sorunun doğru seçeneği
  const pack = JSON.parse(text);
  return pack.questions.map((q) => q.options[q.answer]);
}

console.log(describePack(packText));
console.log(correctAnswers(packText));
```

</details>
