# Video senaryosu: Gün 2, Değişkenler ve hazır fonksiyonlar

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~147 sn

Piko, kahramanın bilgilerini etiketli kutularda saklamayı anlatıyor: değişkenler, veri tipleri, input() ile girdi almak ve len, round, max gibi hazır fonksiyonlar.

Ders metni: [gun-02.md](../gunler/gun-02.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 11 sn | konusma (sag) |
| 2 | kod | 12 sn | isaret (sag) |
| 3 | anlatim | 12 sn | on (sol) |
| 4 | kod | 14 sn | konusma (sag) |
| 5 | kod | 10 sn | isaret (sag) |
| 6 | kod | 14 sn | konusma (sag) |
| 7 | kod | 12 sn | mutlu (sag) |
| 8 | hata | 14 sn | sasirma (sag) |
| 9 | soru | 8 sn | dusunme (sag) |
| 10 | cikti | 8 sn | mutlu (sag) |
| 11 | gorev | 14 sn | isaret (sol) |
| 12 | ozet | 8 sn | on (sag) |
| 13 | kapanis | 10 sn | tebrik (orta) |

## Sahne 1: acilis (11 sn)

**Seslendirme:** Selam, ben Piko! Hâlâ Başlangıç Kampı'ndayız. Oyunumuzun bir kahramanı olacak. Ama bilgisayar kahramanın adını, canını, altınını nasıl hatırlayacak? Bugün hafızada etiketli kutular açıyoruz!

**Ekranda başlık:** Gün 2: Değişkenler ve hazır fonksiyonlar

**Görsel:** `gorseller/python/harita/kamp.webp`

**Maskot:** konusma pozu, sag

## Sahne 2: kod (12 sn)

**Seslendirme:** Değişken, içine bilgi koyduğun etiketli bir kutu. Buradaki eşittir matematikteki eşittir değil: sağdaki değeri soldaki kutuya koy demek. Sonra kutunun adını yazarak içindekini kullanırsın.

**Ekranda başlık:** Değişken: etiketli bir kutu

**Kod** (vurgulanan satırlar: 1, 2):

```python
name = "Piko"
hp = 100
print(name)
print(hp)
```

**Çıktı:**

```text
Piko
100
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: İki karton kutu belirir; üzerlerinde name ve hp etiketleri, içlerine değerler düşer.*

## Sahne 3: anlatim (12 sn)

**Seslendirme:** Kutulara isim verirken birkaç kural var. İsim harfle ya da alt çizgiyle başlar, boşluk içermez. Büyük ve küçük harf fark eder. En önemlisi de anlamlı isimler seçmek.

**Ekranda başlık:** İsim verme kuralları

**Ekranda maddeler:**

- Harfle ya da _ ile başla: score
- Boşluk yok, _ kullan: player_name
- Score ile score ayrı kutular
- Anlamlı isim seç: x yerine gold

**Maskot:** on pozu, sol

## Sahne 4: kod (14 sn)

**Seslendirme:** Kutulara farklı türde bilgiler girer. Yazıya str, tam sayıya int, ondalıklı sayıya float, doğru ya da yanlışa bool deriz. Bir değerin tipini merak edersen type fonksiyonuna sorman yeter.

**Ekranda başlık:** Veri tipleri

**Kod** (vurgulanan satırlar: 6, 7):

```python
name = "Piko"
hp = 100
speed = 2.5
is_alive = True
print(name, hp, speed, is_alive)
print(type(name))
print(type(hp))
```

**Çıktı:**

```text
Piko 100 2.5 True
<class 'str'>
<class 'int'>
```

**Maskot:** konusma pozu, sag

## Sahne 5: kod (10 sn)

**Seslendirme:** Kutuya yeni bir değer koyunca eskisinin yerine geçer. Üçüncü satır şunu der: altının şimdiki değerini al, yirmi beş ekle, sonucu aynı kutuya geri koy.

**Ekranda başlık:** Kutunun içini değiştirmek

**Kod** (vurgulanan satırlar: 3):

```python
gold = 10
print("Başta:", gold)
gold = gold + 25
print("Hazineden sonra:", gold)
```

**Çıktı:**

```text
Başta: 10
Hazineden sonra: 35
```

**Maskot:** isaret pozu, sag

## Sahne 6: kod (14 sn)

**Seslendirme:** input ile kullanıcıya soru sorarsın. Gelen cevap her zaman yazıdır. Sayı lazımsa int ile çevirirsin. Bu sitede cevaplarını editörün altındaki Girdi kutusuna yazıyorsun; her satır bir cevap.

**Ekranda başlık:** Kullanıcıdan bilgi almak

**Kod** (vurgulanan satırlar: 1, 3):

```python
name = input("Adın ne? ")
print("Merhaba", name)
age = int(input("Kaç yaşındasın? "))
```

**Çıktı:**

```text
Adın ne? Ece
Merhaba Ece
Kaç yaşındasın? 12
```

**Maskot:** konusma pozu, sag

*Yönetmen notu: Girdi kutusuna 'Ece' ve '12' yazılırken gösterilir.*

## Sahne 7: kod (12 sn)

**Seslendirme:** Python'ın içinde kullanıma hazır fonksiyonlar gelir. len uzunluğu ölçer, float yazıyı ondalıklı sayıya çevirir, round yuvarlar, max ve min de en büyüğü ve en küçüğü bulur.

**Ekranda başlık:** Hazır fonksiyonlar

**Kod**:

```python
name = "Piko"
print(len(name))
print(float("2.5") + 1)
print(round(7.6))
print(max(3, 9, 4), min(3, 9, 4))
```

**Çıktı:**

```text
4
3.5
8
9 3
```

**Maskot:** mutlu pozu, sag

## Sahne 8: hata (14 sn)

**Seslendirme:** En sık hata: yazı ile sayıyı toplamaya çalışmak. Tırnak içindeki on iki bir yazı, bir ise sayı. Python TypeError diyor: yazıya sadece yazı eklenebilir. Bunu nasıl düzelteceğini Tip dedektifi görevinde sen bulacaksın.

**Ekranda başlık:** Yazı + sayı = hata

**Kod** (vurgulanan satırlar: 2):

```python
age = "12"
print(age + 1)
```

**Çıktı:**

```text
TypeError: can only concatenate str (not "int") to str
```

**Maskot:** sasirma pozu, sag

## Sahne 9: soru (8 sn)

**Seslendirme:** Hadi bakalım. Sence bu kod ne yazdırır? On mu, beş mi, yoksa başka bir şey mi?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```python
gold = 10
gold = gold + 5
print(gold)
```

**Maskot:** dusunme pozu, sag

## Sahne 10: cikti (8 sn)

**Seslendirme:** On beş! Önce kutuda on vardı. İkinci satır ona beş ekledi ve sonucu aynı kutuya geri koydu.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 2):

```python
gold = 10
gold = gold + 5
print(gold)
```

**Çıktı:**

```text
15
```

**Maskot:** mutlu pozu, sag

## Sahne 11: gorev (14 sn)

**Seslendirme:** Görev zamanı! Önce kutuya kendi adını koyacaksın. Sonra üç değişkenle bir kahraman kartı hazırlayacaksın. Tip dedektifi görevinde hata veren bir kodu kurtaracaksın. Challenge'da da iki kutunun içeriğini yer değiştireceksin.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Kutuyu doldur
- Görev 2: Kahraman kartı
- Görev 3: Tip dedektifi
- Sahne görevi: Değişkenli ordu
- Challenge: Kutuları değiştir

**Maskot:** isaret pozu, sol

## Sahne 12: ozet (8 sn)

**Seslendirme:** Bugün kutular açtık, içlerine farklı tipte bilgiler koyduk. Kullanıcıdan bilgi aldık ve hazır fonksiyonlarla iş gördük.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- Değişken = etiketli kutu; = sağdakini sola koyar
- Tipler: str, int, float, bool; type() ile bak
- input() hep yazı verir; int() ile sayıya çevir

**Maskot:** on pozu, sag

## Sahne 13: kapanis (10 sn)

**Seslendirme:** Kamptaki eğitimin bitti, tebrikler! Yarın Python Köyü'ne gidiyoruz. Köyün pazarında operatörlerle hesap yapacak, doğru mu yanlış mı diye sorular soracağız.

**Ekranda başlık:** Yarın: Operatörler

**Görsel:** `gorseller/python/harita/koy.webp`

**Maskot:** tebrik pozu, orta

*Yönetmen notu: Harita kamptan köye doğru kayar.*
