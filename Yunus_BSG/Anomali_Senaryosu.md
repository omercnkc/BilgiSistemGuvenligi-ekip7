# Şebekeden Bağımsız Güneş Enerjili EA Şarj İstasyonuna Yönelik Anomali Senaryosu

## 1. Sistem Genel Tanımı

Senaryonun temeli, şebekeden tamamen bağımsız çalışan, güneş enerjisiyle beslenen bir elektrikli araç (EA) şarj istasyonuna dayanmaktadır. Sistem şu ana bileşenlerden oluşur:
- 2 adet 350 kW hızlı şarj istasyonu
- 1 MW güneş enerjisi santrali
- 1 MW / 4 MWh batarya enerji depolama sistemi (BEDS)
- 1 MW boşaltma yükü (dump load)

Enerji Yönetim Sistemi (EYS) ile yerel kontrolörler arasında bir iletişim ağı bulunur. Batarya sistemi, DC bara (DC link) voltajını regüle etmekte; dump load ise fazla enerjiyi tüketerek bataryanın aşırı şarj olmasını engellemektedir.

## 2. Anomali Tanımı

Bu çalışmada ele alınan anomali, şarj istasyonunun iletişim ağlarına ve ölçüm cihazlarına yapılan siber saldırılar sonucunda DC bara voltajının normal sınırlar dışına çıkarılmasıdır.

- **Hedeflenen Güvenlik Özellikleri:**
  - Kullanılabilirlik (availability)
  - Bütünlük (integrity)

- **Saldırı Türleri (Anomali Metrikleri):**
  1. **Kontrol ile İlgili Saldırılar (Control-Related Attacks):**
     - Saldırganın EYS'den gönderilen kontrol komutlarını taklit etmesi.
     - Örnekler:
       - Batarya doluyken dump load'un devre dışı bırakılması.
       - Güneş enerjisi üretimi mevcutken üretimin kesilmesi komutunun verilmesi.

  2. **Ölçümlere Yönelik Saldırılar (Measurement Attacks):**
     - Yanlış Veri Enjeksiyonu (False Data Injection - FDI) ile voltaj ölçümlerinin manipüle edilmesi.
     - Hizmet Reddi (Denial of Service - DoS) saldırıları ile ölçümlerin geciktirilmesi veya tamamen engellenmesi.

Bu saldırılar sonucunda, EYS ve kontrol algoritmaları yanlış kararlar alır, DC bara voltajı dengesiz hale gelir ve sonuçta koruma röleleri istasyonu kapatır.

## 3. Saldırganın Amacı

Saldırganın temel amacı, sistem bileşenleri arasındaki kontrol ve ölçüm trafiğini manipüle ederek:
- Şarj istasyonunun hizmet dışı kalmasına,
- Tüm hızlı şarj ünitelerinin eş zamanlı çökmesine,
- Batarya ve güç elektroniği elemanlarında fiziksel hasar riskinin artmasına
neden olmaktır.

## 4. Muhtemel Saldırı Adımları

1. İletişim ağının keşfi (network reconnaissance)
2. EYS ile yerel kontrolörler arasındaki trafiğin dinlenmesi
3. Kimlik doğrulama zafiyetleri varsa yetkisiz erişim elde edilmesi
4. Sahte kontrol komutlarının gönderilmesi (örneğin, dump load'u kapatmak)
5. Voltaj ve akım ölçümlerine FDI saldırıları ile yanlış değerler enjekte edilmesi
6. Koruma sistemlerinin tetiklenmesi ve istasyonun devre dışı kalması

## 5. Sonuç

Senaryo, şebekeden bağımsız güneş enerjili EA şarj istasyonlarının, hem kontrol komutları hem de ölçüm verileri üzerinden gerçekleştirilen siber saldırılarla ne kadar kritik şekilde etkilenebileceğini göstermektedir. Özellikle uzak bölgelerdeki bu tür istasyonlar için, siber güvenlik önlemlerinin klasik IT sistemlerinden çok daha bütünsel ve fizik-farkındalı bir şekilde ele alınması gerekmektedir.