# TZ-masking experiment: US Eastern system TZ + short flash_lite masked probe, then restore MSK.
# Run as one-shot schtasks AFTER InnoSitter finishes (serial: hub tolerates parallel LS, but keep it clean).
$W = "C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows"
$Log = "$W\tz_probe.log"
"=== tz_probe start $(Get-Date -Format o) ===" | Out-File -Append $Log -Encoding utf8
"before: $(tzutil /g)" | Out-File -Append $Log -Encoding utf8
tzutil /s "Eastern Standard Time" 2>&1 | Out-File -Append $Log -Encoding utf8
"after-set: $(tzutil /g)" | Out-File -Append $Log -Encoding utf8
Set-Location C:\Users\usful\agywork
$env:INNO_PROXY = "http://127.0.0.1:18081"
python -u "$W\masked_probe2.py" flash_lite 300 2>&1 | Out-File -Append $Log -Encoding utf8
tzutil /s "Russian Standard Time" 2>&1 | Out-File -Append $Log -Encoding utf8
"restored: $(tzutil /g)" | Out-File -Append $Log -Encoding utf8
"=== tz_probe end $(Get-Date -Format o) ===" | Out-File -Append $Log -Encoding utf8
