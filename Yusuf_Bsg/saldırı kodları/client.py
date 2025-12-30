import hmac, hashlib, json, time
import requests

SECRET_KEY = "dev-secret-change-me"
URL = "http://127.0.0.1:8000/ocpp-message"
# sende /api/ocpp-message ise:
# URL = "http://127.0.0.1:8000/api/ocpp-message"

def canonical_json(obj) -> bytes:
    return json.dumps(obj, separators=(",", ":"), sort_keys=True).encode("utf-8")

def sign(message: dict) -> str:
    return hmac.new(SECRET_KEY.encode("utf-8"), canonical_json(message), hashlib.sha256).hexdigest()

payload = {
    "message": {
        "action": "Heartbeat",
        "timestamp": time.time()
    }
}

# 1) Doğru imza -> 200 beklenir
sig_ok = sign(payload["message"])
r1 = requests.post(URL, json=payload, headers={"X-Signature": sig_ok})

# 2) Yanlış imza -> 401 beklenir
r2 = requests.post(URL, json=payload, headers={"X-Signature": "WRONG"})

# 3) İmzasız -> 401 beklenir
r3 = requests.post(URL, json=payload)

def print_result(name, resp):
    if resp.status_code == 200:
        print(f"{name}: TEST BAŞARILI ✅ (kabul edildi)")
    elif resp.status_code == 401:
        print(f"{name}: TEST BAŞARISIZ ❌ (401 imza yok/yanlış)")
    else:
        print(f"{name}: BEKLENMEYEN ⚠️", resp.status_code, resp.text)

print_result("DOĞRU İMZA", r1)
print_result("YANLIŞ İMZA", r2)
print_result("İMZASIZ", r3)

