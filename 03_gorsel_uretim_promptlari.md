# Teslimat 3 — Görsel ve Video Üretim Promptları

## Kullanım ilkeleri

1. **Gerçek görüntü önce gelir.** S1, S2, S3, S8 ve S9’da gerçek görüntü (G1, G2, R1–R6) varsa YZ kullanılmaz. Buradaki promptlar o sahneler için **yalnızca yedektir**.
2. **YZ ile UlaşımPark/Kocaeli Büyükşehir otobüsü taklit edilmez.** YZ promptlarında otobüs **nötr beyaz/açık gri, markasız, yazısız** tanımlanır. Yeşil livery, logo, hat tabelası yazısı, plaka **üretilmez**. Bu görünüm yalnızca gerçek görüntüden gelir.
3. **Hiçbir yazı modele çizdirilmez.** Tüm ekran yazıları, etiketler, kartlar ve arayüz metinleri kurguda eklenir (Teslimat 5). Promptlarda “no text” şartı vardır.
4. Her prompt **bağımsızdır.** Herhangi bir araca (Veo, Sora, Kling, Runway, Midjourney, Firefly vb.) tek başına yapıştırılabilir. Araç negatif prompt alanı destekliyorsa “Negative” bölümü oraya, desteklemiyorsa prompt sonuna “Avoid: …” olarak eklenir.
5. **Süre:** Çoğu model 5–10 sn üretir. Sahne daha uzunsa iki parça üretilip kurguda birleştirilir.
6. **Görsel devamlılık:** Tüm YZ sahnelerinde aynı “konsept otobüs” tanımı kullanılır (aşağıda **CB** bloğu). Mümkünse önce bir referans görsel (P4-IMG) üretilir, diğer sahneler bu görselden image-to-video ile türetilir.
7. Üretilen her YZ planı kurguda **“Konsept görselleştirme”** etiketiyle gösterilir.

### Ortak blok CB: Konsept otobüs tanımı (tüm YZ promptlarına aynen eklenir)

```
CONCEPT BUS: a generic modern 12-meter low-floor city bus, smooth rounded front, large windscreen, plain matte light-grey/white body with a slightly darker grey lower skirt, dark tinted side windows, low flat roof equipment housings. Absolutely no logos, no lettering, no destination sign text, no license plate characters, no brand colors, no livery graphics. Realistic proportions, two axles, symmetrical wheels, correct number of doors (three double doors on the right side).
```

### Ortak blok NEG: Negatif prompt (tüm promptlara eklenir)

```
Negative: text, letters, numbers, captions, subtitles, watermark, logo, brand names, readable signs, license plate characters, garbled typography, fake UI text, distorted or melted vehicle, extra wheels, missing wheels, asymmetrical wheels, warped windows, bus floating above road, wrong scale, duplicated buses merging, sensors on windscreen, sensors blocking doors, mirrors or headlights, oversized sci-fi antennas, glowing neon cyberpunk aesthetic, holograms floating in the street, red alarm lights, police lights, smoke or fire, explosions, dystopian mood, people's faces in close-up, deformed hands, crowd distortion, flickering, morphing geometry, low resolution, oversaturated colors, lens flare overload.
```

### Ortak blok STYLE: Görsel üslup

```
STYLE: photorealistic corporate documentary cinematography, natural daylight, soft overcast-to-sunny sky with scattered cumulus clouds, calm and trustworthy mood, restrained color palette (natural greens, concrete greys, soft sky blues), gentle contrast, shallow-to-medium depth of field, 24mm–50mm lens look, smooth stabilized camera movement, 16:9, 1920x1080 or higher, 24–30 fps, no film grain overload.
```

---

## P1 — S1 · Hareket hâlindeki şehir (YEDEK, gerçek drone görüntüsü yoksa)

**Türkçe özet:** Sabah ışığında körfez kıyısındaki bir Türk sanayi-kıyı şehrinin havadan görüntüsü. Viyadük, tramvay hattı, akan trafik. Gerçek Kocaeli görüntüsü bulunamazsa “temsili şehir” olarak kullanılır, Kocaeli’ymiş gibi sunulmaz.

```
Cinematic aerial drone shot at early morning golden-hour light over a mid-sized coastal Turkish city on a calm gulf: dense mid-rise residential blocks on green hillsides, a long highway viaduct along the shoreline, a modern tram line with an articulated tram gliding between tree-lined lanes, steady flow of cars and a few generic white city buses on a wide multi-lane avenue, distant industrial port cranes softly hazed by morning light. Camera: high-altitude slow forward dolly with slight downward tilt, perfectly smooth, 6 seconds. Light: warm low sun from the left, long soft shadows, light morning haze over the water. Mood: a city waking up and moving, calm and hopeful.
STYLE: photorealistic corporate documentary cinematography, natural daylight, restrained palette, gentle contrast, 16:9, 1920x1080, 30 fps.
Negative: text, signs with readable letters, logos, watermark, futuristic skyscrapers, sci-fi elements, distorted vehicles, flickering, oversaturated colors, drone propellers in frame.
```

## P2 — S2 · Düzenli seferler (YEDEK, sol panel için; gerçek G1 varsa kullanılmaz)

**Türkçe özet:** Bulutlu-güneşli havada geniş bir caddede kameraya doğru art arda gelen markasız otobüsler. Dikey 9:16 üretilir (sol panel için).

```
Vertical 9:16 street-level shot, camera fixed on the median at knee height, a wide multi-lane urban avenue with overhead tram catenary wires, a roadside metal fence and tidy mid-rise apartment blocks, bright sky with large white cumulus clouds. Several identical generic city buses approach the camera one after another at steady speed and pass closely to the right of frame, one articulated version among them.
CONCEPT BUS: generic modern low-floor city bus, plain matte light-grey/white body, darker grey lower skirt, tinted windows, no logos, no lettering, no destination text, no license plate characters, realistic proportions, correct wheels and doors.
Camera: locked-off, slight natural motion blur on passing buses, 6 seconds.
STYLE: photorealistic documentary, natural daylight, 1080x1920, 30 fps.
Negative: text, logos, plate numbers, garbled signs, merging buses, extra wheels, warped bodies, people close-up, neon, flicker.
```

## P3 — S3 · Fikir anı (YEDEK)

**Türkçe özet:** Otobüsün tavan hattını gösteren yan yakın plan, ağır çekim. Grafik (çizgi/halka) kurguda eklenir; model çizmez.

```
Close side-profile shot of a generic city bus driving slowly past the camera from left to right, framed on the upper body and roofline: clean flat roof edge, low equipment housing at the front of the roof, tinted windows reflecting clouds. Slow-motion feel (60 fps conformed to 30), shallow depth of field with softly blurred street and trees behind. Bright day with scattered clouds. Leave clear empty sky space above the roof for later graphics.
CONCEPT BUS: generic modern low-floor city bus, plain matte light-grey/white body, darker grey lower skirt, no logos, no lettering, no destination text, no plate characters.
Camera: static, 50mm lens look, 5 seconds.
STYLE: photorealistic corporate cinematography, natural soft light, 16:9.
Negative: text, logos, holograms, glowing lines, sci-fi effects, distorted roof, warped windows, extra wheels, flicker.
```

## P4-IMG — S4 · Konsept otobüs referans görseli (önce bu üretilir)

**Türkçe özet:** Sensör yerleşimini gösteren, stüdyoda, nötr gri, “teknik maket” görünümlü konsept otobüs. Etiketler yok; yalnızca fiziksel modüller. Tüm YZ sahneleri için devamlılık referansı.

```
High-end product visualization of a generic modern 12-meter city bus as a clean technical concept model, three-quarter front-high view, in a seamless soft light-grey studio with gentle floor reflection. Body finish: matte neutral light grey, darker grey lower skirt, dark tinted windows, absolutely no logos, no text, no livery.
Physically plausible, compact sensor modules, all small and low-profile, color-accented in a single muted teal so they are identifiable:
1) front section of the roof: a small closed rectangular particulate-matter sampling box with a short forward-facing protected inlet;
2) next to it on the front roof: a small white louvered radiation-shield housing for temperature and humidity (stacked round plates);
3) the very front edge of the roof: a thin short gas-sampling inlet tube, clearly away from the rear of the vehicle;
4) upper side body above the front wheel: a small microphone module with a foam windscreen;
5) roof center: a low flat dome GNSS and cellular antenna;
6) chassis near the front axle (visible through a subtle semi-transparent cut-away panel): a small accelerometer box bolted to the frame;
7) inside behind the driver area (visible through the same subtle cut-away): a compact rugged gateway data box.
Nothing on the windscreen, mirrors, headlights, doors or windows. Modules look like real industrial hardware, not sci-fi.
Lighting: soft large-area studio light, subtle rim light, clean shadows. Photorealistic render quality, 16:9, 3840x2160.
Negative: text, labels, letters, numbers, logos, glowing neon, holograms, oversized antennas, sensors on windscreen or doors, cables hanging, distorted body, extra wheels, cartoon style, toy look, busy background.
```

## P4-VID — S4 · Sensör yörüngesi (image-to-video, P4-IMG başlangıç karesi)

**Türkçe özet:** Referans görselden başlayıp otobüsün etrafında 90° yavaş yörünge hareketi. Sensör modülleri sabit, vurgu ışığı sırayla yanar. Etiketler kurguda eklenir.

```
Using the provided concept bus image as the first frame: a slow, perfectly smooth 90-degree orbit camera move around the stationary concept bus, starting from a low front-left angle and ending at a slightly elevated three-quarter front-right view. The bus and all sensor modules stay exactly the same shape, size and position throughout (no morphing). One by one, each small teal sensor module receives a soft, subtle highlight glow for about one second (roof particulate box, temperature/humidity shield, gas inlet tube, side microphone module, roof antenna dome, then the accelerometer and gateway box seen through the semi-transparent cut-away), then the glow fades. Soft light-grey studio, gentle floor reflection, calm technical mood. 10 seconds, 30 fps, 16:9.
Negative: text, labels, logos, morphing vehicle, changing sensor positions, extra sensors appearing, camera shake, fast motion, neon, holograms, sparks, flicker.
```

> **Önerilen alternatif:** S4 için Blender/C4D’de basit bir otobüs modeli + sensör modülleri. Bu yol, YZ’nin sensör yerini oynatma riskini tamamen ortadan kaldırır ve montaj mühendisiyle konum üzerinde birlikte çalışılabilir.

## P5 — S5 · Veri akışı arka planı (yalnızca zemin; animasyon MG ile)

**Türkçe özet:** Sade, koyu-lacivert, hafif eğimli soyut harita zemini. Veri paketleri, ikonlar ve yazılar After Effects’te eklenir.

```
Minimal abstract top-down city map background at a gentle 15-degree tilt: thin soft-white road lines on a deep desaturated navy-slate base, a smooth coastline shape on one side with slightly lighter water tone, subtle topographic hill shading, very faint grid. Clean, calm, premium data-visualization look, lots of negative space, no icons, no labels. Slow imperceptible drift of the camera to the right, 10 seconds, 16:9, 3840x2160.
Negative: text, labels, street names, numbers, logos, neon glow, cyberpunk, holograms, particles, lens flares, busy details, 3D buildings.
```

## P6 — S6 · Harita ve analiz (YZ kullanılmaz)

S6 **gerçek coğrafya** (Kocaeli kıyı çizgisi ve yol ağı) gerektirdiği için YZ ile üretilmez. YZ coğrafyayı uydurur ve “gerçek harita” gibi algılanır. Önerilen yol:
- Altlık: OpenStreetMap verisinden sade stil (ör. QGIS / Mapbox Studio / kepler.gl dışa aktarımı), 4K.
- Katmanlar: Temsili nokta verisi hat geometrileri boyunca üretilir, yoğunluk (heatmap) katmanına dönüştürülür.
- Animasyon: After Effects’te zoom, zaman kaydırıcı, halka vurguları.
- Atıf: “© OpenStreetMap katkıcıları”.

## P7 — S7 · Senaryo kartları ve harita yakın planları (YZ kullanılmaz)

S7a/b/c tamamen MG’dir; aynı harita altlığının yakın planları + kart bileşeni. Sol paneller gerçek görüntüdür (G1/R4). YZ yedeği gerekirse sol panel için **P2** kullanılır.

## P8 — S8 · Saha doğrulaması (YEDEK, gerçek çekim veya stok yoksa)

**Türkçe özet:** Logosuz iş kıyafetli bir saha teknisyeni yol kenarında tablete bakarak bir noktayı kontrol ediyor. Yüz kameraya dönük değil, el ve tablet ön planda. Tablet ekranı boş/bulanık; içerik kurguda eklenir.

```
Medium over-the-shoulder shot of a municipal field technician in a plain high-visibility safety vest (no logos, no text) and a plain grey work jacket, standing at the edge of an asphalt city street in daylight, looking down at a tablet held in both hands, then glancing at a section of road surface in front of them. The tablet screen shows only a soft, blurred, out-of-focus map-like color field (no readable content). The technician's face is not visible (seen from behind and slightly to the side). Background: softly blurred trees, curb, a distant generic light-grey city bus passing. Handheld but stabilized camera, gentle push-in, 6 seconds, natural overcast daylight, calm professional mood.
STYLE: photorealistic corporate documentary, 16:9, 30 fps.
Negative: readable screen content, text, logos, badges, name tags, close-up face, deformed hands, extra fingers, police, emergency vehicles, warning lights, construction chaos, flicker.
```

## P9 — S9 · Final (YEDEK, R6 yoksa)

**Türkçe özet:** Bulutlu, aydınlık gökyüzü altında açık bir yolda ilerleyen tek markasız otobüs; kamera yavaşça yükselir. Harita geçişi kurguda yapılır.

```
Wide cinematic shot of a single generic city bus driving along a freshly paved open two-lane road on the edge of a city, fields and low hills on both sides, dramatic but bright sky full of large white cumulus clouds with patches of blue, sunlight breaking through. Camera starts low behind and to the side of the bus and slowly rises upward and backward, revealing the road curving toward the distant city on the horizon. Calm, optimistic, quiet ending mood. 8 seconds, ultra smooth.
CONCEPT BUS: generic modern low-floor city bus, plain matte light-grey/white body, darker grey lower skirt, tinted windows, small low-profile roof equipment housings, no logos, no lettering, no destination text, no license plate characters.
STYLE: photorealistic corporate cinematography, natural daylight, restrained palette, 16:9, 3840x2160, 30 fps.
Negative: text, logos, plates, multiple buses, distorted vehicle, extra wheels, sci-fi elements, glowing lines in the sky, lens flare overload, flicker.
```

---

## Kurguya bırakılan öğeler (modele kesinlikle çizdirilmez)

| Öğe | Neden |
|---|---|
| Tüm ekran yazıları ve altyazılar | Türkçe karakterleri (ç, ğ, ı, İ, ö, ş, ü, â) modeller sıkça bozar |
| Sensör etiketleri, bildirim kartları, rozetler | Tutarlılık ve düzeltilebilirlik |
| UlaşımPark / Kocaeli Büyükşehir logoları | Resmî dosya + onay gerekir, YZ hatalı üretir |
| Otobüs livery’si, hat tabelaları, plakalar | Yalnızca gerçek görüntüden |
| Harita coğrafyası ve veri katmanları | Gerçek coğrafya gerekir; YZ uydurur |
| “Temsili veri / Konsept görselleştirme” etiketleri | Şeffaflık zorunluluğu |

## YZ çıktısı kabul kontrol listesi
- [ ] Görüntüde okunabilir veya anlamsız yazı, logo, plaka yok
- [ ] Teker sayısı, kapı sayısı ve gövde oranları doğru, kareler arasında değişmiyor
- [ ] Sensörler P4-IMG’deki konumlarda; cam, ayna, far ve kapıların üzerinde değil
- [ ] Neon, hologram, alarm ışığı, dramatik/distopik öğe yok
- [ ] Yakın plan insan yüzü veya bozuk el yok
- [ ] Renk ve ışık, gerçek görüntülerle (G1/G2) aynı kurguda yan yana durabilecek kadar uyumlu
