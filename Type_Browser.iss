[Setup]
AppName=Type Browser
AppVersion=1.1.0
DefaultDirName={pf}\Type Browser
DefaultGroupName=Type Browser
UninstallDisplayIcon={app}\icon.png
OutputBaseFilename=Type_Browser_Installer
Compression=lzma
SolidCompression=yes

[Files]
Source: "dist\Type_Browser.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "icon.png"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Type Browser"; Filename: "{app}\Type_Browser.exe"; IconFilename: "{app}\icon.png"
Name: "{group}\Uninstall Type Browser"; Filename: "{uninstallexe}"
Name: "{userdesktop}\Type Browser"; Filename: "{app}\Type_Browser.exe"; IconFilename: "{app}\icon.png"; Tasks: desktopicon

[Tasks]
Name: "desktopicon"; Description: "Create a &desktop icon"; GroupDescription: "Additional icons:"

[Run]
Filename: "{app}\Type_Browser.exe"; Description: "Launch Type Browser"; Flags: nowait postinstall skipifsilent 