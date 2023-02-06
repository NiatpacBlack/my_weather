@echo off
chcp 1251
cd "%~dp0"
call "venv\Scripts\activate.bat"
@echo on
python my_weather.py
@echo off
pause