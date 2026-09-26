# Gün 10: Nesneler

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Fonksiyon Nebulası  ·  **Maskot:** Kodi

**Bugünün hedefi:** Nesne oluşturmak, özelliklerini okuyup değiştirmek, metot yazmak ve nesne dizileriyle çalışmak

> Nebuladaki bir uzay istasyonuna yanaştık. Görevli geminin kimlik kartını istiyor: adı, hızı, yakıtı, mürettebatı... Birbirine ait bu bilgileri tek bir pakette tutmanın yolu **nesne (object)**.

![Fonksiyon Nebulası](../../gorseller/javascript/bolgeler/nebula.webp)

## Konu anlatımı

### Nesne: anahtar ve değer

Nesne süslü parantezle yazılır; içinde `anahtar: değer` çiftleri vardır. Değerlere **nokta** ya da **köşeli parantez** ile ulaşırsın:

```js
const ship = {
  name: "Kartal",
  speed: 40000,
  crew: ["Deniz", "Ada"],
};

console.log(ship.name);        // Kartal
console.log(ship["speed"]);    // 40000
const key = "crew";
console.log(ship[key]);        // ['Deniz', 'Ada']

ship.speed = 45000;            // değiştir
ship.color = "gümüş";          // yeni anahtar ekle
delete ship.color;             // anahtarı sil
```

Anahtar bir değişkenin içindeyse köşeli parantez şarttır: `ship[key]`. Olmayan bir anahtarı okursan `undefined` gelir. Python bildiysen: nesne, sözlüğe (dict) benzer.

### Metotlar ve this

Nesnenin içindeki fonksiyonlara **metot** denir. Metodun içinde `this`, metodu çağıran nesnenin kendisidir:

```js
const rocket = {
  name: "Kartal",
  fuel: 50,
  refuel(amount) {
    this.fuel += amount;
    return this.fuel;
  },
};

console.log(rocket.refuel(20));  // 70
```

`rocket.refuel(...)` çağrısında `this` = `rocket`. Metotları `refuel(amount) { ... }` biçiminde yaz; ok fonksiyonunun kendi `this`'i olmadığı için metot olarak kullanma.

### Nesneleri dolaşmak

| Yazım | Ne verir |
| --- | --- |
| `Object.keys(ship)` | Anahtarlar dizisi: `['name', 'speed']` |
| `Object.values(ship)` | Değerler dizisi: `['Kartal', 40000]` |
| `Object.entries(ship)` | Çiftler dizisi: `[['name', 'Kartal'], ['speed', 40000]]` |

`for...in` bir nesnenin anahtarlarını sırayla dolaşır:

```js
for (const key in ship) {
  console.log(key, "→", ship[key]);
}
```

Karıştırma: diziler için `for...of`, nesnenin anahtarları için `for...in`.

### Nesne dizileri ve parçalama

Gerçek programlarda çoğu zaman **nesnelerden oluşan diziler** kullanılır. **Parçalama (destructuring)** ile bir nesnenin anahtarlarını tek satırda değişkenlere alabilirsin:

```js
const crew = [
  { name: "Deniz", role: "pilot" },
  { name: "Ada", role: "mühendis" },
];

for (const member of crew) {
  const { name, role } = member;   // parçalama
  console.log(name, "-", role);
}

// Döngü başında da parçalanabilir:
for (const { name } of crew) {
  console.log(name);
}
```

Tersi de kolay: değişken adı anahtarla aynıysa kısaca yazabilirsin. `const title = "Ödev";` varken `{ title }` yazmak `{ title: title }` demektir.

## Örnekler

### Gemi kartı

```js
const ship = { name: "Kartal", speed: 40000, fuel: 80 };
console.log(ship.name);
ship.fuel -= 20;
ship.color = "gümüş";
console.log(ship);
for (const key in ship) {
  console.log(key, "→", ship[key]);
}
console.log(Object.keys(ship));
```

*const nesnenin içi değişebilir; sadece ship başka bir nesneye bağlanamaz.*

### Mürettebat listesi

```js
const crew = [
  { name: "Deniz", role: "pilot", hours: 120 },
  { name: "Ada", role: "mühendis", hours: 95 },
];

let total = 0;
for (const { name, role, hours } of crew) {
  console.log(`${name} (${role}): ${hours} saat`);
  total += hours;
}
console.log("Toplam uçuş:", total, "saat");
```

*Döngü başında { name, role, hours } yazarak her nesneyi parçaladık.*

## Görevler

### Görev 1: Gezegen kartı

1. `planet` adında bir nesne oluştur: `name` `"Mars"`, `moons` `2`, `color` `"kızıl"`.
2. Nesneyi oluşturduktan **sonra** nokta ile yeni bir anahtar ekle: `visited` `true`.
3. Nokta ile değerleri okuyarak şu satırı yazdır: `Mars: 2 uydu, kızıl`

**Başlangıç kodu:**

```js
// 1) planet nesnesini oluştur

// 2) visited anahtarını ekle

// 3) bilgi satırını yazdır
```

**İpuçları:**

1. const planet = { name: "Mars", moons: 2, color: "kızıl" };
2. planet.visited = true;
3. Şablon metinde ${planet.name} gibi değerleri kullan.

<details><summary>Çözüm</summary>

```js
// 1) planet nesnesini oluştur
const planet = {
  name: "Mars",
  moons: 2,
  color: "kızıl",
};

// 2) visited anahtarını ekle
planet.visited = true;

// 3) bilgi satırını yazdır
console.log(`${planet.name}: ${planet.moons} uydu, ${planet.color}`);
```

</details>

### Görev 2: Bilgi okuyucu

`ship` nesnesiyle çalış:

- `value`: `field` değişkenindeki anahtarın değeri. Köşeli parantez kullan: `ship[field]`
- `keyCount`: nesnede kaç anahtar var? (`Object.keys`)
- Bir `for...in` döngüsüyle her anahtarı ve değerini `anahtar: değer` biçiminde yazdır (`name: Kartal` gibi).

**Başlangıç kodu:**

```js
const ship = { name: "Kartal", speed: 40000, fuel: 80 };
const field = "speed";

// value, keyCount ve for...in döngüsü
```

**İpuçları:**

1. const value = ship[field];
2. Object.keys(ship) bir dizi verir; uzunluğu .length
3. for (const key in ship) { console.log(`${key}: ${ship[key]}`); } gibi

<details><summary>Çözüm</summary>

```js
const ship = { name: "Kartal", speed: 40000, fuel: 80 };
const field = "speed";

// value, keyCount ve for...in döngüsü
const value = ship[field];
const keyCount = Object.keys(ship).length;
for (const key in ship) {
  console.log(`${key}: ${ship[key]}`);
}
```

</details>

### Görev 3: Roket metotları

`rocket` nesnesine iki metot ekle:

- `refuel(amount)`: `this.fuel`'e `amount` eklesin ama yakıt **100'ü geçmesin**; yeni yakıtı döndürsün.
- `status()`: `Kartal: yakıt 80` biçiminde metin döndürsün (ad ve yakıt `this` ile okunmalı).

**Başlangıç kodu:**

```js
const rocket = {
  name: "Kartal",
  fuel: 50,
  // refuel(amount) ve status() metotlarını ekle
};

console.log(rocket.refuel(30));
console.log(rocket.status());
```

**İpuçları:**

1. Metot yazımı: refuel(amount) { ... }, (araya virgül koymayı unutma)
2. this.fuel = Math.min(this.fuel + amount, 100);
3. status() { return `${this.name}: yakıt ${this.fuel}`; }

<details><summary>Çözüm</summary>

```js
const rocket = {
  name: "Kartal",
  fuel: 50,
  // refuel(amount) ve status() metotlarını ekle
  refuel(amount) {
    this.fuel = Math.min(this.fuel + amount, 100);
    return this.fuel;
  },
  status() {
    return `${this.name}: yakıt ${this.fuel}`;
  },
};

console.log(rocket.refuel(30));
console.log(rocket.status());
```

</details>

## Challenge: Mürettebat raporu

`crewReport(list)` fonksiyonu bir mürettebat dizisi alsın ve şu nesneyi döndürsün:

- `totalHours`: herkesin uçuş saatlerinin toplamı
- `pilots`: rolü `"pilot"` olanların adları (dizi)
- `veteran`: en çok uçuş saati olan kişinin adı

Döngüde **parçalama** kullan: `for (const { name, role, hours } of list)`. Kontrol, fonksiyonunu başka bir mürettebatla da çağıracak.

**Başlangıç kodu:**

```js
const crew = [
  { name: "Deniz", role: "pilot", hours: 120 },
  { name: "Ada", role: "mühendis", hours: 95 },
  { name: "Can", role: "doktor", hours: 60 },
  { name: "Ece", role: "pilot", hours: 150 },
];

function crewReport(list) {
  // ...
}

console.log(crewReport(crew));
```

**İpuçları:**

1. Döngüden önce: let totalHours = 0; const pilots = []; let veteran = ""; let maxHours = -1;
2. Daha büyük saat görünce maxHours ve veteran'ı güncelle.
3. Kısa yazım: return { totalHours, pilots, veteran };

<details><summary>Çözüm</summary>

```js
const crew = [
  { name: "Deniz", role: "pilot", hours: 120 },
  { name: "Ada", role: "mühendis", hours: 95 },
  { name: "Can", role: "doktor", hours: 60 },
  { name: "Ece", role: "pilot", hours: 150 },
];

function crewReport(list) {
  let totalHours = 0;
  const pilots = [];
  let veteran = "";
  let maxHours = -1;
  for (const { name, role, hours } of list) {
    totalHours += hours;
    if (role === "pilot") {
      pilots.push(name);
    }
    if (hours > maxHours) {
      maxHours = hours;
      veteran = name;
    }
  }
  return { totalHours, pilots, veteran };
}

console.log(crewReport(crew));
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Oyuncu nesnesi**

### Yıldız Avcısı: Oyuncu nesnesi

Oyuncunun bütün bilgilerini tek bir `player` nesnesinde toplayalım. Başlangıç bilgileri hazır; şu üç metodu ekle:

- `collectStar()`: `stars`'ı 1 artırsın, yeni yıldız sayısını döndürsün.
- `hit()`: `lives`'ı 1 azaltsın ama **0'ın altına düşürmesin**; kalan canı döndürsün.
- `status()`: `Kartal | Yıldız: 2 | Can: 2` biçiminde metin döndürsün (`this` ile).

Alttaki hazır satırlar oyuncuya 2 yıldız toplatıp 1 kez vuruluyor ve durumu yazdırıyor.

**Başlangıç kodu:**

```js
const player = {
  name: "Kartal",
  lives: 3,
  stars: 0,
  inventory: ["kalkan"],
  // collectStar(), hit() ve status() metotlarını ekle
};

player.collectStar();
player.collectStar();
player.hit();
console.log(player.status());
```

**İpuçları:**

1. collectStar() { this.stars++; return this.stars; },
2. hit() içinde: if (this.lives > 0) { this.lives--; }
3. status() { return `${this.name} | Yıldız: ${this.stars} | Can: ${this.lives}`; }

<details><summary>Çözüm</summary>

```js
const player = {
  name: "Kartal",
  lives: 3,
  stars: 0,
  inventory: ["kalkan"],
  collectStar() {
    this.stars++;
    return this.stars;
  },
  hit() {
    if (this.lives > 0) {
      this.lives--;
    }
    return this.lives;
  },
  status() {
    return `${this.name} | Yıldız: ${this.stars} | Can: ${this.lives}`;
  },
};

player.collectStar();
player.collectStar();
player.hit();
console.log(player.status());
```

</details>

### Kişisel Web Sitem: Profil nesnesi

Sitenin "Hakkımda" bölümü bir `profile` nesnesinden beslensin. Nesnede `name` (adın), `age` (yaşın, sayı), `hobbies` (hobilerin, dizi) ve şu iki metot olsun:

- `addHobby(hobby)`: hobiyi `hobbies`'e eklesin, yeni hobi sayısını döndürsün.
- `intro()`: şu biçimde bir metin döndürsün (bilgiler `this` ile okunsun, hobiler `join(", ")` ile):

```
Ben Deniz, 12 yaşındayım. Hobilerim: kodlama, satranç, astronomi.
```

Sonra `addHobby("astronomi")` çağır ve `intro()` sonucunu yazdır.

**Başlangıç kodu:**

```js
const profile = {
  // name, age, hobbies, addHobby ve intro
};

// astronomi hobisini ekle ve tanıtımı yazdır
```

**İpuçları:**

1. addHobby(hobby) { this.hobbies.push(hobby); return this.hobbies.length; },
2. Şablon metinde ${this.hobbies.join(", ")} kullan.
3. profile.addHobby("astronomi"); console.log(profile.intro());

<details><summary>Çözüm</summary>

```js
const profile = {
  name: "Deniz",
  age: 12,
  hobbies: ["kodlama", "satranç"],
  addHobby(hobby) {
    this.hobbies.push(hobby);
    return this.hobbies.length;
  },
  intro() {
    return `Ben ${this.name}, ${this.age} yaşındayım. Hobilerim: ${this.hobbies.join(", ")}.`;
  },
};

// astronomi hobisini ekle ve tanıtımı yazdır
profile.addHobby("astronomi");
console.log(profile.intro());
```

</details>

### Çalışma Asistanım: Görev nesnesi

Görevler artık birer nesne! `makeTask(title, minutes)` fonksiyonu yeni bir görev nesnesi döndürsün: `{ title, minutes, done: false }`. `minutes` verilmezse **25** olsun.

Hazır satırlar iki görev ekleyip ilkini bitiriyor. Sonra `for...of` ile görevleri dolaşıp (istersen parçalayarak) şu biçimde yazdır:

```
[x] Matematik ödevi (40 dk)
[ ] Kitap okuma (25 dk)
```

**Başlangıç kodu:**

```js
// makeTask fonksiyonunu yaz

const tasks = [];
tasks.push(makeTask("Matematik ödevi", 40));
tasks.push(makeTask("Kitap okuma"));
tasks[0].done = true;

// Görevleri for...of ile yazdır
```

**İpuçları:**

1. function makeTask(title, minutes = 25) { return { title, minutes, done: false }; }
2. for (const { title, minutes, done } of tasks) { ... }
3. const box = done ? "[x]" : "[ ]";

<details><summary>Çözüm</summary>

```js
// makeTask fonksiyonunu yaz
function makeTask(title, minutes = 25) {
  return { title, minutes, done: false };
}

const tasks = [];
tasks.push(makeTask("Matematik ödevi", 40));
tasks.push(makeTask("Kitap okuma"));
tasks[0].done = true;

// Görevleri for...of ile yazdır
for (const { title, minutes, done } of tasks) {
  const box = done ? "[x]" : "[ ]";
  console.log(`${box} ${title} (${minutes} dk)`);
}
```

</details>

### Bilgi Yarışması: Soru nesnesi

Bir sorunun bütün bilgileri artık tek nesnede: metni, seçenekleri, doğru seçeneğin sırası (`correct`, 0'dan başlar) ve puanı. İki metot ekle:

- `check(index)`: `index` doğru seçeneğin sırasıysa `true`, değilse `false` döndürsün.
- `score(index)`: cevap doğruysa `this.points`, yanlışsa `0` döndürsün (içeride `this.check` kullanabilirsin).

Sonra soruyu yazdır ve seçenekleri bir döngüyle `1) Mars` biçiminde numaralandır:

```
Güneş sistemindeki en büyük gezegen hangisidir?
1) Mars
2) Jüpiter
3) Venüs
```

**Başlangıç kodu:**

```js
const question = {
  text: "Güneş sistemindeki en büyük gezegen hangisidir?",
  options: ["Mars", "Jüpiter", "Venüs"],
  correct: 1,
  points: 10,
  // check(index) ve score(index) metotlarını ekle
};

// Soruyu ve seçenekleri yazdır

console.log("Kazanılan puan:", question.score(1));
```

**İpuçları:**

1. check(index) { return index === this.correct; },
2. score(index) { return this.check(index) ? this.points : 0; }
3. Seçenekler için for (let i = 0; i < question.options.length; i++) ve numara i + 1

<details><summary>Çözüm</summary>

```js
const question = {
  text: "Güneş sistemindeki en büyük gezegen hangisidir?",
  options: ["Mars", "Jüpiter", "Venüs"],
  correct: 1,
  points: 10,
  check(index) {
    return index === this.correct;
  },
  score(index) {
    return this.check(index) ? this.points : 0;
  },
};

// Soruyu ve seçenekleri yazdır
console.log(question.text);
for (let i = 0; i < question.options.length; i++) {
  console.log(`${i + 1}) ${question.options[i]}`);
}

console.log("Kazanılan puan:", question.score(1));
```

</details>
