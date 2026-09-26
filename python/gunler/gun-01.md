# Gün 1: Python ile tanışma

**Kurs:** 30 Günde Python  ·  **Bölge:** Başlangıç Kampı  ·  **Maskot:** Piko

**Bugünün hedefi:** print() ile ekrana yazı yazmak ve Python'ı hesap makinesi gibi kullanmak

> Selam! Ben Piko. Bilgisayarlar çok hızlıdır ama ne yapacaklarını kendileri bilmez. Onlara ne yapacaklarını sen söyleyeceksin. Bugün bilgisayara ilk kez konuşmayı öğreteceğiz!

![Başlangıç Kampı](../../gorseller/python/harita/kamp.webp)

## Konu anlatımı

### Kod nedir?

Kod, bilgisayara verdiğin talimatların listesidir. Python bu talimatları **yukarıdan aşağıya, satır satır** okur ve sırayla yapar.

Python dünyada en çok kullanılan programlama dillerinden biri. Oyunlar, web siteleri, yapay zekâ programları... Hepsinde Python var.

### print() ile konuş

`print()` parantezin içine yazdığın şeyi ekrana yazar. Yazıları **tırnak içine** alırız, sayıları almayız.

```python
print("Merhaba!")
print(42)
```

Virgül koyarak birden çok şeyi yan yana yazdırabilirsin. Python aralarına boşluk koyar.

### Python bir hesap makinesi

- `+` toplama, `-` çıkarma
- `*` çarpma, `/` bölme
- `**` üs alma: `2 ** 3` sonucu `8`

İşlemi tırnak içine yazarsan Python hesaplamaz, olduğu gibi yazar: `print("2 + 2")` ekrana `2 + 2` yazar.

### Yorumlar ve hatalar

`#` ile başlayan satırlar **yorumdur**. Python onları okumaz; kendine not bırakmak için kullanırsın.

Bir harfi yanlış yazarsan Python hata verir. Korkma! Hata, sorunun hangi satırda olduğunu söyler ve ben de sana ne anlama geldiğini Türkçe anlatırım.

### Sahnede çizim: her yıldız bir Piko

Bazı görevlerde yazdırdığın şey **sahnede resme dönüşür**. Kurallar çok basit:

- `*` yazdırırsan sahnede bir **Piko** belirir
- `#` bir **duvar**, `o` bir **altın**, `H` bir **kalp** olur
- boşluk boş bir karedir

Yani `print("***")` yan yana üç Piko dizer. Alt alta üç kez yazdırırsan 3 satırlık bir Piko ordusu kurarsın!

## Örnekler

### İlk program

```python
print("Merhaba Dünya!")
```

*Çalıştır'a bas ve çıktıya bak.*

### Hesap yapalım

```python
print(3 + 4)
print(10 * 5)
print(2 ** 10)
print("3 + 4")
```

*Son satır neden hesaplanmadı? Çünkü tırnak içinde!*

### Virgülle yazdır

```python
# Bu bir yorum, Python bunu okumaz
print("Piko", "diyor ki:", "Selam!")
print("Yaşım:", 12)
```

### Piko sırası

```python
print("*****")
print("#####")
```

*Çalıştır'a bas: beş Piko ve altlarında beş duvar.*

## Görevler

### Görev 1: İlk sözün

Ekrana tam olarak `Merhaba Python!` yazdır.

**Başlangıç kodu:**

```python
# print() kullanarak yaz
```

**İpuçları:**

1. print() fonksiyonunu kullan.
2. Yazılar tırnak içinde olmalı: print("...")
3. Büyük/küçük harfler ve ünlem de aynı olmalı: Merhaba Python!

<details><summary>Çözüm</summary>

```python
print("Merhaba Python!")
```

</details>

### Görev 2: Kendini tanıt

Ekrana `Benim adım` ile başlayan ve adınla biten bir cümle yazdır. Örneğin: `Benim adım Ayşe`

**Başlangıç kodu:**

```python

```

**İpuçları:**

1. Tek bir print() yeterli.
2. Tırnağın içine "Benim adım" ve adını yaz.

<details><summary>Çözüm</summary>

```python
print("Benim adım Deniz")
```

</details>

### Görev 3: Bir yılda kaç saat?

Bir yılda 365 gün, bir günde 24 saat var. Sonucu kendin hesaplama; `365 * 24` işlemini Python'a yaptır ve yazdır.

**Başlangıç kodu:**

```python

```

**İpuçları:**

1. Çarpma işareti *
2. İşlemi tırnak içine yazma, yoksa Python hesaplamaz.

<details><summary>Çözüm</summary>

```python
print(365 * 24)
```

</details>

### Sahne görevi: Piko ordusu

Her `*` sahnede bir Piko. `print()` ile **3 satır**, her satırda **3 Piko** olan bir ordu diz. Sahnede soluk görünen şekli doldur!

**Başlangıç kodu:**

```python
print("***")
```

**İpuçları:**

1. Bir satır için print("***") yeterli.
2. Alt alta üç satır için üç tane print() yaz.

<details><summary>Çözüm</summary>

```python
print("***")
print("***")
print("***")
```

</details>

## Challenge: Yıldızlı afiş

En az 3 satırdan oluşan bir afiş yazdır. En az 3 satırda `*` olsun. Küçük bir sır: `print("*" * 20)` yan yana 20 yıldız yazar!

**Başlangıç kodu:**

```python

```

**İpuçları:**

1. Üç ayrı print() kullanabilirsin.
2. Yıldızlı çizgi için "*" * 20

<details><summary>Çözüm</summary>

```python
print("*" * 20)
print("*  PİKO GELİYOR  *")
print("*" * 20)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Karşılama ekranı**

### Piko'nun Macerası: Karşılama ekranı

Oyunumuzun adı **Piko'nun Macerası**. Oyun açıldığında görünecek karşılama ekranını yaz: oyunun adını ve `Oyuna hoş geldin!` mesajını yazdır. İstersen yıldızlarla süsle.

**Başlangıç kodu:**

```python
# Piko'nun Macerası: karşılama ekranı
print("*" * 30)
```

**İpuçları:**

1. İki yeni print() satırı ekle.
2. Yazıları tam olarak görevde yazdığı gibi yaz.

<details><summary>Çözüm</summary>

```python
print("*" * 30)
print("Piko'nun Macerası")
print("Oyuna hoş geldin!")
print("*" * 30)
```

</details>

### Harcama Defteri: Rapor başlığı

Bu yolda kendi **Harcama Defteri** programını yazacaksın: harcamalarını kaydedecek, bütçeni izleyecek ve rapor çıkaracak.

İlk parça raporun başlığı. Önce 30 tane `=` işaretinden oluşan bir çizgi, sonra `Harcama Defteri` ve `Aylık rapor hazırlanıyor...` yazdır.

**Başlangıç kodu:**

```python
# Harcama Defteri: rapor başlığı
```

**İpuçları:**

1. Üç tane print() yeterli.
2. Çizgi için print("=" * 30) yazabilirsin.

<details><summary>Çözüm</summary>

```python
print("=" * 30)
print("Harcama Defteri")
print("Aylık rapor hazırlanıyor...")
```

</details>

### Görev Asistanı: Asistanın açılışı

Bu yolda kendi **Görev Asistanı** programını yazacaksın: görevlerini düzenleyecek, hatırlatacak ve tekrar eden işleri senin yerine yapacak.

İlk parça açılış mesajı. `Görev Asistanı` ve `Bugünün planı hazırlanıyor...` yazdır, altına 30 tane `-` işaretinden bir çizgi çek.

**Başlangıç kodu:**

```python
# Görev Asistanı: açılış
```

**İpuçları:**

1. Üç tane print() yeterli.
2. Çizgi için print("-" * 30)

<details><summary>Çözüm</summary>

```python
print("Görev Asistanı")
print("Bugünün planı hazırlanıyor...")
print("-" * 30)
```

</details>

### Kişisel Web Sitem: Site üreticisinin açılışı

Bu yolda kendi **Kişisel Web Sitem** programını yazacaksın: yazılarını HTML sayfalarına çevirecek, menüsünü kuracak ve siteni yayına hazırlayacak küçük bir site üreticisi.

İlk parça açılış mesajı. `Kişisel Web Sitem` ve `Sayfalar hazırlanıyor...` yazdır, altına 30 tane `~` işaretinden bir çizgi çek.

**Başlangıç kodu:**

```python
# Kişisel Web Sitem: açılış
```

**İpuçları:**

1. Üç tane print() yeterli.
2. Çizgi için print("~" * 30) yazabilirsin.

<details><summary>Çözüm</summary>

```python
print("Kişisel Web Sitem")
print("Sayfalar hazırlanıyor...")
print("~" * 30)
```

</details>

### Sohbet Botu: Botun ilk sözleri

Bu yolda kendi **Sohbet Botu**'nu yazacaksın: mesajları anlayan, kurallara göre cevap veren ve konuşmaları hatırlayan küçük bir yapay zekâ asistanı.

İlk parça botun açılış ekranı. Önce 30 tane `-` işaretinden oluşan bir çizgi, sonra `Sohbet Botu çalışıyor...` ve `Bot: Merhaba! Sana nasıl yardım edebilirim?` yazdır.

**Başlangıç kodu:**

```python
# Sohbet Botu: karşılama ekranı
```

**İpuçları:**

1. Üç tane print() yeterli.
2. Çizgi için print("-" * 30) yazabilirsin.

<details><summary>Çözüm</summary>

```python
print("-" * 30)
print("Sohbet Botu çalışıyor...")
print("Bot: Merhaba! Sana nasıl yardım edebilirim?")
```

</details>

### Okul Not Defteri: Defterin kapağı

Bu yolda kendi **Okul Not Defteri** programını yazacaksın: derslerini ve notlarını tutacak, ortalamanı hesaplayacak, sınavlarını hatırlatacak ve karneni çıkaracak.

İlk parça defterin kapağı. Önce 30 tane `*` işaretinden oluşan bir çizgi, sonra `Okul Not Defteri` ve `Bu dönemin notları yükleniyor...` yazdır.

**Başlangıç kodu:**

```python
# Okul Not Defteri: kapak
```

**İpuçları:**

1. Üç tane print() yeterli.
2. Çizgi için print("*" * 30) yazabilirsin.

<details><summary>Çözüm</summary>

```python
print("*" * 30)
print("Okul Not Defteri")
print("Bu dönemin notları yükleniyor...")
```

</details>
