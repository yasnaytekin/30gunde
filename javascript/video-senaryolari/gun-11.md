# Video senaryosu: Gün 11, map, filter, reduce

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~161 sn

Nebulanın derinlerinde radar yüzlerce yıldız listeliyor: map ile dönüştürmek, filter ve find ile süzmek, reduce ile tek değere indirmek, sort ile doğru sıralamak ve metotları zincirlemek.

Ders metni: [gun-11.md](../gunler/gun-11.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 11 sn | el-sallama (sag) |
| 2 | kod | 17 sn | isaret (alt-sag) |
| 3 | kod | 18 sn | konusma (alt-sag) |
| 4 | kod | 17 sn | isaret (alt-sag) |
| 5 | hata | 14 sn | sasirma (sag) |
| 6 | kod | 16 sn | mutlu (alt-sag) |
| 7 | kod | 16 sn | isaret (alt-sag) |
| 8 | soru | 10 sn | dusunme (sag) |
| 9 | cikti | 9 sn | mutlu (sag) |
| 10 | gorev | 12 sn | isaret (sol) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 10 sn | tebrik (sag) |

## Sahne 1: acilis (11 sn)

**Seslendirme:** Selam, ben Kodi! Fonksiyon Nebulası'nın derinlerindeyiz. Radar yüzlerce yıldız listeliyor. Hepsini tek tek döngüyle mi gezeceğiz? Hayır, dizilere süper güçler vereceğiz!

**Ekranda başlık:** Gün 11: map, filter, reduce

**Görsel:** `gorseller/javascript/bolgeler/nebula.webp`

**Maskot:** el-sallama pozu, sag

*Yönetmen notu: Radar ekranında çok sayıda yıldız noktası belirir.*

## Sahne 2: kod (17 sn)

**Seslendirme:** map, dizinin her elemanına bir fonksiyon uygular ve sonuçlardan yeni bir dizi yapar. Asıl dizi değişmez, bak tanks aynı kaldı. Fonksiyon ikinci değer olarak elemanın sırasını da alabilir.

**Ekranda başlık:** map: her elemanı dönüştür

**Kod** (vurgulanan satırlar: 2, 7):

```js
const tanks = [80, 15, 60];
const percent = tanks.map((t) => t + "%");
console.log(percent);
console.log(tanks);

const names = ["Ada", "Can"];
console.log(names.map((name, i) => (i + 1) + ". " + name));
```

**Çıktı:**

```text
[ '80%', '15%', '60%' ]
[ 80, 15, 60 ]
[ '1. Ada', '2. Can' ]
```

**Maskot:** isaret pozu, alt-sag

## Sahne 3: kod (18 sn)

**Seslendirme:** filter, koşula uyanlardan yeni bir dizi yapar. find ise dizi değil, ilk uyan elemanı verir; hiçbiri uymazsa undefined. some en az biri uyuyor mu, every hepsi uyuyor mu diye sorar.

**Ekranda başlık:** filter, find, some, every

**Kod** (vurgulanan satırlar: 2, 3, 5, 6):

```js
const fuel = [80, 15, 60, 5];
console.log(fuel.filter((f) => f < 20));
console.log(fuel.find((f) => f < 20));
console.log(fuel.find((f) => f > 100));
console.log(fuel.some((f) => f < 10));
console.log(fuel.every((f) => f > 0));
```

**Çıktı:**

```text
[ 15, 5 ]
15
undefined
true
true
```

**Maskot:** konusma pozu, alt-sag

## Sahne 4: kod (17 sn)

**Seslendirme:** reduce bütün diziyi tek bir değere indirger. sum şimdiye kadar biriken değer, s sıradaki eleman. Sıfırdan başlar: üç, sekiz, on. Başlangıç değerini yazmayı unutma!

**Ekranda başlık:** reduce: tek bir değere indirgemek

**Kod** (vurgulanan satırlar: 2):

```js
const stars = [3, 5, 2];
const total = stars.reduce((sum, s) => sum + s, 0);
console.log(total);
```

**Çıktı:**

```text
10
```

**Maskot:** isaret pozu, alt-sag

*Yönetmen notu: Adımlar animasyonla belirir: 0 + 3 = 3, 3 + 5 = 8, 8 + 2 = 10.*

## Sahne 5: hata (14 sn)

**Seslendirme:** Tuzağa dikkat! sort elemanları metin gibi karşılaştırır. Metinde bir, dokuzdan önce gelir; bu yüzden yüz, dokuzun önüne geçti. Hata mesajı yok ama sonuç yanlış.

**Ekranda başlık:** sort sayıları metin gibi sıralar

**Kod** (vurgulanan satırlar: 1):

```js
console.log([10, 9, 100].sort());
```

**Çıktı:**

```text
[ 10, 100, 9 ]
```

**Maskot:** sasirma pozu, sag

## Sahne 6: kod (16 sn)

**Seslendirme:** Çözüm: bir karşılaştırma fonksiyonu vermek. a eksi b küçükten büyüğe, b eksi a büyükten küçüğe sıralar. sort asıl diziyi değiştirdiği için önce slice ile kopyaladık.

**Ekranda başlık:** Sayıları doğru sıralamak

**Kod** (vurgulanan satırlar: 2, 3):

```js
const nums = [10, 9, 100];
console.log(nums.slice().sort((a, b) => a - b));
console.log(nums.slice().sort((a, b) => b - a));
console.log(nums);
```

**Çıktı:**

```text
[ 9, 10, 100 ]
[ 100, 10, 9 ]
[ 10, 9, 100 ]
```

**Maskot:** mutlu pozu, alt-sag

## Sahne 7: kod (16 sn)

**Seslendirme:** Bu metotlar dizi döndürdüğü için arka arkaya zincirlenebilir. Kopyaladık, uzaklığa göre sıraladık, sadece adları aldık ve okla birleştirdik. Uzaklıklar milyon kilometre.

**Ekranda başlık:** Zincirleme

**Kod** (vurgulanan satırlar: 7, 8, 9):

```js
const planets = [
  { name: "Mars", distance: 228 },
  { name: "Merkür", distance: 58 },
  { name: "Venüs", distance: 108 },
];
const order = planets
  .slice()
  .sort((a, b) => a.distance - b.distance)
  .map((p) => p.name);
console.log(order.join(" → "));
```

**Çıktı:**

```text
Merkür → Venüs → Mars
```

**Maskot:** isaret pozu, alt-sag

## Sahne 8: soru (10 sn)

**Seslendirme:** Önce elliden büyük skorları süzüyoruz, sonra her birini beşe bölüyoruz. Sence sonuç dizisi ne olur?

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```js
const scores = [40, 75, 90, 20];
const result = scores
  .filter((s) => s > 50)
  .map((s) => s / 5);
console.log(result);
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (9 sn)

**Seslendirme:** On beş ve on sekiz! filter yetmiş beş ile doksanı bıraktı, map de ikisini beşe böldü.

**Ekranda başlık:** Cevap

**Kod**:

```js
const scores = [40, 75, 90, 20];
const result = scores
  .filter((s) => s > 50)
  .map((s) => s / 5);
console.log(result);
```

**Çıktı:**

```text
[ 15, 18 ]
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (12 sn)

**Seslendirme:** Görevlerin: hızları iki katına çıkaran yeni bir dizi yap, radar sinyallerini ayıkla ve depolardaki yakıtın toplamını ve ortalamasını bul.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: İki kat hız
- Görev 2: Sinyal ayıklama
- Görev 3: Toplam yakıt

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (11 sn)

**Seslendirme:** Özet: map dönüştürür, filter süzer, reduce tek değere indirir. Sayıları sıralarken sort'a mutlaka karşılaştırma fonksiyonu ver.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- map dönüştürür, filter süzer, find ilkini bulur
- reduce tek değer üretir: başlangıç değerini yaz
- sort((a, b) => a - b) ve zincirleme

**Maskot:** on pozu, sag

## Sahne 12: kapanis (10 sn)

**Seslendirme:** Radar ustası oldun, bravo! Yarın nebulanın ucundaki istasyona kenetleniyoruz. Set, Map ve verinin ortak dili JSON bizi bekliyor.

**Ekranda başlık:** Yarın: Set, Map ve JSON

**Görsel:** `maskotlar/kodi-javascript/kahraman.png`

**Maskot:** tebrik pozu, sag
