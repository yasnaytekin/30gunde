# Video senaryosu: Gün 2, Değişkenler ve veri tipleri

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~142 sn

Roketin göstergelerini saklamak için let ve const ile değişken oluşturuyor, metin, sayı ve mantıksal değerleri typeof ile tanıyoruz.

Ders metni: [gun-02.md](../gunler/gun-02.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 10 sn | el-sallama (sag) |
| 2 | anlatim | 10 sn | konusma (sag) |
| 3 | kod | 14 sn | isaret (alt-sag) |
| 4 | anlatim | 12 sn | konusma (sol) |
| 5 | hata | 14 sn | sasirma (sag) |
| 6 | kod | 15 sn | isaret (alt-sag) |
| 7 | anlatim | 13 sn | konusma (sag) |
| 8 | soru | 10 sn | dusunme (sag) |
| 9 | cikti | 10 sn | mutlu (sag) |
| 10 | gorev | 13 sn | isaret (sol) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 10 sn | tebrik (sag) |

## Sahne 1: acilis (10 sn)

**Seslendirme:** Selam kaptan, ben Kodi! Roketin panelinde onlarca gösterge var: yakıt, hız, pilotun adı. Bu bilgilerin hepsini nerede saklayacağız dersin?

**Ekranda başlık:** Gün 2: Değişkenler ve veri tipleri

**Görsel:** `gorseller/javascript/bolgeler/kalkis.webp`

**Maskot:** el-sallama pozu, sag

*Yönetmen notu: Kontrol panelindeki göstergeler tek tek yanar.*

## Sahne 2: anlatim (10 sn)

**Seslendirme:** Cevap: değişkenlerde! Değişken, üstünde etiket olan bir kutu gibidir. Kutuyu let ile oluşturur, eşittir işaretiyle içine bir değer koyarsın.

**Ekranda başlık:** Değişken: etiketli bir kutu

**Ekranda maddeler:**

- let ile kutuyu oluştur
- = ile içine değer koy
- Adıyla istediğin zaman kullan

**Maskot:** konusma pozu, sag

## Sahne 3: kod (14 sn)

**Seslendirme:** fuel adında bir kutu açtık ve içine 100 koyduk. Üçüncü satırda değerini 80 yaptık. Dikkat et, değiştirirken başına tekrar let yazmıyoruz; let sadece ilk seferde.

**Ekranda başlık:** Kutu açmak ve değiştirmek

**Kod** (vurgulanan satırlar: 1, 3):

```js
let fuel = 100;
console.log(fuel);
fuel = 80;
console.log(fuel);
```

**Çıktı:**

```text
100
80
```

**Maskot:** isaret pozu, alt-sag

## Sahne 4: anlatim (12 sn)

**Seslendirme:** Değeri sonradan değişecek kutular için let kullan: yakıt, skor gibi. Hiç değişmeyecek olanlar için const: roketin adı gibi. Eski kodlarda var görebilirsin, artık kullanmıyoruz.

**Ekranda başlık:** let mi, const mı?

**Ekranda maddeler:**

- let: değişecek değerler (yakıt, skor)
- const: sabit değerler (roketin adı)
- var: eski yöntem, artık let ve const

**Maskot:** konusma pozu, sol

## Sahne 5: hata (14 sn)

**Seslendirme:** Bir const kutusunun değerini değiştirmeye çalışırsak ne olur? JavaScript itiraz eder: sabit bir değişkene atama yapılamaz. Değer değişecekse baştan let kullanmalıydık.

**Ekranda başlık:** const değiştirilemez

**Kod** (vurgulanan satırlar: 2):

```js
const shipName = "Kartal-1";
shipName = "Şahin";
```

**Çıktı:**

```text
TypeError: Assignment to constant variable.
```

**Maskot:** sasirma pozu, sag

## Sahne 6: kod (15 sn)

**Seslendirme:** Her değerin bir türü vardır. Metin string, sayı number, doğru ya da yanlış ise boolean. typeof bize türü söyler. Bak, tırnak içindeki 42 artık bir metin!

**Ekranda başlık:** Veri tipleri

**Kod** (vurgulanan satırlar: 2):

```js
console.log(typeof 42);
console.log(typeof "42");
console.log(typeof true);
```

**Çıktı:**

```text
number
string
boolean
```

**Maskot:** isaret pozu, alt-sag

*Yönetmen notu: Üç tür üç farklı renkli etiketle gösterilir.*

## Sahne 7: anlatim (13 sn)

**Seslendirme:** İsim verirken kurallar var. Rakamla başlayamaz, boşluk olmaz. Birden fazla kelimeyi camelCase yazarız. Büyük küçük harf de fark eder: fuel ile Fuel ayrı kutulardır.

**Ekranda başlık:** İsim verme kuralları

**Ekranda maddeler:**

- ship2 olur, 2ship olmaz
- camelCase: pilotName, fuelLevel
- fuel ve Fuel iki ayrı değişken

**Maskot:** konusma pozu, sag

## Sahne 8: soru (10 sn)

**Seslendirme:** Roket kartımızı hazırladık. fuel eksi 20 satırına dikkat et. Sence son satır ne yazdırır? Durdur ve düşün.

**Ekranda başlık:** Sence ne yazdırır?

**Kod** (vurgulanan satırlar: 3):

```js
const shipName = "Kartal-1";
let fuel = 100;
fuel = fuel - 20;
console.log(shipName, "yakıt:", fuel);
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (10 sn)

**Seslendirme:** Kartal-1 yakıt: 80! Üçüncü satır eski değerden 20 çıkardı ve sonucu yine fuel kutusuna koydu.

**Ekranda başlık:** Cevap

**Kod**:

```js
const shipName = "Kartal-1";
let fuel = 100;
fuel = fuel - 20;
console.log(shipName, "yakıt:", fuel);
```

**Çıktı:**

```text
Kartal-1 yakıt: 80
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görev zamanı! Kendi pilot kartını oluştur, kalkışta harcanan yakıtı hesaplat ve tür dedektifi olup üç değişkenin türünü bul.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Pilot kartı
- Görev 2: Yakıt harcaması
- Görev 3: Tür dedektifi

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (11 sn)

**Seslendirme:** Özetleyelim: değişken etiketli bir kutudur. Değişecekse let, değişmeyecekse const. Üç temel tür var: metin, sayı ve mantıksal değer.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- Değişken = etiketli kutu
- let değişir, const değişmez
- string, number, boolean ve typeof

**Maskot:** on pozu, sag

## Sahne 12: kapanis (10 sn)

**Seslendirme:** Harika iş kaptan! Yarın roketin hesaplarını yapacağız: Ay'a kaç saatte varırız, yakıt yeter mi? Operatörler ve Math geliyor.

**Ekranda başlık:** Yarın: Operatörler ve Math

**Görsel:** `maskotlar/kodi-javascript/kahraman.png`

**Maskot:** tebrik pozu, sag
