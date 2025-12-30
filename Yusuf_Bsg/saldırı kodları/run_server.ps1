# run_server.ps1
Set-Location -Path $PSScriptRoot

# venv aktif et
if (!(Test-Path ".\.venv\Scripts\Activate.ps1")) {
  Write-Host "ERROR: .venv not found. Create it with: py -3.14 -m venv .venv" -ForegroundColor Red
  exit 1
}
. .\.venv\Scripts\Activate.ps1

# env ayarları (istersen değiştir)
$env:OCPP_HMAC_SECRET = "super-long-random-secret"
$env:OCPP_ALLOWED_SKEW_SECONDS = "120"

Write-Host "Starting server on http://127.0.0.1:8000 ..." -ForegroundColor Green
python -m uvicorn backend.app.main:app --reload --host 127.0.0.1 --port 8000
