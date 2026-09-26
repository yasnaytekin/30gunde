# Video senaryosu: Gün 20, Kalıcı veri

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~160 sn

Kodi, Olay Kuşağı'nın son durağında localStorage ile metin, sayı, dizi ve nesne saklamayı; açılışta yükleyip varsayılan değer kullanmayı ve || ile ?? farkını anlatıyor.

Ders metni: [gun-20.md](../gunler/gun-20.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | el-sallama (sag) |
| 2 | kod | 17 sn | isaret (sag) |
| 3 | kod | 17 sn | konusma (sol) |
| 4 | kod | 16 sn | isaret (sag) |
| 5 | kod | 17 sn | konusma (sag) |
| 6 | kod | 17 sn | isaret (sol) |
| 7 | kod | 14 sn | mutlu (sag) |
| 8 | hata | 14 sn | sasirma (sag) |
| 9 | gorev | 13 sn | isaret (sol) |
| 10 | ozet | 12 sn | konusma (sag) |
| 11 | kapanis | 11 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Kodi! Sayfayı yenileyince skorun sıfırlanıyor mu? Olay Kuşağı'nın son durağında gemine bir hafıza takıyoruz. Bugün localStorage ile bilgileri kalıcı yapacağız!

**Ekranda başlık:** Gün 20: Kalıcı veri

**Görsel:** `gorseller/javascript/bolgeler/kusak.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (17 sn)

**Seslendirme:** localStorage her sitenin tarayıcıda kendine ait küçük bir defteridir. Sayfa kapansa da içindekiler kalır. setItem kaydeder, getItem okur, removeItem siler. Kayıt yoksa getItem null verir.

**Ekranda başlık:** Tarayıcının defteri

**Kod** (vurgulanan satırlar: 1, 2, 3):

```js
localStorage.setItem("pilot", "Ada");      // kaydet
const name = localStorage.getItem("pilot"); // "Ada"
localStorage.removeItem("pilot");          // sil
console.log(localStorage.getItem("pilot"));
```

**Çıktı:**

```text
null
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (17 sn)

**Seslendirme:** Dikkat: localStorage her şeyi metin olarak saklar. 42 kaydedersen geri tırnaklı 42 gelir. Hesap yapmadan önce Number ile çevir. Sondaki veya sıfır da kayıt yoksa sıfır kullanılmasını sağlar.

**Ekranda başlık:** Sayılar metin olarak saklanır

**Kod** (vurgulanan satırlar: 2, 3):

```js
localStorage.setItem("best", 42);
localStorage.getItem("best");        // "42" (metin!)
const best = Number(localStorage.getItem("best")) || 0;
console.log(best + 1);
```

**Çıktı:**

```text
43
```

**Maskot:** konusma pozu, sol

## Sahne 4: kod (16 sn)

**Seslendirme:** Varsayılan değer için iki araç var. Veya işareti, yanlış sayılan her değerde sağ tarafı kullanır, sıfır bile olsa. Çift soru işareti ise yalnızca null ve undefined'da devreye girer.

**Ekranda başlık:** || ve ?? farkı

**Kod** (vurgulanan satırlar: 1, 2):

```js
console.log(0 || 5);
console.log(0 ?? 5);
console.log(null ?? "yeni pilot");
console.log(Number(null) || 0);
```

**Çıktı:**

```text
5
0
yeni pilot
0
```

**Maskot:** isaret pozu, sag

## Sahne 5: kod (17 sn)

**Seslendirme:** Dizi ve nesneleri saklamak için önce JSON.stringify ile metne çeviririz, okurken JSON.parse ile geri çeviririz. Kayıt yoksa JSON.parse null verir; çift soru işaretiyle boş bir dizi kullanırız.

**Ekranda başlık:** Diziler ve nesneler: JSON

**Kod** (vurgulanan satırlar: 2, 3):

```js
const items = ["kalkan", "lazer"];
localStorage.setItem("inventory", JSON.stringify(items));
const back = JSON.parse(localStorage.getItem("inventory")) ?? [];
console.log(back.length);
```

**Çıktı:**

```text
2
```

**Maskot:** konusma pozu, sag

## Sahne 6: kod (17 sn)

**Seslendirme:** Kalıcı veri kullanan her sayfa aynı düzeni izler: açılışta yükle, ekranda göster, değişince yeniden kaydet. Ayarlarda eksik alanları yayma ile varsayılanlardan doldururuz. Kayıtlı olanlar üste yazılır.

**Ekranda başlık:** Açılışta yükle, değişince kaydet

**Kod** (vurgulanan satırlar: 3):

```js
const DEFAULTS = { sound: true, volume: 5 };
const saved = JSON.parse('{"volume":8}') ?? {}; // kayıttan gelmiş gibi
const settings = { ...DEFAULTS, ...saved };
console.log(settings);
```

**Çıktı:**

```text
{ sound: true, volume: 8 }
```

**Maskot:** isaret pozu, sol

## Sahne 7: kod (14 sn)

**Seslendirme:** İşte düzenin kendisi: not kutusu açılışta kayıttan doluyor, her yazışta yeniden kaydediliyor. Sayfayı yenilesen de notun yerinde duruyor!

**Ekranda başlık:** Örnek: kaptan notu

**Kod** (vurgulanan satırlar: 2, 4):

```js
const note = document.querySelector("#note");
note.value = localStorage.getItem("note") ?? "";
note.addEventListener("input", () => {
  localStorage.setItem("note", note.value);
});
```

**Çıktı:**

```text
Yazdığın not, sayfa yenilendikten sonra da kutuda görünür.
```

**Maskot:** mutlu pozu, sag

## Sahne 8: hata (14 sn)

**Seslendirme:** Sık hata: diziyi JSON'a çevirmeden kaydetmek. localStorage onu kendi bildiği gibi metne çevirir ve köşeli parantezler kaybolur. Geri okuyunca dizi değil, düz bir metin gelir!

**Ekranda başlık:** Sık hata: JSON'u unutmak

**Kod** (vurgulanan satırlar: 1):

```js
localStorage.setItem("inventory", ["kalkan", "lazer"]);
console.log(localStorage.getItem("inventory"));
```

**Çıktı:**

```text
kalkan,lazer   (dizi değil, metin!)
```

**Maskot:** sasirma pozu, sag

## Sahne 9: gorev (13 sn)

**Seslendirme:** Görev zamanı! Sayfayı kaçıncı kez açtığını sayan bir sayaç, adını hatırlayan bir selam ve JSON ile saklanan bir envanter listesi yapacaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Ziyaret sayacı
- Görev 2: Pilotu hatırla
- Görev 3: Envanter kaydı

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (12 sn)

**Seslendirme:** Özetleyelim: setItem, getItem ve removeItem ile tarayıcının defterini kullan. Sayıları Number ile çevir, dizileri ve nesneleri JSON ile sakla. Kayıt yoksa varsayılan değer kullan.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- setItem / getItem / removeItem
- Her şey metin: Number() ve JSON.stringify / parse
- Kayıt yoksa: || 0, ?? [], { ...DEFAULTS, ...saved }

**Maskot:** konusma pozu, sag

## Sahne 11: kapanis (11 sn)

**Seslendirme:** Tebrikler, Olay Kuşağı'nı geçtin! Yarın Piksel Gezegeni'ne iniyoruz. Orada canvas adlı tuvale kodla çizim yapacağız. Görüşürüz!

**Ekranda başlık:** Yarın: Canvas ile çizim

**Görsel:** `gorseller/javascript/bolgeler/piksel.webp`

**Maskot:** tebrik pozu, orta
