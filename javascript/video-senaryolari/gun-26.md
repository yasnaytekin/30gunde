# Video senaryosu: Gün 26, fetch ve API

**Kurs:** 30 Günde JavaScript  ·  **Maskot:** Kodi  ·  **Süre:** ~176 sn

Kodi, Async İstasyonu'nun anteniyle API kavramını, fetch ve res.json ile JSON veri almayı, res.ok ve durum kodlarını, sorgu metnini ve yükleniyor, başarılı, hata durumlarını anlatıyor.

Ders metni: [gun-26.md](../gunler/gun-26.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | el-sallama (sag) |
| 2 | anlatim | 15 sn | konusma (sol) |
| 3 | kod | 18 sn | isaret (sag) |
| 4 | kod | 17 sn | konusma (sol) |
| 5 | kod | 18 sn | isaret (sag) |
| 6 | hata | 14 sn | sasirma (sag) |
| 7 | kod | 15 sn | konusma (sol) |
| 8 | anlatim | 13 sn | dusunme (sag) |
| 9 | soru | 9 sn | dusunme (sag) |
| 10 | cikti | 9 sn | mutlu (sag) |
| 11 | gorev | 13 sn | isaret (sol) |
| 12 | ozet | 12 sn | konusma (sag) |
| 13 | kapanis | 11 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Kodi! Async İstasyonu'nun dev anteni açıldı! Artık uzaktaki sunuculardan veri isteyebiliriz. Peki bir sunucuya nasıl soru sorulur? Bugün fetch ile API'lerle konuşuyoruz!

**Ekranda başlık:** Gün 26: fetch ve API

**Görsel:** `gorseller/javascript/bolgeler/istasyon.webp`

**Maskot:** el-sallama pozu, sag

## Sahne 2: anlatim (15 sn)

**Seslendirme:** API, bir programın başka programlara açtığı kapıdır. Belli bir adrese istek gönderirsin, sunucu sana veri döndürür. Hava durumu uygulaması sıcaklığı böyle alır. Cevap çoğu zaman JSON biçimindedir.

**Ekranda başlık:** API nedir?

**Ekranda maddeler:**

- İstek: /demo-api/sehirler
- Cevap: JSON
- Kursun deneme API'si: şehirler, sorular, seviyeler, görevler

**Maskot:** konusma pozu, sol

*Yönetmen notu: Antenden sunucuya giden bir istek oku, geri dönen bir JSON paketi animasyonu.*

## Sahne 3: kod (18 sn)

**Seslendirme:** fetch isteği gönderir ve bir Promise döndürür; await ile cevabı bekleriz. Gelen cevap bir zarf gibidir. İçindeki veriyi okumak için bir kez daha bekleriz: res.json. İki await var, çünkü önce başlık, sonra gövde gelir.

**Ekranda başlık:** fetch ve res.json()

**Kod** (vurgulanan satırlar: 2, 3):

```js
async function loadCities() {
  const res = await fetch("/demo-api/sehirler");
  const cities = await res.json();
  console.log(cities.length, "şehir geldi");
}
loadCities();
```

**Çıktı:**

```text
8 şehir geldi
```

**Maskot:** isaret pozu, sag

## Sahne 4: kod (17 sn)

**Seslendirme:** Gelen veriyi sayfaya dökmek, dün ve önceki günlerde öğrendiklerimizin birleşimi. Her şehir için bir liste elemanı oluşturuyoruz. Sonunda kaç şehir geldiğini yazıyoruz.

**Ekranda başlık:** Veriyi sayfada göster

**Kod** (vurgulanan satırlar: 3, 4, 5, 6):

```js
const res = await fetch("/demo-api/sehirler");
const cities = await res.json();
for (const city of cities) {
  const li = document.createElement("li");
  li.textContent = `${city.ad}: ${city.sicaklik}°C`;
  list.append(li);
}
info.textContent = `${cities.length} şehir geldi.`;
```

**Çıktı:**

```text
Önce "Yükleniyor...", sonra şehirler listesi ve "8 şehir geldi."
```

**Maskot:** konusma pozu, sol

## Sahne 5: kod (18 sn)

**Seslendirme:** Her cevabın bir durum kodu vardır: 200 tamam, 404 bulunamadı, 500 sunucuda sorun. res.ok, kod 200 ile 299 arasındaysa true olur. Bağlantı hiç kurulamazsa fetch gerçekten hata fırlatır; onu try ve catch yakalar.

**Ekranda başlık:** res.ok ve durum kodları

**Kod** (vurgulanan satırlar: 3, 4, 8):

```js
try {
  const res = await fetch("/demo-api/hata");
  if (!res.ok) {
    info.textContent = `Hata! Durum kodu: ${res.status}`;
    return;
  }
  // başarılı: veriyi göster
} catch (err) {
  info.textContent = "Bağlantı kurulamadı.";
}
```

**Çıktı:**

```text
Hata! Durum kodu: 500
```

**Maskot:** isaret pozu, sag

## Sahne 6: hata (14 sn)

**Seslendirme:** Sık hata: fetch'in 404'te ya da 500'de hata fırlatacağını sanmak. Fırlatmaz! res.ok'u kontrol etmezsen hata sayfasını veri sanıp okumaya çalışırsın.

**Ekranda başlık:** Sık hata: res.ok'u kontrol etmemek

**Kod** (vurgulanan satırlar: 2):

```js
const res = await fetch("/demo-api/yanlis-adres"); // 404
const data = await res.json(); // hata yok sandın!
info.textContent = `${data.length} kayıt`;
```

**Çıktı:**

```text
Liste yerine anlamsız bir sonuç ya da beklenmedik bir hata çıkar.
```

**Maskot:** sasirma pozu, sag

## Sahne 7: kod (15 sn)

**Seslendirme:** Adresin sonuna soru işareti, anahtar ve değer ekleyerek süzülmüş veri isteyebilirsin. Değerde boşluk ya da Türkçe harf varsa encodeURIComponent onu adrese uygun hale getirir.

**Ekranda başlık:** Sorgu metni

**Kod** (vurgulanan satırlar: 2):

```js
const region = "İç Anadolu";
const url = `/demo-api/sehirler?bolge=${encodeURIComponent(region)}`;
console.log(url);
```

**Çıktı:**

```text
/demo-api/sehirler?bolge=%C4%B0%C3%A7%20Anadolu
```

**Maskot:** konusma pozu, sol

## Sahne 8: anlatim (13 sn)

**Seslendirme:** İyi bir sayfa kullanıcıyı bekletirken bilgilendirir. Her istekte üç durumu düşün: yükleniyor, başarılı ve hata. Sayfayı asla boş bırakma!

**Ekranda başlık:** Üç durum

**Ekranda maddeler:**

- Yükleniyor: istekten önce "Yükleniyor..."
- Başarılı: veriyi göster
- Hata: anlaşılır bir mesaj

**Maskot:** dusunme pozu, sag

## Sahne 9: soru (9 sn)

**Seslendirme:** Soru zamanı! Sunucu 404 döndürdü. Sence fetch hata fırlatır mı, yoksa res.ok false mu olur?

**Ekranda başlık:** Sence hangisi?

**Ekranda maddeler:**

- A) fetch hata fırlatır, catch çalışır
- B) res.ok false olur, res.status 404

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (9 sn)

**Seslendirme:** Cevap B! fetch cevabı aldığı sürece hata fırlatmaz. 404 de bir cevaptır; bu yüzden res.ok'u kendin kontrol edersin.

**Ekranda başlık:** Cevap: B

**Kod**:

```js
console.log(res.ok, res.status);
```

**Çıktı:**

```text
false 404
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (13 sn)

**Seslendirme:** Görev zamanı! Deneme API'sinden şehir listesini çekeceksin, düğmelerle bölgeye göre süzeceksin ve yükleniyor, başarılı, hata durumlarının hepsini gösteren bir fonksiyon yazacaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Şehir listesi
- Görev 2: Bölge filtresi
- Görev 3: Yükleniyor ve hata

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (12 sn)

**Seslendirme:** Özetleyelim: fetch ile iste, await res.json ile oku. res.ok'u kontrol et, bağlantı hatasını try ve catch ile yakala. Kullanıcıya her zaman durumu göster.

**Ekranda başlık:** Özet

**Ekranda maddeler:**

- await fetch(url) → await res.json()
- if (!res.ok) … res.status  ·  try/catch
- Yükleniyor → başarılı / hata

**Maskot:** konusma pozu, sag

## Sahne 13: kapanis (11 sn)

**Seslendirme:** Antenin çalışıyor, kaptan! Yarın istasyonun son durağında bir gemi fabrikası kuracağız: sınıflar ve modüller. Görüşürüz!

**Ekranda başlık:** Yarın: Sınıflar ve modüller

**Görsel:** `gorseller/javascript/arka-plan/bg-space-wide.webp`

**Maskot:** tebrik pozu, orta
