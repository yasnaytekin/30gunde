# Video senaryosu: Gün 1, JavaScript ile tanışma

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~129 sn

Kodi, Kalkış Üssü'nde roketine ilk mesajı gönderiyor: console.log ile ekrana yazdırmayı, yorum yazmayı ve hata mesajını okumayı öğreniyoruz.

Ders metni: [gun-01.md](../gunler/gun-01.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 10 sn | el-sallama (sag) |
| 2 | anlatim | 12 sn | konusma (sag) |
| 3 | kod | 14 sn | isaret (alt-sag) |
| 4 | kod | 14 sn | konusma (alt-sag) |
| 5 | kod | 13 sn | isaret (alt-sag) |
| 6 | hata | 15 sn | sasirma (sag) |
| 7 | soru | 9 sn | dusunme (sag) |
| 8 | cikti | 8 sn | mutlu (sag) |
| 9 | gorev | 13 sn | isaret (sol) |
| 10 | ozet | 11 sn | on (sag) |
| 11 | kapanis | 10 sn | tebrik (sag) |

## Sahne 1: acilis (10 sn)

**Seslendirme:** Selam, ben Kodi! Kalkış Üssü'ne hoş geldin kaptan. Roketimiz pistte, kontrol paneli senin komutunu bekliyor. Peki roketle hangi dilde konuşacağız?

**Ekranda başlık:** Gün 1: JavaScript ile tanışma

**Görsel:** `gorseller/javascript/bolgeler/kalkis.webp`

**Maskot:** el-sallama pozu, sag

*Yönetmen notu: Kalkış Üssü görseli yavaşça yakınlaşır, pistteki roketin ışıkları yanıp söner.*

## Sahne 2: anlatim (12 sn)

**Seslendirme:** Cevap JavaScript! Web sayfalarını canlandıran dil bu. Açılan menüler, oyundaki skor, haritadaki konum... Üstelik tarayıcının içinde çalışır, hiçbir şey kurman gerekmez.

**Ekranda başlık:** JavaScript nedir?

**Ekranda maddeler:**

- Web sayfalarını canlandıran programlama dili
- Menüler, oyunlar, haritalar
- Tarayıcıda çalışır: kurulum yok

**Maskot:** konusma pozu, sag

## Sahne 3: kod (14 sn)

**Seslendirme:** İlk komutumuz console.log. Parantezin içine ne yazarsan Çıktı alanına onu yazar. Metinler tırnak içinde, sayılar tırnaksız. Üçüncü satırda işlemi de kendisi hesaplıyor.

**Ekranda başlık:** console.log ile konuşmak

**Kod** (vurgulanan satırlar: 1, 3):

```js
console.log("Merhaba, dünya!");
console.log(42);
console.log(3 + 4);
```

**Çıktı:**

```text
Merhaba, dünya!
42
7
```

**Maskot:** isaret pozu, alt-sag

*Yönetmen notu: Satır sonundaki noktalı virgül kısa bir parıltıyla vurgulanır: komutun bittiğini gösterir.*

## Sahne 4: kod (14 sn)

**Seslendirme:** Şimdi dikkat! Tırnaksız 3 + 4 hesaplanır, tırnak içindeki ise olduğu gibi yazılır. Virgülle birden fazla değer verirsen, aralarına boşluk koyarak yan yana yazar.

**Ekranda başlık:** Sayılar ve metinler

**Kod** (vurgulanan satırlar: 2, 3):

```js
console.log(3 + 4);
console.log("3 + 4");
console.log("Yakıt:", 100, "litre");
```

**Çıktı:**

```text
7
3 + 4
Yakıt: 100 litre
```

**Maskot:** konusma pozu, alt-sag

## Sahne 5: kod (13 sn)

**Seslendirme:** İki bölü ile başlayan satır bir yorumdur. JavaScript onu okumaz, o sana ve arkadaşlarına bırakılan bir nottur. Birden fazla satırlık yorumu bölü yıldızla açıp kapatırsın.

**Ekranda başlık:** Yorumlar

**Kod** (vurgulanan satırlar: 1, 3, 4):

```js
// Bu satır çalışmaz, sadece bir not
console.log("Bu satır çalışır");
/* Birden fazla satırlık
   yorum böyle yazılır */
```

**Çıktı:**

```text
Bu satır çalışır
```

**Maskot:** isaret pozu, alt-sag

## Sahne 6: hata (15 sn)

**Seslendirme:** Eyvah, kırmızı bir mesaj! Korkma, hata mesajı bir ipucudur. Consle tanımlı değil diyor: console yanlış yazılmış. Satır numarasına bak, o satırı dikkatle oku, düzelt ve tekrar çalıştır.

**Ekranda başlık:** Hata mesajı bir ipucudur

**Kod** (vurgulanan satırlar: 1):

```js
consle.log("Merhaba");
```

**Çıktı:**

```text
ReferenceError: consle is not defined
```

**Maskot:** sasirma pozu, sag

*Yönetmen notu: Hata satırı kırmızı yanar, ardından 'consle' kelimesi 'console' olarak düzelir.*

## Sahne 7: soru (9 sn)

**Seslendirme:** Sıra sende! Bu iki satır aynı şeyi mi yazdırır, yoksa farklı mı? Videoyu durdur ve tahminini söyle.

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```js
console.log("10 * 2");
console.log(10 * 2);
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (8 sn)

**Seslendirme:** İlki tırnak içinde olduğu için aynen yazıldı. İkincisini JavaScript hesapladı ve 20 yazdı. Bildiysen harikasın!

**Ekranda başlık:** Cevap

**Kod**:

```js
console.log("10 * 2");
console.log(10 * 2);
```

**Çıktı:**

```text
10 * 2
20
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (13 sn)

**Seslendirme:** Şimdi görev zamanı! Kontrol merkezine ilk sinyalini gönder, kalkış kontrol listesini sırayla yazdır ve bir yılda kaç saat olduğunu JavaScript'e hesaplat.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: İlk sinyal
- Görev 2: Kalkış kontrol listesi
- Görev 3: Uçuş hesabı

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (11 sn)

**Seslendirme:** Bugün üç şey öğrendik: console.log ile yazdırmak, yorumlarla not bırakmak ve hata mesajını bir ipucu gibi okumak.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- console.log(...) Çıktı alanına yazar
- // ile yorum: JavaScript okumaz
- Hata mesajı nerede ve ne olduğunu söyler

**Maskot:** on pozu, sag

## Sahne 11: kapanis (10 sn)

**Seslendirme:** İlk sinyal gönderildi, tebrikler kaptan! Yarın yakıtı, hızı ve pilotun adını etiketli kutulara saklayacağız: değişkenler bizi bekliyor.

**Ekranda başlık:** Yarın: Değişkenler ve veri tipleri

**Görsel:** `maskotlar/kodi-javascript/kahraman.png`

**Maskot:** tebrik pozu, sag

*Yönetmen notu: Arka planda roketin motorları ısınır; sonra Kodi el sallayarak çıkar.*
