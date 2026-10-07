# 30 Günde JavaScript: video planı

Python videolarında kurduğumuz düzenin JavaScript'e nasıl taşınacağı. Şablonun kullanımı için: [video-sablonu/README.md](../video-sablonu/README.md).

## Python'da ne yaptık?

- **120 video:** 30 gün × 2 dil (Türkçe, İngilizce) × 2 yön (yatay 1920×1080, dikey 1080×1920 Reels/Shorts).
- **Tek komut:** `cd video-sablonu/ders-videosu && python3 uret.py python <gün>`. Senaryodan seslendirme, konuşan maskot,
  müzik, efektler ve altyazı (`.srt`) çıkar. Çıktı: `cikti/python/gun-XX/`.
- **Senaryo:** `python/video-senaryolari/gun-XX.json` (+ okunur `.md`), İngilizcesi `en/` altında.
  Sahne türleri: `acilis`, `anlatim`, `kod`, `cikti`, `hata` (+ `duzeltme`), `soru` (3-2-1 sayaç), `gorev`, `ozet`, `kapanis`.
- **Akış:** giriş kartı ("Gün N", başlık, "Bu derste" maddeleri) → sahneler (kod yazılıyormuş gibi belirir, "Çalıştır",
  çıktı açılır) → çıkış kartı (30gunde.com.tr).
- **Ses:** çevrim dışı sherpa-onnx. TR: Piper `fahrettin`, EN: Kokoro `am_michael`. Sahne süreleri sese göre ayarlanır,
  altyazılar cümle cümle eşzamanlı. Telaffuz düzeltmeleri `ses.py` → `TELAFFUZ`.
- **Maskot:** Piko'da gerçek dudak senkronu var (`maskotlar/piko-python/konusma-rig/`, `araclar/agiz-rig.py`).
- **Müzik/efekt:** `muzik.py` ile kodla sentezlenir, telifsiz. Konuşurken müzik kısılır.
- **YouTube:** kanal `youtube.com/@30gundekod`. Kitaplardaki QR kodlar kanala gider, okuyucu "Gün N" videosunu açar.
  Bu yüzden video başlıkları **"Gün N: ..."** / **"Day N: ..."** biçiminde olmalı.

## JavaScript'te durum

| | Durum |
| --- | --- |
| Türkçe senaryolar | ✅ 30 gün hazır (`javascript/video-senaryolari/gun-XX.json` + `.md`, 365 sahne) |
| İngilizce senaryolar | ❌ yok (`javascript/video-senaryolari/en/` oluşturulacak) |
| Şablon desteği | ✅ `uret.py javascript <gün>` çalışır: uzay teması, Kodi pozları, `kod.js`, "Cava skript" telaffuzu |
| Kodi dudak senkronu | ❌ yok: pozlar olduğu gibi gösteriliyor (`konusma-kareleri/1–7.png` mevcut, rig çıkarılmadı) |
| Sayfa (DOM) çıktısı | ❌ 62 sahnede `document`/`canvas`/`fetch` var, şablon yalnızca konsol çıktısı gösteriyor |

## Yapılacaklar (sırayla)

1. **İngilizce senaryolar:** Türkçe senaryoları `en/` altına çevir. Kod ve çıktılar kitabın İngilizce verisiyle
   (`javascript/veri/en/`) aynı olsun: aynı değişken/metin adları, "Star Hunter", İngilizce Demo API
   (`kitap/demo_api_en.js`: cities, questions, levels, tasks, posts).
2. **Sayfa çıktısı sahnesi:** DOM kodlarında "Çıktı" paneli yerine **tarayıcı penceresi** görünsün. Ekran görüntüsünü
   kitaptaki gibi Chromium'da gerçek sayfayı çalıştırarak alabiliriz (`kitap/kitap.py` → `sayfa_goruntusu`: HTML + CSS +
   localStorage + deneme API'si). Senaryoya `ekran.sayfa: {html, css, storage}` alanı eklenir; tıklama/klavye anlatılan
   sahnelerde "önce/sonra" iki kare yeter.
3. **Kodi dudak senkronu:** `araclar/agiz-rig.py`'yi Kodi'nin konuşma kareleriyle çalıştırıp
   `maskotlar/kodi-javascript/konusma-rig/` üret. `build.py` şu an rig'i yalnızca Piko'dan okuyor, kursa göre seçsin.
4. **Ses:** Kodi'ye ayrı bir ses istersek `ses.py` → `SESLER`'e kurs bazlı seçim ekle. Yoksa Piko'nun sesleri kullanılır.
   Telaffuz listesine JS terimlerini ekle: `console.log`, `const`, `async`, `await`, `DOM`, `JSON`, `fetch`, `canvas`.
5. **Adlar:** şablondaki İngilizce kurs adı "JavaScript in 30 Days", kitaplarda ise "30 Days of JavaScript".
   İkisini birleştir (Python için de aynısı geçerli).
6. **Üretim:** önce bir gün dene (`python3 uret.py javascript 1 --onizleme 5,30,90`), sonra 30 gün × 2 dil × 2 yön = 120 video.
7. **Yayın:** YouTube'da "30 Günde JavaScript" ve "30 Days of JavaScript" oynatma listeleri. Açıklamaya 30gunde.com.tr
   bağlantısını ve altyazı dosyalarını ekle.

## Kontrol listesi (her video)

- Kod çalışıyor ve ekrandaki çıktı gerçek çıktıyla aynı mı? (kitap verisiyle karşılaştır)
- Kodi'nin anlatımı altyazıyla eşzamanlı mı, telaffuz doğru mu?
- Dikey sürümde kod ve çıktı okunuyor mu?
- Başlık "Gün N" / "Day N" ile başlıyor mu? Kitaplardaki QR'dan gelenler bunu arıyor.
