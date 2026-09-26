# Ders videosu için arka plan müziği, efektler ve miksaj. Tamamen kodla sentezlenir (numpy/scipy), telif yok.
# Müzik, maskot konuşurken otomatik olarak kısılır (ducking). Doğrudan çağrılmaz; uret.py kullanır.
import numpy as np
from scipy.signal import butter, sosfilt

SR = 48000


def tt(d):
    return np.arange(int(d * SR)) / SR


def lp(x, f, o=2):
    return sosfilt(butter(o, f, "lowpass", fs=SR, output="sos"), x)


def hp(x, f, o=2):
    return sosfilt(butter(o, f, "highpass", fs=SR, output="sos"), x)


def bp(x, lo, hi, o=2):
    return sosfilt(butter(o, [lo, hi], "bandpass", fs=SR, output="sos"), x)


def mid(n):
    return 440 * 2 ** ((n - 69) / 12)


class Track:
    def __init__(self, dur):
        self.n = int(dur * SR) + SR
        self.L = np.zeros(self.n); self.R = np.zeros(self.n)

    def add(self, sig, t0, gain=1.0, pan=0.0):
        i0 = int(t0 * SR)
        if i0 >= self.n:
            return
        if i0 < 0:
            sig = sig[-i0:]; i0 = 0
        n = min(len(sig), self.n - i0)
        l = np.cos((pan + 1) * np.pi / 4) * 1.414; r = np.sin((pan + 1) * np.pi / 4) * 1.414
        self.L[i0:i0 + n] += sig[:n] * gain * l
        self.R[i0:i0 + n] += sig[:n] * gain * r


# --- sesler ---
def epiano(freq, d=1.2):
    t = tt(d)
    s = np.sin(2 * np.pi * freq * t + 0.6 * np.sin(2 * np.pi * freq * 2 * t) * np.exp(-t * 5))
    s += 0.25 * np.sin(2 * np.pi * freq * 3 * t) * np.exp(-t * 7)
    return s * np.exp(-t * 2.6) * np.minimum(1, t / 0.004)


def bell(freq, d=1.4):
    t = tt(d)
    s = np.sin(2 * np.pi * freq * t) + .35 * np.sin(2 * np.pi * freq * 2.76 * t) * np.exp(-t * 6) + .2 * np.sin(2 * np.pi * freq * 5.4 * t) * np.exp(-t * 10)
    return s * np.exp(-t * 3.0) * np.minimum(1, t / 0.002)


def pad(notes, d, rng):
    t = tt(d); s = np.zeros(len(t))
    for n in notes:
        for det in (-0.08, 0.0, 0.07):
            f = mid(n + det)
            ph = rng.uniform(0, 6.28)
            s += np.sin(2 * np.pi * f * t + ph) + 0.3 * np.sin(2 * np.pi * 2 * f * t + ph) + 0.12 * np.sin(2 * np.pi * 3 * f * t + ph)
    s = lp(s, 1400)
    a = np.minimum(1, t / 0.6) * np.minimum(1, np.maximum(0, d - t) / 0.6)
    return s * a / (len(notes) * 3)


def bass(freq, d):
    t = tt(d)
    s = np.sin(2 * np.pi * freq * t) + 0.25 * np.sin(2 * np.pi * 2 * freq * t)
    return s * np.minimum(1, t / 0.01) * np.exp(-t / 0.6)


def kick():
    t = tt(0.35); f = 45 + 80 * np.exp(-t / 0.04)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.12)


def hat(rng, dec=0.025):
    t = tt(0.1)
    return hp(rng.standard_normal(len(t)), 8000) * np.exp(-t / dec)


def shaker(rng):
    t = tt(0.12)
    return bp(rng.standard_normal(len(t)), 5000, 11000) * np.sin(np.pi * t / 0.12) ** 2


# --- efektler ---
def whoosh(rng, d=0.45):
    t = tt(d); n = rng.standard_normal(len(t))
    out = np.zeros(len(t)); seg = int(SR * 0.015)
    for i in range(0, len(t), seg):
        f = 400 * (4000 / 400) ** (i / len(t))
        out[i:i + seg] = bp(n[i:i + seg * 3], f * 0.7, min(f * 1.5, 20000), 1)[:len(out[i:i + seg])]
    return out * np.sin(np.pi * t / d) ** 2


def pop():
    t = tt(0.14); f = 900 * np.exp(-t / 0.03) + 300
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.035)


def click(rng):
    t = tt(0.03)
    return bp(rng.standard_normal(len(t)), 2000, 7000) * np.exp(-t / 0.006)


def ding():
    return bell(mid(84), 1.2) * 0.6 + np.pad(bell(mid(91), 1.0), (0, int(0.2 * SR))) * 0.35


def buzz():
    t = tt(0.32)
    s = np.sign(np.sin(2 * np.pi * 110 * t)) * 0.5 + np.sin(2 * np.pi * 116 * t) * 0.5
    return lp(s, 1200) * np.minimum(1, t / 0.01) * np.exp(-t / 0.18)


def tick():
    t = tt(0.08)
    return np.sin(2 * np.pi * 1800 * t) * np.exp(-t / 0.015)


def sparkle(rng):
    out = np.zeros(int(1.2 * SR))
    for k, n in enumerate([84, 88, 91, 96, 100]):
        b = bell(mid(n), 0.8) * 0.5
        i = int(k * 0.07 * SR); out[i:i + len(b)] += b[:len(out) - i]
    return out


def muzik(total, zaman, seed=3):
    """Sakin, neşeli bir döngü: C – Am – F – G, 92 BPM. Giriş ve çıkışta biraz daha belirgin."""
    rng = np.random.default_rng(seed)
    tr = Track(total)
    bpm = 92; beat = 60 / bpm; bar = beat * 4
    chords = [[60, 64, 67, 71], [57, 60, 64, 67], [53, 57, 60, 64], [55, 59, 62, 65]]
    roots = [36, 33, 29, 31]
    arp = [0, 2, 1, 3, 2, 1, 3, 2]
    nbars = int(np.ceil(total / bar)) + 1
    end = total - 0.2
    for b in range(nbars):
        t0 = b * bar
        if t0 > end:
            break
        c = chords[b % 4]
        tr.add(pad(c, bar + 0.6, rng), t0, 0.55)
        tr.add(bass(mid(roots[b % 4]), bar * 0.95), t0, 0.35)
        for k in range(8):
            if t0 + k * beat / 2 > end - 0.3:
                break
            n = c[arp[k]] + 12
            tr.add(epiano(mid(n), 0.9), t0 + k * beat / 2, 0.16 if k % 2 == 0 else 0.11, pan=0.25 if k % 2 else -0.25)
        if b >= 1:  # ilk ölçü sadece melodi
            for k in range(4):
                if t0 + k * beat > end - 0.3:
                    break
                if k in (0, 2):
                    tr.add(kick(), t0 + k * beat, 0.32)
                tr.add(shaker(rng), t0 + k * beat + beat / 2, 0.05, pan=0.3)
                tr.add(hat(rng), t0 + k * beat, 0.03, pan=-0.3)
    # bitiş akoru
    tr.add(pad([48, 60, 64, 67, 72], 3.0, rng), max(0, total - 3.0), 0.7)
    tr.add(bell(mid(72), 2.5), max(0, total - 3.0), 0.25)
    m = np.stack([tr.L, tr.R])
    fade = np.ones(m.shape[1]); fe = int(total * SR)
    fade[fe:] = 0; fl = int(1.5 * SR); fade[fe - fl:fe] = np.linspace(1, 0, fl) ** 1.5
    return m * fade


def efektler(total, zaman, seed=5):
    rng = np.random.default_rng(seed)
    tr = Track(total)
    for k, s in enumerate(zaman["segs"]):
        if k > 0:
            tr.add(whoosh(rng), s["t0"] - 0.2, 0.10)
        if s["tur"] in ("giris", "cikis"):
            tr.add(sparkle(rng), s["t0"] + 0.25, 0.20)
        if s.get("typ0") is not None and s["tur"] != "cikti":
            t = s["typ0"]
            while t < s["typ1"]:
                tr.add(click(rng), t, 0.10, pan=rng.uniform(-0.3, 0.3)); t += rng.uniform(0.06, 0.11)
        if s.get("out_at") is not None:
            tr.add(buzz() if s["tur"] == "hata" else pop(), s["out_at"], 0.16 if s["tur"] == "hata" else 0.30)
            if s["tur"] == "cikti":
                tr.add(ding(), s["out_at"] + 0.05, 0.16)
        if s.get("fix_at") is not None:
            tr.add(ding(), s["fix_at"] + 0.3, 0.18)
        if s.get("sayac") is not None:
            for j in range(3):
                tr.add(tick(), s["sayac"] + j, 0.22)
        if s["tur"] == "kapanis":
            tr.add(sparkle(rng), s["t0"] + 0.4, 0.18)
    return np.stack([tr.L, tr.R])


def miksaj(voice, zaman):
    """Ses + müzik (konuşurken kısılır) + efektler → stereo float32, 48 kHz."""
    total = zaman["sure"]
    n = int(total * SR) + int(0.5 * SR)
    mus = muzik(total, zaman)[:, :n]
    fx = efektler(total, zaman)[:, :n]
    v = np.zeros(n); v[:min(n, len(voice))] = voice[:n]
    mus = np.pad(mus, ((0, 0), (0, n - mus.shape[1])))
    fx = np.pad(fx, ((0, 0), (0, n - fx.shape[1])))
    mus /= (np.abs(mus).max() or 1)
    # konuşma zarfına göre müzik seviyesi: konuşurken 0.10, arada 0.24, giriş/çıkışın konuşmasız anlarında 0.34
    target = np.full(n, 0.24)
    for s in zaman["segs"]:
        if s["tur"] in ("giris", "cikis"):
            a, b = int(s["t0"] * SR), int(s["t1"] * SR); target[a:b] = 0.34
    hop = 480
    env = np.array([np.abs(v[i:i + hop]).max() for i in range(0, n, hop)])
    talk = np.convolve(env > 0.02, np.ones(40), "same") > 0  # ±0,2 sn tampon
    talk = np.repeat(talk, hop)[:n]
    target = np.where(talk, 0.10, target)
    g = np.zeros(n); prev = target[0]
    # yumuşak geçiş (atak ~80 ms, bırakış ~500 ms), bloklar hâlinde
    blk = 240
    for i in range(0, n, blk):
        tgt = target[i]
        a = 1 - np.exp(-blk / (SR * (0.08 if tgt < prev else 0.5)))
        prev = prev + a * (tgt - prev); g[i:i + blk] = prev
    out = np.stack([v, v]) * 0.95 + mus * g + fx * 0.9
    peak = np.abs(out).max()
    if peak > 0.98:
        out *= 0.98 / peak
    return out.T.astype(np.float32)
