# Video senaryosu: Gün 29, Projeyi toparlama

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~178 sn

Kodi, JavaScript Yıldızı yolunda projeyi herkes için kullanışlı yapmayı anlatıyor: düğme ve klavyeyi aynı fonksiyona bağlamak, küçük ekranlar için matchMedia, aria-label, aria-expanded, aria-live ve focus ile erişilebilirlik, init/update/render düzeni.

Ders metni: [gun-29.md](../gunler/gun-29.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 13 sn | el-sallama (sag) |
| 2 | kod | 18 sn | isaret (sag) |
| 3 | anlatim | 14 sn | konusma (sol) |
| 4 | kod | 13 sn | isaret (sag) |
| 5 | anlatim | 18 sn | konusma (sol) |
| 6 | kod | 14 sn | isaret (sag) |
| 7 | kod | 18 sn | konusma (sol) |
| 8 | hata | 14 sn | uzgun (sag) |
| 9 | soru | 10 sn | dusunme (sag) |
| 10 | cikti | 10 sn | mutlu (sag) |
| 11 | gorev | 13 sn | isaret (sol) |
| 12 | ozet | 12 sn | konusma (sag) |
| 13 | kapanis | 11 sn | el-sallama (orta) |

## Sahne 1: acilis (13 sn)

**Seslendirme:** Selam, ben Kodi! Projen neredeyse hazır, kaptan. Ama arkadaşın onu telefonda açınca klavye yok, ekran küçük. Peki herkes oynayabilir mi? Bugün projeni herkes için kullanışlı yapıyoruz!

**Ekranda başlık:** Gün 29: Projeyi toparlama

**Görsel:** `gorseller/javascript/bolgeler/yildiz.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (18 sn)

**Seslendirme:** Çözüm: ekrana düğmeler koy ve hem tuşlar hem düğmeler aynı fonksiyonu çağırsın. Hareketin tek bir yeri olur: move. click hem fareyle hem dokunmayla çalışır.

**Ekranda başlık:** Düğme ve tuş, tek fonksiyon

**Kod** (vurgulanan satırlar: 1, 5, 8):

```js
function move(dx) {
  x = Math.min(10, Math.max(0, x + dx));
  pos.textContent = `Konum: ${x}`;
}
leftBtn.addEventListener("click", () => move(-1));
rightBtn.addEventListener("click", () => move(1));
document.addEventListener("keydown", (e) => {
  if (e.key === "ArrowLeft") move(-1);
  if (e.key === "ArrowRight") move(1);
});
```

**Çıktı:**

```text
◀ düğmesi de sol ok tuşu da "Konum: 4" yazdırır.
```

**Maskot:** isaret pozu, sag

## Sahne 3: anlatim (14 sn)

**Seslendirme:** Basılı tutmayı algılamak istersen pointerdown ve pointerup kullan; fare, parmak ve kalemin hepsinde çalışırlar. Parmak imleçten büyüktür: düğmeler en az 44 piksel olsun.

**Ekranda başlık:** Dokunmatik kontroller

**Ekranda maddeler:**

- click: fare + dokunma
- pointerdown / pointerup: basılı tutma
- Dokunulacak düğmeler en az 44–48 piksel

**Maskot:** konusma pozu, sol

## Sahne 4: kod (13 sn)

**Seslendirme:** Düzeni çoğunlukla CSS'teki media kuralları ayarlar. JavaScript'te de ekranı sorabilirsin: matchMedia'nın matches değeri o anki durumu true ya da false verir.

**Ekranda başlık:** Küçük ekranlar: matchMedia

**Kod** (vurgulanan satırlar: 1):

```js
const isSmall = window.matchMedia("(max-width: 600px)").matches;
if (isSmall) {
  console.log("Küçük ekran: dokunmatik düğmeleri göster");
}
```

**Çıktı:**

```text
Telefonda: Küçük ekran: dokunmatik düğmeleri göster
```

**Maskot:** isaret pozu, sag

## Sahne 5: anlatim (18 sn)

**Seslendirme:** Bazı kullanıcılar ekran okuyucu kullanır, bazıları yalnızca klavyeyle gezinir. Tıklanan şey için button kullan. Simge düğmelerine aria-label ver, değişen mesajlara aria-live ekle, focus ile odağı doğru yere taşı.

**Ekranda başlık:** Erişilebilirlik: herkes kullanabilsin

**Ekranda maddeler:**

- <div> değil <button>: Tab, Enter, Boşluk kendiliğinden
- aria-label="Sola git" (◀ yerine okunur)
- aria-live="polite": değişen mesajlar okunur
- element.focus(): odağı taşı

**Maskot:** konusma pozu, sol

## Sahne 6: kod (14 sn)

**Seslendirme:** Açılır menüde düğme, menünün açık mı kapalı mı olduğunu aria-expanded ile söyler. Ekran okuyucu önce daraltılmış, açınca genişletilmiş diye okur.

**Ekranda başlık:** Örnek: açılır menü

**Kod** (vurgulanan satırlar: 4, 5):

```js
btn.addEventListener("click", () => {
  const open = nav.hidden; // gizliyse şimdi açılacak
  nav.hidden = !open;
  btn.setAttribute("aria-expanded", String(open));
  btn.setAttribute("aria-label", open ? "Menüyü kapat" : "Menüyü aç");
});
```

**Çıktı:**

```text
Menü açılır; ekran okuyucu: "Menüyü kapat, genişletilmiş"
```

**Maskot:** isaret pozu, sag

## Sahne 7: kod (18 sn)

**Seslendirme:** Proje büyüdükçe kod dağılır. Üç parçalı düzen işini kolaylaştırır: veriler tek bir state nesnesinde, update yalnızca veriyi değiştirir, render yalnızca ekrana çizer. init ise olayları bağlar ve ilk çizimi yapar.

**Ekranda başlık:** init, update, render

**Kod** (vurgulanan satırlar: 2, 5):

```js
const state = { score: 0 };
function update(action) {
  if (action === "star") state.score += 10;
}
function render() {
  console.log(`Skor: ${state.score}`); // sayfada: scoreEl.textContent
}
render();
update("star");
update("star");
render();
```

**Çıktı:**

```text
Skor: 0
Skor: 20
```

**Maskot:** konusma pozu, sol

## Sahne 8: hata (14 sn)

**Seslendirme:** Sık hata: tıklanan şeyi div ile yapmak. Fareyle çalışır ama Tab ile seçilemez, Enter ile basılamaz. Ekran okuyucu da onun bir düğme olduğunu bilmez!

**Ekranda başlık:** Sık hata: düğme yerine div

**Kod** (vurgulanan satırlar: 1):

```html
<div id="left">◀</div>                            <!-- klavyeyle kullanılamaz -->
<button id="left" aria-label="Sola git">◀</button> <!-- doğrusu -->
```

**Maskot:** uzgun pozu, sag

## Sahne 9: soru (10 sn)

**Seslendirme:** Soru zamanı! update iki kez çağrıldı ama render hiç çağrılmadı. Sence skor ve ekrandaki yazı ne olur?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```js
const state = { score: 0 };
let screen = "Skor: 0"; // ekrandaki yazı
function update(action) { if (action === "star") state.score += 10; }
function render() { screen = `Skor: ${state.score}`; }
update("star");
update("star");
console.log(state.score, screen);
```

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (10 sn)

**Seslendirme:** Cevap: skor 20 ama ekranda hâlâ Skor sıfır yazıyor! Ekrana yalnızca render dokunur. Veriyi değiştirince render'ı çağırmayı unutma.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 7):

```js
const state = { score: 0 };
let screen = "Skor: 0"; // ekrandaki yazı
function update(action) { if (action === "star") state.score += 10; }
function render() { screen = `Skor: ${state.score}`; }
update("star");
update("star");
console.log(state.score, screen);
```

**Çıktı:**

```text
20 Skor: 0
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (13 sn)

**Seslendirme:** Görev zamanı! Düğmelerin ve ok tuşlarının aynı fonksiyonu çağırdığı bir kontrol, etiketli ve odağı taşıyan simge düğmeleri ve init, update, render düzeninde bir yakıt göstergesi yapacaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Tek fonksiyon, iki yol
- Görev 2: Etiket ve odak
- Görev 3: init, update, render

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (12 sn)

**Seslendirme:** Özetleyelim: düğme ve klavye aynı fonksiyonu çağırsın. button, aria-label ve focus ile herkes kullanabilsin. Veriyi update değiştirsin, ekrana render çizsin.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- Tek fonksiyon: move(dx) ← düğme + tuş
- button, aria-label, aria-expanded, aria-live, focus()
- state + update + render + init

**Maskot:** konusma pozu, sag

## Sahne 13: kapanis (11 sn)

**Seslendirme:** Projen artık herkes için hazır! Yarın yolculuğumuzun son günü: parçaları birleştirecek, projeni yayınlamayı öğrenecek ve JavaScript Yıldızı'na ulaşacağız. Görüşürüz!

**Ekranda başlık:** Yarın: Final

**Görsel:** `gorseller/javascript/arka-plan/bg-space-wide.webp`

**Maskot:** el-sallama pozu, orta
