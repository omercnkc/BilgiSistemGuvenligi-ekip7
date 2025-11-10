# Rapor: “Hayalet Araç” Yükü (Ghost/Phantom Vehicle Load) — Anomali ve Güvenlik Analizi



## 1. Kısa Özet
“Hayalet Araç” yükü senaryosu: Saldırgan, fiziksel olarak bağlı olmayan (yani gerçekte şarj kablosu takılı olmayan) araçlar için şarj oturumları başlatarak veya sahte şarj oturum verisi göndererek şebekede beklenmedik düşük voltaj / anormal yük davranışları yaratır. Bu durum enerji dengesini bozar, izlemeyi yanıltır ve doğrulanmamış 'tüketim' sinyalleriyle şebeke koruma mantıklarını tetikleyebilir. 
________________________________________

## 2. Neden mümkün? (Saldırı yüzeyleri ve zaafiyetler)
•	Şarj istasyonları ve yönetim yazılımları (OCPP, API’ler, CPO platformları) internet / yönetim ağına bağlıdır; zayıf konfigürasyon, eksik kimlik doğrulama veya açık API’ler saldırgan için giriş noktası sağlar. Bu altyapının suistimal edilmesiyle sahte oturumlar/komutlar yaratmak teknik olarak mümkündür. 
•	Yönetim sunucuları/aggregator’lar yanlış veya doğrulanmamış telemetriyi kabul ederse, "aktif şarj" olarak raporlanan ama fiilen bağlı olmayan araçlar üzerinden yanlış yük hesapları oluşabilir. Bu, izleme/ölçekleme kararlarını yanıltır. 
_______________________________________

## 3. Saldırının işleyişi (adım adım)
1.	Keşif: Hedef CPO/EVSE ağlarının ve API uç noktalarının tespiti.
2.	İstismar: Zayıf kimlik doğrulama, açık yönetim portları, veya çalınmış API/otomasyon kimlik bilgileriyle sistem erişimi. 
3.	Sahte Oturum Başlatma: Yönetim sistemine veya backend’e, sahte bir ‘charging session’ / startCharging komutu gönderilir; oturum metrikleri (akım, gerilim, teslim edilen enerji) ya tamamen sahte ya da kısmen manipüle edilmiş olur. 
4.	Eşzamanlı Etki: Binlerce sahte oturum aynı dönem içinde raporlanır — gözlemciler bunun gerçek bir yük değişimi olduğunu düşünebilir; şebeke kontrol mekanizmaları yanlış tepki verebilir. 
________________________________________

## 4. Potansiyel Etkiler
•	Yanıltıcı SCADA/EMS kararları: Şebeke yönetimi yanlış yük düşüklüğü/çoğalması algılayıp gereksiz şalt/rezerv devreye alma veya frekans kontrol hamleleri yapabilir. 
•	Gerçek şebeke instabilitesi: Eğer saldırgan aynı anda hem şarj başlatma hem de şarj durdurma manipülasyonu yaparsa, frekans/gerilim dalgalanmaları görülebilir. 
•	İşletme ve finansal zarar: Yanlış faturalama, enerji alım/satım hataları, kullanıcı güven kaybı.
________________________________________

## 5. Anomali Tespiti — Teknik Yaklaşımlar
Aşağıdaki yöntemler “hayalet yük” durumunu tespit etmekte kullanılabilir:
1.	Çapraz-kontrol (cross-validation) Telemetri: Fiziksel enerji ölçümü (trafo/trafo-havuzu düzeyinde gerçek akım/gerilim) ile istasyon raporlarını karşılaştır. Tutarsızlık varsa uyarı. (örn. trafo akımı artmıyor ama istasyonlar birlikte şarj gösteriyorsa.) 
2.	Zaman-serisi Anomali Algoritmaları: LSTM autoencoder, Isolation Forest, change-point detection ile oturum başlatma/bitirme desenlerindeki anormallikler yakalanır. Özellikle eş zamanlı yüksek sayıda oturum başlangıcı bir sinyaldir. 
3.	Topolojik / Grid-aware ML: Şebeke topolojisini kullanan modeller (graph-based) ile hangi istasyonların bir trafo bölgesini etkilediği bilinerek uç noktadan gelen yük raporları doğrulanır. 
4.	Federated / Distributed Detection: Gizliliği koruyarak farklı CPO’lar/DSO’lar arası modeller paylaşımıyla geniş kapsamlı anomaliler tespit edilebilir. 
________________________________________

## 6. Önleme ve Azaltma (Mitigasyon) Önerileri
•	Sertifika tabanlı mutual TLS ve güçlü kimlik doğrulama: Tüm EVSE ↔ CPO ve CPO ↔ Aggregator kanalları şifrelenmiş ve sertifika ile doğrulanmalı. 
•	Komut/oturum doğrulama katmanı: Start/stop gibi kritik komutlar için oturum doğrulama, rate-limit ve insan onayı/çok faktörlü unsur (özellikle toplu/aynı anda gelen komutlarda) uygulanmalı.
•	Trafo/borough-level cross-checking: İstasyon raporları ile trafo ölçümleri anlık olarak eşleştirilmeli; büyük sapma halinde otomatik karantinaya alma. 
•	Güvenli firmware & update süreçleri: EVSE yazılımı güncellemeleri imzalanmalı, cihaz bütünlüğü periyodik olarak doğrulanmalı. 
•	Olay simülasyonu & tabletop tatbikatları: Olası “hayalet” senaryoları DSO–CPO ortak tatbikatlarıyla test edilmeli. NIST/ulusal rehberlere göre risk profili güncellenmeli.
________________________________________

## 7. Deneysel/Öğretici Aktivite Önerisi (ders için iyi gösterge)
Eğer dersin kapsamında uygulama yapmak istersen, önerebileceğim kısa proje:
1.	Basit bir simülasyon ortamı kur: birkaç trafo bölgesi, 100 istasyon, tek bir aggregator.
2.	Normal çalışma verisi üret (rastgele ama fiziksel tutarlı akım/enerji).
3.	Saldırı: belli bir zaman aralığında 50–200 istasyondan sahte 'start' oturumu gönder.
4.	Uygula: Isolation Forest ve bir trafo-ile-istemci cross-check kuralı ile anomali tespiti.
(Ben sana bu kod iskeletini hazır şekilde yazabilirim — Python + pandas + scikit-learn ile.)

