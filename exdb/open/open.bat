@echo off
set SAVE_MCO_ROOT=%MCO_ROOT%
set MCO_ROOT=%CD%\..\..\..
python open.py
set MCO_ROOT=%SAVE_MCO_ROOT%
pause
