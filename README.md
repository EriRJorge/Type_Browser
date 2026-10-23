# Type Browser

Type Browser is a lightweight desktop browser built with Python, PyQt5, and
Qt WebEngine. It provides a familiar tabbed browsing experience with a
modern dark interface, persistent bookmarks and history, downloads, zoom
controls, private-by-default permissions, and useful keyboard shortcuts.

## Features

- Chrome-style tabs and address bar with URL and web search support
- Back, forward, reload, home, fullscreen, and new-tab controls
- Bookmarks, browsing history, downloads, and configurable preferences
- Dark and light themes, page zoom, find-in-page, save page, and dev tools
- Persistent Chromium cache and browser data under the user's profile
- Web notifications, camera, microphone, geolocation, and screen capture
  denied by default

## Requirements

- Windows 10 or later (64-bit recommended)
- Python 3.8 or newer
- PyQt5 5.15 or newer
- PyQtWebEngine 5.15 or newer

## Development setup

```powershell
git clone https://github.com/EriRJorge/Type_Browser.git
cd Type_Browser
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python TypeBrowser.py
```

If PowerShell execution policy prevents activation, run the interpreter
directly with `.venv\Scripts\python.exe TypeBrowser.py`.

## Building for Windows

Build a standalone executable with:

```powershell
python build_robust.py
```

The Inno Setup definition in `Type_Browser.iss` can package the resulting
`dist\Type_Browser.exe` into an installer. Test the executable on a clean
Windows machine before distributing it.

## Keyboard shortcuts

| Shortcut | Action |
| --- | --- |
| `Ctrl+T` | New tab |
| `Ctrl+W` | Close tab |
| `Ctrl+L` | Focus address bar |
| `Ctrl+R` | Reload |
| `Ctrl+B` | Toggle bookmark |
| `Ctrl+H` | History |
| `Ctrl+,` | Settings |
| `Ctrl+F` | Find in page |
| `Ctrl++` / `Ctrl+-` / `Ctrl+0` | Zoom in / out / reset |
| `Alt+Left` / `Alt+Right` | Back / forward |
| `F11` | Toggle fullscreen |
| `Ctrl+Q` | Exit |

## User data

Bookmarks, history, and settings are stored in `.type_browser` in the user's
home directory. Chromium cache and persistent web storage are kept separately
so browsing data survives application updates.

## License

This project is licensed under the [MIT License](LICENSE.txt).
