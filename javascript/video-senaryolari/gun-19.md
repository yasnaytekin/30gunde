# Video senaryosu: Gün 19, CSS'i kodla kontrol etmek

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~159 sn

Kodi, Olay Kuşağı'nda style, classList, CSS değişkenleri ve data-* özellikleriyle bir sayfanın görünüşünü JavaScript'ten değiştirmeyi; gece modu ve renk seçici örnekleriyle anlatıyor.

Ders metni: [gun-19.md](../gunler/gun-19.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | el-sallama (sag) |
| 2 | kod | 16 sn | isaret (sag) |
| 3 | anlatim | 16 sn | konusma (sol) |
| 4 | kod | 16 sn | mutlu (sag) |
| 5 | kod | 17 sn | isaret (sag) |
| 6 | kod | 15 sn | konusma (sol) |
| 7 | hata | 13 sn | uzgun (sag) |
| 8 | soru | 9 sn | dusunme (sag) |
| 9 | cikti | 9 sn | mutlu (sag) |
| 10 | gorev | 13 sn | isaret (sol) |
| 11 | ozet | 12 sn | konusma (sag) |
| 12 | kapanis | 11 sn | el-sallama (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Kodi! Gemim artık hareket ediyor ve zamanı ölçüyor. Şimdi sıra görünüşte! Tek bir tıklamayla bütün kokpiti gece moduna çevirebilir miyiz? Bugün CSS'i kodla kontrol ediyoruz.

**Ekranda başlık:** Gün 19: CSS'i kodla kontrol etmek

**Görsel:** `gorseller/javascript/bolgeler/kusak.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (16 sn)

**Seslendirme:** Her elemanın bir style nesnesi var. CSS'teki tireli adlar burada birleşik yazılır: background-color, backgroundColor olur. Değerler metindir, o yüzden birimi unutma: 150 değil, 150px.

**Ekranda başlık:** element.style

**Kod** (vurgulanan satırlar: 2, 3):

```js
const box = document.querySelector("#box");
box.style.backgroundColor = "#f7df1e";
box.style.width = "150px"; // 150 değil, "150px"
```

**Çıktı:**

```text
Kargo kutusu sarıya boyanır ve 150 piksel genişler.
```

**Maskot:** isaret pozu, sag

## Sahne 3: anlatim (16 sn)

**Seslendirme:** Çok sayıda stili tek tek yazmak yerine görünüşü CSS'te bir sınıfa yaz. JavaScript yalnızca sınıfı ekler ya da çıkarır. toggle varsa çıkarır, yoksa ekler; contains ise sınıf var mı diye sorar.

**Ekranda başlık:** classList ile durumlar

**Kod** (vurgulanan satırlar: 3, 4):

```js
shield.classList.add("active");      // ekle
shield.classList.remove("active");   // çıkar
shield.classList.toggle("active");   // varsa çıkar, yoksa ekle
shield.classList.contains("active"); // true / false
```

**Maskot:** konusma pozu, sol

## Sahne 4: kod (16 sn)

**Seslendirme:** İşte gece modu. Bütün renkler CSS'te, night sınıfının içinde duruyor. Düğme yalnızca sınıfı değiştiriyor, sonra contains ile durumu okuyup kendi yazısını güncelliyor.

**Ekranda başlık:** Örnek: gece modu

**Kod** (vurgulanan satırlar: 2, 3, 4):

```js
btn.addEventListener("click", () => {
  document.body.classList.toggle("night");
  const night = document.body.classList.contains("night");
  btn.textContent = night ? "Gündüz modu" : "Gece modu";
});
```

**Çıktı:**

```text
Sayfa koyu renklere geçer, düğmede "Gündüz modu" yazar.
```

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Tıklama anında sayfa gündüzden geceye yumuşak bir geçişle döner.*

## Sahne 5: kod (17 sn)

**Seslendirme:** CSS'te iki tireyle başlayan adlar değişkendir ve var ile her yerde kullanılır. JavaScript'le değişkeni tek satırda değiştirirsin; onu kullanan her şey birden güncellenir. Okumak için getComputedStyle kullanıyoruz.

**Ekranda başlık:** CSS değişkenleri

**Kod** (vurgulanan satırlar: 3, 4):

```js
/* CSS:  :root { --accent: #f7df1e; } */
const root = document.documentElement; // <html>
root.style.setProperty("--accent", "#b388ff");
const now = getComputedStyle(root).getPropertyValue("--accent").trim();
console.log(now);
```

**Çıktı:**

```text
#b388ff  (--accent kullanan her kenarlık ve düğme mora döner)
```

**Maskot:** isaret pozu, sag

## Sahne 6: kod (15 sn)

**Seslendirme:** data ile başlayan özellikler elemana kendi bilgini eklemenin yoludur. JavaScript'te dataset ile okunur ve yazılır. CSS de bu özelliklere göre seçim yapabilir.

**Ekranda başlık:** data-* ve dataset

**Kod** (vurgulanan satırlar: 2, 3):

```js
// <button data-color="#e53935">Kızıl</button>
console.log(btn.dataset.color);
document.body.dataset.mode = "gece";
// artık <body data-mode="gece">
```

**Çıktı:**

```text
#e53935
```

**Maskot:** konusma pozu, sol

## Sahne 7: hata (13 sn)

**Seslendirme:** Sık hata: style'a birimsiz sayı vermek. Tarayıcı bunu geçersiz sayar ve sessizce yok sayar. Hata mesajı çıkmaz, kutu sadece yerinden kıpırdamaz!

**Ekranda başlık:** Sık hata: birimi unutmak

**Kod** (vurgulanan satırlar: 1):

```js
box.style.width = 150;     // işe yaramaz
box.style.width = "150px"; // doğrusu
```

**Çıktı:**

```text
İlk satırdan sonra kutunun genişliği değişmez.
```

**Maskot:** uzgun pozu, sag

## Sahne 8: soru (9 sn)

**Seslendirme:** Soru zamanı! Kalkan sınıfı şu an kapalı. toggle'ı iki kez çağırırsak sence konsolda ne yazar?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```js
shield.classList.toggle("active");
shield.classList.toggle("active");
console.log(shield.classList.contains("active"));
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (9 sn)

**Seslendirme:** Cevap false! İlk toggle sınıfı ekledi, ikinci toggle geri çıkardı. Kalkan başladığı gibi kapalı kaldı.

**Ekranda başlık:** Cevap

**Kod**:

```js
shield.classList.toggle("active");
shield.classList.toggle("active");
console.log(shield.classList.contains("active"));
```

**Çıktı:**

```text
false
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görevlerin hazır! Önce style ile bir kargo kutusunu boyayacaksın. Sonra açılıp kapanan bir kalkan, en sonda da düğmelerle rengi değişen bir gezegen yapacaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Kutuyu boya
- Görev 2: Kalkan
- Görev 3: Gezegen rengi

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (12 sn)

**Seslendirme:** Özetleyelim: tek bir stil için style, durumlar için classList, bütün temayı değiştirmek için CSS değişkenleri. Kendi bilgini eklemek için de data özellikleri.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- style.backgroundColor = "..." (birimle!)
- classList: add, remove, toggle, contains
- --değişken + setProperty; data-* + dataset

**Maskot:** konusma pozu, sag

## Sahne 12: kapanis (11 sn)

**Seslendirme:** Gemin artık hem hızlı hem şık! Ama sayfayı yenileyince skor sıfırlanıyor, değil mi? Yarın gemine bir hafıza takacağız: kalıcı veri. Görüşürüz!

**Ekranda başlık:** Yarın: Kalıcı veri

**Görsel:** `gorseller/javascript/arka-plan/bg-space-wide.webp`

**Maskot:** el-sallama pozu, orta
