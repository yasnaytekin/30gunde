# Video senaryosu: Gün 19, Dosya işlemleri

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~155 sn

Piko, Keşif Adası'nın deniz fenerinde bulunan kaptan günlüğünden yola çıkarak dosyaya yazmayı, dosyadan okumayı ve JSON ile oyun kaydetmeyi anlatıyor.

Ders metni: [gun-19.md](../gunler/gun-19.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | mutlu (sag) |
| 2 | anlatim | 15 sn | isaret (sol) |
| 3 | kod | 16 sn | isaret (sag) |
| 4 | kod | 16 sn | isaret (sol) |
| 5 | kod | 17 sn | konusma (sag) |
| 6 | anlatim | 10 sn | dusunme (sag) |
| 7 | hata | 11 sn | sasirma (sol) |
| 8 | soru | 10 sn | dusunme (sag) |
| 9 | cikti | 10 sn | uzgun (sol) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 12 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Gün 19: Dosya işlemleri! Bu derste dosyaya yazmayı, dosyadan okumayı ve JSON ile oyunu kaydetmeyi öğreneceksin.

- open ve dosya modları
- Yaz, oku, sonuna ekle
- JSON ile kaydet

## Sahne 1: acilis (14 sn)

**Seslendirme:** Selam, ben Piko! Keşif Adası'nın deniz fenerinde eski bir kaptan günlüğü bulduk. Kaptan her akşam olanları yazmış, biz de yıllar sonra okuyabiliyoruz. Programların da böyle bir defteri var: dosyalar. Bugün oyunumuzu kaydetmeyi öğreniyoruz!

**Ekranda başlık:** Gün 19: Dosya işlemleri

**Ekranda maddeler:**

- Keşif Adası
- Yaz, oku, JSON ile kaydet

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Arka plan: Keşif Adası bölge görseli (gorseller/python/harita/ada.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Deniz fenerinde tozlu bir kaptan günlüğü açılır.*

## Sahne 2: anlatim (15 sn)

**Seslendirme:** open fonksiyonu bir dosyayı açar. İkinci bilgi moddur: r okumak, a sonuna eklemek için. w yazmak içindir ama dikkat, dosya varsa içini siler! with ise işimiz bitince dosyayı kendisi kapatır.

**Ekranda başlık:** Dosya açmak: open ve modlar

**Ekranda maddeler:**

- "r" oku (varsayılan)
- "w" yaz: varsa içini siler
- "a" sonuna ekle
- with dosyayı otomatik kapatır

**Maskot:** isaret pozu, sol

## Sahne 3: kod (16 sn)

**Seslendirme:** Önce w moduyla iki satır yazıyorum. Satır sonlarındaki ters eğik çizgi n yeni satır demek, çünkü write kendiliğinden alt satıra geçmez. Sonra dosyayı açıp read ile hepsini okuyorum.

**Ekranda başlık:** Yaz ve oku

**Kod** (vurgulanan satırlar: 1, 5):

```python
with open("gunluk.txt", "w") as f:
    f.write("1. gün: Kampa vardık\n")
    f.write("2. gün: Köyü gezdik\n")

with open("gunluk.txt") as f:
    print(f.read())
```

**Çıktı:**

```text
1. gün: Kampa vardık
2. gün: Köyü gezdik
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: Dosya kullandığı için doğrulayıcıda çalıştırılmaz; çıktı geçici bir klasörde çalıştırılarak alındı.*

## Sahne 4: kod (16 sn)

**Seslendirme:** a moduyla açınca eski satırlar silinmiyor, yenisi sona ekleniyor. Okurken dosyayı satır satır dolaşıyorum. strip satır sonundaki fazlalığı temizliyor, enumerate de numara veriyor.

**Ekranda başlık:** Sonuna ekle

**Kod** (vurgulanan satırlar: 4, 8):

```python
with open("liste.txt", "w") as f:
    f.write("kılıç\n")

with open("liste.txt", "a") as f:
    f.write("iksir\n")

with open("liste.txt") as f:
    for i, line in enumerate(f, 1):
        print(i, line.strip())
```

**Çıktı:**

```text
1 kılıç
2 iksir
```

**Maskot:** isaret pozu, sol

*Yönetmen notu: Dosya kullandığı için doğrulayıcıda çalıştırılmaz; çıktı geçici bir klasörde çalıştırılarak alındı.*

## Sahne 5: kod (17 sn)

**Seslendirme:** Sözlük ve listeleri kaydetmenin en kolay yolu JSON. json.dump sözlüğü dosyaya yazıyor, json.load da onu geri sözlük olarak okuyor. os.path.exists ile dosyanın var olup olmadığına da bakabilirsin.

**Ekranda başlık:** JSON ile kaydet

**Kod** (vurgulanan satırlar: 5, 9):

```python
import json, os

hero = {"name": "Piko", "hp": 80, "bag": ["harita"]}
with open("kayit.json", "w") as f:
    json.dump(hero, f)

print("Dosya var mı?", os.path.exists("kayit.json"))
with open("kayit.json") as f:
    print(json.load(f))
```

**Çıktı:**

```text
Dosya var mı? True
{'name': 'Piko', 'hp': 80, 'bag': ['harita']}
```

**Maskot:** konusma pozu, sag

*Yönetmen notu: Dosya kullandığı için doğrulayıcıda çalıştırılmaz; çıktı geçici bir klasörde çalıştırılarak alındı.*

## Sahne 6: anlatim (10 sn)

**Seslendirme:** Bu sitede yazdığın dosyalar sadece o çalıştırma boyunca yaşar. Kendi bilgisayarında ise diske yazılır ve program kapansa da kalır.

**Ekranda başlık:** Bu sitede dosyalar

**Ekranda maddeler:**

- Sitede: sadece o çalıştırma boyunca
- Kendi bilgisayarında: kalıcı
- Görevlerde önce yaz, sonra aynı kodda oku

**Maskot:** dusunme pozu, sag

## Sahne 7: hata (11 sn)

**Seslendirme:** Sık hata: olmayan bir dosyayı okumaya çalışmak. Python FileNotFoundError verir. Dosya adını kontrol et ya da önce os.path.exists ile bak.

**Ekranda başlık:** Sık hata: dosya yok

**Kod** (vurgulanan satırlar: 1):

```python
with open("kayip-harita.txt") as f:
    print(f.read())
```

**Çıktı:**

```text
FileNotFoundError: [Errno 2] No such file or directory: 'kayip-harita.txt'
```

**Maskot:** sasirma pozu, sol

## Sahne 8: soru (10 sn)

**Seslendirme:** Mini soru! Aynı dosyayı iki kez w moduyla açıp önce kılıç, sonra iksir yazıyorum. Sence en sonda dosyada ne var?

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```python
with open("canta.txt", "w") as f:
    f.write("kılıç\n")

with open("canta.txt", "w") as f:
    f.write("iksir\n")

with open("canta.txt") as f:
    print(f.read())
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (10 sn)

**Seslendirme:** Sadece iksir! w modu dosyayı her açılışta sıfırlar, kılıç silindi. İkisi de kalsın istiyorsan ikinci kez a moduyla açmalısın.

**Ekranda başlık:** Cevap

**Kod**:

```python
with open("canta.txt", "w") as f:
    f.write("kılıç\n")

with open("canta.txt", "w") as f:
    f.write("iksir\n")

with open("canta.txt") as f:
    print(f.read())
```

**Çıktı:**

```text
iksir
```

**Maskot:** uzgun pozu, sol

*Yönetmen notu: Dosya kullandığı için doğrulayıcıda çalıştırılmaz; çıktı geçici bir klasörde çalıştırılarak alındı.*

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görevlerde bir günlük yazıp okuyacak, çantadaki eşyaları dosyaya yazıp satırları sayacak ve bir skoru sona ekleyeceksin. Projede de oyunu JSON ile kaydedip geri yüklüyorsun.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Günlük yaz
- Görev 2: Satırları say
- Görev 3: Sonuna ekle
- Challenge: JSON kaydet ve yükle
- Proje: Oyunu kaydetme

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** Özetle: with open ile dosyayı aç, modu doğru seç, sözlükleri de JSON ile sakla.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- with open(ad, mod): "r", "w", "a"
- write yazar, read ve for line okur
- json.dump kaydeder, json.load yükler

**Maskot:** on pozu, sag

## Sahne 12: kapanis (12 sn)

**Seslendirme:** Oyunumuz artık kaydedilebiliyor, harika! Yarın limana gemiler yanaşıyor. Başkalarının yazdığı hazır paketleri ve onları getiren pip'i tanıyacağız. Görüşürüz!

**Ekranda başlık:** Yarın: Paket yöneticisi pip

**Ekranda maddeler:**

- Paket ve PyPI
- requirements.txt

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** Bu dersin interaktif hâli 30gunde.com.tr'de seni bekliyor. Kodunu tarayıcıda yaz, hemen çalıştır ve görevleri tamamla!

**Ekranda:** İnteraktif dersler için **30gunde.com.tr**

- Kodunu tarayıcıda yaz ve çalıştır
- Görevleri tamamla, rozet kazan
- 30 günde adım adım Python
