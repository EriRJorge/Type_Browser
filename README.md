# Type Browser

A lightweight, privacy-focused personal web browser built with Python and PyQt5.

## Features

- Modern and clean user interface
- Tabbed browsing
- Bookmarks management
- Browsing history
- Download manager
- Settings and preferences
- Dark/Light theme support
- Keyboard shortcuts
- Context menu
- Full-screen mode
- Zoom controls
- Find in page
- Save page as
- View page source
- Inspect element

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Type_Browser.git
cd Type_Browser
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the browser:
```bash
python TypeBrowser.py
```

### Keyboard Shortcuts

- `Ctrl+T`: New tab
- `Ctrl+W`: Close tab
- `Ctrl+R`: Reload page
- `Ctrl+L`: Focus URL bar
- `Ctrl+B`: Toggle bookmark
- `Ctrl+H`: Show history
- `Ctrl+,`: Show settings
- `Ctrl+F`: Find in page
- `Ctrl++`: Zoom in
- `Ctrl+-`: Zoom out
- `Ctrl+0`: Reset zoom
- `F11`: Toggle fullscreen
- `Ctrl+N`: New window
- `Ctrl+S`: Save page
- `Ctrl+Z`: Undo
- `Ctrl+Y`: Redo
- `Ctrl+X`: Cut
- `Ctrl+C`: Copy
- `Ctrl+V`: Paste
- `Alt+Left`: Back
- `Alt+Right`: Forward

## Data Storage

Browser data (bookmarks, history, settings) is stored in the following location:
- Windows: `%USERPROFILE%\.type_browser`
- Linux/Mac: `~/.type_browser`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**TypeBrowser** is a lightweight, privacy-focused web browser built with Python and PyQt5. It offers a user-friendly interface with tabbed browsing, navigation features, and a customizable home page. This project focuses on simplicity and privacy, providing basic web browsing functionalities with minimal distractions.

## Features
- **Tabbed Browsing**: Open multiple websites in separate tabs.
- **Navigation Toolbar**: Includes back, forward, reload, and home buttons for easy navigation.
- **URL Bar**: A dynamic URL bar to display and navigate to websites.
- **Customizable Home Page**: Set a default homepage (Google is set by default).
- **Download Interception**: Placeholder functionality for handling download requests.
- **Permission Handling**: Simplified permissions for web page features (useful for handling media requests).
- **About Dialog**: Display information about the app, including its version and a brief description.

## Installation
To run this application, you need Python 3.x and the following libraries:

- PyQt5
- PyQtWebEngine

### Step-by-step installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TypeBrowser.git
   ```

2. Install the dependencies:
   ```bash
   pip install PyQt5 PyQtWebEngine
   ```

3. Run the application:
   ```bash
   python type_browser.py
   ```

## Usage
- **New Tab**: Open a new tab using the **Ctrl+T** keyboard shortcut.
- **Close Tab**: Close the current tab with **Ctrl+W**.
- **Navigate**: Type a URL in the address bar and press **Enter** to navigate to it.
- **Back/Forward**: Use the back and forward buttons to navigate through your browsing history.
- **Reload**: Reload the current page using **Ctrl+R** or the reload button.

## Keyboard Shortcuts
- **Ctrl+T**: Open a new tab.
- **Ctrl+W**: Close the current tab.
- **Ctrl+R**: Reload the current page.
- **Ctrl+Q**: Exit the browser.

 
