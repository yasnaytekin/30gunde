# Video senaryosu: Gün 28, API kullanmak

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~146 sn

Piko, Python Dağı'ndaki kamp evinin telsiziyle API kavramını; JSON cevaplarını json.loads ile açmayı, json.dumps ile göndermeyi, durum kodlarını ve iç içe veriyi anlatıyor.

Ders metni: [gun-28.md](../gunler/gun-28.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | konusma (sag) |
| 2 | anlatim | 14 sn | isaret (sol) |
| 3 | kod | 16 sn | isaret (sag) |
| 4 | kod | 14 sn | isaret (sol) |
| 5 | anlatim | 16 sn | konusma (sag) |
| 6 | soru | 11 sn | dusunme (sag) |
| 7 | cikti | 12 sn | mutlu (sol) |
| 8 | hata | 12 sn | sasirma (sag) |
| 9 | gorev | 13 sn | konusma (sag) |
| 10 | ozet | 11 sn | on (sag) |
| 11 | kapanis | 13 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Gün 28: API kullanmak! Bu derste API'nin ne olduğunu, JSON cevaplarını açmayı, durum kodlarını kontrol etmeyi ve iç içe veride gezinmeyi öğreneceksin.

- API nedir?
- json.loads ve json.dumps
- Durum kodları ve iç içe veri

## Sahne 1: acilis (14 sn)

**Seslendirme:** Selam, ben Piko! Python Dağı'nın yarısındaki kamp evinde bir telsiz var. Hava istasyonunu arıyorum: Zirvede hava nasıl? İstasyon kısa ve düzenli bir cevap veriyor. Programlar da birbiriyle böyle konuşur. Bu kurallara API denir!

**Ekranda başlık:** Gün 28: API kullanmak

**Ekranda maddeler:**

- Python Dağı
- API, JSON, durum kodları

**Maskot:** konusma pozu, sag

*Yönetmen notu: Arka plan: Python Dağı bölge görseli (gorseller/python/harita/dag.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Kamp evinde cızırdayan bir telsiz, uzakta bir hava istasyonu.*

## Sahne 2: anlatim (14 sn)

**Seslendirme:** API, bir programın başka bir programdan bilgi istemesinin kurallarıdır. Restoranı düşün: mutfağa girmezsin, garsona sipariş verirsin, garson yemeği getirir. API o garsondur.

**Ekranda başlık:** API nedir?

**Ekranda maddeler:**

- Sen → garson (API) → mutfak (sunucu)
- Hava durumu, döviz kuru, oyun skorları

**Maskot:** isaret pozu, sol

## Sahne 3: kod (16 sn)

**Seslendirme:** API'ler çoğunlukla JSON ile cevap verir. JSON bir sözlüğe benzer ama aslında bir yazıdır. json.loads onu gerçek bir sözlüğe çeviriyor. JSON'daki küçük harfli true da Python'da büyük harfli True oluyor.

**Ekranda başlık:** JSON'u aç: json.loads

**Kod** (vurgulanan satırlar: 4, 7):

```python
import json

response = '{"sehir": "İzmir", "derece": 27, "gunesli": true}'
data = json.loads(response)
print(type(data))
print(f"{data['sehir']}: {data['derece']} derece")
print("Güneşli mi?", data["gunesli"])
```

**Çıktı:**

```text
<class 'dict'>
İzmir: 27 derece
Güneşli mi? True
```

**Maskot:** isaret pozu, sag

## Sahne 4: kod (14 sn)

**Seslendirme:** Tersi de var: json.dumps sözlüğü JSON yazısına çevirir, API'ye veri gönderirken lazım olur. İlk satırda ö harfi bir kaçış koduna dönüştü. ensure_ascii False dersen Türkçe harfler olduğu gibi kalır.

**Ekranda başlık:** Sözlükten JSON: json.dumps

**Kod** (vurgulanan satırlar: 4, 5):

```python
import json

order = {"urun": "fener", "adet": 2, "ödendi": False}
print(json.dumps(order))
print(json.dumps(order, ensure_ascii=False))
```

**Çıktı:**

```text
{"urun": "fener", "adet": 2, "\u00f6dendi": false}
{"urun": "fener", "adet": 2, "ödendi": false}
```

**Maskot:** isaret pozu, sol

## Sahne 5: anlatim (16 sn)

**Seslendirme:** Kendi bilgisayarında internetten veri almak için requests paketi kullanılır. Önce durum koduna bakarsın: iki yüz ise her şey yolunda, cevabı json ile açarsın. Değilse hatayı gösterirsin. Bu sitede internete çıkamadığımız için cevaplar hazır gelecek.

**Ekranda başlık:** requests ile istek (kendi bilgisayarında)

**Kod** (vurgulanan satırlar: 4):

```python
import requests

r = requests.get("https://api.ornek.com/hava?sehir=izmir")
if r.status_code == 200:
    data = r.json()
    print(data["derece"])
else:
    print("Hata:", r.status_code)
```

**Çıktı:**

```text
27
```

**Maskot:** konusma pozu, sag

*Yönetmen notu: İnternet gerektirdiği için çalıştırılmaz; çıktı örnek API cevabına göre beklenen değerdir.*

## Sahne 6: soru (11 sn)

**Seslendirme:** Gerçek cevaplar çoğu zaman iç içedir: sözlüğün içinde liste, listenin içinde sözlük. Sence bu satır hangi sayıyı yazdırır?

**Ekranda başlık:** Sence ne yazdırır?

**Kod** (vurgulanan satırlar: 5):

```python
import json

response = '{"sehir": "Van", "gunler": [{"gun": "Pzt", "derece": 18}, {"gun": "Sal", "derece": 21}]}'
data = json.loads(response)
print(data["gunler"][1]["derece"])
```

**Maskot:** dusunme pozu, sag

## Sahne 7: cikti (12 sn)

**Seslendirme:** Yirmi bir! Adım adım indik: önce günler listesi, sonra bir numaralı eleman, yani salı, en son da derece. Sayma sıfırdan başlıyor, unutma.

**Ekranda başlık:** Cevap: adım adım in

**Ekranda maddeler:**

- data["gunler"] → liste
- [1] → Salı
- ["derece"] → 21

**Kod**:

```python
import json

response = '{"sehir": "Van", "gunler": [{"gun": "Pzt", "derece": 18}, {"gun": "Sal", "derece": 21}]}'
data = json.loads(response)
print(data["gunler"][1]["derece"])
```

**Çıktı:**

```text
21
```

**Maskot:** mutlu pozu, sol

## Sahne 8: hata (12 sn)

**Seslendirme:** Sık hata: JSON yazısını açmadan sözlük gibi kullanmak. response hâlâ bir yazı ve yazıya anahtarla ulaşamazsın, TypeError alırsın. Önce json.loads ile aç!

**Ekranda başlık:** Sık hata: açılmamış JSON

**Kod** (vurgulanan satırlar: 2):

```python
response = '{"sehir": "İzmir", "derece": 27}'
print(response["derece"])
```

**Çıktı:**

```text
TypeError: string indices must be integers, not 'str'
```

**Maskot:** sasirma pozu, sag

## Sahne 9: gorev (13 sn)

**Seslendirme:** Görevlerde hava durumu cevabını açacak, bir ülke listesinden isimleri toplayacak ve durum koduna göre doğru mesajı yazdıracaksın. Projede de görev servisinden açık görevleri çekiyorsun.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Hava durumu
- Görev 2: Ülke listesi
- Görev 3: Durum kontrolü
- Challenge: Sipariş gönder
- Proje: Görev servisi

**Maskot:** konusma pozu, sag

## Sahne 10: ozet (11 sn)

**Seslendirme:** Özetle: API programların konuşma kuralıdır. Cevabı json.loads ile aç, durum kodunu kontrol et, iç içe veride adım adım in.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- API = programlar arası garson
- json.loads ve json.dumps
- Önce status_code, sonra veri

**Maskot:** on pozu, sag

## Sahne 11: kapanis (13 sn)

**Seslendirme:** Telsizi ustaca kullandın! Yarın rolleri değiştiriyoruz: soruları cevaplayan istasyon biz olacağız. GET, POST, PUT ve DELETE ile kendi API'mizi yazacağız. Görüşürüz!

**Ekranda başlık:** Yarın: API yapmak

**Ekranda maddeler:**

- Kendi API'n
- GET, POST, PUT, DELETE

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** Bu dersin interaktif hâli 30gunde.com.tr'de seni bekliyor. Kodunu tarayıcıda yaz, hemen çalıştır ve görevleri tamamla!

**Ekranda:** İnteraktif dersler için **30gunde.com.tr**

- Kodunu tarayıcıda yaz ve çalıştır
- Görevleri tamamla, rozet kazan
- 30 günde adım adım Python
