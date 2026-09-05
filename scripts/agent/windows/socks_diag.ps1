curl.exe -v --max-time 6 --proxy socks5h://127.0.0.1:1080 https://generativelanguage.googleapis.com/ 2>&1 | Select-Object -First 25
