Set-Location C:\Users\usful\Desktop\Projects\inno_notes
git pull --ff-only 2>&1 | Select-Object -Last 1
python scripts/agent/windows/masked_probe.py 2>&1 | Out-File -Append C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows\masked_probe.log -Encoding utf8
