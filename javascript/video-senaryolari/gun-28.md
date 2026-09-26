# Video senaryosu: Gün 28, Temiz kod

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~164 sn

Kodi, JavaScript Yıldızı'nın ışığında anlamlı isimleri, küçük ve tekrarsız fonksiyonları, sihirli sayılar yerine sabitleri, erken dönüşü, parçalamayı ve varsayılan değerleri anlatıyor.

Ders metni: [gun-28.md](../gunler/gun-28.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | el-sallama (sag) |
| 2 | kod | 17 sn | isaret (sag) |
| 3 | kod | 18 sn | konusma (sol) |
| 4 | kod | 17 sn | isaret (sag) |
| 5 | kod | 16 sn | konusma (sol) |
| 6 | kod | 18 sn | isaret (sag) |
| 7 | hata | 13 sn | uzgun (sag) |
| 8 | soru | 9 sn | dusunme (sag) |
| 9 | cikti | 8 sn | mutlu (sag) |
| 10 | gorev | 13 sn | isaret (sol) |
| 11 | ozet | 12 sn | konusma (sag) |
| 12 | kapanis | 11 sn | el-sallama (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Kodi! JavaScript Yıldızı'nın ışığı göründü! Usta kaptanlar kodlarını yalnızca çalışır değil, okunur yazar. Bugün dağınık kodu toplayıp temiz kod yazmayı öğreniyoruz!

**Ekranda başlık:** Gün 28: Temiz kod

**Görsel:** `gorseller/javascript/bolgeler/yildiz.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (17 sn)

**Seslendirme:** İki kod da aynı işi yapıyor. Ama hangisi ne yaptığını anlatıyor? Değişken adı ne tuttuğunu, fonksiyon adı ne yaptığını söylesin. Doğru yanlış tutan adlar soru gibi okunsun: isReady, canLaunch.

**Ekranda başlık:** İsimler bir şey anlatmalı

**Kod** (vurgulanan satırlar: 5, 6):

```js
// Anlaşılmıyor
const d = 7;
function c(a) { return a * 24; }
// Kendini anlatıyor
const daysLeft = 7;
function daysToHours(days) { return days * 24; }
console.log(daysToHours(daysLeft));
```

**Çıktı:**

```text
168
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (18 sn)

**Seslendirme:** Kodun ortasındaki açıklamasız sayılara sihirli sayı denir. On ne, elli ne? Onlara isim ver. Hiç değişmeyen ayarları büyük harfle yazmak yaygın bir alışkanlıktır. Davranış aynı, okunuş çok farklı.

**Ekranda başlık:** Sihirli sayılar yerine sabitler

**Kod** (vurgulanan satırlar: 2, 3, 6):

```js
// Önce: function x(a, b) { return a * 10 + (b ? 50 : 0); }
const STAR_POINTS = 10;
const BONUS_POINTS = 50;
function calculateScore(stars, hasBonus) {
  const bonus = hasBonus ? BONUS_POINTS : 0;
  return stars * STAR_POINTS + bonus;
}
console.log(calculateScore(3, true));
```

**Çıktı:**

```text
80
```

**Maskot:** konusma pozu, sol

## Sahne 4: kod (17 sn)

**Seslendirme:** Her fonksiyonun tek bir işi olsun. Aynı kodu iki kez kopyaladıysan dur ve onu bir fonksiyona çevir. Buna DRY denir: kendini tekrarlama. Değişiklik gerekince tek bir yeri düzeltirsin.

**Ekranda başlık:** Küçük fonksiyonlar, tekrarsız kod

**Kod** (vurgulanan satırlar: 1, 5):

```js
function scoreLine(name, score) {
  return `${name.padEnd(5, ".")} ${score} puan`;
}
const pilots = [["Ada", 12], ["Can", 30]];
pilots.forEach(([name, score]) => console.log(scoreLine(name, score)));
```

**Çıktı:**

```text
Ada.. 12 puan
Can.. 30 puan
```

**Maskot:** isaret pozu, sag

## Sahne 5: kod (16 sn)

**Seslendirme:** İç içe if'ler yerine erken dönüş kullan. Önce sorunlu durumları eleyip fonksiyondan çık, asıl işi en sona bırak. Kod yukarıdan aşağı düz okunur, hiç else kalmaz.

**Ekranda başlık:** Erken dönüş

**Kod** (vurgulanan satırlar: 2, 3, 4):

```js
function openHatch(pilot) {
  if (!pilot) return "Kimse yok";
  if (!pilot.hasKey) return "Anahtar yok";
  return "Kapak açıldı";
}
console.log(openHatch(null));
console.log(openHatch({ hasKey: true }));
```

**Çıktı:**

```text
Kimse yok
Kapak açıldı
```

**Maskot:** konusma pozu, sol

## Sahne 6: kod (18 sn)

**Seslendirme:** Parçalama bir nesneden ya da diziden değerleri tek satırda çıkarır. Parametrede de kullanılır ve varsayılan değer alabilir. Mert'in seviyesi verilmediği için bir kullanıldı.

**Ekranda başlık:** Parçalama ve varsayılan değer

**Kod** (vurgulanan satırlar: 2, 4):

```js
const pilot = { name: "Deniz", level: 4, ship: "Kartal" };
const { name, ship } = pilot;
console.log(`${name}, ${ship} gemisinde.`);
function greet({ name, level = 1 }) {
  return `Merhaba ${name}, seviye ${level}`;
}
console.log(greet({ name: "Mert" }));
```

**Çıktı:**

```text
Deniz, Kartal gemisinde.
Merhaba Mert, seviye 1
```

**Maskot:** isaret pozu, sag

## Sahne 7: hata (13 sn)

**Seslendirme:** Sık hata: kodun ne yaptığını tekrar eden yorumlar yazmak. İyi bir yorum ne yapıldığını değil, neden öyle yapıldığını anlatır.

**Ekranda başlık:** Sık hata: gereksiz yorum

**Kod** (vurgulanan satırlar: 2):

```js
let lap = 0; // 0'dan başlıyoruz çünkü ilk tur ısınma turu (yararlı)
lap = lap + 1; // lap'i 1 artır (gereksiz)
```

**Maskot:** uzgun pozu, sag

## Sahne 8: soru (9 sn)

**Seslendirme:** Soru zamanı! Diziden ilk iki değeri parçalama ile alıyoruz. Sence ne yazar?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```js
const [gold, silver] = ["Ada", "Can", "Ece"];
console.log(gold, silver);
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (8 sn)

**Seslendirme:** Cevap: Ada Can! Dizi parçalamada sıra önemlidir. Ece'ye bir ad vermediğimiz için alınmadı.

**Ekranda başlık:** Cevap

**Kod**:

```js
const [gold, silver] = ["Ada", "Can", "Ece"];
console.log(gold, silver);
```

**Çıktı:**

```text
Ada Can
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görev zamanı! Dağınık bir yakıt hesabındaki sihirli sayılara isim vereceksin, kopyalanmış satırları tek fonksiyona toplayacaksın ve iç içe if'leri erken dönüşle düzleştireceksin.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Sihirli sayılara isim ver
- Görev 2: Tekrarı kaldır
- Görev 3: Erken dönüş

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (12 sn)

**Seslendirme:** Özetleyelim: anlatan isimler seç, fonksiyonlar küçük ve tekrarsız olsun. Sayılara isim ver, erken dönüş kullan, parçalama ile değerleri kısaca al.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- Anlamlı isimler: isReady, loadTasks
- Tek iş, DRY, SABİTLER, erken dönüş
- Parçalama ve varsayılan değer

**Maskot:** konusma pozu, sag

## Sahne 12: kapanis (11 sn)

**Seslendirme:** Kodun artık parıl parıl! Yarın projeni toparlıyoruz: düğmeler ve klavye aynı işi yapacak, oyun telefonda da oynanacak. Görüşürüz!

**Ekranda başlık:** Yarın: Projeyi toparlama

**Görsel:** `gorseller/javascript/arka-plan/bg-space-wide.webp`

**Maskot:** el-sallama pozu, orta
