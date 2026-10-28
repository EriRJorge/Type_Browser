import PyInstaller.__main__
import os
import shutil

print("Building Type Browser with robust configuration...")
print("The native application format for this operating system will be created...")

# Clean previous builds
dist_path = "dist"
build_path = "build"

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

# Create PyInstaller command using the robust spec file
PyInstaller.__main__.run([
    'Type_Browser_robust.spec',
    '--noconfirm',
    '--clean'
])

print("\nBuild completed!")
print("The native application should now be more compatible across supported systems.")