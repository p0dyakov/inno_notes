$key = "$env:USERPROFILE\.ssh\hostkey_us"
if (-not (Test-Path $key)) { ssh-keygen -t ed25519 -N "" -f $key }
Get-Content "$key.pub"
