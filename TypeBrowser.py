#Type_Browser.py
# First Type_Software Project
#Eri R Jorge
#3/6/2025 - Project started
#3/6/2025 - Added the main window and tabbed browsing, added navigation toolbar and menu bar with basic actions and shortcuts
#3/8/2025 - Fixed tab functionality and improved visual styling, Added Keep Alive Features



import sys
import os
from PyQt5.QtCore import QUrl, Qt, QSize, QTimer
from PyQt5.QtWidgets import (QApplication, QMainWindow, QToolBar, QAction, 
                            QLineEdit, QTabWidget, QWidget, QVBoxLayout, 
                            QShortcut, QMenu, QDialog, QLabel, QVBoxLayout, 
                            QPushButton, QHBoxLayout, QFileDialog, QMessageBox,
                            QStatusBar, QFrame)
from PyQt5.QtGui import QIcon, QKeySequence, QFont, QColor, QPalette
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtWebEngineWidgets import QWebEngineProfile

VERSION = "1.0.2"
APP_NAME = "Type_Browser"

class DownloadInterceptor(QWebEngineProfile):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.download_path = os.path.expanduser("~/Downloads")

    def interceptRequest(self, info):
        # TODO: Implement custom download behavior here
        pass

class WebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.featurePermissionRequested.connect(self.handlePermissionRequest)
    
    def handlePermissionRequest(self, url, feature):
        # TODO: Implement proper permission handling
        # simplified example
        self.setFeaturePermission(url, feature, QWebEnginePage.PermissionGrantedByUser)

class WebView(QWebEngineView):
    def __init__(self, main_window=None):
        super().__init__()
        self.main_window = main_window
        self.page = WebPage(self)
        self.setPage(self.page)
        
    def createWindow(self, windowType):
        if windowType == QWebEnginePage.WebBrowserTab and self.main_window:
            return self.main_window.add_new_tab()
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
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #2979ff;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #448aff;
            }
        """)
        close_button.clicked.connect(self.accept)
        layout.addWidget(close_button, alignment=Qt.AlignCenter)
        
        self.setLayout(layout)
        self.setStyleSheet("""
            QDialog {
                background-color: #f5f5f5;
            }
            QLabel {
                color: #333333;
            }
        """)

class BrowserTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        
        self.webview = WebView(parent)
        self.layout.addWidget(self.webview)
        self.setLayout(self.layout)
        
    def navigate(self, url):
        # Convert QUrl to string if needed
        if isinstance(url, QUrl):
            url = url.toString()
            
        # Ensure url is a string
        url_str = str(url)
        
        if not url_str.startswith('http'):
            # Check if it's a valid domain or search query
            if '.' in url_str and ' ' not in url_str:
                url_str = 'https://' + url_str
            else:
                url_str = f'https://www.google.com/search?q={url_str}'
        
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(APP_NAME)
        self.setWindowIcon(QIcon("icon.png"))  # Add an icon file in your package
        self.setMinimumSize(1024, 768)
        
        # Set application style
        self.apply_style()
        
        # Initialize UI components
        self.tabs = QTabWidget()
        self.tabs.setTabsClosable(True)
        self.tabs.tabCloseRequested.connect(self.close_tab)
        self.tabs.currentChanged.connect(self.tab_changed)
        self.tabs.setDocumentMode(True)  # Makes tabs look cleaner
        
        # Add + button for new tab
        self.tabs.setCornerWidget(self.create_new_tab_button())
        
        self.setCentralWidget(self.tabs)
        
        # Navigation toolbar
        self.create_navigation_toolbar()
        
        # Create menubar
        self.create_menu()
        
        # Create status bar
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        # Set up keyboard shortcuts
        QShortcut(QKeySequence("Ctrl+T"), self, self.add_new_tab)
        QShortcut(QKeySequence("Ctrl+W"), self, self.close_current_tab)
        QShortcut(QKeySequence("Ctrl+R"), self, self.reload_page)
        QShortcut(QKeySequence("Ctrl+L"), self, self.focus_url_bar)
        
        # Add homepage tab
        self.add_new_tab("https://typesearch.click/")
        
        # Center the window on screen
        self.center_on_screen()

    def apply_style(self):
        # Set application font
        app_font = QFont("Segoe UI", 10)
        QApplication.setFont(app_font)
        
        # Set global stylesheet
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
            QTabWidget::pane {
                border: none;
            }
            QTabWidget::tab-bar {
                alignment: left;
            }
            QTabBar::tab {
                background-color: #e0e0e0;
                color: #333333;
                padding: 8px 12px;
                margin-right: 2px;
                border-top-left-radius: 4px;
                border-top-right-radius: 4px;
            }
            QTabBar::tab:selected {
                background-color: #ffffff;
                border-bottom: none;
            }
            QTabBar::tab:hover {
                background-color: #f0f0f0;
            }
            QToolBar {
                background-color: #ffffff;
                border-bottom: 1px solid #e0e0e0;
                spacing: 5px;
                padding: 2px;
            }
            QToolButton {
                background-color: transparent;
                border: none;
                padding: 5px;
                border-radius: 4px;
            }
            QToolButton:hover {
                background-color: #f0f0f0;
            }
            QLineEdit {
                padding: 5px;
                border: 1px solid #e0e0e0;
                border-radius: 4px;
                background-color: #ffffff;
            }
            QLineEdit:focus {
                border: 1px solid #2979ff;
            }
            QStatusBar {
                background-color: #f5f5f5;
                color: #757575;
            }
            QMenu {
                background-color: #ffffff;
                border: 1px solid #e0e0e0;
            }
            QMenu::item {
                padding: 5px 20px;
            }
            QMenu::item:selected {
                background-color: #f0f0f0;
            }
        """)

    def create_new_tab_button(self):
        button = QPushButton("+")
        button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                border: none;
                padding: 5px 10px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #f0f0f0;
            }
        """)
        button.setToolTip("Open new tab")
        button.clicked.connect(self.add_new_tab)
        return button

    def create_navigation_toolbar(self):
        nav_toolbar = QToolBar("Navigation")
        nav_toolbar.setIconSize(QSize(20, 20))
        nav_toolbar.setMovable(False)
        self.addToolBar(nav_toolbar)
        
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
        
        # Add some spacing
        spacer = QWidget()
        spacer.setFixedWidth(5)
        nav_toolbar.addWidget(spacer)
        
        # URL bar with better styling
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        self.urlbar.setPlaceholderText("Search or enter website name")
        nav_toolbar.addWidget(self.urlbar)

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
    
    def add_new_tab(self, url="https://typesearch.click/"):
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
    
    def close_tab(self, index):
        if self.tabs.count() > 1:
            self.tabs.removeTab(index)
        else:
            # If this is the last tab, create a new one before closing
            cur_index = self.tabs.currentIndex()
            self.add_new_tab()
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

    def closeEvent(self, event):
        print("Close event received")
        reply = QMessageBox.question(self, 'Confirm Exit',
                                "Are you sure you want to quit?",
                                QMessageBox.Yes | QMessageBox.No,
                                QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

def main():
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    
    # Set application style for all widgets
    app.setStyle("Fusion")

    # Keep-alive timer to prevent abrupt closure
    keep_alive = QTimer()
    keep_alive.timeout.connect(lambda: None)
    keep_alive.start(500)  # Check every 500ms
    
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()