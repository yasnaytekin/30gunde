# 30 Günde: Python ve JavaScript kurs içeriği

[30gunde.com.tr](https://30gunde.com.tr) kurslarının içerik deposu: maskot pozları, görseller, müfredatlar,
gün gün konu anlatımları ve konu anlatım videoları için senaryolar ile video şablonları.

| | 30 Günde Python | 30 Günde JavaScript |
|---|---|---|
| Maskot | **Piko**: mavi-sarı sevimli yılan | **Kodi**: göğsünde "JS" yazan astronot robot |
| Tema | Macera haritası: kamptan Python Dağı'na | Uzay yolculuğu: Kalkış Üssü'nden JavaScript Yıldızı'na |
| Müfredat | [python/mufredat.md](python/mufredat.md) | [javascript/mufredat.md](javascript/mufredat.md) |
| Günler | [python/gunler/](python/gunler/) | [javascript/gunler/](javascript/gunler/) |
| Video senaryoları | [python/video-senaryolari/](python/video-senaryolari/) | [javascript/video-senaryolari/](javascript/video-senaryolari/) |

## Klasörler

```
maskotlar/
  pozlar.json               # iki maskotun pozları, ne zaman kullanılacakları, dudak senkronu kareleri
  piko-python/              # pozlar/, yuzler/ (a, e, i, o, u... ağız şekilleri), avatarlar/
  kodi-javascript/          # pozlar/, konusma-kareleri/ (1–7), kahraman.png, kaynak/poz-sayfasi.png
gorseller/
  python/                   # harita bölgeleri (webp + yol verisi), rozetler, logo, paylaşım görseli
  javascript/               # bölge gezegenleri, arka planlar, simgeler, paylaşım görseli, kaynak/ (orijinaller)
python/ ve javascript/
  mufredat.md               # 30 günün bölge bölge özeti
  gunler/gun-XX.md          # konu anlatımı, örnekler, görevler (çözümleriyle), challenge, proje adımları
  veri/gun-XX.json          # aynı içerik makinece okunur biçimde (kontrol kodları dahil); veri/kurs.json
  video-senaryolari/        # gun-XX.json (sahne sahne senaryo) + gun-XX.md (okunur hali)
video-sablonu/
  ders-videosu/             # senaryodan video üreten şablon (yatay 16:9 ve dikey 9:16)
  tanitim-videosu/          # 30 sn'lik tanıtım videosunun kaynağı (sahneler, kodla üretilen müzik)
araclar/
  disa-aktar.py             # içeriği uygulamanın lessons.json dosyalarından yeniden üretir
  senaryo-dogrula.py        # senaryoları doğrular (kodları çalıştırıp çıktıyı karşılaştırır), .md üretir
  agiz-rig.py               # Piko pozlarından dudak senkronu parçaları üretir
  SENARYO-REHBERI.md        # yeni senaryo yazarken uyulacak kurallar ve JSON şeması
```

## Konu anlatım videosu üretmek

1. Senaryoyu oku ya da düzenle: `python/video-senaryolari/gun-01.md` (kaynağı `.json`); İngilizcesi `python/video-senaryolari/en/`.
2. Doğrula: `python3 araclar/senaryo-dogrula.py python 1-1`
3. Videoyu üret (seslendirme, konuşan maskot, müzik, giriş ve 30gunde.com.tr çıkışı dahil):
   `cd video-sablonu/ders-videosu && python3 uret.py python 1` → `cikti/python/gun-01/` (ayrıntılar: [video-sablonu/README.md](video-sablonu/README.md))

Her senaryo 8–14 sahneden oluşur (açılış, anlatım, kod ve çıktı, sık yapılan hata, mini soru, görevler,
özet, kapanış). Toplam süre: Python 30 video ~70 dk, JavaScript 30 video ~79 dk.

## Notlar

- Python'da Keşif Adası (ada), Bilgi Limanı (liman) ve Python Dağı (dag) bölgelerinin harita görselleri
  henüz yok; yalnızca yol verileri (`.road.json`) var. Görseller eklenince 16–30. gün senaryolarının açılış
  sahnelerine `ekran.gorsel` olarak bağlanabilir (sahnelerdeki yönetmen notları yerini gösteriyor).
- Piko pozları uygulamadaki boyutlarıyla (~300 px) eklendi; Kodi pozları poz sayfasındaki özgün boyutlarında
  (PNG, kayıpsız). Daha büyük boyutlar gerekirse kaynak çizimlerden yeniden kesilmeli.
- Görev çözümleri bilinçli olarak bu depoda açık durur.

© 30 Günde. Maskotlar, görseller ve ders içerikleri 30 Günde'ye aittir; izin alınmadan kullanılamaz.
