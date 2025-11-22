9.1. Güçlü Yönler (Strengths)

Merkezi CSMS altyapısı var
Tüm istasyonların merkeze bağlı olması, log ve fatura verilerini tek noktadan toplama ve analiz etme imkânı sağlıyor.

Otomatik faturalandırma ve log tutma mekanizması mevcut
Ay sonu faturalandırma ve oturum kayıtları zaten sistemde tutuluyor; bu da anomali analizi için veri zemini oluşturuyor.

Anomali kuralları tanımlanmış ve olay tespit edilmiş
Aylık tüketimde aşırı artış, aynı gün farklı illerde çok sayıda oturum vb. kurallar sayesinde U-4582 vakası yakalanmış.

Olay sonrası iyileştirme adımları belirlenmiş
Kart güvenliği, gerçek zamanlı anomali tespiti, log izleme ve müşteri/hukuki süreçlere dair net öneriler sunulmuş.

Bilgi güvenliği farkındalığı artmış
Bu olay, kurumun RFID güvenliği, anomali tespiti ve SIEM ihtiyacını görmesini sağlamış durumda.

9.2. Zayıf Yönler (Weaknesses)

RFID kartlar kriptografik olarak yeterince güvenli değil
Sadece kart ID’si üzerinden doğrulama yapılıyor, kart klonlamaya açık bir yapı var.

Karşılıklı kimlik doğrulama (mutual authentication) eksik
Kart–istasyon–merkez arasında güçlü şifreleme ve kimlik doğrulama mekanizması yok.

Gerçek zamanlı anomali tespit sistemi başlangıçta yok
Aynı kartın kısa sürede farklı illerde kullanılması gibi bariz anomali durumları anlık yakalanamamış.

Log analizi reaktif, proaktif değil
Loglar tutuluyor ama SIEM vb. merkezi analiz araçlarıyla sürekli izlenmediği için olay geç fark ediliyor.

İstasyon yönetim ekranlarında zayıf erişim kontrolü
Lokal tanımlama ekranlarına yetkisiz erişim riski, kart manipülasyonu ihtimalini artırıyor.

Müşteri tarafında anlık bildirim/uyarı mekanizması zayıf
Kullanıcıya “olağan dışı kullanım” uyarısı gitmediği için mağduriyet daha geç fark ediliyor.

9.3. Fırsatlar (Opportunities)

Güvenlik yatırımıyla marka itibarını güçlendirme fırsatı
Kriptografik kartlar, mobil token/QR, 2FA gibi önlemler alınırsa, firma “güvenli şarj altyapısı” imajıyla öne çıkabilir.

Regülasyonlara uyum ve teşviklerden yararlanma
Enerji ve siber güvenlik regülasyonlarına uyum sağlamak, hem ceza riskini azaltır hem de bazı teşvik/hibe programlarını açabilir.

Yeni ürün ve hizmet geliştirme
Gerçek zamanlı anomali tespiti, müşteri portalı, anlık bildirim, harcama limiti koyma gibi özellikler, ek gelir/avantaj sağlayabilir.

Akademik ve endüstriyel iş birlikleri
Anomali tespiti, makine öğrenmesi, siber güvenlik alanlarında üniversite ve teknoloji firmalarıyla ortak projeler yürütülebilir.

Müşteri güvenini artırma
Bu vaka doğru yönetilir ve şeffaf şekilde çözülürse, “şirket mağduriyetleri telafi ediyor ve proaktif önlem alıyor” algısı oluşabilir.

9.4. Tehditler (Threats)

Gelişmiş kart klonlama ve siber saldırı teknikleri
Saldırganlar RFID, mobil uygulama ve backend API’lere yönelik daha karmaşık saldırılar geliştirebilir.

Finansal kayıp ve yasal yaptırımlar
Çok sayıda kullanıcının mağdur olması halinde şirket ciddi geri ödeme, ceza ve tazminat yüküyle karşılaşabilir.

Müşteri güven kaybı ve itibar zedelenmesi
“Şarj istasyonları güvensiz, kartlar kopyalanıyor” algısı yayılırsa, kullanıcılar alternatif firmalara yönelebilir.

Regülasyonların sıkılaşması
Bu tür vakalar arttıkça, devlet kurumları daha katı güvenlik ve KVKK/kişisel veri yükümlülükleri getirebilir.

İç tehditler (insider)
İstasyon personelinin veya içeriden biri tarafından kart bilgisi sızdırılması riski sürekli var.