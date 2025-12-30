import os, time, json, hmac, hashlib
from typing import Any, Dict
from fastapi import APIRouter, Header, HTTPException

router = APIRouter()

OCPP_HMAC_SECRET = os.getenv("OCPP_HMAC_SECRET", "")
ALLOWED_SKEW_SECONDS = int(os.getenv("OCPP_ALLOWED_SKEW_SECONDS", "120"))

_seen_nonces: Dict[str, float] = {}

def _cleanup_nonces(now: float):
    ttl = 600  # 10 dk
    for k, t in list(_seen_nonces.items()):
        if now - t > ttl:
            _seen_nonces.pop(k, None)

def canonical_json(obj: Any) -> bytes:
    return json.dumps(obj, separators=(",", ":"), sort_keys=True, ensure_ascii=False).encode("utf-8")

def verify_replay(x_timestamp: str, x_nonce: str):
    try:
        ts = int(x_timestamp)
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid X-Timestamp")

    now = int(time.time())
    if abs(now - ts) > ALLOWED_SKEW_SECONDS:
        raise HTTPException(status_code=401, detail="Timestamp outside allowed window")

    if not x_nonce or len(x_nonce) < 8:
        raise HTTPException(status_code=400, detail="Invalid X-Nonce")

    _cleanup_nonces(now)
    if x_nonce in _seen_nonces:
        raise HTTPException(status_code=409, detail="Replay detected (nonce reused)")
    _seen_nonces[x_nonce] = float(now)

def verify_hmac(payload: Any, signature_hex: str):
    if not OCPP_HMAC_SECRET:
        raise HTTPException(status_code=500, detail="OCPP_HMAC_SECRET missing")

    expected = hmac.new(
        OCPP_HMAC_SECRET.encode("utf-8"),
        canonical_json(payload),
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(expected, (signature_hex or "").strip()):
        raise HTTPException(status_code=401, detail="Invalid signature")

@router.post("/ocpp-message")
def ocpp_message_handler(
    payload: dict,
    x_signature: str = Header(default="", alias="X-Signature"),
    x_timestamp: str = Header(default="", alias="X-Timestamp"),
    x_nonce: str = Header(default="", alias="X-Nonce"),
):
    verify_replay(x_timestamp, x_nonce)
    verify_hmac(payload, x_signature)

    action = payload.get("action")
    if not action or not isinstance(action, str):
        raise HTTPException(status_code=400, detail="Missing/invalid action")

    return {"status": "accepted"}
