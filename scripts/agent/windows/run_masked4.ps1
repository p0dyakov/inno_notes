New-Item -ItemType Directory -Force C:\Users\usful\agywork | Out-Null
Set-Location C:\Users\usful\agywork
python -u C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows\masked_probe2.py flash_lite 600 2>&1 | Out-File -Append C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows\masked_probe4.log -Encoding utf8
