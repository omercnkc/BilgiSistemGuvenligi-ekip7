def collatz_siradaki_sayi(n):
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

def anahtar_akisi_uret(anahtar_no, uzunluk):
    akıs = []
    mevcut_sayi = anahtar_no
    for _ in range(uzunluk):
        if mevcut_sayi <= 1:
            mevcut_sayi = anahtar_no + _ + 7 
        mevcut_sayi = collatz_siradaki_sayi(mevcut_sayi)
        byte_degeri = mevcut_sayi % 256
        akıs.append(byte_degeri)
    return akıs

def islemi_yap(metin, anahtar_no):
    if isinstance(metin, str):
        metin_byte = metin.encode('utf-8')
    else:
        metin_byte = metin
    
    anahtar_dizisi = anahtar_akisi_uret(anahtar_no, len(metin_byte))
    sonuc = []
    for i in range(len(metin_byte)):
        karisik_karakter = metin_byte[i] ^ anahtar_dizisi[i]
        sonuc.append(karisik_karakter)
    return bytes(sonuc)

mesaj = "Bsg için oluşturulmuş gizli bir mesajdır."
gizli_sayi = 121823795

print(f"Orijinal Mesaj: {mesaj}")

sifreli_hali = islemi_yap(mesaj, gizli_sayi)
print(f"Sifrelenmis Hali (Hex): {sifreli_hali.hex()}")

cozulmus_hali_byte = islemi_yap(sifreli_hali, gizli_sayi)
cozulmus_mesaj = cozulmus_hali_byte.decode('utf-8')

print(f"Geri Cozülen Mesaj: {cozulmus_mesaj}")