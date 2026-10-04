// 30 Günde JavaScript: deneme API'si (/demo-api/...).
// Etkileşimli derslerde hazır gelir. Kendi bilgisayarında denerken bu kodu betiğinin EN ÜSTÜNE yapıştır:
// fetch("/demo-api/...") istekleri internete çıkmadan buradaki verilerle cevaplanır.
const DEMO_API = {
  sehirler: [
    { ad: "İstanbul", bolge: "Marmara", nufus: 15655924, sicaklik: 19 },
    { ad: "Ankara", bolge: "İç Anadolu", nufus: 5864049, sicaklik: 15 },
    { ad: "İzmir", bolge: "Ege", nufus: 4479525, sicaklik: 23 },
    { ad: "Antalya", bolge: "Akdeniz", nufus: 2722103, sicaklik: 26 },
    { ad: "Gaziantep", bolge: "Güneydoğu Anadolu", nufus: 2193363, sicaklik: 21 },
    { ad: "Trabzon", bolge: "Karadeniz", nufus: 829123, sicaklik: 17 },
    { ad: "Erzurum", bolge: "Doğu Anadolu", nufus: 744200, sicaklik: 9 },
    { ad: "Eskişehir", bolge: "İç Anadolu", nufus: 921630, sicaklik: 13 },
  ],
  sorular: [
    { soru: "Güneş'e en yakın gezegen hangisi?", secenekler: ["Venüs", "Merkür", "Mars"], dogru: 1 },
    { soru: "Kızıl gezegen olarak bilinen hangisi?", secenekler: ["Mars", "Jüpiter", "Neptün"], dogru: 0 },
    { soru: "Halkalarıyla ünlü gezegen hangisi?", secenekler: ["Uranüs", "Satürn", "Dünya"], dogru: 1 },
    { soru: "JavaScript'te sabit hangi kelimeyle tanımlanır?", secenekler: ["let", "var", "const"], dogru: 2 },
    { soru: "Ay, Dünya'nın uydusu mudur?", secenekler: ["Evet", "Hayır"], dogru: 0 },
  ],
  seviyeler: {
    1: { seviye: 1, yildiz: 5, dusman: 1, hiz: 2 },
    2: { seviye: 2, yildiz: 8, dusman: 3, hiz: 3 },
    3: { seviye: 3, yildiz: 12, dusman: 5, hiz: 4 },
  },
  gorevler: [
    { id: 1, baslik: "Roketi boya", bitti: true },
    { id: 2, baslik: "Yakıt al", bitti: false },
    { id: 3, baslik: "Haritayı çiz", bitti: true },
    { id: 4, baslik: "Kalkış saatini seç", bitti: false },
  ],
  yazilar: [
    { id: 1, baslik: "İlk kodum", ozet: "console.log ile ekrana ilk mesajımı yazdım." },
    { id: 2, baslik: "Sayfayı canlandırdım", ozet: "Düğmeler, olaylar ve DOM ile sayfa artık tepki veriyor." },
    { id: 3, baslik: "Oyunum hazır", ozet: "Canvas ve oyun döngüsüyle Yıldız Avcısı'nı bitirdim." },
  ],
};

const gercekFetch = window.fetch.bind(window);
window.fetch = async (adres, ...digerleri) => {
  const url = new URL(String(adres), location.href);
  if (!url.pathname.startsWith("/demo-api/")) return gercekFetch(adres, ...digerleri);
  await new Promise((r) => setTimeout(r, 120)); // gerçek bir sunucu gibi biraz beklet
  const cevap = (veri, durum = 200) =>
    new Response(JSON.stringify(veri), { status: durum, headers: { "Content-Type": "application/json" } });
  const [, , ad, no] = url.pathname.split("/");
  if (ad === "sehirler") {
    const bolge = url.searchParams.get("bolge") || "";
    return cevap(DEMO_API.sehirler.filter((s) => s.bolge.includes(bolge)));
  }
  if (ad === "seviyeler") return DEMO_API.seviyeler[no] ? cevap(DEMO_API.seviyeler[no]) : cevap({ hata: "seviye yok" }, 404);
  if (ad === "hata") return cevap({ hata: "sunucu hatası" }, 500);
  if (ad in DEMO_API && !no) return cevap(DEMO_API[ad]);
  return cevap({ hata: "bulunamadı" }, 404);
};
