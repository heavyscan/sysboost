# SysBoost Build Script (Windows)

Write-Host "Starting SysBoost Build Process..." -ForegroundColor Cyan

# Cleanup
if (Test-Path "./dist") { Remove-Item -Recurse -Force "./dist" }
if (Test-Path "./build") { Remove-Item -Recurse -Force "./build" }

# Install PyInstaller if not present
pip install pyinstaller

# Run Build
pyinstaller --clean sysboost.spec

Write-Host "Build Complete! Check the 'dist' folder." -ForegroundColor Green
