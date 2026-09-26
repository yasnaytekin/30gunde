# Video senaryosu: Gün 13, DOM'a giriş

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~170 sn

DOM Gezegeni'ne iniyoruz: sayfanın DOM ağacını tanıyor, querySelector ile eleman buluyor; metnini, sınıfını, stilini ve niteliklerini JavaScript ile değiştiriyoruz.

Ders metni: [gun-13.md](../gunler/gun-13.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 11 sn | el-sallama (sag) |
| 2 | anlatim | 13 sn | konusma (sag) |
| 3 | kod | 16 sn | isaret (alt-sag) |
| 4 | kod | 16 sn | mutlu (alt-sag) |
| 5 | kod | 15 sn | konusma (alt-sag) |
| 6 | kod | 16 sn | isaret (alt-sag) |
| 7 | kod | 14 sn | konusma (alt-sag) |
| 8 | hata | 15 sn | sasirma (sag) |
| 9 | soru | 11 sn | dusunme (sag) |
| 10 | cikti | 10 sn | mutlu (sag) |
| 11 | gorev | 12 sn | isaret (sol) |
| 12 | ozet | 11 sn | on (sag) |
| 13 | kapanis | 10 sn | tebrik (sag) |

## Sahne 1: acilis (11 sn)

**Seslendirme:** Selam, ben Kodi! DOM Gezegeni'ne iniş yaptık. Buradaki her şey bir web sayfası: başlıklar, paragraflar, düğmeler. Peki JavaScript sayfaya nasıl dokunur?

**Ekranda başlık:** Gün 13: DOM'a giriş

**Görsel:** `gorseller/javascript/bolgeler/dom.webp`

**Maskot:** el-sallama pozu, sag

*Yönetmen notu: Roket gezegene iner; yüzeyde web sayfası parçaları parlar.*

## Sahne 2: anlatim (13 sn)

**Seslendirme:** Tarayıcı bir HTML sayfasını açınca onu bir ağaca çevirir. Her etiket bir nesne olur. Bu ağacın adı DOM, kökü de document. Nesneyi değiştirdiğin an sayfa da değişir.

**Ekranda başlık:** DOM nedir?

**Ekranda maddeler:**

- HTML → nesnelerden bir ağaç
- Ağacın kökü: document
- Nesneyi değiştir, sayfa değişsin

**Maskot:** konusma pozu, sag

*Yönetmen notu: document'tan dallanan h1, p, ul ve li kutucuklarıyla bir ağaç çizilir.*

## Sahne 3: kod (16 sn)

**Seslendirme:** querySelector, CSS seçicisine uyan ilk elemanı verir: id için diyez, sınıf için nokta. Hepsini almak için querySelectorAll kullanırız; dönen listeyi for of ile gezeriz.

**Ekranda başlık:** querySelector ile eleman bulmak

**Kod** (vurgulanan satırlar: 1, 2, 3):

```js
const title = document.querySelector("#title");
const note = document.querySelector(".note");
const planets = document.querySelectorAll(".planet");
console.log(planets.length);
for (const p of planets) {
  console.log(p.textContent);
}
```

**Çıktı:**

```text
Çıktı alanında:
3
Merkür
Venüs
Mars
```

**Maskot:** isaret pozu, alt-sag

## Sahne 4: kod (16 sn)

**Seslendirme:** Elemanı bulduk, şimdi değiştirelim. textContent içindeki metni değiştirir, style tek bir stili verir, classList.add de bir sınıf ekler. Çalıştır'a basınca sayfa anında değişiyor!

**Ekranda başlık:** Metni ve görünümü değiştirmek

**Kod** (vurgulanan satırlar: 2, 3, 7):

```js
const title = document.querySelector("#title");
title.textContent = "Merhaba, DOM Gezegeni!";
title.style.color = "#d63384";

const note = document.querySelector(".note");
note.textContent = "Bu satırı JavaScript yazdı.";
note.classList.add("big");
```

**Çıktı:**

```text
Sayfada pembe renkli "Merhaba, DOM Gezegeni!" başlığı ve altında büyük yazılı "Bu satırı JavaScript yazdı." paragrafı görünür.
```

**Maskot:** mutlu pozu, alt-sag

*Yönetmen notu: Önizlemede eski metinler silinip yenileri yazılır, başlık pembeye döner.*

## Sahne 5: kod (15 sn)

**Seslendirme:** innerHTML verdiğin metni HTML olarak yorumlar, textContent ise düz metin olarak yazar. Güvenlik kuralı: kullanıcının yazdığı metni asla innerHTML ile koyma. Metin için hep textContent.

**Ekranda başlık:** textContent ve innerHTML

**Kod** (vurgulanan satırlar: 1, 2):

```js
document.querySelector("#a").innerHTML = "<b>Kalın</b>";
document.querySelector("#b").textContent = "<b>Kalın</b>";
```

**Çıktı:**

```text
Birinci satırda kalın bir "Kalın" kelimesi; ikinci satırda etiketleriyle birlikte düz metin: <b>Kalın</b>
```

**Maskot:** konusma pozu, alt-sag

## Sahne 6: kod (16 sn)

**Seslendirme:** Görünümü değiştirmenin en temiz yolu sınıflar. add ekler, remove çıkarır, toggle varsa çıkarır yoksa ekler. CSS'teki tireli adlar style'da camelCase olur: backgroundColor.

**Ekranda başlık:** classList ve style

**Kod** (vurgulanan satırlar: 2, 3, 4, 6):

```js
const panel = document.querySelector("#panel");
panel.classList.remove("closed");
panel.classList.add("glow");
panel.classList.toggle("dark");
console.log(panel.classList.contains("glow"));
panel.style.backgroundColor = "#0b1026";
```

**Çıktı:**

```text
Çıktı alanında: true
Sayfada gizli panel görünür olur; parlayan, koyu temalı ve lacivert arka planlı.
```

**Maskot:** isaret pozu, alt-sag

## Sahne 7: kod (14 sn)

**Seslendirme:** href, src, disabled gibi niteliklere de ulaşabiliriz. setAttribute değiştirir, getAttribute okur, removeAttribute kaldırır. Kalkış düğmesi artık tıklanabilir!

**Ekranda başlık:** Nitelikler

**Kod** (vurgulanan satırlar: 2, 3, 5):

```js
const link = document.querySelector("#docs");
link.setAttribute("href", "https://developer.mozilla.org");
console.log(link.getAttribute("href"));
const btn = document.querySelector("#launch");
btn.removeAttribute("disabled");
```

**Çıktı:**

```text
Çıktı alanında: https://developer.mozilla.org
Sayfada Belgeler bağlantısı MDN'e gider; Kalkış düğmesi artık tıklanabilir.
```

**Maskot:** konusma pozu, alt-sag

## Sahne 8: hata (15 sn)

**Seslendirme:** En sık hata: seçicide diyezi unutmak. status diye bir etiket yok, querySelector null döndürdü. null'ın metni değiştirilemez. Bu hatayı görürsen seçicini kontrol et: diyez mi, nokta mı?

**Ekranda başlık:** Cannot set properties of null

**Kod** (vurgulanan satırlar: 1):

```js
const status = document.querySelector("status");
status.textContent = "İniş tamam!";
```

**Çıktı:**

```text
TypeError: Cannot set properties of null (setting 'textContent')
```

**Maskot:** sasirma pozu, sag

## Sahne 9: soru (11 sn)

**Seslendirme:** Sayfada üç gezegen var ve querySelector ile metni değiştiriyoruz. Sence kaç gezegenin yazısı değişir?

**Ekranda başlık:** Sence sayfada ne olur?

**Kod**:

```js
const p = document.querySelector(".planet");
p.textContent = "Ziyaret edildi";
```

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (10 sn)

**Seslendirme:** Sadece biri! querySelector uyan ilk elemanı verir; Venüs ile Mars olduğu gibi kaldı. Hepsi için querySelectorAll gerekir.

**Ekranda başlık:** Cevap

**Kod**:

```js
const p = document.querySelector(".planet");
p.textContent = "Ziyaret edildi";
```

**Çıktı:**

```text
Sayfadaki liste: Ziyaret edildi, Venüs, Mars
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (12 sn)

**Seslendirme:** Bugünden itibaren görevlerde hazır bir sayfa var; sen yalnızca JavaScript yazıyorsun. Görev merkezine ilk dokunuşu yap, paneli sınıf ve stille hazırla, sonra bütün gezegenleri işaretle.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: İlk dokunuş
- Görev 2: Sınıf ve stil
- Görev 3: Bütün gezegenler

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (11 sn)

**Seslendirme:** Özet: sayfa bir DOM ağacıdır. querySelector ile elemanı bul, sonra metnini, sınıfını, stilini ve niteliklerini değiştir.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- querySelector ilkini, querySelectorAll hepsini verir
- Metin için textContent
- classList, style ve setAttribute

**Maskot:** on pozu, sag

## Sahne 13: kapanis (10 sn)

**Seslendirme:** Sayfaya ilk dokunuşun tamam, tebrikler! Yarın sayfa sana tepki verecek: düğmeye basınca, kutuya yazınca. Olaylar geliyor!

**Ekranda başlık:** Yarın: Olaylar

**Görsel:** `maskotlar/kodi-javascript/kahraman.png`

**Maskot:** tebrik pozu, sag
