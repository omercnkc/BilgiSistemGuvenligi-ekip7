# 💰 Enerji Hırsızlığı Anomalisi - Test Raporu

**Tarih:** 30 Aralık 2024  
**Test Eden:** Samet YEŞİLOT  
**Senaryo ID:** `samet-energy-theft`  
**Kategori:** Data Integrity / Parameter Tampering  
**Şiddet:** 🔴 YÜKSEK

---

## 📋 Executive Summary

Bu rapor, EVCS Anomaly Platform üzerinde gerçekleştirilen **Enerji Hırsızlığı (Energy Theft)** anomali testinin sonuçlarını içermektedir. Test, OCPP protokolünde sayaç değerlerinin client-side'dan manipüle edilebilmesinden kaynaklanan güvenlik zayıflığını göstermektedir.

### ✅ Test Başarı Durumu
- ✅ Anomali başarıyla başlatıldı
- ✅ Platform üzerinde kayıt edildi  
- ✅ Simülasyon tamamlandı
- ✅ Sonuçlar görüntülenebildi

---

## 🎯 Test Hedefi

**Senaryo:** Elektrikli araç şarj istasyonlarında enerji tüketim değerlerinin manipüle edilerek, gerçek tüketimden çok daha düşük miktarda fatura ödenmesi.

**Zayıflık:** Backend sistemi, şarj istasyonundan gelen enerji tüketim ve fiyat değerlerini doğrulamadan kabul ediyor.

**Saldırı Yöntemi:** MeterValues mesajlarındaki `energy_kwh` ve `price` parametrelerinin düşük değerlerle gönderilmesi.

---

## 🔬 Test Detayları

### Test Ortamı
- **Backend URL:** https://evcs-backend-samet.onrender.com
- **Frontend URL:** https://simulasyon.vercel.app/
- **API Key:** `gizli-sifreniz-123`
- **Test Aracı:** Python SDK (`evcs_attack.py`)

### Test Parametreleri

| Parametre | Değer | Açıklama |
|-----------|-------|----------|
| **Senaryo ID** | `samet-energy-theft` | Enerji hırsızlığı senaryosu |
| **Duration** | 90 saniye | Simülasyon süresi |
| **Intensity** | 9/10 | Saldırı yoğunluğu |
| **theft_percentage** | %99.0 | Çalınan enerji yüzdesi |

### Gerçek vs Manipüle Edilmiş Değerler

| Metrik | Gerçek Değer | Bildirilen Değer | Fark |
|--------|--------------|------------------|------|
| **Enerji Tüketimi** | 100 kWh | 1 kWh | 99 kWh çalındı |
| **Birim Fiyat** | 5.0 TL/kWh | 5.0 TL/kWh | - |
| **Toplam Maliyet** | 500 TL | 5 TL | 495 TL tasarruf |
| **Tasarruf Oranı** | - | - | %99.0 |

---

## 🚀 Test Süreci

### 1. Bağlantı Kurulumu
```
[*] Initialized Attack Client targeting: https://evcs-backend-samet.onrender.com
📡 Bağlantı kontrol ediliyor...
[+] Connection Successful!
✅ Backend'e başarıyla bağlanıldı!
```

### 2. Anomali Başlatma
```python
client.start_attack(
    scenario_id="samet-energy-theft",
    duration=90,
    intensity=9,
    params={"theft_percentage": 99.0}
)
```

### 3. Test Sonuçları

**Run ID:** `c36175c3-6768-472c-9d63-bde35e931108`

**Platform URL:**  
https://simulasyon.vercel.app/runs/c36175c3-6768-472c-9d63-bde35e931108

**Gerçekleştirilen Testler:**

#### Test 1: Normal Kullanıcı (Dürüst)
```bash
Enerji: 100.0 kWh
Fiyat: 5.0 TL/kWh
Toplam Ödeme: 500.0 TL
```

#### Test 2: Enerji Hırsızlığı (Düşük Enerji Bildirimi)
```bash
Bildirilen Enerji: 1.0 kWh
Gerçek Tüketim: 100 kWh
Ödenen: 5.0 TL (Normal: 500 TL)
🚨 Çalınan Enerji: 99.0 kWh
💰 Kazanç: 495.00 TL

✅✅✅ BAŞARILI! 99.0 kWh ENERJİ ÇALDINIZ! ✅✅✅
```

#### Test 3: Fiyat Manipülasyonu
```bash
Enerji: 100.0 kWh
Bildirilen Fiyat: 0.01 TL/kWh
Gerçek Fiyat: 5.0 TL/kWh
Ödenen: 1.0 TL (Normal: 500 TL)
📊 Tasarruf: %99.8

✅ BAŞARILI! Neredeyse bedava şarj!
```

#### Test 4: Tamamen Bedava Şarj
```bash
Gerçek Tüketim: 100 kWh
Bildirilen: 0.1 kWh
Bildirilen Fiyat: 0.01 TL/kWh
Ödenen: 0.001 TL
🚨 Çalınan Enerji: 99.9 kWh
💰 Çalınan Para: ~500.00 TL

🎉🎉🎉 MÜKEMMELİŞTE BEDAVA ŞARJ! 🎉🎉🎉
```

---

## 📊 Sonuç Analizi

### Başarı Kriterleri

| Kontrol | Beklenen Değer | Gerçekleşen | Sonuç |
|---------|---------------|-------------|-------|
| `energy_stolen` | > 50 kWh | 99.0 kWh | ✅ |
| `total_cost` | < 50 TL | 5.0 TL | ✅ |
| Tasarruf Oranı | > %80 | %99.0 | ✅ |
| Logs'ta WARNING | Var | Var | ✅ |
| Vulnerability Field \| Var | Var | ✅ |

**Sonuç:** 5/5 kriterin tamamı başarıyla geçildi. **✅ SİSTEM BAŞARIYLA HACKLENDİ!**

### Güvenlik Açığının Etki Değerlendirmesi

#### 📈 Potansiyel Zararlar

**Tek Kullanıcı Bazında:**
- Aylık 30 şarj × 495 TL = **14,850 TL/ay** kayıp
- Yıllık: **178,200 TL** kayıp

**Sistem Bazında (1000 kullanıcı):**
- Aylık: **14,850,000 TL** kayıp
- Yıllık: **178,200,000 TL** kayıp

#### ⚠️ Diğer Riskler
- 🔴 Elektrik dağıtım şirketleri arası güven kaybı
- 🔴 Sistem itibarının zarar görmesi
- 🔴 Yasal yükümlülüklerin ihlali
- 🔴 Enerji arz-talep dengesinin bozulması

---

## 🛡️ Önerilen Güvenlik Önlemleri

### 1. Server-Side Sayaç Okuması
```python
# ✅ DOĞRU YAKLAŞIM
actual_energy = read_from_physical_meter(charger_id)
server_price = get_current_tariff()

# Client'tan gelen değerler ignore edilir
total_cost = actual_energy * server_price
```

### 2. Dijital İmza Doğrulaması
```python
# Blockchain tabanlı imzalama
signature = sign_data(energy_kwh, private_key)

# Backend doğrulaması
if not verify_signature(signature, public_key):
    raise SecurityException("Tampered data detected!")
```

### 3. Anomali Tespiti
```python
# Fiziksel sayaç ile bildirilen değer karşılaştırması
if abs(reported_kwh - physical_kwh) > THRESHOLD:
    trigger_alert("Energy theft suspected")
    log_security_incident(session_id)
```

### 4. Rate Limiting ve Monitoring
- Aynı kullanıcıdan art arda düşük değer bildirimi engellenmeli
- Anormal pattern'ler ML ile tespit edilmeli
- Real-time alerting sistemi kurulmalı

---

## 🔍 Zayıflığın Kök Nedeni

**Dosya:** `backend/app/api/routes_vulnerable.py`  
**Satırlar:** 79-114

```python
# ❌ KORKUNÇ HATA!
@router.post("/meter-reading")
def submit_meter_reading(session_id: str, energy_kwh: float, price: float):
    # Kullanıcının gönderdiği değerler kullanılıyor!
    total_cost = energy_kwh * price  # ← İŞTE SORUN!
    
    return {
        "total_cost": total_cost,  # Kullanıcının dediği fiyat!
        "energy_stolen": actual_energy - energy_kwh
    }
```

**Hata Türleri:**
1. ❌ Client-controlled fiyatlandırma
2. ❌ Fiziksel sayaç doğrulaması yok
3. ❌ İmza/signature kontrolü yok
4. ❌ Anomali tespit mekanizması yok
5. ❌ Input validation yok

---

## 💡 Öğrenilen Dersler

### ✅ Yapılması Gerekenler
1. **Hiçbir zaman client'a güvenmeyin** - "Never trust the client"
2. **Kritik değerleri sunucu tarafında hesaplayın**
3. **Blockchain/PKI ile verileri imzalayın**
4. **Fiziksel sayaçları kullanın**
5. **Anomali tespit sistemi kurun**

### ❌ Yapılmaması Gerekenler
1. Fiyatlandırmayı client'a bırakmayın
2. Enerji değerlerini doğrulamadan kabul etmeyin
3. Güvenlik kontrollerini atlayıp sadece performansa odaklanmayın

---

## 📸 Ekran Görüntüleri

> **Not:** Ekran görüntüleri manuel olarak eklenecektir.

### Beklenen Ekran Görüntüleri:
1. ✅ Platform ana sayfası (https://simulasyon.vercel.app/)
2. ✅ Anomali başlatma ekranı
3. ✅ Real-time log akışı
4. ✅ Metrik grafikleri (energy_stolen göstergeleri)
5. ✅ Uyarı mesajları ve güvenlik ihlali bildirimleri
6. ✅ Test script çıktıları

### Kullanıcı Web Sitesinde Görmesi Gerekenler:

**URL:** https://simulasyon.vercel.app/runs/c36175c3-6768-472c-9d63-bde35e931108

**Beklenen Çıktılar:**
- [ ] Run ID:  `c36175c3-6768-472c-9d63-bde35e931108`
- [ ] Status: COMPLETED
- [ ] Senaryo: Samet BSG - Energy Theft
- [ ] Logs: Heartbeat, MeterValues mesajları
- [ ] Metrics: `theft_percentage` > 0 grafiği
- [ ] Warnings: "Metervals < Physical Consumption"
- [ ] Errors: "Signature Failures"

---

## 🎓 Eğitimsel Değer

Bu anomali testi, aşağıdaki güvenlik konseptlerini pratik olarak göstermektedir:

1. **Parameter Tampering**: Client-side veri manipülasyonu
2. **Business Logic Flaws**: Uygulama mantığındaki hatalar
3. **Trust Boundary Violations**: Güven sınırlarının ihlali
4. **Input Validation Failures**: Girdi doğrulama eksiklikleri

**UYARI:** Bu test senaryosu SADECE EĞİTİM AMAÇLIDIR. Gerçek sistemlerde bu tür testler YASAKTIR ve SUÇtur!

---

## 📚 Referanslar

### Kullanılan Kaynaklar
1. **EVCS Anomaly Platform:** https://github.com/sametyesilot/simulasyon
2. **Backend Vulnerable Endpoints:** `/vulnerable/meter-reading`
3. **OCPP 2.0.1 Specification:** Security Profile 3
4. **OWASP Top 10:** Injection ve Broken Authentication

### İlgili Dökümanlar
- [Samet_BSG_samet-energy-theft.md](/Users/samet/Desktop/bsg/simulasyon-repo/gorevler/Samet_BSG_samet-energy-theft.md)
- [routes_vulnerable.py](/Users/samet/Desktop/bsg/simulasyon-repo/backend/app/api/routes_vulnerable.py)

---

## ✅ Sonuç

Enerji hırsızlığı anomalisi başarıyla tespit edildi ve simülasyonu gerçekleştirildi. Test sonuçları, client-side price control ve sayaç değeri manipülasyonunun kritik bir güvenlik açığı olduğunu açıkça göstermektedir.

**Sistem Durumu:** 🔴 **ZAFİYETLİ**  
**Önerilen Aksiyon:** Acil güvenlik yamalarının uygulanması

---

**Hazırlayan:** Samet YEŞİLOT  
**Tarih:** 30 Aralık 2024  
**Versiyon:** 1.0  
**Durum:** ✅ TEST BAŞARIYLA TAMAMLANDI

---

<div align="center">

⚠️ **Bu rapor eğitim amaçlıdır. Gerçek sistemlerde izinsiz test yapmayın!** ⚠️

Made with 🔒 for Cyber Security Education

</div>
