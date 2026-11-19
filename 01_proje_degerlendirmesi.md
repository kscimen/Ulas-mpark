# Teslimat 1 — Proje Değerlendirmesi

> Proje önerisi aşamasındadır. Burada geçen sensör sınıfları, mimari ve pilot adımları **öneri**dir. Maliyet, hedef değer veya performans rakamı verilmemiştir; bunlar pilot öncesi piyasa araştırması ve baz ölçümle belirlenmelidir.

---

## 1. İsim değerlendirmesi

| Aday | Değerlendirme | Karar |
|---|---|---|
| UlaşımPark Akıllı Mobil Çevresel İzleme Sistemi | Açıklayıcı ama uzun; resmî yazışma başlığı olarak uygun | **Resmî proje başlığı** |
| **UlaşımPark Mobil Sensör Ağı** | Kısa, Türkçe, sahipliği (UlaşımPark) ve ne olduğunu (sensör ağı) net söylüyor; “çevre izleme otoritesi” iddiası taşımıyor | **Önerilen kısa çalışma adı** |
| Kocaeli Akıllı Çevre İzleme Ağı | İl genelinde bir çevre izleme yetkisi çağrıştırıyor; bu yetki Çevre birimleri ve Bakanlık’ta. Kurumlar arası sahiplik karışabilir | Önerilmez |
| UlaşımPark Smart Mobility & Environment | İngilizce; kamu iletişiminde yabancı dil tercihi zayıf | Önerilmez |
| Kocaeli Hareketli Veri Ağı | Akılda kalıcı ama sahibi ve içeriği belirsiz | Kampanya dili için alternatif |

**Kural:** İsim, onaylanana kadar her yerde “çalışma adı / proje önerisi” notuyla kullanılır. Logo veya alt marka tasarlanmaz.

---

## 2. Fikrin güçlü yönleri

1. **Var olan hareketi kullanır.** Otobüsler zaten her gün, belli güzergâhlarda, belli saatlerde dolaşıyor. Ölçüm için ayrıca araç veya personel görevlendirmek gerekmiyor.
2. **Tekrarlı geçiş = doğal doğrulama.** Aynı nokta günde defalarca, farklı araçlarla geçiliyor. Tek ölçümle karar yerine tekrar eden sinyale dayanmak mümkün. Bu, düşük maliyetli sensörlerin zayıflığını kısmen dengeliyor.
3. **Sabit istasyonları tamamlar.** Sabit istasyonlar az sayıda noktada yüksek kaliteli veri üretir. Mobil ağ, aradaki boşlukları daha düşük doğrulukla ama daha geniş alanda gösterebilir.
4. **Kurumlar arası değer.** Aynı veri; çevre, fen işleri/yol bakım, ulaşım planlama ve doğalgaz dağıtım şirketi gibi birden fazla birime fayda sağlayabilir.
5. **Ölçeklenebilir.** Küçük bir pilotla başlayıp sonuçlara göre genişletilebilir. Başarısız bir sensör türü projeyi bütünüyle durdurmaz, yalnızca o katman çıkarılır.
6. **Görünür kamu hizmeti.** Toplu taşımanın şehir yaşamına ek katkısını somut biçimde anlatır.

---

## 3. Sensör ve donanım sınıfları — uygulanabilirlik matrisi

Puanlama: ●●● yüksek, ●● orta, ● düşük. Kaynak: genel mühendislik değerlendirmesi. Pilotta sahada doğrulanmalıdır.

| Katman | Önerilen sensör sınıfı | Teknik olgunluk (araç üstü) | Göreli maliyet | Ölçüm güvenilirliği | Pilot önceliği |
|---|---|---|---|---|---|
| GNSS konum + zaman | Çok uyduluklu (GPS/Galileo/GLONASS/BeiDou) GNSS alıcı; mümkünse mevcut araç takip sistemi | ●●● | ● | ●●● (şehir içi yansıma hariç) | **Zorunlu** |
| Partikül madde (PM2.5/PM10) | Optik/lazer saçılımlı partikül sensörü, aktif fanlı, nem düzeltmeli | ●●● | ● | ●● (kalibrasyonla) | **1. öncelik** |
| Sıcaklık / nem | Radyasyon kalkanlı dijital T/RH sensörü | ●●● | ● | ●● (araç ısısından etkilenir) | **1. öncelik** (PM düzeltmesi için de gerekli) |
| Yol titreşimi | Şasiye rijit bağlı 3 eksenli ivmeölçer / IMU | ●●● | ● | ●● (tekrarlı geçişle) | **1. öncelik** |
| Gaz (CH₄) | (a) NDIR metan sensörü: düşük maliyet, düşük hassasiyet; (b) lazer tabanlı (TDLAS vb.) yüksek hassasiyetli analizör | (a) ●● / (b) ●● | (a) ●● / (b) ●●● | (a) ● sızıntı izi için yetersiz / (b) ●●● | **Ayrı alt çalışma**, 1–2 araç |
| Gürültü | IEC 61672 sınıfına uygun ses seviyesi ölçer modülü, rüzgâr korumalı, yalnızca dB(A) hesaplayan | ●● | ●● | ● (araç kendi gürültüsü baskın) | **Deneysel**, 2. faz |
| Rüzgâr (opsiyonel) | Araç hızıyla düzeltilmiş ultrasonik anemometre veya dış kaynak meteoroloji verisi | ● | ●● | ● | Gaz çalışması varsa gerekli |

### 3.1 Partikül madde (PM2.5/PM10)
- **Montaj:** Tavanın ön bölümü, egzoz çıkışından uzak, aracın hareket yönüne bakan ama doğrudan hava akışına maruz kalmayan korumalı emiş. Dizel araçlarda egzoz konumu mutlaka hesaba katılmalı.
- **Etkileyen faktörler:** Yüksek nem (partikül şişmesi → yüksek okuma), araç hızıyla değişen hava akışı, yol tozu, fren/lastik aşınması, durak bekleme anları.
- **Gerekenler:** Nem düzeltmesi (veya ısıtmalı emiş), sensör yaşlanma takibi, düzenli temizlik ve **referans istasyonlarla yan yana kalibrasyon** (co-location).
- **Referans:** Çevre, Şehircilik ve İklim Değişikliği Bakanlığı’nın Ulusal Hava Kalitesi İzleme Ağı’na bağlı, Kocaeli’deki sabit istasyonlar. Güzergâhı bu istasyonların yakınından geçen hatlar pilot için avantajlıdır.

### 3.2 Gaz (metan / doğalgaz) — en riskli katman
- **CNG çelişkisi:** Sağlanan videolarda en az bir aracın CNG’li olduğu görülüyor. CNG’li bir araçta yakıt sistemi, egzoz (yanmamış metan) ve dolum istasyonları metan kaynağıdır. Araç üstü sensör kendi aracının metanını ölçebilir.
  - Çözüm seçenekleri: (1) Gaz pilotu için **CNG olmayan** (dizel/elektrikli) araç seçmek, (2) emişi aracın en ön-üst noktasına, yakıt hattı ve egzozdan uzağa yerleştirmek, (3) araç duruşları, dolum istasyonu yakınları ve rölanti anları için otomatik dışlama kuralları, (4) mümkünse araç üzerinde ikinci bir “öz-kaynak” referans sensörü.
- **Hassasiyet sorunu:** Atmosferdeki metan zaten yaklaşık 2 ppm civarındadır. Sokaktaki sızıntı izleri çoğu zaman bunun ancak biraz üzerindedir ve araç hızında saniyeler içinde geçer. Genel amaçlı MOX/elektrokimyasal sensörler bunu güvenilir göremez. Hızlı tepki veren, ppb düzeyinde lazer tabanlı analizörler gerekir. Bu cihazlar diğer sensörlere göre belirgin biçimde pahalıdır.
- **Kaynak ayrımı:** Metan; doğalgaz şebekesi, kanalizasyon, çöp, atık su ve sulak alanlardan da gelir. Gelişmiş sistemlerde etan eş-ölçümü doğalgaz kaynağını ayırt etmeye yardımcı olur, ancak maliyeti artırır.
- **Konumlandırma ilkesi:** Sistem **kaçak teşhisi yapmaz**. “Bu koordinatta, bu saatte, olağan dışı metan yükselmesi ölçüldü” bilgisini **doğalgaz dağıtım şirketine (Kocaeli’de İZGAZ)** ve ilgili belediye birimine doğrulama talebi olarak iletir. Acil durum hattının (187) yerine geçmez.
- **Öneri:** Gaz katmanı, ana pilottan ayrı, 1–2 araçlık, dağıtım şirketiyle birlikte tasarlanan bir **fizibilite alt çalışması** olarak ele alınmalı. Videoda da “şüpheli ölçüm → uzman doğrulaması” dili korunmalı.

### 3.3 Gürültü
- Araç üstü mikrofon, aracın kendi motor, lastik ve rüzgâr gürültüsünü baskın olarak ölçer. Mutlak çevresel gürültü seviyesi çıkarmak zordur.
- Gerçekçi kullanım: (a) belli hız aralığında, aynı noktadaki **göreli değişimler**, (b) durak bekleme anlarında (motor rölanti etkisi ayrıştırılarak) ortam seviyesi.
- **Gizlilik:** Ses kenar cihazda anında dB(A) değerine çevrilir; **ses kaydı ve konuşma içeriği tutulmaz, iletilmez**. Bu, donanım/yazılım tasarımıyla garanti edilmeli ve belgelenmelidir.
- Resmî stratejik gürültü haritaları mevzuat gereği modelleme ve standart ölçümle üretilir. Mobil veri bunların yerini tutmaz, yalnızca destekleyici bir göstergedir.

### 3.4 Yol titreşimi
- İvmeölçer şasiye rijit bağlanmalı (gövde panelleri yerine). Ölçüm araç hızı, yük durumu ve süspansiyon tipine göre normalize edilmeli.
- Tek bir sarsıntı çukur demek değildir (rögar kapağı, hız kesici, ray geçişi olabilir). **Farklı araçlarda ve farklı seferlerde aynı konumda tekrarlanan** sinyaller önceliklendirilir. Bilinen hız kesici/ray geçişi konumları maskelenir.
- Çıktı “olası yol yüzeyi bozukluğu, saha kontrolü önerilir” şeklindedir.

### 3.5 Konum ve zaman
- Ölçümler GNSS zamanıyla senkronlanır. Şehir içi yüksek bina ve köprü altlarında konum sapması olur; harita eşleme (map-matching) ile hat geometrisine oturtulur.
- **Varsayım:** Araçlarda mevcut bir araç takip (AVL) sistemi olabilir. Yeniden kullanılabilirse ayrı GNSS ve modem ihtiyacı azalır. Mevcut sistem sağlayıcısıyla teknik görüşme gerekir.

### 3.6 Araç entegrasyonu (tüm katmanlar)
- **Elektrik:** Araç 24 V sistemi, kontak kapalıyken ne olacağı, akü tüketimi, sigorta ve kablo güzergâhı.
- **Elektromanyetik uyumluluk:** Araç üstü elektronik için E-işareti / UNECE R10 (EMC) uygunluğu aranmalı.
- **Mekanik:** Tavan yüklemesi, CNG tank kaportasıyla çakışma, garaj kapı ve tavan yükseklikleri, **otomatik yıkama fırçaları**, titreşim dayanımı, IP koruma sınıfı.
- **Garanti ve mevzuat:** Araç üreticisi garantisi, muayene uygunluğu ve montaj projesi teknik onaya tabidir. Videoda montaj “konsept yerleşim” olarak gösterilir.
- **Bakım:** Filtre/emiş temizliği, kalibrasyon periyodu, arızalı sensör değişimi. Bu işlerin hangi ekibe ait olacağı tanımlanmalıdır.

---

## 4. Veri iletişimi ve merkezi platform

```
[Sensörler] ─▶ [Araç içi ağ geçidi / edge]
                 • zaman+konum damgası
                 • temel kalite kontrol (aralık, takılma, sıçrama)
                 • titreşimden öznitelik çıkarımı (ham yüksek frekans veri gönderilmez)
                 • sesi dB(A)'ya çevirme (ses içeriği tutulmaz)
                 • yerel tampon depolama (bağlantı kesilirse)
               ─▶ [Mobil ağ (4G/5G), şifreli bağlantı (TLS), hafif protokol (ör. MQTT)]
               ─▶ [Merkezi veri platformu]
                 • zaman serisi + mekânsal veritabanı
                 • kalite bayrakları, kalibrasyon katsayıları, sensör sağlık izleme
                 • harita servisleri (katmanlar, zaman kaydırıcı)
                 • analitik / YZ modülleri
                 • kural tabanlı bildirim motoru (eşik + tekrar + doğrulama durumu)
               ─▶ [Yetkili kullanıcı arayüzü]  ─▶ [İlgili birime bildirim]
                                                    ◀── saha doğrulama sonucu (geri besleme)
```

- **“Anlık” değil “yakın gerçek zamanlı”.** Gönderim aralığı (ör. birkaç saniye ile birkaç dakika arası) ve kabul edilebilir gecikme pilotta tanımlanmalıdır. O zamana kadar iletişimde “yakın gerçek zamanlı” ifadesi kullanılır.
- **Açık standartlar:** Sensör verisi için OGC SensorThings API gibi açık bir standart, ileride Kocaeli Büyükşehir’in diğer akıllı şehir sistemleri ve açık veri portalıyla entegrasyonu kolaylaştırır. Bu entegrasyon **henüz yoktur**, hedeflenen yapıdır.
- **Barındırma:** Kamu verisinin yerinde/yurt içinde barındırılması, Bilgi İşlem Dairesi’nin güvenlik politikalarına uyum.
- **Veri sahipliği:** Verinin sahibi (UlaşımPark mı, Büyükşehir mi), erişim yetkileri ve diğer birimlerle paylaşım protokolü baştan yazılmalıdır.

---

## 5. Yapay zekânın gerçekçi kullanım alanları

| Görev | Yöntem sınıfı (örnek) | Çıktı | İnsan rolü |
|---|---|---|---|
| **Sensör kalibrasyonu** | Referans istasyon verisiyle eğitilen düzeltme modelleri (regresyon, gradyan artırma) | Nem/sıcaklık etkisi düzeltilmiş PM değerleri | Model doğrulama, periyodik yeniden eğitim |
| Olağan dışı değer tespiti | İstatistiksel taban çizgisi, zaman-mekân bazlı aykırı değer modelleri | “Bu ölçüm bu saat ve bölge için olağan dışı” bayrağı | Eşiklerin uzmanlarca belirlenmesi |
| Mekânsal yoğunlaşma | Sıcak nokta analizi, kümeleme | Haritada tekrarlayan yüksek değer bölgeleri | Yorumlama, saha kontrol kararı |
| Yol bozukluğu önceliklendirme | Tekrarlı geçiş kümelemesi, hız normalizasyonu | Öncelik sıralı saha kontrol listesi | Saha ekibi doğrulaması |
| Gaz şüphesi yönlendirme | Arka plan çıkarımı + öz-kaynak filtreleri + kural motoru | Doğrulama talebi (konum, zaman, güven düzeyi) | **Uzman ekip doğrulaması zorunlu** |
| Eğilim ve özet | Zaman serisi karşılaştırmaları; isteğe bağlı dil modeli ile metin özetleri | Haftalık/aylık özet raporları | Yöneticinin değerlendirmesi |
| Sensör sağlığı | Kayma (drift) ve arıza tespiti | Bakım uyarısı | Bakım ekibi |

**İlke:** YZ, sinyal ile gürültüyü ayırmaya ve dikkat edilmesi gereken yeri işaretlemeye yardım eder. **Teşhis koymaz, karar vermez.** Her bildirim; eşik, uzman kuralı, sensör kalite bayrağı ve saha doğrulamasıyla birlikte çalışır. Saha sonuçları modele geri beslenir.

---

## 6. Teknik ve operasyonel riskler

| # | Risk | Etki | Azaltma |
|---|---|---|---|
| R1 | Düşük maliyetli sensörlerde kayma ve nem etkisi | Yanlış yüksek/düşük değer | Co-location kalibrasyonu, periyodik kontrol, kalite bayrağı |
| R2 | **CNG araçta öz-kaynak metan** | Yanlış gaz alarmı, güven kaybı | Gaz pilotunu CNG olmayan araçta yap; dışlama kuralları |
| R3 | Araç kaynaklı PM/gürültü | Sistematik sapma | Montaj konumu, hız/duruş filtreleri |
| R4 | Kapsama yanlılığı (yalnız hat güzergâhları, servis saatleri) | Haritada boşluklar yanlış yorumlanabilir | Kapsama haritasını ayrıca göster; “ölçüm yok” ≠ “temiz” |
| R5 | Yanlış alarm yükü | Birimlerin bildirimleri göz ardı etmesi | Tekrar şartı, kademeli bildirim, pilotta birimlerle eşik belirleme |
| R6 | Araç garantisi / mevzuat / EMC | Montaj iptali | Üretici ve muayene süreçleriyle erken görüşme, sertifikalı donanım |
| R7 | Bakım yükü, yıkama, vandalizm | Veri kaybı, ek maliyet | Sağlam muhafaza, bakım sorumluluğunun tanımı |
| R8 | İletişim kesintisi | Veri boşluğu | Yerel tampon, tekrar gönderim |
| R9 | Veri sahipliği ve kurumlar arası iş akışı belirsizliği | Bildirimlerin sahipsiz kalması | Protokol, sorumlu birim ve yanıt süresi tanımı |
| R10 | Siber güvenlik | Veri bütünlüğü, sistem erişimi | Şifreleme, cihaz kimlik doğrulama, erişim kontrolü, kayıt |
| R11 | Kamuoyu algısı (“otobüsler bizi dinliyor”) | İtibar riski | Ses kaydı yapılmadığının açık iletişimi, kamera yok |

---

## 7. Gizlilik ve güvenlik ilkeleri

- Amaç çevresel ve kentsel ölçümdür. **Yolcu verisi, kamera görüntüsü ve ses kaydı toplanmaz.**
- Gürültü için yalnızca ses seviyesi değeri üretilir. Ham ses cihazda bile saklanmaz.
- Araç konumu ile vardiya/sürücü bilgisi birleştirilmez. Analiz platformunda araç kimliği gerekirse takma adlandırılır (KVKK).
- Erişim rol bazlıdır; tüm erişimler kayıt altına alınır. Saklama süreleri tanımlanır.
- Gaz ve diğer uyarılar ilgili uzman ekiplerin doğrulamasına tabidir.
- Belediye birimleriyle entegrasyon **hedeflenen yapıdır**, mevcut değildir.

---

## 8. Pilot uygulama önerisi

| Faz | İçerik | Çıktı |
|---|---|---|
| **Faz 0. Hazırlık** | Paydaş toplantıları (UlaşımPark, Çevre birimi, Fen İşleri/Yol Bakım, Bilgi İşlem, İZGAZ); veri sahipliği; mevcut AVL/telematik incelemesi; sensör piyasa araştırması; montaj ön projesi | Pilot planı, sorumluluk matrisi, bütçe tahmini |
| **Faz 1. Masa başı ve yan yana kalibrasyon** | Sensör kitlerinin bir referans istasyonu yanında sabit olarak çalıştırılması; ardından garajda araç üstü testler (elektrik, EMC, yıkama, titreşim) | Kalibrasyon katsayıları, montaj doğrulaması |
| **Faz 2. Sınırlı saha pilotu** | Az sayıda otobüs (örn. 3–5), referans istasyonlarına yakın 2–3 hat; PM + T/RH + titreşim + GNSS. Gaz için 1–2 CNG olmayan araçla ayrı alt çalışma | Kalite kontrollü veri seti, kapsama analizi |
| **Faz 3. Süreç testi** | Bildirim akışının bir veya iki birimle denenmesi; saha doğrulama sonuçlarının sisteme geri beslenmesi | Bildirim → doğrulama süreleri, doğrulanma oranları |
| **Faz 4. Değerlendirme ve karar** | Başarı göstergelerinin baz değerlerle karşılaştırılması; sensör seti, hat ve kapsam kararı | Genişletme / revizyon / sonlandırma kararı |

Süreler Faz 0’da, gerçek tedarik ve onay süreçlerine göre belirlenmelidir.

### Başarı göstergeleri (hedef değerler pilot öncesi belirlenmeli)

| Gösterge | Nasıl ölçülür |
|---|---|
| Kalite kontrolünden geçen ölçüm oranı | Geçerli kayıt / toplam kayıt |
| Veri aktarım başarı oranı ve gecikme | Gönderilen/ulaşan paket; ölçüm–kayıt zaman farkı dağılımı |
| Konum doğruluğu | Bilinen noktalardaki sapma, map-matching başarı oranı |
| Kalibrasyon sapması | Referans istasyon yanından geçişlerde fark; zaman içindeki kayma |
| Anomali doğrulanma oranı | Saha kontrolüyle doğrulanan / bildirilen |
| Bildirim süresi | Anomali tespiti → birime ulaşma |
| Saha doğrulanma süresi ve oranı | Birim yanıt süresi, doğrulanan olay oranı |
| Araç başı maliyet | Donanım + montaj + iletişim + bakım (yıllık) |
| Kapsama | Güzergâh-km ve saat dilimine göre ölçüm yoğunluğu |

---

## 9. Varsayımlar ve netleşmemiş konular

- Filonun yakıt türü dağılımı (CNG / dizel / elektrikli).
- Araçlarda mevcut AVL, modem, güç ve veri altyapısı, sağlayıcı sözleşmeleri.
- Verinin sahibi ve sistemin hangi birimin bütçesinden/sorumluluğunda olacağı.
- Bildirim alacak birimlerin ve doğalgaz dağıtım şirketinin işbirliğine açıklığı.
- Sabit istasyon verisine erişim (Bakanlık / Büyükşehir) ve kalibrasyon için yan yana ölçüm izni.
- Sensör tedarik, garanti, muayene ve montaj onay süreçleri.
- Bütçe ve finansman modeli (öz kaynak, AB/kalkınma ajansı akıllı şehir hibeleri vb.). Hiçbir maliyet tahmini yapılmamıştır.
