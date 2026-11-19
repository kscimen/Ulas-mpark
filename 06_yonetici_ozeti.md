# UlaşımPark Mobil Sensör Ağı — Proje Önerisi Özeti

*Çalışma adı · Proje önerisi · Hazırlayan: [Ad Soyad, unvan/birim]*

**Problem / ihtiyaç.** Kocaeli’de hava kalitesi, yol yüzeyi ve çevresel koşullar sınırlı sayıdaki sabit istasyon, şikâyet ve periyodik saha kontrolleriyle izleniyor. Sabit istasyonlar yüksek kaliteli ama nokta bazlı veri üretiyor. Aradaki geniş alanlar ve gün içi değişimler daha az görünür kalıyor. Yeni sabit istasyon kurmak maliyetli ve yavaş.

**Önerilen çözüm.** Şehirde düzenli güzergâhlarda çalışan UlaşımPark otobüslerine uygun sensörler yerleştirilerek araçlar **hareketli ölçüm noktalarına** dönüştürülür. Sistem sabit istasyonların yerine geçmez; onları **tamamlar**.

**Nasıl çalışır?**
1. Otobüs üstü sensörler partikül madde (PM2.5/PM10), sıcaklık/nem ve yol titreşimi ölçer. Gaz (metan) ve gürültü ayrı, deneysel katmanlar olarak değerlendirilir.
2. Her ölçüm GNSS konumu ve zamanla eşleştirilir. Araç içi veri birimi veriyi kontrol eder, paketler ve mobil ağ üzerinden **yakın gerçek zamanlı** olarak merkezi platforma gönderir. Bağlantı yoksa yerelde saklar.
3. Platform veriyi kalite kontrolünden geçirir ve haritaya işler. Yapay zekâ destekli analizler sensör kalibrasyonuna yardımcı olur, olağan dışı değerleri, tekrar eden örüntüleri ve yoğunlaşan bölgeleri öne çıkarır.
4. Belirlenen eşik ve tekrar kurallarına göre ilgili birime **inceleme / doğrulama bildirimi** oluşturulur. Kararı her zaman uzman ekipler verir. Saha sonuçları sisteme geri beslenir.

**Beklenen faydalar** *(pilotla doğrulanacak)*
- Mevcut araç hareketini kullanarak daha geniş alanda, daha sık güncellenen konum bazlı çevresel veri
- Sabit istasyonlar arasındaki boşlukların tamamlanması, bölgesel farkların görünür olması
- Tekrarlayan yol titreşimi sinyalleriyle yol bakımının önceliklendirilmesine destek
- Çevre, yol bakım, ulaşım planlama ve altyapı birimleri için ortak veri kaynağı
- Kamuya, toplu taşımanın şehre ek katkısını gösteren görünür bir akıllı şehir uygulaması

**Pilot uygulama önerisi**
- **Faz 0. Hazırlık:** Paydaşlar (UlaşımPark, Çevre birimi, Fen İşleri/Yol Bakım, Bilgi İşlem, İZGAZ), veri sahipliği, mevcut araç takip altyapısının incelenmesi, montaj ön projesi, bütçe.
- **Faz 1. Kalibrasyon:** Sensörlerin bir referans istasyonu yanında yan yana çalıştırılması; garajda araç üstü testler (elektrik, EMC, yıkama, titreşim).
- **Faz 2. Saha pilotu:** Az sayıda otobüs (örn. 3–5), referans istasyonlarına yakın 2–3 hat; PM, sıcaklık/nem, titreşim, GNSS. Gaz ölçümü, **CNG olmayan** 1–2 araçla ve dağıtım şirketiyle birlikte ayrı bir fizibilite çalışması olarak.
- **Faz 3–4. Süreç testi ve karar:** Bildirim → saha doğrulama akışının bir-iki birimle denenmesi; genişletme / revizyon kararı.

**Başarı göstergeleri** *(hedef değerler pilot öncesinde baz ölçümle belirlenecek)*
Kalite kontrolünden geçen ölçüm oranı · veri aktarım başarısı ve gecikmesi · konum doğruluğu · referans istasyona göre kalibrasyon sapması · anomali bildirimlerinin saha doğrulanma oranı · bildirim ve doğrulama süreleri · araç başı yıllık donanım, iletişim ve bakım maliyeti · hat ve saat bazında kapsama.

**Bilinen riskler ve ön koşullar.** Düşük maliyetli sensörlerde kalibrasyon ihtiyacı · **CNG’li araçlarda metan ölçümünün aracın kendisinden etkilenmesi** · araç garantisi, montaj ve EMC onayları · bakım sorumluluğu · kurumlar arası veri paylaşım protokolü. Yolcu verisi, kamera görüntüsü ve ses kaydı **toplanmaz**; gürültü için yalnızca ses seviyesi değeri hesaplanır.

**Karar talebi.** Faz 0 hazırlık çalışmasının başlatılması ve ilgili birimlerden birer temsilcinin belirlenmesi.
