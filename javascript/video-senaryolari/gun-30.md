# Video senaryosu: Gün 30, Final

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~179 sn

Kodi, 30 günlük yolculuğun son durağı JavaScript Yıldızı'nda sekiz bölgede öğrenilenleri özetliyor, hepsini birleştiren örnekler gösteriyor, projeyi yayınlamayı, son kontrol listesini ve sonraki adımları anlatıp kursu kutlamayla kapatıyor.

Ders metni: [gun-30.md](../gunler/gun-30.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 11 sn | el-sallama (sag) |
| 2 | anlatim | 15 sn | mutlu (sol) |
| 3 | anlatim | 16 sn | mutlu (sag) |
| 4 | kod | 18 sn | isaret (sag) |
| 5 | kod | 13 sn | konusma (sol) |
| 6 | anlatim | 18 sn | isaret (sag) |
| 7 | hata | 14 sn | sasirma (sag) |
| 8 | soru | 10 sn | dusunme (sag) |
| 9 | cikti | 9 sn | mutlu (sag) |
| 10 | anlatim | 13 sn | dusunme (sol) |
| 11 | gorev | 13 sn | isaret (sol) |
| 12 | anlatim | 13 sn | konusma (sag) |
| 13 | kapanis | 16 sn | tebrik (orta) |

## Sahne 1: acilis (11 sn)

**Seslendirme:** Selam, ben Kodi! Karşımızda parıldayan ışık JavaScript Yıldızı! 30 günlük yolculuğumuzun son durağındayız. Bugün parçaları birleştiriyor ve projeni dünyaya göstermeye hazırlanıyoruz!

**Ekranda başlık:** Gün 30: Final

**Görsel:** `gorseller/javascript/bolgeler/yildiz.webp`

**Maskot:** el-sallama pozu, sag

*Yönetmen notu: Yıldız görseline doğru hızlı bir roket yolculuğu; son karede yıldız ekranı doldurur.*

## Sahne 2: anlatim (15 sn)

**Seslendirme:** Hadi yolculuğa bir göz atalım! Kalkış Üssü'nde değişkenleri, Döngü Ayı'nda koşulları ve döngüleri öğrendik. Fonksiyon Nebulası'nda nesneler ve map, DOM Gezegeni'nde sayfayı değiştirmek geldi.

**Ekranda başlık:** Neler öğrendin? (1)

**Ekranda maddeler:**

- Kalkış Üssü: değişkenler, operatörler, metinler
- Döngü Ayı: koşullar, diziler, döngüler, fonksiyonlar
- Fonksiyon Nebulası: kapsam, nesneler, map/filter/reduce, JSON
- DOM Gezegeni: sayfayı değiştirmek, olaylar, formlar

**Görsel:** `gorseller/javascript/bolgeler/kalkis.webp`

**Maskot:** mutlu pozu, sol

*Yönetmen notu: Her madde gelirken ilgili bölge görseli küçük bir kart olarak belirir.*

## Sahne 3: anlatim (16 sn)

**Seslendirme:** Olay Kuşağı'nda klavye, zamanlayıcılar ve kalıcı veri; Piksel Gezegeni'nde canvas ve oyun döngüsü. Async İstasyonu'nda hatalar, Promise, fetch ve sınıflar. Burada da temiz kod ve erişilebilirlik!

**Ekranda başlık:** Neler öğrendin? (2)

**Ekranda maddeler:**

- Olay Kuşağı: klavye, zamanlayıcılar, CSS, localStorage
- Piksel Gezegeni: canvas, animasyon, oyun döngüsü
- Async İstasyonu: hatalar, Promise, fetch, sınıflar
- JavaScript Yıldızı: temiz kod, erişilebilirlik, final

**Görsel:** `gorseller/javascript/bolgeler/istasyon.webp`

**Maskot:** mutlu pozu, sag

## Sahne 4: kod (18 sn)

**Seslendirme:** İşte birçok bölge tek bir kodda: JSON'dan gelen veri, bir sınıf, getter, parçalama, sıralama ve await. Pilotlar yıldız sayısına göre sıralanıp rütbeleriyle yazılıyor. Bunu artık sen de yazabilirsin!

**Ekranda başlık:** Hepsi bir arada

**Kod** (vurgulanan satırlar: 1, 7, 8):

```js
class Pilot {
  constructor({ name, stars }) { this.name = name; this.stars = stars; }
  get rank() { return this.stars >= 20 ? "Kaptan" : "Çırak"; }
}
const wait = (ms) => new Promise((resolve) => setTimeout(resolve, ms));
const data = JSON.parse('[{"name":"Ada","stars":12},{"name":"Can","stars":30}]');
await wait(100); // sunucudan geliyormuş gibi
const pilots = data.map((p) => new Pilot(p)).sort((a, b) => b.stars - a.stars);
pilots.forEach(({ name, stars, rank }) => console.log(`${name}: ${stars} yıldız, ${rank}`));
```

**Çıktı:**

```text
Can: 30 yıldız, Kaptan
Ada: 12 yıldız, Çırak
```

**Maskot:** isaret pozu, sag

## Sahne 5: kod (13 sn)

**Seslendirme:** Sayfa tarafında da hepsi bir arada: veriler state'te, update değiştirip localStorage'a kaydediyor, render çiziyor. Sayfayı yenilesen de yıldızların kaldığı yerden devam eder.

**Ekranda başlık:** Örnek: kalıcı yıldız sayacı

**Kod** (vurgulanan satırlar: 1, 4, 7):

```js
const state = { stars: Number(localStorage.getItem("stars")) || 0 };
function update(action) {
  if (action === "plus") state.stars += 1;
  localStorage.setItem("stars", String(state.stars));
}
function render() { countEl.textContent = `${state.stars} yıldız`; }
plusBtn.addEventListener("click", () => { update("plus"); render(); });
render();
```

**Çıktı:**

```text
Her tıklamada "1 yıldız", "2 yıldız"...; sayfa yenilense de sayı kalır.
```

**Maskot:** konusma pozu, sol

## Sahne 6: anlatim (18 sn)

**Seslendirme:** Gerçek bir sitede genelde üç dosya olur: iskelet için index.html, görünüş için style.css, davranış için script.js. Bunları GitHub Pages ya da Netlify gibi bir statik site servisine yükleyince herkesin açabileceği bir adresin olur.

**Ekranda başlık:** Projeni yayınla

**Ekranda maddeler:**

- index.html · style.css · script.js
- GitHub Pages ya da Netlify
- Hesabı bir yetişkinle aç; kişisel bilgi paylaşma

**Kod** (vurgulanan satırlar: 2):

```html
<link rel="stylesheet" href="style.css">
<script src="script.js" defer></script>
```

**Maskot:** isaret pozu, sag

## Sahne 7: hata (14 sn)

**Seslendirme:** Yayınlarken sık hata: betiği sayfanın başında defer olmadan yüklemek. Kod, düğmeler oluşmadan çalışır, querySelector null döndürür ve TypeError alırsın. defer eklemek sorunu çözer.

**Ekranda başlık:** Sık hata: defer'i unutmak

**Kod** (vurgulanan satırlar: 2, 3):

```js
// <head> içinde: <script src="script.js"></script>  (defer yok)
const plusBtn = document.querySelector("#plus"); // null!
plusBtn.addEventListener("click", () => {});
```

**Çıktı:**

```text
TypeError: Cannot read properties of null (reading 'addEventListener')
```

**Maskot:** sasirma pozu, sag

## Sahne 8: soru (10 sn)

**Seslendirme:** Son soru, kaptan! 11. günden bir hatıra: önce süz, sonra topla. Sence bu kod ne yazar?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```js
const stars = [3, 8, 5];
const total = stars.filter((s) => s > 4).reduce((a, b) => a + b, 0);
console.log(`Toplam: ${total}`);
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (9 sn)

**Seslendirme:** Cevap: Toplam 13! filter dörtten büyük olan sekiz ve beşi bıraktı, reduce da onları topladı. Hâlâ hatırlıyorsun!

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 2):

```js
const stars = [3, 8, 5];
const total = stars.filter((s) => s > 4).reduce((a, b) => a + b, 0);
console.log(`Toplam: ${total}`);
```

**Çıktı:**

```text
Toplam: 13
```

**Maskot:** mutlu pozu, sag

## Sahne 10: anlatim (13 sn)

**Seslendirme:** Paylaşmadan önce kendine sor: konsolda kırmızı hata var mı? Telefonda çalışıyor mu? Her şey klavyeyle yapılabiliyor mu? Veri gelmezse kullanıcı ne görüyor?

**Ekranda başlık:** Son kontrol listesi

**Ekranda maddeler:**

- Konsolda kırmızı hata yok
- Telefonda da kullanılabiliyor
- Klavye + aria-label tamam
- Anlaşılır adlar, tekrar yok
- fetch hatasında anlamlı mesaj

**Maskot:** dusunme pozu, sol

## Sahne 11: gorev (13 sn)

**Seslendirme:** Son görevlerin! Adını hatırlayan bir mezuniyet kartı, yazdıkça süzülen canlı bir şehir araması ve en iyi üç pilotu saklayan bir skor tablosu sınıfı. Hepsi öğrendiklerini birleştiriyor.

**Ekranda başlık:** Final görevleri

**Ekranda maddeler:**

- Görev 1: Mezuniyet kartı
- Görev 2: Canlı arama
- Görev 3: Skor tablosu sınıfı

**Maskot:** isaret pozu, sol

## Sahne 12: anlatim (13 sn)

**Seslendirme:** Sıradaki durak neresi? Daha çok proje yap! Sonra TypeScript, React gibi arayüz araçları, sunucuda JavaScript için Node.js ya da Phaser gibi oyun kütüphaneleri seni bekliyor.

**Ekranda başlık:** Sıradaki durak

**Ekranda maddeler:**

- Daha çok proje
- TypeScript
- React, Vue, Svelte
- Node.js
- Phaser ile oyunlar

**Maskot:** konusma pozu, sag

## Sahne 13: kapanis (16 sn)

**Seslendirme:** Tebrikler, kaptan! 30 günde sıfırdan çalışan projeler yazan bir JavaScript geliştiricisi oldun. Seninle yolculuk etmek harikaydı. Unutma, bu bir son değil, yeni bir kalkış! Görüşmek üzere!

**Ekranda başlık:** 30 Günde JavaScript tamamlandı!

**Görsel:** `maskotlar/kodi-javascript/kahraman.png`

**Maskot:** tebrik pozu, orta

*Yönetmen notu: Konfeti ve havai fişek efekti; Kodi'nin kahraman görseli yıldızın önünde belirir, sonunda roket kalkışıyla kararır.*
