# Video senaryosu: Gün 18, Zamanlayıcılar

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~156 sn

Kodi, Olay Kuşağı'nda setTimeout, setInterval ve clearInterval ile zamanlanmış işleri, üst üste binen sayaçları önlemeyi ve Date ile saat göstermeyi anlatıyor.

Ders metni: [gun-18.md](../gunler/gun-18.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 11 sn | el-sallama (sag) |
| 2 | kod | 15 sn | isaret (sag) |
| 3 | kod | 16 sn | konusma (sag) |
| 4 | hata | 14 sn | sasirma (sag) |
| 5 | kod | 18 sn | isaret (sol) |
| 6 | kod | 15 sn | konusma (sag) |
| 7 | kod | 14 sn | mutlu (sol) |
| 8 | soru | 9 sn | dusunme (sag) |
| 9 | cikti | 9 sn | mutlu (sag) |
| 10 | gorev | 13 sn | isaret (sol) |
| 11 | ozet | 12 sn | konusma (sag) |
| 12 | kapanis | 10 sn | tebrik (orta) |

## Sahne 1: acilis (11 sn)

**Seslendirme:** Selam, ben Kodi! Olay Kuşağı'nda zaman da bir olaydır: her saniye bir tık! Bir işi bir saniye sonra, ya da her saniye yaptırabilir miyiz? Bugün zamanlayıcıları öğreniyoruz!

**Ekranda başlık:** Gün 18: Zamanlayıcılar

**Görsel:** `gorseller/javascript/bolgeler/kusak.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (15 sn)

**Seslendirme:** setTimeout bir fonksiyonu bir kez, verdiğin milisaniye sonra çalıştırır. Bin milisaniye bir saniyedir. Dikkat et: setTimeout beklemez! Fonksiyonu kenara koyar ve kod hemen devam eder.

**Ekranda başlık:** setTimeout: biraz sonra

**Kod** (vurgulanan satırlar: 2, 4, 5):

```js
console.log("Geri sayım başladı");
setTimeout(() => {
  console.log("Kalkış!");
}, 1000);
console.log("Bu satır önce yazılır!");
```

**Çıktı:**

```text
Geri sayım başladı
Bu satır önce yazılır!
Kalkış!
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: Çıktının son satırı bir saniye gecikmeyle belirir.*

## Sahne 3: kod (16 sn)

**Seslendirme:** setInterval ise fonksiyonu her seferinde yeniden çalıştırır, ta ki sen durdurana kadar. Bize bir kimlik numarası döndürür; beşinci tıkta onu clearInterval'a verip sayacı durduruyoruz.

**Ekranda başlık:** setInterval ve clearInterval

**Kod** (vurgulanan satırlar: 2, 5):

```js
let count = 0;
const timer = setInterval(() => {
  count++;
  console.log("Tık", count);
  if (count === 5) clearInterval(timer);
}, 200);
```

**Çıktı:**

```text
Tık 1
Tık 2
Tık 3
Tık 4
Tık 5
```

**Maskot:** konusma pozu, sag

## Sahne 4: hata (14 sn)

**Seslendirme:** Sık hata: Başlat düğmesine iki kez basılınca iki ayrı sayaç çalışır ve süre iki kat hızlı akar! Hata mesajı çıkmaz, sadece sayı garip biçimde hızlanır.

**Ekranda başlık:** Sık hata: üst üste binen sayaçlar

**Kod** (vurgulanan satırlar: 2):

```js
startBtn.addEventListener("click", () => {
  setInterval(tick, 1000); // her tıklamada yeni sayaç!
});
```

**Çıktı:**

```text
İki tıklamadan sonra süre saniyede 2 artar.
```

**Maskot:** sasirma pozu, sag

## Sahne 5: kod (18 sn)

**Seslendirme:** Çözüm: sayaç zaten çalışıyorsa yenisini kurma. timer null değilse start hemen çıkar. Burada start'ı iki kez çağırdık ama yalnızca tek sayaç çalıştı. Durdururken de timer'ı tekrar null yapıyoruz.

**Ekranda başlık:** Çözüm: tek sayaç

**Kod** (vurgulanan satırlar: 5, 8, 9, 10):

```js
let timer = null;
let n = 0;
function tick() { n++; console.log("Tık", n); if (n === 3) stop(); }
function start() {
  if (timer !== null) return; // zaten çalışıyor
  timer = setInterval(tick, 100);
}
function stop() { clearInterval(timer); timer = null; }
start();
start();
```

**Çıktı:**

```text
Tık 1
Tık 2
Tık 3
```

**Maskot:** isaret pozu, sol

## Sahne 6: kod (15 sn)

**Seslendirme:** new Date şu anı verir; içinden saati, dakikayı, saniyeyi alabiliriz. padStart tek haneli sayının başına sıfır ekler. Aylar sıfırdan başlar, yani Ocak sıfırdır!

**Ekranda başlık:** Date ve padStart

**Kod** (vurgulanan satırlar: 1, 2):

```js
const t = new Date(2026, 0, 5, 9, 7, 3); // 5 Ocak 2026
const h = String(t.getHours()).padStart(2, "0");
const m = String(t.getMinutes()).padStart(2, "0");
const s = String(t.getSeconds()).padStart(2, "0");
console.log(`${h}:${m}:${s}`);
```

**Çıktı:**

```text
09:07:03
```

**Maskot:** konusma pozu, sag

## Sahne 7: kod (14 sn)

**Seslendirme:** Hepsini birleştirip canlı bir saat yapalım. showTime'ı önce bir kez hemen çağırıyoruz, sonra setInterval her saniye güncelliyor.

**Ekranda başlık:** Canlı üs saati

**Kod** (vurgulanan satırlar: 5, 6):

```js
const clock = document.querySelector("#clock");
function showTime() {
  clock.textContent = new Date().toLocaleTimeString("tr-TR");
}
showTime(); // hemen göster
setInterval(showTime, 1000); // sonra her saniye
```

**Çıktı:**

```text
Üs saati: 14:32:08 (her saniye bir sonraki saniyeye geçer)
```

**Maskot:** mutlu pozu, sol

## Sahne 8: soru (9 sn)

**Seslendirme:** Soru! Bekleme süresi sıfır milisaniye. Sence önce A mı yazılır, yoksa B mi?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```js
setTimeout(() => console.log("A"), 0);
console.log("B");
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (9 sn)

**Seslendirme:** Önce B! Süre sıfır bile olsa setTimeout fonksiyonu kenara koyar. Şimdiki kod bitince sıra A'ya gelir.

**Ekranda başlık:** Cevap

**Kod**:

```js
setTimeout(() => console.log("A"), 0);
console.log("B");
```

**Çıktı:**

```text
B
A
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görev zamanı! Gecikmeli bir kalkış mesajı, Dur düğmesiyle duran bir uçuş sayacı ve belli sayıda yanıp sönüp kendiliğinden duran bir işaret ışığı yapacaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Gecikmeli kalkış
- Görev 2: Uçuş süresi
- Görev 3: Yanıp sönen işaret

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (12 sn)

**Seslendirme:** Özetleyelim: setTimeout bir kez, setInterval tekrar tekrar çalışır. Kimlik numarasını sakla ve clearInterval ile durdur. Aynı anda tek sayaç çalıştığından emin ol.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- setTimeout(fn, ms): bir kez, sonra
- setInterval + clearInterval(timer)
- timer !== null ise yeni sayaç kurma

**Maskot:** konusma pozu, sag

## Sahne 12: kapanis (10 sn)

**Seslendirme:** Zaman artık senin kontrolünde! Yarın renkleri, temaları ve efektleri JavaScript'ten değiştireceğiz: CSS'i kodla kontrol etmek. Görüşürüz!

**Ekranda başlık:** Yarın: CSS'i kodla kontrol etmek

**Görsel:** `gorseller/javascript/arka-plan/bg-space-wide.webp`

**Maskot:** tebrik pozu, orta
