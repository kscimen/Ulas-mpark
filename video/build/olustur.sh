#!/usr/bin/env bash
# Videonun tamamını üretir: zaman çizelgesi -> müzik/efekt -> grafik render (paralel) -> ses miksajı -> MP4.
# Gereken: ffmpeg, python3 + numpy, node + playwright (Chromium).
# Kullanım: KARE_DIR=/kare/klasoru build/olustur.sh      (KARE_DIR: build/kareler.sh çıktısı)
set -euo pipefail
cd "$(dirname "$0")"
KARE_DIR="${KARE_DIR:?KARE_DIR ayarlayın (build/kareler.sh ile üretilen kare klasörü)}"
ISCI="${ISCI:-3}"
python3 -I zaman.py
python3 -I muzik.py
N=$(python3 -I -c "import json,math;d=json.load(open('out/timeline.json'));print(math.ceil(d['total']*d['fps']))")
PARCA=$(( (N + ISCI - 1) / ISCI ))
rm -f out/parca_*.mp4
for i in $(seq 0 $((ISCI-1))); do
  S=$((i*PARCA)); E=$(( (i+1)*PARCA < N ? (i+1)*PARCA : N ))
  node render.js out/timeline.json "$KARE_DIR" out/parca_$i.mp4 $S $E &
done
wait
: > out/parcalar.txt; for i in $(seq 0 $((ISCI-1))); do echo "file 'parca_$i.mp4'" >> out/parcalar.txt; done
ffmpeg -v error -y -f concat -safe 0 -i out/parcalar.txt -c copy out/goruntu.mp4
python3 -I miks.py
# ses: -16 LUFS hedef (sunum / çevrim içi)
ffmpeg -v error -y -i out/miks.wav -af loudnorm=I=-16:TP=-1.5:LRA=9 -ar 48000 out/miks_norm.wav
ffmpeg -v error -y -i out/goruntu.mp4 -i out/miks_norm.wav -map 0:v -map 1:a -c:v libx264 -preset slow -crf 20 -pix_fmt yuv420p \
  -c:a aac -b:a 256k -movflags +faststart -shortest ../UlasimPark_MobilSensorAgi_Egitici_Sunum.mp4
echo "Tamam: video/UlasimPark_MobilSensorAgi_Egitici_Sunum.mp4"
