# Video senaryosu: Gün 1, Python ile tanışma

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~133 sn

Piko, Başlangıç Kampı'nda print() ile ekrana yazı yazmayı, Python'ı hesap makinesi gibi kullanmayı, yorumları ve ilk hata mesajını anlatıyor.

Ders metni: [gun-01.md](../gunler/gun-01.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | mutlu (sag) |
| 2 | anlatim | 10 sn | on (sol) |
| 3 | kod | 12 sn | isaret (sag) |
| 4 | kod | 12 sn | mutlu (sag) |
| 5 | kod | 12 sn | isaret (sag) |
| 6 | kod | 10 sn | mutlu (alt-sag) |
| 7 | hata | 14 sn | sasirma (sag) |
| 8 | soru | 8 sn | dusunme (sag) |
| 9 | cikti | 10 sn | mutlu (sag) |
| 10 | gorev | 14 sn | isaret (sol) |
| 11 | ozet | 10 sn | on (sag) |
| 12 | kapanis | 9 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Piko! Başlangıç Kampı'na hoş geldin. Bilgisayarlar çok hızlıdır ama ne yapacaklarını kendileri bilmez. Onlara ne yapacaklarını sen söyleyeceksin. Hazır mısın? Bugün bilgisayarla ilk kez konuşuyoruz!

**Ekranda başlık:** Gün 1: Python ile tanışma

**Görsel:** `gorseller/python/harita/kamp.webp`

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Harita üzerinde kamp bölgesine yakınlaşma; Piko kamp ateşinin yanından kafasını uzatır.*

## Sahne 2: anlatim (10 sn)

**Seslendirme:** Kod, bilgisayara verdiğin talimatların listesi. Python bu talimatları yukarıdan aşağıya, satır satır okur ve sırayla yapar. Oyunlarda, web sitelerinde, yapay zekâda hep Python var.

**Ekranda başlık:** Kod nedir?

**Ekranda maddeler:**

- Kod: bilgisayara verilen talimatlar
- Python yukarıdan aşağıya, satır satır okur
- Oyunlar, web siteleri, yapay zekâ

**Maskot:** on pozu, sol

## Sahne 3: kod (12 sn)

**Seslendirme:** İlk sihirli sözcüğümüz print. Parantezin içine ne koyarsan ekrana onu yazar. Yazıları tırnak içine alırız, sayıları almayız. Çalıştır'a basınca iki satır beliriyor.

**Ekranda başlık:** print() ile konuş

**Kod** (vurgulanan satırlar: 1, 2):

```python
print("Merhaba Dünya!")
print(42)
```

**Çıktı:**

```text
Merhaba Dünya!
42
```

**Maskot:** isaret pozu, sag

## Sahne 4: kod (12 sn)

**Seslendirme:** Python aynı zamanda kocaman bir hesap makinesi. Artı toplar, yıldız çarpar, iki yıldız da üs alır. İkinin onuncu kuvveti tam bin yirmi dört eder!

**Ekranda başlık:** Python bir hesap makinesi

**Kod** (vurgulanan satırlar: 3):

```python
print(3 + 4)
print(10 * 5)
print(2 ** 10)
```

**Çıktı:**

```text
7
50
1024
```

**Maskot:** mutlu pozu, sag

## Sahne 5: kod (12 sn)

**Seslendirme:** Kare işaretiyle başlayan satır bir yorum. Python onu okumaz, sen kendine not bırakırsın. Virgülle birden çok şeyi yan yana yazdırabilirsin; Python aralarına kendiliğinden boşluk koyar.

**Ekranda başlık:** Yorumlar ve virgül

**Kod** (vurgulanan satırlar: 1, 2):

```python
# Bu bir yorum, Python bunu okumaz
print("Piko", "diyor ki:", "Selam!")
print("Yaşım:", 12)
```

**Çıktı:**

```text
Piko diyor ki: Selam!
Yaşım: 12
```

**Maskot:** isaret pozu, sag

## Sahne 6: kod (10 sn)

**Seslendirme:** Bazı görevlerde yazdırdığın şey sahnede resme dönüşür. Her yıldız bir Piko, her kare işareti bir duvar olur. İşte beş Piko ve altında beş duvar!

**Ekranda başlık:** Sahnede çizim

**Kod**:

```python
print("*****")
print("#####")
```

**Çıktı:**

```text
*****
#####
```

**Maskot:** mutlu pozu, alt-sag

*Yönetmen notu: Çıktının yanında sahne ızgarası: yıldızlar Piko figürlerine, # işaretleri duvar karelerine dönüşür.*

## Sahne 7: hata (14 sn)

**Seslendirme:** Şimdi bir harfi unutalım. Python kırmızı bir mesajla NameError diyor: prin diye bir şey tanımıyorum. Hatta print'i mi demek istedin diye soruyor! Korkma, hata mesajı sorunun yerini gösterir. Harfi düzelt, tekrar çalıştır.

**Ekranda başlık:** İlk hatamız

**Kod** (vurgulanan satırlar: 1):

```python
prin("Merhaba!")
```

**Çıktı:**

```text
NameError: name 'prin' is not defined. Did you mean: 'print'?
```

**Maskot:** sasirma pozu, sag

*Yönetmen notu: Hata satırı kırmızı yanıp söner; eksik 't' harfi yerine yerleşince yeşile döner.*

## Sahne 8: soru (8 sn)

**Seslendirme:** Sıra sende. Sence bu iki satır aynı şeyi mi yazar? Bir saniye düşün...

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```python
print(3 + 4)
print("3 + 4")
```

**Maskot:** dusunme pozu, sag

*Yönetmen notu: Ekranda 3 saniyelik geri sayım.*

## Sahne 9: cikti (10 sn)

**Seslendirme:** Hayır! İlk satır hesaplar ve yedi yazar. İkinci satırdaki işlem tırnak içinde, yani bir yazı. Python onu hesaplamaz, olduğu gibi ekrana basar.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 2):

```python
print(3 + 4)
print("3 + 4")
```

**Çıktı:**

```text
7
3 + 4
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (14 sn)

**Seslendirme:** Şimdi sahne senin! Önce ekrana ilk sözünü yazdıracak, sonra kendini tanıtacaksın. Bir yılda kaç saat olduğunu da bulacaksın, ama hesabı sen yapma, Python'a yaptır. Sahne görevinde de kendi Piko ordunu dizeceksin.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: İlk sözün
- Görev 2: Kendini tanıt
- Görev 3: Bir yılda kaç saat?
- Sahne görevi: Piko ordusu
- Challenge: Yıldızlı afiş

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (10 sn)

**Seslendirme:** Bugün print ile ekrana yazdık, Python'a hesap yaptırdık, yorum bıraktık ve ilk hata mesajımızı okuduk. Fena değil, değil mi?

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- print() ekrana yazar; yazılar tırnak içinde
- + - * / ** ile hesap yapılır
- # ile yorum yazılır; hata mesajı yol gösterir

**Maskot:** on pozu, sag

## Sahne 12: kapanis (9 sn)

**Seslendirme:** İlk kodunu yazdın, tebrikler! Yarın bilgisayarın hafızasında etiketli kutular açacağız. Kahramanımızın adını ve canını bu kutularda saklayacağız. Görüşürüz!

**Ekranda başlık:** Yarın: Değişkenler

**Görsel:** `gorseller/python/rozetler/ilk-kod.webp`

**Maskot:** tebrik pozu, orta

*Yönetmen notu: İlk Kod rozeti ekrana süzülür, ardından kamp haritası yavaşça kararır.*
