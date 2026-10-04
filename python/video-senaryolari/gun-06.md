# Video senaryosu: Gün 6, Tuple'lar

**Kurs:** 30 Günde Python  ·  **Maskot:** Piko  ·  **Süre:** ~124 sn

Piko, Veri Ormanı'ndaki mühürlü koordinatlar üzerinden tuple'ları anlatıyor: oluşturmak, neden değiştirilemediğini görmek, listeye çevirmek, açmak ve tek elemanlı tuple tuzağı.

Ders metni: [gun-06.md](../gunler/gun-06.md)

| # | Tür | Süre | Maskot |
|---|---|---|---|
| 1 | acilis | 12 sn | mutlu (sag) |
| 2 | kod | 12 sn | isaret (sag) |
| 3 | hata | 14 sn | sasirma (sag) |
| 4 | kod | 14 sn | konusma (sag) |
| 5 | kod | 12 sn | isaret (sag) |
| 6 | kod | 12 sn | konusma (sag) |
| 7 | soru | 10 sn | dusunme (sag) |
| 8 | cikti | 10 sn | mutlu (sag) |
| 9 | gorev | 14 sn | isaret (sol) |
| 10 | ozet | 6 sn | on (sag) |
| 11 | kapanis | 8 sn | tebrik (orta) |

## Giriş (konu tanıtımı)

**Seslendirme:** Gün 6: Tuple'lar! Bu derste değiştirilemeyen mühürlü kutuları, onları açmayı ve tek elemanlı tuple tuzağını öğreneceksin.

- Tuple nedir, neden değişmez?
- list() ve tuple() ile dönüştürme
- Tuple açmak: x, y = pos

## Sahne 1: acilis (12 sn)

**Seslendirme:** Selam, ben Piko! Veri Ormanı'nın ağaçlarına eski kaşifler işaretler kazımış: üç virgül beş, sekiz virgül iki. Bunlar gizli yerlerin koordinatları ve kimse onları değiştiremez. Bugün mühürlü kutuları, yani tuple'ları açıyoruz!

**Ekranda başlık:** Gün 6: Tuple'lar

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** mutlu pozu, sag

*Yönetmen notu: Ağaç kabuklarında (3, 5) ve (8, 2) işaretleri parlar.*

## Sahne 2: kod (12 sn)

**Seslendirme:** Tuple listeye çok benzer ama parantezle yazılır. Elemanlara yine sıra numarasıyla ulaşırsın, len de çalışır. Peki farkı ne? Bir kez oluşturulduktan sonra değiştirilemez.

**Ekranda başlık:** Tuple nedir?

**Kod** (vurgulanan satırlar: 1):

```python
colors = ("mavi", "sarı", "yeşil")
print(colors[0])
print(colors[-1])
print(len(colors))
```

**Çıktı:**

```text
mavi
yeşil
3
```

**Maskot:** isaret pozu, sag

## Sahne 3: hata (14 sn)

**Seslendirme:** Mührü kırmayı deneyelim. Python TypeError veriyor: tuple eleman değiştirmeye izin vermez. Bu bir özellik! Haritadaki koordinatlar, haftanın günleri gibi hiç değişmemesi gereken bilgileri kazara bozmamızı engeller.

**Ekranda başlık:** Mühür kırılmaz

**Kod** (vurgulanan satırlar: 2):

```python
colors = ("mavi", "sarı", "yeşil")
colors[0] = "kırmızı"
```

**Çıktı:**

```text
TypeError: 'tuple' object does not support item assignment
```

**Maskot:** sasirma pozu, sag

## Sahne 4: kod (14 sn)

**Seslendirme:** Yine de değiştirmen gerekirse bir yolu var. list ile kilidi açarsın, listeyi değiştirirsin, sonra tuple ile yeniden mühürlersin. Yani tuple'ı değiştirmenin tek yolu yeni bir tuple yapmak.

**Ekranda başlık:** Kilidi aç, değiştir, kilitle

**Kod** (vurgulanan satırlar: 2, 4):

```python
colors = ("mavi", "sarı")
items = list(colors)
items.append("yeşil")
colors = tuple(items)
print(colors)
print(type(colors))
```

**Çıktı:**

```text
('mavi', 'sarı', 'yeşil')
<class 'tuple'>
```

**Maskot:** konusma pozu, sag

## Sahne 5: kod (12 sn)

**Seslendirme:** Tuple'daki değerleri tek satırda ayrı değişkenlere dağıtabilirsin. Buna açma denir. Soldaki iki isim, sağdaki iki değeri sırayla alır: x üç, y beş olur.

**Ekranda başlık:** Tuple açmak

**Kod** (vurgulanan satırlar: 2):

```python
pos = (3, 5)
x, y = pos
print("x =", x)
print("y =", y)
```

**Çıktı:**

```text
x = 3
y = 5
```

**Maskot:** isaret pozu, sag

## Sahne 6: kod (12 sn)

**Seslendirme:** Tuple'ların faydalı aletleri de var. in var mı diye sorar, index kaçıncı sırada olduğunu söyler. İki tuple'ı artıyla toplarsan yepyeni bir tuple elde edersin.

**Ekranda başlık:** Faydalı işlemler

**Kod**:

```python
colors = ("mavi", "sarı", "yeşil")
print("sarı" in colors)
print(colors.index("sarı"))
print((1, 2) + (3, 4))
```

**Çıktı:**

```text
True
1
(1, 2, 3, 4)
```

**Maskot:** konusma pozu, sag

## Sahne 7: soru (10 sn)

**Seslendirme:** Şimdi küçük bir tuzak! İki değişken de parantezli bir beş gibi duruyor. Sence ikisinin tipi aynı mı?

**Ekranda başlık:** Sence ne yazar?

**Kod**:

```python
a = (5)
b = (5,)
print(type(a))
print(type(b))
```

**Maskot:** dusunme pozu, sag

## Sahne 8: cikti (10 sn)

**Seslendirme:** Aynı değil! Virgül olmayınca Python onu parantez içindeki sıradan bir sayı sanar. Tek elemanlı tuple yazarken virgülü unutma.

**Ekranda başlık:** Cevap

**Kod** (vurgulanan satırlar: 2):

```python
a = (5)
b = (5,)
print(type(a))
print(type(b))
```

**Çıktı:**

```text
<class 'int'>
<class 'tuple'>
```

**Maskot:** mutlu pozu, sag

## Sahne 9: gorev (14 sn)

**Seslendirme:** Görev zamanı! Bir konumu iki değişkene açacak, renk paletinin ilk ve son rengini bulacak ve mühürlü bir çantaya yeni eşya ekleyeceksin. Challenge'da iki değişkeni üçüncü bir değişken kullanmadan yer değiştireceksin.

**Ekranda başlık:** Bugünün görevleri

**Ekranda maddeler:**

- Görev 1: Konumu aç
- Görev 2: Renk paleti
- Görev 3: Yeni eşya ekle
- Challenge: Yer değiştir

**Maskot:** isaret pozu, sol

## Sahne 10: ozet (6 sn)

**Seslendirme:** Bugün mühürlü kutuları açtık, içlerindekileri dağıttık ve virgül tuzağını öğrendik.

**Ekranda başlık:** Bugün öğrendiklerin

**Ekranda maddeler:**

- Tuple: ( ) ile yazılır, değiştirilemez
- list() ile aç, tuple() ile yeniden mühürle
- x, y = pos ile aç; tek eleman için (5,)

**Maskot:** on pozu, sag

## Sahne 11: kapanis (8 sn)

**Seslendirme:** Koordinatlar güvende! Yarın ormanda aynı yerlerden defalarca geçeceğiz ve tekrarları kendiliğinden atan set'lerle tanışacağız.

**Ekranda başlık:** Yarın: Set'ler

**Görsel:** `gorseller/python/harita/orman.webp`

**Maskot:** tebrik pozu, orta

## Çıkış (30gunde.com.tr yönlendirmesi)

**Seslendirme:** Bu dersin interaktif hâli 30gunde.com.tr'de seni bekliyor. Kodunu tarayıcıda yaz, hemen çalıştır ve görevleri tamamla!

**Ekranda:** İnteraktif dersler için **30gunde.com.tr**

- Kodunu tarayıcıda yaz ve çalıştır
- Görevleri tamamla, rozet kazan
- 30 günde adım adım Python
