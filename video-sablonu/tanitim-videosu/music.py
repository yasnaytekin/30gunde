"""30 sn'lik telifsiz lansman müziği + efektler — tamamen kodla sentezlenir (numpy/scipy)."""
import numpy as np
from scipy.signal import butter, sosfilt
from scipy.io import wavfile

SR = 48000
DUR = 30.0
N = int(SR * DUR)
BPM = 120
BEAT = 60 / BPM
BAR = BEAT * 4
rng = np.random.default_rng(7)
L = np.zeros(N); R = np.zeros(N)

def add(sig, t0, gain=1.0, pan=0.0):
    i0 = int(t0 * SR)
    if i0 >= N: return
    if i0 < 0: sig = sig[-i0:]; i0 = 0
    n = min(len(sig), N - i0)
    l = np.cos((pan + 1) * np.pi / 4); r = np.sin((pan + 1) * np.pi / 4)
    L[i0:i0 + n] += sig[:n] * gain * l * 1.414
    R[i0:i0 + n] += sig[:n] * gain * r * 1.414

def tt(d): return np.arange(int(d * SR)) / SR
def env(d, a=0.005, dec=0.2):
    t = tt(d); e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-t / dec); return e
def bp(x, lo, hi, o=2): return sosfilt(butter(o, [lo, hi], "bandpass", fs=SR, output="sos"), x)
def lp(x, f, o=2): return sosfilt(butter(o, f, "lowpass", fs=SR, output="sos"), x)
def hp(x, f, o=2): return sosfilt(butter(o, f, "highpass", fs=SR, output="sos"), x)
def mid(n): return 440 * 2 ** ((n - 69) / 12)

# --- instruments ---
def kick():
    t = tt(0.45); f = 45 + 110 * np.exp(-t / 0.045)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-t / 0.16) + 0.3 * np.sin(ph) * np.exp(-t / 0.02)
def clap():
    t = tt(0.25); n = rng.standard_normal(len(t))
    e = np.exp(-t / 0.07) * (1 + 0.6 * ((t % 0.012) < 0.004) * (t < 0.03))
    return bp(n, 900, 4000) * e * 0.9
def hat(dec=0.03):
    t = tt(0.12); return hp(rng.standard_normal(len(t)), 7000) * np.exp(-t / dec) * 0.5
def pluck(freq, d=0.5, bright=1.0):
    t = tt(d); s = np.zeros(len(t))
    for k, a in [(1, 1), (2, .5 * bright), (3, .28 * bright), (4, .15 * bright), (5, .08 * bright)]:
        s += a * np.sin(2 * np.pi * freq * k * t) * np.exp(-t * (6 + 4 * k))
    return s * np.minimum(1, t / 0.003)
def bell(freq, d=1.2):
    t = tt(d)
    s = np.sin(2 * np.pi * freq * t) + .4 * np.sin(2 * np.pi * freq * 2.76 * t) * np.exp(-t * 6) + .25 * np.sin(2 * np.pi * freq * 5.4 * t) * np.exp(-t * 10)
    return s * np.exp(-t * 3.2) * np.minimum(1, t / 0.002)
def saw(freq, d, harm=12):
    t = tt(d); s = np.zeros(len(t))
    for k in range(1, harm + 1): s += np.sin(2 * np.pi * freq * k * t) / k
    return s
def bass_note(freq, d):
    s = saw(freq, d, 8); s = lp(s, 700)
    t = tt(d); return s * np.minimum(1, t / 0.005) * np.exp(-t / 0.35) * 0.9
def pad(notes, d):
    t = tt(d); s = np.zeros(len(t))
    for n in notes:
        for det in (-0.12, 0.0, 0.11):
            s += saw(mid(n + det), d, 6)
    s = lp(s, 1800)
    a = np.minimum(1, t / 0.25) * np.minimum(1, (d - t) / 0.3)
    return s * a / (len(notes) * 3)
def noise_sweep(d, f0, f1, rise=True):
    t = tt(d); n = rng.standard_normal(len(t)); out = np.zeros(len(t))
    # piecewise band sweep
    seg = int(SR * 0.02)
    for i in range(0, len(t), seg):
        x = i / len(t); f = f0 * (f1 / f0) ** x
        out[i:i + seg] = bp(n[i:i + seg * 3], f * 0.7, min(f * 1.4, SR / 2 - 100), 1)[:len(out[i:i + seg])]
    e = (t / d) ** 2 if rise else np.sin(np.pi * t / d) ** 1.5
    return out * e

# --- harmony: C  G  Am  F (per bar) ---
CH = [[60, 64, 67], [55, 59, 62, 67], [57, 60, 64], [53, 57, 60]]
ROOT = [36, 43, 45, 41]
nbars = int(np.ceil(DUR / BAR))

# sidechain envelope (duck under kick)
duck = np.ones(N)
def kick_at(t0, g=1.0):
    add(kick(), t0, 0.95 * g)
    i0 = int(t0 * SR); d = tt(0.3); e = 1 - 0.55 * np.exp(-d / 0.09)
    n = min(len(e), N - i0);
    if n > 0: duck[i0:i0 + n] = np.minimum(duck[i0:i0 + n], e[:n])

music_L = np.zeros(N); music_R = np.zeros(N)
DROP = 4.0; BREAK = 26.5; CTA = 27.0

for b in range(nbars):
    t0 = b * BAR
    ch = CH[b % 4]; root = ROOT[b % 4]
    # pad throughout
    add(pad(ch, BAR + 0.1), t0, 0.28 if t0 >= DROP else 0.26, 0)
    # plucked 16th arpeggio (intro too)
    arp = [ch[0] + 12, ch[1] + 12, ch[2] + 12, ch[1] + 12]
    for s in range(16):
        ts = t0 + s * BEAT / 4
        if ts >= DUR - 0.6: break
        if BREAK <= ts < CTA: continue
        n = arp[s % 4] + (12 if s % 8 == 7 else 0)
        add(pluck(mid(n), 0.35, 0.8), ts, 0.14 if ts < DROP else 0.085, -0.35 if s % 2 else 0.35)
    for k in range(4):
        tb = t0 + k * BEAT
        if tb >= DUR - 0.2: break
        if tb < DROP:
            # intro: soft hats only on 8ths off-beat
            if tb >= 1.9: add(hat(), tb + BEAT / 2, 0.25, 0.3)
            continue
        if BREAK <= tb < CTA: continue
        if tb >= 29.0: continue
        kick_at(tb)
        if k in (1, 3): add(clap(), tb, 0.45, 0.1)
        add(hat(), tb + BEAT / 2, 0.35, 0.3)
        add(hat(0.012), tb + BEAT / 4, 0.18, -0.3); add(hat(0.012), tb + 3 * BEAT / 4, 0.18, -0.3)
        # bass: 8ths, root/octave
        for e8 in range(2):
            n = root + (12 if e8 else 0)
            add(bass_note(mid(n), BEAT / 2 * 0.95), tb + e8 * BEAT / 2, 0.42, 0)

# lead melody (bell) from drop to break — simple catchy motif, in C major
MEL = [  # (beat offset within 2-bar phrase, midi, length beats)
    (0, 76, 1), (1, 79, .5), (1.5, 76, .5), (2, 74, 1), (3, 72, 1),
    (4, 74, 1), (5, 76, .5), (5.5, 79, .5), (6, 81, 1.5), (7.5, 79, .5),
]
MEL2 = [(0, 76, 1), (1, 79, .5), (1.5, 81, .5), (2, 84, 1), (3, 81, 1),
        (4, 79, 1), (5, 77, .5), (5.5, 76, .5), (6, 74, 1.5), (7.5, 72, .5)]
ph = 0
t = 8.0
while t < BREAK - 0.1:
    motif = MEL if ph % 2 == 0 else MEL2
    for off, n, ln in motif:
        ts = t + off * BEAT
        if ts >= BREAK - 0.1: break
        add(bell(mid(n), 0.9), ts, 0.13, 0.15)
    ph += 1; t += 2 * BAR

# ---- master music: sidechain ----
L *= duck; R *= duck

# ---- SFX (not ducked) ----
def whoosh(tc):
    s = noise_sweep(0.55, 400, 6000, rise=False); add(s, tc - 0.38, 0.22, -0.4); add(s[::-1] * 0, tc, 0)
def click(tc, g=0.35):
    t = tt(0.03); s = hp(rng.standard_normal(len(t)), 2500) * np.exp(-t / 0.005); add(s, tc, g, 0.1)
def key(tc, i):
    t = tt(0.05); f = 1800 + (i * 137) % 900
    s = (hp(rng.standard_normal(len(t)), 2000) * 0.6 + np.sin(2 * np.pi * f * t) * 0.3) * np.exp(-t / 0.008)
    add(s, tc, 0.13, (i % 3 - 1) * 0.3)
def popfx(tc, pitch=1.0):
    t = tt(0.12); f = (500 + 900 * (t / 0.12)) * pitch
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.035); add(s, tc, 0.18, 0)
def chime(tc):
    for i, n in enumerate([72, 76, 79, 84]): add(bell(mid(n), 1.2), tc + i * 0.07, 0.2, -0.2 + i * 0.13)
def coin(tc):
    add(pluck(mid(88), 0.3, .3), tc, 0.16, .3); add(pluck(mid(93), 0.5, .3), tc + 0.08, 0.18, .3)
def sparkle(tc, n=10, seed=1):
    r = np.random.default_rng(seed)
    for i in range(n): add(bell(mid(int(84 + r.integers(0, 12))), 0.5), tc + i * 0.045 + r.random() * 0.02, 0.06, r.uniform(-.7, .7))
def crash(tc, g=0.3):
    t = tt(2.0); s = hp(rng.standard_normal(len(t)), 5000) * np.exp(-t / 0.4); add(s, tc, g * 0.5, 0.3); add(hp(rng.standard_normal(len(t)), 5000) * np.exp(-t / 0.4), tc, g * 0.5, -0.3)
def impact(tc):
    t = tt(1.2); f = 30 + 60 * np.exp(-t / 0.1)
    s = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.5); add(s, tc, 0.7, 0)

# typing (scene 1: 0.35–1.75, 44 chars; scene 4: 12.55–13.75, 24 chars)
CODE_LEN = 51
for i in range(1, CODE_LEN + 1):
    if i % 1 == 0: key(0.35 + 1.4 * i / CODE_LEN, i)
for i in range(1, 25): key(12.55 + 1.2 * i / 24, i + 7)
click(1.9, 0.5)
for i in range(12): click(2.05 + i * 0.08, 0.08)  # output ticks
click(14.0, 0.5); chime(14.15); coin(14.3)
for tc in (4, 8, 12, 16, 20, 24, 27): whoosh(tc)
crash(4.0, 0.2); impact(4.0)
for i in range(3): popfx(5.3 + i * 0.18, 1 + i * .12)
for i in range(3): popfx(14.5 + i * 0.15, 1.1 + i * .1)
for i in range(6): popfx(16.35 + i * 0.12, 0.9 + i * .08)
popfx(18.7, 1.3)
for i in range(7): popfx(20.3 + i * 0.13, 0.9 + i * .07)
sparkle(4.85, 10, 1); sparkle(21.5, 14, 2); sparkle(27.25, 12, 3)
# riser into CTA
add(noise_sweep(1.0, 300, 9000, rise=True), 26.0, 0.3, 0)
for i in range(8): add(pluck(mid(72 + i), 0.2, .6), 26.0 + i * 0.125, 0.07 + i * 0.01, 0)
impact(27.0); crash(27.0, 0.22)
add(pad([60, 64, 67, 72], 3.0), 27.0, 0.35, 0)
add(bass_note(mid(36), 2.5) * 1.0, 27.0, 0.5)
for i, n in enumerate([72, 76, 79, 84, 88]): add(bell(mid(n), 2.5), 27.0 + i * 0.06, 0.12, -0.4 + 0.2 * i)
# final gentle outro kicks
for k in range(4): kick_at(27.0 + k * BEAT, 0.6)

# master
mix = np.stack([L, R], 1)
mix = hp(mix.T, 30).T
fade_in = np.minimum(1, np.arange(N) / (0.05 * SR))
fade_out = np.clip((DUR - np.arange(N) / SR) / 1.2, 0, 1)
mix *= (fade_in * fade_out)[:, None]
mix = np.tanh(mix * 1.1) / np.tanh(1.1)  # soft clip glue
mix /= np.max(np.abs(mix)) / 0.89
wavfile.write("music.wav", SR, (mix * 32767).astype(np.int16))
print("ok", mix.shape, float(np.sqrt(np.mean(mix ** 2))))
