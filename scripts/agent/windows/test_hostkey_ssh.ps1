ssh.exe -i "$env:USERPROFILE\.ssh\hostkey_us" -o BatchMode=yes -o ConnectTimeout=8 -o StrictHostKeyChecking=accept-new root@80.209.241.71 "echo WIN_TO_US_OK"
