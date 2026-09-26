# Gün 9: Ok fonksiyonları ve kapsam

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Fonksiyon Nebulası  ·  **Maskot:** Kodi

**Bugünün hedefi:** Ok fonksiyonu yazmak, kapsamı anlamak, fonksiyonları değer gibi kullanmak ve hatırlayan fonksiyonlar (closure) yapmak

> Fonksiyon Nebulası'na girdik! Bu renkli bulutta fonksiyonlar değişkenlere konuyor, başka fonksiyonlara gönderiliyor, hatta bir şeyleri **hatırlıyor**. Bugün **ok fonksiyonlarını** ve **kapsamı** keşfediyoruz.

![Fonksiyon Nebulası](../../gorseller/javascript/bolgeler/nebula.webp)

## Konu anlatımı

### Ok fonksiyonu (=>)

Fonksiyon yazmanın kısa bir yolu daha var: **ok fonksiyonu**. Fonksiyonu bir değişkene koyarsın, parametrelerden sonra `=>` yazarsın:

```js
// Uzun hali
function square(n) {
  return n * n;
}

// Ok fonksiyonu hali
const square2 = (n) => n * n;

// Birden çok satır gerekirse süslü parantez ve return
const describe = (name, speed) => {
  const kmh = speed * 3600;
  return `${name}: saatte ${kmh} km`;
};
```

Tek satırlık ok fonksiyonunda `return` yazılmaz; `=>` işaretinden sonraki değer kendiliğinden döndürülür. Parametre yoksa boş parantez yazılır: `() => ...`

### Kapsam: değişken nerede yaşar?

`let` ve `const` ile oluşturulan bir değişken yalnızca içinde oluşturulduğu **süslü parantez bloğunda** yaşar. Buna **kapsam** denir:

```js
const ship = "Kartal";      // dışarıda: her yerden görünür
if (true) {
  const note = "iç not";    // sadece bu bloğun içinde
  console.log(ship, note);  // ikisi de görünür
}
console.log(note);          // Hata: note is not defined
```

İçerideki kod dışarıdaki değişkenleri görür ve değiştirebilir; dışarıdaki kod içeridekileri göremez. Blok içinde aynı adla yeniden `let` yazarsan **yeni, ayrı** bir değişken oluşur!

Eski kodlardaki `var` blokları dinlemez, bloğun dışından da görünür. Bu yüzden karışıklık çıkarır; sen `let` ve `const` kullan.

### Fonksiyon da bir değerdir

JavaScript'te fonksiyonlar sayı ya da metin gibi birer **değerdir**: değişkene konur, başka bir fonksiyona gönderilir. Başka bir fonksiyona gönderilen fonksiyona **callback (geri çağırma)** denir:

```js
function doTwice(action) {
  action();
  action();
}

doTwice(() => console.log("Motor ateşlendi!"));
```

Dizilerin `forEach` metodu da callback alır ve her eleman için onu çağırır:

```js
const planets = ["Mars", "Venüs"];
planets.forEach((planet) => console.log(planet));
```

### Closure: hatırlayan fonksiyonlar

Bir fonksiyon, içinde başka bir fonksiyon oluşturup onu döndürebilir. İçteki fonksiyon, dıştaki fonksiyonun değişkenlerini **hatırlar**; dıştaki fonksiyon bitse bile! Buna **closure** denir:

```js
function makeCounter() {
  let count = 0;
  return () => {
    count++;
    return count;
  };
}

const counterA = makeCounter();
const counterB = makeCounter();
console.log(counterA());  // 1
console.log(counterA());  // 2
console.log(counterB());  // 1 (kendi count'u var)
```

`makeCounter` her çağrıldığında yepyeni bir `count` oluşur. Bu yüzden her sayaç kendi sayısını tutar ve dışarıdan kimse o sayıyı bozamaz.

## Örnekler

### Ok fonksiyonları

```js
const double = (n) => n * 2;
const greet = (name) => `Merhaba ${name}!`;
const isFull = (fuel) => fuel >= 100;

console.log(double(21));
console.log(greet("Ada"));
console.log(isFull(80));
```

*Tek satırlık ok fonksiyonlarında return yazılmaz.*

### Hatırlayan sayaç

```js
function makeCounter() {
  let count = 0;
  return () => {
    count++;
    return count;
  };
}

const laps = makeCounter();
laps();
laps();
console.log("Tur:", laps());

const other = makeCounter();
console.log("Diğer sayaç:", other());
```

*laps ile other ayrı count değişkenlerini hatırlıyor.*

## Görevler

### Görev 1: Oka çevir

1. `triple` fonksiyonunu **ok fonksiyonu** olarak yeniden yaz: `const triple = ...`
2. `isPositive` adında bir ok fonksiyonu yaz: sayı 0'dan büyükse `true`, değilse `false` döndürsün.

Kodunda `function` kelimesi kalmasın.

**Başlangıç kodu:**

```js
function triple(n) {
  return n * 3;
}

// triple'ı ok fonksiyonu olarak yeniden yaz, sonra isPositive'i ekle

console.log(triple(4));
console.log(isPositive(-2));
```

**İpuçları:**

1. const triple = (n) => n * 3;
2. Karşılaştırmanın sonucu zaten true/false: (n) => n > 0

<details><summary>Çözüm</summary>

```js
// triple'ı ok fonksiyonu olarak yeniden yaz, sonra isPositive'i ekle
const triple = (n) => n * 3;
const isPositive = (n) => n > 0;

console.log(triple(4));
console.log(isPositive(-2));
```

</details>

### Görev 2: Kapsam dedektifi

**1.** Bu kod `Çok hızlı!` yazmalıydı ama `Hız normal.` yazıyor. Neden? Blok içindeki `let` **yeni** bir değişken oluşturuyor! Hatayı düzelt: kodda yalnızca bir tane `let message` kalsın.

**2.** `addFuel` adında bir ok fonksiyonu yaz: aldığı miktarı dışarıdaki `fuel` değişkenine eklesin ve `fuel`'in yeni değerini döndürsün. Sonra `addFuel(25)`'i iki kez çağır. `fuel` 90 olmalı.

**Başlangıç kodu:**

```js
let message = "Hız normal.";
const speed = 120;

if (speed > 100) {
  let message = "Çok hızlı!";
}

console.log(message);

let fuel = 40;
// addFuel ok fonksiyonunu yaz ve iki kez 25 ile çağır

console.log("Yakıt:", fuel);
```

**İpuçları:**

1. Blok içinde let yazmazsan dışarıdaki message değişir: message = "Çok hızlı!";
2. const addFuel = (amount) => { fuel += amount; return fuel; };

<details><summary>Çözüm</summary>

```js
let message = "Hız normal.";
const speed = 120;

if (speed > 100) {
  message = "Çok hızlı!";
}

console.log(message);

let fuel = 40;
// addFuel ok fonksiyonunu yaz ve iki kez 25 ile çağır
const addFuel = (amount) => {
  fuel += amount;
  return fuel;
};
addFuel(25);
addFuel(25);

console.log("Yakıt:", fuel);
```

</details>

### Görev 3: Tekrarlayıcı

`repeat(times, action)` fonksiyonu, `action` fonksiyonunu 1'den `times`'a kadar her sayıyla bir kez çağırsın: `action(1)`, `action(2)`, ...

Alttaki satır `repeat`'e bir ok fonksiyonu gönderiyor; çıktı `Tur 1`, `Tur 2`, `Tur 3` olmalı.

**Başlangıç kodu:**

```js
const repeat = (times, action) => {
  // action'ı 1'den times'a kadar her sayıyla çağır
};

repeat(3, (n) => console.log(`Tur ${n}`));
```

**İpuçları:**

1. İçeride bir for döngüsü: for (let i = 1; i <= times; i++)
2. Döngüde action(i); çağır.

<details><summary>Çözüm</summary>

```js
const repeat = (times, action) => {
  // action'ı 1'den times'a kadar her sayıyla çağır
  for (let i = 1; i <= times; i++) {
    action(i);
  }
};

repeat(3, (n) => console.log(`Tur ${n}`));
```

</details>

## Challenge: Yakıt deposu fabrikası

`makeTank(capacity)` fonksiyonu bir **fill** fonksiyonu döndürsün. Depo boş (0) başlar. Her `fill(amount)` çağrısında:

- depoya `amount` eklenir, ama depo `capacity`'yi **aşamaz**,
- depodaki güncel miktar döndürülür.

Her `makeTank` çağrısı ayrı bir depo oluşturmalı. Örnek: `const mainTank = makeTank(100);` ile `mainTank(30)` → `30`, `mainTank(50)` → `80`, `mainTank(40)` → `100`

**Başlangıç kodu:**

```js
function makeTank(capacity) {
  // depodaki miktarı tutan bir değişken ve onu güncelleyen bir fonksiyon
}

const mainTank = makeTank(100);
console.log(mainTank(30));
console.log(mainTank(50));
console.log(mainTank(40));
```

**İpuçları:**

1. makeCounter'a benzer: let level = 0; sonra bir ok fonksiyonu döndür.
2. Math.min(level + amount, capacity) kapasiteyi aşmayı engeller.
3. İçteki fonksiyon return level; demeli.

<details><summary>Çözüm</summary>

```js
function makeTank(capacity) {
  // depodaki miktarı tutan bir değişken ve onu güncelleyen bir fonksiyon
  let level = 0;
  return (amount) => {
    level = Math.min(level + amount, capacity);
    return level;
  };
}

const mainTank = makeTank(100);
console.log(mainTank(30));
console.log(mainTank(50));
console.log(mainTank(40));
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Sayaç üreten fonksiyon**

### Yıldız Avcısı: Sayaç fabrikası

Oyunda birçok şeyi saymamız gerekecek: yıldızlar, skor, düşmanlar... Her biri için ayrı kod yazmak yerine sayaç üreten bir fonksiyon yazalım.

`makeCounter(step)` bir fonksiyon döndürsün. Döndürülen fonksiyon her çağrıldığında sayıyı `step` kadar artırıp yeni sayıyı döndürsün. `step` verilmezse **1** olsun.

Sonra `countStar = makeCounter()` ve `addScore = makeCounter(10)` oluştur; bir döngüyle 3 yıldız topla (her turda ikisini de çağır). Beklenen çıktı: `Yıldız: 3 | Skor: 30`

**Başlangıç kodu:**

```js
function makeCounter(step = 1) {
  // ...
}

const countStar = makeCounter();
const addScore = makeCounter(10);
let stars = 0;
let score = 0;

// 3 yıldız topla: her turda stars = countStar(); score = addScore();

console.log(`Yıldız: ${stars} | Skor: ${score}`);
```

**İpuçları:**

1. let count = 0; sonra bir ok fonksiyonu döndür.
2. İçteki fonksiyon: count += step; return count;
3. for (let i = 0; i < 3; i++) { stars = countStar(); score = addScore(); }

<details><summary>Çözüm</summary>

```js
function makeCounter(step = 1) {
  let count = 0;
  return () => {
    count += step;
    return count;
  };
}

const countStar = makeCounter();
const addScore = makeCounter(10);
let stars = 0;
let score = 0;

// 3 yıldız topla: her turda stars = countStar(); score = addScore();
for (let i = 0; i < 3; i++) {
  stars = countStar();
  score = addScore();
}

console.log(`Yıldız: ${stars} | Skor: ${score}`);
```

</details>

### Kişisel Web Sitem: Ziyaret sayacı

Sitenin her sayfası kaç kez ziyaret edildiğini hatırlasın. `makeVisitCounter(pageName)` bir fonksiyon döndürsün; o fonksiyon her çağrıldığında ziyareti bir artırıp şu metni döndürsün:

```
Hakkımda sayfası 2 kez ziyaret edildi.
```

Her sayfanın sayacı ayrı olmalı. Alttaki hazır satırlar fonksiyonunu kullanıyor.

**Başlangıç kodu:**

```js
function makeVisitCounter(pageName) {
  // ...
}

const visitAbout = makeVisitCounter("Hakkımda");
const visitProjects = makeVisitCounter("Projeler");
console.log(visitAbout());
console.log(visitProjects());
console.log(visitAbout());
```

**İpuçları:**

1. let visits = 0; sonra bir ok fonksiyonu döndür.
2. İçteki fonksiyon: visits++; ve şablon metni return et.

<details><summary>Çözüm</summary>

```js
function makeVisitCounter(pageName) {
  let visits = 0;
  return () => {
    visits++;
    return `${pageName} sayfası ${visits} kez ziyaret edildi.`;
  };
}

const visitAbout = makeVisitCounter("Hakkımda");
const visitProjects = makeVisitCounter("Projeler");
console.log(visitAbout());
console.log(visitProjects());
console.log(visitAbout());
```

</details>

### Çalışma Asistanım: Pomodoro sayacı

Pomodoro yönteminde belli bir süre odaklanıp mola verirsin; her odak süresi bir **tur**dur.

`makePomodoro` adında bir **ok fonksiyonu** yaz. `minutes` parametresi alsın (verilmezse **25**) ve bir fonksiyon döndürsün. Döndürülen fonksiyon her çağrıldığında turu bir artırıp şu metni döndürsün:

```
Tur 2 bitti: toplam 50 dakika
```

**Başlangıç kodu:**

```js
// makePomodoro ok fonksiyonunu yaz

const focus = makePomodoro();
console.log(focus());
console.log(focus());
```

**İpuçları:**

1. const makePomodoro = (minutes = 25) => { ... };
2. İçeride let rounds = 0; ve bir ok fonksiyonu döndür.
3. Toplam dakika: rounds * minutes

<details><summary>Çözüm</summary>

```js
// makePomodoro ok fonksiyonunu yaz
const makePomodoro = (minutes = 25) => {
  let rounds = 0;
  return () => {
    rounds++;
    return `Tur ${rounds} bitti: toplam ${rounds * minutes} dakika`;
  };
};

const focus = makePomodoro();
console.log(focus());
console.log(focus());
```

</details>

### Bilgi Yarışması: Puan tutucu

`makeScoreKeeper(points)` bir fonksiyon döndürsün (`points` verilmezse **10**). Döndürülen fonksiyon `isCorrect` alsın: `true` ise puana `points` eklesin; her durumda güncel puanı döndürsün.

Sonra `results` dizisini döngüyle dolaşıp her sonucu `keeper`'a gönder ve son puanı `finalScore`'a koy. Beklenen çıktı: `Puan: 30`

**Başlangıç kodu:**

```js
function makeScoreKeeper(points = 10) {
  // ...
}

const keeper = makeScoreKeeper();
const results = [true, false, true, true];
let finalScore = 0;

// Her sonucu keeper'a gönder

console.log("Puan:", finalScore);
```

**İpuçları:**

1. let score = 0; sonra (isCorrect) => { ... } döndür.
2. if (isCorrect) { score += points; } return score;
3. for (const result of results) { finalScore = keeper(result); }

<details><summary>Çözüm</summary>

```js
function makeScoreKeeper(points = 10) {
  let score = 0;
  return (isCorrect) => {
    if (isCorrect) {
      score += points;
    }
    return score;
  };
}

const keeper = makeScoreKeeper();
const results = [true, false, true, true];
let finalScore = 0;

// Her sonucu keeper'a gönder
for (const result of results) {
  finalScore = keeper(result);
}

console.log("Puan:", finalScore);
```

</details>
