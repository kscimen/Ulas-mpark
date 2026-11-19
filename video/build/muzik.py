"""Özgün fon müziği ve ses efektleri (numpy ile sentez; harici lisans gerektirmez).
Okur: build/out/timeline.json  ·  Yazar: build/out/muzik.wav, build/out/sfx_*.wav"""
import json, os, wave
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'build', 'out')
SR = 48000
tl = json.load(open(os.path.join(OUT, 'timeline.json'), encoding='utf-8'))
T = tl['total'] + 1.0
N = int(T * SR)
rng = np.random.default_rng(7)

def yaz(path, x):
    x = np.asarray(x, dtype=np.float64)
    if x.ndim == 1:
        x = np.stack([x, x], 1)
    x = x / max(1e-9, np.abs(x).max()) * 0.89
    w = wave.open(path, 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
    w.writeframes((x * 32767).astype('<i2').tobytes()); w.close()

def hz(n):  # MIDI -> Hz
    return 440.0 * 2 ** ((n - 69) / 12)

BPM = 92.0
beat = 60.0 / BPM
bar = 4 * beat
# D majör: Dmaj9 – Bm9 – Gmaj9 – Asus2  (her akor 2 ölçü)
chords = [[50, 57, 62, 66, 69, 76], [47, 54, 62, 66, 69, 73], [43, 50, 59, 62, 66, 69], [45, 52, 57, 59, 64, 71]]
t = np.arange(N) / SR
L = np.zeros(N); R = np.zeros(N)

def sc(tp):
    return [s for s in tl['scenes'] if s['type'] == tp]
t_ritim0 = sc('sensor')[0]['start'] - 0.2
t_ritim1 = sc('pilot')[0]['start'] + sc('pilot')[0]['dur']
t_final = sc('final')[0]['start']

# --- pad ---
clen = 2 * bar
nch = int(np.ceil(T / clen)) + 1
env_len = int(clen * SR)
for i in range(nch):
    t0 = i * clen
    if t0 > t_final + 0.5:
        break
    last = t0 + clen > t_final
    ln = int((clen + (8.0 if last else 1.6)) * SR)
    s0 = int(t0 * SR); s1 = min(N, s0 + ln); n = s1 - s0
    if n <= 0: continue
    tt = np.arange(n) / SR
    env = np.minimum(1, tt / 1.2) * np.clip((ln / SR - tt) / 1.6, 0, 1)
    ch = chords[i % 4] if not last else chords[0]
    for k, note in enumerate(ch):
        f = hz(note)
        for det, pan in ((-0.12, 0.3), (0.12, 0.7)):
            ph = rng.uniform(0, 6.28)
            v = np.sin(2 * np.pi * (f * (1 + det / 100)) * tt + ph) + 0.25 * np.sin(2 * np.pi * 2 * f * tt + ph)
            v *= env * (0.11 if k == 0 else 0.07)
            L[s0:s1] += v * (1 - pan); R[s0:s1] += v * pan

# --- bas (ölçü başı) ---
for i in range(int(T / bar)):
    t0 = i * bar
    if t0 < 2 * bar or t0 > t_final + 2 * bar: continue
    ch = chords[int(t0 // clen) % 4] if t0 < t_final else chords[0]
    s0 = int(t0 * SR); n = min(N - s0, int(bar * SR))
    tt = np.arange(n) / SR
    v = np.sin(2 * np.pi * hz(ch[0] - 12) * tt) * np.exp(-tt * 1.4) * np.minimum(1, tt / 0.02) * 0.22
    L[s0:s0 + n] += v; R[s0:s0 + n] += v

# --- arpej (sekizlik) ---
step = beat / 2
for i in range(int(T / step)):
    t0 = i * step
    if t0 < sc('acilis')[0]['start'] + 1 or t0 > t_final + 1.5: continue
    ch = chords[int(t0 // clen) % 4]
    pat = [3, 4, 5, 4, 2, 4, 5, 3]
    note = ch[pat[i % 8]] + 12
    s0 = int(t0 * SR); n = min(N - s0, int(0.9 * SR))
    tt = np.arange(n) / SR
    f = hz(note)
    v = (np.sin(2 * np.pi * f * tt) + 0.3 * np.sin(2 * np.pi * 2 * f * tt) * np.exp(-tt * 12)) * np.exp(-tt * 5.5)
    v *= np.minimum(1, tt / 0.004) * (0.075 if i % 2 == 0 else 0.055)
    pan = 0.35 + 0.3 * ((i % 4) / 3)
    L[s0:s0 + n] += v * (1 - pan); R[s0:s0 + n] += v * pan

# --- yumuşak ritim (vuruş + hafif hi-hat) ---
for i in range(int(T / beat)):
    t0 = i * beat
    if not (t_ritim0 <= t0 <= t_ritim1): continue
    s0 = int(t0 * SR); n = min(N - s0, int(0.35 * SR)); tt = np.arange(n) / SR
    k = np.sin(2 * np.pi * (48 + 60 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 9) * 0.28
    L[s0:s0 + n] += k; R[s0:s0 + n] += k
    s1 = int((t0 + beat / 2) * SR); n2 = min(N - s1, int(0.06 * SR))
    if n2 > 0:
        hh = rng.normal(0, 1, n2) * np.exp(-np.arange(n2) / SR * 70) * 0.025
        hh = np.diff(np.concatenate([[0], hh]))  # yüksek geçiren
        L[s1:s1 + n2] += hh * 0.8; R[s1:s1 + n2] += hh

# --- yankı (üstel gürültü IR, FFT konvolüsyon) ---
irn = int(2.4 * SR)
ir_t = np.arange(irn) / SR
def rev(x, seed):
    ir = np.random.default_rng(seed).normal(0, 1, irn) * np.exp(-ir_t * 2.6)
    ir[:int(0.012 * SR)] = 0
    m = 1 << int(np.ceil(np.log2(len(x) + irn)))
    y = np.fft.irfft(np.fft.rfft(x, m) * np.fft.rfft(ir, m), m)[:len(x)]
    return y / np.abs(y).max() * np.abs(x).max()
L2 = 0.72 * L + 0.42 * rev(L, 1)
R2 = 0.72 * R + 0.42 * rev(R, 2)
# giriş/çıkış
fade = np.ones(N)
fi = int(1.5 * SR); fade[:fi] = np.linspace(0, 1, fi)
fo_s = int((tl['total'] - 2.5) * SR); fade[fo_s:] = np.linspace(1, 0, N - fo_s)
yaz(os.path.join(OUT, 'muzik.wav'), np.stack([L2 * fade, R2 * fade], 1))

# --- efektler ---
def env_exp(n, k): return np.exp(-np.arange(n) / SR * k)
n = int(0.12 * SR); tt = np.arange(n) / SR
tick = np.sin(2 * np.pi * 1760 * tt) * env_exp(n, 45) * 0.5 + np.sin(2 * np.pi * 2640 * tt) * env_exp(n, 80) * 0.2
yaz(os.path.join(OUT, 'sfx_tick.wav'), tick)
n = int(1.1 * SR); tt = np.arange(n) / SR
nz = rng.normal(0, 1, n)
sweep = np.zeros(n); a = 0.0; out = 0.0
fc = 300 + 3500 * np.sin(np.pi * tt / tt[-1]) ** 2
alpha = 1 - np.exp(-2 * np.pi * fc / SR)
for i in range(n):
    out += alpha[i] * (nz[i] - out); sweep[i] = out
whoosh = sweep * np.sin(np.pi * tt / tt[-1]) ** 1.5
yaz(os.path.join(OUT, 'sfx_whoosh.wav'), whoosh)
n = int(2.5 * SR); tt = np.arange(n) / SR
chime = sum(np.sin(2 * np.pi * hz(m) * tt) * env_exp(n, d) * g for m, d, g in [(86, 2.2, .5), (93, 3, .3), (98, 4, .18)])
chime *= np.minimum(1, tt / 0.005)
yaz(os.path.join(OUT, 'sfx_chime.wav'), chime)
print('müzik', round(T, 1), 'sn')
