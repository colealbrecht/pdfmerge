#!/usr/bin/env bash

pyinstaller --windowed --onefile --hidden-import pikepdf._cpphelpers ./pdfmerge.py
