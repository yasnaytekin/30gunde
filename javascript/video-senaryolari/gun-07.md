# Video senaryosu: Gün 7, Döngüler

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~158 sn

Döngü Ayı'nın yörüngesinde işleri tekrarlatıyoruz: for, while ve for...of döngüleri, döngüyle toplam biriktirmek, break ve continue.

Ders metni: [gun-07.md](../gunler/gun-07.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 10 sn | el-sallama (sag) |
| 2 | kod | 16 sn | isaret (alt-sag) |
| 3 | kod | 15 sn | konusma (alt-sag) |
| 4 | kod | 12 sn | isaret (alt-sag) |
| 5 | kod | 12 sn | isaret (alt-sag) |
| 6 | kod | 14 sn | mutlu (alt-sag) |
| 7 | kod | 14 sn | konusma (alt-sag) |
| 8 | hata | 14 sn | sasirma (sag) |
| 9 | soru | 9 sn | dusunme (sag) |
| 10 | cikti | 9 sn | mutlu (sag) |
| 11 | gorev | 12 sn | isaret (sol) |
| 12 | ozet | 11 sn | on (sag) |
| 13 | kapanis | 10 sn | tebrik (sag) |

## Sahne 1: acilis (10 sn)

**Seslendirme:** Selam, ben Kodi! Döngü Ayı'nın yörüngesine girdik. Burada her şey tekrar eder: tur, tur, bir tur daha. Aynı komutu yüz kez yazar mısın? Ben yazmam!

**Ekranda başlık:** Gün 7: Döngüler

**Görsel:** `gorseller/javascript/bolgeler/ay.webp`

**Maskot:** el-sallama pozu, sag

*Yönetmen notu: Roket Ay'ın etrafında tur atar.*

## Sahne 2: kod (16 sn)

**Seslendirme:** for bir işi belirli sayıda tekrarlar. Parantezde üç parça var: başlangıç bir kez çalışır, koşul her turdan önce sınanır, i artı artı de her turun sonunda sayacı artırır.

**Ekranda başlık:** for döngüsü

**Kod** (vurgulanan satırlar: 1):

```js
for (let i = 1; i <= 3; i++) {
  console.log("Tur", i);
}
```

**Çıktı:**

```text
Tur 1
Tur 2
Tur 3
```

**Maskot:** isaret pozu, alt-sag

*Yönetmen notu: Birinci satırdaki üç parça sırayla farklı renklerle vurgulanır.*

## Sahne 3: kod (15 sn)

**Seslendirme:** while, koşul doğru olduğu sürece tekrar eder. Kaç tur süreceğini bilmediğimizde işe yarar. Koşul turdan önce sınandığı için yakıt 10 iken bir tur daha atıldı ve eksiye düştü.

**Ekranda başlık:** while döngüsü

**Kod** (vurgulanan satırlar: 2, 3):

```js
let fuel = 100;
while (fuel > 0) {
  fuel -= 30;
  console.log("Kalan yakıt:", fuel);
}
```

**Çıktı:**

```text
Kalan yakıt: 70
Kalan yakıt: 40
Kalan yakıt: 10
Kalan yakıt: -20
```

**Maskot:** konusma pozu, alt-sag

## Sahne 4: kod (12 sn)

**Seslendirme:** Bir dizinin her elemanına bakmanın en kolay yolu for of. Her turda sıradaki gezegen planet değişkenine gelir.

**Ekranda başlık:** for...of ile dizi dolaşmak

**Kod** (vurgulanan satırlar: 2):

```js
const planets = ["Merkür", "Venüs", "Dünya"];
for (const planet of planets) {
  console.log(planet);
}
```

**Çıktı:**

```text
Merkür
Venüs
Dünya
```

**Maskot:** isaret pozu, alt-sag

## Sahne 5: kod (12 sn)

**Seslendirme:** Sıra numarası da lazımsa klasik for kullan. i sıfırdan başlar ve length'e kadar gider; ekrana yazarken bir ekliyoruz.

**Ekranda başlık:** İndeksle dolaşmak

**Kod** (vurgulanan satırlar: 2, 3):

```js
const planets = ["Merkür", "Venüs", "Dünya"];
for (let i = 0; i < planets.length; i++) {
  console.log(i + 1, planets[i]);
}
```

**Çıktı:**

```text
1 Merkür
2 Venüs
3 Dünya
```

**Maskot:** isaret pozu, alt-sag

## Sahne 6: kod (14 sn)

**Seslendirme:** Toplam biriktirmek için döngüden önce sıfırla başlayan bir değişken açarız. Her turda depodaki yakıtı ona ekleriz. Üç depo, toplam yüz litre!

**Ekranda başlık:** Toplam biriktirmek

**Kod** (vurgulanan satırlar: 2, 4):

```js
const tanks = [40, 25, 35];
let total = 0;
for (const tank of tanks) {
  total += tank;
}
console.log(total);
```

**Çıktı:**

```text
100
```

**Maskot:** mutlu pozu, alt-sag

## Sahne 7: kod (14 sn)

**Seslendirme:** continue bu turu atlar ve sonrakine geçer, break ise döngüyü hemen bitirir. Üç atlandı, beşte de döngü durdu.

**Ekranda başlık:** break ve continue

**Kod** (vurgulanan satırlar: 3, 6):

```js
for (let i = 1; i <= 6; i++) {
  if (i === 3) {
    continue;
  }
  if (i === 5) {
    break;
  }
  console.log(i);
}
```

**Çıktı:**

```text
1
2
4
```

**Maskot:** konusma pozu, alt-sag

## Sahne 8: hata (14 sn)

**Seslendirme:** En tehlikeli hata: sonsuz döngü! Burada yakıt hiç azalmıyor, koşul hep doğru kalıyor ve program donuyor. Döngünün içinde koşulu değiştiren bir şey mutlaka olmalı.

**Ekranda başlık:** Sonsuz döngü

**Kod** (vurgulanan satırlar: 2):

```js
let fuel = 100;
while (fuel > 0) {
  console.log("Kalan yakıt:", fuel);
}
```

**Çıktı:**

```text
Kalan yakıt: 100
Kalan yakıt: 100
Kalan yakıt: 100
... (hiç bitmez, program donar)
```

**Maskot:** sasirma pozu, sag

*Yönetmen notu: Çıktı alanı durmadan akar, sonra ekran kırmızı bir 'donmuş' efektiyle kesilir.*

## Sahne 9: soru (9 sn)

**Seslendirme:** Her turda iki yıldız topluyoruz. Döngü kaç tur döner ve sonunda kaç yıldızımız olur?

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```js
let stars = 0;
for (let i = 0; i < 4; i++) {
  stars += 2;
}
console.log(stars);
```

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (9 sn)

**Seslendirme:** Sekiz yıldız! i sıfır, bir, iki ve üç için dört tur döndü; her turda iki eklendi.

**Ekranda başlık:** Cevap

**Kod**:

```js
let stars = 0;
for (let i = 0; i < 4; i++) {
  stars += 2;
}
console.log(stars);
```

**Çıktı:**

```text
8
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (12 sn)

**Seslendirme:** Görevlerin: tek bir console.log ile ondan geriye say, yakıt depolarını döngüyle topla ve while ile kaç yörünge turu atabileceğini bul.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Geri sayım
- Görev 2: Yakıt depoları
- Görev 3: Yörünge turları

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (11 sn)

**Seslendirme:** Özet: for belirli sayıda tekrarlar, while koşul doğru oldukça. for of diziyi dolaşır. Biriktireceğin değişkeni döngüden önce aç.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- for: başlangıç; koşul; artış
- while: koşulu içeride değiştir
- for...of, biriktirme, break ve continue

**Maskot:** on pozu, sag

## Sahne 13: kapanis (10 sn)

**Seslendirme:** Yörünge turları tamam, tebrikler! Yarın sık kullandığımız komutları bir ada paketleyip istediğimiz kadar çağıracağız: fonksiyonlar.

**Ekranda başlık:** Yarın: Fonksiyonlar

**Görsel:** `maskotlar/kodi-javascript/kahraman.png`

**Maskot:** tebrik pozu, sag
