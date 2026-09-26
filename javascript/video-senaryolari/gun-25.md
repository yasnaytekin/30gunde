# Video senaryosu: Gün 25, Promise ve async/await

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~176 sn

Kodi, Async İstasyonu'nda asenkron işleri, Promise oluşturmayı, then/catch ile sonucu ve hatayı almayı, async/await ile beklemeyi ve Promise.all ile işleri birlikte yürütmeyi anlatıyor.

Ders metni: [gun-25.md](../gunler/gun-25.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | el-sallama (sag) |
| 2 | kod | 15 sn | isaret (sag) |
| 3 | kod | 17 sn | konusma (sol) |
| 4 | kod | 16 sn | isaret (sag) |
| 5 | kod | 16 sn | konusma (sol) |
| 6 | kod | 15 sn | isaret (sag) |
| 7 | kod | 17 sn | mutlu (sol) |
| 8 | hata | 14 sn | sasirma (sag) |
| 9 | soru | 9 sn | dusunme (sag) |
| 10 | cikti | 9 sn | mutlu (sag) |
| 11 | gorev | 13 sn | isaret (sol) |
| 12 | ozet | 12 sn | konusma (sag) |
| 13 | kapanis | 11 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Kodi! İstasyonda hiçbir iş anında bitmiyor: yakıt dolumu sürüyor, sinyaller gecikiyor. JavaScript beklemeyi nasıl öğrenir? Bugün Promise ve async await ile tanışıyoruz!

**Ekranda başlık:** Gün 25: Promise ve async/await

**Görsel:** `gorseller/javascript/bolgeler/istasyon.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (15 sn)

**Seslendirme:** Bazı işler zaman alır. JavaScript bu sırada durup beklemez, diğer işlere devam eder ve uzun iş bitince haber alır. Bu yüzden çıktı sırası bir, iki, üç olur. Bu tür işlere asenkron denir.

**Ekranda başlık:** Neden bekleme gerekir?

**Kod** (vurgulanan satırlar: 2):

```js
console.log("1. Sinyal gönderildi");
setTimeout(() => console.log("3. Cevap geldi"), 100);
console.log("2. Beklerken başka işler");
```

**Çıktı:**

```text
1. Sinyal gönderildi
2. Beklerken başka işler
3. Cevap geldi
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (17 sn)

**Seslendirme:** Promise, iş bitince sana sonucu vereceğim sözüdür. Önce bekler, sonra ya tamamlanır ya da reddedilir. resolve sözü tutar ve then içindeki fonksiyon o değerle çalışır.

**Ekranda başlık:** Promise: bir söz

**Kod** (vurgulanan satırlar: 2, 3, 6):

```js
function wait(ms) {
  return new Promise((resolve) => {
    setTimeout(() => resolve("hazır"), ms);
  });
}
wait(100).then((result) => console.log("Sonuç:", result));
```

**Çıktı:**

```text
Sonuç: hazır
```

**Maskot:** konusma pozu, sol

## Sahne 4: kod (16 sn)

**Seslendirme:** reject ise sözü bozar. O zaman then atlanır, catch içindeki fonksiyon hatayla çalışır. Burada yedinci seviye yok, bu yüzden söz bozuluyor.

**Ekranda başlık:** reject ve catch

**Kod** (vurgulanan satırlar: 3, 9):

```js
function loadLevel(n) {
  return new Promise((resolve, reject) => {
    if (n > 5) reject(new Error(`Seviye ${n} bulunamadı`));
    else resolve(`Seviye ${n} yüklendi`);
  });
}
loadLevel(7)
  .then((text) => console.log(text))
  .catch((error) => console.log("Hata:", error.message));
```

**Çıktı:**

```text
Hata: Seviye 7 bulunamadı
```

**Maskot:** isaret pozu, sag

## Sahne 5: kod (16 sn)

**Seslendirme:** then zincirleri uzayınca okumak zorlaşır. async bir fonksiyonun içinde await, Promise bitene kadar bekler. Kod yukarıdan aşağı, sırayla okunur. async fonksiyon da bir Promise döndürür.

**Ekranda başlık:** async ve await

**Kod** (vurgulanan satırlar: 4, 6, 10):

```js
function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
async function countdown() {
  console.log("Geri sayım...");
  await wait(100);
  console.log("Kalkış!");
  return "yörüngede";
}
console.log(await countdown());
```

**Çıktı:**

```text
Geri sayım...
Kalkış!
yörüngede
```

**Maskot:** konusma pozu, sol

## Sahne 6: kod (15 sn)

**Seslendirme:** Reddedilen bir Promise'i await edersen hata fırlatılır. Dün öğrendiğimiz try ve catch ile yakalarız. Beşinci seviye yüklenir, dokuzuncu ise yakalanır.

**Ekranda başlık:** await ve try/catch

**Kod** (vurgulanan satırlar: 3, 5):

```js
async function start(n) {
  try {
    console.log(await loadLevel(n));
  } catch (error) {
    console.log("Sorun:", error.message);
  }
}
await start(5);
await start(9);
```

**Çıktı:**

```text
Seviye 5 yüklendi
Sorun: Seviye 9 bulunamadı
```

**Maskot:** isaret pozu, sag

## Sahne 7: kod (17 sn)

**Seslendirme:** Birbirini beklemesi gerekmeyen işleri sırayla beklemek zaman kaybıdır. Promise.all hepsini aynı anda başlatır ve sonuçları aynı sırayla bir dizi olarak verir. Süre toplam değil, en uzunu kadar!

**Ekranda başlık:** Promise.all: birlikte bekle

**Kod** (vurgulanan satırlar: 5):

```js
function loadPart(name, ms) {
  return new Promise((resolve) => setTimeout(() => resolve(name + " hazır"), ms));
}
const start = Date.now();
const parts = await Promise.all([loadPart("Motor", 150), loadPart("Kanat", 100)]);
console.log(parts);
console.log("250 ms'den kısa sürdü:", Date.now() - start < 250);
```

**Çıktı:**

```text
[ 'Motor hazır', 'Kanat hazır' ]
250 ms'den kısa sürdü: true
```

**Maskot:** mutlu pozu, sol

## Sahne 8: hata (14 sn)

**Seslendirme:** Sık hata: await'i unutmak. O zaman değişkene sonuç değil, henüz bekleyen bir Promise gelir. Hata mesajı çıkmaz ama ekranda beklediğin yazı yerine garip bir şey görürsün.

**Ekranda başlık:** Sık hata: await'i unutmak

**Kod** (vurgulanan satırlar: 1):

```js
const level = loadPart("Seviye 1", 100); // await yok!
console.log(level);
```

**Çıktı:**

```text
Promise { <pending> }
```

**Maskot:** sasirma pozu, sag

## Sahne 9: soru (9 sn)

**Seslendirme:** Soru zamanı! Bekleme süresi sıfır. Sence A, B ve C hangi sırayla yazılır?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```js
console.log("A");
wait(0).then(() => console.log("B"));
console.log("C");
```

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (9 sn)

**Seslendirme:** Cevap A, C, B! Söz sıfır milisaniyede bile olsa sonradan tutulur. Şimdiki kod bitmeden then çalışmaz.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 5):

```js
function wait(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}
console.log("A");
wait(0).then(() => console.log("B"));
console.log("C");
```

**Çıktı:**

```text
A
C
B
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (13 sn)

**Seslendirme:** Görev zamanı! Kendi bekleme sözünü yazacaksın, async bir yakıt dolumu fonksiyonu yapacaksın ve motor çok ısınırsa hatayı yakalayan bir uçuş öncesi kontrolü kuracaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Bekleme sözü
- Görev 2: Yakıt dolumu
- Görev 3: Motor kontrolü

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (12 sn)

**Seslendirme:** Özetleyelim: Promise bir sözdür; resolve tutar, reject bozar. Sonucu then ya da await ile al, hatayı catch ile yakala. Bağımsız işleri Promise.all ile birlikte beklet.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- new Promise((resolve, reject) => ...)
- then / catch  ·  async + await + try/catch
- Promise.all([...]): birlikte, aynı sırayla

**Maskot:** konusma pozu, sag

## Sahne 13: kapanis (11 sn)

**Seslendirme:** Bekleme ustası oldun! Yarın bu bilgiyi gerçek bir işte kullanacağız: fetch ile bir sunucudan veri isteyeceğiz. Görüşürüz!

**Ekranda başlık:** Yarın: fetch ve API

**Görsel:** `gorseller/javascript/arka-plan/bg-space-wide.webp`

**Maskot:** tebrik pozu, orta
