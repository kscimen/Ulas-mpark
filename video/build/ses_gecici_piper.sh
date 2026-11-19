#!/usr/bin/env bash
# GEÇİCİ kılavuz ses: açık kaynak Piper Türkçe sesi ile anlatım üretir.
# Profesyonel seslendirme gelince video/ses/v01.wav ... v09.wav dosyalarını onlarla değiştirip
# build/olustur.sh'i yeniden çalıştırmanız yeterlidir (süreler otomatik uyarlanır).
set -euo pipefail
cd "$(dirname "$0")/.."
MODEL="${PIPER_MODEL:?PIPER_MODEL=/yol/tr_TR-fahrettin-medium.onnx olarak ayarlayın}"
python3 - "$MODEL" <<'PY'
import json, subprocess, sys
model=sys.argv[1]
for s in json.load(open('anlatim.json', encoding='utf-8')):
    subprocess.run([sys.executable,'-m','piper','-m',model,'-f',f"ses/{s['id']}_raw.wav",
                    '--length-scale','1.08','--sentence-silence','0.45','--noise-scale','0.6','--noise-w-scale','0.7'],
                   input=s['metin'].encode('utf-8'), check=True)
    # 48 kHz'e çevir, hafif EQ + kompresör + normalizasyon
    subprocess.run(['ffmpeg','-v','error','-y','-i',f"ses/{s['id']}_raw.wav",'-af',
        'highpass=f=70,equalizer=f=200:t=q:w=1:g=2,equalizer=f=3500:t=q:w=1.5:g=2.5,acompressor=threshold=-20dB:ratio=3:attack=5:release=80,loudnorm=I=-17:TP=-2:LRA=7',
        '-ar','48000','-ac','1',f"ses/{s['id']}.wav"], check=True)
    print(s['id'],'ok')
PY
rm -f ses/*_raw.wav
