# Video senaryosu: Gün 22, Animasyon

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~173 sn

Kodi, Piksel Gezegeni'nde requestAnimationFrame ile animasyon döngüsü kurmayı, update ve draw'u ayırmayı, hız ve kenardan sekme hesaplamayı ve zaman farkıyla (dt) her ekranda aynı hızda hareket etmeyi anlatıyor.

Ders metni: [gun-22.md](../gunler/gun-22.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | el-sallama (sag) |
| 2 | anlatim | 14 sn | konusma (sol) |
| 3 | kod | 17 sn | isaret (sag) |
| 4 | kod | 16 sn | konusma (sag) |
| 5 | kod | 18 sn | isaret (sol) |
| 6 | kod | 17 sn | konusma (sag) |
| 7 | kod | 14 sn | isaret (sol) |
| 8 | hata | 13 sn | sasirma (sag) |
| 9 | soru | 9 sn | dusunme (sag) |
| 10 | cikti | 8 sn | mutlu (sag) |
| 11 | gorev | 12 sn | isaret (sol) |
| 12 | ozet | 12 sn | konusma (sag) |
| 13 | kapanis | 11 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Kodi! Piksel Gezegeni'nde resimler kıpırdamaya başladı! Çizgi filmler gibi oyunlar da saniyede onlarca resmi art arda çizer. Bugün bir animasyon döngüsü kuruyoruz!

**Ekranda başlık:** Gün 22: Animasyon

**Görsel:** `gorseller/javascript/bolgeler/piksel.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: anlatim (14 sn)

**Seslendirme:** Ekrandaki her hareket aslında hızla değişen resimlerdir. Her karede üç şey olur: nesnelerin yerini biraz değiştir, eski resmi sil, yeni resmi çiz. Sonra tekrar!

**Ekranda başlık:** Animasyon nasıl çalışır?

**Ekranda maddeler:**

- 1. Yeri biraz değiştir
- 2. Eski resmi sil
- 3. Yeni resmi çiz

**Maskot:** konusma pozu, sol

*Yönetmen notu: Üç adım bir çark gibi dönerek gösterilir; her turda gemi biraz ilerler.*

## Sahne 3: kod (17 sn)

**Seslendirme:** Tarayıcı bunun için bize requestAnimationFrame verir: bir sonraki resmi çizmeden hemen önce bu fonksiyonu çalıştır. Fonksiyon kendini yeniden isteyince saniyede yaklaşık 60 karelik bir döngü olur.

**Ekranda başlık:** requestAnimationFrame

**Kod** (vurgulanan satırlar: 4, 6):

```js
function loop() {
  update();                    // hesapla
  draw();                      // çiz
  requestAnimationFrame(loop); // bir sonraki kareyi iste
}
requestAnimationFrame(loop);
```

**Çıktı:**

```text
loop saniyede yaklaşık 60 kez çalışır, sayfa donmaz.
```

**Maskot:** isaret pozu, sag

## Sahne 4: kod (16 sn)

**Seslendirme:** İyi bir alışkanlık: hesaplamayı ve çizimi ayır. update yalnızca sayıları değiştirir, draw yalnızca çizer. Böylece update'i tek başına çağırıp sonucunu kontrol edebilirsin.

**Ekranda başlık:** update ve draw'u ayır

**Kod** (vurgulanan satırlar: 3, 8):

```js
const ball = { x: 20, y: 60, r: 10, vx: 2 };
function update() {
  ball.x += ball.vx; // yalnızca sayıları değiştirir
}
update();
update();
update();
console.log(ball.x);
```

**Çıktı:**

```text
26
```

**Maskot:** konusma pozu, sag

## Sahne 5: kod (18 sn)

**Seslendirme:** Hız, her karede konumun ne kadar değişeceğidir. Kenara çarpınca geri dönmesi için hızın işaretini çeviririz. Burada top 195'te, sağ kenarı geçiyor ve hızı eksi üçe dönüyor.

**Ekranda başlık:** Hız ve kenardan sekme

**Kod** (vurgulanan satırlar: 4, 5):

```js
const canvas = { width: 200 };
const ball = { x: 195, r: 10, vx: 3 };
ball.x += ball.vx;
if (ball.x + ball.r > canvas.width || ball.x - ball.r < 0) {
  ball.vx = -ball.vx;
}
console.log(ball.x, ball.vx);
```

**Çıktı:**

```text
198 -3
```

**Maskot:** isaret pozu, sol

*Yönetmen notu: Yanda tuval üzerinde topun sağ duvara çarpıp geri döndüğü kısa bir animasyon.*

## Sahne 6: kod (17 sn)

**Seslendirme:** Bazı ekranlar saniyede 60, bazıları 120 kare çizer. Hızı saniye başına yazıp iki kare arasında geçen süreyle çarparsak oyun her ekranda aynı hızda oynar. Bu süreye dt diyoruz.

**Ekranda başlık:** Zaman farkı: dt

**Kod** (vurgulanan satırlar: 4, 5):

```js
const rocket = { x: 0, speed: 120 }; // piksel/saniye
let last = 1000;
const time = 1250;                   // rAF'ın verdiği zaman (ms)
const dt = (time - last) / 1000;     // saniye
rocket.x += rocket.speed * dt;
console.log(dt, rocket.x);
```

**Çıktı:**

```text
0.25 30
```

**Maskot:** konusma pozu, sag

## Sahne 7: kod (14 sn)

**Seslendirme:** Gerçek döngüde zamanı rAF kendisi verir. requestAnimationFrame bir numara da döndürür; cancelAnimationFrame o numarayı alınca döngü durur.

**Ekranda başlık:** Döngüde dt ve durdurmak

**Kod** (vurgulanan satırlar: 3, 7, 9):

```js
function loop(time) {
  if (!last) last = time;          // ilk kare
  const dt = (time - last) / 1000;
  last = time;
  update(dt);
  draw();
  frameId = requestAnimationFrame(loop);
}
// durdurmak için: cancelAnimationFrame(frameId);
```

**Çıktı:**

```text
Roket her ekranda saniyede 120 piksel ilerler.
```

**Maskot:** isaret pozu, sol

## Sahne 8: hata (13 sn)

**Seslendirme:** Sık hata: draw içinde eski resmi silmeyi unutmak. O zaman her kare bir öncekinin üstüne çizilir ve top arkasında uzun bir iz bırakır!

**Ekranda başlık:** Sık hata: clearRect'i unutmak

**Kod** (vurgulanan satırlar: 2):

```js
function draw() {
  // ctx.clearRect(0, 0, canvas.width, canvas.height); unutuldu!
  ctx.beginPath();
  ctx.arc(ball.x, ball.y, ball.r, 0, Math.PI * 2);
  ctx.fill();
}
```

**Çıktı:**

```text
Top hareket ederken arkasında kalın bir turuncu şerit kalır.
```

**Maskot:** sasirma pozu, sag

## Sahne 9: soru (9 sn)

**Seslendirme:** Soru zamanı! Kutu 10'da, hızı eksi 4. update iki kez çalışırsa sence x kaç olur?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```js
const box = { x: 10, vx: -4 };
function update() { box.x += box.vx; }
update();
update();
console.log(box.x);
```

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (8 sn)

**Seslendirme:** Cevap 2! Hız eksi olunca kutu her karede 4 piksel sola gider: 10, 6, sonra 2.

**Ekranda başlık:** Cevap

**Kod**:

```js
const box = { x: 10, vx: -4 };
function update() { box.x += box.vx; }
update();
update();
console.log(box.x);
```

**Çıktı:**

```text
2
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (12 sn)

**Seslendirme:** Görev zamanı! Önce kayan bir kutu için update ve draw yazacaksın. Sonra dört duvardan seken bir top, en sonda da saniyede 120 piksel giden bir roket.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: İlk hareket
- Görev 2: Duvardan sek
- Görev 3: Saniyede 120 piksel

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (12 sn)

**Seslendirme:** Özetleyelim: requestAnimationFrame ile döngü kur, update ile hesapla, draw ile sil ve çiz. Kenarda hızın işaretini çevir, hızı dt ile çarp.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- requestAnimationFrame(loop): her karede yeniden
- update hesaplar, draw siler ve çizer
- Sekme: vx = -vx  ·  Zaman: x += speed * dt

**Maskot:** konusma pozu, sag

## Sahne 13: kapanis (11 sn)

**Seslendirme:** Gemin artık uçuyor! Yarın Piksel Gezegeni'nin son durağında her şeyi birleştiriyoruz: çarpışmalar, skor ve oyun bitti. Gerçek bir oyun döngüsü! Görüşürüz!

**Ekranda başlık:** Yarın: Oyun döngüsü

**Görsel:** `gorseller/javascript/arka-plan/bg-space-wide.webp`

**Maskot:** tebrik pozu, orta
