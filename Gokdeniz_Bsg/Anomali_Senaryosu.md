# Rapor: Elektrikli Araç Şarj Anomali Senaryosu

**Anomali:** Mobil uygulama API'lerindeki zayıf yetkilendirme kontrolleri ve sunucu tarafı kontrollerinin zayıflığı.

---

### Senaryo Başlığı: Mobil Uygulama API Zafiyeti Yoluyla Hesap Ele Geçirme ve "İmkansız Seyahat" (Impossible Travel) Anomalisi

### Özet

Bu senaryoda saldırgan, bir EV kullanıcısının mobil uygulama hesabını (örn. oltalama veya API brute-force ile) ele geçirir. Ekosistemin bulut altyapısı (CSMS), API üzerinden gelen `StartTransaction` (Şarjı Başlat) komutlarını yeterince doğrulamamaktadır. Saldırgan, ele geçirdiği hesapla, kullanıcının normal konumundan coğrafi olarak çok uzak bir istasyonda şarj işlemi istedi. Bu durum, hesabın çalındığını ve enerji hırsızlığı yapıldığını gösteren belirgin bir "imkansız seyahat" anomalisi oluşturur.

---

### 1. Başlangıç

Kullanıcı (UserID: 'ahmet123') normalde İstanbul'daki ev ve ofis istasyonlarını kullanmaktadır. Hesabı, mobil uygulamasıyla tam senkronizedir.

### 2. Anomali Oluşumu

Saldırgan, 'ahmet123' hesabını ele geçirir. Saldırgan, Ankara'daki halka açık bir istasyona aracını bağlar ve 'ahmet123' hesabını kullanarak mobil API üzerinden `StartTransaction` komutu gönderir. CSMS, sadece 'ahmet123' hesabının geçerli bir oturuma (session token) sahip olup olmadığına bakar, ancak bu isteğin coğrafi konumunu (IP adresi, istasyon konumu) kullanıcının profiliyle karşılaştırmaz.

### 3. Algılama Mantığı

* `StartTransaction` talebi, hesabın bilinen/geçmiş konum profili (geo-profiling) ile uyuşuyor mu?
* Aynı hesaptan 1 saat içinde coğrafi olarak imkansız iki farklı konumdan (örn. 10:00'da İstanbul'dan, 10:15'te Ankara'dan) istek geliyor mu? (İmkansız Seyahat Tespiti)
* API isteğinin geldiği IP adresi, istasyonun coğrafi konumuyla tutarlı mı?
* İşlem, kullanıcının "ev istasyonu" olarak işaretlediği bir istasyon dışında, sık kullanılmayan ve coğrafi olarak uzak bir istasyonda mı başlatıldı?

### 4. Karar ve Tepki

Coğrafi anomali veya İmkansız Seyahat tespiti halinde `StartTransaction` talebi reddedilir. Hesap geçici olarak dondurulur. Kullanıcıya kayıtlı e-posta/telefon üzerinden "Hesabınızla şüpheli bir konumdan şarj işlemi başlatılmaya çalışıldı" uyarısı gönderilir ve parola sıfırlaması istenir. Olay, "Account Takeover / Impossible Travel" olarak loglanır.

### 5. Kaynaklar

[^1]: Antoun, J., Kabir, M.E., Moussa, B., Atallah, R., Assi, C. (2020). A detailed security assessment of the EV charging ecosystem. *IEEE Network*.
