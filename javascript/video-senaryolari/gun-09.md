# Video senaryosu: Gün 9, Ok fonksiyonları ve kapsam

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~143 sn

Fonksiyon Nebulası'nda ok fonksiyonlarını, değişkenlerin yaşadığı kapsamı, fonksiyonları değer gibi göndermeyi (callback) ve bir şeyleri hatırlayan fonksiyonları (closure) keşfediyoruz.

Ders metni: [gun-09.md](../gunler/gun-09.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 11 sn | el-sallama (sag) |
| 2 | kod | 16 sn | isaret (alt-sag) |
| 3 | kod | 13 sn | konusma (alt-sag) |
| 4 | hata | 17 sn | sasirma (sag) |
| 5 | kod | 16 sn | isaret (alt-sag) |
| 6 | kod | 18 sn | mutlu (alt-sag) |
| 7 | soru | 10 sn | dusunme (sag) |
| 8 | cikti | 9 sn | mutlu (sag) |
| 9 | gorev | 12 sn | isaret (sol) |
| 10 | ozet | 11 sn | on (sag) |
| 11 | kapanis | 10 sn | tebrik (sag) |

## Sahne 1: acilis (11 sn)

**Seslendirme:** Selam, ben Kodi! Fonksiyon Nebulası'na girdik. Bu renkli bulutta fonksiyonlar değişkenlere konuyor, başka fonksiyonlara gönderiliyor, hatta bir şeyleri hatırlıyor. Nasıl mı?

**Ekranda başlık:** Gün 9: Ok fonksiyonları ve kapsam

**Görsel:** `gorseller/javascript/bolgeler/nebula.webp`

**Maskot:** el-sallama pozu, sag

*Yönetmen notu: Roket renkli nebula bulutunun içine süzülür.*

## Sahne 2: kod (16 sn)

**Seslendirme:** Ok fonksiyonu, fonksiyon yazmanın kısa yolu. Fonksiyonu bir değişkene koyar, parametrelerden sonra ok işareti yazarız. Tek satırlık ok fonksiyonunda return yazılmaz; oktan sonraki değer kendiliğinden döner.

**Ekranda başlık:** Ok fonksiyonu: =>

**Kod** (vurgulanan satırlar: 1, 2, 3):

```js
const double = (n) => n * 2;
const greet = (name) => `Merhaba ${name}!`;
const isFull = (fuel) => fuel >= 100;

console.log(double(21));
console.log(greet("Ada"));
console.log(isFull(80));
```

**Çıktı:**

```text
42
Merhaba Ada!
false
```

**Maskot:** isaret pozu, alt-sag

## Sahne 3: kod (13 sn)

**Seslendirme:** Birden fazla satır gerekirse süslü parantez açarız. O zaman return'ü kendimiz yazmalıyız. Saniyedeki hızı saatliğe çevirdik.

**Ekranda başlık:** Çok satırlı ok fonksiyonu

**Kod** (vurgulanan satırlar: 1, 3):

```js
const describe = (name, speed) => {
  const kmh = speed * 3600;
  return `${name}: saatte ${kmh} km`;
};

console.log(describe("Kartal", 11));
```

**Çıktı:**

```text
Kartal: saatte 39600 km
```

**Maskot:** konusma pozu, alt-sag

## Sahne 4: hata (17 sn)

**Seslendirme:** Kapsam, değişkenin nerede yaşadığıdır. let ve const ile açılan değişken sadece kendi süslü parantez bloğunda yaşar. İçeriden dışarısı görünür, ama dışarıdan içerisi görünmez. Bu yüzden son satır hata verdi.

**Ekranda başlık:** Kapsam: değişken nerede yaşar?

**Kod** (vurgulanan satırlar: 3, 6):

```js
const ship = "Kartal";
if (true) {
  const note = "iç not";
  console.log(ship, note);
}
console.log(note);
```

**Çıktı:**

```text
Kartal iç not
ReferenceError: note is not defined
```

**Maskot:** sasirma pozu, sag

*Yönetmen notu: Blok bir kutu gibi çizilir; note kutunun içinde kalır, dışarıdan bakan ok kırmızıya döner.*

## Sahne 5: kod (16 sn)

**Seslendirme:** Fonksiyonlar da birer değerdir; başka bir fonksiyona gönderilebilir. Gönderilen fonksiyona callback denir. doTwice onu iki kez çağırdı. forEach de her eleman için callback'i çağırır.

**Ekranda başlık:** Fonksiyon da bir değerdir

**Kod** (vurgulanan satırlar: 5, 8):

```js
function doTwice(action) {
  action();
  action();
}
doTwice(() => console.log("Motor ateşlendi!"));

const planets = ["Mars", "Venüs"];
planets.forEach((planet) => console.log(planet));
```

**Çıktı:**

```text
Motor ateşlendi!
Motor ateşlendi!
Mars
Venüs
```

**Maskot:** isaret pozu, alt-sag

## Sahne 6: kod (18 sn)

**Seslendirme:** Şimdi sihirli kısım: closure! makeCounter içinde bir fonksiyon oluşturup döndürüyor. İçteki fonksiyon count değişkenini hatırlıyor. Her sayacın kendi count'u var: A iki oldu, B bir.

**Ekranda başlık:** Closure: hatırlayan fonksiyonlar

**Kod** (vurgulanan satırlar: 2, 3, 4):

```js
function makeCounter() {
  let count = 0;
  return () => {
    count++;
    return count;
  };
}
const counterA = makeCounter();
const counterB = makeCounter();
console.log(counterA(), counterA(), counterB());
```

**Çıktı:**

```text
1 2 1
```

**Maskot:** mutlu pozu, alt-sag

*Yönetmen notu: İki sayaç iki ayrı küçük kutu olarak gösterilir, her birinde kendi count'u.*

## Sahne 7: soru (10 sn)

**Seslendirme:** laps sayacını iki kez sessizce çağırıyoruz, üçüncüde yazdırıyoruz. Sence kaç yazar?

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```js
function makeCounter() {
  let count = 0;
  return () => {
    count++;
    return count;
  };
}
const laps = makeCounter();
laps();
laps();
console.log("Tur:", laps());
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (9 sn)

**Seslendirme:** Tur: 3! Yazdırmasak bile her çağrı count'u artırdı; fonksiyon sayıyı hatırladı.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 9, 10, 11):

```js
function makeCounter() {
  let count = 0;
  return () => {
    count++;
    return count;
  };
}
const laps = makeCounter();
laps();
laps();
console.log("Tur:", laps());
```

**Çıktı:**

```text
Tur: 3
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (12 sn)

**Seslendirme:** Görevlerin: iki fonksiyonu oka çevir, kapsam dedektifi olup gizli hatayı bul ve bir işi istediğin kadar tekrarlayan bir fonksiyon yaz.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Oka çevir
- Görev 2: Kapsam dedektifi
- Görev 3: Tekrarlayıcı

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (11 sn)

**Seslendirme:** Özet: ok fonksiyonu kısa yazımdır. Değişken kendi bloğunda yaşar. Fonksiyonlar gönderilebilir, closure ile değişkenleri hatırlar.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- (n) => n * 2: tek satırda return yok
- let/const bloğunda yaşar
- callback ve closure

**Maskot:** on pozu, sag

## Sahne 11: kapanis (10 sn)

**Seslendirme:** Nebulada harika bir gündü! Yarın bir uzay istasyonuna yanaşıyoruz. Geminin bütün bilgilerini tek pakette tutmayı öğreneceğiz: nesneler.

**Ekranda başlık:** Yarın: Nesneler

**Görsel:** `maskotlar/kodi-javascript/kahraman.png`

**Maskot:** tebrik pozu, sag
