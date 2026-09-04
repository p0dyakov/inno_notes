#Requires -Version 5.1
<#
.SYNOPSIS
  Status + setup for the inno_notes automation stack on Windows:
  Yandex Browser (xbox-dns.ru DoH + Gemini proxy exclusions), Antigravity,
  Sota VPN, Tailscale (+SSH for remote management), Python deps, repos.
  Run in an elevated PowerShell for machine-policy steps.
  Safe to re-run: status first, changes only where needed.
#>
[CmdletBinding()]
param(
  [switch]$Apply,          # without -Apply: status/verify only
  [string]$RepoRoot = "$env:USERPROFILE\Desktop\Projects\inno_notes",
  [string]$InnofilesRoot = "$env:USERPROFILE\Desktop\Projects\inno_files"
)

$ErrorActionPreference = 'Continue'
$GeminiBypass = @('aistudio.google.com', 'alkalimakersuite-pa.clients6.google.com', 'gemini.google.com', 'generativelanguage.googleapis.com', 'daily-cloudcode-pa.googleapis.com')
$DohUrl = 'https://xbox-dns.ru/dns-query'

function Step($name) { Write-Host "`n== $name" -ForegroundColor Cyan }
function Ok($m) { Write-Host "  [OK] $m" -ForegroundColor Green }
function Warn($m) { Write-Host "  [!!] $m" -ForegroundColor Yellow }
function Info($m) { Write-Host "  .. $m" -ForegroundColor Gray }

$isAdmin = ([Security.Principal.WindowsPrincipal][Security.Principal.WindowsIdentity]::GetCurrent()).IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)
Info "Admin: $isAdmin (machine policies need elevation)"

Step '1. Python + deps'
$py = Get-Command python -ErrorAction SilentlyContinue
if ($py) { Ok "python: $(python --version 2>&1) at $($py.Source)"; python -c 'import httpx' 2>$null; if ($LASTEXITCODE -eq 0) { Ok 'httpx installed' } else { Warn 'httpx missing'; if ($Apply) { python -m pip install --quiet httpx; Ok 'httpx installed' } } }
else { Warn 'python not found (install 3.11+ and re-run)' }

Step '2. Tailscale (+SSH for remote management)'
$ts = Get-Command tailscale -ErrorAction SilentlyContinue
if ($ts) { $st = tailscale status 2>&1 | Out-String; ($st -split "`n" | Select-Object -First 6) | ForEach-Object { Info $_.Trim() }; if ($Apply) { tailscale up --ssh 2>&1 | Select-Object -First 2 | ForEach-Object { Info $_.Trim() }; Ok 'tailscale up --ssh attempted (enables remote mgmt)' } }
else { Warn 'tailscale not found (install Tailscale, log in)' }

Step '3. Sota VPN'
$sota = @(Get-Process 'SotaVPN','Sota Connect' -ErrorAction SilentlyContinue)
if ($sota.Count) { Ok "Sota Connect running ($($sota.Count) proc)" } else { Warn 'Sota Connect not running (start it; US exit per setup)' }

Step '4. Antigravity (auth + hub)'
$agy = @(Get-Process Antigravity -ErrorAction SilentlyContinue)
if ($agy.Count) { Ok "Antigravity running ($($agy.Count) proc)" } else { Warn 'Antigravity not running (install, log in with Google, keep it running during generation)' }
$agyData = Join-Path $env:APPDATA 'Antigravity\app_storage.json'
if (Test-Path $agyData) {
  $m = Select-String -Path $agyData -Pattern '"(new-convo-last-selected-project|lastCreatedProjectId)"\s*:\s*"([0-9a-f-]+)"' | Select-Object -First 1
  if ($m) { Ok "project id present in app_storage.json" } else { Warn 'no project id in app_storage.json (open Antigravity once)' }
} else { Warn 'no %APPDATA%\Antigravity\app_storage.json yet' }

Step '5. Yandex Browser: DoH xbox-dns.ru'
$polBase = 'HKLM:\SOFTWARE\Policies\YandexBrowser'
$cur = (Get-ItemProperty -Path $polBase -Name DnsOverHttpsTemplates -ErrorAction SilentlyContinue).DnsOverHttpsTemplates
Info "policy DnsOverHttpsTemplates: $($cur -join ', ')"
if ($cur -contains $DohUrl) { Ok 'DoH provider already xbox-dns.ru' }
elseif ($Apply -and $isAdmin) {
  New-Item -Path $polBase -Force | Out-Null
  New-ItemProperty -Path $polBase -Name DnsOverHttpsMode -Value 'secure' -PropertyType String -Force | Out-Null
  New-ItemProperty -Path $polBase -Name DnsOverHttpsTemplates -Value $DohUrl -PropertyType String -Force | Out-Null
  Ok 'DoH policy set (restart Yandex Browser)'
} elseif ($Apply) { Warn 'need elevation for machine DoH policy (or set Yandex Settings > Privacy > DNS manually)' }

Step '6. Proxy exclusions for Gemini domains'
$inet = 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Internet Settings'
$ov = (Get-ItemProperty -Path $inet -Name ProxyOverride -ErrorAction SilentlyContinue).ProxyOverride
Info "current ProxyOverride: $ov"
$missing = $GeminiBypass | Where-Object { $ov -notlike "*$_*" }
if (-not $missing) { Ok 'all Gemini hosts already excluded' }
elseif ($Apply) {
  $new = (($ov -split ';' | Where-Object { $_ }) + $missing | Select-Object -Unique) -join ';'
  Set-ItemProperty -Path $inet -Name ProxyOverride -Value $new
  Ok "ProxyOverride updated (+$($missing.Count) hosts)"
  if ($isAdmin) {
    New-Item -Path $polBase -Force | Out-Null
    New-ItemProperty -Path $polBase -Name ProxyMode -Value 'system' -PropertyType String -Force | Out-Null
    New-ItemProperty -Path $polBase -Name ProxyBypassList -Value ($GeminiBypass -join ',') -PropertyType String -Force | Out-Null
    Ok 'Chromium ProxyBypassList policy set for Yandex'
  }
}

Step '7. Verify: xbox-DoH answers for Gemini hosts (expect 87.228.47.x relay)'
$DohCheck = {
  param($HostName)
  $labels = $HostName.Split('.') | ForEach-Object { [byte]$_.Length; [Text.Encoding]::ASCII.GetBytes($_) }
  $q = New-Object Collections.Generic.List[byte]
  $q.AddRange([byte[]](0x22,0x22,0x01,0x00,0x00,0x01,0x00,0x00,0x00,0x00,0x00,0x00))
  foreach ($l in $labels) { if ($l -is [byte]) { $q.Add($l) } else { $q.AddRange($l) } }
  $q.AddRange([byte[]](0x00,0x00,0x01,0x00,0x01))
  $b64 = [Convert]::ToBase64String($q.ToArray()).TrimEnd('=').Replace('+','-').Replace('/','_')
  try {
    $r = Invoke-WebRequest -UseBasicParsing -Uri "${DohUrl}?dns=${b64}" -Headers @{ Accept = 'application/dns-message' } -TimeoutSec 12
    $ips = [regex]::Matches([Text.Encoding]::GetEncoding('iso-8859-1').GetString($r.RawContentStream.ToArray()), '\x00\x04(.{4})', 'Singleline') |
      ForEach-Object { ($_.Groups[1].Value.ToCharArray() | ForEach-Object { [int]$_ }) -join '.' }
    return ($ips | Select-Object -Unique) -join ', '
  } catch { return "ERROR: $($_.Exception.Message)" }
}
foreach ($h in @('aistudio.google.com', 'alkalimakersuite-pa.clients6.google.com', 'gemini.google.com', 'generativelanguage.googleapis.com')) {
  $ans = & $DohCheck $h
  if ($ans -match '87\.228\.47\.') { Ok "$h -> $ans" } else { Warn "$h -> $ans" }
}


Step '7b. Pre-push hook (format gate)'
$hookSrc = Join-Path $RepoRoot 'scripts\agent\hooks\pre-push'
foreach ($r in @($RepoRoot, $InnofilesRoot)) {
  $dest = Join-Path $r '.git\hooks\pre-push'
  if ((Test-Path $hookSrc) -and (Test-Path (Join-Path $r '.git'))) {
    Copy-Item $hookSrc $dest -Force
    Info "hook installed: $dest"
  }
}

Step '8. Repos'
foreach ($r in @($RepoRoot, $InnofilesRoot)) { if (Test-Path $r) { Ok $r } else { Warn "missing: $r" } }

Step '9. Antigravity hub quota (needs Antigravity running)'
if ((Test-Path (Join-Path $RepoRoot 'scripts\agent\llm_antigravity.py')) -and $py) {
  Push-Location (Join-Path $RepoRoot 'scripts\agent')
  python llm_antigravity.py 2>&1 | Select-Object -First 6 | ForEach-Object { Info $_ }
  Pop-Location
} else { Warn 'repo scripts not found yet' }

Write-Host "`nDone. Re-run with -Apply (elevated) to apply missing settings." -ForegroundColor Cyan
