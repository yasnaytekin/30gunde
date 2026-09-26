# Video senaryosu: Gün 3, Operatörler ve Math

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~151 sn

Kalkıştan önceki hesapları yapıyoruz: aritmetik, karşılaştırma ve mantıksal operatörler ile Math'in yuvarlama, en büyük ve rastgele sayı araçları.

Ders metni: [gun-03.md](../gunler/gun-03.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 10 sn | el-sallama (sag) |
| 2 | kod | 16 sn | isaret (alt-sag) |
| 3 | kod | 15 sn | isaret (alt-sag) |
| 4 | kod | 15 sn | konusma (alt-sag) |
| 5 | kod | 13 sn | isaret (alt-sag) |
| 6 | kod | 14 sn | mutlu (alt-sag) |
| 7 | hata | 14 sn | uzgun (sag) |
| 8 | soru | 10 sn | dusunme (sag) |
| 9 | cikti | 10 sn | mutlu (sag) |
| 10 | gorev | 13 sn | isaret (sol) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 10 sn | tebrik (sag) |

## Sahne 1: acilis (10 sn)

**Seslendirme:** Selam, ben Kodi! Roket kalkmak üzere ama önce hesap lazım. Ay'a kaç saatte varırız? Yakıt yeter mi? Bugün JavaScript'i bir hesap makinesine çeviriyoruz.

**Ekranda başlık:** Gün 3: Operatörler ve Math

**Görsel:** `gorseller/javascript/bolgeler/kalkis.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (16 sn)

**Seslendirme:** Toplama, çıkarma, çarpma, bölme bildiğin gibi. Yüzde işareti bölmeden kalanı verir, iki yıldız üs alır. Artı eşittir 5 ekler, artı artı ise bir artırır. Skor 16 oldu!

**Ekranda başlık:** Aritmetik operatörler

**Kod** (vurgulanan satırlar: 2, 5, 6):

```js
console.log(7 / 2);
console.log(7 % 2);
console.log(2 ** 3);
let score = 10;
score += 5;
score++;
console.log(score);
```

**Çıktı:**

```text
3.5
1
8
16
```

**Maskot:** isaret pozu, alt-sag

## Sahne 3: kod (15 sn)

**Seslendirme:** Karşılaştırmaların sonucu hep true ya da false olur. Eşitlik için üç eşittir kullan. Son satıra bak: biri metin, biri sayı, bu yüzden eşit değiller.

**Ekranda başlık:** Karşılaştırma: === ve arkadaşları

**Kod** (vurgulanan satırlar: 4):

```js
console.log(10 > 3);
console.log(5 === 5);
console.log(5 !== 5);
console.log("5" === 5);
```

**Çıktı:**

```text
true
true
false
false
```

**Maskot:** isaret pozu, alt-sag

*Yönetmen notu: Ekranın köşesinde küçük bir uyarı: '== yerine hep === kullan'.*

## Sahne 4: kod (15 sn)

**Seslendirme:** Ve işareti iki şartın ikisi de doğruysa true verir. Veya işareti birinin doğru olması yeterli der. Ünlem ise tersine çevirir. Kalkış için yakıt da hava da tamam!

**Ekranda başlık:** Mantıksal operatörler: && || !

**Kod** (vurgulanan satırlar: 3, 4, 5):

```js
const fuel = 80;
const weather = "açık";
console.log(fuel >= 50 && weather === "açık");
console.log(fuel > 90 || weather === "açık");
console.log(!true);
```

**Çıktı:**

```text
true
true
false
```

**Maskot:** konusma pozu, alt-sag

## Sahne 5: kod (13 sn)

**Seslendirme:** Math, JavaScript'in hazır hesap kutusu. round en yakın tam sayıya yuvarlar, floor aşağı yuvarlar, max da en büyüğünü bulur.

**Ekranda başlık:** Math ile hesap

**Kod** (vurgulanan satırlar: 1, 2, 3):

```js
console.log(Math.round(4.6));
console.log(Math.floor(4.6));
console.log(Math.max(3, 9, 5));
```

**Çıktı:**

```text
5
4
9
```

**Maskot:** isaret pozu, alt-sag

## Sahne 6: kod (14 sn)

**Seslendirme:** Math.random sıfır ile bir arasında rastgele bir sayı verir. Altıyla çarpıp aşağı yuvarlar, bir eklersek bir ile altı arasında bir zar elde ederiz. Her çalıştırmada farklı!

**Ekranda başlık:** Zar at

**Kod** (vurgulanan satırlar: 1):

```js
const dice = Math.floor(Math.random() * 6) + 1;
console.log("Zar:", dice);
```

**Çıktı:**

```text
Zar: 4   (her çalıştırmada 1 ile 6 arasında değişir)
```

**Maskot:** mutlu pozu, alt-sag

*Yönetmen notu: Çıktı alanında sayı birkaç kez hızla değişir, sonra durur.*

## Sahne 7: hata (14 sn)

**Seslendirme:** Sık yapılan bir hata: Math'i küçük harfle yazmak. JavaScript math diye bir şey tanımıyor. Unutma, büyük küçük harf fark eder: Math büyük M ile yazılır.

**Ekranda başlık:** Büyük harf önemli

**Kod** (vurgulanan satırlar: 1):

```js
console.log(math.round(4.6));
```

**Çıktı:**

```text
ReferenceError: math is not defined
```

**Maskot:** uzgun pozu, sag

## Sahne 8: soru (10 sn)

**Seslendirme:** 20 malzemeyi altışarlı kutulara yerleştiriyoruz. Kaç kutu dolar, kaç malzeme artar? Durdur ve hesapla.

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```js
const items = 20;
const perBox = 6;
console.log("Dolu kutu:", Math.floor(items / perBox));
console.log("Artan:", items % perBox);
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (10 sn)

**Seslendirme:** Üç kutu dolar, iki malzeme artar. floor bölümü aşağı yuvarladı, yüzde işareti de kalanı verdi.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 3, 4):

```js
const items = 20;
const perBox = 6;
console.log("Dolu kutu:", Math.floor(items / perBox));
console.log("Artan:", items % perBox);
```

**Çıktı:**

```text
Dolu kutu: 3
Artan: 2
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görevlerin hazır! Ay yolculuğunun kaç saat süreceğini hesapla, kargo kutularını say ve iki şartı birleştirerek kalkış iznini ver.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Ay yolculuğu
- Görev 2: Kargo kutuları
- Görev 3: Kalkış izni

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (11 sn)

**Seslendirme:** Bugün hesap yapmayı, üç eşittirle karşılaştırmayı, şartları ve ile veya ile birleştirmeyi ve Math araçlarını öğrendik.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- + - * / % ** ve += ile hesap
- === ile karşılaştır, sonuç true/false
- && || ! ve Math.round, floor, max, random

**Maskot:** on pozu, sag

## Sahne 12: kapanis (10 sn)

**Seslendirme:** Hesaplar tamam kaptan! Yarın roketimiz istasyonlarla mesajlaşacak. Metinleri birleştirmeyi ve dönüştürmeyi öğreneceğiz.

**Ekranda başlık:** Yarın: Metinlerle çalışmak

**Görsel:** `maskotlar/kodi-javascript/kahraman.png`

**Maskot:** tebrik pozu, sag
