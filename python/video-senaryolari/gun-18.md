# Video senaryosu: Gün 18, Düzenli ifadeler

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~152 sn

Piko, Keşif Adası'nın yazılı mağarasında re modülüyle desen kurmayı; findall, search, fullmatch, sub ve gruplarla metinden bilgi çekmeyi anlatıyor.

Ders metni: [gun-18.md](../gunler/gun-18.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 13 sn | sasirma (sag) |
| 2 | anlatim | 13 sn | konusma (sag) |
| 3 | anlatim | 15 sn | isaret (sol) |
| 4 | kod | 14 sn | isaret (sag) |
| 5 | kod | 14 sn | isaret (sol) |
| 6 | kod | 16 sn | konusma (sag) |
| 7 | hata | 12 sn | uzgun (sag) |
| 8 | soru | 10 sn | dusunme (sag) |
| 9 | cikti | 9 sn | mutlu (sol) |
| 10 | gorev | 13 sn | konusma (sag) |
| 11 | ozet | 11 sn | on (sag) |
| 12 | kapanis | 12 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Gün 18: Düzenli ifadeler! Bu derste re modülüyle metinlerde desen aramayı; findall, search ve sub ile bilgi bulmayı ve değiştirmeyi öğreneceksin.

- Desen nedir?
- findall, search, sub
- Gruplarla parçalamak

## Sahne 1: acilis (13 sn)

**Seslendirme:** Selam, ben Piko! Keşif Adası'nın mağarasındayız. Duvarlar yazılarla dolu, bir yerlerde gizli sayılar ve şifreler saklı. Hepsini tek tek okumak günler sürer! Neyse ki Python'ın bir büyüteci var: düzenli ifadeler.

**Ekranda başlık:** Gün 18: Düzenli ifadeler

**Ekranda maddeler:**

- Keşif Adası
- re modülü (regex)

**Maskot:** sasirma pozu, sag

*Yönetmen notu: Arka plan: Keşif Adası bölge görseli (gorseller/python/harita/ada.webp). Dosya repoda henüz yok; eklenince ekran.gorsel alanına yazılmalı. Mağara duvarında yazılar, Piko elinde büyüteçle.*

## Sahne 2: anlatim (13 sn)

**Seslendirme:** Düzenli ifade, aradığın şeyin tarifidir. Yan yana rakamlar ya da içinde e harfi olan kelime gibi. Tarifi sen yazarsın, re modülü onu metnin içinde bulur.

**Ekranda başlık:** Desen nedir?

**Ekranda maddeler:**

- Desen = aradığın şeyin tarifi
- import re
- Desenin başına r koy: r"..."

**Maskot:** konusma pozu, sag

## Sahne 3: anlatim (15 sn)

**Seslendirme:** Tarif yazarken özel karakterler kullanırız. Ters eğik çizgi d bir rakam, ters eğik çizgi w bir harf ya da rakam demek. Artı işareti bir ya da daha fazla, süslü parantezdeki sayı ise tam kaç tane olduğunu söyler.

**Ekranda başlık:** Özel karakterler

**Ekranda maddeler:**

- \d rakam, \w harf/rakam, \s boşluk
- . herhangi bir karakter
- + bir ya da daha fazla, * sıfır ya da daha fazla
- {3} tam 3 tane, [0-9] aralık
- ^ başlangıç, $ son

**Maskot:** isaret pozu, sol

## Sahne 4: kod (14 sn)

**Seslendirme:** findall eşleşen her parçayı liste olarak verir. Artılı desen yan yana rakamları tek parça sayıyor, on iki bir bütün. Artısız desen ise her rakamı ayrı ayrı topluyor.

**Ekranda başlık:** Sayıları bul: findall

**Kod** (vurgulanan satırlar: 4, 5):

```python
import re

text = "Piko 3 elma, 12 altın ve 7 iksir buldu"
print(re.findall(r"\d+", text))
print(re.findall(r"\d", text))
```

**Çıktı:**

```text
['3', '12', '7']
['3', '1', '2', '7']
```

**Maskot:** isaret pozu, sag

## Sahne 5: kod (14 sn)

**Seslendirme:** search ilk eşleşmeyi bulur; burada ilk dört yan yana rakam, yani şifre. sub ise eşleşen her şeyi değiştirir. Tüm rakamları yıldıza çevirip bilgileri gizledim.

**Ekranda başlık:** Ara ve değiştir: search, sub

**Kod** (vurgulanan satırlar: 4, 5):

```python
import re

msg = "Şifrem 4821, telefonum 05321234567"
print(re.search(r"\d{4}", msg).group())
print(re.sub(r"\d", "*", msg))
```

**Çıktı:**

```text
4821
Şifrem ****, telefonum ***********
```

**Maskot:** isaret pozu, sol

## Sahne 6: kod (16 sn)

**Seslendirme:** Parantezler deseni gruplara ayırır. İlk grup ismi, ikinci grup sayıyı yakalıyor ve group ile alıyorum. Desene uymayan satırda search None veriyor, if de bunu yakalıyor.

**Ekranda başlık:** Gruplarla parçala

**Kod** (vurgulanan satırlar: 4, 6):

```python
import re

for line in ["Ece 45 altın", "Can 7 altın", "yanlış satır"]:
    m = re.search(r"(\w+) (\d+) altın", line)
    if m:
        print(m.group(1), "->", int(m.group(2)))
    else:
        print("Eşleşme yok:", line)
```

**Çıktı:**

```text
Ece -> 45
Can -> 7
Eşleşme yok: yanlış satır
```

**Maskot:** konusma pozu, sag

## Sahne 7: hata (12 sn)

**Seslendirme:** En sık hata şu: eşleşme yokken doğrudan group çağırmak. search bir şey bulamazsa None döner ve None'ın group'u olmadığı için AttributeError alırsın. Önce if m ile kontrol et!

**Ekranda başlık:** Sık hata: None.group()

**Kod** (vurgulanan satırlar: 4):

```python
import re

m = re.search(r"\d+", "burada sayı yok")
print(m.group())
```

**Çıktı:**

```text
AttributeError: 'NoneType' object has no attribute 'group'
```

**Maskot:** uzgun pozu, sag

## Sahne 8: soru (10 sn)

**Seslendirme:** Sıra sende! fullmatch metnin tamamı desene uyuyor mu diye bakar. Desen tam üç rakam istiyor. Sence iki satır ne yazdırır?

**Ekranda başlık:** Sence ne yazdırır?

**Kod**:

```python
import re

print(bool(re.fullmatch(r"\d{3}", "123")))
print(bool(re.fullmatch(r"\d{3}", "1234")))
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (9 sn)

**Seslendirme:** İlki True, çünkü tam üç rakam. İkincisi False: dört rakam var ve fullmatch fazlasını kabul etmez.

**Ekranda başlık:** Cevap

**Kod**:

```python
import re

print(bool(re.fullmatch(r"\d{3}", "123")))
print(bool(re.fullmatch(r"\d{3}", "1234")))
```

**Çıktı:**

```text
True
False
```

**Maskot:** mutlu pozu, sol

## Sahne 10: gorev (13 sn)

**Seslendirme:** Görevlerde metindeki sayıları bulup toplayacak, bir e-posta adresi arayacak ve şifreyi gizleyeceksin. Projede de git kuzey üç gibi komutları çözen bir fonksiyon yazıyorsun.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Sayıları topla
- Görev 2: E-posta var mı?
- Görev 3: Şifreyi gizle
- Challenge: Telefon numarası
- Proje: Komut çözücü

**Maskot:** konusma pozu, sag

## Sahne 11: ozet (11 sn)

**Seslendirme:** Özetle: deseni tarif et, findall ile hepsini bul, search ile ilkini yakala, sub ile değiştir.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- \d, \w, +, {n} ile desen kurulur
- findall, search, fullmatch, sub
- Parantezli gruplar group(1), group(2) ile alınır

**Maskot:** on pozu, sag

## Sahne 12: kapanis (12 sn)

**Seslendirme:** Mağaranın şifrelerini çözdük, tebrikler! Yarın bulduklarımızı kaybetmemek için dosyalara yazmayı ve JSON ile oyunu kaydetmeyi öğreneceğiz. Görüşürüz!

**Ekranda başlık:** Yarın: Dosya işlemleri

**Ekranda maddeler:**

- Dosyaya yaz, dosyadan oku
- JSON ile kaydet

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** Bu dersin interaktif hâli 30gunde.com.tr'de seni bekliyor. Kodunu tarayıcıda yaz, hemen çalıştır ve görevleri tamamla!

**Ekranda:** İnteraktif dersler için **30gunde.com.tr**

- Kodunu tarayıcıda yaz ve çalıştır
- Görevleri tamamla, rozet kazan
- 30 günde adım adım Python
