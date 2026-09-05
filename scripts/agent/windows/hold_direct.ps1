$W = "C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows"
"hold-direct start $(Get-Date -Format o)" | Out-File -Append "$W\holder.log" -Encoding utf8
Set-Location C:\Users\usful\agywork
$env:INNO_PROXY = ""
python -u "$W\hold_ls2.py" 2>&1 | Out-File -Append "$W\holder.log" -Encoding utf8
