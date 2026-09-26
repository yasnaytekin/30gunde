# Gün 5: Koşullar

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Döngü Ayı  ·  **Maskot:** Kodi

**Bugünün hedefi:** if, else if, else, üçlü operatör ve switch ile karar vermek

> Döngü Ayı'na yaklaşıyoruz! Uzayda her an bir karar vermek gerekiyor: yakıt azsa uyar, hava kötüyse bekle. Bugün koduna **karar verme** yeteneği kazandıracağız.

![Döngü Ayı](../../gorseller/javascript/bolgeler/ay.webp)

## Konu anlatımı

### if ve else

`if` (eğer) parantezdeki koşul doğruysa süslü parantezin içini çalıştırır. `else` (değilse) koşul yanlışsa çalışır:

```js
const fuel = 15;
if (fuel < 20) {
  console.log("Uyarı: yakıt az!");
} else {
  console.log("Yakıt yeterli.");
}
```

Süslü parantezin içindeki satırlar iki boşlukla içeri yazılır; okuması kolay olsun diye.

### else if: birden fazla seçenek

Koşullar yukarıdan aşağı sınanır; ilk doğru olan çalışır, gerisine bakılmaz:

```js
const speed = 70;
if (speed > 100) {
  console.log("Çok hızlı!");
} else if (speed > 50) {
  console.log("İyi hız.");
} else {
  console.log("Yavaş.");
}
```

### Üçlü operatör: kısa karar

İki seçenekten birini seçip bir değişkene koymanın kısa yolu: `koşul ? doğruysa : yanlışsa`

```js
const lives = 0;
const message = lives > 0 ? "Devam!" : "Oyun bitti";
```

### switch ve doğruluk

Bir değeri birçok seçenekle karşılaştırırken `switch` düzenli görünür:

```js
switch (planet) {
  case "Mars":
    info = "Kızıl gezegen";
    break;
  default:
    info = "Bilinmiyor";
}
```

`break` unutulursa bir alttaki seçenek de çalışır!

Bilgi: `if` içinde yalnızca `true`/`false` değil her değer kullanılabilir. `0`, `""` (boş metin), `null`, `undefined` ve `NaN` **yanlış** sayılır; geri kalan her şey **doğru** sayılır.

## Örnekler

### Yakıt uyarısı

```js
const fuel = 15;
if (fuel < 20) {
  console.log("Uyarı: yakıt az!");
} else {
  console.log("Yakıt yeterli.");
}
```

*fuel'i 50 yapıp tekrar çalıştır.*

### Üçlü operatör

```js
const hour = 21;
const mode = hour >= 7 && hour < 19 ? "gündüz" : "gece";
console.log("Kokpit modu:", mode);
```

## Görevler

### Görev 1: Oksijen alarmı

`oxygen` 30'dan **küçükse** `status` "alarm", değilse "normal" olsun. `if`/`else` kullan.

(Kod önce `status`'u boş oluşturuyor; sen koşula göre değerini ver.)

**Başlangıç kodu:**

```js
const oxygen = 24;
let status = "";

// if / else ile status'a değer ver

console.log("Oksijen durumu:", status);
```

**İpuçları:**

1. if (oxygen < 30) { ... } else { ... }
2. İçeride let yazma: status = "alarm";

<details><summary>Çözüm</summary>

```js
const oxygen = 24;
let status = "";

// if / else ile status'a değer ver
if (oxygen < 30) {
  status = "alarm";
} else {
  status = "normal";
}

console.log("Oksijen durumu:", status);
```

</details>

### Görev 2: Not hesaplayıcı

`score`'a göre `grade` harfini belirle:

- 85 ve üstü: `"A"`
- 70 ve üstü: `"B"`
- 50 ve üstü: `"C"`
- diğer: `"D"`

**Başlangıç kodu:**

```js
const score = 78;
let grade = "";

// if / else if / else ile grade'i belirle

console.log("Not:", grade);
```

**İpuçları:**

1. En büyük sınırdan başla: if (score >= 85)
2. Sonra else if (score >= 70) ...

<details><summary>Çözüm</summary>

```js
const score = 78;
let grade = "";

// if / else if / else ile grade'i belirle
if (score >= 85) {
  grade = "A";
} else if (score >= 70) {
  grade = "B";
} else if (score >= 50) {
  grade = "C";
} else {
  grade = "D";
}

console.log("Not:", grade);
```

</details>

### Görev 3: Gece mi gündüz mü?

Saat 7 ile 19 arasındaysa (7 dahil, 19 hariç) `mode` "gündüz", değilse "gece" olsun. Bu sefer **üçlü operatör** (`? :`) kullan.

**Başlangıç kodu:**

```js
const hour = 21;

// mode'u üçlü operatörle belirle

console.log("Kokpit modu:", mode);
```

**İpuçları:**

1. Koşul: hour >= 7 && hour < 19
2. const mode = koşul ? "gündüz" : "gece";

<details><summary>Çözüm</summary>

```js
const hour = 21;

// mode'u üçlü operatörle belirle
const mode = hour >= 7 && hour < 19 ? "gündüz" : "gece";

console.log("Kokpit modu:", mode);
```

</details>

## Challenge: Gezegen rehberi

`switch` kullanarak `planet`'e göre `info` değişkenine değer ver:

- `"Merkür"` → `"En yakın gezegen"`
- `"Mars"` → `"Kızıl gezegen"`
- `"Jüpiter"` → `"En büyük gezegen"`
- diğer: `"Bilinmeyen gezegen"`

**Başlangıç kodu:**

```js
const planet = "Mars";
let info = "";

// switch ile info'ya değer ver

console.log(planet, "→", info);
```

**İpuçları:**

1. Her case'in sonunda break; olmalı.
2. default: diğer bütün durumlar için çalışır.

<details><summary>Çözüm</summary>

```js
const planet = "Mars";
let info = "";

// switch ile info'ya değer ver
switch (planet) {
  case "Merkür":
    info = "En yakın gezegen";
    break;
  case "Mars":
    info = "Kızıl gezegen";
    break;
  case "Jüpiter":
    info = "En büyük gezegen";
    break;
  default:
    info = "Bilinmeyen gezegen";
}

console.log(planet, "→", info);
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Oyunun durumu**

### Yıldız Avcısı: Oyun durumu

Oyunun her anında üç durumdan biri var. `message` değişkenine koşullarla değer ver:

- Can `0` ise: `"Oyun bitti!"`
- Değilse ve yıldız `10` ya da daha fazlaysa: `"Tebrikler, kazandın!"`
- Diğer durumda: kaç yıldız kaldığını söyle, örneğin `"Devam! 2 yıldız kaldı."` (sayıyı hesapla)

**Başlangıç kodu:**

```js
let lives = 1;
let stars = 8;
let message = "";

// if / else if / else ile message'a değer ver

console.log(message);
```

**İpuçları:**

1. Önce can kontrolü: if (lives === 0)
2. Kalan yıldız: 10 - stars; şablon metinle yaz.

<details><summary>Çözüm</summary>

```js
let lives = 1;
let stars = 8;
let message = "";

// if / else if / else ile message'a değer ver
if (lives === 0) {
  message = "Oyun bitti!";
} else if (stars >= 10) {
  message = "Tebrikler, kazandın!";
} else {
  message = `Devam! ${10 - stars} yıldız kaldı.`;
}

console.log(message);
```

</details>

### Kişisel Web Sitem: Saate göre karşılama

Site, ziyaretçiyi saate göre karşılasın. `greeting` değişkenine değer ver:

- 12'den önce: `"Günaydın"`
- 18'den önce: `"İyi günler"`
- diğer: `"İyi akşamlar"`

Sonra `Günaydın, siteme hoş geldin!` biçiminde yazdır.

**Başlangıç kodu:**

```js
const hour = 9;
let greeting = "";

// greeting'e değer ver

console.log(`${greeting}, siteme hoş geldin!`);
```

**İpuçları:**

1. if (hour < 12) { ... } else if (hour < 18) { ... } else { ... }

<details><summary>Çözüm</summary>

```js
const hour = 9;
let greeting = "";

// greeting'e değer ver
if (hour < 12) {
  greeting = "Günaydın";
} else if (hour < 18) {
  greeting = "İyi günler";
} else {
  greeting = "İyi akşamlar";
}

console.log(`${greeting}, siteme hoş geldin!`);
```

</details>

### Çalışma Asistanım: Hedef kontrolü

Asistan günlük hedefe göre mesaj versin. `message` değişkenine değer ver:

- Tamamlanan görev hedefe ulaştıysa: `"Bugünün hedefi tamam!"`
- Hiç görev yapılmadıysa: `"Hadi başlayalım!"`
- Diğer durumda kaç görev kaldığını söyle: `"2 görev kaldı"` (sayıyı hesapla)

**Başlangıç kodu:**

```js
const dailyGoal = 3;
let tasksDone = 1;
let message = "";

// message'a değer ver

console.log(message);
```

**İpuçları:**

1. Önce hedef kontrolü: if (tasksDone >= dailyGoal)
2. Kalan: dailyGoal - tasksDone

<details><summary>Çözüm</summary>

```js
const dailyGoal = 3;
let tasksDone = 1;
let message = "";

// message'a değer ver
if (tasksDone >= dailyGoal) {
  message = "Bugünün hedefi tamam!";
} else if (tasksDone === 0) {
  message = "Hadi başlayalım!";
} else {
  message = `${dailyGoal - tasksDone} görev kaldı`;
}

console.log(message);
```

</details>

### Bilgi Yarışması: Cevabı değerlendir

Yarışmacının cevabını değerlendir:

- Cevap doğruysa `score`'a 10 ekle ve `Doğru! +10 puan` yazdır.
- Yanlışsa `Yanlış. Doğru cevap: Pasifik` yazdır (doğru cevap `correct`'ten gelsin).
- En sonda `Puan: 50` biçiminde puanı yazdır.

**Başlangıç kodu:**

```js
const correct = "Pasifik";
const answer = "Pasifik";
let score = 40;

// Cevabı değerlendir

console.log("Puan:", score);
```

**İpuçları:**

1. if (answer === correct) { ... } else { ... }
2. score += 10; puanı 10 artırır.

<details><summary>Çözüm</summary>

```js
const correct = "Pasifik";
const answer = "Pasifik";
let score = 40;

// Cevabı değerlendir
if (answer === correct) {
  score += 10;
  console.log("Doğru! +10 puan");
} else {
  console.log(`Yanlış. Doğru cevap: ${correct}`);
}

console.log("Puan:", score);
```

</details>
