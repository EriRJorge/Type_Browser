@echo off
echo Creating Type Browser Installer Package...
echo.

REM Configuration
set APP_NAME=Type Browser
set APP_VERSION=1.1.0
set APP_EXE=Type_Browser.exe
set APP_ICON=icon.png
set OUTPUT_NAME=Type_Browser_Setup.exe

REM Check if executable exists
if not exist "dist\%APP_EXE%" (
    echo Error: Executable not found: dist\%APP_EXE%
    echo Please run 'python build_simple.py' first to create the executable.
    pause
    exit /b 1
)

REM Check if icon exists
if not exist "%APP_ICON%" (
    echo Error: Icon not found: %APP_ICON%
    pause
    exit /b 1
)

REM Create installer directory
set INSTALLER_DIR=installer_package
if exist "%INSTALLER_DIR%" rmdir /s /q "%INSTALLER_DIR%"
mkdir "%INSTALLER_DIR%"

REM Copy files to installer directory
echo Copying files...
copy "dist\%APP_EXE%" "%INSTALLER_DIR%\"
copy "%APP_ICON%" "%INSTALLER_DIR%\"

REM Create installer batch file
echo Creating installer script...
(
echo @echo off
echo echo Installing %APP_NAME% v%APP_VERSION%...
echo echo.
echo.
echo REM Check for administrator privileges
echo net session ^>nul 2^>^&1
echo if %%errorLevel%% neq 0 ^(
echo     echo This installer requires administrator privileges.
echo     echo Please right-click and select "Run as administrator"
echo     pause
echo     exit /b 1
echo ^)
echo.
echo REM Set installation directory
echo set INSTALL_DIR=%%ProgramFiles%%\%APP_NAME%
echo.
echo REM Create installation directory
echo if not exist "%%INSTALL_DIR%%" mkdir "%%INSTALL_DIR%%"
echo.
echo REM Copy application files
echo echo Copying application files...
echo copy "%APP_EXE%" "%%INSTALL_DIR%%\" /Y
echo copy "%APP_ICON%" "%%INSTALL_DIR%%\" /Y
echo.
echo REM Create desktop shortcut
echo echo Creating desktop shortcut...
echo set SCRIPT="%%TEMP%%\CreateShortcut.vbs"
echo echo Set oWS = WScript.CreateObject^("WScript.Shell"^) ^> %%SCRIPT%%
echo echo sLinkFile = "%%USERPROFILE%%\Desktop\%APP_NAME%.lnk" ^>^> %%SCRIPT%%
echo echo Set oLink = oWS.CreateShortcut^(sLinkFile^) ^>^> %%SCRIPT%%
echo echo oLink.TargetPath = "%%INSTALL_DIR%%\%APP_EXE%" ^>^> %%SCRIPT%%
echo echo oLink.IconLocation = "%%INSTALL_DIR%%\%APP_ICON%" ^>^> %%SCRIPT%%
echo echo oLink.Save ^>^> %%SCRIPT%%
echo cscript //nologo %%SCRIPT%%
echo del %%SCRIPT%%
echo.
echo REM Create start menu shortcuts
echo echo Creating start menu shortcuts...
echo set START_MENU=%%APPDATA%%\Microsoft\Windows\Start Menu\Programs\%APP_NAME%
echo if not exist "%%START_MENU%%" mkdir "%%START_MENU%%"
echo.
echo REM Main application shortcut
echo set SCRIPT="%%TEMP%%\CreateAppShortcut.vbs"
echo echo Set oWS = WScript.CreateObject^("WScript.Shell"^) ^> %%SCRIPT%%
echo echo sLinkFile = "%%START_MENU%%\%APP_NAME%.lnk" ^>^> %%SCRIPT%%
echo echo Set oLink = oWS.CreateShortcut^(sLinkFile^) ^>^> %%SCRIPT%%
echo echo oLink.TargetPath = "%%INSTALL_DIR%%\%APP_EXE%" ^>^> %%SCRIPT%%
echo echo oLink.IconLocation = "%%INSTALL_DIR%%\%APP_ICON%" ^>^> %%SCRIPT%%
echo echo oLink.Save ^>^> %%SCRIPT%%
echo cscript //nologo %%SCRIPT%%
echo del %%SCRIPT%%
echo.
echo REM Create uninstaller
echo echo Creating uninstaller...
echo ^> "%%INSTALL_DIR%%\Uninstall.bat" echo @echo off
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo echo Uninstalling %APP_NAME%...
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo.
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo REM Remove shortcuts
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo if exist "%%USERPROFILE%%\Desktop\%APP_NAME%.lnk" del "%%USERPROFILE%%\Desktop\%APP_NAME%.lnk"
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo if exist "%%APPDATA%%\Microsoft\Windows\Start Menu\Programs\%APP_NAME%" rmdir /s /q "%%APPDATA%%\Microsoft\Windows\Start Menu\Programs\%APP_NAME%"
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo.
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo REM Remove application files
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo if exist "%%INSTALL_DIR%%\%APP_EXE%" del "%%INSTALL_DIR%%\%APP_EXE%"
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo if exist "%%INSTALL_DIR%%\%APP_ICON%" del "%%INSTALL_DIR%%\%APP_ICON%"
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo.
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo REM Remove installation directory
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo if exist "%%INSTALL_DIR%%" rmdir "%%INSTALL_DIR%%"
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo.
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo echo %APP_NAME% has been uninstalled successfully.
echo ^>^> "%%INSTALL_DIR%%\Uninstall.bat" echo pause
echo.
echo REM Uninstaller shortcut
echo set SCRIPT="%%TEMP%%\CreateUninstallShortcut.vbs"
echo echo Set oWS = WScript.CreateObject^("WScript.Shell"^) ^> %%SCRIPT%%
echo echo sLinkFile = "%%START_MENU%%\Uninstall %APP_NAME%.lnk" ^>^> %%SCRIPT%%
echo echo Set oLink = oWS.CreateShortcut^(sLinkFile^) ^>^> %%SCRIPT%%
echo echo oLink.TargetPath = "%%INSTALL_DIR%%\Uninstall.bat" ^>^> %%SCRIPT%%
echo echo oLink.Save ^>^> %%SCRIPT%%
echo cscript //nologo %%SCRIPT%%
echo del %%SCRIPT%%
echo.
echo echo.
echo echo %APP_NAME% has been installed successfully!
echo echo Installation directory: %%INSTALL_DIR%%
echo echo Desktop shortcut created.
echo echo Start menu shortcuts created.
echo echo.
echo echo Press any key to exit...
echo pause ^>nul
) > "%INSTALLER_DIR%\install.bat"

REM Create README file
echo Creating README...
(
echo Type Browser v%APP_VERSION% Installer
echo ====================================
echo.
echo This package contains the Type Browser application installer.
echo.
echo To install:
echo 1. Right-click on install.bat and select "Run as administrator"
echo 2. Follow the installation prompts
echo 3. The application will be installed to Program Files
echo 4. Desktop and start menu shortcuts will be created
echo.
echo To uninstall:
echo 1. Go to Start Menu ^> Programs ^> %APP_NAME%
echo 2. Click "Uninstall %APP_NAME%"
echo.
echo System Requirements:
echo - Windows 10 or later
echo - No additional dependencies required ^(all included^)
echo.
echo Copyright ^(c^) 2025 Type Browser Team
) > "%INSTALLER_DIR%\README.txt"

REM Create ZIP file
echo Creating installer package...
powershell -Command "Add-Type -AssemblyName System.IO.Compression.FileSystem; [System.IO.Compression.ZipFile]::CreateFromDirectory('%INSTALLER_DIR%', '%OUTPUT_NAME%')"

REM Cleanup
rmdir /s /q "%INSTALLER_DIR%"

echo.
echo Installer package created successfully!
echo Output file: %OUTPUT_NAME%
echo.
echo The installer package contains:
echo - %APP_EXE% ^(main application^)
echo - %APP_ICON% ^(application icon^)
echo - install.bat ^(installer script^)
echo - README.txt ^(installation instructions^)
echo.
echo Customers can extract this ZIP file and run install.bat as administrator
echo to install the application with all dependencies included.
echo.
pause 