@echo off
REM Make sure you're in the backend folder and virtualenv activated
pip install -r requirements.txt
pyinstaller --onefile --add-data "data;data" --name backend app.py
echo Build complete. Check dist\backend.exe
pause