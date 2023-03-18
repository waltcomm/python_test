@echo off
cd .venv
cd Scripts
call activate.bat
cd ..
cd ..
.\.venv\Scripts\python -m pytest
rem .\.venv\Scripts\pytest.exe