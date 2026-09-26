# Video şablonları

İki şablon var. İkisi de aynı yöntemle çalışır: sahneler bir HTML sayfasında `renderAt(t)` fonksiyonuyla
zamana göre çizilir, Playwright (Chromium) her kareyi çeker, ffmpeg kareleri videoya dönüştürür.
Böylece çıktı her seferinde birebir aynı olur.

Gerekenler: Python 3, `pip install playwright numpy scipy` + `playwright install chromium`, ffmpeg.
Yazı tipi olarak Poppins (Google Fonts) ve kod için DejaVu Sans Mono kurulu olmalı.

## ders-videosu/: gün gün konu anlatım videoları

`python/video-senaryolari/gun-XX.json` ve `javascript/video-senaryolari/gun-XX.json` dosyalarını okur.

```bash
cd video-sablonu/ders-videosu
python3 build.py ../../javascript/video-senaryolari/gun-01.json   # built.html üretir
python3 preview.py h 3,20,45                                     # birkaç anın ekran görüntüsü
python3 render.py h                                              # yatay 1920x1080 → ders_h.mp4
python3 render.py v                                              # dikey 1080x1920 → ders_v.mp4 (Reels/Shorts)
SUBTITLES=0 python3 render.py h                                  # altyazısız
```

- Her sahne senaryodaki `sure_sn` kadar sürer. Kod sahnelerinde kod yazılıyormuş gibi belirir,
  vurgulanan satırlar parlar, çıktı paneli sonra açılır. Maskot pozu sahneden sahneye değişir.
- Seslendirme henüz yok: altyazı olarak senaryodaki `anlatim` metni gösterilir. Seslendirme
  (insan sesi ya da TTS) sahne sürelerine göre kaydedilip ffmpeg ile eklenebilir:
  `ffmpeg -i ders_h.mp4 -i ses.wav -c:v copy -c:a aac -shortest gun-01.mp4`
- Tema kursa göre otomatik seçilir: Python açık renk harita teması, JavaScript lacivert uzay teması.

## tanitim-videosu/: 30 saniyelik tanıtım videosu (30 Günde Python)

Sitenin ekran görüntüleriyle yapılmış lansman videosu. Kaynak olarak ve yeni tanıtımlar için örnek.

```bash
cd video-sablonu/tanitim-videosu
python3 build.py            # built.html (ikonlar gömülür)
python3 music.py            # music.wav: kodla üretilmiş müzik (numpy/scipy)
python3 preview.py h 3,12   # önizleme kareleri
python3 render.py h         # silent_h.mp4 (v: dikey)
ffmpeg -i silent_h.mp4 -i music.wav -c:v copy -c:a aac -shortest tanitim_h.mp4
```
