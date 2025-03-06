#TypeBrowser.py
# First Type_Software Project
#Eri R Jorge
#3/6/3025 - Project started
#3/6/2025 - Added the main window and tabbed browsing, added navigation toolbar and menu bar with basic actions and shortcuts




import sys
import os
from PyQt5.QtCore import QUrl, Qt, QSize
from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar, QAction, 
                            QLineEdit, QTabWidget, QWidget, QVBoxLayout, 
                            QShortcut, QMenu, QDialog, QLabel, QVBoxLayout, 
                            QPushButton, QHBoxLayout, QFileDialog, QMessageBox)
from PyQt5.QtGui import QIcon, QKeySequence
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWebEngineWidgets import QWebEngineProfile

VERSION = "1.0.0"
APP_NAME = "TypeBrowser"

class DownloadInterceptor(QWebEngineProfile):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.download_path = os.path.expanduser("~/Downloads")

    def interceptRequest(self, info):
        # You could implement custom download behavior here
        pass

class WebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.featurePermissionRequested.connect(self.handlePermissionRequest)
    
    def handlePermissionRequest(self, url, feature):
        # For a real product, implement proper permission handling
        # This is just a simplified example
        self.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)

class WebView(QWebEngineView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.page = WebPage(self)
        self.setPage(self.page)
        
    def createWindow(self, windowType):
        if windowType == QWebEnginePage.WebBrowserTab:
            return self.window().createTab()
        return None

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle(f"About {APP_NAME}")
        self.setFixedSize(400, 300)
        
        layout = QVBoxLayout()
        
        # App info
        title_label = QLabel(f"<h1>{APP_NAME}</h1>")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        version_label = QLabel(f"<h3>Version {VERSION}</h3>")
        version_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(version_label)
        
        description = QLabel(
            "<p>A lightweight, privacy-focused personal web browser.</p>"
            "<p>Built with Python and PyQt5.</p>"
        )
        description.setAlignment(Qt.AlignCenter)
        description.setWordWrap(True)
        layout.addWidget(description)
        
        # Close button
        close_button = QPushButton("Close")
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)

class BrowserTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        self.webview = WebView(self)
        self.layout.addWidget(self.webview)
        self.setLayout(self.layout)
        
    def navigate(self, url):
        if not url.startswith('http'):
            url = 'https://' + url
        self.webview.load(QUrl(url))
        
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon("icon.png"))  # Add an icon file in your package
        self.setMinimumSize(1024, 768)
        
        # Initialize UI components
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.tab_changed)
        
        self.setCentralWidget(self.tabs)
        
        # Navigation toolbar
        nav_toolbar = QToolBar("Navigation")
        nav_toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(nav_toolbar)
        
        back_action = QAction("←", self)
        back_action.setStatusTip("Go back to previous page")
        back_action.triggered.connect(self.navigate_back)
        nav_toolbar.addAction(back_action)
        
        forward_action = QAction("→", self)
        forward_action.setStatusTip("Go forward to next page")
        forward_action.triggered.connect(self.navigate_forward)
        nav_toolbar.addAction(forward_action)
        
        reload_action = QAction("↻", self)
        reload_action.setStatusTip("Reload current page")
        reload_action.triggered.connect(self.reload_page)
        nav_toolbar.addAction(reload_action)
        
        home_action = QAction("🏠", self)
        home_action.setStatusTip("Go to homepage")
        home_action.triggered.connect(self.navigate_home)
        nav_toolbar.addAction(home_action)
        
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        nav_toolbar.addWidget(self.urlbar)
        
        # Create menubar
        self.create_menu()
        
        # Set up keyboard shortcuts
        QShortcut(QKeySequence("Ctrl+T"), self, self.add_new_tab)
        QShortcut(QKeySequence("Ctrl+W"), self, self.close_current_tab)
        QShortcut(QKeySequence("Ctrl+R"), self, self.reload_page)
        
        # Add homepage tab
        self.add_new_tab()
        
        # Center the window on screen
        self.center_on_screen()

    def center_on_screen(self):
        # Center the window on the screen
        screen_geometry = QApplication.desktop().availableGeometry()
        window_geometry = self.frameGeometry()
        window_geometry.moveCenter(screen_geometry.center())
        self.move(window_geometry.topLeft())
        
    def create_menu(self):
        menu_bar = self.menuBar()
        
        # File Menu
        file_menu = menu_bar.addMenu("File")
        
        new_tab_action = QAction("New Tab", self)
        new_tab_action.setShortcut("Ctrl+T")
        new_tab_action.triggered.connect(self.add_new_tab)
        file_menu.addAction(new_tab_action)
        
        close_tab_action = QAction("Close Tab", self)
        close_tab_action.setShortcut("Ctrl+W")
        close_tab_action.triggered.connect(self.close_current_tab)
        file_menu.addAction(close_tab_action)
        
        file_menu.addSeparator()
        
        exit_action = QAction("Exit", self)
        exit_action.setShortcut("Ctrl+Q")
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Edit Menu
        edit_menu = menu_bar.addMenu("Edit")
        
        # View Menu
        view_menu = menu_bar.addMenu("View")
        
        # History Menu
        history_menu = menu_bar.addMenu("History")
        
        # Bookmarks Menu
        bookmarks_menu = menu_bar.addMenu("Bookmarks")
        
        # Tools Menu
        tools_menu = menu_bar.addMenu("Tools")
        
        # Help Menu
        help_menu = menu_bar.addMenu("Help")
        
        about_action = QAction("About", self)
        about_action.triggered.connect(self.show_about_dialog)
        help_menu.addAction(about_action)
    
    def show_about_dialog(self):
        dialog = AboutDialog(self)
        dialog.exec_()
    
    def add_new_tab(self, url="https://www.google.com"):
        tab = BrowserTab(self)
        index = self.tabs.addTab(tab, "New Tab")
        self.tabs.setCurrentIndex(index)
        tab.navigate(url)
        tab.webview.titleChanged.connect(lambda title, tab=tab: self.update_tab_title(tab, title))
        tab.webview.urlChanged.connect(lambda url, tab=tab: self.update_urlbar(url, tab))
        return tab.webview
    
    def createTab(self):
        # This is called when a new tab is needed by the browser
        return self.add_new_tab()
    
    def update_tab_title(self, tab, title):
        index = self.tabs.indexOf(tab)
        if index >= 0:
            truncated_title = title[:20] + "..." if len(title) > 20 else title
            self.tabs.setTabText(index, truncated_title)
    
    def update_urlbar(self, url, tab=None):
        # Only update the URL bar if the tab is the current one
        if tab and self.tabs.currentWidget() == tab:
            self.urlbar.setText(url.toString())
            self.urlbar.setCursorPosition(0)
    
    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            self.add_new_tab()
            self.tabs.removeTab(index)
    
    def close_current_tab(self):
        self.close_tab(self.tabs.currentIndex())
    
    def tab_changed(self, index):
        if index >= 0:
            tab = self.tabs.widget(index)
            url = tab.current_url()
            self.update_urlbar(QUrl(url))
    
    def navigate_to_url(self):
        url = self.urlbar.text()
        self.tabs.currentWidget().navigate(url)
    
    def navigate_back(self):
        self.tabs.currentWidget().back()
    
    def navigate_forward(self):
        self.tabs.currentWidget().forward()
    
    def reload_page(self):
        self.tabs.currentWidget().refresh()
    
    def navigate_home(self):
        self.tabs.currentWidget().navigate("https://www.google.com")

def main():
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()