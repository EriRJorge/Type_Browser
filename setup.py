import PyInstaller.__main__
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

PyInstaller.__main__.run([
    'TypeBrowser.py',
    '--name=Type_Browser',
    '--icon=icon.png',
    '--onefile',
    '--windowed',
    '--add-data=icon.png;.',
    '--add-data=browser_data.py;.',
    '--add-data=settings_dialog.py;.',
    '--add-data=download_manager.py;.',
    '--add-data=about_dialog.py;.',
    '--add-data=bookmark_manager.py;.',
    '--clean',
    '--noconfirm'
]) 