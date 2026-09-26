# Video senaryosu: Gün 5, Koşullar

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~151 sn

Döngü Ayı'na yaklaşırken koda karar verme yeteneği kazandırıyoruz: if, else if, else, üçlü operatör, switch ve doğru-yanlış sayılan değerler.

Ders metni: [gun-05.md](../gunler/gun-05.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 10 sn | el-sallama (sag) |
| 2 | kod | 15 sn | isaret (alt-sag) |
| 3 | kod | 15 sn | isaret (alt-sag) |
| 4 | kod | 13 sn | konusma (alt-sag) |
| 5 | kod | 16 sn | isaret (alt-sag) |
| 6 | kod | 14 sn | konusma (alt-sag) |
| 7 | hata | 15 sn | sasirma (sag) |
| 8 | soru | 10 sn | dusunme (sag) |
| 9 | cikti | 10 sn | mutlu (sag) |
| 10 | gorev | 12 sn | isaret (sol) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 10 sn | tebrik (sag) |

## Sahne 1: acilis (10 sn)

**Seslendirme:** Selam, ben Kodi! Döngü Ayı'na yaklaşıyoruz. Uzayda her an bir karar gerekir: yakıt azsa uyar, hava kötüyse bekle. Peki kodumuz nasıl karar verecek?

**Ekranda başlık:** Gün 5: Koşullar

**Görsel:** `gorseller/javascript/bolgeler/ay.webp`

**Maskot:** el-sallama pozu, sag

*Yönetmen notu: Döngü Ayı ekranın ortasında büyüyerek yaklaşır.*

## Sahne 2: kod (15 sn)

**Seslendirme:** if, yani eğer: parantezdeki koşul doğruysa süslü parantezin içi çalışır. else, yani değilse: koşul yanlışsa bu kısım çalışır. Yakıt 15, yirmiden az, o yüzden uyarı geldi.

**Ekranda başlık:** if ve else

**Kod** (vurgulanan satırlar: 2, 4):

```js
const fuel = 15;
if (fuel < 20) {
  console.log("Uyarı: yakıt az!");
} else {
  console.log("Yakıt yeterli.");
}
```

**Çıktı:**

```text
Uyarı: yakıt az!
```

**Maskot:** isaret pozu, alt-sag

*Yönetmen notu: İçeri yazılmış satırlar hafifçe parlar: iki boşluk girinti.*

## Sahne 3: kod (15 sn)

**Seslendirme:** Daha fazla seçenek için else if kullanırız. Koşullar yukarıdan aşağı sınanır, ilk doğru olan çalışır ve gerisine bakılmaz. Hız 70, yüzü geçmiyor ama elliyi geçiyor.

**Ekranda başlık:** else if: birden fazla seçenek

**Kod** (vurgulanan satırlar: 4, 5):

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

**Çıktı:**

```text
İyi hız.
```

**Maskot:** isaret pozu, alt-sag

## Sahne 4: kod (13 sn)

**Seslendirme:** İki seçenekten birini seçmenin kısa yolu üçlü operatör: koşul, soru işareti, doğruysa değer, iki nokta, yanlışsa değer. Can kalmadığı için oyun bitti.

**Ekranda başlık:** Üçlü operatör: koşul ? a : b

**Kod** (vurgulanan satırlar: 2):

```js
const lives = 0;
const message = lives > 0 ? "Devam!" : "Oyun bitti";
console.log(message);
```

**Çıktı:**

```text
Oyun bitti
```

**Maskot:** konusma pozu, alt-sag

## Sahne 5: kod (16 sn)

**Seslendirme:** Bir değeri birçok seçenekle karşılaştırırken switch düzenli görünür. Eşleşen case çalışır, hiçbiri eşleşmezse default. break'i unutma, yoksa alttaki seçenek de çalışır!

**Ekranda başlık:** switch

**Kod** (vurgulanan satırlar: 4, 6, 7):

```js
const planet = "Mars";
let info;
switch (planet) {
  case "Mars":
    info = "Kızıl gezegen";
    break;
  default:
    info = "Bilinmiyor";
}
console.log(info);
```

**Çıktı:**

```text
Kızıl gezegen
```

**Maskot:** isaret pozu, alt-sag

## Sahne 6: kod (14 sn)

**Seslendirme:** if içine her değer yazılabilir. Sıfır, boş metin, null, undefined ve NaN yanlış sayılır, geri kalan her şey doğru. Pilot adı boş olduğu için else çalıştı.

**Ekranda başlık:** Doğru ve yanlış sayılan değerler

**Ekranda maddeler:**

- Yanlış sayılanlar: 0, "", null, undefined, NaN

**Kod** (vurgulanan satırlar: 1, 2):

```js
const pilot = "";
if (pilot) {
  console.log("Hoş geldin,", pilot);
} else {
  console.log("Pilot adı boş!");
}
```

**Çıktı:**

```text
Pilot adı boş!
```

**Maskot:** konusma pozu, alt-sag

## Sahne 7: hata (15 sn)

**Seslendirme:** Sık yapılan hata: if içinde tek eşittir yazmak. Tek eşittir karşılaştırmaz, değer atar! fuel const olduğu için hata aldık; let olsaydı yakıt sessizce sıfırlanırdı. Karşılaştırmada hep üç eşittir.

**Ekranda başlık:** = ile === aynı değil

**Kod** (vurgulanan satırlar: 2):

```js
const fuel = 50;
if (fuel = 0) {
  console.log("Yakıt bitti!");
}
```

**Çıktı:**

```text
TypeError: Assignment to constant variable.
```

**Maskot:** sasirma pozu, sag

## Sahne 8: soru (10 sn)

**Seslendirme:** Skor 90. İki koşul da doğru gibi görünüyor. Sence hangi mesaj yazılır? Durdur ve düşün.

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```js
const score = 90;
if (score > 50) {
  console.log("Geçti");
} else if (score > 80) {
  console.log("Harika");
} else {
  console.log("Tekrar dene");
}
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (10 sn)

**Seslendirme:** Cevap Geçti! İlk koşul doğru olduğu için orada durduk, Harika satırına hiç bakılmadı. Koşulların sırası çok önemli.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 2, 3):

```js
const score = 90;
if (score > 50) {
  console.log("Geçti");
} else if (score > 80) {
  console.log("Harika");
} else {
  console.log("Tekrar dene");
}
```

**Çıktı:**

```text
Geçti
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (12 sn)

**Seslendirme:** Görevlerin: oksijen azalınca alarm ver, puana göre harf notu hesapla ve üçlü operatörle kokpitin gece mi gündüz mü olduğuna karar ver.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Oksijen alarmı
- Görev 2: Not hesaplayıcı
- Görev 3: Gece mi gündüz mü?

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (11 sn)

**Seslendirme:** Özet: if ve else ile karar verir, else if ile seçenek eklersin. Kısa kararlar için üçlü operatör, çok seçenek için switch var.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- if / else if / else: ilk doğru koşul çalışır
- koşul ? a : b ile kısa karar
- switch'te break'i unutma

**Maskot:** on pozu, sag

## Sahne 12: kapanis (10 sn)

**Seslendirme:** Artık kodun karar verebiliyor, bravo! Yarın kargo bölmesini dolduruyoruz. Onlarca eşyayı tek bir listede tutmayı öğreneceğiz: diziler.

**Ekranda başlık:** Yarın: Diziler

**Görsel:** `maskotlar/kodi-javascript/kahraman.png`

**Maskot:** tebrik pozu, sag
