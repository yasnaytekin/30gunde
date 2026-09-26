# Gün 11: map, filter, reduce

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Fonksiyon Nebulası  ·  **Maskot:** Kodi

**Bugünün hedefi:** map, filter, reduce, find, some, every ve sort ile dizileri dönüştürmek, süzmek ve sıralamak

> Fonksiyon Nebulası'nın derinlerindesin, kaptan. Radarın yüzlerce yıldızı listeliyor; hepsini tek tek döngüyle gezmek yerine dizilere **map, filter ve reduce** gibi süper güçler vereceğiz.

![Fonksiyon Nebulası](../../gorseller/javascript/bolgeler/nebula.webp)

## Konu anlatımı

### map: her elemanı dönüştür

`map`, dizinin **her elemanına** bir fonksiyon uygular ve sonuçlardan **yeni bir dizi** yapar. Asıl dizi değişmez:

```js
const prices = [10, 20, 30];
const doubled = prices.map((p) => p * 2);
console.log(doubled); // [20, 40, 60]
console.log(prices);  // [10, 20, 30]
```

Yeni dizinin uzunluğu her zaman eskisiyle aynıdır. Fonksiyon ikinci bir değer de alır: elemanın **sırası** (index, 0'dan başlar).

```js
const names = ["Ada", "Can"];
const lines = names.map((name, i) => (i + 1) + ". " + name);
console.log(lines); // ['1. Ada', '2. Can']
```

### filter, find, some ve every

`filter` koşulu sağlayan elemanlardan yeni bir dizi yapar. Fonksiyon `true` döndürürse eleman kalır, `false` döndürürse elenir:

```js
const fuel = [80, 15, 60, 5];
const low = fuel.filter((f) => f < 20);   // [15, 5]
const first = fuel.find((f) => f < 20);   // 15
const none = fuel.find((f) => f > 100);   // undefined
fuel.some((f) => f < 10);                 // true
fuel.every((f) => f > 0);                 // true
```

- `find` dizi değil, **ilk uyan elemanı** verir; hiçbiri uymazsa `undefined`.
- `some`: **en az biri** uyuyorsa `true`.
- `every`: **hepsi** uyuyorsa `true`.

### reduce: tek bir değere indirgemek

`reduce` bütün diziyi dolaşıp **tek bir değer** üretir: toplam, en büyük değer, bir sayaç... İki şey verirsin: bir fonksiyon ve başlangıç değeri.

```js
const stars = [3, 5, 2];
const total = stars.reduce((sum, s) => sum + s, 0);
console.log(total); // 10
```

Fonksiyonun ilk parametresi (burada `sum`) şimdiye kadar **biriken** değer, ikincisi sıradaki eleman. Adım adım: 0 + 3 = 3, 3 + 5 = 8, 8 + 2 = 10.

Başlangıç değerini (`0`) yazmayı unutma; nesne dizilerinde mutlaka gerekir:

```js
const tanks = [{ fuel: 40 }, { fuel: 25 }];
const all = tanks.reduce((sum, t) => sum + t.fuel, 0); // 65
```

### sort ve zincirleme

`sort` diziyi sıralar ama dikkat: elemanları **metin gibi** karşılaştırır! Sayılar için bir karşılaştırma fonksiyonu ver:

```js
[10, 9, 100].sort();                  // [10, 100, 9]  yanlış!
[10, 9, 100].sort((a, b) => a - b);   // [9, 10, 100]  küçükten büyüğe
[10, 9, 100].sort((a, b) => b - a);   // [100, 10, 9]  büyükten küçüğe
```

Fonksiyon negatif bir sayı döndürürse `a` öne, pozitif döndürürse `b` öne geçer. Nesneleri bir alana göre sıralamak için: `players.sort((a, b) => b.score - a.score)`.

`sort` **asıl diziyi değiştirir**. Asıl dizi bozulmasın istiyorsan önce `slice()` ile kopyala: `scores.slice().sort(...)`.

Bu metotlar dizi döndürdüğü için arka arkaya **zincirlenebilir**:

```js
const winners = players
  .filter((p) => p.score > 50)
  .sort((a, b) => b.score - a.score)
  .map((p) => p.name);
```

## Örnekler

### Yakıt raporu

```js
const tanks = [80, 15, 60, 5, 45];

const percent = tanks.map((t) => t + "%");
const low = tanks.filter((t) => t < 20);
const total = tanks.reduce((sum, t) => sum + t, 0);

console.log("Depolar:", percent);
console.log("Az kalanlar:", low);
console.log("Toplam yakıt:", total);
console.log("Hiç boş depo yok mu?", tanks.every((t) => t > 0));
```

*tanks dizisine 0 ekleyip tekrar çalıştır: every ne der?*

### Gezegenleri sırala

```js
const planets = [
  { name: "Mars", distance: 228 },
  { name: "Merkür", distance: 58 },
  { name: "Jüpiter", distance: 778 },
  { name: "Venüs", distance: 108 },
];

const order = planets
  .slice()
  .sort((a, b) => a.distance - b.distance)
  .map((p, i) => (i + 1) + ". " + p.name);

console.log(order.join("\n"));
console.log("İlk uzak gezegen:", planets.find((p) => p.distance > 500).name);
```

*Uzaklıklar milyon km. sort'taki a ile b'nin yerini değiştirip tekrar çalıştır.*

## Görevler

### Görev 1: İki kat hız

`speeds` dizisindeki her hızı **2 ile çarparak** `doubled` adında yeni bir dizi oluştur. `map` kullan; `speeds` değişmesin.

**Başlangıç kodu:**

```js
const speeds = [3, 7, 12, 5];

// doubled dizisini map ile oluştur

console.log(doubled);
```

**İpuçları:**

1. const doubled = speeds.map((s) => ...);
2. Her eleman için s * 2 döndür.

<details><summary>Çözüm</summary>

```js
const speeds = [3, 7, 12, 5];

// doubled dizisini map ile oluştur
const doubled = speeds.map((s) => s * 2);

console.log(doubled);
```

</details>

### Görev 2: Sinyal ayıklama

Radar sinyallerini ayıkla:

1. `strong`: 30 ve üstü sinyallerden oluşan yeni dizi (`filter`).
2. `firstWeak`: 10'dan küçük **ilk** sinyal (`find`).

**Başlangıç kodu:**

```js
const signals = [12, 45, 8, 60, 33, 5];

// strong ve firstWeak'i oluştur

console.log("Güçlü:", strong);
console.log("İlk zayıf:", firstWeak);
```

**İpuçları:**

1. signals.filter((s) => s >= 30)
2. find ilk uyan elemanı verir: signals.find((s) => s < 10)

<details><summary>Çözüm</summary>

```js
const signals = [12, 45, 8, 60, 33, 5];

// strong ve firstWeak'i oluştur
const strong = signals.filter((s) => s >= 30);
const firstWeak = signals.find((s) => s < 10);

console.log("Güçlü:", strong);
console.log("İlk zayıf:", firstWeak);
```

</details>

### Görev 3: Toplam yakıt

`reduce` ile bütün depolardaki yakıtı topla ve `total` değişkenine koy. Sonra ortalamayı `average` değişkenine hesapla (toplam / depo sayısı).

Çıktı: `Toplam yakıt: 105` ve `Ortalama: 35`

**Başlangıç kodu:**

```js
const tanks = [
  { name: "A", fuel: 42 },
  { name: "B", fuel: 27 },
  { name: "C", fuel: 36 },
];

// total ve average'ı hesapla

console.log("Toplam yakıt:", total);
console.log("Ortalama:", average);
```

**İpuçları:**

1. tanks.reduce((sum, t) => sum + t.fuel, 0)
2. Başlangıç değeri 0'ı unutma.
3. average = total / tanks.length

<details><summary>Çözüm</summary>

```js
const tanks = [
  { name: "A", fuel: 42 },
  { name: "B", fuel: 27 },
  { name: "C", fuel: 36 },
];

// total ve average'ı hesapla
const total = tanks.reduce((sum, t) => sum + t.fuel, 0);
const average = total / tanks.length;

console.log("Toplam yakıt:", total);
console.log("Ortalama:", average);
```

</details>

## Challenge: Skor analizi

`scores` dizisini analiz et, ama `scores` **değişmesin**:

- `sorted`: küçükten büyüğe sıralı kopya (`[7, 9, 25, 40, 100]`). Karşılaştırma fonksiyonu kullan!
- `top3`: en yüksek 3 skor, büyükten küçüğe (`[100, 40, 25]`). İpucu: `slice(0, 3)` ilk 3 elemanı verir.
- `allPassed`: bütün skorlar 5'ten büyük mü? (`every`)
- `hasPerfect`: 100 olan bir skor var mı? (`some`)

**Başlangıç kodu:**

```js
const scores = [40, 100, 9, 25, 7];

// sorted, top3, allPassed, hasPerfect

console.log(sorted, top3, allPassed, hasPerfect);
```

**İpuçları:**

1. Kopya için önce slice(): scores.slice().sort((a, b) => a - b)
2. Büyükten küçüğe: (a, b) => b - a
3. scores.every((s) => s > 5)

<details><summary>Çözüm</summary>

```js
const scores = [40, 100, 9, 25, 7];

// sorted, top3, allPassed, hasPerfect
const sorted = scores.slice().sort((a, b) => a - b);
const top3 = scores.slice().sort((a, b) => b - a).slice(0, 3);
const allPassed = scores.every((s) => s > 5);
const hasPerfect = scores.some((s) => s === 100);

console.log(sorted, top3, allPassed, hasPerfect);
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Skor tablosu**

### Yıldız Avcısı: Skor tablosu

Oyunun skor tablosunu hazırla. `leaderboard(list)` fonksiyonunu yaz:

- Oyuncuları skora göre **büyükten küçüğe** sıralasın,
- `"1. Ece - 150"` biçiminde metinlerden oluşan bir **dizi** döndürsün (sıra numarası `map`'in ikinci parametresinden),
- Asıl `list` dizisinin sırası değişmesin (önce `slice()` ile kopyala).

**Başlangıç kodu:**

```js
const players = [
  { name: "Ada", score: 120 },
  { name: "Can", score: 85 },
  { name: "Ece", score: 150 },
  { name: "Mert", score: 95 },
];

function leaderboard(list) {
  // kopyala, sırala, sonra map ile metne çevir
}

console.log(leaderboard(players));
```

**İpuçları:**

1. list.slice().sort((a, b) => b.score - a.score)
2. .map((p, i) => `${i + 1}. ${p.name} - ${p.score}`)
3. Fonksiyonda return yazmayı unutma.

<details><summary>Çözüm</summary>

```js
const players = [
  { name: "Ada", score: 120 },
  { name: "Can", score: 85 },
  { name: "Ece", score: 150 },
  { name: "Mert", score: 95 },
];

function leaderboard(list) {
  // kopyala, sırala, sonra map ile metne çevir
  return list
    .slice()
    .sort((a, b) => b.score - a.score)
    .map((p, i) => `${i + 1}. ${p.name} - ${p.score}`);
}

console.log(leaderboard(players));
```

</details>

### Kişisel Web Sitem: Projeleri filtrele

Sitende projelerini etikete göre süzeceğiz. `titlesByTag(list, tag)` fonksiyonunu yaz: etiketi (`tag`) verilen etikete eşit olan projelerin yalnızca **başlıklarını** dizi olarak döndürsün (`filter` + `map`).

Örnek: `titlesByTag(projects, "js")` → `["Hesap Makinesi", "Yıldız Oyunu"]`

**Başlangıç kodu:**

```js
const projects = [
  { title: "Hesap Makinesi", tag: "js", year: 2026 },
  { title: "Kedi Galerisi", tag: "html", year: 2025 },
  { title: "Yıldız Oyunu", tag: "js", year: 2026 },
  { title: "Tarif Defteri", tag: "css", year: 2025 },
];

function titlesByTag(list, tag) {
  // filter ile süz, map ile başlıkları al
}

console.log("js projelerim:", titlesByTag(projects, "js"));
```

**İpuçları:**

1. list.filter((p) => p.tag === tag)
2. Sonuna .map((p) => p.title) ekle.
3. return yazmayı unutma.

<details><summary>Çözüm</summary>

```js
const projects = [
  { title: "Hesap Makinesi", tag: "js", year: 2026 },
  { title: "Kedi Galerisi", tag: "html", year: 2025 },
  { title: "Yıldız Oyunu", tag: "js", year: 2026 },
  { title: "Tarif Defteri", tag: "css", year: 2025 },
];

function titlesByTag(list, tag) {
  // filter ile süz, map ile başlıkları al
  return list.filter((p) => p.tag === tag).map((p) => p.title);
}

console.log("js projelerim:", titlesByTag(projects, "js"));
```

</details>

### Çalışma Asistanım: Çalışma istatistiği

Asistan günün istatistiğini çıkarsın. `stats(list)` fonksiyonunu yaz; `{ done, minutes }` nesnesi döndürsün:

- `done`: tamamlanan (`done: true`) görev sayısı (`filter`),
- `minutes`: **tamamlanan** görevlerin toplam dakikası (`reduce`).

Çıktı: `Tamamlanan: 3 görev, 80 dakika`

**Başlangıç kodu:**

```js
const tasks = [
  { title: "Matematik ödevi", minutes: 40, done: true },
  { title: "Fizik tekrarı", minutes: 30, done: false },
  { title: "İngilizce kelimeler", minutes: 15, done: true },
  { title: "Kitap okuma", minutes: 25, done: true },
];

function stats(list) {
  // tamamlananları süz, dakikalarını topla
}

const s = stats(tasks);
console.log(`Tamamlanan: ${s.done} görev, ${s.minutes} dakika`);
```

**İpuçları:**

1. const finished = list.filter((t) => t.done);
2. finished.reduce((sum, t) => sum + t.minutes, 0)
3. return { done: finished.length, minutes: ... };

<details><summary>Çözüm</summary>

```js
const tasks = [
  { title: "Matematik ödevi", minutes: 40, done: true },
  { title: "Fizik tekrarı", minutes: 30, done: false },
  { title: "İngilizce kelimeler", minutes: 15, done: true },
  { title: "Kitap okuma", minutes: 25, done: true },
];

function stats(list) {
  // tamamlananları süz, dakikalarını topla
  const finished = list.filter((t) => t.done);
  const minutes = finished.reduce((sum, t) => sum + t.minutes, 0);
  return { done: finished.length, minutes };
}

const s = stats(tasks);
console.log(`Tamamlanan: ${s.done} görev, ${s.minutes} dakika`);
```

</details>

### Bilgi Yarışması: Sonuç özeti

Yarışma bitince sonuç özeti gösterilecek. `summary(list)` fonksiyonu şu nesneyi döndürsün:

- `correctCount`: doğru cevap sayısı (`filter`),
- `score`: doğru cevapların puanlarının toplamı (`reduce`),
- `missed`: yanlış cevaplanan soruların **metinleri** (`filter` + `map`).

**Başlangıç kodu:**

```js
const answers = [
  { question: "Ay hangi gezegenin uydusu?", correct: true, points: 10 },
  { question: "En büyük gezegen hangisi?", correct: false, points: 10 },
  { question: "Kızıl gezegen hangisi?", correct: true, points: 20 },
  { question: "Halkalı gezegen hangisi?", correct: false, points: 20 },
];

function summary(list) {
  // correctCount, score, missed
}

console.log(summary(answers));
```

**İpuçları:**

1. const right = list.filter((a) => a.correct);
2. score: right.reduce((sum, a) => sum + a.points, 0)
3. missed: list.filter((a) => !a.correct).map((a) => a.question)

<details><summary>Çözüm</summary>

```js
const answers = [
  { question: "Ay hangi gezegenin uydusu?", correct: true, points: 10 },
  { question: "En büyük gezegen hangisi?", correct: false, points: 10 },
  { question: "Kızıl gezegen hangisi?", correct: true, points: 20 },
  { question: "Halkalı gezegen hangisi?", correct: false, points: 20 },
];

function summary(list) {
  // correctCount, score, missed
  const right = list.filter((a) => a.correct);
  return {
    correctCount: right.length,
    score: right.reduce((sum, a) => sum + a.points, 0),
    missed: list.filter((a) => !a.correct).map((a) => a.question),
  };
}

console.log(summary(answers));
```

</details>
