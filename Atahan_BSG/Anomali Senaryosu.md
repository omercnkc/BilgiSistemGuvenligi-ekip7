Raporum, Bilgi Sistemleri ve Güvenliği dersi kapsamında, elektrikli araç şarj istasyonlarının (EVCS) güvenliğini analiz etmeyi amaçlamaktadır.

1.  Ana Odak ve Makale Temeli
Projemin temeli, "Anomaly Detection in Electric Vehicle Charging Stations Using Federated Learning" başlıklı güncel bir akademik makaledir.

Merkezi konu, büyük şarj ağlarında kullanıcı gizliliğini koruyarak etkili bir anomali tespiti yapma zorluğudur.

Çözüm yaklaşımı olarak, dağıtık öğrenme modeli olan Federated Learning (Birleşik Öğrenme) metodu inceledim.

2. İncelenen Kritik Anomali Senaryosu
İncelediğim anomali senaryosu, şarj istasyonu ağına yönelik bir Hizmet Reddi (DoS) Saldırısıdır.

Bu anomali, şarj cihazı ile merkezi sunucu (CSMS) arasındaki iletişim protokolü olan OCPP trafiğinde ortaya çıkar.

Anomali Tanımı: Normalde az sayıda olması beklenen "Kimlik Doğrulama İsteği" gibi kritik OCPP mesajlarının, saldırı anında frekansında ani ve anormal bir artış olmasıdır.

Etkileri: Bu durum, yasal kullanıcıların şarj olmasını engeller, hizmet sağlayıcının gelir kaybına yol açar ve enerji şebekesindeki dengeyi tehdit eder.

3. SWOT Analizi (Ana Çıkarımlar)
Güçlü Yön (S): En büyük avantajımız, veri gizliliğini koruyan Federated Learning (FL) metodunu kullanma potansiyelidir. Veri, yerelde kalır.

Zayıf Yön (W): Farklı markaların farklı yazılımlar kullanması nedeniyle oluşan sistem ve veri uyumsuzluğu (Heterojenite), güvenlik modelinin performansını düşürmektedir.

Fırsat (O): FL, ölçek büyüdükçe gizlilik avantajıyla öne çıkarak yüksek doğrulukta güvenlik çözümleri sunma fırsatı yaratır.

Tehdit (T): DoS ve kripto madenciliği gibi mevcut siber saldırıların yanı sıra, FL modellerine özel "Model Zehirlenmesi" gibi yeni saldırı türleri tehdit oluşturur.

4. Çözüm Önerileri ve Değerlendirme
Temel Çözüm: Merkezi sistem yerine, her istasyonda FL ile eğitilmiş yerel Giriş Tespit Sistemlerinin (IDS) kullanılması önerilebilir.

Tamamlayıcı Çözüm: Protokol seviyesinde, şüpheli IP'lerden gelen kritik OCPP komutları için Hız Sınırlaması (Rate Limiting) getirilmelidir.

Öğrenilen Ders: Raporum, modern altyapılarda güvenliğin, sadece merkezi bir duvar örmekten öte, dağıtık ve gizlilik odaklı (FL gibi) yaklaşımları gerektirdiğini göstermiştir.

Eksik Yön: Proje teorik kalmıştır; önerilen çözümün gerçek bir simülasyon ortamında test edilerek nicel başarı (doğruluk, hata oranları) ölçülememiştir.
