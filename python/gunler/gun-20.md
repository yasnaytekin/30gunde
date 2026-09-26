# Gün 20: Paket yöneticisi pip

**Kurs:** 30 Günde Python  ·  **Bölge:** Keşif Adası  ·  **Maskot:** Piko

**Bugünün hedefi:** Paket ve pip kavramlarını öğrenmek, requirements.txt dosyalarını okuyup yazmak

> Keşif Adası'nın limanına her gün gemiler yanaşıyor. Gemilerden dünyanın her yerinden kutular iniyor: içlerinde başka programcıların yaptığı hazır aletler var. Python dünyasında bu kutulara **paket**, onları getiren gemiye de **pip** diyoruz.

![Keşif Adası](../../gorseller/python/harita/ada.webp)

## Konu anlatımı

### Paket nedir?

Paket, başkalarının yazıp herkesle paylaştığı modüller topluluğudur. Dünyada yüz binlerce Python paketi var ve hepsi **PyPI** (Python Package Index) adlı dev bir depoda durur.

Örneğin `requests` internetten veri almayı, `pygame` oyun yapmayı, `pandas` tablo işlemeyi kolaylaştırır.

### pip komutları

`pip` paketleri kurmaya yarayan programdır. Bu komutlar Python kodunun içine değil, bilgisayarındaki **terminale** yazılır:

```
pip install requests        # kur
pip install pygame==2.5.2   # belli bir sürümü kur
pip list                    # kurulu paketleri göster
pip uninstall requests      # kaldır
pip freeze                  # paketleri sürümleriyle listele
```

### requirements.txt

Bir projenin hangi paketlere ihtiyacı olduğu `requirements.txt` dosyasına yazılır. Her satırda bir paket ve sürümü olur:

```
requests==2.31.0
pygame==2.5.2
```

Başka biri projeni indirdiğinde `pip install -r requirements.txt` yazarak hepsini tek seferde kurar.

### Sürüm numaraları

`2.31.0` gibi sürümler **büyük.küçük.yama** şeklinde okunur. Karşılaştırırken dikkat! Yazı olarak karşılaştırırsan `"2.4.1" > "2.31.0"` çıkar, çünkü Python harf harf bakar ve `4`, `3`'ten büyüktür. Doğrusu parçaları sayıya çevirmektir:

```python
v = tuple(int(p) for p in "2.31.0".split("."))   # (2, 31, 0)
```

Bu sitedeki Python, bazı popüler paketlerle birlikte gelir. `import this` yazıp çalıştır, sana bir sürpriz var.

## Örnekler

### Python'ın bilgelikleri

```python
import this
```

*Python'ın yazım felsefesi. İngilizce ama güzel!*

### Satırı parçala

```python
line = "requests==2.31.0"
name, version = line.split("==")
print("Paket:", name)
print("Sürüm:", version)
```

### Sürüm tuzağı

```python
a = "2.4.1"
b = "2.31.0"
print("Yazı olarak:", a > b)
va = tuple(int(p) for p in a.split("."))
vb = tuple(int(p) for p in b.split("."))
print("Sayı olarak:", va > vb)
```

*Hangisi doğru? 31, 4'ten büyük olduğu için 2.31.0 daha yeni.*

## Görevler

### Görev 1: Satırı parçala

`line` içindeki paket adını `name`, sürümü `version` değişkenine koy.

**Başlangıç kodu:**

```python
line = "requests==2.31.0"

name = ""
version = ""

print(name, version)
```

**İpuçları:**

1. line.split("==") iki parçalı bir liste verir.
2. Tuple açma gibi iki değişkene dağıtabilirsin.

<details><summary>Çözüm</summary>

```python
line = "requests==2.31.0"

name, version = line.split("==")

print(name, version)
```

</details>

### Görev 2: requirements okuyucu

`text` bir requirements.txt içeriği. Her satırı parçalayıp `packages` sözlüğüne `{paket: sürüm}` olarak ekle. Boş satırları atla.

**Başlangıç kodu:**

```python
text = """requests==2.31.0
flask==3.0.0

numpy==1.26.4"""

packages = {}

print(packages)
```

**İpuçları:**

1. text.splitlines() satırları verir.
2. Boş satırı atlamak için: if line == "": continue

<details><summary>Çözüm</summary>

```python
text = """requests==2.31.0
flask==3.0.0

numpy==1.26.4"""

packages = {}
for line in text.splitlines():
    line = line.strip()
    if line == "":
        continue
    name, version = line.split("==")
    packages[name] = version

print(packages)
```

</details>

### Görev 3: Hangisi daha yeni?

`v1` ve `v2` sürümlerini **sayı olarak** karşılaştır. Daha yeni olanı `newer` değişkenine koy (eşitse `v1`).

**Başlangıç kodu:**

```python
v1 = "2.4.1"
v2 = "2.31.0"

newer = v1

print("Daha yeni:", newer)
```

**İpuçları:**

1. Her sürümü parçala: v1.split(".")
2. Parçaları int'e çevirip tuple yap, tuple'lar sayı gibi karşılaştırılır.

<details><summary>Çözüm</summary>

```python
v1 = "2.4.1"
v2 = "2.31.0"

t1 = tuple(int(p) for p in v1.split("."))
t2 = tuple(int(p) for p in v2.split("."))
newer = v2 if t2 > t1 else v1

print("Daha yeni:", newer)
```

</details>

## Challenge: Eksik paketler

`needed` projenin istediği paketler, `installed` kurulu olanlar. Kurulması gereken paketleri alfabetik sırayla `to_install` listesine koy.

**Başlangıç kodu:**

```python
needed = {"requests", "pygame", "rich"}
installed = {"pygame", "numpy"}

to_install = []

print(to_install)
```

**İpuçları:**

1. Set farkını hatırla: needed - installed
2. sorted() sonucu liste olarak verir.

<details><summary>Çözüm</summary>

```python
needed = {"requests", "pygame", "rich"}
installed = {"pygame", "numpy"}

to_install = sorted(needed - installed)

print(to_install)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Paket listesi**

### Piko'nun Macerası: Paket listesi

Oyunumuzu bilgisayarında çalıştırmak isteyenler için bir requirements.txt hazırlayalım. `packages` sözlüğünden, paketleri **alfabetik sırayla** `ad==sürüm` biçiminde satır satır içeren `requirements` yazısını oluştur ve yazdır:

```
pygame==2.5.2
rich==13.7.0
```

**Başlangıç kodu:**

```python
packages = {"rich": "13.7.0", "pygame": "2.5.2"}

requirements = ""

print(requirements)
```

**İpuçları:**

1. sorted(packages.items()) paketleri isme göre sıralar.
2. Satırları birleştirmek için "\n".join(liste)

<details><summary>Çözüm</summary>

```python
packages = {"rich": "13.7.0", "pygame": "2.5.2"}

lines = [f"{name}=={version}" for name, version in sorted(packages.items())]
requirements = "\n".join(lines)

print(requirements)
```

</details>

### Harcama Defteri: requirements.txt

Harcama Defteri'ni başka bir bilgisayarda çalıştırmak için gereken paketleri yazalım. `packages` sözlüğünden (paket -> sürüm), paketleri **alfabetik sırayla** `ad==sürüm` biçiminde satır satır içeren `requirements` yazısını oluştur ve yazdır:

```
matplotlib==3.8.2
pandas==2.1.4
```

**Başlangıç kodu:**

```python
packages = {"pandas": "2.1.4", "matplotlib": "3.8.2"}
```

**İpuçları:**

1. sorted(packages) anahtarları alfabetik verir.
2. "\n".join(lines) satırları alt alta birleştirir.

<details><summary>Çözüm</summary>

```python
packages = {"pandas": "2.1.4", "matplotlib": "3.8.2"}
lines = []
for name in sorted(packages):
    lines.append(f"{name}=={packages[name]}")
requirements = "\n".join(lines)
print(requirements)
```

</details>

### Görev Asistanı: requirements.txt okuma

Asistan bir projenin `requirements.txt` dosyasını okuyabilsin. `parse_requirements(text)`:

- Her `ad==sürüm` satırını sözlüğe koysun: `{"requests": "2.31.0"}`
- Boş satırları ve `#` ile başlayan yorum satırlarını atlasın.

**Başlangıç kodu:**

```python
def parse_requirements(text):
    pass
```

**İpuçları:**

1. text.splitlines() satırları verir.
2. line.split("==") adı ve sürümü ayırır.

<details><summary>Çözüm</summary>

```python
def parse_requirements(text):
    packages = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        name, version = line.split("==")
        packages[name] = version
    return packages
```

</details>

### Kişisel Web Sitem: requirements.txt okuma

Arkadaşın site üreticini kendi bilgisayarında çalıştırmak istiyor. `requirements` yazısındaki paketleri okuyup `versions` sözlüğüne koy (paket -> sürüm):

- `==` içermeyen satırları (boş satırlar ve `#` ile başlayan yorumlar) atla.
- Kalan satırları `split("==")` ile ad ve sürüme ayır.

Sonra paket sayısını ve paketleri **alfabetik sırayla** yazdır:

```
3 paket
beautifulsoup4: 4.12.3
jinja2: 3.1.3
markdown: 3.5.2
```

**Başlangıç kodu:**

```python
requirements = """markdown==3.5.2
# sayfaları güzelleştirmek için
jinja2==3.1.3

beautifulsoup4==4.12.3
"""
versions = {}
```

**İpuçları:**

1. for line in requirements.splitlines(): her satırı sırayla verir; if "==" not in line: continue ile atla.
2. name, version = line.strip().split("==")

<details><summary>Çözüm</summary>

```python
requirements = """markdown==3.5.2
# sayfaları güzelleştirmek için
jinja2==3.1.3

beautifulsoup4==4.12.3
"""
versions = {}
for line in requirements.splitlines():
    if "==" not in line:
        continue
    name, version = line.strip().split("==")
    versions[name] = version
print(len(versions), "paket")
for name in sorted(versions):
    print(f"{name}: {versions[name]}")
```

</details>

### Sohbet Botu: Paket kontrolü

Botun çalışması için gereken paketler `requirements` yazısında (`requirements.txt` gibi, her satırda `ad==sürüm`). Bilgisayarda kurulu olanlar `installed` sözlüğünde (paket -> sürüm).

- `missing`: hiç kurulu olmayan paketlerin adları
- `different`: kurulu ama sürümü farklı olan paketlerin adları

Satırları `requirements.splitlines()` ile, adı ve sürümü `line.split("==")` ile ayırabilirsin. Sonra şöyle yazdır:

```
Eksik: ['beautifulsoup4']
Farklı sürüm: ['pandas']
Çalıştır: pip install -r requirements.txt
```

Eksik ya da farklı sürümlü paket yoksa son satır yerine `Her şey hazır!` yazdır.

**Başlangıç kodu:**

```python
requirements = """requests==2.31.0
beautifulsoup4==4.12.3
pandas==2.1.4"""
installed = {"requests": "2.31.0", "pandas": "2.0.3"}
```

**İpuçları:**

1. name, version = line.split("==") satırı iki parçaya ayırır.
2. Önce name not in installed, sonra elif installed[name] != version.

<details><summary>Çözüm</summary>

```python
requirements = """requests==2.31.0
beautifulsoup4==4.12.3
pandas==2.1.4"""
installed = {"requests": "2.31.0", "pandas": "2.0.3"}
missing = []
different = []
for line in requirements.splitlines():
    name, version = line.split("==")
    if name not in installed:
        missing.append(name)
    elif installed[name] != version:
        different.append(name)
print("Eksik:", missing)
print("Farklı sürüm:", different)
if missing or different:
    print("Çalıştır: pip install -r requirements.txt")
else:
    print("Her şey hazır!")
```

</details>

### Okul Not Defteri: Eksik paketler

Not Defteri'nin ileride kullanacağı paketler `required` yazısında (`requirements.txt` biçiminde, her satır `ad==sürüm`). Bilgisayarında kurulu olanlar `installed` sözlüğünde (paket -> sürüm).

- `to_install`: kurulu olmayan **ya da** sürümü farklı olan satırların listesi (`required`'daki sırayla)
- `to_install` boş değilse `pip install` komutunu yazdır:

```
pip install beautifulsoup4==4.12.3 numpy==1.26.4
```

- Boşsa `Tüm paketler kurulu.` yazdır.

**Başlangıç kodu:**

```python
required = """pandas==2.1.4
beautifulsoup4==4.12.3
numpy==1.26.4"""
installed = {"pandas": "2.1.4", "numpy": "1.24.0"}
```

**İpuçları:**

1. required.splitlines() satırları verir; line.split("==") adı ve sürümü ayırır.
2. installed.get(name) paket kurulu değilse None verir; sürümle karşılaştır. " ".join(to_install) listeyi boşlukla birleştirir.

<details><summary>Çözüm</summary>

```python
required = """pandas==2.1.4
beautifulsoup4==4.12.3
numpy==1.26.4"""
installed = {"pandas": "2.1.4", "numpy": "1.24.0"}
to_install = []
for line in required.splitlines():
    name, version = line.split("==")
    if installed.get(name) != version:
        to_install.append(line)
if to_install:
    print("pip install " + " ".join(to_install))
else:
    print("Tüm paketler kurulu.")
```

</details>
