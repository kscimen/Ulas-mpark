#!/usr/bin/env bash
# Kaynak videolardan kullanılacak kesitleri 608x1080 panel karelerine çevirir.
# G2'de: sürücü bölgesi ve plaka bulanıklaştırılır; yolcu yüzleri kadraj dışında bırakılır.
# Kullanım: build/kareler.sh <video1.mp4 (yolda otobüsler)> <video2.mp4 (Kentler Arası Bağlantı)> <cikti_klasoru>
set -euo pipefail
V1="$1"; V2="$2"; FR="$3"
mkdir -p "$FR/g1" "$FR/g2a" "$FR/g2b"
# G1: tüm plan (14,3 sn)
ffmpeg -v error -y -i "$V1" -vf "scale=608:1080:flags=lanczos,eq=saturation=1.04:contrast=1.03" -q:v 3 "$FR/g1/%04d.jpg"
# G2 0,0–1,6 sn: durakta otobüs önü (logolar görünür); sürücü + plaka bulanık
ffmpeg -v error -y -ss 0 -t 1.6 -i "$V2" -filter_complex "[0:v]crop=490:870:230:280,scale=608:1080:flags=lanczos,split=3[b][p][d];[p]crop=110:40:330:716,boxblur=10[pb];[d]crop=120:150:182:378,boxblur=6[db];[b][pb]overlay=330:716[t];[t][db]overlay=182:378" -q:v 3 "$FR/g2a/%04d.jpg"
# G2 2,95–4,25 sn: terminalde hareket eden otobüs (yüksekten)
ffmpeg -v error -y -ss 2.95 -t 1.3 -i "$V2" -vf "scale=608:1080:flags=lanczos" -q:v 3 "$FR/g2b/%04d.jpg"
echo "kareler: $(ls "$FR/g1" | wc -l) / $(ls "$FR/g2a" | wc -l) / $(ls "$FR/g2b" | wc -l)"
