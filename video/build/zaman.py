"""Zaman çizelgesi: anlatım (ses/vXX.wav) sürelerinden tüm sahne, efekt ve altyazı zamanlarını üretir.
Çıktı: build/out/timeline.json ve build/out/altyazi_TR.srt.
Profesyonel seslendirme gelince yalnızca ses dosyaları değişir, gerisi otomatik uyarlanır."""
import json, os, re, subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, 'build', 'out')
os.makedirs(OUT, exist_ok=True)

anlatim = {s['id']: s for s in json.load(open(os.path.join(ROOT, 'anlatim.json'), encoding='utf-8'))}

def sure(path):
    return float(subprocess.check_output(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                                          '-of', 'csv=p=0', path]).decode().strip())

CARD = 2.8
plan = [
    ('intro', None, 5.0, 0, 0),
    ('acilis', 'v01', None, 0.6, 1.0),
    ('kart', None, CARD, 0, 0, {'no': '01', 'baslik': 'Fikir', 'alt': 'Otobüsler neden veri toplayabilir?'}),
    ('fikir', 'v02', None, 0.4, 1.2),
    ('kart', None, CARD, 0, 0, {'no': '02', 'baslik': 'Neler ölçülür?', 'alt': 'Sensör katmanı'}),
    ('sensor', 'v03', None, 0.5, 1.4),
    ('kart', None, CARD, 0, 0, {'no': '03', 'baslik': 'Veri nasıl akar?', 'alt': 'Araçtan merkezi platforma'}),
    ('veri', 'v04', None, 0.5, 1.2),
    ('kart', None, CARD, 0, 0, {'no': '04', 'baslik': 'Yapay zekâ ne yapar?', 'alt': 'Analiz ve önceliklendirme'}),
    ('yz', 'v05', None, 0.5, 1.4),
    ('kart', None, CARD, 0, 0, {'no': '05', 'baslik': 'Kullanım senaryoları', 'alt': 'Hava · Gaz · Yol'}),
    ('senaryo', 'v06', None, 0.5, 1.2),
    ('kart', None, CARD, 0, 0, {'no': '06', 'baslik': 'Doğrulama ve pilot', 'alt': 'İnsan kararı, adım adım uygulama'}),
    ('dogrulama', 'v07', None, 0.4, 0.8),
    ('pilot', 'v08', None, 0.3, 1.4),
    ('final', 'v09', None, 1.2, 4.2),
    ('kunye', None, 4.0, 0, 0),
]

def cumleler(text):
    return [c.strip() for c in re.split(r'(?<=[.?!])\s+', text) if c.strip()]

scenes, subs, sfx = [], [], []
t = 0.0
for item in plan:
    kind, vid, dur, pre, post = item[:5]
    extra = item[5] if len(item) > 5 else {}
    sc = {'id': f'{kind}_{len(scenes):02d}', 'type': kind, 'start': round(t, 3), **extra}
    kz = None
    if vid:
        vd = sure(os.path.join(ROOT, 'ses', f'{vid}.wav'))
        dur = pre + vd + post
        metin = anlatim[vid]['metin']
        sc.update(vo=vid, vo_start=round(t + pre, 3), vo_dur=round(vd, 3), text=metin)
        cs = cumleler(metin)
        tot = sum(len(c) for c in cs)
        ct = t + pre
        for c in cs:
            d = vd * len(c) / tot
            subs.append({'start': round(ct, 3), 'end': round(ct + d - 0.05, 3), 'text': c})
            ct += d
        def kz(word, t0=t + pre, vd=vd, metin=metin):
            i = metin.find(word)
            assert i >= 0, word
            return round(t0 + vd * i / len(metin), 3)
    sc['dur'] = round(dur, 3)
    if kind == 'kart':
        sfx.append({'t': round(t, 3), 's': 'whoosh'})
        sfx.append({'t': round(t + 0.45, 3), 's': 'chime'})
    if kz:
        ev = {}
        if kind == 'sensor':
            for k, w in [('pm', 'partikül'), ('th', 'sıcaklık'), ('gaz', 'gaz'), ('ses', 'ses seviyesi'),
                         ('tit', 'yol titreşimi'), ('gnss', 'sensörler yerleştirilir'), ('gw', 'Sensörler, aracın'),
                         ('onay', 'Montaj')]:
                ev[k] = kz(w)
        elif kind == 'veri':
            ev = {'konum': kz('konum'), 'birim': kz('Araç üzerindeki'), 'ag': kz('mobil ağ'),
                  'kesinti': kz('Bağlantı kesilirse'), 'geri': kz('bağlantı geri')}
        elif kind == 'yz':
            ev = {'kalite': kz('kalite'), 'harita': kz('haritaya'), 'kalib': kz('kalibrasyon'),
                  'olagan': kz('olağan'), 'oruntu': kz('tekrar eden'), 'bolge': kz('yoğunlaşan')}
        elif kind == 'senaryo':
            ev = {'a': sc['vo_start'], 'b': kz('Şüpheli'), 'c': kz('Aynı noktada')}
        elif kind == 'fikir':
            ev = {'soru': sc['vo_start'], 'ajanda': kz('Bu sunumda')}
        elif kind == 'pilot':
            ev = {'f1': kz('hazırlık'), 'f2': kz('kalibrasyon'), 'f3': kz('birkaç otobüs'),
                  'f4': kz('değerlendirme'), 'tamam': kz('Sabit ölçüm')}
        elif kind == 'dogrulama':
            ev = {'son': kz('Son değerlendirme')}
        elif kind == 'acilis':
            ev = {'otobus': kz('Bu hareketin')}
        sc['ev'] = ev
        if kind in ('sensor', 'yz', 'pilot', 'veri', 'senaryo'):
            for v in ev.values():
                sfx.append({'t': v, 's': 'tick'})
    scenes.append(sc)
    t += dur

total = round(t, 3)
json.dump({'fps': 30, 'w': 1920, 'h': 1080, 'total': total, 'scenes': scenes, 'subs': subs, 'sfx': sfx},
          open(os.path.join(OUT, 'timeline.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f'{h:02d}:{m:02d}:{s:02d},{ms:03d}'
with open(os.path.join(OUT, 'altyazi_TR.srt'), 'w', encoding='utf-8') as f:
    for i, s in enumerate(subs, 1):
        f.write(f"{i}\n{ts(s['start'])} --> {ts(s['end'])}\n{s['text']}\n\n")
print('toplam', total, 'sn,', len(scenes), 'sahne,', len(subs), 'altyazı')
