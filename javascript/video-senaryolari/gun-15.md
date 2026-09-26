# Video senaryosu: Gün 15, Eleman oluşturmak

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~173 sn

DOM Gezegeni'nde inşaat zamanı: createElement ile yeni eleman oluşturmak, append ve prepend ile eklemek, silmek, bir diziden render() ile liste çizmek ve dataset ile bilgi saklamak.

Ders metni: [gun-15.md](../gunler/gun-15.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 11 sn | el-sallama (sag) |
| 2 | kod | 15 sn | isaret (alt-sag) |
| 3 | kod | 16 sn | konusma (alt-sag) |
| 4 | kod | 12 sn | isaret (alt-sag) |
| 5 | kod | 18 sn | mutlu (alt-sag) |
| 6 | hata | 15 sn | uzgun (sag) |
| 7 | kod | 15 sn | konusma (alt-sag) |
| 8 | kod | 17 sn | isaret (alt-sag) |
| 9 | soru | 11 sn | dusunme (sag) |
| 10 | cikti | 10 sn | mutlu (sag) |
| 11 | gorev | 12 sn | isaret (sol) |
| 12 | ozet | 11 sn | on (sag) |
| 13 | kapanis | 10 sn | tebrik (sag) |

## Sahne 1: acilis (11 sn)

**Seslendirme:** Selam, ben Kodi! DOM Gezegeni'nde inşaat zamanı! Şimdiye kadar sayfada var olan elemanları değiştirdik. Peki hiç olmayan bir elemanı nasıl yaratırız?

**Ekranda başlık:** Gün 15: Eleman oluşturmak

**Görsel:** `gorseller/javascript/bolgeler/dom.webp`

**Maskot:** el-sallama pozu, sag

*Yönetmen notu: Gezegen yüzeyinde küçük vinçler yeni blokları yerine koyar.*

## Sahne 2: kod (15 sn)

**Seslendirme:** Yeni bir eleman üç adımda eklenir: oluştur, doldur, ekle. createElement elemanı yalnızca bellekte yaratır; append ile bir yere eklemeden sayfada görünmez.

**Ekranda başlık:** Oluştur, doldur, ekle

**Kod** (vurgulanan satırlar: 2, 3, 5):

```js
const list = document.querySelector("#cargo");
const li = document.createElement("li");
li.textContent = "Yakıt hücresi";
li.classList.add("item");
list.append(li);
```

**Çıktı:**

```text
Boş listede bir madde belirir: Yakıt hücresi
```

**Maskot:** isaret pozu, alt-sag

## Sahne 3: kod (16 sn)

**Seslendirme:** Döngüyle bir diziden bütün listeyi kurabiliriz. append sona ekler, prepend ise başa. Güneş'i en son oluşturduk ama prepend sayesinde listenin en başına geçti.

**Ekranda başlık:** append ve prepend

**Kod** (vurgulanan satırlar: 6, 10):

```js
const planets = ["Merkür", "Venüs", "Mars"];
const list = document.querySelector("#list");
for (const name of planets) {
  const li = document.createElement("li");
  li.textContent = name;
  list.append(li);
}
const sun = document.createElement("li");
sun.textContent = "Güneş (merkez)";
list.prepend(sun);
console.log("Eleman sayısı:", list.children.length);
```

**Çıktı:**

```text
Sayfadaki liste: Güneş (merkez), Merkür, Venüs, Mars
Çıktı alanında: Eleman sayısı: 4
```

**Maskot:** konusma pozu, alt-sag

## Sahne 4: kod (12 sn)

**Seslendirme:** remove bir elemanı sayfadan siler. Bir kutunun içini tamamen boşaltmak için içeriğini boş metin yapmak yeter.

**Ekranda başlık:** Silmek ve temizlemek

**Kod** (vurgulanan satırlar: 1, 2):

```js
document.querySelector("#old").remove();
document.querySelector("#list").textContent = "";
```

**Çıktı:**

```text
"Eski mesaj" paragrafı sayfadan kalkar, liste tamamen boşalır.
```

**Maskot:** isaret pozu, alt-sag

## Sahne 5: kod (18 sn)

**Seslendirme:** Asıl güç burada: veriyi dizide tutup ekranı diziden çizmek. render fonksiyonu listeyi önce temizler, sonra diziden baştan kurar. Kural basit: önce veriyi değiştir, sonra render çağır.

**Ekranda başlık:** Diziden liste: render()

**Kod** (vurgulanan satırlar: 4, 12, 13):

```js
const items = ["Oksijen", "Su", "Yakıt"];
const list = document.querySelector("#list");
function render() {
  list.textContent = "";
  for (const item of items) {
    const li = document.createElement("li");
    li.textContent = item;
    list.append(li);
  }
}
render();
items.push("Kalkan");
render();
```

**Çıktı:**

```text
Sayfada dört maddelik liste, her biri bir kez: Oksijen, Su, Yakıt, Kalkan
```

**Maskot:** mutlu pozu, alt-sag

*Yönetmen notu: Solda dizi, sağda liste; dizi değişince ok çizilir ve liste yeniden kurulur.*

## Sahne 6: hata (15 sn)

**Seslendirme:** Temizlemeyi unutursak ne olur? Hata mesajı çıkmaz ama her render eski listenin altına her şeyi bir kez daha ekler. Oksijen ve Su iki kez göründü! render'ın ilk işi temizlemek.

**Ekranda başlık:** Temizlemeyi unutmak

**Kod** (vurgulanan satırlar: 3, 4):

```js
const items = ["Oksijen", "Su"];
const list = document.querySelector("#list");
function render() {
  for (const item of items) {
    const li = document.createElement("li");
    li.textContent = item;
    list.append(li);
  }
}
render();
items.push("Yakıt");
render();
```

**Çıktı:**

```text
Sayfadaki liste: Oksijen, Su, Oksijen, Su, Yakıt
```

**Maskot:** uzgun pozu, sag

## Sahne 7: kod (15 sn)

**Seslendirme:** Bir elemanda kendi bilgini data ile başlayan niteliklerde saklayabilirsin. JavaScript'te bunlara dataset ile ulaşılır. Tireli adlar camelCase olur. Dikkat: değer her zaman metindir!

**Ekranda başlık:** dataset: data-* nitelikleri

**Kod** (vurgulanan satırlar: 2, 3, 4):

```js
const li = document.createElement("li");
li.dataset.id = 7;
li.dataset.maxSpeed = 900;
console.log(li.dataset.id, typeof li.dataset.id);
console.log(li.outerHTML);
```

**Çıktı:**

```text
Çıktı alanında:
7 string
<li data-id="7" data-max-speed="900"></li>
```

**Maskot:** konusma pozu, alt-sag

## Sahne 8: kod (17 sn)

**Seslendirme:** dataset ve olay yetkilendirme birlikte çok güçlü. render her Sil düğmesine sıra numarasını data-index olarak yazdı. Listeye tek dinleyici koyduk: tıklanan düğmenin sırasını okuyup diziden siliyor, sonra yeniden çiziyoruz.

**Ekranda başlık:** Tıklananı silmek

**Kod** (vurgulanan satırlar: 3, 4):

```js
list.addEventListener("click", (e) => {
  if (e.target.tagName !== "BUTTON") return;
  stars.splice(Number(e.target.dataset.index), 1);
  render();
});
```

**Çıktı:**

```text
Sirius'un yanındaki Sil düğmesine tıklanınca Sirius diziden çıkar ve liste yeniden çizilir: yalnızca Vega kalır.
```

**Maskot:** isaret pozu, alt-sag

## Sahne 9: soru (11 sn)

**Seslendirme:** Döngü üç yıldız oluşturuyor ama her birini prepend ile ekliyor. Sence liste hangi sırayla görünür?

**Ekranda başlık:** Sence sayfada ne görünür?

**Kod**:

```js
const list = document.querySelector("#list");
for (let i = 1; i <= 3; i++) {
  const li = document.createElement("li");
  li.textContent = "Yıldız " + i;
  list.prepend(li);
}
```

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (10 sn)

**Seslendirme:** Tersten! Her yeni yıldız başa eklendiği için en son oluşturulan Yıldız 3 en üstte duruyor.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 5):

```js
const list = document.querySelector("#list");
for (let i = 1; i <= 3; i++) {
  const li = document.createElement("li");
  li.textContent = "Yıldız " + i;
  list.prepend(li);
}
```

**Çıktı:**

```text
Sayfadaki liste: Yıldız 3, Yıldız 2, Yıldız 1
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (12 sn)

**Seslendirme:** Görevlerin: yük listesine kodla ilk elemanları ekle, diziden listeyi çizen bir render yaz ve her yüke kimlik etiketi takıp tıklananı bul.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: İlk elemanlar
- Görev 2: Diziden liste
- Görev 3: Kimlik etiketleri

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (11 sn)

**Seslendirme:** Özet: oluştur, doldur, ekle. Veriyi dizide tut, render ile önce temizle sonra çiz. Elemana bilgi saklamak için dataset kullan.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- createElement, append, prepend, remove
- render(): temizle, diziden baştan çiz
- dataset: data-* değerleri metindir

**Maskot:** on pozu, sag

## Sahne 13: kapanis (10 sn)

**Seslendirme:** İnşaat tamam, harika iş çıkardın! Yarın pilotlardan bilgi alacağız: formlardan değer okuyup doğrulamayı ve hataları sayfada göstermeyi öğreneceğiz.

**Ekranda başlık:** Yarın: Formlar

**Görsel:** `maskotlar/kodi-javascript/kahraman.png`

**Maskot:** tebrik pozu, sag
