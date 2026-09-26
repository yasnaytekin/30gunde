# Video senaryosu: Gün 8, Dictionary

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~122 sn

Piko, Veri Ormanı'ndaki canlıların kimlik kartlarını sözlüklerle tutuyor: anahtarla değere ulaşmak, eklemek, değiştirmek, silmek, get() ile güvenli bakış ve iç içe veriler.

Ders metni: [gun-08.md](../gunler/gun-08.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | konusma (sag) |
| 2 | kod | 12 sn | isaret (sag) |
| 3 | kod | 12 sn | konusma (sag) |
| 4 | hata | 9 sn | sasirma (sag) |
| 5 | kod | 11 sn | mutlu (sag) |
| 6 | kod | 11 sn | isaret (sag) |
| 7 | kod | 10 sn | konusma (sag) |
| 8 | soru | 10 sn | dusunme (sag) |
| 9 | cikti | 9 sn | mutlu (sag) |
| 10 | gorev | 11 sn | isaret (sol) |
| 11 | ozet | 6 sn | on (sag) |
| 12 | kapanis | 9 sn | tebrik (orta) |

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Piko! Veri Ormanı'nda yaşayan her canlının bir kimlik kartı var: adı, canı, gücü. Bunları bir listede tutarsak hangisi hangisiydi karışır. Bugün Python'ın sözlükleriyle tanışıyoruz!

**Ekranda başlık:** Gün 8: Dictionary

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** konusma pozu, sag

## Sahne 2: kod (12 sn)

**Seslendirme:** Gerçek sözlükte kelimeye bakıp anlamını bulursun. Python sözlüğünde de anahtara bakıp değeri bulursun. Listede sıra numarası kullanırdık, sözlükte ise isim kullanıyoruz.

**Ekranda başlık:** Anahtar ve değer

**Kod** (vurgulanan satırlar: 1):

```python
player = {"name": "Piko", "hp": 100, "gold": 50}
print(player["name"])
print(player["gold"])
```

**Çıktı:**

```text
Piko
50
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: Kimlik kartı çizimi: sol sütunda anahtarlar, sağ sütunda değerler.*

## Sahne 3: kod (12 sn)

**Seslendirme:** Yeni bir anahtar eklemek için köşeli parantezle adını yazıp değer koyarsın. Aynı yolla bir değeri değiştirirsin. del ise anahtarı değeriyle birlikte siler.

**Ekranda başlık:** Ekle, değiştir, sil

**Kod** (vurgulanan satırlar: 2, 3, 4):

```python
player = {"name": "Piko", "hp": 100, "gold": 50}
player["level"] = 1
player["hp"] = player["hp"] - 10
del player["gold"]
print(player)
```

**Çıktı:**

```text
{'name': 'Piko', 'hp': 90, 'level': 1}
```

**Maskot:** konusma pozu, sag

## Sahne 4: hata (9 sn)

**Seslendirme:** Olmayan bir anahtarı sorarsan Python KeyError verir. Mesaj çok net: sözlükte shield diye bir anahtar yok.

**Ekranda başlık:** KeyError

**Kod** (vurgulanan satırlar: 2):

```python
player = {"name": "Piko", "hp": 100}
print(player["shield"])
```

**Çıktı:**

```text
KeyError: 'shield'
```

**Maskot:** sasirma pozu, sag

## Sahne 5: kod (11 sn)

**Seslendirme:** Kurtarıcımız get! Hata vermez. Anahtar varsa değerini, yoksa senin belirlediğin yedek değeri döndürür. Goblinin adı var ama kalkanı yok.

**Ekranda başlık:** Güvenli bakış: get()

**Kod** (vurgulanan satırlar: 3):

```python
enemy = {"name": "Goblin", "hp": 30}
print(enemy.get("name"))
print(enemy.get("shield", "Kalkanı yok!"))
```

**Çıktı:**

```text
Goblin
Kalkanı yok!
```

**Maskot:** mutlu pozu, sag

## Sahne 6: kod (11 sn)

**Seslendirme:** keys tüm anahtarları, values tüm değerleri verir. in bir anahtar var mı diye sorar, len de kaç anahtar olduğunu söyler.

**Ekranda başlık:** Sözlüğü incelemek

**Kod**:

```python
player = {"name": "Piko", "hp": 100}
print(player.keys())
print(player.values())
print("hp" in player, len(player))
```

**Çıktı:**

```text
dict_keys(['name', 'hp'])
dict_values(['Piko', 100])
True 2
```

**Maskot:** isaret pozu, sag

## Sahne 7: kod (10 sn)

**Seslendirme:** Değer olarak liste bile koyabilirsin. Kahramanın çantası artık kimlik kartının içinde! Çantaya append ile yeni bir eşya ekliyoruz.

**Ekranda başlık:** İç içe veriler

**Kod** (vurgulanan satırlar: 2):

```python
hero = {"name": "Piko", "inventory": ["kılıç", "iksir"]}
hero["inventory"].append("harita")
print(hero["inventory"])
print(len(hero["inventory"]), "eşya")
```

**Çıktı:**

```text
['kılıç', 'iksir', 'harita']
3 eşya
```

**Maskot:** konusma pozu, sag

## Sahne 8: soru (10 sn)

**Seslendirme:** Dikkatli bak! İkinci satır yeni bir anahtar mı ekliyor, yoksa başka bir şey mi yapıyor? Bu kod ne yazdırır?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```python
hero = {"name": "Piko", "hp": 100}
hero["hp"] = 80
print(len(hero), hero["hp"])
```

**Maskot:** dusunme pozu, sag

## Sahne 9: cikti (9 sn)

**Seslendirme:** İki ve seksen! hp anahtarı zaten vardı, bu yüzden yeni anahtar eklenmedi. Sadece değeri değişti.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 2):

```python
hero = {"name": "Piko", "hp": 100}
hero["hp"] = 80
print(len(hero), hero["hp"])
```

**Çıktı:**

```text
2 80
```

**Maskot:** mutlu pozu, sag

## Sahne 10: gorev (11 sn)

**Seslendirme:** Görevlerde oyuncuya altın ekleyecek, goblinin canını azaltacak ve kalkanı güvenle okuyacaksın. Challenge'da bir fiyat sözlüğüyle sepetin hesabını çıkaracaksın. Fiyatları elle yazmak yok!

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Altın ekle
- Görev 2: Hasar al
- Görev 3: Güvenli bakış
- Challenge: Market hesabı

**Maskot:** isaret pozu, sol

## Sahne 11: ozet (6 sn)

**Seslendirme:** Bugün bilgileri isimle sakladık, güncelledik ve hata almadan güvenle okumayı öğrendik.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- Sözlük: {anahtar: değer}, isimle ulaşılır
- sozluk[anahtar] = değer ekler ya da değiştirir
- get() ile hata olmadan bak; keys, values, in

**Maskot:** on pozu, sag

## Sahne 12: kapanis (9 sn)

**Seslendirme:** Veri Ormanı'nı tamamladın, tebrikler! Yarın Mantık Kalesi'ne varıyoruz. Kapısı sadece anahtarı olanlara açılan kalede programa karar vermeyi öğreteceğiz.

**Ekranda başlık:** Yarın: Koşullar

**Görsel:** `gorseller/python/harita/kale.webp`

**Maskot:** tebrik pozu, orta

*Yönetmen notu: Harita ormandan kaleye doğru kayar.*
