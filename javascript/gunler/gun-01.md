# Gün 1: JavaScript ile tanışma

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Kalkış Üssü  ·  **Maskot:** Kodi

**Bugünün hedefi:** console.log ile ekrana yazdırmak, yorum yazmak ve hata mesajı okumak

> Kalkış Üssü'ne hoş geldin, kaptan! Roketin pistte ama kontrol paneli senin komutlarını bekliyor. Roketin konuştuğu dil **JavaScript**: bugün ona ilk mesajını göndereceksin.

![Kalkış Üssü](../../gorseller/javascript/bolgeler/kalkis.webp)

## Konu anlatımı

### JavaScript nedir?

JavaScript, web sayfalarını canlandıran programlama dilidir. Bir düğmeye bastığında açılan menü, oyundaki skor, haritadaki konum: çoğunun arkasında JavaScript vardır.

JavaScript tarayıcının içinde çalışır. Bu yüzden bilgisayarına hiçbir şey kurman gerekmez: bu sayfadaki editöre yazdığın kod doğrudan tarayıcında çalışır.

### console.log ile konuşmak

`console.log(...)` parantezin içine yazdığın şeyi **Çıktı** alanına yazar. Metinler tırnak içinde yazılır, sayılar tırnaksız:

```js
console.log("Merhaba, dünya!");
console.log(42);
console.log(3 + 4);
```

Virgülle birden fazla değer verirsen aralarına boşluk koyarak yazar: `console.log("Yakıt:", 100)` çıktısı `Yakıt: 100` olur.

Satır sonundaki `;` (noktalı virgül) komutun bittiğini gösterir. Çoğu zaman yazmasan da çalışır ama yazmak iyi bir alışkanlıktır.

### Yorumlar

`//` ile başlayan satırlar **yorumdur**: JavaScript onları okumaz, kod sana ve arkadaşlarına not bırakmak içindir.

```js
// Bu satır çalışmaz, sadece bir not
console.log("Bu satır çalışır");
/* Birden fazla satırlık
   yorum böyle yazılır */
```

### Hata mesajı bir ipucudur

Kodda bir yanlışlık olursa kırmızı bir hata mesajı görürsün. Korkma: hata mesajı sana **nerede** ve **ne** olduğunu söyler.

```js
consle.log("Merhaba");
```

Bu kod `consle is not defined` hatası verir: `console` yanlış yazılmış. Mesajdaki satır numarasına bak, o satırı dikkatle oku, düzelt ve tekrar çalıştır. Programcılar günün büyük kısmını bunu yaparak geçirir.

## Örnekler

### İlk sinyal

```js
console.log("Merhaba, dünya!");
console.log("Roket hazır.");
```

*Çalıştır'a bas ve Çıktı alanına bak.*

### Sayılar ve metinler

```js
console.log(3 + 4);
console.log("3 + 4");
console.log("Yakıt:", 100, "litre");
```

*Tırnak içindeki 3 + 4 hesaplanmaz, olduğu gibi yazılır.*

## Görevler

### Görev 1: İlk sinyal

Kontrol merkezine tam olarak şu mesajı gönder: `Merhaba, uzay!`

**Başlangıç kodu:**

```js
// Mesajını aşağıya yaz
```

**İpuçları:**

1. console.log(...) kullan.
2. Metin tırnak içinde olmalı: "Merhaba, uzay!"
3. console.log("Merhaba, uzay!");

<details><summary>Çözüm</summary>

```js
// Mesajını aşağıya yaz
console.log("Merhaba, uzay!");
```

</details>

### Görev 2: Kalkış kontrol listesi

Kalkıştan önce kontrol listesini sırayla yazdır. Her satır ayrı bir `console.log` olsun:

```
Yakıt: tamam
Motor: tamam
Kalkışa hazır!
```

**Başlangıç kodu:**

```js
console.log("Yakıt: tamam");

// Diğer iki satırı ekle
```

**İpuçları:**

1. Her satır için ayrı bir console.log yaz.
2. Sıra önemli: önce Motor, sonra Kalkışa hazır!

<details><summary>Çözüm</summary>

```js
console.log("Yakıt: tamam");
console.log("Motor: tamam");
console.log("Kalkışa hazır!");
```

</details>

### Görev 3: Uçuş hesabı

Bir yılda kaç saat var? Sonucu kendin hesaplama: `console.log` içinde **`365 * 24`** işlemini JavaScript'e yaptır.

**Başlangıç kodu:**

```js
// 365 * 24 işleminin sonucunu yazdır
```

**İpuçları:**

1. Çarpma işareti * (yıldız) karakteridir.
2. İşlemi tırnak içine yazarsan hesaplanmaz!
3. console.log(365 * 24);

<details><summary>Çözüm</summary>

```js
// 365 * 24 işleminin sonucunu yazdır
console.log(365 * 24);
```

</details>

## Challenge: Tek satırda geri sayım

Tek bir `console.log` kullanarak şu 4 satırı yazdır:

```
3
2
1
Ateşle!
```

İpucu: metnin içindeki `\n` yeni satıra geçer.

**Başlangıç kodu:**

```js
// Sadece bir console.log kullan
```

**İpuçları:**

1. "a\nb" yazdırılınca a ve b ayrı satırlara düşer.
2. console.log("3\n2\n1\nAteşle!");

<details><summary>Çözüm</summary>

```js
// Sadece bir console.log kullan
console.log("3\n2\n1\nAteşle!");
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Oyunun açılış ekranı**

### Yıldız Avcısı: Açılış ekranı

**Yıldız Avcısı** oyunumuzun açılış ekranını yazdıralım. Şu üç satırı yazdır; ikinci satırda `Pilot:` yazısından sonra kendi adın ya da takma adın olsun:

```
*** YILDIZ AVCISI ***
Pilot: Deniz
Görev: 10 yıldız topla!
```

**Başlangıç kodu:**

```js
// Oyunun açılış ekranı
```

**İpuçları:**

1. Üç ayrı console.log yazabilirsin.
2. İkinci satır "Pilot: " ile başlamalı, ardından adın gelmeli.

<details><summary>Çözüm</summary>

```js
// Oyunun açılış ekranı
console.log("*** YILDIZ AVCISI ***");
console.log("Pilot: Deniz");
console.log("Görev: 10 yıldız topla!");
```

</details>

### Kişisel Web Sitem: Karşılama yazısı

**Kişisel Web Sitem** projemize başlıyoruz. Sitenin karşılama yazısını yazdır. İlk satırda kendi adın olsun:

```
Merhaba! Ben Deniz.
Bu benim ilk web sitem.
```

**Başlangıç kodu:**

```js
// Sitenin karşılama yazısı
```

**İpuçları:**

1. İki ayrı console.log yaz.
2. İlk satır "Merhaba! Ben " ile başlayıp nokta ile bitmeli.

<details><summary>Çözüm</summary>

```js
// Sitenin karşılama yazısı
console.log("Merhaba! Ben Deniz.");
console.log("Bu benim ilk web sitem.");
```

</details>

### Çalışma Asistanım: Açılış mesajı

**Çalışma Asistanım** uygulamasının açılış mesajını yazdır:

```
=== Çalışma Asistanım ===
Hedef: Her gün bir adım
```

**Başlangıç kodu:**

```js
// Asistanın açılış mesajı
```

**İpuçları:**

1. İki ayrı console.log yaz.
2. Eşittir işaretlerinin sayısına dikkat: üç tane.

<details><summary>Çözüm</summary>

```js
// Asistanın açılış mesajı
console.log("=== Çalışma Asistanım ===");
console.log("Hedef: Her gün bir adım");
```

</details>

### Bilgi Yarışması: İlk soru

**Bilgi Yarışması** projemize başlıyoruz. Karşılama mesajını ve ilk soruyu yazdır:

```
Bilgi Yarışmasına hoş geldin!
Soru 1: Ay, hangi gezegenin uydusudur?
```

**Başlangıç kodu:**

```js
// Yarışmanın ilk ekranı
```

**İpuçları:**

1. İki ayrı console.log yaz.
2. Soru işaretini unutma.

<details><summary>Çözüm</summary>

```js
// Yarışmanın ilk ekranı
console.log("Bilgi Yarışmasına hoş geldin!");
console.log("Soru 1: Ay, hangi gezegenin uydusudur?");
```

</details>
