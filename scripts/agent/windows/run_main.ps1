$W = "C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows"
Set-Location C:\Users\usful\agywork
"=== MAIN $(Get-Date -Format o) ===" | Out-File -Append "$W\main.log" -Encoding utf8
python -u "$W\main_gate.py" 2>&1 | Out-File -Append "$W\main.log" -Encoding utf8
