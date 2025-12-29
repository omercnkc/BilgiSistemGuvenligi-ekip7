# Sözde Kod (Pseudocode) - Doğrusal Eşliksel Üreteç (LCG)

Bu algoritma, matematiksel bir formül kullanarak rastgeleymiş gibi görünen bir sayı dizisi (Sözde Rastgele Sayılar) üretir.

## Algoritma Mantığı

1.  **BAŞLAT (INIT):**
    *   Sisteme bir başlangıç değeri (**Seed**) ver.
    *   Eğer **Seed** verilmediyse, şimdiki zamanı **Seed** olarak ayarla.
    *   Sabitleri Yükle:
        *   **m** (Modül) = 2^31 (veya büyük bir asal sayı)
        *   **a** (Çarpan) = 1103515245
        *   **c** (Artış) = 12345
        *   **Durum** (State) = Seed

2.  **FONKSİYON NEXT (Sonraki Sayıyı Üret):**
    *   Geçerli **Durum** değerini al.
    *   Yeni **Durum** değerini hesapla:
        *   `Yeni_Durum = (a * Eski_Durum + c) MOD m`
    *   **Durum** değişkenini güncelle (`Durum = Yeni_Durum`).
    *   **Durum** değerini DÖNDÜR.

3.  **FONKSİYON RANGE (Aralıklı Sayı Üret - min, max):**
    *   `Ham_Sayi` = **NEXT()** fonksiyonunu çağır.
    *   Belirli aralığa sığdır:
        *   `Sonuc = min + (Ham_Sayi MOD (max - min + 1))`
    *   `Sonuc` değerini DÖNDÜR.

4.  **PROGRAM AKIŞI:**
    *   Algoritmayı başlat (INIT).
    *   Döngü içinde istenilen kadar **RANGE** veya **NEXT** fonksiyonunu çağır.
    *   Sonuçları ekrana yazdır.
    *   BİTİR.
