import PyInstaller.__main__
import os
import shutil

# Get the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Clean previous builds
dist_path = os.path.join(current_dir, 'dist')
build_path = os.path.join(current_dir, 'build')

try:
    if os.path.exists(dist_path):
        shutil.rmtree(dist_path)
except Exception as e:
    print(f"Warning: could not remove dist directory: {e}")

try:
    if os.path.exists(build_path):
        shutil.rmtree(build_path)
except Exception as e:
    print(f"Warning: could not remove build directory: {e}")

# Create PyInstaller command using the .spec file
PyInstaller.__main__.run([
    'Type_Browser.spec',
    '--noconfirm',
    '--clean'
]) 