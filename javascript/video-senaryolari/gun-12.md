# Video senaryosu: Gün 12, Set, Map ve JSON

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~168 sn

Nebulanın ucundaki istasyonda Set ile tekrarları ayıklıyor, Map ile anahtar-değer tutuyor, spread ile kopyalıyor ve veriyi JSON'a çevirip geri alıyoruz.

Ders metni: [gun-12.md](../gunler/gun-12.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 11 sn | el-sallama (sag) |
| 2 | kod | 15 sn | isaret (alt-sag) |
| 3 | kod | 12 sn | mutlu (alt-sag) |
| 4 | kod | 17 sn | konusma (alt-sag) |
| 5 | anlatim | 10 sn | dusunme (sag) |
| 6 | kod | 16 sn | isaret (alt-sag) |
| 7 | kod | 17 sn | konusma (alt-sag) |
| 8 | hata | 14 sn | sasirma (sag) |
| 9 | soru | 11 sn | dusunme (sag) |
| 10 | cikti | 11 sn | mutlu (sag) |
| 11 | gorev | 12 sn | isaret (sol) |
| 12 | ozet | 11 sn | on (sag) |
| 13 | kapanis | 11 sn | tebrik (sag) |

## Sahne 1: acilis (11 sn)

**Seslendirme:** Selam, ben Kodi! Nebulanın ucundaki istasyona kenetlendik. İstasyon bilgisayarı başka gemilerle ortak bir dil konuşuyor: JSON. Bugün iki yeni kutu da tanıyacağız: Set ve Map.

**Ekranda başlık:** Gün 12: Set, Map ve JSON

**Görsel:** `gorseller/javascript/bolgeler/nebula.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (15 sn)

**Seslendirme:** Set her değeri yalnızca bir kez tutar. Mars'ı ikinci kez eklemeye çalıştık ama görmezden geldi, bu yüzden boyut iki. has ile bir değer var mı diye sorarız.

**Ekranda başlık:** Set: tekrarsız kutu

**Kod** (vurgulanan satırlar: 4, 5):

```js
const visited = new Set();
visited.add("Mars");
visited.add("Venüs");
visited.add("Mars");
console.log(visited.size);
console.log(visited.has("Mars"));
```

**Çıktı:**

```text
2
true
```

**Maskot:** isaret pozu, alt-sag

## Sahne 3: kod (12 sn)

**Seslendirme:** Set'in en sevilen işi: bir diziden tekrarları atmak. new Set tekrarları siler, üç nokta da onu yeniden diziye çevirir.

**Ekranda başlık:** Tekrarları atmak

**Kod** (vurgulanan satırlar: 2):

```js
const logs = ["Mars", "Ay", "Mars", "Ay", "Venüs"];
const unique = [...new Set(logs)];
console.log(unique);
```

**Çıktı:**

```text
[ 'Mars', 'Ay', 'Venüs' ]
```

**Maskot:** mutlu pozu, alt-sag

## Sahne 4: kod (17 sn)

**Seslendirme:** Map de anahtar ve değer tutar ama kendi metotlarıyla: set ekler, get okur. Aynı anahtara yeniden set yaparsak değer güncellenir. for of ile her çifti anahtar ve değer olarak açarız.

**Ekranda başlık:** Map: anahtar → değer

**Kod** (vurgulanan satırlar: 2, 4, 6):

```js
const cargo = new Map();
cargo.set("su", 40);
cargo.set("yakıt", 25);
cargo.set("su", 35);
console.log(cargo.get("su"), cargo.size);
for (const [item, amount] of cargo) {
  console.log(item, amount);
}
```

**Çıktı:**

```text
35 2
su 35
yakıt 25
```

**Maskot:** konusma pozu, alt-sag

## Sahne 5: anlatim (10 sn)

**Seslendirme:** Hangisini ne zaman kullanalım? Alanları belli şeyler için nesne. Sürekli eklenip silinen, sayılan şeyler için Map daha rahat.

**Ekranda başlık:** Nesne mi, Map mi?

**Ekranda maddeler:**

- Nesne: oyuncu, gemi gibi alanları belli şeyler
- Map: envanter adetleri, kelime sayacı

**Maskot:** dusunme pozu, sag

## Sahne 6: kod (16 sn)

**Seslendirme:** Üç nokta, yani spread, bir diziyi ya da nesneyi açıp içindekileri döker. Böylece kopya çıkarır, üstüne ekleriz. full'da yakıtın üzerine yüz yazıldı, ship ise değişmedi.

**Ekranda başlık:** Spread (...): aç ve kopyala

**Kod** (vurgulanan satırlar: 2, 5):

```js
const crew = ["Ada", "Can"];
const bigger = [...crew, "Ece"];
console.log(bigger);
const ship = { name: "Kartal", fuel: 50 };
const full = { ...ship, fuel: 100 };
console.log(ship.fuel, full.fuel);
```

**Çıktı:**

```text
[ 'Ada', 'Can', 'Ece' ]
50 100
```

**Maskot:** isaret pozu, alt-sag

## Sahne 7: kod (17 sn)

**Seslendirme:** JSON, veriyi metne çevirmenin standart yolu. stringify nesneyi metne çevirir, bak türü artık string. parse ise metni yeniden nesneye çevirir. Anahtarlar hep çift tırnaklı.

**Ekranda başlık:** JSON: verinin ortak dili

**Kod** (vurgulanan satırlar: 2, 5):

```js
const player = { name: "Ada", level: 3, items: ["kalkan", "lazer"] };
const text = JSON.stringify(player);
console.log(text);
console.log(typeof text);
const back = JSON.parse(text);
console.log(back.items[1]);
```

**Çıktı:**

```text
{"name":"Ada","level":3,"items":["kalkan","lazer"]}
string
lazer
```

**Maskot:** konusma pozu, alt-sag

*Yönetmen notu: Nesne bir paket gibi sıkıştırılıp metin şeridine dönüşür, sonra geri açılır.*

## Sahne 8: hata (14 sn)

**Seslendirme:** Bozuk bir metni parse etmeye çalışırsak SyntaxError alırız. Burada anahtar çift tırnaksız yazılmış; JSON bunu kabul etmez. Mesaj, sorunun hangi konumda olduğunu da söylüyor.

**Ekranda başlık:** Bozuk JSON

**Kod** (vurgulanan satırlar: 1):

```js
const data = JSON.parse("{name: 'Ada'}");
```

**Çıktı:**

```text
SyntaxError: Expected property name or '}' in JSON at position 1
```

**Maskot:** sasirma pozu, sag

## Sahne 9: soru (11 sn)

**Seslendirme:** b'yi eşittirle, c'yi spread ile oluşturduk. Sonra b'ye Venüs ekledik. Sence a ile c'nin uzunluğu kaç?

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```js
const a = ["Mars", "Ay"];
const b = a;
const c = [...a];
b.push("Venüs");
console.log(a.length, c.length);
```

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (11 sn)

**Seslendirme:** Üç ve iki! b yeni bir dizi değil, a ile aynı diziyi gösteriyor; b değişince a da değişti. c ise gerçek bir kopya.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 2, 3):

```js
const a = ["Mars", "Ay"];
const b = a;
const c = [...a];
b.push("Venüs");
console.log(a.length, c.length);
```

**Çıktı:**

```text
3 2
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (12 sn)

**Seslendirme:** Görevlerin: seyir defterindeki tekrarlı yıldızları ayıkla, kargo haritasını güncelleyip topla ve seyir defterini JSON'a çevirip geri al.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Tekrarsız yıldızlar
- Görev 2: Kargo haritası
- Görev 3: Seyir defteri

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (11 sn)

**Seslendirme:** Özet: Set tekrarsız tutar, Map anahtar ve değer tutar. Spread kopyalar. JSON veriyi metne çevirir ve geri alır.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- Set: add, has, size; [...new Set(dizi)]
- Map: set, get, has, size
- Spread ile kopya; JSON.stringify ve JSON.parse

**Maskot:** on pozu, sag

## Sahne 13: kapanis (11 sn)

**Seslendirme:** Fonksiyon Nebulası tamamlandı, harikasın! Yarın DOM Gezegeni'ne iniyoruz. Kodumuz artık web sayfasındaki yazıları ve renkleri değiştirecek.

**Ekranda başlık:** Yarın: DOM'a giriş

**Görsel:** `gorseller/javascript/bolgeler/dom.webp`

**Maskot:** tebrik pozu, sag

*Yönetmen notu: Roket nebuladan çıkar, DOM Gezegeni ekranı doldurur.*
