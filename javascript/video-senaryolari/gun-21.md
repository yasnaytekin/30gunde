# Video senaryosu: Gün 21, Canvas ile çizim

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~172 sn

Kodi, Piksel Gezegeni'nde canvas ve 2d çizim bağlamını, koordinat sistemini, dikdörtgen, daire, çizgi ve yazı çizmeyi ve bir diziden döngüyle resim çizmeyi anlatıyor.

Ders metni: [gun-21.md](../gunler/gun-21.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | el-sallama (sag) |
| 2 | kod | 15 sn | isaret (sag) |
| 3 | anlatim | 15 sn | dusunme (sol) |
| 4 | kod | 17 sn | konusma (sag) |
| 5 | kod | 17 sn | isaret (sol) |
| 6 | kod | 12 sn | konusma (sag) |
| 7 | kod | 16 sn | mutlu (sag) |
| 8 | hata | 14 sn | uzgun (sag) |
| 9 | soru | 12 sn | dusunme (sag) |
| 10 | cikti | 8 sn | mutlu (sag) |
| 11 | gorev | 12 sn | isaret (sol) |
| 12 | ozet | 12 sn | konusma (sag) |
| 13 | kapanis | 10 sn | el-sallama (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Kodi! Piksel Gezegeni'ne indik. Burada her şey minicik renkli noktalardan, yani piksellerden oluşuyor. Kodla resim çizebilir miyiz? Bugün canvas ile çizim yapıyoruz!

**Ekranda başlık:** Gün 21: Canvas ile çizim

**Görsel:** `gorseller/javascript/bolgeler/piksel.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (15 sn)

**Seslendirme:** canvas etiketi boş bir resim tuvalidir. Üzerine çizmek için ondan bir fırça isteriz: getContext iki d. ctx artık bütün çizim komutlarını bilen nesnedir.

**Ekranda başlık:** Tuval ve fırça

**Kod** (vurgulanan satırlar: 2):

```js
const canvas = document.querySelector("#game");
const ctx = canvas.getContext("2d");
console.log(canvas.width, canvas.height);
```

**Çıktı:**

```text
300 200
```

**Maskot:** isaret pozu, sag

## Sahne 3: anlatim (15 sn)

**Seslendirme:** Tuvalde her noktanın bir x, y adresi var. Sol üst köşe sıfır, sıfırdır. x sağa gittikçe, y ise aşağı gittikçe büyür. Yani bir şeyi yukarı taşımak için y'yi azaltırsın!

**Ekranda başlık:** Koordinatlar: y aşağı doğru büyür

**Ekranda maddeler:**

- Sol üst köşe: (0, 0)
- Sağ üst köşe: (300, 0)
- Sol alt köşe: (0, 200)
- Orta: (150, 100)

**Maskot:** dusunme pozu, sol

*Yönetmen notu: Tuvalin üstünde x ve y okları çizilir; y okunun aşağıyı gösterdiği vurgulanır.*

## Sahne 4: kod (17 sn)

**Seslendirme:** Önce rengi seç, sonra çiz. fillRect dolu bir dikdörtgen çizer: x, y, genişlik, yükseklik. strokeRect içi boş bir çerçeve, clearRect ise silgi. x, y noktası dikdörtgenin sol üst köşesidir.

**Ekranda başlık:** Dikdörtgen, çerçeve, silgi

**Kod** (vurgulanan satırlar: 1, 2, 5):

```js
ctx.fillStyle = "#0b1026";       // dolgu rengi
ctx.fillRect(0, 0, 300, 200);    // x, y, genişlik, yükseklik
ctx.strokeStyle = "#f7df1e";     // çizgi rengi
ctx.lineWidth = 3;
ctx.strokeRect(20, 20, 60, 40);  // içi boş çerçeve
```

**Çıktı:**

```text
Lacivert bir zemin ve sol üstte sarı çerçeveli bir kutu.
```

**Maskot:** konusma pozu, sag

## Sahne 5: kod (17 sn)

**Seslendirme:** Daireler bir yol olarak çizilir: beginPath ile başla, arc ile şekli tarif et, fill ile doldur. arc'ın son iki değeri tam bir tur demek. Yazı için de font ve fillText var.

**Ekranda başlık:** Daire ve yazı

**Kod** (vurgulanan satırlar: 1, 2, 4):

```js
ctx.beginPath();
ctx.arc(150, 100, 30, 0, Math.PI * 2); // merkez, yarıçap, tam tur
ctx.fillStyle = "#ff9800";
ctx.fill();
ctx.fillStyle = "white";
ctx.font = "16px sans-serif";
ctx.fillText("Yıldız Avcısı", 10, 20);
```

**Çıktı:**

```text
Tuvalin ortasında turuncu bir gezegen, sol üstte beyaz "Yıldız Avcısı" yazısı.
```

**Maskot:** isaret pozu, sol

## Sahne 6: kod (12 sn)

**Seslendirme:** Çizgi de bir yoldur. moveTo kalemi bir noktaya koyar, lineTo oraya kadar çizgiyi tarif eder, stroke da çizer.

**Ekranda başlık:** Çizgi

**Kod** (vurgulanan satırlar: 2, 3, 5):

```js
ctx.beginPath();
ctx.moveTo(10, 190);  // kalemi buraya koy
ctx.lineTo(290, 190); // buraya kadar çiz
ctx.strokeStyle = "white";
ctx.stroke();
```

**Çıktı:**

```text
Tuvalin altında soldan sağa beyaz bir yer çizgisi.
```

**Maskot:** konusma pozu, sag

## Sahne 7: kod (16 sn)

**Seslendirme:** Asıl güç, resmi veriden çizmek. Dizideki her yıldız için aynı komutu döngüyle çalıştırıyoruz. Diziye yeni bir yıldız eklersen resim de değişir!

**Ekranda başlık:** Veriden çizim

**Kod** (vurgulanan satırlar: 3, 4):

```js
const stars = [{ x: 40, y: 30 }, { x: 120, y: 80 }, { x: 250, y: 50 }];
ctx.fillStyle = "#f7df1e";
for (const star of stars) {
  ctx.fillRect(star.x, star.y, 6, 6);
}
```

**Çıktı:**

```text
Lacivert gökyüzünde üç küçük sarı yıldız.
```

**Maskot:** mutlu pozu, sag

## Sahne 8: hata (14 sn)

**Seslendirme:** Sık hata: rengi çizdikten sonra seçmek. fillStyle yalnızca kendisinden sonraki çizimleri etkiler. Bu kutu kırmızı değil, önceki renkte çizilir. Hata mesajı da çıkmaz!

**Ekranda başlık:** Sık hata: sıra önemli

**Kod** (vurgulanan satırlar: 2):

```js
ctx.fillRect(20, 30, 60, 40);
ctx.fillStyle = "#e53935"; // çok geç!
```

**Çıktı:**

```text
Kutu kırmızı değil, varsayılan siyah renkte çizilir.
```

**Maskot:** uzgun pozu, sag

## Sahne 9: soru (12 sn)

**Seslendirme:** Soru zamanı! Tuval 300'e 200. Roket şu an 60, 80 noktasında. Onu yukarı taşımak için x'i mi, y'yi mi değiştirirsin; artırarak mı, azaltarak mı?

**Ekranda başlık:** Sence hangisi?

**Ekranda maddeler:**

- A) x'i artır
- B) x'i azalt
- C) y'yi artır
- D) y'yi azalt

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (8 sn)

**Seslendirme:** Cevap D: y'yi azalt! Tuvalde y aşağı doğru büyür, bu yüzden yukarı çıkmak için küçültürüz.

**Ekranda başlık:** Cevap: D

**Kod**:

```js
ctx.fillRect(60, 40, 16, 50); // y: 80 → 40, roket yukarıda
```

**Çıktı:**

```text
Roket tuvalde daha yukarıda çizilir.
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (12 sn)

**Seslendirme:** Görevlerin hazır! Tuvalin tamamını boyayıp üstüne bir kutu koyacaksın, turuncu bir gezegen çizeceksin ve yıldızları bir diziden çizen bir fonksiyon yazacaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Uzay zemini
- Görev 2: Turuncu gezegen
- Görev 3: Yıldızları diziden çiz

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (12 sn)

**Seslendirme:** Özetleyelim: getContext ile fırçayı al. Sol üst köşe sıfır, sıfır ve y aşağı doğru büyür. Önce rengi seç, sonra çiz; resmi diziden döngüyle çiz.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- canvas.getContext("2d")
- (0, 0) sol üst; y aşağı büyür
- fillRect, arc + fill, moveTo/lineTo + stroke, döngüyle çizim

**Maskot:** konusma pozu, sag

## Sahne 13: kapanis (10 sn)

**Seslendirme:** Harika bir ilk resim! Ama şimdilik her şey yerinde duruyor. Yarın tuvaldeki gemiyi hareket ettireceğiz: animasyon! Görüşürüz!

**Ekranda başlık:** Yarın: Animasyon

**Görsel:** `gorseller/javascript/arka-plan/bg-space-wide.webp`

**Maskot:** el-sallama pozu, orta
