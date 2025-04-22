@echo off
REM Change to project root directory (wrap in quotes because of '&' character)
cd /d "C:\TechPathshala\R&D\refactor_UpdatedImprovedCodeReviewer"

REM Set PYTHONPATH (again, quotes for safety)
set "PYTHONPATH=C:\TechPathshala\R&D\refactor_UpdatedImprovedCodeReviewer"

REM Confirm values
echo Current directory: %CD%
echo PYTHONPATH set to: %PYTHONPATH%

REM Run the script
python cli\main.py

pause
