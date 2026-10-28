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

- Windows 10 or later, macOS 11 or later, or a modern 64-bit Linux distribution
- Python 3.8 or newer
- PyQt5 5.15 or newer
- PyQtWebEngine 5.15 or newer

## Development setup

```text
git clone https://github.com/EriRJorge/Type_Browser.git
cd Type_Browser
python -m venv .venv
# Windows PowerShell:
.venv\Scripts\Activate.ps1
# macOS/Linux:
# source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python TypeBrowser.py
```

If activation is unavailable, run the virtual environment's Python
interpreter directly. PyQt5 and PyQtWebEngine provide native Qt WebEngine
packages for each supported operating system.

## Building a standalone application

PyInstaller must be run on the operating system being packaged. The shared
specification can build a native application on Windows, macOS, or Linux:

```text
python -m PyInstaller Type_Browser_robust.spec --noconfirm --clean
```

The output is written to `dist` with the native application format for that
platform (`.exe` on Windows, an application bundle on macOS, and an executable
on Linux). The repository's GitHub Actions workflow builds all three targets
on their native runners.

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
