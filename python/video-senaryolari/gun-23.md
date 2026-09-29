# Video senaryosu: Gün 23, Sanal ortam

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~163 sn

Piko, Bilgi Limanı'ndaki iki geminin ayrı ambarları üzerinden sanal ortamın neden gerektiğini, venv komutlarını ve paket listesini paylaşmayı anlatıyor.

Ders metni: [gun-23.md](../gunler/gun-23.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | konusma (sag) |
| 2 | anlatim | 16 sn | dusunme (sol) |
| 3 | anlatim | 17 sn | isaret (sag) |
| 4 | anlatim | 10 sn | mutlu (sol) |
| 5 | hata | 13 sn | uzgun (sag) |
| 6 | anlatim | 14 sn | konusma (sag) |
| 7 | soru | 10 sn | dusunme (sag) |
| 8 | cikti | 10 sn | sasirma (sol) |
| 9 | kod | 12 sn | isaret (sag) |
| 10 | kod | 11 sn | isaret (sol) |
| 11 | gorev | 13 sn | konusma (sag) |
| 12 | ozet | 11 sn | on (sag) |
| 13 | kapanis | 12 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Gün 23: Sanal ortam! Bu derste sanal ortamın neden gerektiğini, venv komutlarını ve paket listesini paylaşmayı öğreneceksin.

- Sürüm çakışması sorunu
- venv komutları
- requirements.txt ile paylaşmak

## Sahne 1: acilis (14 sn)

**Seslendirme:** Selam, ben Piko! Bilgi Limanı'nda iki gemi yan yana duruyor: biri balık taşıyor, diğeri çiçek. Yükler karışsa ne olurdu, düşünsene! Her geminin kendi ambarı var. Python projelerinin de kendi ambarı olmalı. Adı: sanal ortam.

**Ekranda başlık:** Gün 23: Sanal ortam

**Ekranda maddeler:**

- Bilgi Limanı
- venv ile proje düzeni

**Maskot:** konusma pozu, sag

*Yönetmen notu: Arka plan: Bilgi Limanı bölge görseli (gorseller/python/harita/liman.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Yan yana iki gemi; birinin ambarında balık, diğerinde çiçek.*

## Sahne 2: anlatim (16 sn)

**Seslendirme:** Sorunu görelim. Oyun projen pygame 2.5 istiyor, eski bir projen de 2.1. Bilgisayarda tek bir paket kutusu varsa ikisi aynı anda kurulamaz, birini güncellersen öbürü bozulur. Sanal ortam her projeye ayrı bir kutu verir.

**Ekranda başlık:** Sorun: sürüm çakışması

**Ekranda maddeler:**

- oyun → pygame 2.5
- eski-oyun → pygame 2.1
- Tek kutu: biri bozulur
- Sanal ortam: her projeye ayrı kutu

**Maskot:** dusunme pozu, sol

## Sahne 3: anlatim (17 sn)

**Seslendirme:** Bu komutlar terminale, proje klasöründeyken yazılır. İlki nokta venv adında bir ortam kurar. Sonra onu etkinleştirirsin: Windows'ta Scripts klasöründeki activate, macOS ve Linux'ta source komutu. Kapatmak için deactivate yeter.

**Ekranda başlık:** Oluştur ve etkinleştir (terminalde)

**Ekranda maddeler:**

- python -m venv .venv
- Windows: .venv\Scripts\activate
- macOS/Linux: source .venv/bin/activate
- Kapat: deactivate

**Maskot:** isaret pozu, sag

## Sahne 4: anlatim (10 sn)

**Seslendirme:** Terminalin başında parantez içinde .venv yazısını görürsen ortam açık demektir. Artık pip install ile kurduğun her paket sadece bu projeye gider.

**Ekranda başlık:** Ortam açık mı?

**Ekranda maddeler:**

- (.venv) ~/oyun $
- pip install pygame → sadece bu projeye

**Maskot:** mutlu pozu, sol

## Sahne 5: hata (13 sn)

**Seslendirme:** Sık hata: paketi bir ortama kurup programı başka bir ortamda çalıştırmak, ya da ortamı etkinleştirmeyi unutmak. Python paketi bulamaz ve ModuleNotFoundError verir. Önce ortamı aç, sonra çalıştır.

**Ekranda başlık:** Sık hata: yanlış ortam

**Kod** (vurgulanan satırlar: 1):

```python
import pygame
```

**Çıktı:**

```text
ModuleNotFoundError: No module named 'pygame'
```

**Maskot:** uzgun pozu, sag

*Yönetmen notu: Paketin kurulu olmadığı bir ortamda çalıştırıldığında görülen hata; doğrulayıcıda çalıştırılmaz.*

## Sahne 6: anlatim (14 sn)

**Seslendirme:** Ortam klasörü büyüktür ve paylaşılmaz. Onun yerine paket listesini paylaşırız: pip freeze listeyi requirements dosyasına yazar. Arkadaşın kendi ortamını kurup aynı paketleri yükler. .venv klasörü de gitignore'a eklenir.

**Ekranda başlık:** Ortamı paylaşmak

**Ekranda maddeler:**

- pip freeze > requirements.txt
- pip install -r requirements.txt
- .venv klasörü .gitignore dosyasına

**Maskot:** konusma pozu, sag

## Sahne 7: soru (10 sn)

**Seslendirme:** Kodda da benzer bir tuzak var. Listeyi site değişkenine atadım ve site'a flask ekledim. Sence game listesi ne olur?

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```python
game = ["pygame"]
site = game
site.append("flask")
print("Oyun:", game)
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Game de değişti! Çünkü iki isim aynı kutuyu gösteriyor. Tıpkı iki projenin tek bir paket kutusunu paylaşması gibi.

**Ekranda başlık:** Cevap: paylaşılan kutu

**Kod**:

```python
game = ["pygame"]
site = game
site.append("flask")
print("Oyun:", game)
```

**Çıktı:**

```text
Oyun: ['pygame', 'flask']
```

**Maskot:** sasirma pozu, sol

## Sahne 9: kod (12 sn)

**Seslendirme:** Çözüm ayrı bir kopya almak. copy ile site kendi kutusuna sahip oluyor, game olduğu gibi kalıyor. Sanal ortam da projelere tam olarak bunu yapar.

**Ekranda başlık:** Ayrı kopya: copy()

**Kod** (vurgulanan satırlar: 2):

```python
game = ["pygame"]
site = game.copy()
site.append("flask")
print("Oyun:", game)
print("Site:", site)
```

**Çıktı:**

```text
Oyun: ['pygame']
Site: ['pygame', 'flask']
```

**Maskot:** isaret pozu, sag

## Sahne 10: kod (11 sn)

**Seslendirme:** Ortamları sözlükle taklit edelim. İki projede aynı paketin farklı sürümleri, birbirine hiç karışmadan yaşıyor.

**Ekranda başlık:** Ortamları taklit edelim

**Kod** (vurgulanan satırlar: 2, 3):

```python
envs = {
    "oyun": {"pygame": "2.5.2"},
    "eski-oyun": {"pygame": "2.1.0"},
}
for name, packages in envs.items():
    print(name, "->", packages)
```

**Çıktı:**

```text
oyun -> {'pygame': '2.5.2'}
eski-oyun -> {'pygame': '2.1.0'}
```

**Maskot:** isaret pozu, sol

## Sahne 11: gorev (13 sn)

**Seslendirme:** Görevlerde ortam komutlarını üretecek, bir listenin ayrı kopyasını alacak ve iki proje arasındaki sürüm çakışmalarını bulacaksın. Projede de paylaşılacak dosyaları seçiyorsun.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Komutları hazırla
- Görev 2: Ayrı kopya
- Görev 3: Çakışmayı bul
- Challenge: Ortama kur
- Proje: Proje düzeni

**Maskot:** konusma pozu, sag

## Sahne 12: ozet (11 sn)

**Seslendirme:** Özetle: her projeye bir sanal ortam kur, etkinleştir, paketleri içine yükle ve sadece listeyi paylaş.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- Sanal ortam = projeye özel paket kutusu
- python -m venv .venv, activate, deactivate
- Paylaşılan: requirements.txt, .venv değil

**Maskot:** on pozu, sag

## Sahne 13: kapanis (12 sn)

**Seslendirme:** Ambarlar tertemiz, aferin! Yarın limanın kayıt ofisine uğruyoruz. Ortalama, ortanca ve NumPy dizileriyle sayıları konuşturacağız. Görüşürüz!

**Ekranda başlık:** Yarın: İstatistik ve NumPy

**Ekranda maddeler:**

- statistics modülü
- NumPy dizileri

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** Bu dersin interaktif hâli 30gunde.com.tr'de seni bekliyor. Kodunu tarayıcıda yaz, hemen çalıştır ve görevleri tamamla!

**Ekranda:** İnteraktif dersler için **30gunde.com.tr**

- Kodunu tarayıcıda yaz ve çalıştır
- Görevleri tamamla, rozet kazan
- 30 günde adım adım Python
