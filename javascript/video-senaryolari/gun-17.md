# Video senaryosu: Gün 17, Klavye ve ses

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~173 sn

Kodi, Olay Kuşağı'nda keydown ve keyup olaylarını, e.key değerlerini, bir elemanı sınırlar içinde hareket ettirmeyi, preventDefault'u ve Web Audio ile bip sesi çalmayı anlatıyor.

Ders metni: [gun-17.md](../gunler/gun-17.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | el-sallama (sag) |
| 2 | kod | 16 sn | isaret (sag) |
| 3 | anlatim | 13 sn | konusma (sol) |
| 4 | kod | 17 sn | isaret (sag) |
| 5 | kod | 18 sn | konusma (sol) |
| 6 | anlatim | 13 sn | dusunme (sag) |
| 7 | kod | 17 sn | mutlu (sag) |
| 8 | hata | 14 sn | uzgun (sag) |
| 9 | soru | 9 sn | dusunme (sag) |
| 10 | cikti | 9 sn | mutlu (sag) |
| 11 | gorev | 13 sn | isaret (sol) |
| 12 | ozet | 12 sn | konusma (sag) |
| 13 | kapanis | 10 sn | el-sallama (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Kodi! Olay Kuşağı'na hoş geldin. Burada her şey bir sinyale tepki veriyor. Peki gemini fareyle değil de klavyeyle yönetebilir misin? Bugün klavye olaylarını ve sesi öğreniyoruz!

**Ekranda başlık:** Gün 17: Klavye ve ses

**Görsel:** `gorseller/javascript/bolgeler/kusak.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (16 sn)

**Seslendirme:** Bir tuşa bastığın an keydown, bıraktığın an keyup olayı olur. Tuşları bütün sayfada duymak için olayı document'a bağlarız. Hangi tuşa basıldığı e.key içindedir.

**Ekranda başlık:** keydown ve e.key

**Kod** (vurgulanan satırlar: 1, 2):

```js
document.addEventListener("keydown", (e) => {
  console.log("Basıldı:", e.key);
});
```

**Çıktı:**

```text
Sol oka basınca konsolda: Basıldı: ArrowLeft
```

**Maskot:** isaret pozu, sag

## Sahne 3: anlatim (13 sn)

**Seslendirme:** İşte en çok kullanacağın tuş adları. Oklar ArrowLeft, ArrowRight gibi yazılır. Boşluk tuşu ise içinde tek boşluk olan bir metindir. Büyük küçük harfe dikkat!

**Ekranda başlık:** e.key değerleri

**Ekranda maddeler:**

- Oklar: "ArrowLeft", "ArrowRight", "ArrowUp", "ArrowDown"
- Enter: "Enter"  ·  Esc: "Escape"
- Boşluk: " "
- Harfler: "a", "A", rakamlar: "1"

**Maskot:** konusma pozu, sol

## Sahne 4: kod (17 sn)

**Seslendirme:** Bir şeyi hareket ettirmek için konumunu bir değişkende tutarız. Math.min büyük sayıyı 260'a indirir, Math.max küçüğünü sıfıra çeker. Böylece roket alanın dışına kaçamaz. Buna sınırlamak denir.

**Ekranda başlık:** Sınırlamak: Math.max ve Math.min

**Kod** (vurgulanan satırlar: 3):

```js
let x = 250;
function move(dx) {
  x = Math.max(0, Math.min(260, x + dx)); // 0 ile 260 arası
  return x;
}
console.log(move(20));
console.log(move(-300));
console.log(move(40));
```

**Çıktı:**

```text
260
0
40
```

**Maskot:** isaret pozu, sag

## Sahne 5: kod (18 sn)

**Seslendirme:** Şimdi hepsi bir arada. Ok tuşları x ve y'yi yirmişer piksel değiştiriyor, başka tuşlar return ile atlanıyor. preventDefault sayfanın kaymasını durduruyor, sonra noktanın left ve top stilini güncelliyoruz.

**Ekranda başlık:** Ok tuşlarıyla nokta

**Kod** (vurgulanan satırlar: 4, 5, 7):

```js
document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowRight") x += 20;
  else if (e.key === "ArrowLeft") x -= 20;
  else return;
  e.preventDefault();
  x = Math.max(0, Math.min(220, x));
  dot.style.left = x + "px";
});
```

**Çıktı:**

```text
Sağ oka her basışta nokta 20 piksel sağa kayar, kenarda durur.
```

**Maskot:** konusma pozu, sol

## Sahne 6: anlatim (13 sn)

**Seslendirme:** Kullanıcı bir kutuya yazı yazarken oyun kısayolları çalışmamalı. Olayın nerede olduğunu e.target söyler. Yazı kutusundaysa hemen çıkıyoruz.

**Ekranda başlık:** Kutuya yazarken kısayol yok

**Kod** (vurgulanan satırlar: 2):

```js
document.addEventListener("keydown", (e) => {
  if (e.target.tagName === "INPUT") return; // kutuya yazılıyor
  // oyun tuşları burada
});
```

**Maskot:** dusunme pozu, sag

## Sahne 7: kod (17 sn)

**Seslendirme:** Tarayıcı kendi başına ses de üretebilir! AudioContext küçük bir ses stüdyosu, oscillator ise ton üreten bir hoparlör gibi. Ses her cihazda çalışmayabilir, bu yüzden try ve catch içine koyuyoruz.

**Ekranda başlık:** Web Audio ile bip

**Kod** (vurgulanan satırlar: 3, 4, 8):

```js
function beep(freq = 440) {
  try {
    const audio = new AudioContext();
    const osc = audio.createOscillator();
    osc.frequency.value = freq; // büyüdükçe ses incelir
    osc.connect(audio.destination);
    osc.start();
    osc.stop(audio.currentTime + 0.15);
  } catch (err) { console.log("Ses çalınamadı."); }
}
```

**Çıktı:**

```text
Düğmeye basınca 0,15 saniyelik kısa bir bip sesi duyulur.
```

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Bip anında ekranda küçük bir ses dalgası animasyonu.*

## Sahne 8: hata (14 sn)

**Seslendirme:** Sık hata: boşluk tuşunu Space diye aramak. e.key boşluk için tek boşluklu bir metin verir, o yüzden bu koşul hiç tutmaz. Hata mesajı da çıkmaz, sadece hiçbir şey olmaz!

**Ekranda başlık:** Sık hata: yanlış tuş adı

**Kod** (vurgulanan satırlar: 2, 3):

```js
document.addEventListener("keydown", (e) => {
  if (e.key === "Space") fire(); // hiç çalışmaz!
  if (e.key === " ") fire();     // doğrusu
});
```

**Çıktı:**

```text
Boşluğa basınca ilk satır hiçbir şey yapmaz.
```

**Maskot:** uzgun pozu, sag

## Sahne 9: soru (9 sn)

**Seslendirme:** Soru zamanı! Roket 240'ta duruyor ve 40 ileri gitmek istiyor. Sence x kaç olur?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```js
let x = 240;
x = Math.max(0, Math.min(260, x + 40));
console.log(x);
```

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (9 sn)

**Seslendirme:** Cevap 260! 240 artı 40, 280 eder ama Math.min onu sınır olan 260'a indirir. Roket kenarda durur.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 2):

```js
let x = 240;
x = Math.max(0, Math.min(260, x + 40));
console.log(x);
```

**Çıktı:**

```text
260
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (13 sn)

**Seslendirme:** Görevlerin hazır! Basılan tuşun adını gösteren bir dedektör, ok tuşlarıyla sınırlar içinde kayan bir roket ve boşluk basılı tutulunca çalışan bir motor yapacaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Tuş dedektörü
- Görev 2: Roketi kaydır
- Görev 3: Motor düğmesi

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (12 sn)

**Seslendirme:** Özetleyelim: keydown ve keyup'ı document'a bağla, tuşu e.key ile tanı. Konumu sınırla ve kendi tuşların için preventDefault çağır. Ses ise bir bonus.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- keydown / keyup + e.key
- Konumu değişkende tut, Math.max/min ile sınırla
- Web Audio ile bip; oyun sese bağlı olmasın

**Maskot:** konusma pozu, sag

## Sahne 13: kapanis (10 sn)

**Seslendirme:** Süper, artık gemin klavyeyi dinliyor! Yarın zamanın kendisini kontrol edeceğiz: geri sayımlar, saatler ve kronometreler. Görüşürüz!

**Ekranda başlık:** Yarın: Zamanlayıcılar

**Görsel:** `gorseller/javascript/arka-plan/bg-space-wide.webp`

**Maskot:** el-sallama pozu, orta
