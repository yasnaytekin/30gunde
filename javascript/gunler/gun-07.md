# Gün 7: Döngüler

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Döngü Ayı  ·  **Maskot:** Kodi

**Bugünün hedefi:** for, while ve for...of ile işleri tekrarlatmak, dizileri dolaşmak ve toplam biriktirmek

> Döngü Ayı'nın yörüngesine girdik! Burada her şey tekrar eder: tur, tur, bir tur daha... Aynı komutu yüz kez yazmak yerine bilgisayara **döngü** ile tekrarlatacağız.

![Döngü Ayı](../../gorseller/javascript/bolgeler/ay.webp)

## Konu anlatımı

### for döngüsü

`for` bir işi belirli sayıda tekrarlar. Parantezin içinde noktalı virgülle ayrılmış üç parça vardır:

```js
for (let i = 1; i <= 5; i++) {
  console.log("Tur", i);
}
```

1. `let i = 1`: başlangıç, bir kez çalışır.
2. `i <= 5`: koşul, her turdan önce sınanır; yanlış olunca döngü biter.
3. `i++`: her turun sonunda çalışır, sayacı bir artırır.

Geriye saymak için `i--` kullanılır: `for (let i = 5; i >= 1; i--)`.

### while döngüsü

`while` (iken) koşul doğru olduğu sürece tekrar eder. Kaç tur süreceğini baştan bilmediğinde işe yarar:

```js
let fuel = 100;
while (fuel > 0) {
  fuel -= 30;
  console.log("Kalan yakıt:", fuel);
}
```

Dikkat: döngünün içinde koşulu değiştiren bir şey olmalı (burada `fuel -= 30`). Yoksa döngü hiç bitmez ve program donar!

### Dizileri dolaşmak

Bir dizinin her elemanına sırayla bakmak için `for...of` en kolay yoldur:

```js
const planets = ["Merkür", "Venüs", "Dünya"];
for (const planet of planets) {
  console.log(planet);
}
```

Sıra numarası da lazımsa klasik `for` ile indeksi kullan:

```js
for (let i = 0; i < planets.length; i++) {
  console.log(i + 1, planets[i]);
}
```

Python bildiysen: `for...of`, Python'daki `for planet in planets` gibidir.

### Biriktirmek, break ve continue

Döngüden önce `0` ile başlayan bir değişken açıp her turda ona ekleyerek **toplam** ya da **sayı** biriktirebilirsin:

```js
const tanks = [40, 25, 35];
let total = 0;
for (const tank of tanks) {
  total += tank;
}
console.log(total);  // 100
```

- `break`: döngüyü hemen bitirir.
- `continue`: bu turun geri kalanını atlar, sonraki tura geçer.

## Örnekler

### Geri sayım

```js
for (let i = 5; i >= 1; i--) {
  console.log(i);
}
console.log("Ateşle!");
```

*i-- sayacı her turda bir azaltır.*

### Toplam ve sayaç

```js
const tanks = [40, 25, 35, 60];
let total = 0;
let full = 0;
for (const tank of tanks) {
  total += tank;
  if (tank >= 40) {
    full++;
  }
}
console.log("Toplam yakıt:", total);
console.log("Dolu depo:", full);
```

*total ve full döngüden ÖNCE oluşturulur; yoksa her turda sıfırlanırlar.*

## Görevler

### Görev 1: Geri sayım

Bir `for` döngüsüyle 10'dan 1'e kadar geri say (her sayı ayrı satırda), en sonda `Kalkış!` yazsın.

On ayrı `console.log` yazma; döngü içinde tek bir `console.log` yeter.

**Başlangıç kodu:**

```js
// for döngüsüyle 10'dan 1'e kadar say

console.log("Kalkış!");
```

**İpuçları:**

1. Başlangıç 10, koşul i >= 1, her turda i--
2. for (let i = 10; i >= 1; i--) { console.log(i); }

<details><summary>Çözüm</summary>

```js
// for döngüsüyle 10'dan 1'e kadar say
for (let i = 10; i >= 1; i--) {
  console.log(i);
}

console.log("Kalkış!");
```

</details>

### Görev 2: Yakıt depoları

`for...of` döngüsüyle `tanks` dizisini dolaş:

- `total`: bütün depoların toplamı
- `bigTanks`: 90 ya da daha fazla yakıtı olan depo sayısı

Sonuçları kendin hesaplayıp yazma; döngü hesaplasın.

**Başlangıç kodu:**

```js
const tanks = [120, 85, 60, 95];
let total = 0;
let bigTanks = 0;

// for...of ile topla ve say

console.log("Toplam yakıt:", total);
console.log("Büyük depo:", bigTanks);
```

**İpuçları:**

1. for (const tank of tanks) { ... }
2. Her turda total += tank;
3. if (tank >= 90) { bigTanks++; }

<details><summary>Çözüm</summary>

```js
const tanks = [120, 85, 60, 95];
let total = 0;
let bigTanks = 0;

// for...of ile topla ve say
for (const tank of tanks) {
  total += tank;
  if (tank >= 90) {
    bigTanks++;
  }
}

console.log("Toplam yakıt:", total);
console.log("Büyük depo:", bigTanks);
```

</details>

### Görev 3: Yörünge turları

Roket her yörünge turunda 30 yakıt harcıyor. Yakıt **30 ya da daha fazla** olduğu sürece tur atmaya devam etsin.

Bir `while` döngüsüyle her turda `fuel`'den 30 çıkar ve `rounds`'u bir artır. Sonunda çıktı: `3 tur atıldı, kalan yakıt: 10`

**Başlangıç kodu:**

```js
let fuel = 100;
let rounds = 0;

// while döngüsü

console.log(`${rounds} tur atıldı, kalan yakıt: ${fuel}`);
```

**İpuçları:**

1. while (fuel >= 30) { ... }
2. İçeride: fuel -= 30; ve rounds++;

<details><summary>Çözüm</summary>

```js
let fuel = 100;
let rounds = 0;

// while döngüsü
while (fuel >= 30) {
  fuel -= 30;
  rounds++;
}

console.log(`${rounds} tur atıldı, kalan yakıt: ${fuel}`);
```

</details>

## Challenge: Asteroit taraması

Tarayıcıdan gelen ölçümleri topla. Ama iki kural var:

- **Negatif** sayılar sensör hatasıdır: `continue` ile atla.
- `99` gelirse tarama bitmiştir: `break` ile döngüden çık (99 ve sonrası sayılmaz).

`total`: geçerli ölçümlerin toplamı, `valid`: geçerli ölçüm sayısı. (0 geçerli bir ölçümdür.)

**Başlangıç kodu:**

```js
const scans = [3, 7, -1, 12, 0, 5, 99, 4];
let total = 0;
let valid = 0;

// Döngüyle topla (continue ve break kullan)

console.log("Geçerli ölçüm:", valid, "| Toplam:", total);
```

**İpuçları:**

1. Önce 99 kontrolü: if (value === 99) { break; }
2. Sonra negatif kontrolü: if (value < 0) { continue; }
3. En sonda: total += value; valid++;

<details><summary>Çözüm</summary>

```js
const scans = [3, 7, -1, 12, 0, 5, 99, 4];
let total = 0;
let valid = 0;

// Döngüyle topla (continue ve break kullan)
for (const value of scans) {
  if (value === 99) {
    break;
  }
  if (value < 0) {
    continue;
  }
  total += value;
  valid++;
}

console.log("Geçerli ölçüm:", valid, "| Toplam:", total);
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Düşman dalgaları**

### Yıldız Avcısı: Düşman dalgaları

Düşmanlar dalga dalga geliyor. `waves` dizisindeki her sayı bir dalgadaki düşman sayısı.

Bir `for` döngüsüyle her dalgayı yazdır ve `totalEnemies`'e ekle; sonunda toplamı yazdır:

```
Dalga 1: 3 düşman
Dalga 2: 5 düşman
Dalga 3: 8 düşman
Toplam: 16 düşman
```

**Başlangıç kodu:**

```js
const waves = [3, 5, 8];
let totalEnemies = 0;

// Her dalgayı döngüyle yazdır ve topla

// Toplamı yazdır
```

**İpuçları:**

1. Sıra numarası lazım: for (let i = 0; i < waves.length; i++)
2. Dalga numarası i + 1, düşman sayısı waves[i]
3. totalEnemies += waves[i];

<details><summary>Çözüm</summary>

```js
const waves = [3, 5, 8];
let totalEnemies = 0;

// Her dalgayı döngüyle yazdır ve topla
for (let i = 0; i < waves.length; i++) {
  console.log(`Dalga ${i + 1}: ${waves[i]} düşman`);
  totalEnemies += waves[i];
}

// Toplamı yazdır
console.log(`Toplam: ${totalEnemies} düşman`);
```

</details>

### Kişisel Web Sitem: Numaralı menü

Menüyü bir `for` döngüsüyle numaralı yazdır. Ziyaretçinin bulunduğu sayfanın (`active`) yanına ` (buradasın)` ekle. Sonunda bağlantı sayısını yazdır:

```
1. Ana Sayfa
2. Hakkımda
3. Projeler (buradasın)
4. İletişim
Toplam 4 bağlantı
```

**Başlangıç kodu:**

```js
const menu = ["Ana Sayfa", "Hakkımda", "Projeler", "İletişim"];
const active = "Projeler";

// Menüyü döngüyle numaralı yazdır

// Bağlantı sayısını yazdır
```

**İpuçları:**

1. for (let i = 0; i < menu.length; i++)
2. Numara i + 1; aktif sayfa kontrolü: menu[i] === active
3. Üçlü operatörle ek metni seç: menu[i] === active ? " (buradasın)" : ""

<details><summary>Çözüm</summary>

```js
const menu = ["Ana Sayfa", "Hakkımda", "Projeler", "İletişim"];
const active = "Projeler";

// Menüyü döngüyle numaralı yazdır
for (let i = 0; i < menu.length; i++) {
  const mark = menu[i] === active ? " (buradasın)" : "";
  console.log(`${i + 1}. ${menu[i]}${mark}`);
}

// Bağlantı sayısını yazdır
console.log(`Toplam ${menu.length} bağlantı`);
```

</details>

### Çalışma Asistanım: Numaralı görev listesi

`tasks` görevleri, `done` ise aynı sıradaki görevin bitip bitmediğini tutuyor. Bir `for` döngüsüyle listeyi yazdır: bitenler `[x]`, bitmeyenler `[ ]` ile. Biten görevleri `doneCount`'ta say ve sonunda yazdır:

```
1. [x] Matematik ödevi
2. [ ] Kitap okuma
3. [ ] İngilizce kelime
4. [x] Oda toplama
Tamamlanan: 2/4
```

**Başlangıç kodu:**

```js
const tasks = ["Matematik ödevi", "Kitap okuma", "İngilizce kelime", "Oda toplama"];
const done = [true, false, false, true];
let doneCount = 0;

// Döngüyle listeyi yazdır ve biten görevleri say

// Tamamlanan satırını yazdır
```

**İpuçları:**

1. Aynı i ile iki diziye de bakabilirsin: tasks[i] ve done[i]
2. const box = done[i] ? "[x]" : "[ ]";
3. if (done[i]) { doneCount++; }

<details><summary>Çözüm</summary>

```js
const tasks = ["Matematik ödevi", "Kitap okuma", "İngilizce kelime", "Oda toplama"];
const done = [true, false, false, true];
let doneCount = 0;

// Döngüyle listeyi yazdır ve biten görevleri say
for (let i = 0; i < tasks.length; i++) {
  const box = done[i] ? "[x]" : "[ ]";
  console.log(`${i + 1}. ${box} ${tasks[i]}`);
  if (done[i]) {
    doneCount++;
  }
}

// Tamamlanan satırını yazdır
console.log(`Tamamlanan: ${doneCount}/${tasks.length}`);
```

</details>

### Bilgi Yarışması: Sorular ve sonuç

Bir `for` döngüsüyle bütün soruları `Soru 1: ...` biçiminde yazdır. Aynı döngüde yarışmacının cevabını (`userAnswers[i]`) doğru cevapla (`answers[i]`) karşılaştır, doğruları `correctCount`'ta say. Sonunda:

```
Doğru sayısı: 2/3
```

**Başlangıç kodu:**

```js
const questions = ["Ay, hangi gezegenin uydusudur?", "Güneş sistemindeki en büyük gezegen hangisidir?", "Kızıl gezegen olarak bilinen gezegen hangisidir?"];
const answers = ["Dünya", "Jüpiter", "Mars"];
const userAnswers = ["Dünya", "Satürn", "Mars"];
let correctCount = 0;

// Soruları yazdır ve doğruları say

// Sonucu yazdır
```

**İpuçları:**

1. for (let i = 0; i < questions.length; i++)
2. if (userAnswers[i] === answers[i]) { correctCount++; }

<details><summary>Çözüm</summary>

```js
const questions = ["Ay, hangi gezegenin uydusudur?", "Güneş sistemindeki en büyük gezegen hangisidir?", "Kızıl gezegen olarak bilinen gezegen hangisidir?"];
const answers = ["Dünya", "Jüpiter", "Mars"];
const userAnswers = ["Dünya", "Satürn", "Mars"];
let correctCount = 0;

// Soruları yazdır ve doğruları say
for (let i = 0; i < questions.length; i++) {
  console.log(`Soru ${i + 1}: ${questions[i]}`);
  if (userAnswers[i] === answers[i]) {
    correctCount++;
  }
}

// Sonucu yazdır
console.log(`Doğru sayısı: ${correctCount}/${questions.length}`);
```

</details>
