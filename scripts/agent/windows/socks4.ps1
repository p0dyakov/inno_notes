curl.exe -s --max-time 7 -4 --proxy socks5h://127.0.0.1:1080 -o NUL -w "g4:%{http_code} t:%{time_total} ip:%{remote_ip}\n" https://generativelanguage.googleapis.com/; Write-Output DONE
