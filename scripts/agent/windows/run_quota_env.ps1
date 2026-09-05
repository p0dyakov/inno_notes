$env:HTTPS_PROXY = "socks5h://127.0.0.1:1080"
$env:HTTP_PROXY = "socks5h://127.0.0.1:1080"
$env:ALL_PROXY = "socks5h://127.0.0.1:1080"
$env:NO_PROXY = "127.0.0.1,localhost,::1"
$env:NODE_OPTIONS = "--dns-result-order=ipv4first"
Set-Location C:\Users\usful\Desktop\Projects\inno_notes
python scripts/agent/llm_antigravity.py 2>&1 | Out-File -Append C:\Users\usful\Desktop\Projects\inno_notes\scripts\agent\windows\probe_env.log -Encoding utf8
