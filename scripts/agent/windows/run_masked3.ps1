New-Item -ItemType Directory -Force C:\Users\usful\agywork | Out-Null
Set-Location C:\Users\usful\agywork
python -u C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows\masked_probe2.py flash 600 2>&1 | Out-File -Append C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows\masked_probe3.log -Encoding utf8
