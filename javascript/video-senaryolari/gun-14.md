# Video senaryosu: Gün 14, Olaylar

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~158 sn

DOM Gezegeni'nde sayfayı olaylara kulak veren bir kontrol paneline çeviriyoruz: addEventListener, e.target, input olayı, durum ile ekranı güncellemek, tek seferlik dinleyici ve olay yetkilendirme.

Ders metni: [gun-14.md](../gunler/gun-14.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 11 sn | el-sallama (sag) |
| 2 | kod | 15 sn | isaret (alt-sag) |
| 3 | kod | 17 sn | konusma (alt-sag) |
| 4 | kod | 15 sn | mutlu (alt-sag) |
| 5 | hata | 15 sn | uzgun (sag) |
| 6 | kod | 14 sn | konusma (alt-sag) |
| 7 | kod | 17 sn | isaret (alt-sag) |
| 8 | soru | 11 sn | dusunme (sag) |
| 9 | cikti | 10 sn | mutlu (sag) |
| 10 | gorev | 12 sn | isaret (sol) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 10 sn | tebrik (sag) |

## Sahne 1: acilis (11 sn)

**Seslendirme:** Selam, ben Kodi! DOM Gezegeni'nde her şey sana tepki vermeyi bekliyor. Bir düğmeye basmak, bir kutuya harf yazmak... Bunların hepsi birer olay. Sayfamız onları nasıl duyacak?

**Ekranda başlık:** Gün 14: Olaylar

**Görsel:** `gorseller/javascript/bolgeler/dom.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (15 sn)

**Seslendirme:** addEventListener bir elemana, bu olay olunca şu fonksiyonu çalıştır der. Fonksiyon hemen çalışmaz; düğmeye her tıklandığında çalışır. Kodu çalıştırdıktan sonra düğmeye kendin tıkla.

**Ekranda başlık:** addEventListener: olayı dinle

**Kod** (vurgulanan satırlar: 2):

```js
const btn = document.querySelector("#start");
btn.addEventListener("click", () => {
  console.log("Tıklandı!");
});
```

**Çıktı:**

```text
Başla düğmesine her tıklandığında Çıktı alanına bir satır "Tıklandı!" eklenir.
```

**Maskot:** isaret pozu, alt-sag

*Yönetmen notu: İmleç düğmeye üç kez tıklar, Çıktı alanında üç satır belirir.*

## Sahne 3: kod (17 sn)

**Seslendirme:** Tarayıcı dinleyiciye bir olay nesnesi verir, adı genelde e. e.target, olayın olduğu elemandır. count değişkeni sayfanın durumu: olay durumu değiştirir, biz de ekranı durumdan güncelleriz.

**Ekranda başlık:** Olay nesnesi ve e.target

**Kod** (vurgulanan satırlar: 4, 5, 6, 7):

```js
let count = 0;
const btn = document.querySelector("#btn");

btn.addEventListener("click", (e) => {
  count++;
  document.querySelector("#info").textContent = `${count} tıklama`;
  console.log("Tıklanan:", e.target.textContent);
});
```

**Çıktı:**

```text
Üç tıklamadan sonra sayfada "3 tıklama" yazar; Çıktı alanında her tıklamada "Tıklanan: Tıkla" satırı çıkar.
```

**Maskot:** konusma pozu, alt-sag

## Sahne 4: kod (15 sn)

**Seslendirme:** Bir kutuya her harf yazıldığında input olayı olur. Kutudaki metin value özelliğinde. Böylece paragraf, sen yazdıkça canlı canlı güncelleniyor.

**Ekranda başlık:** input olayı ve value

**Kod** (vurgulanan satırlar: 4, 5):

```js
const input = document.querySelector("#name");
const hello = document.querySelector("#hello");

input.addEventListener("input", () => {
  hello.textContent = "Merhaba, " + input.value + "!";
});
```

**Çıktı:**

```text
Kutuya "Ada" yazıldıkça paragraf harf harf güncellenir ve sonunda "Merhaba, Ada!" olur.
```

**Maskot:** mutlu pozu, alt-sag

## Sahne 5: hata (15 sn)

**Seslendirme:** Sık yapılan hata: fonksiyonu verirken parantez koymak. launch parantezle yazılınca hemen bir kez çalışır ve tıklamayı hiç dinlemez. Doğrusu parantezsiz: sadece launch.

**Ekranda başlık:** launch mı, launch() mı?

**Kod** (vurgulanan satırlar: 5):

```js
function launch() {
  console.log("Kalkış!");
}
const btn = document.querySelector("#start");
btn.addEventListener("click", launch());
```

**Çıktı:**

```text
Kod çalışır çalışmaz Çıktı alanına bir kez "Kalkış!" yazılır; düğmeye tıklamak hiçbir şey yapmaz.
```

**Maskot:** uzgun pozu, sag

## Sahne 6: kod (14 sn)

**Seslendirme:** Bazen bir dinleyici sadece bir kez çalışmalı. once true yazarsak ilk tıklamadan sonra kendiliğinden kalkar. Elle kaldırmak için removeEventListener aynı adlı fonksiyonu ister.

**Ekranda başlık:** Tek seferlik dinleyici

**Kod** (vurgulanan satırlar: 4):

```js
const btn = document.querySelector("#launch");
btn.addEventListener("click", () => {
  console.log("Kalkış!");
}, { once: true });
```

**Çıktı:**

```text
İlk tıklamada Çıktı alanına "Kalkış!" yazılır; sonraki tıklamalar hiçbir şey yapmaz.
```

**Maskot:** konusma pozu, alt-sag

## Sahne 7: kod (17 sn)

**Seslendirme:** Tıklama olayı kabarcık gibi yukarı, kapsayan elemanlara yükselir. Bu yüzden her düğmeye ayrı dinleyici yerine kutuya tek dinleyici koyarız. Buna olay yetkilendirme denir; e.target hangi düğme olduğunu söyler.

**Ekranda başlık:** Olay yetkilendirme

**Kod** (vurgulanan satırlar: 3, 4, 5):

```js
const hello = document.querySelector("#hello");
const colors = { "kırmızı": "#d1242f", "mavi": "#1f6feb" };
document.querySelector("#colors").addEventListener("click", (e) => {
  if (e.target.tagName !== "BUTTON") return;
  hello.style.color = colors[e.target.textContent];
});
```

**Çıktı:**

```text
"mavi" düğmesine tıklanınca "Merhaba!" yazısı maviye, "kırmızı"ya tıklanınca kırmızıya döner. Tek dinleyici iki düğmeyi de yönetir.
```

**Maskot:** isaret pozu, alt-sag

*Yönetmen notu: Tıklanan düğmeden kutuya doğru yükselen küçük bir kabarcık animasyonu.*

## Sahne 8: soru (11 sn)

**Seslendirme:** Üç canla başlıyoruz. Vur düğmesine iki kez tıklarsan paragrafta ne yazar? Durdur ve düşün.

**Ekranda başlık:** Sence sayfada ne yazar?

**Kod**:

```js
let lives = 3;
const btn = document.querySelector("#hit");
const text = document.querySelector("#lives");
btn.addEventListener("click", () => {
  lives--;
  text.textContent = "Can: " + lives;
});
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (10 sn)

**Seslendirme:** Can: 1! Her tıklamada önce durum bir azaldı, sonra ekran yeni durumla güncellendi.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 5, 6):

```js
let lives = 3;
const btn = document.querySelector("#hit");
const text = document.querySelector("#lives");
btn.addEventListener("click", () => {
  lives--;
  text.textContent = "Can: " + lives;
});
```

**Çıktı:**

```text
İki tıklamadan sonra sayfada: Can: 1
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (12 sn)

**Seslendirme:** Görevlerin: kontrol panelinde hızı düğmelerle yönet, çağrı adını yazıldıkça göster ve yalnızca bir kez çalışan bir kalkış düğmesi yap.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Hız kontrolü
- Görev 2: Çağrı adı
- Görev 3: Tek seferlik kalkış

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (11 sn)

**Seslendirme:** Özet: addEventListener olayı dinler, e.target olayın olduğu elemanı söyler. Önce durumu değiştir, sonra ekranı güncelle. Çok düğme için tek dinleyici yeter.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- addEventListener("click", fonksiyon): parantezsiz
- e.target, input olayı ve value
- Durum → ekran; olay yetkilendirme

**Maskot:** on pozu, sag

## Sahne 12: kapanis (10 sn)

**Seslendirme:** Sayfan artık seni dinliyor, bravo! Yarın DOM Gezegeni'nde inşaat var: JavaScript ile sıfırdan yeni elemanlar üretip sayfaya ekleyeceğiz.

**Ekranda başlık:** Yarın: Eleman oluşturmak

**Görsel:** `maskotlar/kodi-javascript/kahraman.png`

**Maskot:** tebrik pozu, sag
