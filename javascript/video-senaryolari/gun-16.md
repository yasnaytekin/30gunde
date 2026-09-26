# Video senaryosu: Gün 16, Formlar

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~150 sn

Kodi, DOM Gezegeni'nin son durağında pilot kayıt formu üzerinden submit olayını, preventDefault'u, value, checked ve Number ile değer okumayı ve hataları sayfada göstermeyi anlatıyor.

Ders metni: [gun-16.md](../gunler/gun-16.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | el-sallama (sag) |
| 2 | kod | 17 sn | isaret (sag) |
| 3 | kod | 17 sn | konusma (sag) |
| 4 | kod | 16 sn | isaret (sol) |
| 5 | kod | 18 sn | konusma (sag) |
| 6 | hata | 14 sn | sasirma (sag) |
| 7 | soru | 9 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 14 sn | isaret (sol) |
| 10 | ozet | 12 sn | konusma (sag) |
| 11 | kapanis | 11 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Kodi! DOM Gezegeni'nin son durağına geldik. Kontrol kulesi, uçuşa çıkacak her pilotun bilgilerini istiyor. Peki bir formdaki yazıyı JavaScript nasıl okur? Bugün formları öğreniyoruz!

**Ekranda başlık:** Gün 16: Formlar

**Görsel:** `gorseller/javascript/bolgeler/dom.webp`

**Maskot:** el-sallama pozu, sag

*Yönetmen notu: DOM Gezegeni görseli yavaşça yakınlaşır; başlık üstten kayarak gelir.*

## Sahne 2: kod (17 sn)

**Seslendirme:** Form gönderilince submit olayı olur ve tarayıcı normalde sayfayı yeniler. Yazdığın her şey kaybolur! e.preventDefault bunu durdurur. Olayı düğmeye değil forma bağla; böylece Enter tuşu da çalışır.

**Ekranda başlık:** submit ve preventDefault

**Kod** (vurgulanan satırlar: 2, 3):

```js
const form = document.querySelector("#pilot-form");
form.addEventListener("submit", (e) => {
  e.preventDefault(); // sayfa yenilenmesin
  console.log("Form gönderildi!");
});
```

**Çıktı:**

```text
Sayfa yenilenmez; konsolda: Form gönderildi!
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (17 sn)

**Seslendirme:** Kutudaki yazı value özelliğindedir ve her zaman metindir, içine sayı yazılsa bile. Number ile sayıya çeviririz. Sayı olmayan metin NaN verir, boş metin ise sıfır! trim de baştaki ve sondaki boşlukları siler.

**Ekranda başlık:** value her zaman metindir

**Kod** (vurgulanan satırlar: 3, 4, 5):

```js
const raw = "150"; // kutudan gelen değer
console.log(typeof raw);
console.log(Number(raw) + 1);
console.log(Number("abc"));
console.log(Number(""));
console.log("  Ada ".trim());
```

**Çıktı:**

```text
string
151
NaN
0
Ada
```

**Maskot:** konusma pozu, sag

*Yönetmen notu: Konsolda 'değer kutudan gelmiş gibi' açıklaması için küçük bir input kutusu animasyonu gösterilebilir.*

## Sahne 4: kod (16 sn)

**Seslendirme:** Onay kutusunda önemli olan yazı değil, işaretli olup olmadığıdır: checked bize true ya da false verir. Seçim listesinde value, seçili seçeneğin değeridir. Onu da Number ile sayıya çeviriyoruz.

**Ekranda başlık:** checked ve select

**Kod** (vurgulanan satırlar: 3, 4):

```js
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const shield = document.querySelector("#shield").checked;
  const speed = Number(document.querySelector("#speed").value);
  info.textContent = `Kalkan ${shield ? "açık" : "kapalı"}, hız ${speed * 100} km/sn`;
});
```

**Çıktı:**

```text
Kalkan açık, hız 300 km/sn
```

**Maskot:** isaret pozu, sol

## Sahne 5: kod (18 sn)

**Seslendirme:** Formu kabul etmeden önce değerleri kontrol etmeye doğrulama denir. Ad boşsa mesajı sayfanın içine yazıyoruz ve return ile hemen çıkıyoruz. Her şey yolundaysa pilotu karşılayıp form.reset ile kutuları boşaltıyoruz.

**Ekranda başlık:** Doğrulama ve sıfırlama

**Kod** (vurgulanan satırlar: 4, 5, 6, 9):

```js
form.addEventListener("submit", (e) => {
  e.preventDefault();
  const name = document.querySelector("#name").value.trim();
  if (name === "") {
    info.textContent = "Adını yazmayı unuttun!";
    return;
  }
  info.textContent = `Hoş geldin, Kaptan ${name}!`;
  form.reset();
});
```

**Çıktı:**

```text
Kutu boşsa: Adını yazmayı unuttun!
"Ada" yazılırsa: Hoş geldin, Kaptan Ada! (kutu boşalır)
```

**Maskot:** konusma pozu, sag

## Sahne 6: hata (14 sn)

**Seslendirme:** En sık hata: kutudaki sayıyı Number'a çevirmeyi unutmak. Metne sayı eklersen JavaScript toplamaz, yan yana yapıştırır. Hata mesajı bile çıkmaz, sonuç sessizce yanlış olur!

**Ekranda başlık:** Sık hata: Number'ı unutmak

**Kod** (vurgulanan satırlar: 2):

```js
const fuel = document.querySelector("#fuel").value; // "150"
info.textContent = fuel + 50;
```

**Çıktı:**

```text
15050   (beklenen: 200)
```

**Maskot:** sasirma pozu, sag

## Sahne 7: soru (9 sn)

**Seslendirme:** Şimdi sıra sende! Biri metin, biri sayı. Sence bu iki satır ne yazdırır? Videoyu durdur ve düşün.

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```js
const a = "20";
const b = Number("20");
console.log(a + 5);
console.log(b + 5);
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Cevap: ilki 205, ikincisi 25! a bir metin olduğu için beş yanına yapıştırıldı. b ise gerçek bir sayı, bu yüzden toplandı.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 3, 4):

```js
const a = "20";
const b = Number("20");
console.log(a + 5);
console.log(b + 5);
```

**Çıktı:**

```text
205
25
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (14 sn)

**Seslendirme:** Görev zamanı! Önce bir görev kaydı formu yapacaksın. Sonra depo sayısıyla yakıt hesaplayan bir form. Son görevde ise onay kutusu işaretli değilse kalkışa izin vermeyeceksin.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Görev kaydı
- Görev 2: Yakıt hesaplayıcı
- Görev 3: Kalkış onayı

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (12 sn)

**Seslendirme:** Özetleyelim: submit olayını forma bağla ve preventDefault çağır. value her zaman metindir, sayıya Number ile çevir. Hataları sayfada göster ve return ile çık.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- submit + e.preventDefault()
- value metindir → Number(), trim(); checked → true/false
- Doğrula, hatayı sayfada göster, return ile çık

**Maskot:** konusma pozu, sag

## Sahne 11: kapanis (11 sn)

**Seslendirme:** Harika iş, pilot! DOM Gezegeni'ni tamamladın. Yarın Olay Kuşağı'na giriyoruz: gemini klavyeyle yöneteceksin, üstüne bir de bip sesi ekleyeceğiz. Görüşürüz!

**Ekranda başlık:** Yarın: Klavye ve ses

**Görsel:** `gorseller/javascript/bolgeler/kusak.webp`

**Maskot:** tebrik pozu, orta
