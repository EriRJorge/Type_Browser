# -*- mode: python ; coding: utf-8 -*-
import os
import PyQt5

pyqt5_path = PyQt5.__path__[0]
qt_path = os.path.join(pyqt5_path, "Qt5")

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
    ],
    hiddenimports=[
        'PyQt5.sip',
        'PyQt5.QtNetwork',
        'PyQt5.QtWebEngineWidgets',
    ],
    hookspath=['.'],
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
