# test_request.ps1
Set-Location -Path $PSScriptRoot

# venv aktif et
if (!(Test-Path ".\.venv\Scripts\Activate.ps1")) {
  Write-Host "ERROR: .venv not found. Create it with: py -3.14 -m venv .venv" -ForegroundColor Red
  exit 1
}
. .\.venv\Scripts\Activate.ps1

# Secret (run_server.ps1 ile aynı olmalı!)
$secret = "super-long-random-secret"

# Payload (istersen burayı değiştir)
$payloadObj = @{
  action = "Ping"
  foo    = "bar"
}

# ---- Canonical JSON (sort_keys=True eşdeğeri) ----
# Key'leri alfabetik sırala ve JSON'u boşluksuz üret
$ordered = [ordered]@{}
($payloadObj.Keys | Sort-Object) | ForEach-Object { $ordered[$_] = $payloadObj[$_] }
$canonicalJson = ($ordered | ConvertTo-Json -Compress)

# body.json yaz (sunucu payload'u bunu okuyacak)
$canonicalJson | Set-Content -Encoding UTF8 body.json

# ---- HMAC-SHA256 hex signature üret ----
$hmac = [System.Security.Cryptography.HMACSHA256]::new([Text.Encoding]::UTF8.GetBytes($secret))
$hashBytes = $hmac.ComputeHash([Text.Encoding]::UTF8.GetBytes($canonicalJson))
$sig = ([BitConverter]::ToString($hashBytes) -replace '-', '').ToLowerInvariant()

# Timestamp & Nonce
$ts = [int][DateTimeOffset]::UtcNow.ToUnixTimeSeconds()
$nonce = "nonce" + (Get-Random -Minimum 100000 -Maximum 999999)

Write-Host "TS=$ts"
Write-Host "NONCE=$nonce"
Write-Host "SIG=$sig"
Write-Host "BODY=$canonicalJson"

# İsteği gönder
curl.exe -X POST "http://127.0.0.1:8000/ocpp-message" `
  --data-binary "@body.json" `
  -H "Content-Type: application/json" `
  -H "X-Timestamp: $ts" `
  -H "X-Nonce: $nonce" `
  -H "X-Signature: $sig"
