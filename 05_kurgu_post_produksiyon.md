# Teslimat 5 — Kurgu ve Post-Prodüksiyon Planı

## 1. Proje ayarları

| Ayar | Değer | Not |
|---|---|---|
| Zaman çizelgesi | 1920×1080, **30 fps**, kare oranı 1:1 | Kaynak telefon görüntüleri 30 fps; dönüşüm titremesi olmasın |
| Master | ProRes 422 HQ (veya DNxHR HQ), 1080p30 | Arşiv |
| Dağıtım | H.264 High, 1080p30, 16–20 Mbit/s VBR 2-pass, AAC 48 kHz 320 kbit/s, MP4 | Sunum ve e-posta paylaşımı |
| Hafif sürüm | H.264 1080p, ~8 Mbit/s | Mesajlaşma için |
| 4K | Yalnız tüm kaynaklar ≥4K ise | Mevcut gerçek görüntüler 720p, 4K anlamsız |
| Ses | 48 kHz / 24 bit; hedef **−16 LUFS entegre**, true peak ≤ −1 dBTP | Toplantı salonu/online. Yayın gerekirse −23 LUFS sürümü |
| Önerilen yazılım | DaVinci Resolve veya Premiere Pro (kurgu, renk, ses) + After Effects (MG) | Biri yeterli; MG için AE veya Fusion |

## 2. Sahne sıralaması ve süreler

| # | Giriş | Çıkış | Süre | İçerik | Geçiş (çıkışta) |
|---|---|---|---|---|---|
| S1 | 00:00:00 | 00:00:09 | 9 sn | Şehir (2 plan) | Sola kayan panel (wipe), 12 kare |
| S2 | 00:00:09 | 00:00:16 | 7 sn | Split-screen: G1 + hat grafiği; G2 durak | Kesme |
| S3 | 00:00:16 | 00:00:23 | 7 sn | Donma + halka | Kesme (müzik vuruşunda) |
| S4 | 00:00:23 | 00:00:36 | 13 sn | Konsept otobüs + sensörler | Morph (otobüs → harita ikonu), 15 kare |
| S5 | 00:00:36 | 00:00:46 | 10 sn | Veri akışı | Zoom-through (platform düğümü) |
| S6 | 00:00:46 | 00:00:58 | 12 sn | Harita + YZ | Yatay kaydırma |
| S7 | 00:00:58 | 00:01:15 | 17 sn | 3 senaryo (5+6+6) | Çapraz geçiş, 10 kare |
| S8 | 00:01:15 | 00:01:23 | 8 sn | Saha doğrulaması | Luma fade |
| S9 | 00:01:23 | 00:01:32 | 9 sn | Final + slogan | Siyaha 15 kare |
| Kart | 00:01:32 | 00:01:37 | 5 sn | Kapanış kartı | Siyah |

**Kurgu sırası önerisi:** (1) Seslendirmeyi zaman çizelgesine yerleştir. (2) Blokları gerçek sürelere göre kaydır. (3) Müziği seslendirmeye göre kes (vuruşlar S2, S4 ve S9 girişlerine). (4) Görüntüleri yerleştir. (5) MG. (6) Yazılar. (7) Renk. (8) Ses karışımı.

## 3. Dikey kaynak görüntünün (G1, G2) kullanımı

- **Tercih edilen yöntem, bölünmüş ekran:** 720×1280 kaynak, **608×1080**’e küçültülerek tam yükseklikte sol panele yerleştirilir. Ölçek <1 olduğu için netlik kaybı olmaz. Sağ 1312 px alan grafik ve yazı için kullanılır. S2, S3, S7 bu düzeni kullanır.
- **Bulanık arka plan dolgusu kullanılmaz.** Amatör görünür.
- **Tam ekran 16:9 kırpma** yalnızca kaynaktan 1080p’ye büyütme gerektirdiği için önerilmez. Kalite düşer (720 genişlikten 1920’ye yaklaşık 2,7 kat).
- Panel kenarı: 2 px yarı saydam beyaz çizgi veya keskin kenar; köşe yarıçapı 0 (kurumsal sadelik).

## 4. Görüntü temizliği ve hukuki kontroller

- [ ] G1/G2’de **özel araç plakaları bulanıklaştırılır** (izleme maskesi). Otobüs plakaları da tercihen bulanıklaştırılır.
- [ ] G2’de yolcu ve ana karakter yüzleri kullanılan kesitlerde görünmez veya bulanıklaştırılır. G2’nin İstanbul planları (havalimanı, metro) **kullanılmaz**.
- [ ] G1/G2 orijinal müziği **tamamen kapatılır**.
- [ ] G2 ~16 sn ve ~23 sn planları Kocaeli’de çekildiyse kullanılır; teyit edilemezse kullanılmaz.
- [ ] Instagram Reels görüntüleri yalnız orijinal dosya ve UlaşımPark izniyle kullanılır.
- [ ] Stok görüntü ve müzik lisansları kurum içi + online kullanımı kapsar.

## 5. Müzik

- **Karakter:** Modern, sinematik, sakin-iyimser. Yumuşak piyano veya pluck motifi, sıcak pad, hafif elektronik ritim (yaklaşık 90–100 BPM). S4’te tam ritim, S8’de sadeleşme, S9’da tek akorla çözülme. Epik davul, dubstep, distopik synth ve “reklam neşesi” yok.
- **Arama anahtar kelimeleri (lisanslı müzik kütüphaneleri):** *corporate cinematic technology hopeful minimal*, *smart city ambient pulse*, *innovation documentary calm*.
- **Seviye:** Seslendirme varken −18 / −20 dB altta (ducking). Seslendirme yokken (S1 ilk 2 sn, S9 sonu) öne çıkar.
- **Lisans:** Kurum içi gösterim ve olası online paylaşımı kapsayan lisans. Lisans belgesi proje klasörüne konur.

## 6. Ses efektleri (SFX)

| Sahne | Efekt | Seviye |
|---|---|---|
| S1 | Uzak şehir ambiyansı, çok hafif martı | Düşük |
| S2 | Otobüs geçiş “whoosh” (senkron) | Orta-düşük |
| S3 | Donma anında müzik filtreleme + tek yumuşak “ping” | Orta |
| S4 | Etiket başına yumuşak UI “tık” (aralar ≥8 kare) | Düşük |
| S5 | Ritmik veri tıkırtıları; tampon dolarken yumuşak yükselen ton | Düşük |
| S6 | Halka vurgusunda düşük frekanslı “pulse” | Düşük |
| S7 | Kart açılışlarında aynı nazik bildirim sesi (alarm, siren yok) | Orta-düşük |
| S8 | Atölye/sokak ortam sesi | Düşük |
| S9 | Işık geçişinde yumuşak “shimmer”, sonra sessizliğe doğru müzik | Orta |

## 7. Renk düzenleme

- **Hedef görünüm:** Doğal, temiz, hafif sıcak gün ışığı. Yeşiller doğal, gökyüzü hafif doygun, gölgeler hafif yükseltilmiş (yumuşak kontrast). “Teal-orange sinema” abartısı yok.
- **G1/G2 uyumu:** İki telefon kaynağı farklı beyaz dengesinde olabilir. Önce normalize edilir (beyaz tavan kaportası nötr beyaz referansı). Otobüs yeşili **olduğu gibi korunur**, doygunluğu artırılmaz ve kaydırılmaz (kurumsal görünümün bozulmaması için).
- **YZ ve stok plan uyumu:** YZ/stok planları G1’in ışığına yaklaştırılır (renk eşleme).
- **Gürültü azaltma:** Telefon sıkıştırma artefaktlarına hafif uzamsal gürültü azaltma; aşırı yumuşatma yok.
- **Ağır çekim:** S3’teki %50 yavaşlatma için optik akış kare enterpolasyonu kullanılır; bozulma varsa %70’e çıkarılır.

## 8. Grafik dili ve ekran yazıları

### 8.1 Palet (resmî kimlik bilinmediği için nötr öneri, resmî değil)
| Rol | Öneri |
|---|---|
| Zemin (grafik sahneleri) | Koyu lacivert-arduvaz, düşük doygunluk |
| Ana yazı | Kırık beyaz |
| Vurgu 1 (veri, hatlar) | Sakin mavi. UP logosunun mavisi resmî kodla alınırsa o kullanılır |
| Vurgu 2 (sensör modülleri) | Pastel turkuaz |
| Dikkat (anomali) | Kehribar / turuncu. **Kırmızı kullanılmaz** |
| Otobüs yeşili | Yalnız gerçek görüntüde. Grafikte resmî kod gelmeden kullanılmaz |

Resmî kurumsal kimlik kılavuzu temin edilirse palet ve yazı tipi ona göre güncellenir.

### 8.2 Tipografi
- Türkçe karakterleri tam destekleyen sans-serif (ör. **Inter**, **Source Sans 3**, **Noto Sans**: açık lisanslı). Kurum yazı tipi varsa o kullanılır.
- Ana ekran yazısı: 54–64 px, orta kalınlık; etiketler: 28–32 px; künye: 20–22 px.
- Satır başına en fazla ~38 karakter, tek veya iki satır. Ekranda kalma süresi okunma hızına göre en az **2,5 sn + kelime başına 0,3 sn**.
- Güvenli alan: kenarlardan %5 (yazılar için %10).
- Animasyon: 8–12 karelik yumuşak opaklık + 20 px yukarı kayma; çıkış girişin tersi. Daktilo ve glitch efekti yok.

### 8.3 Ekran yazıları tam listesi (Türkçe karakter kontrolüyle)

| Sahne | Yazı |
|---|---|
| S1 | Bir şehir, her gün hareket hâlinde. |
| S3 | Peki ya otobüsler, veri de toplasaydı? |
| S4 | Partikül madde · PM2.5 / PM10 — Sıcaklık · Nem — Gaz yoğunluğu · CH₄ — Ses seviyesi · dB(A) — Yol titreşimi — Konum · GNSS — Araç içi veri birimi |
| S4 alt şerit | Konsept yerleşim — montaj tasarımı teknik onaya tabidir. |
| S5 | Her ölçüm, konum ve zaman bilgisiyle sisteme aktarılır. |
| S5 etiket | Araç içi veri birimi · Mobil ağ · Merkezi platform · Bağlantı yoksa yerel kayıt |
| S6 | Yapay zekâ verileri analiz eder, olağan dışı durumları öne çıkarır. |
| S6 panel | Hava kalitesi · Gaz · Gürültü · Yol |
| S7a kart | Hava kalitesi — Yüksek partikül yoğunluğu → İnceleme önerisi |
| S7b kart | Şüpheli gaz ölçümü — Konum ve zaman iletildi → Uzman doğrulaması bekleniyor |
| S7c kart | Tekrarlayan titreşim — 3 farklı geçiş → Saha kontrolü önerilir |
| S7 | Erken farkındalık. Doğru konum. Hızlı değerlendirme. |
| S8 | Son karar: uzman ekipler. |
| S9 | Her yolculuk, şehir için yeni bir veri. |
| S9 alt | Sabit ölçüm istasyonlarını tamamlayan mobil bir yaklaşım · Pilot uygulama önerisi |
| Kalıcı | Konsept görselleştirme · Temsili veri · Konsept arayüz · © OpenStreetMap katkıcıları |
| Kart | UlaşımPark Mobil Sensör Ağı (çalışma adı) · Proje önerisi · Hazırlayan: [Ad Soyad, unvan] · Görüntülerdeki sensör yerleşimleri, arayüzler ve veriler temsilidir. |

**Not:** “CH₄” alt simge ile yazılır (Unicode ₄). Yazı tipi desteklemiyorsa “CH4” kullanılır. “PM2.5” Türkçe ondalık virgülüyle değil, uluslararası kısaltma olarak noktayla yazılır.

## 9. Altyazı

- Seslendirmenin birebir Türkçe altyazısı **ayrı SRT** dosyası olarak hazırlanır. Ayrıca sessiz izlenebilecek bir **gömülü altyazılı** sürüm çıkarılır (toplantı ortamlarında ses kapalı olabilir).
- Satır başına ≤42 karakter, en fazla 2 satır, en az 1 sn / en fazla 6 sn ekranda.
- Altyazı ekran yazılarıyla çakışırsa altyazı alt güvenli alanda, ekran yazısı üst/orta bölgede kalır.
- İsteğe bağlı İngilizce altyazı (ulusal/uluslararası hibe başvuruları için).

## 10. Logo ve kapanış kartı

- Logolar **yalnızca** resmî vektör/yüksek çözünürlüklü PNG dosyaları ve kullanım onayı varsa eklenir. YZ ile yeniden çizilmez, renkleri değiştirilmez, kurum kılavuzundaki boşluk kurallarına uyulur.
- Onay yoksa kapanış kartı logosuz, yalnız yazıyla hazırlanır. Film gerçek araç görüntülerindeki logolar üzerinden kimliği zaten taşır.
- Kapanış kartı sade zeminde, 5 sn, müzik son akoru üzerinde.

## 11. Çıktılar

| Dosya | İçerik |
|---|---|
| `UP_MobilSensor_Vizyon_v1_1080p30_master.mov` | ProRes master |
| `UP_MobilSensor_Vizyon_v1_1080p30.mp4` | Dağıtım sürümü |
| `UP_MobilSensor_Vizyon_v1_1080p30_altyazili.mp4` | Gömülü altyazılı |
| `UP_MobilSensor_Vizyon_v1_TR.srt` | Altyazı dosyası |
| `UP_MobilSensor_Vizyon_v1_kapak.png` | 1920×1080 küçük resim (S9 karesi + slogan) |
| Opsiyonel `..._9x16.mp4` | Dikey 60 sn kesit (sosyal medya). **Yalnızca kurumsal onaydan sonra** |

## 12. Kalite kontrol listesi (teslim öncesi)

**İçerik ve iddia**
- [ ] “Anlık / gerçek zamanlı / kesin / tüm şehir / her kaçak” ifadeleri yok
- [ ] Hiçbir yerde sayısal ölçüm değeri, maliyet, başarı oranı veya kurum onayı yok
- [ ] Gaz sahnesinde “şüpheli ölçüm → uzman doğrulaması” dili korunmuş; alarm/siren yok
- [ ] “Konsept görselleştirme”, “Temsili veri”, “Konsept arayüz” etiketleri ilgili tüm planlarda var
- [ ] Kapanışta “Proje önerisi” ibaresi var
- [ ] Gerçek bir belediye kontrol merkezi veya mevcut uygulama ekranı gösterilmiyor

**Görüntü**
- [ ] YZ planlarında yazı, logo, plaka, bozuk araç ve sensör konumu hatası yok (Teslimat 3 kabul listesi)
- [ ] Plakalar ve yüzler bulanıklaştırılmış; G2’nin İstanbul planları kullanılmamış
- [ ] Sensör konumları S4 ile diğer sahneler arasında tutarlı
- [ ] Renk planlar arasında tutarlı; otobüs yeşili değiştirilmemiş
- [ ] Siyah kare, atlama, titreme yok; geçişler müzikle uyumlu

**Yazı ve dil**
- [ ] Tüm Türkçe karakterler doğru (ç, ğ, ı, İ, ö, ş, ü, â); “hâlinde”, “zekâ”, “güzergâh”
- [ ] Ekran yazıları okunma süresini karşılıyor, güvenli alanda
- [ ] Altyazı seslendirmeyle birebir ve senkron

**Ses**
- [ ] Entegre −16 LUFS (±1), true peak ≤ −1 dBTP
- [ ] Seslendirme her yerde anlaşılır; müzik ducking doğru
- [ ] Kaynak videoların orijinal sesi/müziği tamamen kapalı
- [ ] Tüm müzik ve SFX lisansları dosyada

**Teknik**
- [ ] 1920×1080, 30 fps, 16:9, ~90–97 sn
- [ ] Bir dizüstü bilgisayarda, bir projektörde ve bir telefonda izlenerek kontrol edildi
- [ ] Anadili Türkçe ve konuya yabancı bir kişiye izletilip “sistem ne yapıyor?” sorusu soruldu
