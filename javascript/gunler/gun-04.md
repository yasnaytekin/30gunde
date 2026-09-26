# Gün 4: Metinlerle çalışmak

**Kurs:** 30 Günde JavaScript  ·  **Bölge:** Kalkış Üssü  ·  **Maskot:** Kodi

**Bugünün hedefi:** Şablon metinlerle mesaj oluşturmak ve metin metotlarını kullanmak

> Roket, uzaydaki istasyonlarla mesajlaşacak. Mesajları birleştirmek, büyük harfe çevirmek, içinde bir kelime aramak gerekecek. Bugün **metinlerin (string)** ustası oluyoruz.

![Kalkış Üssü](../../gorseller/javascript/bolgeler/kalkis.webp)

## Konu anlatımı

### Şablon metin: ters tırnak ve ${ }

Metinleri `+` ile birleştirebilirsin ama **şablon metin** çok daha rahattır. Şablon metin tırnak yerine **ters tırnakla** yazılır, değişkenler `${...}` içine konur:

```js
const pilot = "Deniz";
const planet = "Mars";
console.log(`Merhaba ${pilot}, hedef: ${planet}!`);
// Merhaba Deniz, hedef: Mars!
```

`${...}` içine işlem de yazabilirsin: `${3 + 4}` yazılan yerde çıktıda `7` görünür.

### Uzunluk ve harfler

- `text.length` metnin kaç karakter olduğunu verir.
- `text[0]` ilk karakteri verir; sayma **0'dan** başlar.

```js
const word = "roket";
console.log(word.length);  // 5
console.log(word[0]);      // r
```

### Metin metotları

| Metot | Ne yapar | Örnek → Sonuç |
| --- | --- | --- |
| `toUpperCase()` | Büyük harf | `"nova".toUpperCase()` → `"NOVA"` |
| `toLowerCase()` | Küçük harf | `"NOVA".toLowerCase()` → `"nova"` |
| `includes(x)` | İçinde x var mı? | `"Ay ışığı".includes("Ay")` → `true` |
| `slice(a, b)` | a'dan b'ye kadar parça | `"yıldız".slice(0, 3)` → `"yıl"` |
| `trim()` | Baştaki/sondaki boşlukları siler | `"  hey ".trim()` → `"hey"` |
| `replace(a, b)` | a'yı b ile değiştirir | `"Ay".replace("Ay", "Mars")` → `"Mars"` |

Metotlar metni değiştirmez, **yeni** bir metin verir: sonucu bir değişkene koymalısın.

### Türkçe harfler için bir ipucu

`"istanbul".toUpperCase()` sonucu `"ISTANBUL"` olur: noktasız I! Türkçe kurallarıyla çevirmek için `toLocaleUpperCase("tr")` kullan:

```js
console.log("istanbul".toLocaleUpperCase("tr"));  // İSTANBUL
console.log("IŞIK".toLocaleLowerCase("tr"));      // ışık
```

## Örnekler

### Şablon metin

```js
const ship = "Kartal";
const speed = 40000;
console.log(`${ship} saatte ${speed} km hızla gidiyor.`);
```

*Ters tırnak klavyede genellikle Tab'ın üstünde ya da AltGr + , tuşlarındadır; editörün tuş çubuğunda da var.*

### Metin metotları

```js
const message = "  Acil: Yakıt Azaldı  ";
const clean = message.trim();
console.log(clean.toUpperCase());
console.log(clean.includes("Yakıt"));
console.log(clean.length);
```

## Görevler

### Görev 1: Karşılama mesajı

`greeting` değişkenine şablon metinle `Hoş geldin Deniz, hedef: Mars!` yaz. İsim ve gezegen değişkenlerden (`${...}`) gelsin, sonra yazdır.

**Başlangıç kodu:**

```js
const pilot = "Deniz";
const planet = "Mars";

// greeting'i şablon metinle oluştur

console.log(greeting);
```

**İpuçları:**

1. Ters tırnak ` ile başla ve bitir.
2. const greeting = `Hoş geldin ${pilot}, hedef: ${planet}!`;

<details><summary>Çözüm</summary>

```js
const pilot = "Deniz";
const planet = "Mars";

// greeting'i şablon metinle oluştur
const greeting = `Hoş geldin ${pilot}, hedef: ${planet}!`;

console.log(greeting);
```

</details>

### Görev 2: Çağrı kodu

Her geminin bir çağrı kodu var: adın **büyük harfle** yazılışı, bir tire ve adın **harf sayısı**. `name` "nova" ise `callSign` `NOVA-4` olmalı.

**Başlangıç kodu:**

```js
const name = "nova";

// callSign'ı oluştur

console.log(callSign);
```

**İpuçları:**

1. name.toUpperCase() ve name.length kullan.
2. const callSign = `${name.toUpperCase()}-${name.length}`;

<details><summary>Çözüm</summary>

```js
const name = "nova";

// callSign'ı oluştur
const callSign = `${name.toUpperCase()}-${name.length}`;

console.log(callSign);
```

</details>

### Görev 3: Mesaj tarayıcı

Gelen mesajı incele:

- `isUrgent`: mesajda `"Acil"` kelimesi geçiyor mu? (`includes`)
- `title`: mesajın ilk 11 karakteri (`slice`), yani `"Acil durum:"`

**Başlangıç kodu:**

```js
const message = "Acil durum: yakıt azaldı";

// isUrgent ve title'ı oluştur

console.log(isUrgent);
console.log(title);
```

**İpuçları:**

1. message.includes("Acil") true ya da false verir.
2. message.slice(0, 11) ilk 11 karakteri verir.

<details><summary>Çözüm</summary>

```js
const message = "Acil durum: yakıt azaldı";

// isUrgent ve title'ı oluştur
const isUrgent = message.includes("Acil");
const title = message.slice(0, 11);

console.log(isUrgent);
console.log(title);
```

</details>

## Challenge: Tersten okunuş

`reversed` değişkeni `word`'ün tersten yazılışı olsun ve `isPalindrome` kelimenin tersten de aynı okunup okunmadığını söylesin. "radar" tersten de "radar"dır!

İpucu: `word.split("")` harfleri bir listeye ayırır, `.reverse()` listeyi ters çevirir, `.join("")` yeniden birleştirir. Listeleri ileride detaylı göreceğiz.

**Başlangıç kodu:**

```js
const word = "radar";

// reversed ve isPalindrome

console.log(reversed, isPalindrome);
```

**İpuçları:**

1. Metotlar zincirlenebilir: word.split("").reverse().join("")
2. const isPalindrome = word === reversed;

<details><summary>Çözüm</summary>

```js
const word = "radar";

// reversed ve isPalindrome
const reversed = word.split("").reverse().join("");
const isPalindrome = word === reversed;

console.log(reversed, isPalindrome);
```

</details>

## Proje adımları

Bugünün katkısı (Yıldız Avcısı): **Durum çubuğu**

### Yıldız Avcısı: Durum çubuğu

Oyunun üstünde bir durum çubuğu olacak. Şablon metinle `status` değişkenini oluştur:

- Geminin adı **büyük harfle**
- Yıldız sayısı `/10` ile (kaç yıldızdan kaçı toplandı)
- Can sayısı

`shipName` "Kartal" ise beklenen: `KARTAL | Yıldız: 3/10 | Can: 2`

**Başlangıç kodu:**

```js
const shipName = "Kartal";
let stars = 3;
let lives = 2;

// status'u şablon metinle oluştur

console.log(status);
```

**İpuçları:**

1. Büyük harf için toLocaleUpperCase("tr") Türkçe harfleri de doğru çevirir.
2. const status = `${...} | Yıldız: ${stars}/10 | Can: ${lives}`;

<details><summary>Çözüm</summary>

```js
const shipName = "Kartal";
let stars = 3;
let lives = 2;

// status'u şablon metinle oluştur
const status = `${shipName.toLocaleUpperCase("tr")} | Yıldız: ${stars}/10 | Can: ${lives}`;

console.log(status);
```

</details>

### Kişisel Web Sitem: Menü etiketi

Menüdeki bağlantı adı kullanıcıdan düzensiz geldi: `"  hakkımda "`.

- `label`: boşlukları temizlenmiş ve **ilk harfi büyük** hali: `"Hakkımda"`
- Sonra şunu yazdır: `Menü: Hakkımda (8 harf)` (harf sayısı `label.length`'ten gelsin)

**Başlangıç kodu:**

```js
const raw = "  hakkımda ";

// label'ı oluştur

// Menü satırını yazdır
```

**İpuçları:**

1. Önce trim() ile boşlukları sil.
2. İlk harf: clean[0].toLocaleUpperCase("tr"), gerisi: clean.slice(1)

<details><summary>Çözüm</summary>

```js
const raw = "  hakkımda ";

// label'ı oluştur
const clean = raw.trim();
const label = clean[0].toLocaleUpperCase("tr") + clean.slice(1);

// Menü satırını yazdır
console.log(`Menü: ${label} (${label.length} harf)`);
```

</details>

### Çalışma Asistanım: Görev satırı

Görevler listede büyük harfle ve başında bir onay kutusuyla görünecek.

- `line`: `[ ] ` ve ardından görevin **Türkçe kurallarıyla büyük harfli** hali: `[ ] FİZİK TEKRARI`
- `isLong`: görevin uzunluğu 10 karakterden fazla mı?

**Başlangıç kodu:**

```js
const task = "fizik tekrarı";

// line ve isLong

console.log(line);
console.log("Uzun görev:", isLong);
```

**İpuçları:**

1. toUpperCase "i" harfini "I" yapar; Türkçe için toLocaleUpperCase("tr") kullan.
2. const isLong = task.length > 10;

<details><summary>Çözüm</summary>

```js
const task = "fizik tekrarı";

// line ve isLong
const line = `[ ] ${task.toLocaleUpperCase("tr")}`;
const isLong = task.length > 10;

console.log(line);
console.log("Uzun görev:", isLong);
```

</details>

### Bilgi Yarışması: Cevabı düzenle

Yarışmacılar cevabı farklı yazabilir: `"  PASİFİK "`. Karşılaştırmadan önce düzenleyelim:

- `normalized`: boşlukları silinmiş ve **Türkçe kurallarıyla küçük harfli** cevap
- `isCorrect`: `normalized` ile `"pasifik"` aynı mı?

**Başlangıç kodu:**

```js
const userAnswer = "  PASİFİK ";

// normalized ve isCorrect

console.log(normalized, isCorrect);
```

**İpuçları:**

1. Metotları zincirleyebilirsin: userAnswer.trim().toLocaleLowerCase("tr")
2. const isCorrect = normalized === "pasifik";

<details><summary>Çözüm</summary>

```js
const userAnswer = "  PASİFİK ";

// normalized ve isCorrect
const normalized = userAnswer.trim().toLocaleLowerCase("tr");
const isCorrect = normalized === "pasifik";

console.log(normalized, isCorrect);
```

</details>
