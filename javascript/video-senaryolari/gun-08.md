# Video senaryosu: Gün 8, Fonksiyonlar

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~138 sn

Döngü Ayı'ndan ayrılmadan komutları fonksiyonlara paketliyoruz: tanımlamak ve çağırmak, parametreler, return ile sonuç döndürmek ve varsayılan parametre.

Ders metni: [gun-08.md](../gunler/gun-08.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 11 sn | el-sallama (sag) |
| 2 | kod | 15 sn | isaret (alt-sag) |
| 3 | kod | 14 sn | konusma (alt-sag) |
| 4 | kod | 16 sn | isaret (alt-sag) |
| 5 | kod | 14 sn | konusma (alt-sag) |
| 6 | hata | 15 sn | uzgun (sag) |
| 7 | soru | 10 sn | dusunme (sag) |
| 8 | cikti | 9 sn | mutlu (sag) |
| 9 | gorev | 12 sn | isaret (sol) |
| 10 | ozet | 11 sn | on (sag) |
| 11 | kapanis | 11 sn | tebrik (sag) |

## Sahne 1: acilis (11 sn)

**Seslendirme:** Selam, ben Kodi! Döngü Ayı'ndaki son günümüz. Ayrılmadan önce roketine yeni bir yetenek kazandırıyoruz: komutları bir ad altında paketleyip istediğin kadar çağırmak.

**Ekranda başlık:** Gün 8: Fonksiyonlar

**Görsel:** `gorseller/javascript/bolgeler/ay.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (15 sn)

**Seslendirme:** function kelimesiyle bir fonksiyon tanımlarız. Ama tanımlamak onu çalıştırmaz! Adını parantezle yazıp çağırınca çalışır. İki kez çağırdık, iki kez geri sayım yaptı.

**Ekranda başlık:** Tanımlamak ve çağırmak

**Kod** (vurgulanan satırlar: 1, 6, 7):

```js
function countdown() {
  console.log("3... 2... 1...");
  console.log("Ateşle!");
}

countdown();
countdown();
```

**Çıktı:**

```text
3... 2... 1...
Ateşle!
3... 2... 1...
Ateşle!
```

**Maskot:** isaret pozu, alt-sag

## Sahne 3: kod (14 sn)

**Seslendirme:** Parantezin içine parametre yazarsak fonksiyon her seferinde farklı değerle çalışır. Çağırırken verdiğimiz değerler sırayla name ve planet'e yerleşir.

**Ekranda başlık:** Parametreler

**Kod** (vurgulanan satırlar: 1, 5):

```js
function greet(name, planet) {
  console.log(`Merhaba ${name}, ${planet}'a hoş geldin!`);
}

greet("Deniz", "Mars");
greet("Ada", "Ay");
```

**Çıktı:**

```text
Merhaba Deniz, Mars'a hoş geldin!
Merhaba Ada, Ay'a hoş geldin!
```

**Maskot:** konusma pozu, alt-sag

## Sahne 4: kod (16 sn)

**Seslendirme:** return, sonucu çağrıldığı yere geri verir. Sonucu bir değişkene koyup başka hesapta kullanabiliriz. return çalışınca fonksiyon hemen biter, altındaki satırlar çalışmaz.

**Ekranda başlık:** return: sonucu geri vermek

**Kod** (vurgulanan satırlar: 2, 5):

```js
function travelTime(distance, speed) {
  return distance / speed;
}

const hours = travelTime(384400, 40000);
console.log(Math.round(hours));
```

**Çıktı:**

```text
10
```

**Maskot:** isaret pozu, alt-sag

## Sahne 5: kod (14 sn)

**Seslendirme:** Bir parametre verilmezse kullanılacak değeri eşittirle yazabiliriz. Kartal'a yakıt vermedik, varsayılan yüz kullanıldı. Şahin'e ise altmış verdik.

**Ekranda başlık:** Varsayılan parametre

**Kod** (vurgulanan satırlar: 1):

```js
function launch(ship, fuel = 100) {
  return `${ship} ${fuel} litre yakıtla kalkıyor.`;
}

console.log(launch("Kartal"));
console.log(launch("Şahin", 60));
```

**Çıktı:**

```text
Kartal 100 litre yakıtla kalkıyor.
Şahin 60 litre yakıtla kalkıyor.
```

**Maskot:** konusma pozu, alt-sag

## Sahne 6: hata (15 sn)

**Seslendirme:** Çok sık yapılan hata: return yerine console.log yazmak. Fonksiyon ekrana 10 yazdı ama sonucu geri vermedi. Bu yüzden result undefined oldu. Sonuç lazımsa return kullan!

**Ekranda başlık:** console.log, return değildir

**Kod** (vurgulanan satırlar: 2, 6):

```js
function double(n) {
  console.log(n * 2);
}

const result = double(5);
console.log("Sonuç:", result);
```

**Çıktı:**

```text
10
Sonuç: undefined
```

**Maskot:** uzgun pozu, sag

## Sahne 7: soru (10 sn)

**Seslendirme:** welcome fonksiyonunu iki kez çağırıyoruz, ikincisinde hiç ad vermeden. Sence ikinci satırda ne yazar?

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```js
function welcome(name = "Kaptan") {
  return `Hoş geldin, ${name}!`;
}

console.log(welcome("Deniz"));
console.log(welcome());
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (9 sn)

**Seslendirme:** İkinci çağrıda ad verilmediği için varsayılan değer, yani Kaptan kullanıldı. Hoş geldin, Kaptan!

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 6):

```js
function welcome(name = "Kaptan") {
  return `Hoş geldin, ${name}!`;
}

console.log(welcome("Deniz"));
console.log(welcome());
```

**Çıktı:**

```text
Hoş geldin, Deniz!
Hoş geldin, Kaptan!
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (12 sn)

**Seslendirme:** Görevlerin: güneş panelinin alanını döndüren bir fonksiyon yaz, yakıt durumunu metinle anlatan bir gösterge yap ve varsayılan geri sayımlı bir kalkış mesajı hazırla.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Alan hesaplayıcı
- Görev 2: Yakıt göstergesi
- Görev 3: Kalkış mesajı

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (11 sn)

**Seslendirme:** Özet: fonksiyonu tanımla, sonra çağır. Parametrelerle farklı değerler ver, return ile sonucu geri al. İyi bir fonksiyon tek bir iş yapar.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- function ad() { ... } ve ad() ile çağır
- Parametreler ve varsayılan değerler
- return sonucu geri verir, fonksiyonu bitirir

**Maskot:** on pozu, sag

## Sahne 11: kapanis (11 sn)

**Seslendirme:** Döngü Ayı'nı tamamladın, bravo! Yarın Fonksiyon Nebulası'na dalıyoruz. Ok fonksiyonlarını ve bir şeyleri hatırlayan fonksiyonları keşfedeceğiz.

**Ekranda başlık:** Yarın: Ok fonksiyonları ve kapsam

**Görsel:** `gorseller/javascript/bolgeler/nebula.webp`

**Maskot:** tebrik pozu, sag

*Yönetmen notu: Roket Ay'dan uzaklaşır, renkli nebula görünür.*
