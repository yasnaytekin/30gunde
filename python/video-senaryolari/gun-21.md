# Video senaryosu: Gün 21, Sınıflar ve nesneler

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~150 sn

Piko, Bilgi Limanı'nın tersanesinde class ile kalıp kurmayı; __init__, self, metotlar, __str__ ve kalıtımla nesneler üretmeyi anlatıyor.

Ders metni: [gun-21.md](../gunler/gun-21.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 14 sn | mutlu (sag) |
| 2 | kod | 13 sn | isaret (sag) |
| 3 | kod | 16 sn | isaret (sol) |
| 4 | anlatim | 10 sn | konusma (sag) |
| 5 | soru | 10 sn | dusunme (sag) |
| 6 | cikti | 10 sn | mutlu (sol) |
| 7 | kod | 12 sn | isaret (sag) |
| 8 | kod | 17 sn | isaret (sol) |
| 9 | hata | 12 sn | sasirma (sag) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 12 sn | tebrik (orta) |

## Sahne 1: acilis (14 sn)

**Seslendirme:** Selam, ben Piko! Bilgi Limanı'na vardık! Tersanede gemiler tek bir çizime göre yapılıyor. Çizim bir kez hazırlanıyor, ondan istediğin kadar gemi çıkıyor. Python'da çizime sınıf, üretilen gemilere nesne diyoruz.

**Ekranda başlık:** Gün 21: Sınıflar ve nesneler

**Ekranda maddeler:**

- Yeni bölge: Bilgi Limanı
- class, __init__, self, metot, kalıtım

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Arka plan: Bilgi Limanı bölge görseli (gorseller/python/harita/liman.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Tersanede tek bir gemi çiziminden üç gemi çıkar.*

## Sahne 2: kod (13 sn)

**Seslendirme:** Aslında hep nesne kullandın: Piko yazısı bir str nesnesi. Kendi sınıfımızı class ile kuruyorum, adı büyük harfle başlıyor. Parantezle çağırınca o kalıptan bir nesne çıkıyor.

**Ekranda başlık:** Sınıf ve nesne

**Kod** (vurgulanan satırlar: 1, 4):

```python
class Pet:
    pass

tost = Pet()
print(type(tost))
print(type("Piko"))
```

**Çıktı:**

```text
<class '__main__.Pet'>
<class 'str'>
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (16 sn)

**Seslendirme:** __init__ nesne oluşturulurken kendiliğinden çalışan özel bir metot. self o an üretilen nesnenin kendisi. self.name ve self.happiness bu nesnenin özellikleri oluyor, her nesnenin kendine ait.

**Ekranda başlık:** __init__ ve self

**Kod** (vurgulanan satırlar: 2, 3, 4):

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50

tost = Pet("Tost")
print(tost.name)
print(tost.happiness)
```

**Çıktı:**

```text
Tost
50
```

**Maskot:** isaret pozu, sol

## Sahne 4: anlatim (10 sn)

**Seslendirme:** Sınıfın içindeki fonksiyonlara metot denir. İlk parametreleri her zaman self olur. Böylece metot hangi nesnenin özelliğini değiştireceğini bilir.

**Ekranda başlık:** Metotlar

**Kod** (vurgulanan satırlar: 6, 7):

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50

    def feed(self):
        self.happiness += 10
```

**Maskot:** konusma pozu, sag

## Sahne 5: soru (10 sn)

**Seslendirme:** Aynı kalıptan iki evcil hayvan yaptım ve sadece Tost'u iki kez besledim. Sence ekranda hangi mutluluk değerleri çıkar?

**Ekranda başlık:** Sence ne yazdırır?

**Kod** (vurgulanan satırlar: 11, 12):

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50

    def feed(self):
        self.happiness += 10

tost = Pet("Tost")
misket = Pet("Misket")
tost.feed()
tost.feed()
print(tost.name, tost.happiness)
print(misket.name, misket.happiness)
```

**Maskot:** dusunme pozu, sag

## Sahne 6: cikti (10 sn)

**Seslendirme:** Tost yetmiş oldu, Misket elli kaldı. İki nesne aynı kalıptan çıktı ama her birinin özellikleri ayrı ayrı saklanıyor.

**Ekranda başlık:** Cevap

**Kod**:

```python
class Pet:
    def __init__(self, name):
        self.name = name
        self.happiness = 50

    def feed(self):
        self.happiness += 10

tost = Pet("Tost")
misket = Pet("Misket")
tost.feed()
tost.feed()
print(tost.name, tost.happiness)
print(misket.name, misket.happiness)
```

**Çıktı:**

```text
Tost 70
Misket 50
```

**Maskot:** mutlu pozu, sol

## Sahne 7: kod (12 sn)

**Seslendirme:** __str__ metodu, print bir nesneyi yazdırırken ne görüneceğini belirler. Böylece gemi kendini güzel bir cümleyle tanıtıyor.

**Ekranda başlık:** Kendini tanıtan nesne

**Kod** (vurgulanan satırlar: 6, 7):

```python
class Ship:
    def __init__(self, name, cargo):
        self.name = name
        self.cargo = cargo

    def __str__(self):
        return f"{self.name} gemisi, yük: {self.cargo}"

print(Ship("Martı", 12))
```

**Çıktı:**

```text
Martı gemisi, yük: 12
```

**Maskot:** isaret pozu, sag

## Sahne 8: kod (17 sn)

**Seslendirme:** Kalıtımda bir sınıf başka bir sınıfın her şeyini miras alır. Wizard, Hero'dan geliyor, kendi __init__'i bile yok ama adı biliyor. Üstüne cast metodunu ekliyor. Kendi __init__'ini yazarsan üsttekini super ile çağırırsın.

**Ekranda başlık:** Kalıtım

**Ekranda maddeler:**

- Kendi __init__ yazarsan: super().__init__(name)

**Kod** (vurgulanan satırlar: 5, 6):

```python
class Hero:
    def __init__(self, name):
        self.name = name

class Wizard(Hero):
    def cast(self):
        return f"{self.name} büyü yaptı!"

w = Wizard("Merlin")
print(w.cast())
```

**Çıktı:**

```text
Merlin büyü yaptı!
```

**Maskot:** isaret pozu, sol

## Sahne 9: hata (12 sn)

**Seslendirme:** En sık hata metotta self'i unutmak. Python nesneyi gizlice ilk bilgi olarak gönderir ama metot hiç parametre beklemiyor. Sonuç TypeError!

**Ekranda başlık:** Sık hata: self unutuldu

**Kod** (vurgulanan satırlar: 2):

```python
class Pet:
    def feed():
        print("Mama yedi")

Pet().feed()
```

**Çıktı:**

```text
TypeError: Pet.feed() takes 0 positional arguments but 1 was given
```

**Maskot:** sasirma pozu, sag

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görevlerde bir evcil hayvan sınıfı, para harcayan bir cüzdan ve kendini tanıtan bir kahraman yazacaksın. Projede de maceranın karakterleri birbirine saldırabilecek.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Evcil hayvan
- Görev 2: Cüzdan
- Görev 3: Kendini tanıt
- Challenge: Büyücü
- Proje: Karakter sınıfları

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** Özetle: sınıf kalıp, nesne ondan çıkan şey. __init__ kurar, metotlar iş yapar, kalıtım da miras bırakır.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- class ile kalıp, Pet() ile nesne
- __init__ ve self ile özellikler
- Metotlar ve kalıtım (super)

**Maskot:** on pozu, sag

## Sahne 12: kapanis (12 sn)

**Seslendirme:** Tersanenin ustası oldun! Yarın limanın ilan panosuna gidiyoruz. Web sayfalarından başlık, bağlantı ve metin toplamayı, yani web kazımayı öğreneceğiz. Görüşürüz!

**Ekranda başlık:** Yarın: Web kazıma

**Ekranda maddeler:**

- HTML etiketleri
- BeautifulSoup

**Maskot:** tebrik pozu, orta
