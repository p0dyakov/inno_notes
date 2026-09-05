$W = "C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows"
Set-Location C:\Users\usful\agywork
"=== AB $(Get-Date -Format o) ===" | Out-File -Append "$W\ab.log" -Encoding utf8
python -u "$W\ab_gate.py" 2>&1 | Out-File -Append "$W\ab.log" -Encoding utf8
