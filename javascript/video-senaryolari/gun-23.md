# Video senaryosu: Gün 23, Oyun döngüsü

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~175 sn

Kodi, Piksel Gezegeni'nin son durağında oyunun durumunu tek nesnede tutmayı, güncelle-çarpış-çiz sırasını, AABB dikdörtgen çarpışmasını, filter ile yıldız toplamayı ve newGame ile yeniden başlatmayı anlatıyor.

Ders metni: [gun-23.md](../gunler/gun-23.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | el-sallama (sag) |
| 2 | kod | 15 sn | konusma (sag) |
| 3 | kod | 16 sn | isaret (sol) |
| 4 | kod | 19 sn | isaret (sag) |
| 5 | kod | 17 sn | konusma (sol) |
| 6 | kod | 15 sn | isaret (sag) |
| 7 | cikti | 13 sn | mutlu (sol) |
| 8 | hata | 14 sn | uzgun (sag) |
| 9 | soru | 9 sn | dusunme (sag) |
| 10 | cikti | 9 sn | mutlu (sag) |
| 11 | gorev | 12 sn | isaret (sol) |
| 12 | ozet | 12 sn | konusma (sag) |
| 13 | kapanis | 12 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Kodi! Piksel Gezegeni'nin son durağındayız. Çizmeyi ve hareket ettirmeyi öğrendin. Peki gemi bir yıldıza değdiğini nereden bilir? Bugün gerçek bir oyun döngüsü kuruyoruz!

**Ekranda başlık:** Gün 23: Oyun döngüsü

**Görsel:** `gorseller/javascript/bolgeler/piksel.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (15 sn)

**Seslendirme:** Oyunda o anki her şey, yani oyuncunun yeri, yıldızlar, skor ve oyun bitti mi, duruma dahildir. Hepsini tek bir nesnede tutarsak kaydetmek, yeniden başlatmak ve hata aramak kolaylaşır.

**Ekranda başlık:** Oyunun durumu tek yerde

**Kod** (vurgulanan satırlar: 1, 4, 5):

```js
const game = {
  player: { x: 20, y: 150, w: 30, h: 20 },
  stars: [{ x: 120, y: 40, w: 12, h: 12 }],
  score: 0,
  over: false,
};
```

**Maskot:** konusma pozu, sag

## Sahne 3: kod (16 sn)

**Seslendirme:** Her karede aynı sıra izlenir: önce hareket, sonra çarpışma, en son çizim. Oyun bitince update ve collide durur ama draw son hali göstermeye devam eder.

**Ekranda başlık:** Güncelle, çarpış, çiz

**Kod** (vurgulanan satırlar: 2, 3, 4, 6):

```js
function step() {
  if (!game.over) {
    update();   // her şeyi hareket ettir
    collide();  // çarpışmalar, puan
  }
  draw();       // durumu ekrana çiz
}
```

**Maskot:** isaret pozu, sol

## Sahne 4: kod (19 sn)

**Seslendirme:** İki dikdörtgen hem yatayda hem dikeyde üst üste biniyorsa çarpışır. Bunu dört koşulla yazarız. Biri bile yanlışsa aralarında boşluk vardır. Kenar kenara değmek çarpışma sayılmaz. Buna AABB testi denir.

**Ekranda başlık:** Dikdörtgen çarpışması (AABB)

**Kod** (vurgulanan satırlar: 2, 3):

```js
function hits(a, b) {
  return a.x < b.x + b.w && a.x + a.w > b.x &&
         a.y < b.y + b.h && a.y + a.h > b.y;
}
const ship = { x: 0, y: 0, w: 20, h: 20 };
console.log(hits(ship, { x: 10, y: 10, w: 20, h: 20 }));
console.log(hits(ship, { x: 20, y: 0, w: 20, h: 20 }));
```

**Çıktı:**

```text
true
false
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: İki kutu önce üst üste, sonra kenar kenara gösterilir; kesişen alan sarıyla boyanır.*

## Sahne 5: kod (17 sn)

**Seslendirme:** Değen yıldızları çıkarmanın güvenli yolu filter. Önce kaç yıldız olduğunu saklarız; farkı skora ekleriz. Yıldız kalmayınca oyun biter.

**Ekranda başlık:** Yıldız toplamak

**Kod** (vurgulanan satırlar: 2, 3, 4):

```js
const before = game.stars.length;
game.stars = game.stars.filter((s) => !hits(game.player, s));
game.score += before - game.stars.length;
if (game.stars.length === 0) game.over = true;
```

**Çıktı:**

```text
Gemi yıldıza değince yıldız kaybolur, skor 1 artar.
```

**Maskot:** konusma pozu, sol

## Sahne 6: kod (15 sn)

**Seslendirme:** Yeniden başlatmak için durumu sıfırdan kuran bir fonksiyon yazarız. Her çağrıda yepyeni bir nesne ve yepyeni bir dizi üretir. Böylece toplanan yıldızlar geri gelir.

**Ekranda başlık:** Yeniden başla: newGame

**Kod** (vurgulanan satırlar: 2, 6):

```js
function newGame() {
  return { score: 0, over: false, stars: [{ x: 50, y: 20, w: 10, h: 10 }] };
}
let game = newGame();
game.stars = []; game.score = 1; game.over = true;
game = newGame();
console.log(game.score, game.over, game.stars.length);
```

**Çıktı:**

```text
0 false 1
```

**Maskot:** isaret pozu, sag

## Sahne 7: cikti (13 sn)

**Seslendirme:** Hepsini birleştirince mini bir oyun çıkıyor: ok tuşlarıyla gemiyi yönet, yıldızları topla. Hepsi bitince tebrik mesajı gelir, R ile yeniden başlarsın.

**Ekranda başlık:** Mini oyun: yıldız topla

**Çıktı:**

```text
Skor: 0 → Skor: 1 → Skor: 2 → Tebrikler! Yeniden başlamak için R tuşu
```

**Maskot:** mutlu pozu, sol

*Yönetmen notu: Mini oyunun kısa bir ekran kaydı: mavi gemi üç sarı yıldızı toplar.*

## Sahne 8: hata (14 sn)

**Seslendirme:** Sık hata: yeniden başlatırken yalnızca skoru ve over'ı sıfırlamak. Yıldız dizisi hâlâ boş! Oyun baştan başlar ama ekranda toplanacak tek bir yıldız bile kalmaz.

**Ekranda başlık:** Sık hata: durumu yarım sıfırlamak

**Kod** (vurgulanan satırlar: 4):

```js
let game = { score: 3, over: true, stars: [] }; // hepsi toplandı
function restart() {
  game.score = 0;
  game.over = false; // ya yıldızlar?
}
restart();
console.log(game.stars.length);
```

**Çıktı:**

```text
0   (yıldızlar geri gelmedi)
```

**Maskot:** uzgun pozu, sag

## Sahne 9: soru (9 sn)

**Seslendirme:** Soru zamanı! Gemi sıfırdan başlıyor ve 20 genişliğinde. Meteor ise 25'te. Sence çarpışırlar mı?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```js
const ship = { x: 0, y: 0, w: 20, h: 20 };
const rock = { x: 25, y: 5, w: 10, h: 10 };
console.log(hits(ship, rock));
```

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (9 sn)

**Seslendirme:** Cevap false! Geminin sağ kenarı 20'de bitiyor, meteor 25'te başlıyor. Arada beş piksellik boşluk var.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 2):

```js
function hits(a, b) {
  return a.x < b.x + b.w && a.x + a.w > b.x &&
         a.y < b.y + b.h && a.y + a.h > b.y;
}
const ship = { x: 0, y: 0, w: 20, h: 20 };
const rock = { x: 25, y: 5, w: 10, h: 10 };
console.log(hits(ship, rock));
```

**Çıktı:**

```text
false
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (12 sn)

**Seslendirme:** Görev zamanı! Önce iki dikdörtgenin çarpışıp çarpışmadığını söyleyen fonksiyonu yazacaksın. Sonra can götüren meteorlar, en sonda da bir yeniden başla düğmesi.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Çarpışıyor mu?
- Görev 2: Meteor çarpınca
- Görev 3: Yeniden başla

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (12 sn)

**Seslendirme:** Özetleyelim: durumu tek nesnede tut. Her karede güncelle, çarpışmaya bak, çiz. Dört koşullu hits ile çarpışmayı bul, filter ile topla ve newGame ile yeniden başla.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- game = { player, stars, score, over }
- update → collide → draw
- hits(a, b): 4 koşul  ·  filter ile topla  ·  newGame()

**Maskot:** konusma pozu, sag

## Sahne 13: kapanis (12 sn)

**Seslendirme:** Tebrikler, Piksel Gezegeni'ni tamamladın ve ilk oyun döngünü kurdun! Yarın Async İstasyonu'na yanaşıyoruz. İlk konu: hatalar ve hata ayıklama. Görüşürüz!

**Ekranda başlık:** Yarın: Hatalar ve hata ayıklama

**Görsel:** `gorseller/javascript/bolgeler/istasyon.webp`

**Maskot:** tebrik pozu, orta
