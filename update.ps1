# Usage: .\update.ps1            (or)  .\update.ps1 "commit message"
param([string]$msg = "Update kit content")
Set-Location $PSScriptRoot
$dl = (New-Object -ComObject Shell.Application).NameSpace('shell:Downloads').Self.Path
$new = Get-ChildItem "$dl\kit*.json" -ErrorAction SilentlyContinue | Sort-Object LastWriteTime -Descending | Select-Object -First 1
$cur = Get-Item ".\data\kit.json"
if ($new -and $new.LastWriteTime -gt $cur.LastWriteTime) {
  Copy-Item $new.FullName ".\data\kit.json" -Force
  Write-Host "Naya data liya: $($new.Name)" -ForegroundColor Green
} else {
  Write-Host "Downloads me naya kit.json nahi mila, purana data hi use hoga" -ForegroundColor Yellow
}
python scripts\build.py
if ($LASTEXITCODE -ne 0) { Write-Host "BUILD FAIL - push nahi kiya" -ForegroundColor Red; return }
git add .
git commit -m $msg
git push
start index.html
