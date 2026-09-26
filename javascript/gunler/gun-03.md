# Gün 3: Operatörler ve Math

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Kalkış Üssü  ·  **Maskot:** Kodi

**Bugünün hedefi:** Aritmetik, karşılaştırma ve mantıksal operatörleri kullanmak; Math ile hesap yapmak

> Roket yola çıkmak üzere ama önce hesaplar yapılmalı: Ay'a kaç saatte varılır, yakıt yeter mi, hava uygun mu? Bugün JavaScript'i bir hesap makinesi ve karar vericiye dönüştüreceğiz.

![Kalkış Üssü](../../gorseller/javascript/bolgeler/kalkis.webp)

## Konu anlatımı

### Aritmetik operatörler

| İşlem | Operatör | Örnek | Sonuç |
| --- | --- | --- | --- |
| Toplama | `+` | `7 + 2` | `9` |
| Çıkarma | `-` | `7 - 2` | `5` |
| Çarpma | `*` | `7 * 2` | `14` |
| Bölme | `/` | `7 / 2` | `3.5` |
| Kalan (mod) | `%` | `7 % 2` | `1` |
| Üs | `**` | `2 ** 3` | `8` |

Kısayollar: `score += 10` demek `score = score + 10` demektir. `stars++` bir artırır.

### Karşılaştırma: === ve arkadaşları

Karşılaştırmaların sonucu her zaman `true` ya da `false` olur:

```js
console.log(10 > 3);      // true
console.log(5 === 5);     // true  (eşit mi?)
console.log(5 !== 5);     // false (farklı mı?)
console.log("5" === 5);   // false: biri metin, biri sayı
```

Eşitlik için hep **üç eşittir** `===` kullan. İki eşittir `==` türleri gizlice dönüştürür ve şaşırtıcı sonuçlar verir.

### Mantıksal operatörler

- `&&` (ve): ikisi de doğruysa `true`
- `||` (veya): en az biri doğruysa `true`
- `!` (değil): tersine çevirir

```js
const fuel = 80;
const weather = "açık";
console.log(fuel >= 50 && weather === "açık");  // true
```

### Math ile hesap

- `Math.round(4.6)` → `5` (en yakın tam sayıya yuvarlar)
- `Math.floor(4.6)` → `4` (aşağı yuvarlar)
- `Math.max(3, 9, 5)` → `9`, `Math.min(...)` en küçüğü verir
- `Math.random()` → 0 ile 1 arasında rastgele bir sayı

Zar atmak: `Math.floor(Math.random() * 6) + 1` bize 1 ile 6 arasında rastgele bir tam sayı verir.

## Örnekler

### Kutulara yerleştirme

```js
const items = 20;
const perBox = 6;
console.log("Dolu kutu:", Math.floor(items / perBox));
console.log("Artan:", items % perBox);
```

*% kalanı verir: 20'yi 6'ya bölünce 2 artar.*

### Zar at

```js
const dice = Math.floor(Math.random() * 6) + 1;
console.log("Zar:", dice);
```

*Birkaç kez çalıştır: her seferinde farklı sayı gelebilir.*

## Görevler

### Görev 1: Ay yolculuğu

Ay 384400 km uzakta, roketin hızı saatte 40000 km.

- `hours` değişkenine yolculuğun kaç saat süreceğini hesapla: mesafe / hız, sonucu `Math.round` ile yuvarla.
- `Ay'a 10 saatte varırız.` yazdır (sayı `hours`'tan gelsin).

**Başlangıç kodu:**

```js
const distance = 384400;
const speed = 40000;

// hours'u hesapla

console.log("Ay'a", hours, "saatte varırız.");
```

**İpuçları:**

1. Süre = mesafe / hız
2. const hours = Math.round(distance / speed);

<details><summary>Çözüm</summary>

```js
const distance = 384400;
const speed = 40000;

// hours'u hesapla
const hours = Math.round(distance / speed);

console.log("Ay'a", hours, "saatte varırız.");
```

</details>

### Görev 2: Kargo kutuları

47 malzeme var, her kutuya 6 tane sığıyor.

- `fullBoxes`: kaç kutu tamamen dolar? (`Math.floor` ile)
- `leftover`: kaç malzeme artar? (`%` ile)

**Başlangıç kodu:**

```js
const items = 47;
const perBox = 6;

// fullBoxes ve leftover'ı hesapla

console.log(fullBoxes, "kutu dolu,", leftover, "malzeme arttı");
```

**İpuçları:**

1. Math.floor(items / perBox) bölümün tam kısmını verir.
2. items % perBox kalanı verir.

<details><summary>Çözüm</summary>

```js
const items = 47;
const perBox = 6;

// fullBoxes ve leftover'ı hesapla
const fullBoxes = Math.floor(items / perBox);
const leftover = items % perBox;

console.log(fullBoxes, "kutu dolu,", leftover, "malzeme arttı");
```

</details>

### Görev 3: Kalkış izni

Kalkış için iki şart var: yakıt **en az 50** olmalı **ve** hava `"açık"` olmalı.

`canLaunch` değişkenine bu iki şartı `&&` ile birleştirerek yaz ve yazdır.

**Başlangıç kodu:**

```js
const fuel = 80;
const weather = "açık";

// canLaunch: iki şart da doğru mu?

console.log("Kalkış izni:", canLaunch);
```

**İpuçları:**

1. "en az 50" demek >= 50 demek.
2. const canLaunch = fuel >= 50 && weather === "açık";

<details><summary>Çözüm</summary>

```js
const fuel = 80;
const weather = "açık";

// canLaunch: iki şart da doğru mu?
const canLaunch = fuel >= 50 && weather === "açık";

console.log("Kalkış izni:", canLaunch);
```

</details>

## Challenge: Çift zar

İki zar at ve topla:

- `dice1` ve `dice2`: her biri 1 ile 6 arasında rastgele tam sayı
- `total`: ikisinin toplamı

**Başlangıç kodu:**

```js
// İki zar at

console.log(dice1, "+", dice2, "=", total);
```

**İpuçları:**

1. Math.random() * 6 sonucu 0 ile 6 arasında (6 hariç) bir sayıdır.
2. Math.floor(Math.random() * 6) + 1

<details><summary>Çözüm</summary>

```js
// İki zar at
const dice1 = Math.floor(Math.random() * 6) + 1;
const dice2 = Math.floor(Math.random() * 6) + 1;
const total = dice1 + dice2;

console.log(dice1, "+", dice2, "=", total);
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Skor hesabı**

### Yıldız Avcısı: Skor hesabı

Her yıldız 10 puan. 5 ya da daha fazla yıldız toplayan bonus kazanır.

- `score`: yıldız sayısı çarpı `starPoints`
- `hasBonus`: yıldız sayısı 5 ya da daha fazla mı? (`true`/`false`)

Beklenen çıktı: `Skor: 70 | Bonus: true`

**Başlangıç kodu:**

```js
let stars = 7;
const starPoints = 10;

// score ve hasBonus'u hesapla

console.log("Skor:", score, "| Bonus:", hasBonus);
```

**İpuçları:**

1. const score = stars * starPoints;
2. Karşılaştırmanın sonucu zaten true/false: stars >= 5

<details><summary>Çözüm</summary>

```js
let stars = 7;
const starPoints = 10;

// score ve hasBonus'u hesapla
const score = stars * starPoints;
const hasBonus = stars >= 5;

console.log("Skor:", score, "| Bonus:", hasBonus);
```

</details>

### Kişisel Web Sitem: Ziyaretçi istatistiği

Siten bir haftada 1250 ziyaretçi aldı.

- `dailyAverage`: günlük ortalama ziyaretçi (`Math.round` ile yuvarla)
- `isPopular`: ortalama 100'den büyük mü?

Beklenen çıktı: `Günlük ortalama: 179 | Popüler: true`

**Başlangıç kodu:**

```js
const weeklyVisits = 1250;
const days = 7;

// dailyAverage ve isPopular'ı hesapla

console.log("Günlük ortalama:", dailyAverage, "| Popüler:", isPopular);
```

**İpuçları:**

1. Ortalama = toplam / gün sayısı
2. const dailyAverage = Math.round(weeklyVisits / days);

<details><summary>Çözüm</summary>

```js
const weeklyVisits = 1250;
const days = 7;

// dailyAverage ve isPopular'ı hesapla
const dailyAverage = Math.round(weeklyVisits / days);
const isPopular = dailyAverage > 100;

console.log("Günlük ortalama:", dailyAverage, "| Popüler:", isPopular);
```

</details>

### Çalışma Asistanım: Çalışma süresi

Bugün 135 dakika çalıştın. Bunu saat ve dakikaya çevir:

- `hours`: tam saat (`Math.floor` ile)
- `minutes`: kalan dakika (`%` ile)

Beklenen çıktı: `2 saat 15 dakika çalıştın`

**Başlangıç kodu:**

```js
const studied = 135;

// hours ve minutes'u hesapla

console.log(hours, "saat", minutes, "dakika çalıştın");
```

**İpuçları:**

1. 1 saat = 60 dakika.
2. Math.floor(studied / 60) ve studied % 60

<details><summary>Çözüm</summary>

```js
const studied = 135;

// hours ve minutes'u hesapla
const hours = Math.floor(studied / 60);
const minutes = studied % 60;

console.log(hours, "saat", minutes, "dakika çalıştın");
```

</details>

### Bilgi Yarışması: Başarı yüzdesi

Yarışmacı 5 sorudan 4'ünü bildi.

- `percent`: başarı yüzdesi (doğru / toplam * 100)
- `passed`: yüzde 60 ya da daha fazla mı?

Beklenen çıktı: `Başarı: 80 | Geçti: true`

**Başlangıç kodu:**

```js
const correct = 4;
const total = 5;

// percent ve passed'i hesapla

console.log("Başarı:", percent, "| Geçti:", passed);
```

**İpuçları:**

1. Yüzde = doğru / toplam * 100
2. const passed = percent >= 60;

<details><summary>Çözüm</summary>

```js
const correct = 4;
const total = 5;

// percent ve passed'i hesapla
const percent = correct / total * 100;
const passed = percent >= 60;

console.log("Başarı:", percent, "| Geçti:", passed);
```

</details>
