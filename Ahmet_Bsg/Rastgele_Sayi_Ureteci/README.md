# Rastgele Sayı Üreteci (Random Number Generator) Projesi

Bu proje, Bilgi Sistemleri Güvenliği dersi kapsamında geliştirilmiş bir **Doğrusal Eşliksel Üreteç (Linear Congruential Generator - LCG)** uygulamasıdır. Algoritma, belirlenen matematiksel formüller kullanarak sözde rastgele sayılar (PRNG) üretir.

## 📂 Proje İçeriği

Bu dizinde aşağıdaki dosyalar bulunmaktadır:

1.  **[rng_generator.py](rng_generator.py):** Algoritmanın Python dilinde yazılmış kaynak kodu.
2.  **[pseudocode.md](pseudocode.md):** Algoritmanın çalışma mantığını anlatan sözde kod (pseudocode).
3.  **[flowchart.mermaid](flowchart.mermaid):** Algoritmanın görsel akış şeması.
4.  **[ornek_ciktilar.txt](ornek_ciktilar.txt):** Program çalıştırıldığında üretilen örnek çıktı dosyası.

## 🚀 Nasıl Çalıştırılır?

Bilgisayarınızda Python yüklü ise terminalden aşağıdaki komutu çalıştırabilirsiniz:

```bash
python rng_generator.py
```

## ⚙️ Algoritma Detayları (LCG)

Kullanılan algoritma **Linear Congruential Generator (LCG)** olarak adlandırılır ve şu formüle dayanır:

$$X_{n+1} = (a \cdot X_n + c) \mod m$$

Burada:
*   **$X$**: Rastgele sayı dizisi
*   **$m$**: Modül (2^31 - POSIX standardı)
*   **$a$**: Çarpan (1103515245)
*   **$c$**: Artış miktarı (12345)
*   **$X_0$**: Başlangıç tohumu (Seed) - *Sistem saati kullanılarak otomatik belirlenir.*

## 📝 Ekip / Geliştirici
*   **Ahmet_Bsg** (Bilgi Sistemleri Güvenliği Ekibi)
