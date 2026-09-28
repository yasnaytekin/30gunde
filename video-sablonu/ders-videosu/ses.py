# Seslendirme ve zaman çizelgesi: senaryodaki metinleri maskotun sesiyle okur (sherpa-onnx, çevrim dışı),
# sahne sürelerini sese göre ayarlar, altyazı zamanlarını ve dudak senkronu verisini üretir.
# Doğrudan çağrılmaz; uret.py kullanır.
import hashlib, json, re, subprocess, tempfile
from pathlib import Path

import numpy as np
import soundfile as sf
from scipy.signal import resample_poly

HERE = Path(__file__).resolve().parent
MODELS = HERE / "modeller"
SR = 48000
ENV_FPS = 60  # dudak senkronu verisinin kare hızı

SESLER = {
    # tr: Piper "fahrettin" (erkek sesi; örneklerden seçildi). en: Kokoro "am_michael" (Apache-2.0), biraz inceltilir.
    "tr": {"tur": "piper", "klasor": "vits-piper-tr_TR-fahrettin-medium", "model": "tr_TR-fahrettin-medium.onnx", "hiz": 1.0, "perde": 1.0},
    "en": {"tur": "kokoro", "klasor": "kokoro-en-v0_19", "sid": 6, "hiz": 1.05, "perde": 1.26},
}

# Yalnızca seslendirmeye uygulanır; altyazı özgün metni gösterir. Sahnede "seslendirme" alanı varsa o okunur.
TELAFFUZ = {
    "tr": [
        (r"30gunde\.com\.tr", "otuzgünde nokta kom nokta tee ree"),
        (r"\bPython", "Pay tın"),
        (r"\bJavaScript", "Cava skript"),
        (r"\bNameError\b", "neym erör"),
        (r"\bTypeError\b", "tayp erör"),
        (r"\bIndexError\b", "indeks erör"),
        (r"\bf-string", "ef string"),
        (r"\btuple", "tapıl"),
        (r"\bChallenge", "Çelınc"),
        (r"\bstr\b", "string"),
        (r"\bfloat\b", "flot"),
        (r"\bbool\b", "bul"),
        (r"\btype\b", "tayp"),
        (r"\bround\b", "raund"),
        (r"\bmax\b", "maks"),
        (r"\bsum\b", "sam"),
        (r"\bappend\b", "apend"),
        (r"\bremove\b", "rimuv"),
        (r"\binsert\b", "insört"),
        (r"\bsorted\b", "sortıd"),
        (r"\bupper\b", "apır"),
        (r"\btitle\b", "taytıl"),
        (r"\bcount\b", "kaunt"),
        (r"\bindex\b", "indeks"),
        (r"\band\b", "end"),
        (r"\bKeyError\b", "kii erör"),
        (r"\bSyntaxError\b", "sintaks erör"),
        (r"\bIndentationError\b", "indenteyşın erör"),
        (r"\bDictionary\b", "Dikşıneri"),
        (r"\bdiscard\b", "diskard"),
        (r"\bkeys\b", "kiiz"),
        (r"\bvalues\b", "velyuz"),
        (r"\belse\b", "els"),
        (r"\bwhile\b", "vayl"),
        (r"\brange\b", "reync"),
        (r"\benumerate\b", "inyumıreyt"),
        (r"\bbreak\b", "breyk"),
        (r"\bcontinue\b", "kontinyu"),
        (r"\breturn\b", "ritörn"),
        (r"\bNone\b", "nan"),
        (r"\bTrue\b", "tru"),
        (r"\bFalse\b", "fols"),
        (r"\(\)", ""),
    ],
    "en": [
        (r"30gunde\.com\.tr", "thirty goon-deh dot com dot T R"),
        (r"30 Günde", "thirty goon-deh"),
        (r"\bNameError\b", "Name Error"),
        (r"\bTypeError\b", "Type Error"),
        (r"\bIndexError\b", "Index Error"),
        (r"\bKeyError\b", "Key Error"),
        (r"\bSyntaxError\b", "Syntax Error"),
        (r"\bIndentationError\b", "Indentation Error"),
        (r"\belif\b", "el if"),
        (r"\bf-strings?\b", "F string"),
        (r"\(\)", ""),
    ],
}

GAP = 0.30        # cümleler arası sessizlik (sn)
LEAD = 0.55       # sahne başından sesin başlamasına kadar
TAIL = 0.85       # ses bittikten sonra sahnenin sürmesi


def cumleler(text):
    """Metni cümlelere ayırır; her cümle altyazıda bir ya da (çok uzunsa) iki parça olur."""
    return [p.strip() for p in re.split(r"(?<=[.!?…])\s+", (text or "").strip()) if p.strip()]


def altyazi_parcalari(sentence):
    if len(sentence) <= 110:
        return [sentence]
    i = sentence.find(", ", len(sentence) // 2 - 25)
    return [sentence[: i + 1], sentence[i + 2:]] if i > 0 else [sentence]


def telaffuz(text, dil):
    for a, b in TELAFFUZ[dil]:
        text = re.sub(a, b, text)
    return text


class Ses:
    def __init__(self, dil, cache):
        import sherpa_onnx as so
        self.dil, self.cfg, self.cache = dil, SESLER[dil], Path(cache)
        self.cache.mkdir(parents=True, exist_ok=True)
        c, d = self.cfg, MODELS / SESLER[dil]["klasor"]
        if not d.exists():
            raise SystemExit(f"Ses modeli yok: {d}\nÖnce: bash {HERE / 'modelleri-indir.sh'}")
        if c["tur"] == "piper":
            m = so.OfflineTtsModelConfig(vits=so.OfflineTtsVitsModelConfig(model=str(d / c["model"]), tokens=str(d / "tokens.txt"), data_dir=str(d / "espeak-ng-data")), num_threads=4)
        else:
            m = so.OfflineTtsModelConfig(kokoro=so.OfflineTtsKokoroModelConfig(model=str(d / "model.onnx"), voices=str(d / "voices.bin"), tokens=str(d / "tokens.txt"), data_dir=str(d / "espeak-ng-data")), num_threads=4)
        self._tts = None
        self._cfg = so.OfflineTtsConfig(model=m)
        self._so = so

    def oku(self, text):
        """Tek bir cümleyi seslendirir → 48 kHz mono float32 (baştaki/sondaki sessizlik kırpılmış)."""
        key = hashlib.sha1(json.dumps([self.cfg, text], ensure_ascii=False).encode()).hexdigest()[:16]
        f = self.cache / f"{key}.wav"
        if not f.exists():
            if self._tts is None:
                self._tts = self._so.OfflineTts(self._cfg)
            a = self._tts.generate(text, sid=self.cfg.get("sid", 0), speed=self.cfg["hiz"])
            x = resample_poly(np.asarray(a.samples, dtype=np.float32), SR, a.sample_rate).astype(np.float32)
            sf.write(f, x, SR)
        x, _ = sf.read(f, dtype="float32")
        return trim(x)


def trim(x, thr=0.012, margin=0.03):
    idx = np.nonzero(np.abs(x) > thr)[0]
    if not len(idx):
        return x[:0]
    m = int(margin * SR)
    return x[max(0, idx[0] - m): idx[-1] + m]


def pitch_shift(x, factor):
    if abs(factor - 1) < 1e-3:
        return x
    import imageio_ffmpeg
    with tempfile.TemporaryDirectory() as d:
        a, b = Path(d) / "a.wav", Path(d) / "b.wav"
        sf.write(a, x, SR)
        subprocess.run([imageio_ffmpeg.get_ffmpeg_exe(), "-hide_banner", "-loglevel", "error", "-y", "-i", str(a),
                        "-af", f"rubberband=pitch={factor}:formant=preserved:pitchq=quality", str(b)], check=True)
        y, _ = sf.read(b, dtype="float32")
    n = len(x)
    return np.pad(y, (0, max(0, n - len(y))))[:n]


def segmentler(v):
    """giris + sahneler + cikis → ortak bir liste."""
    out = []
    if v.get("giris"):
        out.append({"tip": "giris", "tur": "giris", **v["giris"]})
    for i, s in enumerate(v["sahneler"]):
        out.append({"tip": "sahne", "i": i, **s})
    if v.get("cikis"):
        out.append({"tip": "cikis", "tur": "cikis", **v["cikis"]})
    return out


def zaman_cizelgesi(v, ses):
    """Her segmenti seslendirir, sahne sürelerini belirler. Dönüş: (zaman dict, ses dizisi)."""
    dil = v.get("dil", "tr")
    segs, parts, t = [], [], 0.0
    for seg in segmentler(v):
        tts_text = seg.get("seslendirme") or seg.get("anlatim", "")
        sub_sents = cumleler(seg.get("anlatim", ""))
        tts_sents = cumleler(tts_text)
        if len(tts_sents) != len(sub_sents):  # seslendirme metni farklı bölünüyorsa altyazıyla eşlemeyi bırak
            tts_sents = [" ".join(tts_sents)]; sub_sents = [" ".join(sub_sents)]
        lead = 1.3 if seg["tur"] == "giris" else LEAD
        t0 = t
        cur = t0 + lead
        sents, subs = [], []
        for sub, tt in zip(sub_sents, tts_sents):
            x = ses.oku(telaffuz(tt, dil))
            d = len(x) / SR
            parts.append((cur, x))
            sents.append([round(cur, 3), round(cur + d, 3)])
            pp = altyazi_parcalari(sub)
            tot = sum(len(p) for p in pp) or 1
            acc = 0
            for p in pp:
                a = cur + d * acc / tot; acc += len(p)
                subs.append({"a": round(a, 3), "b": round(cur + d * acc / tot + (GAP if acc == tot else 0), 3), "text": p})
            cur += d + GAP
        v0 = t0 + lead
        v1 = cur - GAP if sents else v0
        speech = v1 - v0
        seg_out = {"tip": seg["tip"], "tur": seg["tur"], "t0": round(t0, 3), "v0": round(v0, 3), "v1": round(v1, 3), "subs": subs, "cumleler": sents}
        if "i" in seg:
            seg_out["i"] = seg["i"]
        end = v1 + TAIL
        ek = seg.get("ekran") or {}
        if ek.get("kod"):
            n = len(ek["kod"].strip())
            fast = seg["tur"] == "cikti"
            typ0 = t0 + 0.45
            typ1 = typ0 + (0.25 if fast else min(3.2, max(0.8, n * 0.045)))
            seg_out.update(typ0=round(typ0, 3), typ1=round(typ1, 3))
            if ek.get("cikti"):
                ci = ek.get("cikti_cumle", 1 if seg["tur"] == "hata" else None)
                if fast:
                    out_at = v0 + 0.2
                elif ci is not None and ci < len(sents):
                    out_at = sents[ci][0]
                else:
                    out_at = v0 + 0.45 * speech
                out_at = max(out_at, typ1 + 0.35)
                seg_out["out_at"] = round(out_at, 3)
                end = max(end, out_at + 2.5)
            if ek.get("duzeltme") and sents:
                fix = max(sents[-1][0], seg_out.get("out_at", typ1) + 1.5)
                seg_out["fix_at"] = round(fix, 3)
                end = max(end, fix + 2.0)
        if seg["tur"] == "soru":
            seg_out["sayac"] = round(v1 + 0.25, 3)
            end = v1 + 3.6
        if seg["tur"] == "kapanis":
            end = v1 + 1.3
        if seg["tur"] == "cikis":
            end = v1 + 3.2
        end = max(end, t0 + 4.0)
        seg_out["t1"] = round(end, 3)
        segs.append(seg_out)
        t = end
    total = t
    voice = np.zeros(int(total * SR) + SR, dtype=np.float32)
    for st, x in parts:
        i = int(st * SR); voice[i:i + len(x)] += x
    voice = pitch_shift(voice, ses.cfg["perde"])
    peak = np.abs(voice).max() or 1
    voice = voice / peak * 0.89
    agiz, gorus = dudak(voice, total)
    return {"sure": round(total, 3), "env_fps": ENV_FPS, "segs": segs, "agiz": agiz, "gorus": gorus, "dil": dil}, voice


def dudak(voice, total):
    """Ses zarfından ağız açıklığı (0–100) ve kaba ağız şekli (k=kapalı, i, e, a, o, u) üretir."""
    n = int(total * ENV_FPS) + 1
    hop = SR // ENV_FPS
    win = int(0.04 * SR)
    rms = np.zeros(n); cen = np.zeros(n)
    freqs = np.fft.rfftfreq(win, 1 / SR)
    w = np.hanning(win)
    for k in range(n):
        seg = voice[k * hop: k * hop + win]
        if len(seg) < win:
            seg = np.pad(seg, (0, win - len(seg)))
        rms[k] = np.sqrt((seg ** 2).mean())
        sp = np.abs(np.fft.rfft(seg * w))
        band = (freqs > 150) & (freqs < 4000)
        cen[k] = (sp[band] * freqs[band]).sum() / (sp[band].sum() + 1e-9)
    db = 20 * np.log10(rms + 1e-6)
    voiced = db > -45
    ref = np.percentile(db[voiced], 90) if voiced.any() else -20
    o = np.clip((db - (ref - 28)) / 26, 0, 1)
    # hızlı açıl, biraz daha yavaş kapan
    sm = np.zeros(n); prev = 0
    for k in range(n):
        a = 0.6 if o[k] > prev else 0.35
        prev = prev + a * (o[k] - prev); sm[k] = prev
    agiz = [int(round(x * 100)) for x in sm]
    g = []
    for k in range(n):
        if sm[k] < 0.12:
            g.append("k")
        elif cen[k] > 1900:
            g.append("i" if sm[k] < 0.5 else "e")
        elif cen[k] < 1100:
            g.append("u" if sm[k] < 0.45 else "o")
        else:
            g.append("e" if sm[k] < 0.35 else "a")
    return agiz, "".join(g)
