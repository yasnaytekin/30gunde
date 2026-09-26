# Video senaryosu: Gün 17, Hata yönetimi

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~147 sn

Piko, Keşif Adası'nın çürük köprülerinde try, except, else ve finally ile hataları yakalamayı, raise ile de kendi hatasını fırlatmayı gösteriyor.

Ders metni: [gun-17.md](../gunler/gun-17.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 13 sn | konusma (sag) |
| 2 | hata | 11 sn | uzgun (sag) |
| 3 | kod | 15 sn | isaret (sag) |
| 4 | kod | 15 sn | isaret (sol) |
| 5 | anlatim | 10 sn | dusunme (sag) |
| 6 | kod | 14 sn | konusma (sag) |
| 7 | kod | 15 sn | isaret (sol) |
| 8 | soru | 9 sn | dusunme (sag) |
| 9 | cikti | 9 sn | mutlu (sol) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 12 sn | tebrik (orta) |

## Sahne 1: acilis (13 sn)

**Seslendirme:** Selam, ben Piko! Keşif Adası'nda köprüler çürük olabilir. Akıllı bir kaşif her adımda beline bir ip bağlar. Peki programın bir hataya çarpınca çökmek yerine ipe tutunabilir mi? Evet! Bugün hata yönetimini öğreniyoruz.

**Ekranda başlık:** Gün 17: Hata yönetimi

**Ekranda maddeler:**

- Keşif Adası
- try, except, else, finally, raise

**Maskot:** konusma pozu, sag

*Yönetmen notu: Arka plan: Keşif Adası bölge görseli (gorseller/python/harita/ada.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Sallanan bir ip köprü ve beline ip bağlamış Piko.*

## Sahne 2: hata (11 sn)

**Seslendirme:** Önce ipsiz hâlini görelim. Yazıyla yazılmış on iki sayısını int ile sayıya çevirmeye çalışıyorum. Python ValueError verip programı olduğu yerde durduruyor.

**Ekranda başlık:** İpsiz geçiş: program çöker

**Kod** (vurgulanan satırlar: 2):

```python
text = "on iki"
age = int(text)
print("Yaşın:", age)
```

**Çıktı:**

```text
ValueError: invalid literal for int() with base 10: 'on iki'
```

**Maskot:** uzgun pozu, sag

## Sahne 3: kod (15 sn)

**Seslendirme:** Şimdi ipi bağlıyorum. Hata çıkabilecek kodu try içine, hata olursa yapılacak işi except içine yazıyorum. Çevirme başarısız olunca except çalışıyor ve program çökmeden yoluna devam ediyor.

**Ekranda başlık:** try ve except

**Kod** (vurgulanan satırlar: 2, 5):

```python
text = "on iki"
try:
    age = int(text)
    print("Yaşın:", age)
except ValueError:
    print("Lütfen rakamla yaz.")
print("Program devam ediyor.")
```

**Çıktı:**

```text
Lütfen rakamla yaz.
Program devam ediyor.
```

**Maskot:** isaret pozu, sag

## Sahne 4: kod (15 sn)

**Seslendirme:** Her hatanın bir adı var. Burada iki ayrı except yazdım: sayı olmayan yazı için ValueError, sıfıra bölme için ZeroDivisionError. Her birine kendi cevabını veriyorum.

**Ekranda başlık:** Hangi hatayı yakalıyorsun?

**Kod** (vurgulanan satırlar: 4, 6):

```python
for text in ["5", "0", "beş"]:
    try:
        print(100 / int(text))
    except ValueError:
        print("Sayı değil!")
    except ZeroDivisionError:
        print("Sıfıra bölünmez!")
```

**Çıktı:**

```text
20.0
Sıfıra bölünmez!
Sayı değil!
```

**Maskot:** isaret pozu, sol

## Sahne 5: anlatim (10 sn)

**Seslendirme:** Bir uyarı: sadece except yazıp her hatayı yakalamak kolaydır ama gerçek hataları da gizler. Beklediğin hatanın adını mutlaka yaz.

**Ekranda başlık:** İpucu

**Ekranda maddeler:**

- except: her şeyi yakalar, hataları saklar
- except ValueError: sadece beklediğini yakalar
- Mesajı görmek için: except ValueError as err

**Maskot:** dusunme pozu, sag

## Sahne 6: kod (14 sn)

**Seslendirme:** İki yardımcı daha var. else, hiç hata olmazsa çalışır. finally ise hata olsa da olmasa da her zaman çalışır; kapanış işleri için birebir.

**Ekranda başlık:** else ve finally

**Kod** (vurgulanan satırlar: 5, 7):

```python
try:
    n = int("5")
except ValueError:
    print("Hata!")
else:
    print("Başarılı:", n)
finally:
    print("Kontrol bitti.")
```

**Çıktı:**

```text
Başarılı: 5
Kontrol bitti.
```

**Maskot:** konusma pozu, sag

## Sahne 7: kod (15 sn)

**Seslendirme:** Bazen hatayı biz bilerek fırlatırız. set_hp fonksiyonu negatif bir can gelirse raise ile ValueError fırlatıyor. Dışarıda yakalayıp as err ile mesajını ekrana yazıyorum.

**Ekranda başlık:** raise: kendi hatanı fırlat

**Kod** (vurgulanan satırlar: 3, 8):

```python
def set_hp(value):
    if value < 0:
        raise ValueError("Can negatif olamaz")
    return value

try:
    set_hp(-5)
except ValueError as err:
    print("Yakalandı:", err)
```

**Çıktı:**

```text
Yakalandı: Can negatif olamaz
```

**Maskot:** isaret pozu, sol

## Sahne 8: soru (9 sn)

**Seslendirme:** Mini soru! Burada hata yok, sayı sorunsuz çevriliyor. Sence ekranda hangi satırlar görünür?

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```python
try:
    n = int("7")
except ValueError:
    print("Hata!")
else:
    print("Sayı:", n)
finally:
    print("Bitti.")
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (9 sn)

**Seslendirme:** Hata olmadığı için except atlandı, else çalıştı. finally ise her zamanki gibi en sonda geldi.

**Ekranda başlık:** Cevap

**Kod**:

```python
try:
    n = int("7")
except ValueError:
    print("Hata!")
else:
    print("Sayı:", n)
finally:
    print("Bitti.")
```

**Çıktı:**

```text
Sayı: 7
Bitti.
```

**Maskot:** mutlu pozu, sol

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görevlerin hazır! Çökmeyen bir sayı çevirici, try kullanan güvenli bir bölme ve yaşını soran bir program yazacaksın. Projede de oyuncunun yanlış yazdığı komutlar oyunu bozmayacak.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Güvenli sayı
- Görev 2: Güvenli bölme
- Görev 3: Yaşını sor
- Challenge: raise ile koru
- Proje: Sağlam komutlar

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** Özetle: try ile dene, except ile yakala, else ve finally ile toparla, gerekirse raise ile kendin uyar.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- try içindeki hata except ile yakalanır
- else hata yoksa, finally her zaman çalışır
- raise ile anlaşılır bir hata fırlatırsın

**Maskot:** on pozu, sag

## Sahne 12: kapanis (12 sn)

**Seslendirme:** Süpersin! Yarın adanın mağarasına giriyoruz. Duvarlarda gizli sayılar ve şifreler var. Onları bulmak için Python'ın büyütecini, düzenli ifadeleri kullanacağız. Görüşürüz!

**Ekranda başlık:** Yarın: Düzenli ifadeler

**Ekranda maddeler:**

- re modülü
- Metinde desen aramak

**Maskot:** tebrik pozu, orta
