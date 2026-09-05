# Spawn one persistent masked LS; child survives this task. Address -> holder.json
$W = "C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows"
"hold start $(Get-Date -Format o)" | Out-File -Append "$W\holder.log" -Encoding utf8
Set-Location C:\Users\usful\agywork
$env:INNO_PROXY = "http://127.0.0.1:18081"
python -u "$W\hold_ls.py" 2>&1 | Out-File -Append "$W\holder.log" -Encoding utf8
