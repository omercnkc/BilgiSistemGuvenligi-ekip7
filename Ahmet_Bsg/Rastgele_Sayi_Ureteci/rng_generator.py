import time

class LinearCongruentialGenerator:
    """
    Basit bir Lineer Doğrusal Üreteç (Linear Congruential Generator - LCG) sınıfı.
    Formül: X_{n+1} = (a * X_n + c) mod m
    """
    def __init__(self, seed=None):
        """
        Üreteci başlatır.
        Eğer tohum (seed) verilmezse, o anki zamanı kullanır.
        """
        if seed is None:
            # Şimdiki zamanı saniye cinsinden alıp tam sayıya çeviriyoruz
            self.state = int(time.time())
        else:
            self.state = seed
        
        # LCG Sabitleri (Yaygın kullanılan ANSI C standartları)
        # m: Modül (modulus) - 2^31
        self.m = 2**31 
        # a: Çarpan (multiplier)
        self.a = 1103515245
        # c: Artış miktarı (increment)
        self.c = 12345

    def next(self):
        """
        Bir sonraki ham rastgele sayıyı üretir.
        """
        self.state = (self.a * self.state + self.c) % self.m
        return self.state

    def range(self, min_val, max_val):
        """
        Belirtilen aralıkta (min_val ve max_val dahil) rastgele bir sayı üretir.
        """
        raw_random = self.next()
        # Ölçekleme işlemi: min + (raw % (max - min + 1))
        return min_val + (raw_random % (max_val - min_val + 1))

# Örnek Kullanım ve Test
if __name__ == "__main__":
    print("=== Rastgele Sayı Üreteci (LCG) Başlatılıyor ===")
    
    # Üreteci oluştur
    rng = LinearCongruentialGenerator()
    print(f"Başlangıç Tohumu (Seed): {rng.state}")
    print("-" * 40)
    
    print("1. Ham Sayılar (İlk 5 değer):")
    for i in range(5):
        print(f"   {i+1}. Değer: {rng.next()}")
    
    print("\n2. 0 ile 100 arasında Rastgele Sayılar (10 adet):")
    for i in range(10):
        val = rng.range(0, 100)
        print(f"   {i+1}. Sayı: {val}")

    print("-" * 40)
    print("Test tamamlandı.")
