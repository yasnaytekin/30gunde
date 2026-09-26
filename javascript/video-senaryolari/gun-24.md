# Video senaryosu: Gün 24, Hatalar ve hata ayıklama

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~167 sn

Kodi, Async İstasyonu'nda hata mesajlarını okumayı, hata türlerini, try/catch/finally ile hataları yakalamayı, throw ile kendi hatanı fırlatmayı ve adım adım hata ayıklamayı anlatıyor.

Ders metni: [gun-24.md](../gunler/gun-24.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | el-sallama (sag) |
| 2 | hata | 15 sn | sasirma (sag) |
| 3 | anlatim | 16 sn | konusma (sol) |
| 4 | kod | 18 sn | isaret (sag) |
| 5 | kod | 15 sn | konusma (sol) |
| 6 | kod | 18 sn | isaret (sag) |
| 7 | anlatim | 17 sn | dusunme (sol) |
| 8 | soru | 10 sn | dusunme (sag) |
| 9 | cikti | 10 sn | mutlu (sag) |
| 10 | gorev | 13 sn | isaret (sol) |
| 11 | ozet | 12 sn | konusma (sag) |
| 12 | kapanis | 11 sn | el-sallama (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Kodi! Async İstasyonu'na kenetlendik. İstasyonun bilgisayarı arada bir kırmızı alarm veriyor. Panik yok! Bugün hata mesajlarını okumayı ve hataları yakalamayı öğreniyoruz.

**Ekranda başlık:** Gün 24: Hatalar ve hata ayıklama

**Görsel:** `gorseller/javascript/bolgeler/istasyon.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: hata (15 sn)

**Seslendirme:** İşte kırmızı bir alarm. Her hata mesajının üç parçası var: tür, açıklama ve satır numarası. Burada tür ReferenceError, açıklama ise consle tanımlı değil diyor. Yani bir yazım hatası!

**Ekranda başlık:** Hata mesajını oku

**Kod** (vurgulanan satırlar: 2):

```js
const fuel = 50;
consle.log(fuel);
```

**Çıktı:**

```text
ReferenceError: consle is not defined   (2. satır)
```

**Maskot:** sasirma pozu, sag

*Yönetmen notu: Hata mesajının üç parçası ayrı renklerle çerçevelenir: tür, açıklama, satır.*

## Sahne 3: anlatim (16 sn)

**Seslendirme:** En sık göreceğin türler şunlar. ReferenceError: böyle bir isim yok. TypeError: değer bu işe uygun değil. SyntaxError: kod kurallara uymuyor. RangeError: sayı izin verilen aralıkta değil.

**Ekranda başlık:** Hata türleri

**Ekranda maddeler:**

- ReferenceError: consle.log(1)
- TypeError: undefined.length, 5()
- SyntaxError: if (x > 1 {  ·  JSON.parse("{")
- RangeError: new Array(-1)

**Maskot:** konusma pozu, sol

## Sahne 4: kod (18 sn)

**Seslendirme:** Hata çıkabilecek kodu try bloğuna koyarsan program çökmez, hemen catch'e atlar. error nesnesinin name ve message özellikleri var. finally ise hata olsa da olmasa da çalışır.

**Ekranda başlık:** try, catch, finally

**Kod** (vurgulanan satırlar: 2, 5, 7):

```js
try {
  const data = JSON.parse("{bozuk"); // burada hata çıkar
  console.log("Bu satır çalışmaz");
} catch (error) {
  console.log("Yakalandı:", error.name);
} finally {
  console.log("Bu her durumda çalışır");
}
console.log("Program devam ediyor!");
```

**Çıktı:**

```text
Yakalandı: SyntaxError
Bu her durumda çalışır
Program devam ediyor!
```

**Maskot:** isaret pozu, sag

## Sahne 5: kod (15 sn)

**Seslendirme:** Bozuk bir kayıt bütün oyunu durdurmamalı. Her kaydı ayrı ayrı try içinde okuyoruz. Bozuk olan yakalanıyor, döngü sıradakiyle devam ediyor.

**Ekranda başlık:** Örnek: bozuk kayıtlar

**Kod** (vurgulanan satırlar: 3, 5):

```js
const saves = ['{"skor": 12}', "{bozuk kayıt", '{"skor": 30}'];
for (const text of saves) {
  try {
    console.log("Skor:", JSON.parse(text).skor);
  } catch (error) {
    console.log("Okunamadı:", error.name);
  }
}
```

**Çıktı:**

```text
Skor: 12
Okunamadı: SyntaxError
Skor: 30
```

**Maskot:** konusma pozu, sol

## Sahne 6: kod (18 sn)

**Seslendirme:** Bir fonksiyon hatalı veri alırsa sessizce yanlış sonuç vermek yerine açık bir mesajla durmalı. throw fonksiyonu anında durdurur ve hatayı çağıran koda gönderir. Oradaki catch onu yakalar.

**Ekranda başlık:** throw: kendi hatanı fırlat

**Kod** (vurgulanan satırlar: 3, 8, 10):

```js
function setCrew(count) {
  if (count < 1 || count > 6) {
    throw new Error("Ekip 1 ile 6 kişi arasında olmalı");
  }
  return count;
}
try {
  setCrew(9);
} catch (error) {
  console.log("Hata:", error.message);
}
```

**Çıktı:**

```text
Hata: Ekip 1 ile 6 kişi arasında olmalı
```

**Maskot:** isaret pozu, sag

## Sahne 7: anlatim (17 sn)

**Seslendirme:** Programcılar hatayı tahminle değil, adım adım bulur. Mesajı oku, şüphelendiğin değeri console.log ile yazdır, sorunu küçült ve her seferinde tek bir şey değiştirip yeniden çalıştır.

**Ekranda başlık:** Hata ayıklama stratejisi

**Ekranda maddeler:**

- 1. Mesajı oku: tür, açıklama, satır
- 2. Değerlere bak: console.log, console.table
- 3. Sorunu küçült
- 4. Tek şey değiştir, tekrar çalıştır

**Maskot:** dusunme pozu, sol

## Sahne 8: soru (10 sn)

**Seslendirme:** Soru zamanı! try içinde ikinci satır hata veriyor. Sence konsolda hangi harfler, hangi sırayla görünür?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```js
try {
  console.log("A");
  null.length;
  console.log("B");
} catch (error) {
  console.log("C");
} finally {
  console.log("D");
}
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (10 sn)

**Seslendirme:** Cevap A, C, D! null'ın uzunluğu olmadığı için TypeError çıktı ve B atlandı. catch C'yi yazdı, finally de her zamanki gibi D'yi.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 3):

```js
try {
  console.log("A");
  null.length;
  console.log("B");
} catch (error) {
  console.log("C");
} finally {
  console.log("D");
}
```

**Çıktı:**

```text
A
C
D
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görev zamanı! Bozuk metinde çökmeyen bir okuma fonksiyonu, hatalı yakıtta hata fırlatan bir doğrulama ve finally ile her durumda kapanan bir kalkış paneli yazacaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Güvenli okuma
- Görev 2: Yakıt doğrulama
- Görev 3: finally ile kapanış

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (12 sn)

**Seslendirme:** Özetleyelim: hata mesajında tür, açıklama ve satır var. Beklediğin hataları try ve catch ile yakala, temizliği finally'ye koy. Hatalı veride throw ile açıkça dur.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- Tür + açıklama + satır numarası
- try / catch (error) / finally
- throw new Error("...") ile açık mesaj

**Maskot:** konusma pozu, sag

## Sahne 12: kapanis (11 sn)

**Seslendirme:** Artık alarmlardan korkmuyorsun! İstasyonda hiçbir iş anında bitmiyor. Yarın JavaScript'e beklemeyi öğreteceğiz: Promise ve async await. Görüşürüz!

**Ekranda başlık:** Yarın: Promise ve async/await

**Görsel:** `gorseller/javascript/arka-plan/bg-space-wide.webp`

**Maskot:** el-sallama pozu, orta
