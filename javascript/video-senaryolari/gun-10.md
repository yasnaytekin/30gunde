# Video senaryosu: Gün 10, Nesneler

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~157 sn

Nebuladaki istasyonda geminin kimlik kartını hazırlıyoruz: nesne oluşturmak, özellikleri okuyup değiştirmek, this ile metot yazmak, nesneleri dolaşmak ve nesne dizilerini parçalamak.

Ders metni: [gun-10.md](../gunler/gun-10.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 11 sn | el-sallama (sag) |
| 2 | kod | 17 sn | isaret (alt-sag) |
| 3 | kod | 14 sn | konusma (alt-sag) |
| 4 | kod | 16 sn | isaret (alt-sag) |
| 5 | kod | 15 sn | konusma (alt-sag) |
| 6 | kod | 17 sn | isaret (alt-sag) |
| 7 | hata | 15 sn | sasirma (sag) |
| 8 | soru | 10 sn | dusunme (sag) |
| 9 | cikti | 9 sn | mutlu (sag) |
| 10 | gorev | 12 sn | isaret (sol) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 10 sn | tebrik (sag) |

## Sahne 1: acilis (11 sn)

**Seslendirme:** Selam, ben Kodi! Nebuladaki bir uzay istasyonuna yanaştık. Görevli geminin kimlik kartını istiyor: adı, hızı, yakıtı, mürettebatı. Bunları tek pakette nasıl tutarız?

**Ekranda başlık:** Gün 10: Nesneler

**Görsel:** `gorseller/javascript/bolgeler/nebula.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: kod (17 sn)

**Seslendirme:** Nesne süslü parantezle yazılır; içinde anahtar ve değer çiftleri var. Değere noktayla ya da köşeli parantezle ulaşırız. Anahtar bir değişkenin içindeyse köşeli parantez şarttır.

**Ekranda başlık:** Nesne: anahtar ve değer

**Kod** (vurgulanan satırlar: 6, 7, 9):

```js
const ship = {
  name: "Kartal",
  speed: 40000,
  crew: ["Deniz", "Ada"],
};
console.log(ship.name);
console.log(ship["speed"]);
const key = "crew";
console.log(ship[key]);
```

**Çıktı:**

```text
Kartal
40000
[ 'Deniz', 'Ada' ]
```

**Maskot:** isaret pozu, alt-sag

*Yönetmen notu: Nesne bir kimlik kartı gibi çizilir; her anahtar kartın bir satırı.*

## Sahne 3: kod (14 sn)

**Seslendirme:** Değeri değiştirmek de, yeni anahtar eklemek de kolay. delete ile anahtarı sileriz. Olmayan bir anahtarı okursak undefined gelir.

**Ekranda başlık:** Değiştir, ekle, sil

**Kod** (vurgulanan satırlar: 2, 3, 5):

```js
const ship = { name: "Kartal", fuel: 80 };
ship.fuel -= 20;
ship.color = "gümüş";
console.log(ship);
delete ship.color;
console.log(ship.color);
```

**Çıktı:**

```text
{ name: 'Kartal', fuel: 60, color: 'gümüş' }
undefined
```

**Maskot:** konusma pozu, alt-sag

## Sahne 4: kod (16 sn)

**Seslendirme:** Nesnenin içindeki fonksiyona metot denir. Metodun içinde this, metodu çağıran nesnenin kendisidir. rocket.refuel dediğimiz için this burada rocket. Yakıt yetmiş oldu.

**Ekranda başlık:** Metotlar ve this

**Kod** (vurgulanan satırlar: 4, 5):

```js
const rocket = {
  name: "Kartal",
  fuel: 50,
  refuel(amount) {
    this.fuel += amount;
    return this.fuel;
  },
};

console.log(rocket.refuel(20));
```

**Çıktı:**

```text
70
```

**Maskot:** isaret pozu, alt-sag

## Sahne 5: kod (15 sn)

**Seslendirme:** Object.keys anahtarları, Object.values değerleri dizi olarak verir. for in ise nesnenin anahtarlarını sırayla dolaşır. Unutma: diziler için for of, nesneler için for in.

**Ekranda başlık:** Nesneleri dolaşmak

**Kod** (vurgulanan satırlar: 2, 3, 4):

```js
const ship = { name: "Kartal", speed: 40000 };
console.log(Object.keys(ship));
console.log(Object.values(ship));
for (const key in ship) {
  console.log(key, "→", ship[key]);
}
```

**Çıktı:**

```text
[ 'name', 'speed' ]
[ 'Kartal', 40000 ]
name → Kartal
speed → 40000
```

**Maskot:** konusma pozu, alt-sag

## Sahne 6: kod (17 sn)

**Seslendirme:** Gerçek programlarda nesnelerden oluşan diziler kullanırız. Döngünün başında süslü parantez yazarak her nesneyi parçaladık: name, role ve hours tek satırda değişken oldu.

**Ekranda başlık:** Nesne dizileri ve parçalama

**Kod** (vurgulanan satırlar: 6):

```js
const crew = [
  { name: "Deniz", role: "pilot", hours: 120 },
  { name: "Ada", role: "mühendis", hours: 95 },
];
let total = 0;
for (const { name, role, hours } of crew) {
  console.log(`${name} (${role}): ${hours} saat`);
  total += hours;
}
console.log("Toplam uçuş:", total, "saat");
```

**Çıktı:**

```text
Deniz (pilot): 120 saat
Ada (mühendis): 95 saat
Toplam uçuş: 215 saat
```

**Maskot:** isaret pozu, alt-sag

## Sahne 7: hata (15 sn)

**Seslendirme:** İki sık hata var. Anahtarı yanlış yazarsan hata çıkmaz, sessizce undefined gelir. Olmayan bir anahtarın içine girmeye çalışırsan ise kod çöker: undefined'ın özelliği okunamaz.

**Ekranda başlık:** Olmayan anahtar

**Kod** (vurgulanan satırlar: 2, 3):

```js
const ship = { name: "Kartal", speed: 40000 };
console.log(ship.nmae);
console.log(ship.engine.power);
```

**Çıktı:**

```text
undefined
TypeError: Cannot read properties of undefined (reading 'power')
```

**Maskot:** sasirma pozu, sag

## Sahne 8: soru (10 sn)

**Seslendirme:** Şahin 30 yakıtla başlıyor. refuel'i iki kez çağırıyoruz. Sence son satır kaç yazdırır?

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```js
const rocket = {
  name: "Şahin",
  fuel: 30,
  refuel(amount) {
    this.fuel += amount;
    return this.fuel;
  },
};
rocket.refuel(10);
console.log(rocket.refuel(5));
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (9 sn)

**Seslendirme:** 45! İlk çağrı yakıtı 40 yaptı ve nesne bunu hatırladı. İkinci çağrı 5 daha ekledi.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 9, 10):

```js
const rocket = {
  name: "Şahin",
  fuel: 30,
  refuel(amount) {
    this.fuel += amount;
    return this.fuel;
  },
};
rocket.refuel(10);
console.log(rocket.refuel(5));
```

**Çıktı:**

```text
45
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (12 sn)

**Seslendirme:** Görevlerin: Mars için bir gezegen kartı hazırla, bir geminin bilgilerini okuyup dolaş ve rokete yakıt ile durum metotları kazandır.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Gezegen kartı
- Görev 2: Bilgi okuyucu
- Görev 3: Roket metotları

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (11 sn)

**Seslendirme:** Özet: nesne, birbirine ait bilgileri anahtar ve değerle tutar. Metotlar this ile nesneye ulaşır. Nesne dizilerini parçalayarak kolayca dolaşırız.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- { anahtar: değer }, nokta ve [ ] ile erişim
- Metot içinde this = nesnenin kendisi
- Object.keys, for...in ve parçalama

**Maskot:** on pozu, sag

## Sahne 12: kapanis (10 sn)

**Seslendirme:** Kimlik kartı hazır, tebrikler! Yarın radarımız yüzlerce yıldız gösterecek. Dizilere map, filter ve reduce süper güçlerini vereceğiz.

**Ekranda başlık:** Yarın: map, filter, reduce

**Görsel:** `maskotlar/kodi-javascript/kahraman.png`

**Maskot:** tebrik pozu, sag
