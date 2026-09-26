# Video senaryosu: Gün 27, Sınıflar ve modüller

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~152 sn

Kodi, Async İstasyonu'nun gemi fabrikasında class ile nesne kalıpları yazmayı; constructor, this, metot, getter, extends ve super kullanmayı ve kodu modüllere bölme fikrini anlatıyor.

Ders metni: [gun-27.md](../gunler/gun-27.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | el-sallama (sag) |
| 2 | kod | 18 sn | isaret (sag) |
| 3 | kod | 18 sn | konusma (sol) |
| 4 | kod | 18 sn | isaret (sag) |
| 5 | anlatim | 16 sn | konusma (sol) |
| 6 | hata | 14 sn | sasirma (sag) |
| 7 | soru | 10 sn | dusunme (sag) |
| 8 | cikti | 9 sn | mutlu (sag) |
| 9 | gorev | 13 sn | isaret (sol) |
| 10 | ozet | 12 sn | konusma (sag) |
| 11 | kapanis | 12 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Kodi! İstasyonda onlarca gemi var ve hepsinin adı, hızı, yakıtı var. Her birini tek tek yazmak yerine bir kalıp yapsak? Bugün sınıflarla bir gemi fabrikası kuruyoruz!

**Ekranda başlık:** Gün 27: Sınıflar ve modüller

**Görsel:** `gorseller/javascript/bolgeler/istasyon.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (18 sn)

**Seslendirme:** Sınıf bir kalıp gibi çalışır. new ile kalıptan yeni bir nesne, yani bir örnek üretiriz. constructor nesne üretilirken bir kez çalışır; this ise şu anki nesne demektir. Sınıf adları büyük harfle başlar.

**Ekranda başlık:** Sınıf: nesne kalıbı

**Kod** (vurgulanan satırlar: 2, 3, 7):

```js
class Ship {
  constructor(name, speed) {
    this.name = name;
    this.speed = speed;
  }
}
const a = new Ship("Kartal", 10);
const b = new Ship("Şahin", 12);
console.log(a.name, b.speed);
```

**Çıktı:**

```text
Kartal 12
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: Bir fabrika bandından aynı kalıpla iki farklı gemi çıkar.*

## Sahne 3: kod (18 sn)

**Seslendirme:** Sınıfın içine yazılan fonksiyonlara metot denir; başlarına function yazılmaz. fly yakıtı azaltır. get ile yazılan isEmpty ise parantezsiz, bir özellik gibi okunur ama her seferinde yeniden hesaplanır.

**Ekranda başlık:** Metotlar ve getter

**Kod** (vurgulanan satırlar: 3, 6, 12):

```js
class Ship {
  constructor(name) { this.name = name; this.fuel = 100; }
  fly(km) {
    this.fuel -= km / 10;
  }
  get isEmpty() {
    return this.fuel <= 0;
  }
}
const s = new Ship("Kartal");
s.fly(300);
console.log(s.fuel, s.isEmpty);
```

**Çıktı:**

```text
70 false
```

**Maskot:** konusma pozu, sol

## Sahne 4: kod (18 sn)

**Seslendirme:** Bir sınıfı extends ile genişletebilirsin; yeni sınıf eskisinin her şeyini miras alır. super, üst sınıfın constructor'ını çağırır ve this'ten önce yazılır. super.describe ise üstteki metodu kullanıp genişletir.

**Ekranda başlık:** extends ve super

**Kod** (vurgulanan satırlar: 5, 6, 7):

```js
class Ship {
  constructor(name) { this.name = name; }
  describe() { return `${this.name} gemisi`; }
}
class Explorer extends Ship {
  constructor(name, planet) { super(name); this.planet = planet; }
  describe() { return `${super.describe()}, hedef: ${this.planet}`; }
}
const e = new Explorer("Kaşif", "Mars");
console.log(e.describe());
console.log(e instanceof Ship);
```

**Çıktı:**

```text
Kaşif gemisi, hedef: Mars
true
```

**Maskot:** isaret pozu, sag

## Sahne 5: anlatim (16 sn)

**Seslendirme:** Büyük projelerde her şeyi tek dosyaya yazmayız; kodu modüllere böleriz. Bir dosya export ile paylaşır, diğeri import ile alır. Her sınıf kendi dosyasında yaşayabilir.

**Ekranda başlık:** Modüller: kodu dosyalara bölmek

**Kod** (vurgulanan satırlar: 2, 6):

```js
// ship.js
export class Ship { /* ... */ }
export const MAX_SPEED = 20;

// main.js
import { Ship, MAX_SPEED } from "./ship.js";
const s = new Ship("Kartal");
```

**Maskot:** konusma pozu, sol

*Yönetmen notu: Kodun altında küçük not: HTML'de <script type="module" src="main.js"></script>. Kursun editöründe tek betik çalıştığı için görevlerde import yok.*

## Sahne 6: hata (14 sn)

**Seslendirme:** Sık hata: new yazmayı unutmak. Sınıf bir fonksiyon gibi çağrılamaz; JavaScript bunu hemen TypeError ile durdurur. Mesaj diyor ki: sınıf, new olmadan çağrılamaz.

**Ekranda başlık:** Sık hata: new'i unutmak

**Kod** (vurgulanan satırlar: 4):

```js
class Ship {
  constructor(name) { this.name = name; }
}
const s = Ship("Kartal");
```

**Çıktı:**

```text
TypeError: Class constructor Ship cannot be invoked without 'new'
```

**Maskot:** sasirma pozu, sag

## Sahne 7: soru (10 sn)

**Seslendirme:** Soru zamanı! Robotun pili 30 ve iki saat çalışıyor. Getter her okunuşta yeniden hesaplanıyor. Sence ne yazar?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```js
class Robot {
  constructor(battery) { this.battery = battery; }
  work(hours) { this.battery -= hours * 10; }
  get status() { return this.battery > 20 ? "hazır" : "şarj gerekli"; }
}
const bip = new Robot(30);
bip.work(2);
console.log(bip.battery, bip.status);
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (9 sn)

**Seslendirme:** Cevap: 10, şarj gerekli! İki saatte pil 20 azaldı ve 10'a düştü. status okununca yeniden hesaplandı.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 4, 8):

```js
class Robot {
  constructor(battery) { this.battery = battery; }
  work(hours) { this.battery -= hours * 10; }
  get status() { return this.battery > 20 ? "hazır" : "şarj gerekli"; }
}
const bip = new Robot(30);
bip.work(2);
console.log(bip.battery, bip.status);
```

**Çıktı:**

```text
10 şarj gerekli
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (13 sn)

**Seslendirme:** Görev zamanı! Uydularını anlatan bir gezegen sınıfı, yüzde kaç dolu olduğunu söyleyen bir yakıt deposu ve hazır bir gemi sınıfını genişleten bir kargo gemisi yazacaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Gezegen sınıfı
- Görev 2: Yakıt deposu
- Görev 3: Kargo gemisi

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (12 sn)

**Seslendirme:** Özetleyelim: class bir kalıptır, new ile örnek üretir, constructor ve this ile özellik ekler. Metotlar ve getter davranış katar. extends ve super ile genişletir, modüllerle dosyalara bölersin.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- class + constructor + this; new ile örnek
- Metot ve get ile getter
- extends + super  ·  export / import

**Maskot:** konusma pozu, sag

## Sahne 11: kapanis (12 sn)

**Seslendirme:** Gemi fabrikan hazır ve Async İstasyonu'nu tamamladın! Yarın JavaScript Yıldızı'na doğru yola çıkıyoruz. İlk durak: temiz kod. Görüşürüz!

**Ekranda başlık:** Yarın: Temiz kod

**Görsel:** `gorseller/javascript/bolgeler/yildiz.webp`

**Maskot:** tebrik pozu, orta
