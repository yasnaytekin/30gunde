# Gün 2: Değişkenler ve veri tipleri

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Kalkış Üssü  ·  **Maskot:** Kodi

**Bugünün hedefi:** let ve const ile değişken oluşturmak, metin/sayı/mantıksal değerleri tanımak

> Roketin kontrol panelinde onlarca gösterge var: yakıt, hız, pilotun adı... Her birini bir yerde saklamamız lazım. Bugün bilgileri etiketli kutulara, yani **değişkenlere** koyacağız.

![Kalkış Üssü](../../gorseller/javascript/bolgeler/kalkis.webp)

## Konu anlatımı

### Değişken: etiketli bir kutu

Değişken, bir değeri bir adla saklamanı sağlar. Kutuyu `let` ile oluşturur, `=` ile içine değer koyarsın:

```js
let fuel = 100;
console.log(fuel);   // 100
fuel = 80;           // değeri değiştir
console.log(fuel);   // 80
```

Değeri değiştirirken başına tekrar `let` yazılmaz; `let` sadece kutuyu ilk oluştururken kullanılır.

### let mi, const mı?

- `let`: değeri sonradan **değişecek** kutular için (yakıt, skor).
- `const`: değeri hiç **değişmeyecek** kutular için (roketin adı, oyunun kuralları).

```js
const shipName = "Kartal-1";
shipName = "Şahin";  // Hata! const değiştirilemez
```

Eski kodlarda `var` görebilirsin; artık onun yerine `let` ve `const` kullanılıyor.

### Veri tipleri

JavaScript'te her değerin bir türü vardır. Bugün üç temel tür:

- **string** (metin): `"Mars"`, `'Ay'`
- **number** (sayı): `42`, `3.14`, `-7`
- **boolean** (mantıksal): `true` (doğru) ya da `false` (yanlış)

`typeof` bir değerin türünü söyler: `typeof "Mars"` sonucu `"string"`, `typeof 42` sonucu `"number"`.

Dikkat: `"7"` bir metin, `7` bir sayıdır. Tırnak her şeyi değiştirir!

### İsim verme kuralları

- İsim harf, `_` ya da `$` ile başlar; rakamla başlayamaz: `ship2` olur, `2ship` olmaz.
- Boşluk olmaz. Birden fazla kelime **camelCase** yazılır: `pilotName`, `fuelLevel`.
- Büyük/küçük harf fark eder: `fuel` ile `Fuel` iki ayrı değişkendir.
- Bu kursta değişken adlarını İngilizce yazıyoruz; ekrana yazılan metinler Türkçe.

## Örnekler

### Roket kartı

```js
const shipName = "Kartal-1";
let fuel = 100;
fuel = fuel - 20;
console.log(shipName, "yakıt:", fuel);
```

*fuel = fuel - 20: eski değerden 20 çıkar, sonucu yine fuel'e koy.*

### Türler

```js
console.log(typeof 42);
console.log(typeof "42");
console.log(typeof true);
```

## Görevler

### Görev 1: Pilot kartı

Kendi pilot kartını oluştur:

- `pilotName` adında bir **const** oluştur, içine adını yaz (metin).
- `age` adında bir **let** oluştur, içine yaşını yaz (sayı, tırnaksız).
- İkisini `console.log(pilotName, age);` ile yazdır.

**Başlangıç kodu:**

```js
// pilotName ve age değişkenlerini oluştur

console.log(pilotName, age);
```

**İpuçları:**

1. const pilotName = "...";
2. Yaş bir sayı: let age = 12; (tırnak yok)

<details><summary>Çözüm</summary>

```js
// pilotName ve age değişkenlerini oluştur
const pilotName = "Deniz";
let age = 12;

console.log(pilotName, age);
```

</details>

### Görev 2: Yakıt harcaması

Roket kalkışta 35 litre yakıt harcadı.

- `fuel` değişkeninden 35 çıkar (sonucu yine `fuel`'e koy). 65 sayısını elle yazma!
- Sonra `Kalan yakıt: 65` yazdır.

**Başlangıç kodu:**

```js
let fuel = 100;

// fuel'den 35 çıkar

console.log("Kalan yakıt:", fuel);
```

**İpuçları:**

1. Yeni değer eski değerden hesaplanır: fuel = fuel - ...
2. fuel = fuel - 35;

<details><summary>Çözüm</summary>

```js
let fuel = 100;

// fuel'den 35 çıkar
fuel = fuel - 35;

console.log("Kalan yakıt:", fuel);
```

</details>

### Görev 3: Tür dedektifi

Üç değişkenin türünü `typeof` ile sırayla yazdır. Çıktı üç satır olmalı: `number`, `string`, `boolean`.

**Başlangıç kodu:**

```js
const a = 7;
const b = "7";
const c = false;

// Her birinin türünü yazdır
```

**İpuçları:**

1. console.log(typeof a);
2. Üç ayrı console.log yazabilirsin.

<details><summary>Çözüm</summary>

```js
const a = 7;
const b = "7";
const c = false;

// Her birinin türünü yazdır
console.log(typeof a);
console.log(typeof b);
console.log(typeof c);
```

</details>

## Challenge: Yer değiştirme

`left` ile `right` değişkenlerinin değerlerini **değiştir**: sonunda `left` "Mars", `right` "Ay" olsun.

Kural: `"Mars"` ve `"Ay"` metinlerini ikinci kez yazma. Üçüncü bir değişken yardımcı olabilir.

**Başlangıç kodu:**

```js
let left = "Ay";
let right = "Mars";

// Değerleri yer değiştir

console.log(left, right);
```

**İpuçları:**

1. İki bardaktaki suyu değiştirmek için üçüncü bir bardak gerekir.
2. const temp = left; sonra left = right; en son right = temp;

<details><summary>Çözüm</summary>

```js
let left = "Ay";
let right = "Mars";

// Değerleri yer değiştir
const temp = left;
left = right;
right = temp;

console.log(left, right);
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Oyuncunun verileri**

### Yıldız Avcısı: Oyuncu verileri

Oyunun verilerini değişkenlerde tutalım:

- `shipName`: geminin adı (**const**, istediğin ad)
- `stars`: toplanan yıldız, başlangıçta `0` (**let**)
- `lives`: can, başlangıçta `3` (**let**)

Sonra hazır olan satırla durumu yazdır. Örnek çıktı: `Gemi: Kartal | Yıldız: 0 | Can: 3`

**Başlangıç kodu:**

```js
// shipName, stars ve lives değişkenlerini oluştur

console.log("Gemi:", shipName, "| Yıldız:", stars, "| Can:", lives);
```

**İpuçları:**

1. Adı değişmeyecek: const shipName = "...";
2. Değişecek olanlar let ile: let stars = 0;

<details><summary>Çözüm</summary>

```js
// shipName, stars ve lives değişkenlerini oluştur
const shipName = "Kartal";
let stars = 0;
let lives = 3;

console.log("Gemi:", shipName, "| Yıldız:", stars, "| Can:", lives);
```

</details>

### Kişisel Web Sitem: Site bilgileri

Sitenin bilgilerini değişkenlerde tutalım:

- `siteName`: sitenin adı (**const**)
- `author`: senin adın (**const**)
- `visitors`: ziyaretçi sayısı, başlangıçta `0` (**let**)

Örnek çıktı: `Site: Kod Günlüğüm | Yazar: Deniz | Ziyaretçi: 0`

**Başlangıç kodu:**

```js
// siteName, author ve visitors değişkenlerini oluştur

console.log("Site:", siteName, "| Yazar:", author, "| Ziyaretçi:", visitors);
```

**İpuçları:**

1. Değişmeyecekler const, ziyaretçi sayısı let.
2. let visitors = 0;

<details><summary>Çözüm</summary>

```js
// siteName, author ve visitors değişkenlerini oluştur
const siteName = "Kod Günlüğüm";
const author = "Deniz";
let visitors = 0;

console.log("Site:", siteName, "| Yazar:", author, "| Ziyaretçi:", visitors);
```

</details>

### Çalışma Asistanım: Kullanıcı bilgileri

Asistanın bilgilerini değişkenlerde tutalım:

- `userName`: senin adın (**const**)
- `dailyGoal`: günlük görev hedefi, `3` (**const**)
- `tasksDone`: tamamlanan görev, başlangıçta `0` (**let**)

Örnek çıktı: `Kullanıcı: Deniz | Hedef: 3 | Tamamlanan: 0`

**Başlangıç kodu:**

```js
// userName, dailyGoal ve tasksDone değişkenlerini oluştur

console.log("Kullanıcı:", userName, "| Hedef:", dailyGoal, "| Tamamlanan:", tasksDone);
```

**İpuçları:**

1. Hedef sabit: const dailyGoal = 3;
2. Tamamlanan artacak: let tasksDone = 0;

<details><summary>Çözüm</summary>

```js
// userName, dailyGoal ve tasksDone değişkenlerini oluştur
const userName = "Deniz";
const dailyGoal = 3;
let tasksDone = 0;

console.log("Kullanıcı:", userName, "| Hedef:", dailyGoal, "| Tamamlanan:", tasksDone);
```

</details>

### Bilgi Yarışması: Yarışmacı bilgileri

Yarışmanın bilgilerini değişkenlerde tutalım:

- `playerName`: yarışmacının adı (**const**)
- `totalQuestions`: soru sayısı, `5` (**const**)
- `score`: puan, başlangıçta `0` (**let**)

Örnek çıktı: `Yarışmacı: Deniz | Puan: 0 | Soru: 5`

**Başlangıç kodu:**

```js
// playerName, totalQuestions ve score değişkenlerini oluştur

console.log("Yarışmacı:", playerName, "| Puan:", score, "| Soru:", totalQuestions);
```

**İpuçları:**

1. Soru sayısı sabit: const totalQuestions = 5;
2. Puan değişecek: let score = 0;

<details><summary>Çözüm</summary>

```js
// playerName, totalQuestions ve score değişkenlerini oluştur
const playerName = "Deniz";
const totalQuestions = 5;
let score = 0;

console.log("Yarışmacı:", playerName, "| Puan:", score, "| Soru:", totalQuestions);
```

</details>
