# 🔋 Elektrikli Araç Şarj Güvenliği - Anomali Tespiti Projesi

<div align="center">

![OCPP](https://img.shields.io/badge/OCPP-2.0.1-blue?style=for-the-badge)
![Security](https://img.shields.io/badge/Security-Critical-red?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/ML-Anomaly%20Detection-green?style=for-the-badge)

**OCPP Protokolünde PKI/İmza Doğrulama Eksikliği Kaynaklı Firmware Manipülasyonu Anomalisi**

[📋 Hakkımda](#-hakkımda) • [🔍 Anomali Senaryosu](#-anomali-senaryosu) • [📊 SWOT Analizi](#-swot-analizi) • [📚 Kaynaklar](#-kaynaklar)

</div>

---

## 📖 Proje Hakkında

Bu proje, **Elektrikli Araç Şarj İstasyonları (EVSE)** ve **Merkezi Şarj Yönetim Sistemleri (CSMS)** arasındaki iletişim protokolü olan **OCPP (Open Charge Point Protocol)** üzerindeki güvenlik açıklarını ve anomali tespit mekanizmalarını incelemektedir.

### 🎯 Proje Kapsamı

- ✅ OCPP 2.0/2.0.1 güvenlik mekanizmalarının analizi
- ✅ PKI/İmza doğrulama zafiyetlerinin tespiti
- ✅ Firmware manipülasyonu anomali senaryosu
- ✅ Machine Learning tabanlı anomali tespiti yaklaşımları
- ✅ Mobil uygulama güvenliği değerlendirmesi

---

## 🛠️ Teknoloji Yığını

| Kategori | Teknolojiler |
|----------|-------------|
| **Programlama Dilleri** | Kotlin, Python |
| **Mobil Geliştirme** | Android (Kotlin) |
| **Machine Learning** | TensorFlow, Scikit-learn, Anomaly Detection |
| **Güvenlik** | PKI, TLS, TPM, HSM, Blockchain |
| **Protokoller** | OCPP 2.0.1, ISO 15118 |

---

## 📁 Proje Yapısı

```
Samet_BSG/
│
├── README.md                 # Bu dosya
├── Hakkımda.md              # Yetkinlikler ve deneyimler
├── Anomali_Senaryosu.md     # Detaylı anomali senaryosu
└── SWOT.md                  # OCPP güvenliği SWOT analizi
```

---

## 🔍 Anomali Senaryosu

### Senaryo Başlığı
**Zayıf PKI/İmza Doğrulama Eksikliği Kaynaklı Firmware Manipülasyonu Anomalisi**

### Özet
Bu senaryoda saldırgan, şarj istasyonunun PKI/doğrulama mekanizmasındaki imza, nonce ve zaman damgası kontrollerinin zayıf olmasını kullanarak firmware tarafına kötü amaçlı kod enjekte edebilir.

### ⚠️ Riskler
- 🔴 Anormal komut işleme
- 🔴 Sahte ölçüm raporlama
- 🔴 Yanlış yönlendirilmiş enerji akışı
- 🔴 Yetkisiz komut işleme

> 📄 **Detaylı bilgi için:** [Anomali_Senaryosu.md](./Anomali_Senaryosu.md)

---

## 📊 SWOT Analizi

### 💪 Güçlü Yönler
- ✅ Cross-vendor çalışabilirlik
- ✅ TLS desteği ve güvenlik fonksiyonları
- ✅ Diğer standartlarla entegrasyon

### ⚠️ Zayıf Yönler
- ❌ Güvenlik uygulamalarında tutarsızlık
- ❌ TLS tek başına yetersiz
- ❌ Fiziksel uç nokta riskleri

### 🚀 Fırsatlar
- 🔹 PKI / donanım tabanlı güvenlik (TPM, HSM, PUF)
- 🔹 Blockchain & akıllı sözleşmeler
- 🔹 AI tabanlı anomali tespiti

### 🛡️ Tehditler
- ⚠️ MitM, replay, DoS/DDoS saldırıları
- ⚠️ Donanım/firmware manipülasyonu
- ⚠️ Gizlilik ve faturalama riskleri

> 📄 **Detaylı analiz için:** [SWOT.md](./SWOT.md)

---

## 🎓 Hakkımda

### Yetkinlikler
- 🤖 **Machine Learning**: Anomali tespiti, derin öğrenme, model eğitimi
- 📱 **Mobil Uygulama Geliştirme**: Android (Kotlin), modern UI/UX tasarımı
- 🔐 **Güvenlik**: Siber güvenlik, protokol analizi, zafiyet tespiti

### İlgi Alanları
- Elektrikli araç şarj altyapısı güvenliği
- OCPP protokol analizi ve güvenlik açıkları
- Machine Learning tabanlı anomali tespiti
- Mobil uygulama güvenliği

> 📄 **Daha fazla bilgi için:** [Hakkımda.md](./Hakkımda.md)

---

## 📚 Kaynaklar

### Akademik Kaynak
**Garofalaki, Z., Kosmanos, D., Moschoyiannis, S., Kallergis, D., & Douligeris, C. (2022).**  
*Electric Vehicle Charging: A Survey on the Security Issues and Challenges of the Open Charge Point Protocol (OCPP).*  
**IEEE.**

### İlgili Standartlar
- 📘 OCPP 2.0.1 Specification
- 📘 ISO 15118 (Vehicle-to-Grid Communication)
- 📘 IEC 61851 (EV Conductive Charging System)

---

## 📈 Proje İlerlemesi

- [x] Proje klasörü oluşturuldu
- [x] README.md hazırlandı
- [x] Hakkımda.md oluşturuldu
- [x] Anomali senaryosu dokümante edildi
- [x] SWOT analizi tamamlandı
- [ ] Simülasyon ortamı kurulumu
- [ ] Anomali tespit modeli geliştirme
- [ ] Test ve doğrulama

---

## 🤝 Katkıda Bulunma

Bu proje, **Bilgi Sistemleri Güvenliği** dersi kapsamında geliştirilmiştir. Sorularınız veya önerileriniz için iletişime geçebilirsiniz.

---

<div align="center">

**⚡ Güvenli Şarj, Güvenli Gelecek ⚡**

Made with ❤️ for Electric Vehicle Security

</div>

