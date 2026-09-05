$l = Get-NetTCPConnection -LocalPort 1080 -State Listen -ErrorAction SilentlyContinue
Write-Output ("listen1080:" + ($l.Count -gt 0))
Write-Output ("egress:" + (curl.exe -s --max-time 10 --proxy socks5h://127.0.0.1:1080 ifconfig.me))
curl.exe -s --max-time 10 --proxy socks5h://127.0.0.1:1080 -o NUL -w "google:%{http_code} t:%{time_total}\n" https://generativelanguage.googleapis.com/
