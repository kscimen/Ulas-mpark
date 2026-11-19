"""Ses miksajı: anlatım + müzik (anlatım sırasında otomatik kısma) + efektler -> build/out/miks.wav (48 kHz stereo).
Okur: build/out/timeline.json, ses/vXX.wav, build/out/muzik.wav, build/out/sfx_*.wav"""
import json, os, wave
import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'build', 'out'); SR = 48000
tl = json.load(open(os.path.join(OUT, 'timeline.json'), encoding='utf-8'))
N = int((tl['total'] + 0.5) * SR)

def oku(p):
    w = wave.open(p); sr = w.getframerate(); ch = w.getnchannels(); n = w.getnframes()
    x = np.frombuffer(w.readframes(n), dtype='<i2').astype(np.float64) / 32768; w.close()
    x = x.reshape(-1, ch)
    if ch == 1: x = np.repeat(x, 2, 1)
    if sr != SR:  # basit doğrusal yeniden örnekleme
        t = np.arange(int(len(x) * SR / sr)) * sr / SR
        x = np.stack([np.interp(t, np.arange(len(x)), x[:, c]) for c in range(2)], 1)
    return x

def koy(buf, x, t, g=1.0):
    s = int(t * SR); e = min(len(buf), s + len(x))
    if e > s: buf[s:e] += x[:e - s] * g

vo = np.zeros((N, 2)); duck = np.zeros(N)
for sc in tl['scenes']:
    if 'vo' in sc:
        x = oku(os.path.join(ROOT, 'ses', sc['vo'] + '.wav'))
        koy(vo, x, sc['vo_start'], 1.0)
        s = int((sc['vo_start'] - 0.25) * SR); e = int((sc['vo_start'] + sc['vo_dur'] + 0.35) * SR)
        duck[max(0, s):min(N, e)] = 1
# kısma zarfını yumuşat (~0.4 sn)
k = int(0.4 * SR); ker = np.ones(k) / k
duck = np.convolve(duck, ker, mode='same')
mz = oku(os.path.join(OUT, 'muzik.wav'))[:N]
mz = np.pad(mz, ((0, N - len(mz)), (0, 0)))
mz *= (0.55 * (1 - duck) + 0.17 * duck)[:, None]

fx = np.zeros((N, 2))
sfx = {n: oku(os.path.join(OUT, f'sfx_{n}.wav')) for n in ('tick', 'whoosh', 'chime')}
gain = {'tick': 0.10, 'whoosh': 0.22, 'chime': 0.16}
for e in tl['sfx']:
    koy(fx, sfx[e['s']], e['t'], gain[e['s']])

mix = vo * 0.92 + mz + fx
mix /= max(1.0, np.abs(mix).max() / 0.97)
w = wave.open(os.path.join(OUT, 'miks.wav'), 'wb'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
w.writeframes((mix * 32767).astype('<i2').tobytes()); w.close()
print('miks hazır', round(N / SR, 1), 'sn')
