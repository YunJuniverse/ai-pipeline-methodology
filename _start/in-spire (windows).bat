@echo off
REM in-spire — methodology dashboard launcher (Windows)
REM Double-click entry point.

cd /d "%~dp0\.."

if not exist "60_tools\methodology.py" (
  echo [err] 60_tools\methodology.py not found.
  echo Run this file inside a project where methodology is applied.
  pause
  exit /b 1
)

python 60_tools\methodology.py dashboard --open
echo.
echo Dashboard is serving in the background. Stop with:
echo   python 60_tools\methodology.py dashboard stop --all
pause
