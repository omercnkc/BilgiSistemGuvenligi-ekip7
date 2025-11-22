ELEKTRİKLİ ARAÇ ŞARJ İSTASYONLARINDA FATURA / DOLANDIRICILIK 
1. Giriş
Bu raporda, elektrikli araç şarj istasyonlarında kullanılan bilgi sistemlerinde ortaya çıkabilecek faturalandırma ve dolandırıcılık odaklı bir anomali ele alınmaktadır. Amaç, bir kullanıcı hesabı üzerinden aşırı ve gerçekçi olmayan enerji tüketimi tespit edilen senaryoyu inceleyerek bilgi sistemleri güvenliği açısından zayıf noktaları ve alınabilecek önlemleri özetlemektir.
 
2. Sistem Özeti
Enerji şirketi ülke genelinde yaklaşık 200 şarj istasyonu işletmektedir.
•	Kullanıcılar şarjı:
o	Mobil uygulama,
o	RFID kart,
o	Kredi kartı ile başlatabilmektedir.
•	Tüm istasyonlar, merkezdeki Şarj İstasyonu Yönetim Sistemi (CSMS)’e bağlıdır.
•	Faturalandırma modülü, ay sonunda kullanıcıların toplam kWh tüketimine göre faturaları otomatik üretir.
•	Tarife:
o	Gündüz: 1 kWh = 5 TL
o	Gece: 1 kWh = 4 TL
 
3. Anomalinin Tespiti
Ay sonu faturalandırmada U-4582 kullanıcı ID’si için anomali tespit edilmiştir:
•	Önceki aylarda:
o	Aylık ~250 kWh
o	1000–1200 TL fatura
•	Bu ay:
o	2200 kWh tüketim
o	10.500 TL fatura
Detaylı incelemede:
•	Aynı gün içinde birkaç farklı ilde onlarca şarj oturumu görülmüştür.
•	Oturumlar arası süre çok kısadır (5–10 dakika), fiziksel olarak aracın şehir değiştirmesi mümkün değildir.
•	Oturumların çoğu gece saatlerinde, 1–2 kWh’lık küçük ama çok sayıda şarj şeklindedir.
Bu durum, sistemdeki anomali kurallarını tetiklemiş ve “fatura / kullanım anomalisi” olarak işaretlenmiştir.
 
4. Olası Neden
Log ve kart kayıtları incelendiğinde:
•	Tüm oturumların aynı RFID kart kimliğiyle açıldığı görülmüştür.
•	Kart daha önce bir istasyonda tanımlanmış, aynı istasyonda gece saatlerinde şüpheli kart işlemleri loglanmıştır.
Buna göre olası senaryo:
•	Kullanıcıya ait RFID kart kopyalanmıştır.
•	Saldırgan kopya kartla farklı şehirlerde kendi şarjlarını yapmış,
•	Tüm tüketim mağdur kullanıcının hesabına yazılmıştır.
•	Gece tarifesinden faydalanmak için çok sayıda küçük oturum açılmış, böylece toplam kWh ve fatura şişirilmiştir.
 
5. Güvenlik Zafiyetleri
Olayın ortaya çıkardığı başlıca zafiyetler:
•	RFID kartların sadece kart ID’si ile doğrulanması, kriptografik güvenlik ve karşılıklı kimlik doğrulamanın olmaması.
•	İstasyonlardaki lokal kart tanımlama/yönetim ekranlarına erişimin yeterince kısıtlanmaması.
•	Aynı kartın kısa süre içinde farklı şehirlerdeki istasyonlarda kullanılması durumunu gerçek zamanlı izleyen gelişmiş anomali sisteminin başlangıçta bulunmaması.
•	Kart işlemlerine ait logların merkezi olarak yeterince analiz edilmemesi.
 
6. Alınan / Önerilen Önlemler
Olay sonrası uygulanan ve önerilen önlemler:
1.	Kart Güvenliği
o	Basit RFID kartlar yerine kriptografik olarak güvenli kartlar veya mobil uygulama tabanlı token/QR sistemine geçilmesi.
o	Kart–istasyon iletişiminde şifreleme ve karşılıklı kimlik doğrulaması kullanılması.
2.	Gerçek Zamanlı Anomali Tespiti
o	Aynı kartın kısa sürede farklı illerde kullanılması durumunda otomatik blokaj ve alarm.
o	Aylık tüketimi önceki aylara göre belirli katın üzerinde artan kullanıcılar için manuel inceleme süreci.
3.	Yetki ve Log Yönetimi
o	Kart tanımlama işlemlerinin sadece merkezden ve yetkili personel tarafından yapılması.
o	İstasyon yönetim ekranlarına güçlü parola, 2FA ve IP kısıtlaması getirilmesi.
o	Kart ve oturum loglarının SIEM üzerinden düzenli izlenmesi.
4.	Müşteri ve Hukuki Süreç
o	Mağdur kullanıcının faturası dondurularak gerçek tüketim ayrıştırılmış, düzeltilmiş fatura düzenlenmiştir.
o	Gerek görülürse olay adli makamlara bildirilmiştir.
 
7. Sonuç
Bu raporda, elektrikli araç şarj istasyonlarında ortaya çıkan faturalandırma kaynaklı bir güvenlik anomalisi özetlenmiştir. Olay, RFID kart güvenliğinin zayıf olması, anomali tespit mekanizmalarının yetersizliği ve log yönetimindeki eksiklikler nedeniyle gerçekleşmiştir. Elektrikli araç altyapıları büyüdükçe, bu tür sistemlerde kimlik doğrulama, şifreleme, log analizi ve anomali tespiti gibi bilgi güvenliği katmanlarının güçlendirilmesi zorunlu hâle gelmektedir.
8. Kaynakça
1.	Hamdare, S. ve diğ. (2025). Cyber defense in OCPP for EV charging security risks. International Journal of Information Security. 
2.	Alcaraz, C., Cumplido, J., & Lopez, J. (2023). Threats and countermeasures for electric vehicle charging infrastructure. International Journal of Information Security. 
3.	Kern, D. ve diğ. (2023). Detection of Anomalies in Electric Vehicle Charging Sessions. ACM Proceedings – hibrit saldırı tespit ve anomali analizi çalışması. Mitikiri, S. B. ve diğ. (2025). Regression based anomaly detection in electric vehicle charging infrastructure. Sustainable Energy, Grids and Networks. 
4.	Nexess Solutions. (2023). RFID security: Challenges and solutions to protect your sensitive data. (RFID kart klonlama ve güvenlik riskleri üzerine teknik inceleme). 
