# Video senaryosu yazım rehberi

Her gün için 90–180 saniyelik kısa bir konu anlatım videosu. Senaryo JSON olarak yazılır
(`<kurs>/video-senaryolari/gun-XX.json`), okunabilir Markdown'ı doğrulayıcı üretir:

```
python3 araclar/senaryo-dogrula.py python 1-15
```

## Ses ve ton
- Anlatıcı kursun maskotudur ve birinci tekil konuşur: Python'da **Piko**, JavaScript'te **Kodi**.
  ("Selam, ben Kodi! Bugün döngüleri öğreniyoruz.")
- Hedef kitle 12 yaş ve üstü. Sıcak, kısa cümleler; "sen" diye hitap. Türkçe karakterler doğru.
- JavaScript tarafı uzay yolculuğu temalı (roket, gezegen, yıldız), Python tarafı macera haritası temalı (kamp, köy, orman, kale...).
- Seslendirme ekrandakini tekrar okumaz; ekranda kod varken ne yaptığını anlatır.
- Emoji yok. Kurs erişimi anlatılacaksa "erken erişim" denir; fiyat ya da "bedava" vurgusu yapılmaz.
- Kod gösterirken satır satır anlatmak için `vurgu_satirlari` kullan.

## Akış (öneri)
1. `acilis`: maskot el sallar/konuşur, bölge görseli arka planda, günün başlığı. Merak uyandıran bir soru.
2. `anlatim` / `kod` / `cikti`: dersin 3–4 ana fikri, her biri kısa bir kod örneğiyle ve çıktısıyla.
3. `hata`: yeni başlayanların en sık yaptığı hata ve hata mesajının anlamı.
4. `soru`: izleyiciye mini soru ("Sence bu kod ne yazdırır?"), cevap bir sonraki sahnede.
5. `gorev`: günün görevlerini tanıt (çözümü verme).
6. `ozet`: 3 maddelik özet.
7. `kapanis`: yarının konusu ipucu, maskot tebrik/el sallama pozu.

Toplam 8–14 sahne; her sahne 4–20 sn. Seslendirme saniyede ~2,3 kelime (10 sn ≈ 23 kelime).

## JSON şeması
```json
{
  "kurs": "python",               // python | javascript
  "gun": 1,
  "baslik": "Python ile tanışma",
  "maskot": "piko",               // python → piko, javascript → kodi
  "ozet": "Videonun 1–2 cümlelik özeti.",
  "hedef_sure_sn": 150,
  "sahneler": [
    {
      "no": 1,
      "tur": "acilis",            // acilis | anlatim | kod | cikti | hata | soru | gorev | ozet | kapanis
      "sure_sn": 8,
      "anlatim": "Seslendirme metni (maskotun ağzından).",
      "ekran": {
        "baslik": "Gün 1: Python ile tanışma",
        "maddeler": ["...", "..."],
        "kod": "print(\"Merhaba!\")\n",
        "dil": "python",          // python | js | html
        "vurgu_satirlari": [1],
        "cikti": "Merhaba!",
        "html": "<button id=\"b\">Tıkla</button>",   // JS sayfa örneklerinde isteğe bağlı
        "gorsel": "gorseller/python/harita/kamp.webp"  // repodaki gerçek bir dosya
      },
      "maskot": { "poz": "konusma", "konum": "sag", "not": "isteğe bağlı sahne notu" },  // konum: sol | sag | alt-sol | alt-sag | orta | yok
      "calistir": true,           // kod sahnesinde kod çalıştırılıp "cikti" ile karşılaştırılır
      "yonetmen_notu": "İsteğe bağlı: animasyon/geçiş önerisi."
    }
  ]
}
```

Poz adları (`maskotlar/pozlar.json`): on, sol, sag, konusma, mutlu, dusunme, sasirma, tebrik, uzgun, isaret;
Kodi'de ayrıca el-sallama.

## Kod kuralları
- Kodlar dersin kendisinden gelir (anlatım bölümleri ve örnekler); kısa tutulur (en çok ~10 satır).
- `"calistir": true` olan kod gerçekten çalışır ve `cikti` birebir doğru olmalı (doğrulayıcı kontrol eder).
  Python kodu `python3` ile, JavaScript kodu `node` ile çalıştırılır.
- `input()` kullanan Python kodu ve DOM/`document` kullanan JavaScript kodu çalıştırılamaz: bunlarda
  `"calistir": false` yap ve `cikti` alanına ekranda görünmesi gerekeni yaz.
- `hata` sahnesinde `"calistir": true` ise kodun gerçekten hata vermesi beklenir.

## Sesli video için ek alanlar (isteğe bağlı)
`video-sablonu/ders-videosu/uret.py` bu alanları kullanır; doğrulayıcı da denetler.

```json
{
  "dil": "tr",                    // tr | en; İngilizce senaryo <kurs>/video-senaryolari/en/gun-XX.json
  "giris": { "anlatim": "Gün 1: ... Bu derste ... öğreneceksin.", "maddeler": ["...", "...", "..."] },
  "cikis": { "anlatim": "Bu dersin interaktif hâli 30gunde.com.tr'de seni bekliyor...", "baslik": "İnteraktif dersler için",
             "adres": "30gunde.com.tr", "maddeler": ["...", "...", "..."] },
  "sahneler": [{
    "seslendirme": "Yalnızca okunacak metin (telaffuz için); altyazıda anlatim görünür. Cümle sayısı aynı olmalı.",
    "ekran": {
      "cikti_cumle": 3,           // çıktı paneli kaçıncı cümlede açılsın (0'dan başlar); yoksa konuşmanın ortasında
      "izgara": true,             // çıktıyı sahne ızgarası olarak da çiz (* Piko, # duvar, o altın, H kalp)
      "duzeltme": { "kod": "print(\"Merhaba!\")\n", "cikti": "Merhaba!" }  // hata sahnesi: son cümlede kod düzelir
    }
  }]
}
```

- `giris`: videonun başındaki konu tanıtımı; 1–2 cümle, 3 kısa madde.
- `cikis`: videonun sonunda interaktif dersler için 30gunde.com.tr'ye yönlendirme. Fiyat ya da "bedava" vurgusu yok.
- Sahne süreleri seslendirmeye göre ayarlanır; `sure_sn` yine de doğru tahmin edilmeli (sessiz önizleme ve denetim için).
- İngilizce senaryoda kod içindeki metinler de İngilizce olur (`print("Hello World!")`) ve çıktılar yeniden doğrulanır.
