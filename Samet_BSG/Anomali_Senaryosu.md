# 🔴 Rapor: Elektrikli Araç Şarj Anomali Senaryosu

## 📋 Anomali Özeti

**Anomali:** OCPP'deki PKI/doğrulama hataları, fiziksel erişimle anahtar/firmware çalımı, zayıf nonce/zamanlama ve imza eksikliği kötü amaçlı yazılım bulaşmasına olanak tanır.

---

## 🎯 Senaryo Başlığı

**Zayıf PKI/İmza Doğrulama Eksikliği Kaynaklı Firmware Manipülasyonu Anomalisi**

---

## 📖 Özet

Bu senaryoda saldırgan, şarj istasyonunun PKI/doğrulama mekanizmasındaki imza, nonce ve zaman damgası kontrollerinin zayıf olmasını kullanarak firmware tarafına kötü amaçlı kod enjekte edebilir. Fiziksel erişim imkanı olan durumlarda anahtar materyalleri çalınabilir, ardından OCPP mesaj işleme katmanının güvenlik doğrulamaları bypass edilerek istasyon davranışı manipüle edilebilir. Bu durum anormal komut işleme, sahte ölçüm raporlama, yanlış yönlendirilmiş enerji akışı ve yetkisiz komut işleme gibi riskler oluşturur.

---

## 🔄 Senaryo Akışı

### 1️⃣ Başlangıç

Şarj istasyonu normal olarak firmware doğrulama, PKI sertifika kontrolü ve imza doğrulama prosedürünü çalıştırır. OCPP oturumu kurulmuştur, cihaz CSMS ile iletişim halindedir.

**Durum:**
- ✅ OCPP oturumu aktif
- ✅ CSMS ile bağlantı kurulu
- ✅ Firmware doğrulama mekanizması çalışıyor
- ✅ PKI sertifika kontrolü aktif

---

### 2️⃣ Anomali Oluşumu

Nonce, timestamp veya imza doğrulama mekanizmasının zayıf olması sebebiyle firmware update paketi veya kritik kontrol mesajı doğrulanmadan kabul edilir. Kötü amaçlı payload cihazda kalıcı hale gelebilir ve sisteme arka kapı açabilir.

**Saldırı Vektörleri:**
- 🔴 **Zayıf Nonce Kontrolü**: Aynı nonce değerlerinin tekrar kullanılması
- 🔴 **Timestamp Doğrulama Eksikliği**: Zaman penceresi kontrolünün yetersizliği
- 🔴 **İmza Doğrulama Hatası**: Dijital imza kontrolünün bypass edilmesi
- 🔴 **Fiziksel Erişim**: USB portları, modemler üzerinden müdahale
- 🔴 **Anahtar Çalımı**: PKI anahtar materyallerinin fiziksel erişimle çalınması

**Sonuçlar:**
- ⚠️ Kötü amaçlı firmware yüklenmesi
- ⚠️ Arka kapı (backdoor) oluşturulması
- ⚠️ Cihaz davranışının manipüle edilmesi

---

### 3️⃣ Algılama Mantığı

Anomali tespiti için aşağıdaki kontroller yapılmalıdır:

#### ✅ Firmware Hash İmzası Kontrolü
```
Firmware hash imzası referans hash ile uyuşuyor mu?
```
- **Beklenen**: Hash değerleri eşleşmeli
- **Anomali**: Hash uyuşmazlığı tespit edilirse şüpheli firmware

#### ✅ Zaman Damgası Kontrolü
```
Zaman damgası normal tolerans penceresinde mi?
```
- **Beklenen**: Update talebi makul zaman aralığında
- **Anomali**: Zaman penceresi dışı update talebi

#### ✅ Replay Saldırısı Tespiti
```
Aynı firmware update isteği farklı zamanlarda tekrarlanıyor mu?
```
- **Beklenen**: Her update talebi benzersiz olmalı
- **Anomali**: Aynı nonce/request tekrarı

#### ✅ Davranış Analizi
```
Cihaz davranışında normal dışı komut üretimi / meterValues anomalisi var mı?
```
- **Beklenen**: Normal komut işleme ve ölçüm raporlama
- **Anomali**: 
  - Anormal komut üretimi
  - Sahte ölçüm değerleri
  - Beklenmedik enerji akışı

---

### 4️⃣ Karar ve Tepki

Anomali tespit edildiğinde aşağıdaki aksiyonlar alınmalıdır:

#### 🛑 Anında Tepkiler
1. **İşlem Reddi**: Firmware update işlemi reddedilir
2. **Güvenli Mod**: Cihaz kendini güvenli moda alır
3. **Bağlantı Kesme**: CSMS ile bağlantı geçici olarak kesilir
4. **Uyarı Loglama**: Olay detaylı şekilde loglanır

#### 📢 Bildirimler
- **CSMS'e Olay Gönderimi**: Event tipi `"Malicious Firmware Attempt"` olarak gönderilir
- **Teknik Ekip Bilgilendirmesi**: Anında uyarı gönderilir
- **Kullanıcı Bildirimi**: İlgili kullanıcılar bilgilendirilir

#### 🔍 İnceleme Süreci
- Log analizi
- Firmware hash karşılaştırması
- Zaman damgası analizi
- Fiziksel güvenlik kontrolü

---

### 5️⃣ Log Örneği

```
2025-11-02T21:41:00.000Z | StationID: ST-512 | 
FirmwareUpdateID: 33-A2 | 
HASH_Match: False | 
TIMESTAMP: OutOfWindow | 
Event: Suspicious firmware update / signature validation failed | 
Severity: CRITICAL | 
Action: Update rejected, device entered safe mode
```

**Log Alanları:**
- `Timestamp`: Olay zamanı
- `StationID`: Şarj istasyonu kimliği
- `FirmwareUpdateID`: Firmware güncelleme kimliği
- `HASH_Match`: Hash doğrulama sonucu
- `TIMESTAMP`: Zaman damgası durumu
- `Event`: Olay açıklaması
- `Severity`: Önem seviyesi
- `Action`: Alınan aksiyon

---

## 🎯 Risk Değerlendirmesi

| Risk | Etki | Olasılık | Öncelik |
|------|------|----------|---------|
| **Firmware Manipülasyonu** | 🔴 Yüksek | 🟡 Orta | ⚠️ Kritik |
| **Arka Kapı Oluşturma** | 🔴 Yüksek | 🟡 Orta | ⚠️ Kritik |
| **Anormal Komut İşleme** | 🟠 Orta | 🟡 Orta | ⚠️ Yüksek |
| **Sahte Ölçüm Raporlama** | 🟠 Orta | 🟡 Orta | ⚠️ Yüksek |
| **Enerji Akışı Manipülasyonu** | 🔴 Yüksek | 🟢 Düşük | ⚠️ Yüksek |

---

## 🛡️ Önleme Mekanizmaları

### 🔐 Güçlü PKI Uygulaması
- TPM/HSM tabanlı anahtar yönetimi
- Düzenli sertifika yenileme
- Güçlü kriptografik algoritmalar

### ⏱️ Zaman Damgası Doğrulama
- NTP senkronizasyonu
- Tolerans penceresi kontrolü
- Replay saldırısı önleme

### 🔒 Fiziksel Güvenlik
- USB portlarının devre dışı bırakılması
- Fiziksel mühürleme
- Güvenlik kameraları

### 🤖 Machine Learning Tespiti
- Anomali tespit modelleri
- Davranış analizi
- Gerçek zamanlı izleme

---

## 📚 Kaynaklar

**Garofalaki, Z., Kosmanos, D., Moschoyiannis, S., Kallergis, D., & Douligeris, C. (2022).**  
*Electric Vehicle Charging: A Survey on the Security Issues and Challenges of the Open Charge Point Protocol (OCPP).*  
**IEEE.**

---

## 🔗 İlgili Dokümanlar

- [SWOT Analizi](./SWOT.md)
- [Hakkımda](./Hakkımda.md)
- [README](./README.md)

---

<div align="center">

**⚠️ Güvenlik Her Zaman Önceliktir ⚠️**

</div>

