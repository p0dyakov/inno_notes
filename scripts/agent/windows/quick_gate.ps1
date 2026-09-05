# Fast gate: quota snapshot + 75s flash_lite masked probe. Fail fast, log to quick_gate.log.
$W = "C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows"
$Log = "$W\quick_gate.log"
"=== gate $(Get-Date -Format o) ===" | Out-File -Append $Log -Encoding utf8
Set-Location C:\Users\usful\agywork
$env:INNO_PROXY = "http://127.0.0.1:18081"
python -u "$W\quota_now.py" 2>&1 | Out-File -Append $Log -Encoding utf8
python -u "$W\masked_probe2.py" flash_lite 75 2>&1 | Out-File -Append $Log -Encoding utf8
"=== gate end $(Get-Date -Format o) ===" | Out-File -Append $Log -Encoding utf8
