import PyInstaller.__main__
import os

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Define the files to include
files_to_include = [
    'TypeBrowser.py',
    'browser_data.py',
    'settings_dialog.py',
    'download_manager.py',
    'about_dialog.py',
    'bookmark_manager.py',
    'shortcuts_dialog.py',
    'icon.png'
]

# Create PyInstaller command
PyInstaller.__main__.run([
    'TypeBrowser.py',  # Main script
    '--name=Type_Browser',  # Name of the executable
    '--icon=icon.png',  # Application icon
    '--onefile',  # Create a single executable
    '--windowed',  # Don't show console window
    '--clean',  # Clean PyInstaller cache
    '--noconfirm',  # Replace existing spec file
    '--add-data=icon.png;.',  # Include icon
    '--add-data=browser_data.py;.',  # Include browser data module
    '--add-data=settings_dialog.py;.',  # Include settings dialog
    '--add-data=download_manager.py;.',  # Include download manager
    '--add-data=about_dialog.py;.',  # Include about dialog
    '--add-data=bookmark_manager.py;.',  # Include bookmark manager
    '--add-data=shortcuts_dialog.py;.',  # Include shortcuts dialog
    '--hidden-import=PyQt5',
    '--hidden-import=PyQt5.QtCore',
    '--hidden-import=PyQt5.QtGui',
    '--hidden-import=PyQt5.QtWidgets',
    '--hidden-import=PyQt5.QtWebEngineWidgets',
    '--hidden-import=PyQt5.QtWebEngineCore',
    '--hidden-import=PyQt5.QtWebEngine',
    '--hidden-import=PyQt5.sip',
]) 