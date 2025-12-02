# Build helper for creating a single-file executable with PyInstaller (Windows)
# Usage: open PowerShell in project root and run `.uild_exe.ps1`

Write-Output "Installing PyInstaller..."
python -m pip install --upgrade pip
python -m pip install pyinstaller

Write-Output "Running PyInstaller (this may take a few minutes)..."
# The --add-data format on Windows uses a semicolon separator: "source;dest"
pyinstaller --noconfirm --onefile --add-data "www;www" main.py

Write-Output "Build finished. See the 'dist' folder for the executable."
