# Video senaryosu: Gün 11, Fonksiyonlar

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~134 sn

Piko, Alet Atölyesi'nde kendi aletlerini yapmayı anlatıyor: def ile fonksiyon tanımlamak, parametreler, return ile sonuç döndürmek, varsayılan değerler ve *args.

Ders metni: [gun-11.md](../gunler/gun-11.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | mutlu (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 10 sn | konusma (sag) |
| 4 | kod | 13 sn | isaret (sag) |
| 5 | kod | 11 sn | konusma (sag) |
| 6 | kod | 11 sn | mutlu (sag) |
| 7 | hata | 13 sn | sasirma (sag) |
| 8 | soru | 9 sn | dusunme (sag) |
| 9 | cikti | 10 sn | mutlu (sag) |
| 10 | gorev | 13 sn | isaret (sol) |
| 11 | ozet | 8 sn | on (sag) |
| 12 | kapanis | 10 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Gün 11: Fonksiyonlar! Bu derste def ile kendi fonksiyonlarını yazmayı, parametre almayı ve return ile sonuç döndürmeyi öğreneceksin.

- def ile fonksiyon yazmak
- Parametre ve return
- Varsayılan değer ve *args

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Piko! Alet Atölyesi'ne hoş geldin. Burada her aletin bir işi var: çekiç çakar, testere keser. Bir kere yapılan alet defalarca kullanılır. Kodda da aynısı mümkün! Bu aletlere fonksiyon diyoruz.

**Ekranda başlık:** Gün 11: Fonksiyonlar

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Atölye tezgâhına yakınlaşma; duvarda asılı aletler.*

## Sahne 2: kod (14 sn)

**Seslendirme:** def ile kendi fonksiyonunu yaparsın. İçindeki satırlar girintili yazılır ve fonksiyon çağrılana kadar hiç çalışmaz. Adını ve parantezleri yazdığın her yerde iş başına geçer: burada iki kez.

**Ekranda başlık:** def ile fonksiyon tanımlamak

**Kod** (vurgulanan satırlar: 1, 4, 5):

```python
def greet():
    print("Merhaba!")

greet()
greet()
```

**Çıktı:**

```text
Merhaba!
Merhaba!
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (10 sn)

**Seslendirme:** Parantezin içine yazdığın isimler parametre. Fonksiyonu çağırırken bu kutulara değer koyarsın. Aynı alet, farklı malzemeyle farklı sonuç verir.

**Ekranda başlık:** Parametreler

**Kod** (vurgulanan satırlar: 1, 4, 5):

```python
def greet(name):
    print(f"Merhaba {name}, atölyeye hoş geldin!")

greet("Piko")
greet("Deniz")
```

**Çıktı:**

```text
Merhaba Piko, atölyeye hoş geldin!
Merhaba Deniz, atölyeye hoş geldin!
```

**Maskot:** konusma pozu, sag

## Sahne 4: kod (13 sn)

**Seslendirme:** print sonucu sadece ekrana yazar. return ise sonucu çağıran yere geri verir, böylece onu bir değişkene koyup yeniden kullanırsın. Dikkat: return çalışınca fonksiyon orada biter.

**Ekranda başlık:** return: sonucu geri ver

**Kod** (vurgulanan satırlar: 2, 4):

```python
def add(a, b):
    return a + b

total = add(3, 4)
print(total * 2)
```

**Çıktı:**

```text
14
```

**Maskot:** isaret pozu, sag

## Sahne 5: kod (11 sn)

**Seslendirme:** Bir parametreye varsayılan değer verirsen, çağırırken o değeri yazmak zorunda kalmazsın. Miktar verilmezse yirmi kullanılır; verirsen seninki geçerli olur.

**Ekranda başlık:** Varsayılan değerler

**Kod** (vurgulanan satırlar: 1):

```python
def heal(hp, amount=20):
    return hp + amount

print(heal(50))
print(heal(50, 5))
```

**Çıktı:**

```text
70
55
```

**Maskot:** konusma pozu, sag

## Sahne 6: kod (11 sn)

**Seslendirme:** İstediğin kadar değer alan fonksiyonlar için yıldızlı parametre kullanılır. Gelen bütün sayılar bir tuple'da toplanır, biz de döngüyle hepsini toplarız.

**Ekranda başlık:** *args: istediğin kadar değer

**Kod** (vurgulanan satırlar: 1):

```python
def total(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result

print(total(1, 2, 3, 4))
```

**Çıktı:**

```text
10
```

**Maskot:** mutlu pozu, sag

## Sahne 7: hata (13 sn)

**Seslendirme:** En sık karışıklık: return yerine print yazmak. Fonksiyon yediyi ekrana yazar ama geri hiçbir şey vermez, yani None döner. None'ı ikiyle çarpamayınca TypeError geliyor.

**Ekranda başlık:** print mi, return mü?

**Kod** (vurgulanan satırlar: 2, 5):

```python
def add(a, b):
    print(a + b)

total = add(3, 4)
print(total * 2)
```

**Çıktı:**

```text
7
TypeError: unsupported operand type(s) for *: 'NoneType' and 'int'
```

**Maskot:** sasirma pozu, sag

## Sahne 8: soru (9 sn)

**Seslendirme:** Bir fonksiyonun sonucunu yine aynı fonksiyona verebilirsin. Sence bu kod ne yazdırır? Merhaba yazılır mı?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```python
def double(x):
    return x * 2
    print("Merhaba")

print(double(double(3)))
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (10 sn)

**Seslendirme:** On iki! İçteki çağrı altı verdi, dıştaki onu on ikiye çıkardı. Merhaba ise hiç yazılmadı, çünkü return çalışınca fonksiyon orada biter.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 2, 3):

```python
def double(x):
    return x * 2
    print("Merhaba")

print(double(double(3)))
```

**Çıktı:**

```text
12
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görevlerde bir selam fonksiyonu yazacak, dikdörtgenin alanını geri döndürecek ve saldırıya varsayılan hasar vereceksin. Sahne görevinde bir ordu fabrikası kuracaksın. Challenge'da en büyük skoru max kullanmadan bulacaksın.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Selam fonksiyonu
- Görev 2: Alan hesaplayıcı
- Görev 3: Varsayılan hasar
- Sahne görevi: Ordu fabrikası
- Challenge: En büyük skor

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (8 sn)

**Seslendirme:** Bugün kendi aletlerimizi yaptık: onlara malzeme verdik, sonuçlarını geri aldık ve varsayılan ayarlar ekledik.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- def ile tanımla, adıyla çağır
- Parametreler malzeme, return sonuç
- Varsayılan değer: amount=20; çok değer: *args

**Maskot:** on pozu, sag

## Sahne 12: kapanis (10 sn)

**Seslendirme:** İlk aletlerin hazır, tebrikler! Yarın atölyenin dev alet dolabını açıyoruz: başka ustaların yazdığı modüller. Zar atacak, rastgele olaylar üreteceğiz.

**Ekranda başlık:** Yarın: Modüller

**Görsel:** `gorseller/python/harita/atolye.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** Bu dersin interaktif hâli 30gunde.com.tr'de seni bekliyor. Kodunu tarayıcıda yaz, hemen çalıştır ve görevleri tamamla!

**Ekranda:** İnteraktif dersler için **30gunde.com.tr**

- Kodunu tarayıcıda yaz ve çalıştır
- Görevleri tamamla, rozet kazan
- 30 günde adım adım Python
