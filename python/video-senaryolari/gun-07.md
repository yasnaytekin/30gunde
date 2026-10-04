# Video senaryosu: Gün 7, Set'ler

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~118 sn

Piko, Veri Ormanı'nda gezdiği yerleri tekrarsız tutmak için set'leri kullanıyor: tekrarları atmak, eleman eklemek ve çıkarmak, birleşim, kesişim ve fark işlemleri.

Ders metni: [gun-07.md](../gunler/gun-07.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | konusma (sag) |
| 2 | kod | 14 sn | isaret (sag) |
| 3 | kod | 10 sn | mutlu (sag) |
| 4 | kod | 14 sn | konusma (sag) |
| 5 | hata | 12 sn | uzgun (sag) |
| 6 | kod | 13 sn | isaret (sag) |
| 7 | soru | 8 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 11 sn | isaret (sol) |
| 10 | ozet | 7 sn | on (sag) |
| 11 | kapanis | 7 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Gün 7: Set'ler! Bu derste tekrarları kendiliğinden atan set'leri, eleman eklemeyi ve çıkarmayı, birleşim, kesişim ve fark işlemlerini öğreneceksin.

- Set: tekrarsız koleksiyon
- add, discard, remove
- Birleşim, kesişim, fark

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Piko! Ormanda dolaşırken aynı yerlerden defalarca geçtim. Her geçişi haritaya yazarsam sayfa dolacak! Aslında bana sadece hangi yerleri gördüğüm lazım. Bugün tekrarları kendiliğinden atan set'lerle tanışıyoruz.

**Ekranda başlık:** Gün 7: Set'ler

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** konusma pozu, sag

## Sahne 2: kod (14 sn)

**Seslendirme:** Set süslü parantezle yazılır ve içinde aynı eleman iki kez bulunamaz. Kampı iki kez yazdık ama set bir tane tuttu. Set'in sırası yoktur; düzenli görmek istersen sorted kullan.

**Ekranda başlık:** Set nedir?

**Kod** (vurgulanan satırlar: 1):

```python
places = {"kamp", "köy", "kamp"}
print(len(places))
print(sorted(places))
```

**Çıktı:**

```text
2
['kamp', 'köy']
```

**Maskot:** isaret pozu, sag

## Sahne 3: kod (10 sn)

**Seslendirme:** Bir listeyi set içine koyarsan tekrarlar kaybolur. Beş renk yazılmış ama aslında sadece üç farklı renk var.

**Ekranda başlık:** Listeden tekrarları atmak

**Kod** (vurgulanan satırlar: 2):

```python
colors = ["mavi", "sarı", "mavi", "yeşil", "sarı"]
unique = set(colors)
print(len(colors), "renk yazıldı")
print(len(unique), "farklı renk")
print(sorted(unique))
```

**Çıktı:**

```text
5 renk yazıldı
3 farklı renk
['mavi', 'sarı', 'yeşil']
```

**Maskot:** mutlu pozu, sag

## Sahne 4: kod (14 sn)

**Seslendirme:** add bir eleman ekler. İksiri iki kez eklemeye çalıştık ama set'te hâlâ bir tane var. discard siler, eleman yoksa sessizce geçer. in ile sormak da set'lerde çok hızlıdır.

**Ekranda başlık:** Ekle ve çıkar

**Kod** (vurgulanan satırlar: 2, 3, 4):

```python
bag = {"kılıç", "iksir"}
bag.add("harita")
bag.add("iksir")
bag.discard("kılıç")
print(sorted(bag))
print("iksir" in bag)
```

**Çıktı:**

```text
['harita', 'iksir']
True
```

**Maskot:** konusma pozu, sag

## Sahne 5: hata (12 sn)

**Seslendirme:** remove da siler ama olmayan bir elemanı silmeye çalışırsan KeyError verir: çantada kalkan yok! Emin değilsen discard kullan, o hiç şikâyet etmez.

**Ekranda başlık:** remove ve KeyError

**Kod** (vurgulanan satırlar: 2):

```python
bag = {"kılıç", "iksir"}
bag.remove("kalkan")
```

**Çıktı:**

```text
KeyError: 'kalkan'
```

**Maskot:** uzgun pozu, sag

## Sahne 6: kod (13 sn)

**Seslendirme:** Matematikteki kümeler gibi iki set'i karşılaştırabilirsin. Dikey çizgi birleşim, ve işareti kesişim, eksi ise fark verir. Ece ile ikimizin de gezdiği yerler kale ve köy.

**Ekranda başlık:** Küme işlemleri

**Kod** (vurgulanan satırlar: 3, 4, 5):

```python
piko = {"orman", "köy", "kale"}
ece = {"köy", "kale", "liman"}
print("İkisi de:", sorted(piko & ece))
print("Hepsi:", sorted(piko | ece))
print("Sadece Piko:", sorted(piko - ece))
```

**Çıktı:**

```text
İkisi de: ['kale', 'köy']
Hepsi: ['kale', 'köy', 'liman', 'orman']
Sadece Piko: ['orman']
```

**Maskot:** isaret pozu, sag

*Yönetmen notu: İki kesişen daire: ortak bölgede kale ve köy parlar.*

## Sahne 7: soru (8 sn)

**Seslendirme:** Boş bir set yapmak istiyoruz. İki yol denedik. Sence ikisinin tipi ne çıkar?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```python
a = {}
b = set()
print(type(a))
print(type(b))
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Süslü parantezin boşu set değil, boş bir sözlük! Boş set için set yazmalısın. Sözlükle de yarın tanışacağız.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 2):

```python
a = {}
b = set()
print(type(a))
print(type(b))
```

**Çıktı:**

```text
<class 'dict'>
<class 'set'>
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (11 sn)

**Seslendirme:** Görevlerde ziyaret listesindeki tekrarları silecek, haritana yeni bir yer ekleyecek ve iki arkadaşın ortak oyunlarını bulacaksın. Challenge'da da henüz kazanılmamış rozetlerin peşine düşeceksin.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Tekrarları sil
- Görev 2: Yeni yer keşfet
- Görev 3: Ortak oyunlar
- Challenge: Eksik rozetler

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (7 sn)

**Seslendirme:** Bugün tekrarları kendiliğinden atan koleksiyonları ve iki set'i karşılaştıran küme işlemlerini öğrendik.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- Set: tekrarsız ve sırasız; boş set = set()
- add, discard, remove ve hızlı in
- | birleşim, & kesişim, - fark

**Maskot:** on pozu, sag

## Sahne 11: kapanis (7 sn)

**Seslendirme:** Haritan tertemiz! Yarın ormandaki canlıların kimlik kartlarını hazırlayacağız: anahtar ve değerlerle çalışan sözlükler.

**Ekranda başlık:** Yarın: Dictionary

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** Bu dersin interaktif hâli 30gunde.com.tr'de seni bekliyor. Kodunu tarayıcıda yaz, hemen çalıştır ve görevleri tamamla!

**Ekranda:** İnteraktif dersler için **30gunde.com.tr**

- Kodunu tarayıcıda yaz ve çalıştır
- Görevleri tamamla, rozet kazan
- 30 günde adım adım Python
