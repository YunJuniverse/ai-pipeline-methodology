# setup-windows.ps1 — in-spire (windows).lnk 바로가기 자동 생성 (아이콘 임베드)
# 사용자 1회 실행:
#   1. _start 폴더에서 우클릭 → PowerShell 에서 실행
#   2. 또는: powershell -ExecutionPolicy Bypass -File .\setup-windows.ps1

$here = Split-Path -Parent $MyInvocation.MyCommand.Path
$batPath = Join-Path $here "in-spire (windows).bat"
$icoPath = Join-Path $here "assets\in-spire.ico"
$lnkPath = Join-Path $here "in-spire (windows).lnk"

if (-not (Test-Path $batPath)) {
    Write-Host "[err] in-spire (windows).bat not found in $here" -ForegroundColor Red
    exit 1
}

$shell = New-Object -ComObject WScript.Shell
$lnk = $shell.CreateShortcut($lnkPath)
$lnk.TargetPath = $batPath
$lnk.WorkingDirectory = $here
if (Test-Path $icoPath) {
    $lnk.IconLocation = "$icoPath,0"
}
$lnk.Description = "in-spire — methodology dashboard launcher (Windows)"
$lnk.Save()

Write-Host "[ok] Created 'in-spire (windows).lnk' with icon at $lnkPath" -ForegroundColor Green
Write-Host "Double-click the .lnk to launch the dashboard."
