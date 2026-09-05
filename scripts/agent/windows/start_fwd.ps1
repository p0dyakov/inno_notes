schtasks /Delete /TN InnoFwd /F 2>$null | Out-Null
$action = "ssh.exe -i $env:USERPROFILE\.ssh\hostkey_us -N -L 18081:127.0.0.1:18081 -o ServerAliveInterval=30 -o ServerAliveCountMax=3 -o ExitOnForwardFailure=yes root@80.209.241.71"
schtasks /Create /TN InnoFwd /TR "$action" /SC ONSTART /F
schtasks /Run /TN InnoFwd
Start-Sleep 4
curl.exe -s --max-time 8 -x http://127.0.0.1:18081 -o NUL -w "win-via-us:%{http_code} t:%{time_total}\n" https://generativelanguage.googleapis.com/
