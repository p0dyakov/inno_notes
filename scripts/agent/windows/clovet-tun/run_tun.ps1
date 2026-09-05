# Start Clovet full-app tunnel (separate sing-box copy; killed by dead-man ClovetKill).
$D = "C:\Users\usful\clovet-tun"
New-Item -ItemType Directory -Force $D | Out-Null
$Exe = "$D\clovet-sing-box.exe"
if (-not (Test-Path $Exe)) {
  Copy-Item "C:\Program Files\SotaConnect\bin\sing-box.exe" $Exe
}
& $Exe check -c "$D\config.json" 2>&1 | Out-File -Append "$D\tun.log" -Encoding utf8
"=== tun start $(Get-Date -Format o) ===" | Out-File -Append "$D\tun.log" -Encoding utf8
& $Exe run -c "$D\config.json" 2>&1 | Out-File -Append "$D\tun.log" -Encoding utf8
