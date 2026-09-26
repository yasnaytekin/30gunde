# Gün 8: Fonksiyonlar

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Döngü Ayı  ·  **Maskot:** Kodi

**Bugünün hedefi:** Fonksiyon tanımlamak, parametre almak, return ile değer döndürmek ve varsayılan parametre kullanmak

> Döngü Ayı'ndan ayrılmadan önce roketine yeni bir yetenek kazandırıyoruz: sık kullandığın komutları bir ad altında paketlemek. Bu paketlere **fonksiyon** denir; bir kez yaz, istediğin kadar çağır.

![Döngü Ayı](../../gorseller/javascript/bolgeler/ay.webp)

## Konu anlatımı

### Fonksiyon tanımlamak ve çağırmak

`function` kelimesiyle bir fonksiyon tanımlarsın. Tanımlamak onu çalıştırmaz; adını parantezle yazıp **çağırınca** çalışır:

```js
function countdown() {
  console.log("3... 2... 1...");
  console.log("Ateşle!");
}

countdown();  // çalışır
countdown();  // bir daha çalışır
```

Python bildiysen: `def countdown():` yerine `function countdown() { ... }` yazıyoruz.

### Parametreler

Parantezin içine **parametre** yazarsan fonksiyon her çağrıldığında farklı bir değerle çalışabilir:

```js
function greet(name, planet) {
  console.log(`Merhaba ${name}, ${planet}'a hoş geldin!`);
}

greet("Deniz", "Mars");
greet("Ada", "Ay");
```

Çağırırken verdiğin değerler (`"Deniz"`, `"Mars"`) sırayla parametrelere yerleşir.

### return: sonucu geri vermek

`return` fonksiyonun sonucunu çağırdığı yere **geri verir**. Sonucu bir değişkene koyabilir, başka bir hesapta kullanabilirsin:

```js
function travelTime(distance, speed) {
  return distance / speed;
}

const hours = travelTime(384400, 40000);
console.log(Math.round(hours));  // 10
```

- `return` çalışınca fonksiyon **hemen biter**; altındaki satırlar çalışmaz.
- `console.log` sadece ekrana yazar, sonucu geri vermez. `return` yazmayan fonksiyon `undefined` döndürür.

### Varsayılan parametre

Bir parametre verilmezse kullanılacak değeri `=` ile yazabilirsin:

```js
function launch(ship, fuel = 100) {
  return `${ship} ${fuel} litre yakıtla kalkıyor.`;
}

console.log(launch("Kartal"));      // Kartal 100 litre yakıtla kalkıyor.
console.log(launch("Şahin", 60));   // Şahin 60 litre yakıtla kalkıyor.
```

İyi bir fonksiyon **tek bir iş** yapar ve adı o işi anlatır: `travelTime`, `launch`, `attack`...

## Örnekler

### Yolculuk süresi

```js
function travelTime(distance, speed) {
  return distance / speed;
}

console.log("Ay:", travelTime(384400, 40000), "saat");
console.log("İstasyon:", travelTime(400, 25), "saat");
```

*Aynı fonksiyon, farklı değerler: bir kez yazdık, iki kez kullandık.*

### Varsayılan değer

```js
function welcome(name = "Kaptan") {
  return `Hoş geldin, ${name}!`;
}

console.log(welcome("Deniz"));
console.log(welcome());
```

*İkinci çağrıda ad verilmediği için varsayılan "Kaptan" kullanıldı.*

## Görevler

### Görev 1: Alan hesaplayıcı

`area(width, height)` fonksiyonu dikdörtgen bir güneş panelinin alanını (**en × boy**) **döndürsün** (`return`).

Kontrol, fonksiyonunu farklı sayılarla da çağıracak.

**Başlangıç kodu:**

```js
function area(width, height) {
  // alanı döndür
}

console.log(area(3, 4));
```

**İpuçları:**

1. Alan = en * boy
2. return width * height;

<details><summary>Çözüm</summary>

```js
function area(width, height) {
  // alanı döndür
  return width * height;
}

console.log(area(3, 4));
```

</details>

### Görev 2: Yakıt göstergesi

`fuelStatus(fuel)` fonksiyonu yakıt durumunu metin olarak döndürsün:

- yakıt `0` ise: `"boş"`
- 30'dan az ise: `"az"`
- diğer durumda: `"yeterli"`

İpucu: `return` fonksiyonu hemen bitirdiği için `else` yazmana gerek kalmayabilir.

**Başlangıç kodu:**

```js
function fuelStatus(fuel) {
  // koşullara göre bir metin döndür
}

console.log(fuelStatus(0));
console.log(fuelStatus(15));
console.log(fuelStatus(80));
```

**İpuçları:**

1. İlk kontrol: if (fuel === 0) { return "boş"; }
2. Sonra if (fuel < 30) { return "az"; }
3. En sonda: return "yeterli";

<details><summary>Çözüm</summary>

```js
function fuelStatus(fuel) {
  // koşullara göre bir metin döndür
  if (fuel === 0) {
    return "boş";
  }
  if (fuel < 30) {
    return "az";
  }
  return "yeterli";
}

console.log(fuelStatus(0));
console.log(fuelStatus(15));
console.log(fuelStatus(80));
```

</details>

### Görev 3: Kalkış mesajı

`launchMessage(ship, countdown)` fonksiyonu şu metni döndürsün: `Kartal 3 saniye içinde kalkıyor!`

`countdown` verilmezse **varsayılan olarak 3** olsun. Yani `launchMessage("Kartal")` yukarıdaki metni, `launchMessage("Şahin", 10)` ise `Şahin 10 saniye içinde kalkıyor!` metnini vermeli.

**Başlangıç kodu:**

```js
function launchMessage(ship, countdown) {
  // metni döndür
}

console.log(launchMessage("Kartal"));
console.log(launchMessage("Şahin", 10));
```

**İpuçları:**

1. Varsayılan değer parametre listesinde yazılır: countdown = 3
2. return ile şablon metin döndür.

<details><summary>Çözüm</summary>

```js
function launchMessage(ship, countdown = 3) {
  // metni döndür
  return `${ship} ${countdown} saniye içinde kalkıyor!`;
}

console.log(launchMessage("Kartal"));
console.log(launchMessage("Şahin", 10));
```

</details>

## Challenge: En parlak yıldız

`maxOf(numbers)` fonksiyonu bir sayı dizisindeki **en büyük** sayıyı döndürsün. `Math.max` kullanmadan, bir döngüyle bul.

Dikkat: dizideki bütün sayılar negatif olabilir! Başlangıç değerini `0` değil, dizinin ilk elemanı seç.

**Başlangıç kodu:**

```js
function maxOf(numbers) {
  // döngüyle en büyük sayıyı bul ve döndür
}

console.log(maxOf([4, 18, 7, 12]));
```

**İpuçları:**

1. let max = numbers[0]; ile başla.
2. Döngüde daha büyük bir sayı görürsen max'ı güncelle.
3. Döngü bitince return max;

<details><summary>Çözüm</summary>

```js
function maxOf(numbers) {
  // döngüyle en büyük sayıyı bul ve döndür
  let max = numbers[0];
  for (const n of numbers) {
    if (n > max) {
      max = n;
    }
  }
  return max;
}

console.log(maxOf([4, 18, 7, 12]));
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Saldırı fonksiyonu**

### Yıldız Avcısı: Saldırı fonksiyonu

Gemin artık düşmanlara ateş edebiliyor! `attack(enemyHealth, damage)` fonksiyonunu yaz:

- Düşmanın yeni canını döndürsün: `enemyHealth - damage`
- `damage` verilmezse **varsayılan olarak 10** olsun.
- Can **0'ın altına düşmesin**: sonuç eksi çıkarsa `0` döndür.

Sonra `boss`'a önce 35 hasarlık, sonra varsayılan hasarla saldır (`boss = attack(boss, 35);` gibi). Beklenen çıktı: `Boss canı: 55`

**Başlangıç kodu:**

```js
// attack fonksiyonunu yaz

let boss = 100;
// boss'a iki kez saldır

console.log("Boss canı:", boss);
```

**İpuçları:**

1. function attack(enemyHealth, damage = 10) { ... }
2. const result = enemyHealth - damage; eksi ise 0 döndür.
3. boss = attack(boss, 35); sonra boss = attack(boss);

<details><summary>Çözüm</summary>

```js
// attack fonksiyonunu yaz
function attack(enemyHealth, damage = 10) {
  const result = enemyHealth - damage;
  if (result < 0) {
    return 0;
  }
  return result;
}

let boss = 100;
// boss'a iki kez saldır
boss = attack(boss, 35);
boss = attack(boss);

console.log("Boss canı:", boss);
```

</details>

### Kişisel Web Sitem: Başlık fonksiyonu

Sitenin her bölümüne süslü bir başlık lazım. `makeTitle(text, symbol)` fonksiyonu:

- Metni **Türkçe kurallarıyla büyük harfe** çevirsin (`toLocaleUpperCase("tr")`),
- İki yanına `symbol`'ü koysun; `symbol` verilmezse varsayılan `"*"` olsun,
- Sonucu döndürsün: `makeTitle("iletişim")` → `* İLETİŞİM *`, `makeTitle("hakkımda", "#")` → `# HAKKIMDA #`

Sonra `menu` dizisindeki her bölümün başlığını döngüyle yazdır ve en sona `makeTitle("hakkımda", "#")` sonucunu yazdır.

**Başlangıç kodu:**

```js
// makeTitle fonksiyonunu yaz

const menu = ["ana sayfa", "projeler", "iletişim"];
// her bölümün başlığını yazdır

// hakkımda başlığını # ile yazdır
```

**İpuçları:**

1. function makeTitle(text, symbol = "*") { ... }
2. return ile şablon metin: sembol, boşluk, büyük harfli metin, boşluk, sembol
3. for (const item of menu) { console.log(makeTitle(item)); }

<details><summary>Çözüm</summary>

```js
// makeTitle fonksiyonunu yaz
function makeTitle(text, symbol = "*") {
  return `${symbol} ${text.toLocaleUpperCase("tr")} ${symbol}`;
}

const menu = ["ana sayfa", "projeler", "iletişim"];
// her bölümün başlığını yazdır
for (const item of menu) {
  console.log(makeTitle(item));
}

// hakkımda başlığını # ile yazdır
console.log(makeTitle("hakkımda", "#"));
```

</details>

### Çalışma Asistanım: Görev ekle ve bitir

Asistana iki fonksiyon yazalım:

- `addTask(title)`: görevi `tasks` dizisinin sonuna eklesin ve **yeni görev sayısını** döndürsün.
- `completeTask(title)`: görev `tasks` içindeyse oradan çıkarsın, `done` dizisine eklesin ve `true` döndürsün. Görev listede yoksa hiçbir şeyi değiştirmeden `false` döndürsün.

Alttaki hazır satırlar fonksiyonlarını kullanıyor. Beklenen çıktı: `Kalan: Kitap okuma | Biten: Matematik ödevi`

**Başlangıç kodu:**

```js
const tasks = [];
const done = [];

function addTask(title) {
  // ...
}

function completeTask(title) {
  // ...
}

addTask("Matematik ödevi");
addTask("Kitap okuma");
completeTask("Matematik ödevi");
console.log("Kalan:", tasks.join(", "), "| Biten:", done.join(", "));
```

**İpuçları:**

1. addTask: tasks.push(title); return tasks.length;
2. completeTask: önce const index = tasks.indexOf(title); bul. -1 ise return false;
3. Bulduysan tasks.splice(index, 1); done.push(title); return true;

<details><summary>Çözüm</summary>

```js
const tasks = [];
const done = [];

function addTask(title) {
  tasks.push(title);
  return tasks.length;
}

function completeTask(title) {
  const index = tasks.indexOf(title);
  if (index === -1) {
    return false;
  }
  tasks.splice(index, 1);
  done.push(title);
  return true;
}

addTask("Matematik ödevi");
addTask("Kitap okuma");
completeTask("Matematik ödevi");
console.log("Kalan:", tasks.join(", "), "| Biten:", done.join(", "));
```

</details>

### Bilgi Yarışması: Cevap kontrol fonksiyonu

`checkAnswer(answer, correct)` fonksiyonu iki cevabı karşılaştırıp `true` ya da `false` döndürsün. Yarışmacı boşluk bırakabilir ya da büyük harf kullanabilir: karşılaştırmadan önce iki metnin de boşluklarını sil (`trim`) ve **Türkçe kurallarıyla küçük harfe** çevir (`toLocaleLowerCase("tr")`).

Sonra bir döngüyle yarışmacının cevaplarını kontrol et; her doğru cevap için `score`'a 10 ekle. Beklenen çıktı: `Puan: 20`

**Başlangıç kodu:**

```js
function checkAnswer(answer, correct) {
  // ...
}

const correctAnswers = ["Dünya", "Jüpiter", "Mars"];
const userAnswers = [" dünya", "SATÜRN", "mars "];
let score = 0;

// Döngüyle cevapları kontrol et

console.log("Puan:", score);
```

**İpuçları:**

1. const a = answer.trim().toLocaleLowerCase("tr");
2. return a === c; karşılaştırmanın sonucu zaten true/false
3. if (checkAnswer(userAnswers[i], correctAnswers[i])) { score += 10; }

<details><summary>Çözüm</summary>

```js
function checkAnswer(answer, correct) {
  const a = answer.trim().toLocaleLowerCase("tr");
  const c = correct.trim().toLocaleLowerCase("tr");
  return a === c;
}

const correctAnswers = ["Dünya", "Jüpiter", "Mars"];
const userAnswers = [" dünya", "SATÜRN", "mars "];
let score = 0;

// Döngüyle cevapları kontrol et
for (let i = 0; i < userAnswers.length; i++) {
  if (checkAnswer(userAnswers[i], correctAnswers[i])) {
    score += 10;
  }
}

console.log("Puan:", score);
```

</details>
