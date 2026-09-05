# param forwarding to conv_quick.py; log to conv.log
$W = "C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows"
Set-Location C:\Users\usful\agywork
$env:INNO_PROXY = "http://127.0.0.1:18081"
python -u "$W\conv_quick.py" @args 2>&1 | Out-File -Append "$W\conv.log" -Encoding utf8
