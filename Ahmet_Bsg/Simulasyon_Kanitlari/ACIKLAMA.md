# Simülasyon Çıktıları ve Kanıtlar Hakkında

Bu klasör, Elektrikli Araç Şarj İstasyonu (EVCS) simülasyonu üzerinde başarıyla gerçekleştirilen 3 farklı siber saldırı senaryosunun kanıtlarını içermektedir.

Aşağıda her bir saldırı senaryosu ve ilgili dosyalar hakkında detaylı bilgi verilmiştir:

## 1. Zaman Manipülasyonu (Time Travel / Timestamp Spoofing)
*   **İlgili Dosyalar:** `attack_time_travel.log`, `screenshot_time_travel.png`
*   **Açıklama:** Bu senaryoda, simülasyonun blok zinciri katmanına kasıtlı olarak geçmiş tarihli (1 saat öncesine ait) bir işlem gönderilmiştir. Sistemin zaman damgası doğrulamasını (timestamp validation) yapmadığı ve bu sahte işlemi geçerli kabul ettiği kanıtlanmıştır.

## 2. Konsensüs Saldırısı (Consensus / Clock Drift Attack)
*   **İlgili Dosyalar:** `attack_consensus.log`, `screenshot_consensus.png`
*   **Açıklama:** Ağdaki düğümlerin (nodes) zaman senkronizasyonunu bozmak amacıyla, rastgele gelecek ve geçmiş zaman damgalarına sahip çok sayıda paket gönderilmiştir. Bu saldırı, ağın tutarlılığını bozmayı ve "block confirmation" sürelerini uzatmayı hedeflemiştir.

## 3. Yazılım Sürüm Düşürme (Firmware Downgrade Attack)
*   **İlgili Dosyalar:** `attack_firmware_downgrade.log`, `screenshot_firmware_downgrade.png`
*   **Açıklama:** Sistemin güncellemeleri doğrulama mekanizması test edilmiştir. Çok eski tarihlere (30 gün önce) ayarlanmış sahte bir zaman damgası kullanılarak, "v1.0.0-VULNERABLE" ismindeki eski ve güvensiz bir yazılım sürümü, sisteme geçerli bir güncelleme gibi kabul ettirilmiştir. Bu, sistemin eski ve savunmasız bir sürüme geri döndürülebileceğini (downgrade) göstermektedir.
