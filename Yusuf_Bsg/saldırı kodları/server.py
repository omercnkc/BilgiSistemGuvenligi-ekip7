# server.py
import hmac, hashlib, json
from fastapi import FastAPI, Header, HTTPException, Request

app = FastAPI()

SECRET_KEY = "dev-secret-change-me"

def canonical_json(obj) -> bytes:
    # İmza için JSON'u deterministik hale getir
    return json.dumps(obj, separators=(",", ":"), sort_keys=True).encode("utf-8")

def expected_sig(message: dict) -> str:
    return hmac.new(
        SECRET_KEY.encode("utf-8"),
        canonical_json(message),
        hashlib.sha256
    ).hexdigest()

@app.post("/ocpp-message")
async def ocpp_message_handler(request: Request, x_signature: str = Header(default="")):
    payload = await request.json()
    message = payload.get("message", payload)  # istersen {"message": {...}} formatı
    if not x_signature:
        raise HTTPException(status_code=401, detail="Missing signature")

    exp = expected_sig(message)
    if not hmac.compare_digest(exp, x_signature):
        raise HTTPException(status_code=401, detail="Invalid signature")

    return {"status": "accepted", "message_processed": message}
