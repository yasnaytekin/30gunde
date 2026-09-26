# Video şablonları

İki şablon var. İkisi de aynı yöntemle çalışır: sahneler bir HTML sayfasında `renderAt(t)` fonksiyonuyla
zamana göre çizilir, Playwright (Chromium) her kareyi çeker, ffmpeg kareleri videoya dönüştürür.
Böylece çıktı her seferinde birebir aynı olur.

Gerekenler: Python 3, `pip install playwright numpy scipy` + `playwright install chromium`, ffmpeg
(ders videosu `imageio-ffmpeg` paketindeki ffmpeg'i kullanır).
Yazı tipi olarak Poppins (Google Fonts) ve kod için DejaVu Sans Mono kurulu olmalı.

## ders-videosu/: gün gün konu anlatım videoları

Senaryodan **seslendirilmiş, maskotu konuşan, müzikli** videoyu tek komutla üretir:

```bash
cd video-sablonu/ders-videosu
bash modelleri-indir.sh                        # bir kez: seslendirme modelleri (~430 MB, GitHub'dan)
pip install sherpa-onnx soundfile numpy scipy pillow imageio-ffmpeg playwright
python3 uret.py python 1                       # Türkçe + İngilizce, yatay + dikey → 4 video
python3 uret.py python 1 --dil tr --yon h      # yalnızca Türkçe yatay
python3 uret.py python 1 --onizleme 5,30,90    # video yerine o anların ekran görüntüsü (is/… klasörüne)
```

Çıktı: `cikti/<kurs>/gun-XX/<kurs>-gun-XX-<dil>-<yatay|dikey>.mp4` ve her dil için `.srt` altyazı dosyası.
Yatay 1920x1080, dikey 1080x1920 (Reels/Shorts), 30 fps, H.264 + AAC, ses -16 LUFS.

Videonun akışı:

1. **Giriş (konu tanıtımı):** logo, "Gün N", günün başlığı ve "Bu derste" maddeleri; Piko konuyu tanıtır (senaryodaki `giris`).
2. **Sahneler:** senaryodaki sahneler. Kod yazılıyormuş gibi belirir (klavye sesiyle), "Çalıştır" düğmesine basılır,
   çıktı açılır. `hata` sahnesinde hata paneli kırmızı titrer; `ekran.duzeltme` varsa kod düzeltilip yeşile döner.
   `ekran.izgara: true` çıktıyı sahne ızgarası olarak çizer (`*` Piko, `#` duvar, `o` altın, `H` kalp).
   `soru` sahnesinde soru sorulduktan sonra 3-2-1 geri sayım olur.
3. **Çıkış:** "İnteraktif dersler için 30gunde.com.tr" kartı (senaryodaki `cikis`).

Ses ve konuşturma:

- **Seslendirme** çevrim dışı yapılır ([sherpa-onnx](https://github.com/k2-fsa/sherpa-onnx)): Türkçe Piper `tr_TR-fahrettin-medium`,
  İngilizce Kokoro `am_michael` (biraz inceltilmiş). Ayarlar ve telaffuz düzeltmeleri `ses.py` içinde (`SESLER`, `TELAFFUZ`;
  ör. "Python" → "Pay tın"). Bir sahnede özel okuma gerekirse sahneye `"seslendirme": "..."` yazılır, altyazı `anlatim` kalır.
- **Sahne süreleri sese göre** ayarlanır (senaryodaki `sure_sn` yalnızca sessiz önizlemede kullanılır). Altyazılar cümle cümle
  gerçek sesle eşzamanlıdır. Çıktının hangi cümlede açılacağı `ekran.cikti_cumle` (0'dan başlayan cümle sırası) ile seçilebilir.
- **Dudak senkronu:** ses zarfından ağız açıklığı ve kaba ağız şekli çıkarılır. `on` pozunda Piko'nun gerçek ağız kareleri
  (a, e, i, o, u, kapalı) kullanılır; ağzı açık pozlarda (konusma, mutlu, isaret, sasirma, tebrik, sol, sag) ağız parçası
  sesle açılıp kapanır; ağzı kapalı pozlarda (dusunme, uzgun) Piko konuşurken öne döner. Parçaları `araclar/agiz-rig.py`
  üretir (`maskotlar/piko-python/konusma-rig/`). Kodi için dudak senkronu henüz yok (pozlar olduğu gibi gösterilir).
- **Müzik ve efektler** `muzik.py` ile kodla sentezlenir (telifsiz): sakin bir döngü, konuşurken otomatik kısılır;
  geçiş, klavye, çıktı, hata, doğru cevap ve geri sayım efektleri.

Sessiz, hızlı önizleme için eski yol da çalışır: `python3 build.py <senaryo.json>`, `python3 preview.py h 3,20`, `python3 render.py h`.

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
