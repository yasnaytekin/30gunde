# Video senaryosu: Gün 6, Diziler

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~142 sn

Kargo bölmesindeki eşyaları tek bir dizide tutuyoruz: indeksle elemana ulaşmak, push, pop, unshift, shift ile ekleyip çıkarmak, includes ve indexOf ile aramak, slice, splice ve join.

Ders metni: [gun-06.md](../gunler/gun-06.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 10 sn | el-sallama (sag) |
| 2 | kod | 16 sn | isaret (alt-sag) |
| 3 | kod | 17 sn | konusma (alt-sag) |
| 4 | kod | 14 sn | isaret (alt-sag) |
| 5 | kod | 17 sn | konusma (alt-sag) |
| 6 | hata | 15 sn | sasirma (sag) |
| 7 | soru | 10 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 12 sn | isaret (sol) |
| 10 | ozet | 11 sn | on (sag) |
| 11 | kapanis | 10 sn | tebrik (sag) |

## Sahne 1: acilis (10 sn)

**Seslendirme:** Selam, ben Kodi! Döngü Ayı'nda kargo bölmesi doluyor: yakıt hücreleri, kalkanlar, haritalar. Her eşyaya ayrı bir değişken mi açacağız? Hiç sanmıyorum!

**Ekranda başlık:** Gün 6: Diziler

**Görsel:** `gorseller/javascript/bolgeler/ay.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (16 sn)

**Seslendirme:** Dizi, birçok değeri sırayla tutan bir listedir. Köşeli parantezle yazılır. Sayma yine sıfırdan başlar. length eleman sayısını verir, son eleman da length eksi bir sırasındadır.

**Ekranda başlık:** Dizi: sıralı bir liste

**Kod** (vurgulanan satırlar: 1, 4):

```js
const planets = ["Merkür", "Venüs", "Dünya"];
console.log(planets[0]);
console.log(planets.length);
console.log(planets[planets.length - 1]);
```

**Çıktı:**

```text
Merkür
3
Dünya
```

**Maskot:** isaret pozu, alt-sag

*Yönetmen notu: Üç gezegen kutucuk olarak dizilir, altlarında 0, 1, 2 numaraları belirir.*

## Sahne 3: kod (17 sn)

**Seslendirme:** push sona, unshift başa ekler. pop sondakini çıkarıp bize verir, shift de baştakini. Dizi const olsa bile eleman ekleyip çıkarabiliriz; const sadece başka bir diziye bağlanmayı engeller.

**Ekranda başlık:** Eklemek ve çıkarmak

**Kod** (vurgulanan satırlar: 2, 3, 5):

```js
const cargo = ["yakıt", "kalkan"];
cargo.push("harita");
cargo.unshift("su");
console.log(cargo);
const last = cargo.pop();
console.log(last, cargo.length);
```

**Çıktı:**

```text
[ 'su', 'yakıt', 'kalkan', 'harita' ]
harita 3
```

**Maskot:** konusma pozu, alt-sag

## Sahne 4: kod (14 sn)

**Seslendirme:** Aramak için iki metot var. includes, eleman dizide var mı diye bakar. indexOf ise kaçıncı sırada olduğunu söyler; bulamazsa eksi bir verir.

**Ekranda başlık:** Aramak: includes ve indexOf

**Kod** (vurgulanan satırlar: 2, 3, 4):

```js
const team = ["Deniz", "Ece", "Kaan"];
console.log(team.includes("Ece"));
console.log(team.indexOf("Kaan"));
console.log(team.indexOf("Zeynep"));
```

**Çıktı:**

```text
true
2
-1
```

**Maskot:** isaret pozu, alt-sag

## Sahne 5: kod (17 sn)

**Seslendirme:** slice diziyi bozmadan bir parça kopyalar. splice ise diziyi değiştirir: önce Ay'ı sildik, sonra aynı yere Venüs'ü ekledik. join de hepsini aralarına ok koyarak tek metin yaptı.

**Ekranda başlık:** slice, splice ve join

**Kod** (vurgulanan satırlar: 2, 3, 4, 5):

```js
const route = ["Dünya", "Ay", "Mars", "Jüpiter"];
console.log(route.slice(1, 3));
route.splice(1, 1);
route.splice(1, 0, "Venüs");
console.log(route.join(" → "));
```

**Çıktı:**

```text
[ 'Ay', 'Mars' ]
Dünya → Venüs → Mars → Jüpiter
```

**Maskot:** konusma pozu, alt-sag

## Sahne 6: hata (15 sn)

**Seslendirme:** Klasik hata: üç elemanlı dizide üç numaralı sırayı istemek. O sıra boş, undefined geldi. Üstelik onu büyük harfe çevirmeye çalışınca kod çöktü. Son eleman length eksi birde!

**Ekranda başlık:** Olmayan sıra: undefined

**Kod** (vurgulanan satırlar: 2, 3):

```js
const planets = ["Merkür", "Venüs", "Dünya"];
console.log(planets[3]);
console.log(planets[3].toUpperCase());
```

**Çıktı:**

```text
undefined
TypeError: Cannot read properties of undefined (reading 'toUpperCase')
```

**Maskot:** sasirma pozu, sag

## Sahne 7: soru (10 sn)

**Seslendirme:** Rotaya Jüpiter'i ekledik. Sence Mars kaçıncı sırada, ve son satırda hangi metin çıkar? Durdur ve düşün.

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```js
const route = ["Dünya", "Ay", "Mars"];
route.push("Jüpiter");
console.log(route.indexOf("Mars"));
console.log(route.slice(0, 2).join(" + "));
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Mars 2 numaralı sırada, çünkü sayma sıfırdan başlıyor. slice ilk iki elemanı aldı, join de onları artıyla birleştirdi.

**Ekranda başlık:** Cevap

**Kod**:

```js
const route = ["Dünya", "Ay", "Mars"];
route.push("Jüpiter");
console.log(route.indexOf("Mars"));
console.log(route.slice(0, 2).join(" + "));
```

**Çıktı:**

```text
2
Dünya + Ay
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (12 sn)

**Seslendirme:** Görevlerin: gezegen listesinin ilk ve son elemanını bul, kargoyu metotlarla yeniden düzenle ve mürettebat listesinde arama yap.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Gezegen listesi
- Görev 2: Kargo yükleme
- Görev 3: Mürettebat araması

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (11 sn)

**Seslendirme:** Özet: dizi sıralı bir listedir ve sıfırdan sayılır. push, pop, unshift, shift ile değişir. includes ve indexOf ile ararız.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- [ ] ile dizi, [0] ilk eleman, length eleman sayısı
- push / pop / unshift / shift
- includes, indexOf, slice, splice, join

**Maskot:** on pozu, sag

## Sahne 11: kapanis (10 sn)

**Seslendirme:** Kargo yerleşti, harikasın! Yarın Döngü Ayı'nın yörüngesine giriyoruz. Aynı işi yüz kez yazmadan tekrarlatmayı öğreneceğiz: döngüler.

**Ekranda başlık:** Yarın: Döngüler

**Görsel:** `maskotlar/kodi-javascript/kahraman.png`

**Maskot:** tebrik pozu, sag
