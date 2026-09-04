# Watches Antigravity serving; on first success regenerates semester-4 Theory.
# Usage (detached): schtasks /create /tn InnoRegen /tr "powershell -NoProfile -ExecutionPolicy Bypass -File C:\...\regen_watch.ps1" /sc ONCE /st HH:mm /f
#   + schtasks /run /tn InnoRegen. Logs to regen_watch.log next to this script.
param(
  [string]$RepoRoot = "$env:USERPROFILE\Desktop\Projects\inno_notes",
  [string]$InnoRoot = "$env:USERPROFILE\Desktop\Projects\inno_files",
  [int]$Hours = 12,
  [int]$PeriodSec = 1200
)
$Log = Join-Path $PSScriptRoot 'regen_watch.log'
function L($m) { "$(Get-Date -Format 'HH:mm:ss') $m" | Tee-Object -FilePath $Log -Append }
$env:LLM_BACKEND = 'antigravity'
$deadline = (Get-Date).AddHours($Hours)
L "watch start (until $($deadline.ToString('HH:mm')))"
while ((Get-Date) -lt $deadline) {
  & python (Join-Path $PSScriptRoot 'probe_ok.py') >> $Log 2>&1
  if ($LASTEXITCODE -eq 0) {
    L 'serving OK -> regenerating Theory'
    & python (Join-Path $RepoRoot 'scripts\agent\generate.py') --inno-files $InnoRoot --regen-theory 'semester-4/Operating Systems/1.qmd' 'semester-4/Differential Equations/1.qmd' --tries 3 >> $Log 2>&1
    if ($LASTEXITCODE -eq 0) {
      git -C $RepoRoot add -- 'semester-4/Operating Systems/1.qmd' 'semester-4/Differential Equations/1.qmd' >> $Log 2>&1
      git -C $RepoRoot commit -m 'feat(theory): regenerate semester-4 Theory via Antigravity Pro' >> $Log 2>&1
      'REGEN-DONE' | Out-File (Join-Path $PSScriptRoot 'REGEN-DONE.txt')
      L 'regen committed locally (push needs one interactive login or relay)'
      exit 0
    }
    L 'regen failed, keep watching'
  } else { L 'serving still gated' }
  Start-Sleep -Seconds $PeriodSec
}
L 'deadline reached'
exit 1
