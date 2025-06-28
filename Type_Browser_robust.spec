# -*- mode: python ; coding: utf-8 -*-
import os
import sys
from PyInstaller.utils.hooks import collect_data_files, collect_submodules

# Get PyQt5 path
import PyQt5
pyqt5_path = PyQt5.__path__[0]

# Collect all PyQt5 modules
pyqt5_modules = collect_submodules('PyQt5')

# Collect all data files
pyqt5_data = collect_data_files('PyQt5')

a = Analysis(
    ['TypeBrowser.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('icon.png', '.'),
        ('about_dialog.py', '.'),
        ('bookmark_manager.py', '.'),
        ('browser_data.py', '.'),
        ('download_manager.py', '.'),
        ('settings_dialog.py', '.'),
        ('shortcuts_dialog.py', '.'),
    ] + pyqt5_data,
    hiddenimports=[
        'PyQt5.sip',
        'PyQt5.QtCore',
        'PyQt5.QtGui', 
        'PyQt5.QtWidgets',
        'PyQt5.QtNetwork',
        'PyQt5.QtWebEngineWidgets',
        'PyQt5.QtWebEngineCore',
        'PyQt5.QtWebEngine',
        'PyQt5.QtPrintSupport',
        'PyQt5.QtPositioning',
        'PyQt5.QtQuick',
        'PyQt5.QtQuickWidgets',
        'PyQt5.QtWebChannel',
        'PyQt5.QtQml',
        'PyQt5.QtMultimedia',
        'PyQt5.QtMultimediaWidgets',
        'PyQt5.QtBluetooth',
        'PyQt5.QtDBus',
        'PyQt5.QtDesigner',
        'PyQt5.QtHelp',
        'PyQt5.QtLocation',
        'PyQt5.QtMacExtras',
        'PyQt5.QtNfc',
        'PyQt5.QtOpenGL',
        'PyQt5.QtSensors',
        'PyQt5.QtSerialPort',
        'PyQt5.QtSql',
        'PyQt5.QtSvg',
        'PyQt5.QtTest',
        'PyQt5.QtWinExtras',
        'PyQt5.QtXml',
        'PyQt5.QtXmlPatterns',
    ] + pyqt5_modules,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='Type_Browser',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='icon.png',
) 