# Video senaryosu: Gün 20, Paket yöneticisi pip

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~154 sn

Piko, Keşif Adası'nın limanına inen kutulardan yola çıkarak paketleri, pip komutlarını, requirements.txt dosyasını ve sürüm karşılaştırma tuzağını anlatıyor.

Ders metni: [gun-20.md](../gunler/gun-20.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 13 sn | mutlu (sag) |
| 2 | anlatim | 14 sn | konusma (sag) |
| 3 | anlatim | 16 sn | isaret (sol) |
| 4 | hata | 12 sn | uzgun (sag) |
| 5 | anlatim | 15 sn | konusma (sag) |
| 6 | kod | 12 sn | isaret (sol) |
| 7 | anlatim | 9 sn | dusunme (sag) |
| 8 | soru | 9 sn | dusunme (sag) |
| 9 | cikti | 16 sn | sasirma (sol) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 12 sn | on (sag) |
| 12 | kapanis | 13 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Gün 20: Paket yöneticisi pip! Bu derste paketleri, pip komutlarını, requirements.txt dosyasını ve sürüm karşılaştırma tuzağını öğreneceksin.

- Paket ve PyPI
- pip komutları
- requirements.txt ve sürümler

## Sahne 1: acilis (13 sn)

**Seslendirme:** Selam, ben Piko! Keşif Adası'nın limanına her gün gemiler yanaşıyor ve dünyanın dört bir yanından kutular iniyor. İçlerinde başka programcıların yaptığı hazır aletler var. Bu kutulara paket, onları getiren gemiye pip diyoruz!

**Ekranda başlık:** Gün 20: Paket yöneticisi pip

**Ekranda maddeler:**

- Keşif Adası
- Paketler, pip, requirements.txt

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Arka plan: Keşif Adası bölge görseli (gorseller/python/harita/ada.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Limana yanaşan gemiden kutular iner; kutuların üstünde requests, pygame, pandas yazar.*

## Sahne 2: anlatim (14 sn)

**Seslendirme:** Paket, birilerinin yazıp herkesle paylaştığı modüller topluluğudur. Yüz binlerce paket PyPI adlı dev bir depoda durur. requests internetten veri alır, pygame oyun yapar, pandas tablo işler.

**Ekranda başlık:** Paket nedir?

**Ekranda maddeler:**

- PyPI: Python Package Index
- requests: internetten veri
- pygame: oyun
- pandas: tablo

**Maskot:** konusma pozu, sag

## Sahne 3: anlatim (16 sn)

**Seslendirme:** pip paketleri kuran programdır. Bu komutlar Python kodunun içine değil, bilgisayarındaki terminale yazılır. install kurar, iki eşittirle belli bir sürümü seçersin. list ve freeze kurulu paketleri gösterir, uninstall kaldırır.

**Ekranda başlık:** pip komutları (terminalde)

**Ekranda maddeler:**

- pip install requests
- pip install pygame==2.5.2
- pip list  /  pip freeze
- pip uninstall requests

**Maskot:** isaret pozu, sol

## Sahne 4: hata (12 sn)

**Seslendirme:** İşte en sık hata: pip komutunu Python dosyasına yazmak. Python bunu kod sanıyor ve SyntaxError veriyor. pip install her zaman terminalde çalışır.

**Ekranda başlık:** Sık hata: pip kodun içinde

**Kod** (vurgulanan satırlar: 1):

```python
pip install requests
```

**Çıktı:**

```text
SyntaxError: invalid syntax
```

**Maskot:** uzgun pozu, sag

## Sahne 5: anlatim (15 sn)

**Seslendirme:** Bir projenin ihtiyaç duyduğu paketler requirements.txt dosyasına yazılır, her satırda paket ve sürümü. Projeni indiren biri tek komutla hepsini kurar: pip install tire r requirements.txt.

**Ekranda başlık:** requirements.txt

**Ekranda maddeler:**

- requests==2.31.0
- pygame==2.5.2
- Hepsini kur: pip install -r requirements.txt

**Maskot:** konusma pozu, sag

## Sahne 6: kod (12 sn)

**Seslendirme:** Böyle bir satırı Python'la okumak kolay. split ile iki eşittirden bölüyorum, iki parçayı da aynı anda iki değişkene açıyorum.

**Ekranda başlık:** Satırı parçala

**Kod** (vurgulanan satırlar: 2):

```python
line = "requests==2.31.0"
name, version = line.split("==")
print("Paket:", name)
print("Sürüm:", version)
```

**Çıktı:**

```text
Paket: requests
Sürüm: 2.31.0
```

**Maskot:** isaret pozu, sol

## Sahne 7: anlatim (9 sn)

**Seslendirme:** Sürüm numaraları büyük, küçük ve yama diye üç parçadan oluşur. Karşılaştırırken bir tuzak var, hemen görelim.

**Ekranda başlık:** Sürüm numaraları

**Ekranda maddeler:**

- 2.31.0 = büyük.küçük.yama
- Hangisi daha yeni: 2.4.1 mi, 2.31.0 mı?

**Maskot:** dusunme pozu, sag

## Sahne 8: soru (9 sn)

**Seslendirme:** Sence sürümleri yazı olarak karşılaştırınca, 2.4.1 büyük mü çıkar? True mu yazar, False mu?

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```python
a = "2.4.1"
b = "2.31.0"
print("Yazı olarak:", a > b)
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (16 sn)

**Seslendirme:** True yazdı ama bu yanlış! Yazılar harf harf karşılaştırılır ve dört, üçten büyüktür. Doğrusu parçaları sayıya çevirip tuple yapmak. O zaman otuz bir, dörtten büyük çıkar ve 2.31.0 daha yeni olur.

**Ekranda başlık:** Sürüm tuzağı

**Kod** (vurgulanan satırlar: 4, 6):

```python
a = "2.4.1"
b = "2.31.0"
print("Yazı olarak:", a > b)
va = tuple(int(p) for p in a.split("."))
vb = tuple(int(p) for p in b.split("."))
print("Sayı olarak:", va > vb)
```

**Çıktı:**

```text
Yazı olarak: True
Sayı olarak: False
```

**Maskot:** sasirma pozu, sol

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görevlerde bir satırı parçalayacak, bütün bir requirements metnini sözlüğe çevirecek ve iki sürümden hangisinin daha yeni olduğunu bulacaksın. Projede de oyunumuzun paket listesini hazırlıyorsun.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Satırı parçala
- Görev 2: requirements okuyucu
- Görev 3: Hangisi daha yeni?
- Challenge: Eksik paketler
- Proje: Paket listesi

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (12 sn)

**Seslendirme:** Özetle: paketler PyPI'da durur, pip onları terminalden kurar, requirements.txt de listeyi saklar. Bir sürpriz: import this yazıp çalıştır!

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- Paket = paylaşılan hazır modüller
- pip install, list, freeze, uninstall
- Sürümleri sayı olarak karşılaştır

**Maskot:** on pozu, sag

## Sahne 12: kapanis (13 sn)

**Seslendirme:** Keşif Adası'nı bitirdik, tebrikler! Yarın Bilgi Limanı'na yelken açıyoruz. Orada class ile kendi veri tiplerini, yani sınıfları ve nesneleri kuracağız. Görüşürüz!

**Ekranda başlık:** Yarın: Sınıflar ve nesneler

**Ekranda maddeler:**

- Yeni bölge: Bilgi Limanı
- class, __init__, self

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** Bu dersin interaktif hâli 30gunde.com.tr'de seni bekliyor. Kodunu tarayıcıda yaz, hemen çalıştır ve görevleri tamamla!

**Ekranda:** İnteraktif dersler için **30gunde.com.tr**

- Kodunu tarayıcıda yaz ve çalıştır
- Görevleri tamamla, rozet kazan
- 30 günde adım adım Python
