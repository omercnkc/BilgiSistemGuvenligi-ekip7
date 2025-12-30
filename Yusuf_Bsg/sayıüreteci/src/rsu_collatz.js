function collatzStep(x) {
  // AKIŞ: x çiftse x/2, tekse 3x+1
  if (x % 2 === 0) return x / 2;
  return 3 * x + 1;
}

// küçük bir karıştırma: desenleri biraz azaltmak için (tam kripto değil)
function mix32(x) {
  x |= 0;
  x ^= x << 13;
  x ^= x >>> 17;
  x ^= x << 5;
  return x >>> 0;
}

/**
 * seed -> x başlangıcı -> Collatz döngüsü -> 1..300 arası k
 */
function rsuCollatzOneNumber(seed, steps = 40) {
  // Başlangıç x (seed'den türet)
  let x = (seed % 100000) + 1;

  for (let i = 0; i < steps; i++) {
    // 1) Karar + işlem: (x/2) veya (3x+1)
    x = collatzStep(x);

    // 2) (Tahtada RSÜ yanında "random/istatistik güçlü" vurgusu vardı)
    //    Bu yüzden küçük bir mix ekliyoruz.
    x = mix32(x);

    // x'i pozitif ve kontrol altında tutalım
    x = (x % 100000) + 1;
  }

  // Çıkış: 1..300
  return (x % 300) + 1;
}

// CMD'den opsiyonel seed al:
// npm run rsu -- 12345
const seedArg = process.argv[2];
const seed = seedArg ? Number(seedArg) : Date.now();

const k = rsuCollatzOneNumber(seed);

console.log("=== RSÜ (Collatz Akışı) ===");
console.log("Seed:", seed);
console.log("k (1..300):", k);