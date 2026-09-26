# Gün 6: Diziler

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Döngü Ayı  ·  **Maskot:** Kodi

**Bugünün hedefi:** Dizi oluşturmak, elemanlara indeksle ulaşmak, eleman eklemek, çıkarmak ve aramak

> Roketin kargo bölmesi doluyor: yakıt hücreleri, kalkanlar, haritalar... Her birine ayrı bir değişken açmak yerine hepsini tek bir listede tutacağız. Bu listenin adı **dizi (array)**.

![Döngü Ayı](../../gorseller/javascript/bolgeler/ay.webp)

## Konu anlatımı

### Dizi: sıralı bir liste

Birçok değeri tek bir değişkende, sırayla tutmak için **dizi** kullanılır. Dizi köşeli parantezle yazılır, elemanlar virgülle ayrılır:

```js
const planets = ["Merkür", "Venüs", "Dünya"];
console.log(planets[0]);                   // Merkür
console.log(planets.length);               // 3
console.log(planets[planets.length - 1]);  // Dünya (son eleman)
```

Metinlerde olduğu gibi sayma **0'dan** başlar: ilk eleman `[0]`, son eleman `[length - 1]`. Python bildiysen: dizi, Python'daki listeye çok benzer.

### Eleman eklemek ve çıkarmak

Bir elemanı değiştirmek için sırasına yeni değer ver: `planets[1] = "Mars";`. Eklemek ve çıkarmak için dört metot var:

| Metot | Ne yapar | Örnek |
| --- | --- | --- |
| `push(x)` | Sona ekler | `cargo.push("su")` |
| `pop()` | Sondakini çıkarır ve verir | `const last = cargo.pop()` |
| `unshift(x)` | Başa ekler | `cargo.unshift("harita")` |
| `shift()` | Baştakini çıkarır ve verir | `const first = cargo.shift()` |

`const` ile oluşturduğun diziye yine de eleman ekleyip çıkarabilirsin. `const` yalnızca değişkenin **başka bir diziye** bağlanmasını engeller.

### Aramak: includes ve indexOf

```js
const crew = ["Deniz", "Ada", "Can"];
console.log(crew.includes("Ada"));   // true
console.log(crew.indexOf("Can"));    // 2
console.log(crew.indexOf("Mert"));   // -1
```

- `includes(x)`: dizide x var mı? `true` ya da `false` verir.
- `indexOf(x)`: x **kaçıncı sırada**? Bulamazsa `-1` verir.

### slice, splice ve join

```js
const route = ["Dünya", "Ay", "Mars", "Jüpiter"];
console.log(route.slice(1, 3));   // ['Ay', 'Mars']
route.splice(1, 1);               // 1. sıradan 1 eleman sil
route.splice(1, 0, "Venüs");      // 1. sıraya ekle, hiç silme
console.log(route.join(" → "));   // Dünya → Venüs → Mars → Jüpiter
```

- `slice(a, b)` diziyi **değiştirmez**; a'dan b'ye kadar (b hariç) bir kopya verir.
- `splice(sıra, kaç)` diziyi **değiştirir**: o sıradan başlayarak siler. `splice(sıra, 0, yeni)` araya ekler.
- `join(ayraç)` bütün elemanları aralarına ayracı koyarak tek bir metinde birleştirir.

## Örnekler

### Kargo listesi

```js
const cargo = ["yakıt", "kalkan"];
cargo.push("harita");
console.log(cargo);
console.log("Eşya sayısı:", cargo.length);
console.log("Son eklenen:", cargo[cargo.length - 1]);
```

*push diziyi yerinde değiştirir; yeni bir dizi oluşturmaz.*

### Arama ve birleştirme

```js
const crew = ["Deniz", "Ada", "Can", "Ece"];
console.log(crew.includes("Can"));
console.log(crew.indexOf("Ece"));
console.log(crew.indexOf("Mert"));
console.log(crew.slice(1, 3));
console.log(crew.join(" - "));
```

*indexOf bulamadığında -1 verir.*

## Görevler

### Görev 1: Gezegen listesi

`planets` dizisinden şu değişkenleri oluştur:

- `first`: ilk eleman
- `last`: son eleman. `"Mars"` yazma; `planets.length - 1` sırasını kullan.
- `count`: dizide kaç eleman olduğu

**Başlangıç kodu:**

```js
const planets = ["Merkür", "Venüs", "Dünya", "Mars"];

// first, last ve count'u oluştur

console.log(first, last, count);
```

**İpuçları:**

1. İlk eleman: planets[0]
2. Son eleman: planets[planets.length - 1]
3. Eleman sayısı: planets.length

<details><summary>Çözüm</summary>

```js
const planets = ["Merkür", "Venüs", "Dünya", "Mars"];

// first, last ve count'u oluştur
const first = planets[0];
const last = planets[planets.length - 1];
const count = planets.length;

console.log(first, last, count);
```

</details>

### Görev 2: Kargo yükleme

Kargo listesini düzenle. Dizinin ilk satırını değiştirme; sadece metotları kullan:

1. Sondaki `"çöp"` elemanını `pop` ile çıkar.
2. Sona `"kalkan"` ekle (`push`).
3. Başa `"harita"` ekle (`unshift`).

Sonunda `cargo` şöyle olmalı: `['harita', 'yakıt', 'su', 'kalkan']`

**Başlangıç kodu:**

```js
const cargo = ["yakıt", "su", "çöp"];

// pop, push ve unshift ile düzenle

console.log(cargo);
```

**İpuçları:**

1. cargo.pop(); sondaki elemanı çıkarır.
2. cargo.push("kalkan"); ve cargo.unshift("harita");

<details><summary>Çözüm</summary>

```js
const cargo = ["yakıt", "su", "çöp"];

// pop, push ve unshift ile düzenle
cargo.pop();
cargo.push("kalkan");
cargo.unshift("harita");

console.log(cargo);
```

</details>

### Görev 3: Mürettebat araması

Mürettebat listesinde arama yap:

- `hasCan`: listede `"Can"` var mı? (`includes`)
- `adaIndex`: `"Ada"` kaçıncı sırada? (`indexOf`)
- `mertIndex`: `"Mert"` kaçıncı sırada? (listede yok, bakalım ne olacak)

**Başlangıç kodu:**

```js
const crew = ["Deniz", "Ada", "Can", "Ece"];

// hasCan, adaIndex ve mertIndex

console.log(hasCan, adaIndex, mertIndex);
```

**İpuçları:**

1. crew.includes("Can") true ya da false verir.
2. crew.indexOf("Ada") sırayı verir; bulamazsa -1.

<details><summary>Çözüm</summary>

```js
const crew = ["Deniz", "Ada", "Can", "Ece"];

// hasCan, adaIndex ve mertIndex
const hasCan = crew.includes("Can");
const adaIndex = crew.indexOf("Ada");
const mertIndex = crew.indexOf("Mert");

console.log(hasCan, adaIndex, mertIndex);
```

</details>

## Challenge: Rotaya durak ekle

Roketin rotasını düzenle:

1. `splice` ile `"Mars"` ve `"Jüpiter"` arasına `"Asteroit Kuşağı"` ekle (dizinin ilk satırını değiştirme).
2. `firstStops`: rotanın ilk iki durağı (`slice`).
3. `routeText`: bütün duraklar, aralarında ` → ` olacak şekilde (`join`).

Beklenen `routeText`: `Dünya → Ay → Mars → Asteroit Kuşağı → Jüpiter`

**Başlangıç kodu:**

```js
const route = ["Dünya", "Ay", "Mars", "Jüpiter"];

// 1) splice ile ekle
// 2) firstStops
// 3) routeText

console.log(firstStops);
console.log(routeText);
```

**İpuçları:**

1. Jüpiter 3. sırada; oraya ekleyince Jüpiter bir sağa kayar: route.splice(3, 0, "Asteroit Kuşağı")
2. route.slice(0, 2) ilk iki elemanı verir.
3. route.join(" → ")

<details><summary>Çözüm</summary>

```js
const route = ["Dünya", "Ay", "Mars", "Jüpiter"];

// 1) splice ile ekle
route.splice(3, 0, "Asteroit Kuşağı");
// 2) firstStops
const firstStops = route.slice(0, 2);
// 3) routeText
const routeText = route.join(" → ");

console.log(firstStops);
console.log(routeText);
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Envanter listesi**

### Yıldız Avcısı: Envanter listesi

**Yıldız Avcısı** gemisinin bir envanteri olsun. `inventory` dizisiyle:

1. Gemi bir `"yakıt hücresi"` buldu: sona ekle.
2. `"lazer"` bozuldu: `indexOf` ile sırasını bul, `splice` ile çıkar.
3. `hasShield`: envanterde `"kalkan"` var mı?
4. Şu satırı yazdır (eşyalar `join`, sayı `length` ile gelsin):

```
Envanter: kalkan, yakıt hücresi (2 eşya)
```

**Başlangıç kodu:**

```js
const inventory = ["kalkan", "lazer"];

// 1) yakıt hücresi ekle
// 2) lazeri çıkar
// 3) hasShield
// 4) Envanter satırını yazdır
```

**İpuçları:**

1. inventory.push("yakıt hücresi");
2. const laserIndex = inventory.indexOf("lazer"); sonra inventory.splice(laserIndex, 1);
3. Şablon metin içinde ${inventory.join(", ")} ve ${inventory.length} kullan.

<details><summary>Çözüm</summary>

```js
const inventory = ["kalkan", "lazer"];

// 1) yakıt hücresi ekle
inventory.push("yakıt hücresi");
// 2) lazeri çıkar
const laserIndex = inventory.indexOf("lazer");
inventory.splice(laserIndex, 1);
// 3) hasShield
const hasShield = inventory.includes("kalkan");
// 4) Envanter satırını yazdır
console.log(`Envanter: ${inventory.join(", ")} (${inventory.length} eşya)`);
```

</details>

### Kişisel Web Sitem: Menü dizisi

Sitenin menüsünü bir dizide tutalım:

1. `menu` dizisinin sonuna `"İletişim"` ekle.
2. `menuCount`: menüde kaç bağlantı var?
3. `hasBlog`: menüde `"Blog"` var mı?
4. `menuText`: bağlantılar aralarında ` | ` olacak şekilde birleşsin ve yazdır.

Beklenen çıktı: `Ana Sayfa | Hakkımda | Projeler | İletişim`

**Başlangıç kodu:**

```js
const menu = ["Ana Sayfa", "Hakkımda", "Projeler"];

// 1) İletişim'i ekle
// 2) menuCount
// 3) hasBlog
// 4) menuText'i oluştur ve yazdır
```

**İpuçları:**

1. menu.push("İletişim");
2. menu.includes("Blog") true ya da false verir.
3. menu.join(" | ")

<details><summary>Çözüm</summary>

```js
const menu = ["Ana Sayfa", "Hakkımda", "Projeler"];

// 1) İletişim'i ekle
menu.push("İletişim");
// 2) menuCount
const menuCount = menu.length;
// 3) hasBlog
const hasBlog = menu.includes("Blog");
// 4) menuText'i oluştur ve yazdır
const menuText = menu.join(" | ");
console.log(menuText);
```

</details>

### Çalışma Asistanım: Görev dizisi

Asistanın görevlerini bir dizide tutalım:

1. Sona `"İngilizce kelime"` görevini ekle.
2. İlk görev bitti: `shift` ile çıkar ve `finished` değişkenine koy.
3. Şu iki satırı yazdır (görev adı `finished`'dan, sayı `tasks.length`'ten gelsin):

```
Tamamlandı: Matematik ödevi
Kalan görev: 2
```

**Başlangıç kodu:**

```js
const tasks = ["Matematik ödevi", "Kitap okuma"];

// 1) yeni görevi ekle
// 2) finished
// 3) iki satırı yazdır
```

**İpuçları:**

1. tasks.push("İngilizce kelime");
2. shift() çıkardığı elemanı verir: const finished = tasks.shift();

<details><summary>Çözüm</summary>

```js
const tasks = ["Matematik ödevi", "Kitap okuma"];

// 1) yeni görevi ekle
tasks.push("İngilizce kelime");
// 2) finished
const finished = tasks.shift();
// 3) iki satırı yazdır
console.log("Tamamlandı:", finished);
console.log("Kalan görev:", tasks.length);
```

</details>

### Bilgi Yarışması: Soru dizisi

Sorular ve cevaplar iki dizide duruyor; aynı sıradaki soru ile cevap birbirine ait.

1. Üçüncü soruyu ekle: `"Kızıl gezegen olarak bilinen gezegen hangisidir?"`, cevabı `"Mars"`.
2. `total`: kaç soru var?
3. Son soruyu ve cevabını yazdır. Sıra numarası ve metinler dizilerden gelsin (3 sayısını elle yazma):

```
Soru 3: Kızıl gezegen olarak bilinen gezegen hangisidir?
Cevap: Mars
```

**Başlangıç kodu:**

```js
const questions = ["Ay, hangi gezegenin uydusudur?", "Güneş sistemindeki en büyük gezegen hangisidir?"];
const answers = ["Dünya", "Jüpiter"];

// 1) üçüncü soru ve cevabını ekle
// 2) total
// 3) son soruyu ve cevabını yazdır
```

**İpuçları:**

1. Soruyu questions'a, cevabı answers'a push ile ekle.
2. Son eleman: questions[total - 1]
3. Şablon metin: Soru ${total}: ...

<details><summary>Çözüm</summary>

```js
const questions = ["Ay, hangi gezegenin uydusudur?", "Güneş sistemindeki en büyük gezegen hangisidir?"];
const answers = ["Dünya", "Jüpiter"];

// 1) üçüncü soru ve cevabını ekle
questions.push("Kızıl gezegen olarak bilinen gezegen hangisidir?");
answers.push("Mars");
// 2) total
const total = questions.length;
// 3) son soruyu ve cevabını yazdır
console.log(`Soru ${total}: ${questions[total - 1]}`);
console.log(`Cevap: ${answers[total - 1]}`);
```

</details>
