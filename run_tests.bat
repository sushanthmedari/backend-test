@echo off
setlocal
cd /d "%~dp0"

if not exist ".venv\Scripts\python.exe" (
  py -3 -m venv .venv 2>nul
  if errorlevel 1 python -m venv .venv
)

call ".venv\Scripts\activate.bat"
python -m pip install -q -r requirements.txt
python -m pytest -q %*
exit /b %ERRORLEVEL%
