# Eğitici Sunum Videosu: UlaşımPark Mobil Sensör Ağı

**Çıktı:** `UlasimPark_MobilSensorAgi_Egitici_Sunum.mp4` (1920×1080, 30 fps, ~2 dk 31 sn, Türkçe anlatım + gömülü altyazı)
**Altyazı dosyası:** `build/out/altyazi_TR.srt` (üretim sonrası oluşur)

## Yapı (6 bölüm)

| Bölüm | İçerik | Görsel |
|---|---|---|
| Açılış | UlaşımPark logosu, başlık | Kurumsal mavi degrade |
| Giriş | Hareket hâlindeki şehir, düzenli seferler | Gerçek görüntü paneli + şematik hat ağı |
| 01 Fikir | “Peki ya otobüsler veri de toplasaydı?” + sunum gündemi | Gerçek görüntü (ağır çekim, tavanda halka) |
| 02 Neler ölçülür? | 7 sensör katmanı, egzoz bölgesi, teknik onay notu | Markasız teknik otobüs çizimi (animasyonlu) |
| 03 Veri nasıl akar? | Sensör → araç içi birim → mobil ağ → platform; bağlantı kesintisinde yerel kayıt | Akış diyagramı |
| 04 Yapay zekâ ne yapar? | Kalite kontrolü, kalibrasyon, olağan dışı değer, örüntü, yoğunlaşma | Şematik harita (temsili veri) |
| 05 Kullanım senaryoları | A hava kalitesi · B şüpheli gaz → uzman doğrulaması · C yol titreşimi | Gerçek görüntü + harita + bildirim kartı |
| 06 Doğrulama ve pilot | İnsan-karar döngüsü; Faz 0–4 pilot planı; sabit istasyonları tamamlar | Döngü ve zaman çizelgesi |
| Kapanış | “Her yolculuk, şehir için yeni bir veri.” + künye | Kurumsal degrade |

Her bölüm arasında, UlaşımPark logolu ve kurumsal lacivert/mavi zeminli bir **bölüm kartı** var.

## Kullanılan kaynaklar

- **Gerçek görüntü:** Paylaşılan iki videodan kesitler (`build/kareler.sh`).
  - Video 1: 0–14 sn, yolda geçen otobüsler.
  - Video 2: 0,0–1,6 sn (durakta otobüs önü; **sürücü ve plaka bulanıklaştırıldı**, yolcular kadraj dışında) ve 2,95–4,25 sn (terminal). İstanbul’daki havalimanı ve metro planları ile yolcu yüzü içeren planlar **kullanılmadı**.
- **Logo:** Kullanıcının paylaştığı ekran görüntüsünden kırpılan UlaşımPark logosu (`assets/up_logo_beyaz.png`, `assets/up_logo_yazili.png`). **Resmî vektör dosyası gelince değiştirilmeli.**
- **Renkler:** Logodan örneklendi (koyu mavi ≈ #28439A, açık mavi ≈ #2CA9E1, zemin lacivert #0B1A44). Bunlar resmî kurumsal kodlar değildir.
- **Müzik ve efektler:** `build/muzik.py` ile özgün olarak sentezlendi; lisans gerektirmez.
- **Anlatım:** **GEÇİCİ** açık kaynak Türkçe sentetik ses (Piper, `tr_TR-fahrettin-medium`). Profesyonel seslendirme ile değiştirilmesi planlanıyor (aşağıda).

## Profesyonel seslendirmeyle değiştirme

1. Seslendirmene `anlatim.json` içindeki 9 metni verin. Her biri ayrı WAV dosyası olarak kaydedilsin: `v01.wav … v09.wav`, 48 kHz, mono veya stereo, kuru kayıt.
   - Yapay zekâ ses aracı kullanılacaksa önerilen sesler: Magnific/ElevenLabs “Kerem Şahin” (kurumsal bariton) veya vidIQ “Doga” (kurumsal anlatım). Her iki serviste de bu hesapların ücretsiz kotası şu an yetersiz.
2. Dosyaları `video/ses/` klasörüne koyun (eskilerin üzerine yazın).
3. Çalıştırın:
   ```bash
   KARE_DIR=/kare/klasoru video/build/olustur.sh
   ```
   Sahne süreleri, animasyon zamanlamaları, altyazılar ve müzik kısmaları yeni ses sürelerine **otomatik** uyarlanır.

Kareler yoksa önce şunu çalıştırın:
```bash
video/build/kareler.sh <video1.mp4> <video2.mp4> /kare/klasoru
```

## Dosyalar

| Dosya | Görev |
|---|---|
| `anlatim.json` | Bölüm bölüm anlatım metni (tek kaynak) |
| `ses/` | Anlatım WAV dosyaları (şu an geçici ses) |
| `assets/` | Logo dosyaları |
| `build/zaman.py` | Ses sürelerinden zaman çizelgesi, olay zamanları ve SRT |
| `build/muzik.py` | Özgün fon müziği ve efektler |
| `build/sahne.html` | Tüm sahnelerin animasyon motoru (HTML/SVG) |
| `build/render.js` | Chromium ile kare kare render → ffmpeg |
| `build/miks.py` | Anlatım + müzik (otomatik kısma) + efekt miksajı |
| `build/olustur.sh` | Tüm adımları sırayla çalıştırır |
| `build/ses_gecici_piper.sh` | Geçici sentetik anlatımı üretir |

## Bilinen sınırlamalar

- Geçici sentetik seste vurgu ve tonlama profesyonel seviyede değildir. Bazı kelimelerin telaffuzu kontrol edilmeli (“hâlinde”, “zekâ”, “güzergâh”).
- Gerçek görüntü kaynakları dikey ve 720p olduğu için tam ekran değil, sol panel olarak kullanıldı.
- Harita **şematiktir**; gerçek ölçek veya konum göstermez.
- Instagram Reels görüntüleri (drone, atölye vb.) dosya olarak elde olmadığı için kullanılamadı. Orijinalleri gelirse eklenebilir.
