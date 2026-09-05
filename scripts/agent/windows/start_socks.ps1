schtasks /Delete /TN InnoSocks /F 2>$null | Out-Null
$action = "ssh.exe -i $env:USERPROFILE\.ssh\hostkey_us -N -D 127.0.0.1:1080 -o ServerAliveInterval=30 -o ServerAliveCountMax=3 -o ExitOnForwardFailure=yes root@80.209.241.71"
schtasks /Create /TN InnoSocks /TR "$action" /SC ONSTART /F
schtasks /Run /TN InnoSocks
Start-Sleep 3
Get-Process ssh -ErrorAction SilentlyContinue | Select-Object Id
