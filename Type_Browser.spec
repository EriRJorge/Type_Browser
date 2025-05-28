# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['TypeBrowser.py'],
    pathex=[],
    binaries=[],
    datas=[('icon.png', '.'), ('browser_data.py', '.'), ('settings_dialog.py', '.'), ('download_manager.py', '.'), ('about_dialog.py', '.'), ('bookmark_manager.py', '.'), ('shortcuts_dialog.py', '.')],
    hiddenimports=['PyQt5', 'PyQt5.QtCore', 'PyQt5.QtGui', 'PyQt5.QtWidgets', 'PyQt5.QtWebEngineWidgets', 'PyQt5.QtWebEngineCore', 'PyQt5.QtWebEngine', 'PyQt5.sip'],
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
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['icon.png'],
)
