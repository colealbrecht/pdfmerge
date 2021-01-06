@echo off

pyinstaller.exe --windowed --onefile --hidden-import pikepdf._cpphelpers -i ./pdfmerge-icon.ico --add-data "./pdfmerge-icon.png;." pdfmerge.py