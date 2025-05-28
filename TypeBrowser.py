#Type_Browser.py
# First Type_Software Project
#Eri R Jorge
#3/6/2025 - Project started
#3/6/2025 - Added the main window and tabbed browsing, added navigation toolbar and menu bar with basic actions and shortcuts
#3/8/2025 - Fixed tab functionality and improved visual styling, Added Keep Alive Features



import sys
import os
from PyQt5.QtCore import QUrl, Qt, QSize, QTimer, QSettings
from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar, QAction, 
                            QLineEdit, QTabWidget, QWidget, QVBoxLayout, 
                            QShortcut, QMenu, QDialog, QLabel, QVBoxLayout, 
                            QPushButton, QHBoxLayout, QFileDialog, QMessageBox,
                            QStatusBar, QFrame, QMenuBar, QInputDialog)
from PyQt5.QtGui import QIcon, QKeySequence, QFont, QColor, QPalette
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineProfile, QWebEngineSettings
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor
from browser_data import BrowserData
from settings_dialog import SettingsDialog
from download_manager import DownloadManager
from about_dialog import AboutDialog
from bookmark_manager import BookmarkDialog
from shortcuts_dialog import ShortcutsDialog

VERSION = "1.1.0"
APP_NAME = "Type_Browser"

class DownloadInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.download_path = os.path.expanduser("~/Downloads")

    def interceptRequest(self, info):
        if info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeMainFrame:
            # Handle main frame requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeSubFrame:
            # Handle sub-frame requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeStylesheet:
            # Handle stylesheet requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeScript:
            # Handle script requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeImage:
            # Handle image requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeFontResource:
            # Handle font requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeSubResource:
            # Handle sub-resource requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeObject:
            # Handle object requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeMedia:
            # Handle media requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeWorker:
            # Handle worker requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeSharedWorker:
            # Handle shared worker requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypePrefetch:
            # Handle prefetch requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeFavicon:
            # Handle favicon requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeXHR:
            # Handle XHR requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypePing:
            # Handle ping requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeServiceWorker:
            # Handle service worker requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeCSPReport:
            # Handle CSP report requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypePluginResource:
            # Handle plugin resource requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeNavigationPreloadMainFrame:
            # Handle navigation preload main frame requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeNavigationPreloadSubFrame:
            # Handle navigation preload sub-frame requests
            pass
        elif info.resourceType() == QWebEngineUrlRequestInterceptor.ResourceTypeOther:
            # Handle other requests
            pass

class WebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.featurePermissionRequested.connect(self.handlePermissionRequest)
        
        # Enable modern web features
        settings = self.settings()
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        settings.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
        settings.setAttribute(QWebEngineSettings.JavascriptCanAccessClipboard, True)
        settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        settings.setAttribute(QWebEngineSettings.WebGLEnabled, True)
        settings.setAttribute(QWebEngineSettings.Accelerated2dCanvasEnabled, True)
        settings.setAttribute(QWebEngineSettings.AutoLoadImages, True)
        settings.setAttribute(QWebEngineSettings.ErrorPageEnabled, True)
        settings.setAttribute(QWebEngineSettings.FocusOnNavigationEnabled, True)
        settings.setAttribute(QWebEngineSettings.HyperlinkAuditingEnabled, True)
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
        settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
        settings.setAttribute(QWebEngineSettings.ScreenCaptureEnabled, True)
        settings.setAttribute(QWebEngineSettings.ShowScrollBars, True)
        settings.setAttribute(QWebEngineSettings.SpatialNavigationEnabled, True)
        settings.setAttribute(QWebEngineSettings.LinksIncludedInFocusChain, True)
        settings.setAttribute(QWebEngineSettings.AllowGeolocationOnInsecureOrigins, True)
        settings.setAttribute(QWebEngineSettings.AllowRunningInsecureContent, False)
        settings.setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)  # Enable fullscreen support
        
        # Set modern user agent
        self.profile().setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    
    def handlePermissionRequest(self, url, feature):
        # Handle various permission requests
        if feature == QWebEnginePage.Feature.Geolocation:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)
        elif feature == QWebEnginePage.Feature.MediaAudioCapture:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)
        elif feature == QWebEnginePage.Feature.MediaVideoCapture:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)
        elif feature == QWebEnginePage.Feature.MediaAudioVideoCapture:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)
        elif feature == QWebEnginePage.Feature.MouseLock:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)
        elif feature == QWebEnginePage.Feature.DesktopVideoCapture:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)
        elif feature == QWebEnginePage.Feature.DesktopAudioVideoCapture:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)
        elif feature == QWebEnginePage.Feature.Notifications:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)
        else:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)

class WebView(QWebEngineView):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.page = WebPage(self)
        self.setPage(self.page)
        
        # Add context menu
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)
        
        # Handle new window requests
        self.page.createWindow = self.handle_new_window
        
        # Handle fullscreen requests
        self.page.fullScreenRequested.connect(self.handle_fullscreen_request)
        
    def handle_fullscreen_request(self, request):
        if request.toggleOn():
            self.main_window.showFullScreen()
            request.accept()
        else:
            self.main_window.showNormal()
            request.accept()
        
    def handle_new_window(self, windowType):
        # Handle new window requests (e.g., target="_blank" links)
        if windowType == QWebEnginePage.WebBrowserTab and self.main_window:
            new_view = self.main_window.add_new_tab()
            return new_view.page
        return None
        
    def show_context_menu(self, pos):
        menu = QMenu()
        
        # Add context menu items
        back_action = menu.addAction("Back")
        forward_action = menu.addAction("Forward")
        reload_action = menu.addAction("Reload")
        menu.addSeparator()
        
        copy_action = menu.addAction("Copy")
        paste_action = menu.addAction("Paste")
        select_all_action = menu.addAction("Select All")
        menu.addSeparator()
        
        save_page_action = menu.addAction("Save Page As...")
        view_source_action = menu.addAction("View Page Source")
        inspect_action = menu.addAction("Inspect Element")
        
        # Show menu and handle actions
        action = menu.exec_(self.mapToGlobal(pos))
        if action == back_action:
            self.back()
        elif action == forward_action:
            self.forward()
        elif action == reload_action:
            self.reload()
        elif action == copy_action:
            self.page().triggerAction(QWebEnginePage.Copy)
        elif action == paste_action:
            self.page().triggerAction(QWebEnginePage.Paste)
        elif action == select_all_action:
            self.page().triggerAction(QWebEnginePage.SelectAll)
        elif action == save_page_action:
            self.page().triggerAction(QWebEnginePage.SavePage)
        elif action == view_source_action:
            self.page().triggerAction(QWebEnginePage.ViewSource)
        elif action == inspect_action:
            self.page().triggerAction(QWebEnginePage.InspectElement)

class BrowserTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.main_window = parent
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        self.webview = WebView(self.main_window)
        self.layout.addWidget(self.webview)
        self.setLayout(self.layout)
        
        # Connect signals
        self.webview.titleChanged.connect(self.on_title_changed)
        self.webview.urlChanged.connect(self.on_url_changed)
        
    def navigate(self, url):
        if isinstance(url, QUrl):
            url = url.toString()
            
        url_str = str(url)
        
        # If it's the default URL, load it directly
        if url_str == "https://typesearch.click/":
            self.webview.load(QUrl(url_str))
            return
            
        # For other URLs, handle search and protocol
        if not url_str.startswith('http'):
            if '.' in url_str and ' ' not in url_str:
                url_str = 'https://' + url_str
            elif url_str and url_str != "False":  # Only add search query if not empty and not "False"
                url_str = f'https://www.google.com/search?q={url_str}'
            else:
                url_str = "https://typesearch.click/"
        
        self.webview.load(QUrl(url_str))
        
    def refresh(self):
        self.webview.reload()
        
    def back(self):
        self.webview.back()
    
    def forward(self):
        self.webview.forward()
        
    def stop(self):
        self.webview.stop()
        
    def current_url(self):
        return self.webview.url().toString()
        
    def on_title_changed(self, title):
        if self.main_window:
            self.main_window.update_tab_title(self, title)
            
    def on_url_changed(self, url):
        if self.main_window:
            self.main_window.update_urlbar(url, self)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon("icon.png"))
        self.setMinimumSize(1024, 768)
        
        # Initialize browser data
        self.browser_data = BrowserData()
        
        # Initialize download manager
        self.download_manager = DownloadManager(self)
        
        # Set application style
        self.apply_style()
        
        # Initialize UI components
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.tab_changed)
        self.tabs.setDocumentMode(True)
        
        # Remove the corner widget (new tab button)
        self.tabs.setCornerWidget(None)
        
        self.setCentralWidget(self.tabs)
        
        # Navigation toolbar
        self.nav_toolbar = self.create_navigation_toolbar()
        
        # Create menubar
        self.menu_bar = self.create_menu()
        
        # Create status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        # Set up keyboard shortcuts
        self.setup_shortcuts()
        
        # Add homepage tab
        self.add_new_tab()
        
        # Center the window on screen
        self.center_on_screen()

    def showFullScreen(self):
        # Hide UI elements in fullscreen
        self.menu_bar.hide()
        self.nav_toolbar.hide()
        self.statusBar.hide()
        self.tabs.tabBar().hide()  # Completely hide the tab bar
        super().showFullScreen()

    def showNormal(self):
        # Show UI elements when exiting fullscreen
        self.menu_bar.show()
        self.nav_toolbar.show()
        self.statusBar.show()
        self.tabs.tabBar().show()  # Show the tab bar again
        super().showNormal()

    def setup_shortcuts(self):
        # Tab navigation
        QShortcut(QKeySequence("Ctrl+Tab"), self, self.next_tab)
        QShortcut(QKeySequence("Ctrl+Shift+Tab"), self, self.previous_tab)
        
        # Escape key to exit fullscreen
        QShortcut(QKeySequence("Escape"), self, self.exit_fullscreen)

    def exit_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
            
    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def create_menu(self):
        menu_bar = self.menuBar()
        
        # File Menu
        file_menu = menu_bar.addMenu("File")
        
        new_tab_action = QAction("New Tab", self)
        new_tab_action.setShortcut("Ctrl+T")
        new_tab_action.triggered.connect(self.add_new_tab)
        file_menu.addAction(new_tab_action)
        
        new_window_action = QAction("New Window", self)
        new_window_action.setShortcut("Ctrl+N")
        new_window_action.triggered.connect(self.new_window)
        file_menu.addAction(new_window_action)
        
        close_tab_action = QAction("Close Tab", self)
        close_tab_action.setShortcut("Ctrl+W")
        close_tab_action.triggered.connect(self.close_current_tab)
        file_menu.addAction(close_tab_action)
        
        file_menu.addSeparator()
        
        save_page_action = QAction("Save Page As...", self)
        save_page_action.setShortcut("Ctrl+S")
        save_page_action.triggered.connect(self.save_page)
        file_menu.addAction(save_page_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit Menu
        edit_menu = menu_bar.addMenu("Edit")
        
        undo_action = QAction("Undo", self)
        undo_action.setShortcut("Ctrl+Z")
        undo_action.triggered.connect(self.undo)
        edit_menu.addAction(undo_action)
        
        redo_action = QAction("Redo", self)
        redo_action.setShortcut("Ctrl+Y")
        redo_action.triggered.connect(self.redo)
        edit_menu.addAction(redo_action)
        
        edit_menu.addSeparator()
        
        cut_action = QAction("Cut", self)
        cut_action.setShortcut("Ctrl+X")
        cut_action.triggered.connect(self.cut)
        edit_menu.addAction(cut_action)
        
        copy_action = QAction("Copy", self)
        copy_action.setShortcut("Ctrl+C")
        copy_action.triggered.connect(self.copy)
        edit_menu.addAction(copy_action)
        
        paste_action = QAction("Paste", self)
        paste_action.setShortcut("Ctrl+V")
        paste_action.triggered.connect(self.paste)
        edit_menu.addAction(paste_action)
        
        edit_menu.addSeparator()
        
        find_action = QAction("Find", self)
        find_action.setShortcut("Ctrl+F")
        find_action.triggered.connect(self.find_in_page)
        edit_menu.addAction(find_action)
        
        # View Menu
        view_menu = menu_bar.addMenu("View")
        
        zoom_in_action = QAction("Zoom In", self)
        zoom_in_action.setShortcut("Ctrl++")
        zoom_in_action.triggered.connect(self.zoom_in)
        view_menu.addAction(zoom_in_action)
        
        zoom_out_action = QAction("Zoom Out", self)
        zoom_out_action.setShortcut("Ctrl+-")
        zoom_out_action.triggered.connect(self.zoom_out)
        view_menu.addAction(zoom_out_action)
        
        zoom_reset_action = QAction("Reset Zoom", self)
        zoom_reset_action.setShortcut("Ctrl+0")
        zoom_reset_action.triggered.connect(self.zoom_reset)
        view_menu.addAction(zoom_reset_action)
        
        view_menu.addSeparator()
        
        fullscreen_action = QAction("Full Screen", self)
        fullscreen_action.setShortcut("F11")
        fullscreen_action.triggered.connect(self.toggle_fullscreen)
        view_menu.addAction(fullscreen_action)
        
        # History Menu
        history_menu = menu_bar.addMenu("History")
        
        back_action = QAction("Back", self)
        back_action.setShortcut("Alt+Left")
        back_action.triggered.connect(self.navigate_back)
        history_menu.addAction(back_action)
        
        forward_action = QAction("Forward", self)
        forward_action.setShortcut("Alt+Right")
        forward_action.triggered.connect(self.navigate_forward)
        history_menu.addAction(forward_action)
        
        history_menu.addSeparator()
        
        show_history_action = QAction("Show History", self)
        show_history_action.setShortcut("Ctrl+H")
        show_history_action.triggered.connect(self.show_history)
        history_menu.addAction(show_history_action)
        
        # Bookmarks Menu
        bookmarks_menu = menu_bar.addMenu("Bookmarks")
        
        add_bookmark_action = QAction("Add Bookmark", self)
        add_bookmark_action.setShortcut("Ctrl+B")
        add_bookmark_action.triggered.connect(self.toggle_bookmark)
        bookmarks_menu.addAction(add_bookmark_action)
        
        show_bookmarks_action = QAction("Show Bookmarks", self)
        show_bookmarks_action.triggered.connect(self.show_bookmarks)
        bookmarks_menu.addAction(show_bookmarks_action)
        
        # Tools Menu
        tools_menu = menu_bar.addMenu("Tools")
        
        settings_action = QAction("Settings", self)
        settings_action.setShortcut("Ctrl+,")
        settings_action.triggered.connect(self.show_settings)
        tools_menu.addAction(settings_action)
        
        show_downloads_action = QAction("Downloads", self)
        show_downloads_action.setShortcut("Ctrl+J")
        show_downloads_action.triggered.connect(self.show_downloads)
        tools_menu.addAction(show_downloads_action)
        
        tools_menu.addSeparator()
        
        shortcuts_action = QAction("Keyboard Shortcuts", self)
        shortcuts_action.triggered.connect(self.show_shortcuts)
        tools_menu.addAction(shortcuts_action)
        
        # Help Menu
        help_menu = menu_bar.addMenu("Help")
        
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)
        
        return menu_bar

    def new_window(self):
        # Create a new browser window
        window = MainWindow()
        window.show()

    def save_page(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.page().triggerAction(QWebEnginePage.SavePage)

    def undo(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.page().triggerAction(QWebEnginePage.Undo)

    def redo(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.page().triggerAction(QWebEnginePage.Redo)

    def cut(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.page().triggerAction(QWebEnginePage.Cut)

    def copy(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.page().triggerAction(QWebEnginePage.Copy)

    def paste(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.page().triggerAction(QWebEnginePage.Paste)

    def find_in_page(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.page().triggerAction(QWebEnginePage.Find)

    def zoom_in(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.setZoomFactor(
                self.tabs.currentWidget().webview.zoomFactor() + 0.1
            )

    def zoom_out(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.setZoomFactor(
                self.tabs.currentWidget().webview.zoomFactor() - 0.1
            )

    def zoom_reset(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.setZoomFactor(1.0)

    def toggle_fullscreen(self):
        if self.isFullScreen():
            self.showNormal()
        else:
            self.showFullScreen()

    def toggle_bookmark(self):
        if self.tabs.currentWidget():
            current_url = self.tabs.currentWidget().current_url()
            current_title = self.tabs.currentWidget().webview.title()
            
            # Check if already bookmarked
            for bookmark in self.browser_data.bookmarks:
                if bookmark["url"] == current_url:
                    self.browser_data.remove_bookmark(current_url)
                    self.statusBar.showMessage("Bookmark removed", 3000)
                    return
            
            # Add new bookmark
            self.browser_data.add_bookmark(current_title, current_url)
            self.statusBar.showMessage("Bookmark added", 3000)

    def show_bookmarks(self):
        dialog = BookmarkDialog(self.browser_data, self)
        dialog.exec_()

    def show_history(self):
        dialog = QDialog(self)
        dialog.setWindowTitle("History")
        dialog.setMinimumSize(400, 300)
        
        layout = QVBoxLayout()
        
        # Create list widget for history
        from PyQt5.QtWidgets import QListWidget
        list_widget = QListWidget()
        
        for history_item in self.browser_data.history:
            list_widget.addItem(f"{history_item['title']} - {history_item['url']}")
        
        layout.addWidget(list_widget)
        
        # Add buttons
        button_layout = QHBoxLayout()
        open_button = QPushButton("Open")
        clear_button = QPushButton("Clear History")
        close_button = QPushButton("Close")
        
        open_button.clicked.connect(lambda: self.open_history_item(list_widget.currentRow()))
        clear_button.clicked.connect(self.clear_history)
        close_button.clicked.connect(dialog.accept)
        
        button_layout.addWidget(open_button)
        button_layout.addWidget(clear_button)
        button_layout.addWidget(close_button)
        
        layout.addLayout(button_layout)
        dialog.setLayout(layout)
        dialog.exec_()

    def open_history_item(self, index):
        if index >= 0 and index < len(self.browser_data.history):
            history_item = self.browser_data.history[index]
            self.add_new_tab(history_item["url"])

    def clear_history(self):
        reply = QMessageBox.question(self, 'Clear History',
                                   "Are you sure you want to clear all history?",
                                   QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.browser_data.clear_history()
            self.show_history()  # Refresh the dialog

    def show_settings(self):
        dialog = SettingsDialog(self.browser_data, self)
        if dialog.exec_() == QDialog.Accepted:
            # Apply settings
            self.apply_settings()

    def show_downloads(self):
        self.download_manager.show()

    def show_about_dialog(self):
        dialog = AboutDialog(self)
        dialog.exec_()

    def apply_settings(self):
        # Apply theme
        theme = self.browser_data.get_setting("theme", "light")
        if theme == "dark":
            self.setStyleSheet("""
                QMainWindow {
                    background-color: rgba(18, 18, 18, 0.85);
                }
                QTabWidget::pane {
                    border: none;
                    background-color: rgba(30, 30, 30, 0.75);
                    border-radius: 16px;
                    border: 1px solid rgba(255, 255, 255, 0.15);
                }
                QTabWidget::tab-bar {
                    alignment: left;
                    background-color: transparent;
                    left: 8px;
                }
                QTabBar::tab {
                    background-color: rgba(30, 30, 30, 0.75);
                    color: rgba(255, 255, 255, 0.9);
                    padding: 8px 20px;
                    margin-right: 2px;
                    border-top-left-radius: 16px;
                    border-top-right-radius: 16px;
                    min-width: 120px;
                    max-width: 200px;
                    border: 1px solid rgba(255, 255, 255, 0.15);
                    border-bottom: none;
                }
                QTabBar::tab:selected {
                    background-color: rgba(45, 45, 45, 0.85);
                    border-bottom: 2px solid rgba(13, 110, 253, 0.9);
                    color: #ffffff;
                }
                QTabBar::tab:hover {
                    background-color: rgba(40, 40, 40, 0.85);
                }
                QTabBar::close-button {
                    image: none;
                    background: transparent;
                    border: none;
                    margin: 2px;
                    padding: 2px;
                    border-radius: 4px;
                    color: rgba(255, 255, 255, 0.6);
                    font-family: "Segoe UI";
                    font-size: 12px;
                    font-weight: bold;
                    min-width: 16px;
                    max-width: 16px;
                    min-height: 16px;
                    max-height: 16px;
                }
                QTabBar::close-button::after {
                    content: "×";
                }
                QTabBar::close-button:hover {
                    background-color: rgba(255, 255, 255, 0.1);
                    color: #ffffff;
                }
                QTabBar::close-button:pressed {
                    background-color: rgba(255, 255, 255, 0.15);
                    color: rgba(13, 110, 253, 0.9);
                }
                QToolBar {
                    background-color: rgba(30, 30, 30, 0.75);
                    border-bottom: 1px solid rgba(255, 255, 255, 0.15);
                    spacing: 8px;
                    padding: 8px;
                    border-radius: 16px;
                    margin: 4px;
                    border: 1px solid rgba(255, 255, 255, 0.15);
                }
                QToolButton {
                    background-color: transparent;
                    border: none;
                    padding: 8px;
                    border-radius: 12px;
                    color: rgba(255, 255, 255, 0.9);
                    font-size: 14px;
                }
                QToolButton:hover {
                    background-color: rgba(255, 255, 255, 0.1);
                    color: rgba(13, 110, 253, 0.9);
                }
                QToolButton:pressed {
                    background-color: rgba(255, 255, 255, 0.15);
                }
                QAction {
                    color: rgba(255, 255, 255, 0.9);
                    font-size: 14px;
                    padding: 8px;
                    border-radius: 12px;
                }
                QAction:hover {
                    background-color: rgba(255, 255, 255, 0.1);
                    color: rgba(13, 110, 253, 0.9);
                }
                QAction:pressed {
                    background-color: rgba(255, 255, 255, 0.15);
                }
                QLineEdit {
                    padding: 10px;
                    border: 1px solid rgba(255, 255, 255, 0.15);
                    border-radius: 16px;
                    background-color: rgba(30, 30, 30, 0.75);
                    color: #ffffff;
                    selection-background-color: rgba(13, 110, 253, 0.9);
                    selection-color: #ffffff;
                    font-size: 13px;
                }
                QLineEdit:focus {
                    border: 2px solid rgba(13, 110, 253, 0.9);
                    padding: 9px;
                }
                QStatusBar {
                    background-color: rgba(18, 18, 18, 0.85);
                    color: rgba(255, 255, 255, 0.7);
                    border-top: 1px solid rgba(255, 255, 255, 0.15);
                    padding: 4px;
                }
                QMenu {
                    background-color: rgba(30, 30, 30, 0.75);
                    border: 1px solid rgba(255, 255, 255, 0.15);
                    border-radius: 16px;
                    padding: 8px;
                }
                QMenu::item {
                    padding: 8px 24px;
                    border-radius: 12px;
                    margin: 2px 4px;
                    color: rgba(255, 255, 255, 0.9);
                }
                QMenu::item:selected {
                    background-color: rgba(255, 255, 255, 0.1);
                    color: rgba(13, 110, 253, 0.9);
                }
                QMenu::separator {
                    height: 1px;
                    background-color: rgba(255, 255, 255, 0.15);
                    margin: 6px 8px;
                }
                QPushButton {
                    background-color: rgba(13, 110, 253, 0.9);
                    color: #ffffff;
                    border: none;
                    padding: 8px 16px;
                    border-radius: 12px;
                    font-weight: 500;
                }
                QPushButton:hover {
                    background-color: rgba(13, 110, 253, 0.95);
                }
                QPushButton:pressed {
                    background-color: rgba(13, 110, 253, 1);
                }
                QPushButton:disabled {
                    background-color: rgba(108, 117, 125, 0.75);
                    color: rgba(255, 255, 255, 0.5);
                }
                QScrollBar:vertical {
                    border: none;
                    background-color: transparent;
                    width: 10px;
                    margin: 0px;
                }
                QScrollBar::handle:vertical {
                    background-color: rgba(255, 255, 255, 0.2);
                    border-radius: 5px;
                    min-height: 20px;
                    margin: 2px;
                }
                QScrollBar::handle:vertical:hover {
                    background-color: rgba(255, 255, 255, 0.3);
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    height: 0px;
                }
                QScrollBar:horizontal {
                    border: none;
                    background-color: transparent;
                    height: 10px;
                    margin: 0px;
                }
                QScrollBar::handle:horizontal {
                    background-color: rgba(255, 255, 255, 0.2);
                    border-radius: 5px;
                    min-width: 20px;
                    margin: 2px;
                }
                QScrollBar::handle:horizontal:hover {
                    background-color: rgba(255, 255, 255, 0.3);
                }
                QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                    width: 0px;
                }
                QMenuBar {
                    background-color: rgba(30, 30, 30, 0.75);
                    color: rgba(255, 255, 255, 0.9);
                    border-bottom: 1px solid rgba(255, 255, 255, 0.15);
                    padding: 4px;
                }
                QMenuBar::item {
                    background-color: transparent;
                    padding: 6px 12px;
                    border-radius: 12px;
                    margin: 2px;
                }
                QMenuBar::item:selected {
                    background-color: rgba(255, 255, 255, 0.1);
                }
                QMenuBar::item:pressed {
                    background-color: rgba(255, 255, 255, 0.15);
                }
                QDialog {
                    background-color: rgba(30, 30, 30, 0.75);
                    border-radius: 16px;
                    border: 1px solid rgba(255, 255, 255, 0.15);
                }
                QLabel {
                    color: rgba(255, 255, 255, 0.9);
                }
                QCheckBox {
                    color: rgba(255, 255, 255, 0.9);
                    spacing: 8px;
                }
                QCheckBox::indicator {
                    width: 18px;
                    height: 18px;
                    border-radius: 4px;
                    border: 1px solid rgba(255, 255, 255, 0.15);
                }
                QCheckBox::indicator:checked {
                    background-color: rgba(13, 110, 253, 0.9);
                    border: 1px solid rgba(13, 110, 253, 0.9);
                }
                QComboBox {
                    background-color: rgba(30, 30, 30, 0.75);
                    border: 1px solid rgba(255, 255, 255, 0.15);
                    border-radius: 12px;
                    padding: 6px;
                    color: rgba(255, 255, 255, 0.9);
                    min-width: 6em;
                }
                QComboBox:hover {
                    border: 1px solid rgba(13, 110, 253, 0.9);
                }
                QComboBox::drop-down {
                    border: none;
                    width: 20px;
                }
                QComboBox::down-arrow {
                    image: none;
                    border: none;
                }
            """)
        else:
            self.apply_style()  # Apply light theme

        # Apply other settings
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.setZoomFactor(
                self.browser_data.get_setting("zoom_level", 100) / 100
            )

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Confirm Exit',
                                   "Are you sure you want to quit?",
                                   QMessageBox.Yes | QMessageBox.No,
                                   QMessageBox.No)
        if reply == QMessageBox.Yes:
            # Clear history if setting is enabled
            if self.browser_data.get_setting("clear_history_on_exit", False):
                self.browser_data.clear_history()
            event.accept()
        else:
            event.ignore()

    def apply_style(self):
        # Set application font
        app_font = QFont("Segoe UI", 10)
        QApplication.setFont(app_font)
        
        # Set global stylesheet with true glassmorphic style
        self.setStyleSheet("""
            QMainWindow {
                background-color: rgba(18, 18, 18, 0.85);
            }
            
            QTabWidget::pane {
                border: none;
                background-color: rgba(30, 30, 30, 0.75);
                border-radius: 16px;
                border: 1px solid rgba(255, 255, 255, 0.15);
            }
            
            QTabWidget::tab-bar {
                alignment: left;
                background-color: transparent;
                left: 8px;
            }
            
            QTabBar::tab {
                background-color: rgba(30, 30, 30, 0.75);
                color: rgba(255, 255, 255, 0.9);
                padding: 8px 20px;
                margin-right: 2px;
                border-top-left-radius: 16px;
                border-top-right-radius: 16px;
                min-width: 120px;
                max-width: 200px;
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-bottom: none;
            }
            
            QTabBar::tab:selected {
                background-color: rgba(45, 45, 45, 0.85);
                border-bottom: 2px solid rgba(13, 110, 253, 0.9);
                color: #ffffff;
            }
            
            QTabBar::tab:hover {
                background-color: rgba(40, 40, 40, 0.85);
            }

            QTabBar::close-button {
                image: none;
                background: transparent;
                border: none;
                margin: 2px;
                padding: 2px;
                border-radius: 4px;
                color: rgba(255, 255, 255, 0.6);
                font-family: "Segoe UI";
                font-size: 12px;
                font-weight: bold;
                min-width: 16px;
                max-width: 16px;
                min-height: 16px;
                max-height: 16px;
            }

            QTabBar::close-button::after {
                content: "×";
            }

            QTabBar::close-button:hover {
                background-color: rgba(255, 255, 255, 0.1);
                color: #ffffff;
            }

            QTabBar::close-button:pressed {
                background-color: rgba(255, 255, 255, 0.15);
                color: rgba(13, 110, 253, 0.9);
            }
            
            QToolBar {
                background-color: rgba(30, 30, 30, 0.75);
                border-bottom: 1px solid rgba(255, 255, 255, 0.15);
                spacing: 8px;
                padding: 8px;
                border-radius: 16px;
                margin: 4px;
                border: 1px solid rgba(255, 255, 255, 0.15);
            }
            
            QToolButton {
                background-color: transparent;
                border: none;
                padding: 8px;
                border-radius: 12px;
                color: rgba(255, 255, 255, 0.9);
                font-size: 14px;
            }
            
            QToolButton:hover {
                background-color: rgba(255, 255, 255, 0.1);
                color: rgba(13, 110, 253, 0.9);
            }
            
            QToolButton:pressed {
                background-color: rgba(255, 255, 255, 0.15);
            }

            QAction {
                color: rgba(255, 255, 255, 0.9);
                font-size: 14px;
                padding: 8px;
                border-radius: 12px;
            }

            QAction:hover {
                background-color: rgba(255, 255, 255, 0.1);
                color: rgba(13, 110, 253, 0.9);
            }

            QAction:pressed {
                background-color: rgba(255, 255, 255, 0.15);
            }
            
            QLineEdit {
                padding: 10px;
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 16px;
                background-color: rgba(30, 30, 30, 0.75);
                color: #ffffff;
                selection-background-color: rgba(13, 110, 253, 0.9);
                selection-color: #ffffff;
                font-size: 13px;
            }
            
            QLineEdit:focus {
                border: 2px solid rgba(13, 110, 253, 0.9);
                padding: 9px;
            }
            
            QStatusBar {
                background-color: rgba(18, 18, 18, 0.85);
                color: rgba(255, 255, 255, 0.7);
                border-top: 1px solid rgba(255, 255, 255, 0.15);
                padding: 4px;
            }
            
            QMenu {
                background-color: rgba(30, 30, 30, 0.75);
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 16px;
                padding: 8px;
            }
            
            QMenu::item {
                padding: 8px 24px;
                border-radius: 12px;
                margin: 2px 4px;
                color: rgba(255, 255, 255, 0.9);
            }
            
            QMenu::item:selected {
                background-color: rgba(255, 255, 255, 0.1);
                color: rgba(13, 110, 253, 0.9);
            }
            
            QMenu::separator {
                height: 1px;
                background-color: rgba(255, 255, 255, 0.15);
                margin: 6px 8px;
            }
            
            QPushButton {
                background-color: rgba(13, 110, 253, 0.9);
                color: #ffffff;
                border: none;
                padding: 8px 16px;
                border-radius: 12px;
                font-weight: 500;
            }
            
            QPushButton:hover {
                background-color: rgba(13, 110, 253, 0.95);
            }
            
            QPushButton:pressed {
                background-color: rgba(13, 110, 253, 1);
            }
            
            QPushButton:disabled {
                background-color: rgba(108, 117, 125, 0.75);
                color: rgba(255, 255, 255, 0.5);
            }
            
            QScrollBar:vertical {
                border: none;
                background-color: transparent;
                width: 10px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background-color: rgba(255, 255, 255, 0.2);
                border-radius: 5px;
                min-height: 20px;
                margin: 2px;
            }
            
            QScrollBar::handle:vertical:hover {
                background-color: rgba(255, 255, 255, 0.3);
            }
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            
            QScrollBar:horizontal {
                border: none;
                background-color: transparent;
                height: 10px;
                margin: 0px;
            }
            
            QScrollBar::handle:horizontal {
                background-color: rgba(255, 255, 255, 0.2);
                border-radius: 5px;
                min-width: 20px;
                margin: 2px;
            }
            
            QScrollBar::handle:horizontal:hover {
                background-color: rgba(255, 255, 255, 0.3);
            }
            
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                width: 0px;
            }

            QMenuBar {
                background-color: rgba(30, 30, 30, 0.75);
                color: rgba(255, 255, 255, 0.9);
                border-bottom: 1px solid rgba(255, 255, 255, 0.15);
                padding: 4px;
            }

            QMenuBar::item {
                background-color: transparent;
                padding: 6px 12px;
                border-radius: 12px;
                margin: 2px;
            }

            QMenuBar::item:selected {
                background-color: rgba(255, 255, 255, 0.1);
            }

            QMenuBar::item:pressed {
                background-color: rgba(255, 255, 255, 0.15);
            }

            QDialog {
                background-color: rgba(30, 30, 30, 0.75);
                border-radius: 16px;
                border: 1px solid rgba(255, 255, 255, 0.15);
            }

            QLabel {
                color: rgba(255, 255, 255, 0.9);
            }

            QCheckBox {
                color: rgba(255, 255, 255, 0.9);
                spacing: 8px;
            }

            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 4px;
                border: 1px solid rgba(255, 255, 255, 0.15);
            }

            QCheckBox::indicator:checked {
                background-color: rgba(13, 110, 253, 0.9);
                border: 1px solid rgba(13, 110, 253, 0.9);
            }

            QComboBox {
                background-color: rgba(30, 30, 30, 0.75);
                border: 1px solid rgba(255, 255, 255, 0.15);
                border-radius: 12px;
                padding: 6px;
                color: rgba(255, 255, 255, 0.9);
                min-width: 6em;
            }

            QComboBox:hover {
                border: 1px solid rgba(13, 110, 253, 0.9);
            }

            QComboBox::drop-down {
                border: none;
                width: 20px;
            }

            QComboBox::down-arrow {
                image: none;
                border: none;
            }
        """)

    def create_navigation_toolbar(self):
        nav_toolbar = QToolBar("Navigation")
        nav_toolbar.setIconSize(QSize(20, 20))
        nav_toolbar.setMovable(False)
        self.addToolBar(nav_toolbar)
        
        # Create actions with better icons
        back_action = QAction("◀", self)
        back_action.setStatusTip("Go back to previous page")
        back_action.triggered.connect(self.navigate_back)
        nav_toolbar.addAction(back_action)
        
        forward_action = QAction("▶", self)
        forward_action.setStatusTip("Go forward to next page")
        forward_action.triggered.connect(self.navigate_forward)
        nav_toolbar.addAction(forward_action)
        
        reload_action = QAction("⟳", self)
        reload_action.setStatusTip("Reload current page")
        reload_action.triggered.connect(self.reload_page)
        nav_toolbar.addAction(reload_action)
        
        home_action = QAction("🏠", self)
        home_action.setStatusTip("Go to homepage")
        home_action.triggered.connect(self.navigate_home)
        nav_toolbar.addAction(home_action)
        
        # Add new tab button next to home icon
        new_tab_action = QAction("+", self)
        new_tab_action.setStatusTip("New Tab (Ctrl+T)")
        new_tab_action.triggered.connect(self.add_new_tab)
        nav_toolbar.addAction(new_tab_action)
        
        # Add some spacing
        spacer = QWidget()
        spacer.setFixedWidth(12)
        nav_toolbar.addWidget(spacer)
        
        # URL bar with better styling
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        self.urlbar.setPlaceholderText("Search or enter website name")
        self.urlbar.setMinimumHeight(36)
        nav_toolbar.addWidget(self.urlbar)
        
        return nav_toolbar

    def center_on_screen(self):
        # Center the window on the screen
        screen_geometry = QApplication.desktop().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())

    def close_tab(self, index):
        if self.tabs.count() > 1:
            # Get the tab widget before removing it
            tab = self.tabs.widget(index)
            if tab:
                # Clean up the webview
                tab.webview.stop()
                tab.webview.page.deleteLater()
                tab.webview.deleteLater()
                # Remove the tab
                self.tabs.removeTab(index)
        else:
            # If this is the last tab, create a new one before closing
            cur_index = self.tabs.currentIndex()
            self.add_new_tab()
            # Clean up the old tab
            old_tab = self.tabs.widget(cur_index)
            if old_tab:
                old_tab.webview.stop()
                old_tab.webview.page.deleteLater()
                old_tab.webview.deleteLater()
            self.tabs.removeTab(cur_index)
    
    def close_current_tab(self):
        self.close_tab(self.tabs.currentIndex())
    
    def tab_changed(self, index):
        if index >= 0 and self.tabs.count() > 0:
            tab = self.tabs.widget(index)
            if tab:
                url = tab.current_url()
                self.update_urlbar(QUrl(url), tab)
    
    def navigate_to_url(self):
        url = self.urlbar.text()
        if self.tabs.currentWidget():
            self.tabs.currentWidget().navigate(url)
    
    def navigate_back(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().back()
    
    def navigate_forward(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().forward()
    
    def reload_page(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().refresh()
    
    def navigate_home(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().navigate("https://typesearch.click/") 
    
    def focus_url_bar(self):
        self.urlbar.selectAll()
        self.urlbar.setFocus()

    def add_new_tab(self, url=None):
        # Always use typesearch.click as the default URL
        if url is None:
            url = "https://typesearch.click/"
            
        tab = BrowserTab(self)
        index = self.tabs.addTab(tab, "New Tab")
        self.tabs.setCurrentIndex(index)
        
        # Connect signals for title and URL updates
        tab.webview.titleChanged.connect(lambda title, browser_tab=tab: self.update_tab_title(browser_tab, title))
        tab.webview.urlChanged.connect(lambda qurl, browser_tab=tab: self.update_urlbar(qurl, browser_tab))
        tab.webview.loadStarted.connect(lambda: self.statusBar.showMessage("Loading..."))
        tab.webview.loadFinished.connect(lambda: self.statusBar.showMessage("Ready", 3000))
        
        # Now navigate to the URL
        tab.navigate(url)
        
        return tab.webview
    
    def update_tab_title(self, tab, title):
        index = self.tabs.indexOf(tab)
        if index >= 0:
            truncated_title = title[:20] + "..." if len(title) > 20 else title
            self.tabs.setTabText(index, truncated_title or "New Tab")
    
    def update_urlbar(self, url, tab=None):
        # Only update the URL bar if the tab is the current one
        if tab and self.tabs.currentWidget() == tab:
            self.urlbar.setText(url.toString())
            self.urlbar.setCursorPosition(0)

    def show_shortcuts(self):
        dialog = ShortcutsDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            # TODO: Apply the new shortcuts
            pass

    def next_tab(self):
        """Switch to the next tab"""
        current = self.tabs.currentIndex()
        if current < self.tabs.count() - 1:
            self.tabs.setCurrentIndex(current + 1)
        else:
            self.tabs.setCurrentIndex(0)  # Wrap around to first tab

    def previous_tab(self):
        """Switch to the previous tab"""
        current = self.tabs.currentIndex()
        if current > 0:
            self.tabs.setCurrentIndex(current - 1)
        else:
            self.tabs.setCurrentIndex(self.tabs.count() - 1)  # Wrap around to last tab

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def main():
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    
    # Set application icon
    app_icon = QIcon(resource_path("icon.png"))
    app.setWindowIcon(app_icon)
    
    # Set application style for all widgets
    app.setStyle("Fusion")
    
    # Configure global web engine settings
    settings = QWebEngineSettings.globalSettings()
    settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
    settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
    settings.setAttribute(QWebEngineSettings.JavascriptCanOpenWindows, True)
    settings.setAttribute(QWebEngineSettings.JavascriptCanAccessClipboard, True)
    settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
    settings.setAttribute(QWebEngineSettings.WebGLEnabled, True)
    settings.setAttribute(QWebEngineSettings.Accelerated2dCanvasEnabled, True)
    settings.setAttribute(QWebEngineSettings.AutoLoadImages, True)
    settings.setAttribute(QWebEngineSettings.ErrorPageEnabled, True)
    settings.setAttribute(QWebEngineSettings.FocusOnNavigationEnabled, True)
    settings.setAttribute(QWebEngineSettings.HyperlinkAuditingEnabled, True)
    settings.setAttribute(QWebEngineSettings.LocalContentCanAccessFileUrls, True)
    settings.setAttribute(QWebEngineSettings.LocalContentCanAccessRemoteUrls, True)
    settings.setAttribute(QWebEngineSettings.ScreenCaptureEnabled, True)
    settings.setAttribute(QWebEngineSettings.ShowScrollBars, True)
    settings.setAttribute(QWebEngineSettings.SpatialNavigationEnabled, True)
    settings.setAttribute(QWebEngineSettings.LinksIncludedInFocusChain, True)
    settings.setAttribute(QWebEngineSettings.AllowGeolocationOnInsecureOrigins, True)
    settings.setAttribute(QWebEngineSettings.AllowRunningInsecureContent, False)
    
    # Set modern user agent for all profiles
    QWebEngineProfile.defaultProfile().setHttpUserAgent("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")

    # Keep-alive timer to prevent abrupt closure
    keep_alive = QTimer()
    keep_alive.timeout.connect(lambda: None)
    keep_alive.start(500)  # Check every 500ms
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()