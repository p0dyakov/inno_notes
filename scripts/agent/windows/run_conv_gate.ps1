$W = "C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows"
Set-Location C:\Users\usful\agywork
python -u "$W\conv_quick.py" flash_lite 75 2>&1 | Out-File -Append "$W\conv.log" -Encoding utf8
"=== gate end $(Get-Date -Format o) ===" | Out-File -Append "$W\conv.log" -Encoding utf8
