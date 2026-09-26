# Gün 23: Sanal ortam

**Kurs:** 30 Günde Python  ·  **Bölge:** Bilgi Limanı  ·  **Maskot:** Piko

**Bugünün hedefi:** Sanal ortamın ne olduğunu ve neden kullanıldığını anlamak, venv komutlarını tanımak

> Limanda iki gemi yan yana duruyor. Biri balık taşıyor, diğeri çiçek. Yükler karışsa ne olurdu, düşünsene! Her geminin kendi ambarı var. Bilgisayarındaki Python projeleri de böyledir: her projenin kendi paket ambarı olmalı. Bu ambara **sanal ortam** denir.

![Bilgi Limanı](../../gorseller/python/harita/liman.webp)

## Konu anlatımı

### Sorun: sürüm çakışması

Diyelim ki oyun projen `pygame 2.5` istiyor, eski bir proje de `pygame 2.1`. Bilgisayarda tek bir Python ve tek bir paket kutusu varsa ikisi aynı anda kurulamaz. Birini güncellersen öbürü bozulur.

**Sanal ortam** (virtual environment), her projeye kendi ayrı paket kutusunu verir. Böylece projeler birbirini etkilemez.

### Oluşturmak ve açmak

Bu komutlar terminale yazılır, proje klasöründeyken:

```
python -m venv .venv
```

Sonra ortamı **etkinleştirirsin**:

```
# Windows
.venv\Scripts\activate

# macOS ve Linux
source .venv/bin/activate
```

Terminalin başında `(.venv)` görürsen ortam açıktır. Artık `pip install` ile kurduğun her paket sadece bu projeye gider. Kapatmak için `deactivate` yaz.

### Ortamı paylaşmak

Sanal ortam klasörü büyük olur ve başkasıyla paylaşılmaz. Onun yerine paket listesini paylaşırız:

```
pip freeze > requirements.txt
```

Arkadaşın kendi sanal ortamını kurar ve `pip install -r requirements.txt` ile aynı paketleri yükler. `.venv` klasörü de `.gitignore` dosyasına yazılarak paylaşımdan çıkarılır.

### Kodda benzer bir tuzak

Ortamları ayırmanın önemini Python'da da görebiliriz. Bir listeyi başka bir değişkene atarsan **aynı liste** paylaşılır:

```python
game = ["pygame"]
site = game          # aynı kutu!
site.append("flask")
print(game)          # ['pygame', 'flask']
```

Ayrı bir kopya için `site = game.copy()` yazılır. Sanal ortam da projelere ayrı kopyalar vermek gibidir.

## Örnekler

### Paylaşılan kutu tuzağı

```python
game = ["pygame"]
site = game
site.append("flask")
print("Oyun:", game)

game = ["pygame"]
site = game.copy()
site.append("flask")
print("Oyun:", game)
print("Site:", site)
```

### Ortamları taklit edelim

```python
envs = {
    "oyun": {"pygame": "2.5.2"},
    "eski-oyun": {"pygame": "2.1.0"},
}
for name, packages in envs.items():
    print(name, "->", packages)
```

*İki projede aynı paketin farklı sürümleri sorunsuzca yaşıyor.*

### Komutları üret

```python
env = ".venv"
print("Oluştur:", f"python -m venv {env}")
print("Windows:", f"{env}\\Scripts\\activate")
print("macOS/Linux:", f"source {env}/bin/activate")
```

## Görevler

### Görev 1: Komutları hazırla

`env_name` adıyla sanal ortam oluşturma ve macOS/Linux'ta etkinleştirme komutlarını üret:

- `create_cmd`: `python -m venv .venv`
- `activate_cmd`: `source .venv/bin/activate`

**Başlangıç kodu:**

```python
env_name = ".venv"

create_cmd = ""
activate_cmd = ""

print(create_cmd)
print(activate_cmd)
```

**İpuçları:**

1. f-string kullan: f"python -m venv {env_name}"

<details><summary>Çözüm</summary>

```python
env_name = ".venv"

create_cmd = f"python -m venv {env_name}"
activate_cmd = f"source {env_name}/bin/activate"

print(create_cmd)
print(activate_cmd)
```

</details>

### Görev 2: Ayrı kopya

`site` listesi `game` listesinin **ayrı bir kopyası** olsun. `site`'a `"flask"` ekleyince `game` değişmemeli.

**Başlangıç kodu:**

```python
game = ["pygame", "rich"]

site = game
site.append("flask")

print("Oyun:", game)
print("Site:", site)
```

**İpuçları:**

1. site = game.copy()

<details><summary>Çözüm</summary>

```python
game = ["pygame", "rich"]

site = game.copy()
site.append("flask")

print("Oyun:", game)
print("Site:", site)
```

</details>

### Görev 3: Çakışmayı bul

İki proje aynı paketlerin farklı sürümlerini istiyor olabilir. **Her ikisinde de olup** sürümü farklı olan paketlerin adlarını alfabetik sırayla `conflicts` listesine koy.

**Başlangıç kodu:**

```python
project_a = {"pygame": "2.5.2", "numpy": "1.26.4", "rich": "13.7.0"}
project_b = {"pygame": "2.1.0", "numpy": "1.26.4", "flask": "3.0.0"}

conflicts = []

print(conflicts)
```

**İpuçları:**

1. project_a'daki her paket için project_b'de var mı bak.
2. Varsa ve sürümler farklıysa listeye ekle, sonunda sorted()

<details><summary>Çözüm</summary>

```python
project_a = {"pygame": "2.5.2", "numpy": "1.26.4", "rich": "13.7.0"}
project_b = {"pygame": "2.1.0", "numpy": "1.26.4", "flask": "3.0.0"}

conflicts = sorted([name for name in project_a if name in project_b and project_a[name] != project_b[name]])

print(conflicts)
```

</details>

## Challenge: Ortama kur

`install(envs, env, package, version)` fonksiyonu paketi **sadece** verilen ortama kursun. Ortam yoksa önce boş bir ortam oluştursun.

**Başlangıç kodu:**

```python
def install(envs, env, package, version):
    pass

envs = {"oyun": {}}
install(envs, "oyun", "pygame", "2.5.2")
install(envs, "site", "flask", "3.0.0")
print(envs)
```

**İpuçları:**

1. Ortam yoksa: if env not in envs: envs[env] = {}
2. Sonra envs[env][package] = version

<details><summary>Çözüm</summary>

```python
def install(envs, env, package, version):
    if env not in envs:
        envs[env] = {}
    envs[env][package] = version

envs = {"oyun": {}}
install(envs, "oyun", "pygame", "2.5.2")
install(envs, "site", "flask", "3.0.0")
print(envs)
```

</details>

## Proje adımları

Bugünün katkısı (Piko'nun Macerası): **Proje düzeni**

### Piko'nun Macerası: Proje düzeni

Oyunumuzu paylaşmadan önce hangi dosyaların paylaşılacağını seçelim. `files` listesinden **`.venv/` ile başlayanları ve `.pyc` ile bitenleri** çıkar, kalanları alfabetik sırayla `shared` listesine koy ve her birini ayrı satırda yazdır.

**Başlangıç kodu:**

```python
files = ["main.py", ".venv/bin/python", "requirements.txt", "piko/oyun.py", "piko/oyun.pyc", ".venv/lib/site.py"]

shared = []

# Her birini yazdır
```

**İpuçları:**

1. f.startswith(".venv/") ve f.endswith(".pyc") işine yarar.
2. List comprehension içinde not ... and not ... kullan.

<details><summary>Çözüm</summary>

```python
files = ["main.py", ".venv/bin/python", "requirements.txt", "piko/oyun.py", "piko/oyun.pyc", ".venv/lib/site.py"]

shared = sorted([f for f in files if not f.startswith(".venv/") and not f.endswith(".pyc")])

for f in shared:
    print(f)
```

</details>

### Harcama Defteri: Paylaşılacak dosyalar

Projeni paylaşmadan önce hangi dosyaların gideceğini seçelim. `files` listesinden şunları çıkar:

- `.venv/` ile başlayanlar (sanal ortam her bilgisayarda yeniden kurulur)
- `.json` ile bitenler (kişisel harcama verilerin!)

Kalanları alfabetik sırayla `shared` listesine koy ve her birini ayrı satırda yazdır.

**Başlangıç kodu:**

```python
files = ["defter.py", ".venv/bin/python", "harcamalar.json", "README.md", "requirements.txt", ".venv/lib/x.py"]
```

**İpuçları:**

1. f.startswith(".venv/") ve f.endswith(".json")
2. Kalanları sorted() ile sırala.

<details><summary>Çözüm</summary>

```python
files = ["defter.py", ".venv/bin/python", "harcamalar.json", "README.md", "requirements.txt", ".venv/lib/x.py"]
shared = sorted([f for f in files if not f.startswith(".venv/") and not f.endswith(".json")])
for f in shared:
    print(f)
```

</details>

### Görev Asistanı: Kurulum komutları

Asistanı başka bir bilgisayara kurarken sanal ortam gerekiyor. `setup_commands(os_name)` bir komut listesi döndürsün:

1. `python -m venv .venv`
2. Etkinleştirme: `os_name` `"windows"` ise `.venv\\Scripts\\activate`, değilse `source .venv/bin/activate`
3. `pip install -r requirements.txt`

**Başlangıç kodu:**

```python
def setup_commands(os_name):
    pass
```

**İpuçları:**

1. Önce if ile etkinleştirme komutunu seç.
2. Python yazısında ters bölü iki kez yazılır: "\\"

<details><summary>Çözüm</summary>

```python
def setup_commands(os_name):
    if os_name == "windows":
        activate = ".venv\\Scripts\\activate"
    else:
        activate = "source .venv/bin/activate"
    return ["python -m venv .venv", activate, "pip install -r requirements.txt"]


for command in setup_commands("linux"):
    print(command)
```

</details>

### Kişisel Web Sitem: Yüklenecek dosyalar

Siteyi sunucuya yüklerken sadece ziyaretçinin göreceği dosyalar gitsin. `files` listesinden `deploy` listesini oluştur:

- `.venv/` ile başlayanları çıkar (sanal ortam yüklenmez; içinde `.html` dosyaları bile olabilir!).
- Sadece `.html` veya `.css` ile bitenleri al.

`deploy`'u alfabetik sırala, her dosyayı ayrı satırda yazdır ve en sonda `3 dosya yüklenecek` gibi yazdır.

**Başlangıç kodu:**

```python
files = ["index.html", "build.py", ".venv/lib/python3.12/site.py", "style.css", ".venv/share/doc/index.html", "blog/merhaba.html", "requirements.txt", "yazilar.json"]
```

**İpuçları:**

1. f.startswith(".venv/"), f.endswith(".html") ve f.endswith(".css")
2. Koşulları and / or ile birleştir; or kısmını parantez içine al.

<details><summary>Çözüm</summary>

```python
files = ["index.html", "build.py", ".venv/lib/python3.12/site.py", "style.css", ".venv/share/doc/index.html", "blog/merhaba.html", "requirements.txt", "yazilar.json"]
deploy = sorted([f for f in files if not f.startswith(".venv/") and (f.endswith(".html") or f.endswith(".css"))])
for f in deploy:
    print(f)
print(len(deploy), "dosya yüklenecek")
```

</details>

### Sohbet Botu: Neyi paylaşmalı?

Botunu arkadaşlarınla paylaşacaksın ama her dosya gitmemeli:

- `.venv/` ile başlayanlar: sanal ortam, her bilgisayarda `python -m venv .venv` ile yeniden kurulur.
- `__pycache__/` ile başlayanlar: Python'ın kendi ürettiği geçici dosyalar.
- `.json` ile bitenler: sohbet kayıtların, kişisel!
- `.env` ile bitenler: API anahtarı gibi gizli bilgiler.

`should_share(path)` bu dosyalar için `False`, diğerleri için `True` döndürsün. Sonra `shared` listesine paylaşılacak dosyaları (sırası bozulmadan) koy ve her birini ayrı satırda yazdır.

**Başlangıç kodu:**

```python
files = ["bot.py", ".venv/bin/python", "sohbet.json", "__pycache__/bot.pyc", ".env", "requirements.txt", "README.md"]


def should_share(path):
    pass
```

**İpuçları:**

1. path.startswith(".venv/") ve path.endswith(".json") True ya da False verir.
2. shared = [f for f in files if should_share(f)]

<details><summary>Çözüm</summary>

```python
files = ["bot.py", ".venv/bin/python", "sohbet.json", "__pycache__/bot.pyc", ".env", "requirements.txt", "README.md"]


def should_share(path):
    if path.startswith(".venv/") or path.startswith("__pycache__/"):
        return False
    if path.endswith(".json") or path.endswith(".env"):
        return False
    return True


shared = [f for f in files if should_share(f)]
for f in shared:
    print(f)
```

</details>

### Okul Not Defteri: .gitignore hazırlama

Projeni paylaşırken `.venv` sanal ortam klasörü gitmemeli (herkes kendi ortamını kurar) ve notların da gizli kalmalı. Bunları `.gitignore` dosyasına yazarız.

`make_gitignore(private_files)` bir yazı döndürsün:

- İlk iki satır her zaman `.venv/` ve `__pycache__/`
- Sonra `private_files` listesindeki dosyalar, her biri ayrı satırda
- Aynı satır iki kez yazılmasın.

`make_gitignore(["notlar.json"])` şunu döndürmeli:

```
.venv/
__pycache__/
notlar.json
```

**Başlangıç kodu:**

```python
def make_gitignore(private_files):
    pass
```

**İpuçları:**

1. Önce lines = [".venv/", "__pycache__/"] listesiyle başla; if name not in lines: ile tekrarı önle.
2. "\n".join(lines) satırları alt alta birleştirir.

<details><summary>Çözüm</summary>

```python
def make_gitignore(private_files):
    lines = [".venv/", "__pycache__/"]
    for name in private_files:
        if name not in lines:
            lines.append(name)
    return "\n".join(lines)


print(make_gitignore(["notlar.json"]))
```

</details>
