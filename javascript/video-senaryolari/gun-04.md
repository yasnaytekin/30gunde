# Video senaryosu: Gün 4, Metinlerle çalışmak

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~148 sn

Roketin istasyonlarla mesajlaşması için şablon metinleri, metnin uzunluğunu ve harflerini, metin metotlarını ve Türkçe harflerle büyük-küçük dönüşümü öğreniyoruz.

Ders metni: [gun-04.md](../gunler/gun-04.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 10 sn | el-sallama (sag) |
| 2 | kod | 16 sn | isaret (alt-sag) |
| 3 | kod | 12 sn | isaret (alt-sag) |
| 4 | kod | 16 sn | konusma (alt-sag) |
| 5 | kod | 14 sn | isaret (alt-sag) |
| 6 | kod | 13 sn | konusma (alt-sag) |
| 7 | hata | 14 sn | uzgun (sag) |
| 8 | soru | 10 sn | dusunme (sag) |
| 9 | cikti | 10 sn | mutlu (sag) |
| 10 | gorev | 12 sn | isaret (sol) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 10 sn | tebrik (sag) |

## Sahne 1: acilis (10 sn)

**Seslendirme:** Selam, ben Kodi! Kalkış Üssü'ndeki son günümüz. Roket uzaydaki istasyonlarla mesajlaşacak. Mesajları nasıl birleştirir, büyütür, içinde kelime ararız?

**Ekranda başlık:** Gün 4: Metinlerle çalışmak

**Görsel:** `gorseller/javascript/bolgeler/kalkis.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (16 sn)

**Seslendirme:** Şablon metin, tırnak yerine ters tırnakla yazılır. Değişkenleri dolar ve süslü parantez içine koyarsın, yerine değeri gelir. İçine işlem bile yazabilirsin: üç artı dört, yedi oldu.

**Ekranda başlık:** Şablon metin: ters tırnak ve ${ }

**Kod** (vurgulanan satırlar: 3, 4):

```js
const pilot = "Deniz";
const planet = "Mars";
console.log(`Merhaba ${pilot}, hedef: ${planet}!`);
console.log(`Toplam: ${3 + 4}`);
```

**Çıktı:**

```text
Merhaba Deniz, hedef: Mars!
Toplam: 7
```

**Maskot:** isaret pozu, alt-sag

*Yönetmen notu: Ters tırnak karakteri büyütülüp klavyedeki yeri gösterilir.*

## Sahne 3: kod (12 sn)

**Seslendirme:** length metnin kaç karakter olduğunu söyler. Köşeli parantezle tek bir harfe ulaşırsın. Dikkat: sayma sıfırdan başlar, yani ilk harf sıfırıncı!

**Ekranda başlık:** Uzunluk ve harfler

**Kod** (vurgulanan satırlar: 2, 3):

```js
const word = "roket";
console.log(word.length);
console.log(word[0]);
```

**Çıktı:**

```text
5
r
```

**Maskot:** isaret pozu, alt-sag

## Sahne 4: kod (16 sn)

**Seslendirme:** Metinlerin hazır metotları var. trim baştaki ve sondaki boşlukları siler, toUpperCase büyük harfe çevirir, includes içinde bir kelime var mı diye bakar. Temizlenen mesaj 18 karakter.

**Ekranda başlık:** Metin metotları

**Kod** (vurgulanan satırlar: 2, 3, 4):

```js
const message = "  Acil: Yakıt Azaldı  ";
const clean = message.trim();
console.log(clean.toUpperCase());
console.log(clean.includes("Yakıt"));
console.log(clean.length);
```

**Çıktı:**

```text
ACIL: YAKIT AZALDI
true
18
```

**Maskot:** konusma pozu, alt-sag

## Sahne 5: kod (14 sn)

**Seslendirme:** slice bir metinden parça keser: sıfırdan üçe kadar, yani ilk üç harf. replace bir kelimeyi başkasıyla değiştirir. Metotlar asıl metni bozmaz, hep yeni bir metin verir.

**Ekranda başlık:** slice ve replace

**Kod** (vurgulanan satırlar: 2, 3):

```js
const star = "yıldız";
console.log(star.slice(0, 3));
console.log("Hedef: Ay".replace("Ay", "Mars"));
```

**Çıktı:**

```text
yıl
Hedef: Mars
```

**Maskot:** isaret pozu, alt-sag

## Sahne 6: kod (13 sn)

**Seslendirme:** Türkçe için bir ipucu! toUpperCase noktasız I yazar. Türkçe kurallarıyla çevirmek için toLocaleUpperCase'e tr ver. Artık İstanbul noktalı İ ile yazılıyor.

**Ekranda başlık:** Türkçe harfler

**Kod** (vurgulanan satırlar: 2):

```js
console.log("istanbul".toUpperCase());
console.log("istanbul".toLocaleUpperCase("tr"));
console.log("IŞIK".toLocaleLowerCase("tr"));
```

**Çıktı:**

```text
ISTANBUL
İSTANBUL
ışık
```

**Maskot:** konusma pozu, alt-sag

## Sahne 7: hata (14 sn)

**Seslendirme:** En sık hata: şablon metni normal tırnakla yazmak. Hata mesajı çıkmaz ama değişkenin adı olduğu gibi ekrana düşer. Dolar süslü parantez sadece ters tırnak içinde çalışır.

**Ekranda başlık:** Tırnak mı, ters tırnak mı?

**Kod** (vurgulanan satırlar: 2):

```js
const pilot = "Deniz";
console.log("Merhaba ${pilot}");
```

**Çıktı:**

```text
Merhaba ${pilot}
```

**Maskot:** uzgun pozu, sag

## Sahne 8: soru (10 sn)

**Seslendirme:** Şimdi sen söyle: bu kod iki satır yazdırıyor. İkinci satırdaki sayı kaç olur? Boşluklara dikkat!

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```js
const code = "  mars  ";
console.log(code.trim().toUpperCase());
console.log(code.length);
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (10 sn)

**Seslendirme:** Önce temiz ve büyük harfli MARS. Sonra 8, çünkü trim asıl metni değiştirmedi; boşluklar hâlâ orada ve onlar da sayılır.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 3):

```js
const code = "  mars  ";
console.log(code.trim().toUpperCase());
console.log(code.length);
```

**Çıktı:**

```text
MARS
8
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (12 sn)

**Seslendirme:** Görevlerin: şablon metinle bir karşılama mesajı yaz, gemi için bir çağrı kodu üret ve gelen mesajı tarayıp acil olup olmadığını bul.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Karşılama mesajı
- Görev 2: Çağrı kodu
- Görev 3: Mesaj tarayıcı

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (11 sn)

**Seslendirme:** Bugün ters tırnakla şablon metin yazmayı, length ve indeksle harflere ulaşmayı ve metin metotlarını öğrendik.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- `...${değişken}...` ile şablon metin
- length ve text[0]: sayma 0'dan başlar
- trim, toUpperCase, includes, slice, replace

**Maskot:** on pozu, sag

## Sahne 12: kapanis (10 sn)

**Seslendirme:** Kalkış Üssü tamamlandı, roket havalanıyor! Yarın Döngü Ayı'na iniyoruz ve programımız kendi kararlarını vermeyi öğreniyor: koşullar.

**Ekranda başlık:** Yarın: Koşullar

**Görsel:** `gorseller/javascript/bolgeler/ay.webp`

**Maskot:** tebrik pozu, sag

*Yönetmen notu: Roket kalkar, kamera Döngü Ayı görseline geçer.*
