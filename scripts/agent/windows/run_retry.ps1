$W = "C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows"
Set-Location C:\Users\usful\agywork
"=== RETRY $(Get-Date -Format o) ===" | Out-File -Append "$W\retry.log" -Encoding utf8
python -u "$W\retry_tun.py" 2>&1 | Out-File -Append "$W\retry.log" -Encoding utf8
