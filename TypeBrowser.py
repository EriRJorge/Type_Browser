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
from PyQt5.QtWebEngineCore import QWebEngineUrlRequestInterceptor, QWebEngineUrlRequestInfo
from browser_data import BrowserData
from settings_dialog import SettingsDialog
from download_manager import DownloadManager
from about_dialog import AboutDialog
from bookmark_manager import BookmarkDialog
from shortcuts_dialog import ShortcutsDialog

VERSION = "1.1.0"
APP_NAME = "Type_Browser"

class RequestInterceptor(QWebEngineUrlRequestInterceptor):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.download_path = os.path.expanduser("~/Downloads")
        self.chrome_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"

    def interceptRequest(self, info):
        url = info.requestUrl()
        is_crunchyroll = "crunchyroll.com" in url.host()
        
        # Set common headers for all requests
        info.setHttpHeader(b"Accept", b"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7")
        info.setHttpHeader(b"Accept-Language", b"en-US,en;q=0.9")
        info.setHttpHeader(b"Accept-Encoding", b"gzip, deflate, br")
        info.setHttpHeader(b"Connection", b"keep-alive")
        info.setHttpHeader(b"User-Agent", self.chrome_user_agent.encode())
        info.setHttpHeader(b"sec-ch-ua", b'"Chromium";v="123", "Google Chrome";v="123", "Not:A-Brand";v="99"')
        info.setHttpHeader(b"sec-ch-ua-mobile", b"?0")
        info.setHttpHeader(b"sec-ch-ua-platform", b'"Windows"')
        
        # Set security headers for main frame requests
        if info.resourceType() == QWebEngineUrlRequestInfo.ResourceTypeMainFrame:
            info.setHttpHeader(b"Upgrade-Insecure-Requests", b"1")
            info.setHttpHeader(b"Sec-Fetch-Dest", b"document")
            info.setHttpHeader(b"Sec-Fetch-Mode", b"navigate")
            info.setHttpHeader(b"Sec-Fetch-Site", b"none")
            info.setHttpHeader(b"Sec-Fetch-User", b"?1")
            info.setHttpHeader(b"DNT", b"1")
            
            # Set SameSite cookie attribute
            info.setHttpHeader(b"Set-Cookie", b"SameSite=None; Secure")
            
            # Handle HTTPS upgrade
            if url.scheme() == "http" and not url.host().startswith("localhost"):
                https_url = QUrl(url)
                https_url.setScheme("https")
                info.redirect(https_url)
        
        # Special handling for Crunchyroll
        if is_crunchyroll:
            # Add Crunchyroll-specific headers
            info.setHttpHeader(b"Origin", b"https://www.crunchyroll.com")
            info.setHttpHeader(b"Referer", b"https://www.crunchyroll.com/")
            
            # Handle different resource types for Crunchyroll
            resource_type = info.resourceType()
            if resource_type == QWebEngineUrlRequestInfo.ResourceTypeXhr:
                # Add headers for XHR requests
                info.setHttpHeader(b"Content-Type", b"application/json")
                info.setHttpHeader(b"X-Requested-With", b"XMLHttpRequest")
            elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeScript:
                # Add headers for script requests
                info.setHttpHeader(b"Cache-Control", b"no-cache")
            elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeStylesheet:
                # Add headers for stylesheet requests
                info.setHttpHeader(b"Cache-Control", b"no-cache")
            elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeImage:
                # Add headers for image requests
                info.setHttpHeader(b"Cache-Control", b"max-age=31536000")
        
        # Handle different resource types
        resource_type = info.resourceType()
        if resource_type == QWebEngineUrlRequestInfo.ResourceTypeMainFrame:
            # Handle main frame requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeSubFrame:
            # Handle sub-frame requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeStylesheet:
            # Handle stylesheet requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeScript:
            # Handle script requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeImage:
            # Handle image requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeFontResource:
            # Handle font requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeSubResource:
            # Handle sub-resource requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeObject:
            # Handle object requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeMedia:
            # Handle media requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeWorker:
            # Handle worker requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeSharedWorker:
            # Handle shared worker requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypePrefetch:
            # Handle prefetch requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeFavicon:
            # Handle favicon requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeXhr:
            # Handle XHR requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypePing:
            # Handle ping requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeServiceWorker:
            # Handle service worker requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeCspReport:
            # Handle CSP report requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypePluginResource:
            # Handle plugin resource requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeNavigationPreloadMainFrame:
            # Handle navigation preload main frame requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeNavigationPreloadSubFrame:
            # Handle navigation preload sub-frame requests
            pass
        elif resource_type == QWebEngineUrlRequestInfo.ResourceTypeOther:
            # Handle other requests
            pass

class WebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.featurePermissionRequested.connect(self.handlePermissionRequest)
        
        # Enable modern web features and performance optimizations
        settings = self.settings()
        
        # Core Features
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
        settings.setAttribute(QWebEngineSettings.AllowRunningInsecureContent, True)
        settings.setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)
        
        # Modern Web Features
        settings.setAttribute(QWebEngineSettings.JavascriptCanPaste, True)
        settings.setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        settings.setAttribute(QWebEngineSettings.PlaybackRequiresUserGesture, False)
        settings.setAttribute(QWebEngineSettings.DnsPrefetchEnabled, True)
        
        # Set modern user agent with latest Chrome version
        chrome_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
        self.profile().setHttpUserAgent(chrome_user_agent)
        
        # Enable hardware acceleration and caching
        self.profile().setHttpCacheType(QWebEngineProfile.DiskHttpCache)
        self.profile().setPersistentCookiesPolicy(QWebEngineProfile.AllowPersistentCookies)
        self.profile().setCachePath(os.path.join(os.path.expanduser("~"), ".cache", "type_browser"))
        self.profile().setPersistentStoragePath(os.path.join(os.path.expanduser("~"), ".cache", "type_browser"))
        
        # Set additional headers for modern web compatibility
        self.profile().setHttpAcceptLanguage("en-US,en;q=0.9")
        
        # Set up request interceptor for Cloudflare
        self.request_interceptor = RequestInterceptor()
        self.profile().setUrlRequestInterceptor(self.request_interceptor)
        
        # Inject modern web features and error handling
        self.loadFinished.connect(self.inject_modern_features)
        
    def inject_modern_features(self, ok):
        if ok:
            self.runJavaScript("""
                // Modern error handling
                window.onerror = function(msg, url, lineNo, columnNo, error) {
                    console.error('Error: ' + msg + '\\nURL: ' + url + '\\nLine: ' + lineNo + '\\nColumn: ' + columnNo + '\\nError object: ' + JSON.stringify(error));
                    return false;
                };
                
                // Promise rejection handling
                window.addEventListener('unhandledrejection', function(event) {
                    console.error('Unhandled promise rejection:', event.reason);
                });
                
                // Fix for replaceAll error
                if (!String.prototype.replaceAll) {
                    String.prototype.replaceAll = function(str, newStr) {
                        return this.split(str).join(newStr);
                    };
                }
                
                // Fix for webkitStorageInfo deprecation
                if (window.webkitStorageInfo) {
                    window.webkitStorageInfo = {
                        queryUsageAndQuota: function(callback) {
                            if (navigator.webkitTemporaryStorage) {
                                navigator.webkitTemporaryStorage.queryUsageAndQuota(callback);
                            } else {
                                callback(0, 0);
                            }
                        }
                    };
                }
                
                // Fix for lazy loading images without dimensions
                document.addEventListener('DOMContentLoaded', function() {
                    const images = document.querySelectorAll('img[loading="lazy"]');
                    images.forEach(img => {
                        if (!img.width || !img.height) {
                            img.addEventListener('load', function() {
                                if (!this.width || !this.height) {
                                    this.style.width = 'auto';
                                    this.style.height = 'auto';
                                }
                            });
                        }
                    });
                });
                
                // Fix for Crunchyroll specific issues
                document.addEventListener('DOMContentLoaded', function() {
                    // Fix for missing elements
                    const observer = new MutationObserver(function(mutations) {
                        mutations.forEach(function(mutation) {
                            if (mutation.type === 'childList') {
                                mutation.addedNodes.forEach(function(node) {
                                    if (node.nodeType === 1) { // Element node
                                        // Fix for missing dimensions
                                        if (node.tagName === 'IMG' && !node.width && !node.height) {
                                            node.style.width = 'auto';
                                            node.style.height = 'auto';
                                        }
                                        // Fix for missing styles
                                        if (node.classList && node.classList.contains('crunchyroll-element')) {
                                            node.style.display = 'block';
                                            node.style.visibility = 'visible';
                                        }
                                    }
                                });
                            }
                        });
                    });
                    
                    // Start observing the document
                    observer.observe(document.body, {
                        childList: true,
                        subtree: true
                    });
                    
                    // Fix for missing elements on initial load
                    setTimeout(function() {
                        const elements = document.querySelectorAll('.crunchyroll-element');
                        elements.forEach(function(element) {
                            element.style.display = 'block';
                            element.style.visibility = 'visible';
                        });
                    }, 1000);
                });
                
                // Modern web features detection
                if ('serviceWorker' in navigator) {
                    navigator.serviceWorker.register('/sw.js').catch(function(err) {
                        console.log('ServiceWorker registration failed: ', err);
                    });
                }
                
                // Enable modern web features
                if ('Notification' in window) {
                    Notification.requestPermission();
                }
                
                // Enable modern storage features
                if ('localStorage' in window) {
                    window.localStorage.setItem('browser_support', 'modern');
                }
                
                // Enable modern graphics features
                if ('WebGL2RenderingContext' in window) {
                    console.log('WebGL 2.0 is supported');
                }
                
                // Enable modern performance features
                if ('performance' in window) {
                    window.performance.mark('browser_ready');
                }
                
                // Enable modern web features
                if ('IntersectionObserver' in window) {
                    console.log('IntersectionObserver is supported');
                }
                
                // Enable modern web features
                if ('ResizeObserver' in window) {
                    console.log('ResizeObserver is supported');
                }
                
                // Enable modern web features
                if ('MutationObserver' in window) {
                    console.log('MutationObserver is supported');
                }
                
                // Enable modern web features
                if ('CustomElementRegistry' in window) {
                    console.log('Custom Elements are supported');
                }
                
                // Enable modern web features
                if ('ShadowRoot' in window) {
                    console.log('Shadow DOM is supported');
                }
                
                // Enable modern web features
                if ('fetch' in window) {
                    console.log('Fetch API is supported');
                }
                
                // Enable modern web features
                if ('requestAnimationFrame' in window) {
                    console.log('requestAnimationFrame is supported');
                }
                
                // Enable modern web features
                if ('requestIdleCallback' in window) {
                    console.log('requestIdleCallback is supported');
                }
            """)
    
    def javaScriptConsoleMessage(self, level, message, line, source):
        if level == QWebEnginePage.ErrorMessageLevel:
            print(f"Error: {message} at line {line} in {source}")
        elif level == QWebEnginePage.WarningMessageLevel:
            print(f"Warning: {message} at line {line} in {source}")
        elif level == QWebEnginePage.InfoMessageLevel:
            print(f"Info: {message} at line {line} in {source}")
    
    def handlePermissionRequest(self, url, feature):
        # Handle various permission requests
        if feature == QWebEnginePage.Feature.Geolocation:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionDeniedByUser)
        elif feature == QWebEnginePage.Feature.MediaAudioCapture:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionDeniedByUser)
        elif feature == QWebEnginePage.Feature.MediaVideoCapture:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionDeniedByUser)
        elif feature == QWebEnginePage.Feature.MediaAudioVideoCapture:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionDeniedByUser)
        elif feature == QWebEnginePage.Feature.MouseLock:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionDeniedByUser)
        elif feature == QWebEnginePage.Feature.DesktopVideoCapture:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionDeniedByUser)
        elif feature == QWebEnginePage.Feature.DesktopAudioVideoCapture:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionDeniedByUser)
        elif feature == QWebEnginePage.Feature.Notifications:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionDeniedByUser)
        else:
            self.setFeaturePermission(url, feature, QWebEnginePage.PermissionDeniedByUser)

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
        
        # Create developer tools window
        self.dev_tools = None
        
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
            self.page.triggerAction(QWebEnginePage.Copy)
        elif action == paste_action:
            self.page.triggerAction(QWebEnginePage.Paste)
        elif action == select_all_action:
            self.page.triggerAction(QWebEnginePage.SelectAll)
        elif action == save_page_action:
            self.page.triggerAction(QWebEnginePage.SavePage)
        elif action == view_source_action:
            self.page.triggerAction(QWebEnginePage.ViewSource)
        elif action == inspect_action:
            self.show_dev_tools()
            
    def show_dev_tools(self):
        if not self.dev_tools:
            self.dev_tools = QWebEngineView()
            self.dev_tools.setWindowTitle("Developer Tools")
            self.dev_tools.setMinimumSize(800, 600)
            
            # Create a new page for dev tools
            dev_page = QWebEnginePage(self.dev_tools)
            self.dev_tools.setPage(dev_page)
            
            # Connect the dev tools page to the main page
            self.page.setDevToolsPage(dev_page)
            
            # Set up the dev tools window
            self.dev_tools.setWindowFlags(Qt.Window)
            self.dev_tools.setAttribute(Qt.WA_DeleteOnClose)
            self.dev_tools.destroyed.connect(self.on_dev_tools_closed)
            
        # Show the dev tools window
        self.dev_tools.show()
        self.dev_tools.raise_()
        self.dev_tools.activateWindow()
        
    def on_dev_tools_closed(self):
        self.dev_tools = None
        
    def handle_fullscreen_request(self, request):
        if request.toggleOn():
            # Store current window state
            self.main_window.was_fullscreen = self.main_window.isFullScreen()
            
            # Hide all UI elements
            self.main_window.menu_bar.hide()
            self.main_window.unified_toolbar.hide()
            self.main_window.tabs.tabBar().hide()
            
            # Make the web view fill the entire window
            self.setParent(None)
            self.showFullScreen()
            request.accept()
        else:
            # Restore the web view to its original container
            current_tab = self.main_window.tabs.currentWidget()
            self.setParent(current_tab)
            current_tab.layout.addWidget(self)
            self.showNormal()
            
            # Always restore UI elements when exiting webpage fullscreen
            self.main_window.menu_bar.show()
            self.main_window.unified_toolbar.show()
            self.main_window.tabs.tabBar().show()
            
            request.accept()
        
    def handle_new_window(self, windowType):
        # Handle new window requests (e.g., target="_blank" links)
        if windowType == QWebEnginePage.WebBrowserTab and self.main_window:
            new_view = self.main_window.add_new_tab()
            return new_view.page
        return None

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
        
        # Enable window transparency
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowFlags(Qt.FramelessWindowHint)
        
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
        
        # Create a central widget with a layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Create unified toolbar
        self.unified_toolbar = self.create_unified_toolbar()
        layout.addWidget(self.unified_toolbar)
        
        # Add tabs
        layout.addWidget(self.tabs)
        
        # Create menubar
        self.menu_bar = self.create_menu()
        
        # Set up keyboard shortcuts
        self.setup_shortcuts()
        
        # Add homepage tab
        self.add_new_tab()
        
        # Center the window on screen
        self.center_on_screen()

        # Enable window dragging
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if self.old_pos:
            delta = event.globalPos() - self.old_pos
            self.move(self.pos() + delta)
            self.old_pos = event.globalPos()

    def mouseReleaseEvent(self, event):
        self.old_pos = None

    def toggle_maximize(self):
        if self.isMaximized():
            self.showNormal()
        else:
            self.showMaximized()

    def showFullScreen(self):
        # Hide UI elements in fullscreen
        self.menu_bar.hide()
        self.unified_toolbar.hide()
        self.tabs.tabBar().hide()  # Completely hide the tab bar
        super().showFullScreen()

    def showNormal(self):
        # Show UI elements when exiting fullscreen
        self.menu_bar.show()
        self.unified_toolbar.show()
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
            self.tabs.currentWidget().webview.page.triggerAction(QWebEnginePage.SavePage)

    def undo(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.page.triggerAction(QWebEnginePage.Undo)

    def redo(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.page.triggerAction(QWebEnginePage.Redo)

    def cut(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.page.triggerAction(QWebEnginePage.Cut)

    def copy(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.page.triggerAction(QWebEnginePage.Copy)

    def paste(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.page.triggerAction(QWebEnginePage.Paste)

    def find_in_page(self):
        if self.tabs.currentWidget():
            self.tabs.currentWidget().webview.page.triggerAction(QWebEnginePage.Find)

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

    def toggle_bookmark(self):
        if self.tabs.currentWidget():
            current_url = self.tabs.currentWidget().current_url()
            current_title = self.tabs.currentWidget().webview.title()
            
            # Check if already bookmarked
            for bookmark in self.browser_data.bookmarks:
                if bookmark["url"] == current_url:
                    self.browser_data.remove_bookmark(current_url)
                    return
            
            # Add new bookmark
            self.browser_data.add_bookmark(current_title, current_url)

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
                    background: #202124;
                }
                
                QWidget {
                    background: #202124;
                }
                
                QTabWidget::pane {
                    border: none;
                    background: #202124;
                }
                
                QTabWidget::tab-bar {
                    alignment: left;
                    background: #202124;
                    left: 0px;
                }
                
                QTabBar::tab {
                    background: #292a2d;
                    color: #9aa0a6;
                    padding: 6px 16px;
                    margin-right: 1px;
                    border: none;
                    min-width: 100px;
                    max-width: 200px;
                    font-size: 12px;
                    font-weight: 500;
                }
                
                QTabBar::tab:selected {
                    background: #202124;
                    color: #ffffff;
                    border-top: 2px solid #8ab4f8;
                }
                
                QTabBar::tab:hover {
                    background: #35363a;
                }

                QTabBar::close-button {
                    image: none;
                    background: transparent;
                    border: none;
                    margin: 2px;
                    padding: 2px;
                    border-radius: 2px;
                    color: #9aa0a6;
                    font-family: "Segoe UI";
                    font-size: 10px;
                    font-weight: bold;
                    min-width: 12px;
                    max-width: 12px;
                    min-height: 12px;
                    max-height: 12px;
                }

                QTabBar::close-button::after {
                    content: "×";
                }

                QTabBar::close-button:hover {
                    background: #35363a;
                    color: #ffffff;
                }

                QTabBar::close-button:pressed {
                    background: #3c4043;
                }
                
                QToolBar {
                    background: #202124;
                    border-bottom: 1px solid #3c4043;
                    spacing: 4px;
                    padding: 2px;
                }
                
                QToolButton {
                    background: transparent;
                    border: none;
                    padding: 4px;
                    border-radius: 4px;
                    color: #9aa0a6;
                }
                
                QToolButton:hover {
                    background: #35363a;
                    color: #ffffff;
                }
                
                QToolButton:pressed {
                    background: #3c4043;
                }

                QAction {
                    color: #9aa0a6;
                    padding: 4px;
                    border-radius: 4px;
                }

                QAction:hover {
                    background: #35363a;
                    color: #ffffff;
                }

                QAction:pressed {
                    background: #3c4043;
                }
                
                QLineEdit {
                    padding: 4px 12px;
                    border: 1px solid #3c4043;
                    border-radius: 20px;
                    background: #292a2d;
                    color: #ffffff;
                    selection-background-color: #8ab4f8;
                    selection-color: #202124;
                    font-size: 13px;
                    min-height: 28px;
                }
                
                QLineEdit:focus {
                    border: 1px solid #8ab4f8;
                    background: #292a2d;
                }
                
                QStatusBar {
                    background: #202124;
                    color: #9aa0a6;
                    border-top: 1px solid #3c4043;
                    padding: 2px;
                    font-size: 11px;
                }
                
                QMenu {
                    background: #202124;
                    border: 1px solid #3c4043;
                    border-radius: 4px;
                    padding: 4px;
                }
                
                QMenu::item {
                    padding: 6px 24px;
                    border-radius: 4px;
                    margin: 2px 4px;
                    color: #9aa0a6;
                }
                
                QMenu::item:selected {
                    background: #35363a;
                    color: #ffffff;
                }
                
                QMenu::separator {
                    height: 1px;
                    background: #3c4043;
                    margin: 4px 8px;
                }
                
                QPushButton {
                    background: #8ab4f8;
                    color: #202124;
                    border: none;
                    padding: 6px 12px;
                    border-radius: 4px;
                    font-weight: 500;
                    font-size: 12px;
                }
                
                QPushButton:hover {
                    background: #93bbf9;
                }
                
                QPushButton:pressed {
                    background: #7aa7f7;
                }
                
                QPushButton:disabled {
                    background: #3c4043;
                    color: #9aa0a6;
                }
                
                QScrollBar:vertical {
                    border: none;
                    background: transparent;
                    width: 8px;
                    margin: 0px;
                }
                
                QScrollBar::handle:vertical {
                    background: #3c4043;
                    border-radius: 4px;
                    min-height: 20px;
                    margin: 2px;
                }
                
                QScrollBar::handle:vertical:hover {
                    background: #4a4d51;
                }
                
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    height: 0px;
                }
                
                QScrollBar:horizontal {
                    border: none;
                    background: transparent;
                    height: 8px;
                    margin: 0px;
                }
                
                QScrollBar::handle:horizontal {
                    background: #3c4043;
                    border-radius: 4px;
                    min-width: 20px;
                    margin: 2px;
                }
                
                QScrollBar::handle:horizontal:hover {
                    background: #4a4d51;
                }
                
                QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                    width: 0px;
                }

                QMenuBar {
                    background: #202124;
                    color: #9aa0a6;
                    border-bottom: 1px solid #3c4043;
                    padding: 2px;
                }

                QMenuBar::item {
                    background: transparent;
                    padding: 4px 8px;
                    border-radius: 4px;
                    margin: 2px;
                }

                QMenuBar::item:selected {
                    background: #35363a;
                    color: #ffffff;
                }

                QMenuBar::item:pressed {
                    background: #3c4043;
                }

                QDialog {
                    background: #202124;
                    border-radius: 8px;
                    border: 1px solid #3c4043;
                }

                QLabel {
                    color: #ffffff;
                }

                QCheckBox {
                    color: #ffffff;
                    spacing: 8px;
                }

                QCheckBox::indicator {
                    width: 16px;
                    height: 16px;
                    border-radius: 3px;
                    border: 1px solid #3c4043;
                }

                QCheckBox::indicator:checked {
                    background: #8ab4f8;
                    border: 1px solid #8ab4f8;
                }

                QComboBox {
                    background: #292a2d;
                    border: 1px solid #3c4043;
                    border-radius: 4px;
                    padding: 4px 8px;
                    color: #ffffff;
                    min-width: 6em;
                }

                QComboBox:hover {
                    border: 1px solid #8ab4f8;
                }

                QComboBox::drop-down {
                    border: none;
                    width: 20px;
                }

                QComboBox::down-arrow {
                    image: none;
                    border: none;
                }

                #title_bar {
                    background: #202124;
                    border-radius: 8px 8px 0 0;
                    border: 1px solid #3c4043;
                    border-bottom: none;
                    padding: 1px;
                }

                #title_bar QPushButton {
                    background: transparent;
                    border: none;
                    color: #9aa0a6;
                    font-size: 12px;
                    padding: 2px;
                    border-radius: 4px;
                    min-width: 14px;
                    max-width: 14px;
                    min-height: 14px;
                    max-height: 14px;
                }

                #title_bar QPushButton:hover {
                    background: #35363a;
                    color: #ffffff;
                }

                #title_bar QPushButton:pressed {
                    background: #3c4043;
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
        app_font = QFont("Segoe UI", 9)
        QApplication.setFont(app_font)
        
        # Set global stylesheet with VS Code-like dark theme
        self.setStyleSheet("""
            QMainWindow {
                background: #1e1e1e;
            }
            
            QWidget {
                background: #1e1e1e;
                color: #ffffff;
            }
            
            #unified_toolbar {
                background: #1e1e1e;
                border-bottom: 1px solid #333333;
            }
            
            #title_bar {
                background: #1e1e1e;
                border-bottom: 1px solid #333333;
            }
            
            #title_bar QPushButton {
                background: transparent;
                border: none;
                color: #cccccc;
                font-size: 12px;
                padding: 2px;
                border-radius: 2px;
            }
            
            #title_bar QPushButton:hover {
                background: #2d2d2d;
            }
            
            #title_bar QPushButton:pressed {
                background: #3d3d3d;
            }
            
            #nav_bar {
                background: #1e1e1e;
            }
            
            #nav_bar QPushButton {
                background: transparent;
                border: none;
                color: #cccccc;
                font-size: 13px;
                padding: 4px;
                border-radius: 4px;
            }
            
            #nav_bar QPushButton:hover {
                background: #2d2d2d;
            }
            
            #nav_bar QPushButton:pressed {
                background: #3d3d3d;
            }
            
            QLineEdit {
                padding: 4px 12px;
                border: 1px solid #333333;
                border-radius: 4px;
                background: #2d2d2d;
                color: #ffffff;
                selection-background-color: #264f78;
                selection-color: #ffffff;
                font-size: 13px;
                min-height: 24px;
            }
            
            QLineEdit:focus {
                border: 1px solid #007acc;
                background: #2d2d2d;
            }
            
            QTabWidget::pane {
                border: none;
                background: #1e1e1e;
            }
            
            QTabWidget::tab-bar {
                alignment: left;
                background: #1e1e1e;
                left: 0px;
            }
            
            QTabBar::tab {
                background: #2d2d2d;
                color: #cccccc;
                padding: 6px 16px;
                margin-right: 1px;
                border: none;
                min-width: 100px;
                max-width: 200px;
                font-size: 12px;
                font-weight: 500;
            }
            
            QTabBar::tab:selected {
                background: #1e1e1e;
                color: #ffffff;
                border-top: 2px solid #007acc;
            }
            
            QTabBar::tab:hover {
                background: #3d3d3d;
            }

            QTabBar::close-button {
                image: none;
                background: transparent;
                border: none;
                margin: 2px;
                padding: 2px;
                border-radius: 2px;
                color: #cccccc;
                font-family: "Segoe UI";
                font-size: 10px;
                font-weight: bold;
                min-width: 12px;
                max-width: 12px;
                min-height: 12px;
                max-height: 12px;
            }

            QTabBar::close-button::after {
                content: "×";
            }

            QTabBar::close-button:hover {
                background: #3d3d3d;
                color: #ffffff;
            }

            QTabBar::close-button:pressed {
                background: #4d4d4d;
            }
            
            QMenu {
                background: #1e1e1e;
                border: 1px solid #333333;
                border-radius: 4px;
                padding: 4px;
            }
            
            QMenu::item {
                padding: 6px 24px;
                border-radius: 4px;
                margin: 2px 4px;
                color: #ffffff;
            }
            
            QMenu::item:selected {
                background: #2d2d2d;
                color: #ffffff;
            }
            
            QMenu::separator {
                height: 1px;
                background: #333333;
                margin: 4px 8px;
            }
            
            QMenuBar {
                background: #1e1e1e;
                color: #cccccc;
                border-bottom: 1px solid #333333;
                padding: 2px;
            }

            QMenuBar::item {
                background: transparent;
                padding: 4px 8px;
                border-radius: 4px;
                margin: 2px;
            }

            QMenuBar::item:selected {
                background: #2d2d2d;
                color: #ffffff;
            }

            QMenuBar::item:pressed {
                background: #3d3d3d;
            }

            QScrollBar:vertical {
                border: none;
                background: #1e1e1e;
                width: 8px;
                margin: 0px;
            }
            
            QScrollBar::handle:vertical {
                background: #3d3d3d;
                border-radius: 4px;
                min-height: 20px;
                margin: 2px;
            }
            
            QScrollBar::handle:vertical:hover {
                background: #4d4d4d;
            }
            
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                height: 0px;
            }
            
            QScrollBar:horizontal {
                border: none;
                background: #1e1e1e;
                height: 8px;
                margin: 0px;
            }
            
            QScrollBar::handle:horizontal {
                background: #3d3d3d;
                border-radius: 4px;
                min-width: 20px;
                margin: 2px;
            }
            
            QScrollBar::handle:horizontal:hover {
                background: #4d4d4d;
            }
            
            QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                width: 0px;
            }

            QDialog {
                background: #1e1e1e;
                border-radius: 8px;
                border: 1px solid #333333;
            }

            QDialog QLabel {
                color: #ffffff;
            }

            QDialog QPushButton {
                background: #2d2d2d;
                color: #ffffff;
                border: 1px solid #333333;
                padding: 6px 12px;
                border-radius: 4px;
            }

            QDialog QPushButton:hover {
                background: #3d3d3d;
            }

            QDialog QPushButton:pressed {
                background: #4d4d4d;
            }

            QMessageBox {
                background: #1e1e1e;
            }

            QMessageBox QLabel {
                color: #ffffff;
            }

            QMessageBox QPushButton {
                background: #2d2d2d;
                color: #ffffff;
                border: 1px solid #333333;
                padding: 6px 12px;
                border-radius: 4px;
            }

            QMessageBox QPushButton:hover {
                background: #3d3d3d;
            }

            QMessageBox QPushButton:pressed {
                background: #4d4d4d;
            }

            QInputDialog {
                background: #1e1e1e;
            }

            QInputDialog QLabel {
                color: #ffffff;
            }

            QInputDialog QLineEdit {
                background: #2d2d2d;
                color: #ffffff;
                border: 1px solid #333333;
                padding: 6px 12px;
                border-radius: 4px;
            }

            QInputDialog QPushButton {
                background: #2d2d2d;
                color: #ffffff;
                border: 1px solid #333333;
                padding: 6px 12px;
                border-radius: 4px;
            }

            QInputDialog QPushButton:hover {
                background: #3d3d3d;
            }

            QInputDialog QPushButton:pressed {
                background: #4d4d4d;
            }
        """)

    def create_unified_toolbar(self):
        toolbar = QWidget()
        toolbar.setObjectName("unified_toolbar")
        layout = QVBoxLayout(toolbar)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        
        # Title bar
        title_bar = QWidget()
        title_bar.setObjectName("title_bar")
        title_layout = QHBoxLayout(title_bar)
        title_layout.setContentsMargins(8, 4, 8, 4)
        
        # Window title
        title_label = QLabel(APP_NAME)
        title_label.setStyleSheet("color: #cccccc; font-size: 12px;")
        title_layout.addWidget(title_label)
        
        # Window controls
        minimize_btn = QPushButton("—")
        minimize_btn.setFixedSize(14, 14)
        minimize_btn.clicked.connect(self.showMinimized)
        
        maximize_btn = QPushButton("□")
        maximize_btn.setFixedSize(14, 14)
        maximize_btn.clicked.connect(self.toggle_maximize)
        
        close_btn = QPushButton("×")
        close_btn.setFixedSize(14, 14)
        close_btn.clicked.connect(self.close)
        
        title_layout.addWidget(minimize_btn)
        title_layout.addWidget(maximize_btn)
        title_layout.addWidget(close_btn)
        
        layout.addWidget(title_bar)
        
        # Navigation bar
        nav_bar = QWidget()
        nav_bar.setObjectName("nav_bar")
        nav_layout = QHBoxLayout(nav_bar)
        nav_layout.setContentsMargins(8, 4, 8, 4)
        
        # Navigation buttons
        back_btn = QPushButton("←")
        back_btn.setFixedSize(24, 24)
        back_btn.clicked.connect(self.navigate_back)
        
        forward_btn = QPushButton("→")
        forward_btn.setFixedSize(24, 24)
        forward_btn.clicked.connect(self.navigate_forward)
        
        reload_btn = QPushButton("↻")
        reload_btn.setFixedSize(24, 24)
        reload_btn.clicked.connect(self.reload_page)
        
        home_btn = QPushButton("⌂")
        home_btn.setFixedSize(24, 24)
        home_btn.clicked.connect(self.navigate_home)
        
        new_tab_btn = QPushButton("+")
        new_tab_btn.setFixedSize(24, 24)
        new_tab_btn.clicked.connect(self.add_new_tab)
        
        # Loading indicator
        self.loading_label = QLabel()
        self.loading_label.setFixedSize(16, 16)
        self.loading_label.setStyleSheet("""
            QLabel {
                background: transparent;
                color: #007acc;
            }
        """)
        self.loading_label.hide()
        
        # URL bar
        self.urlbar = QLineEdit()
        self.urlbar.setPlaceholderText("Search Google or enter URL")
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        
        # Add widgets to navigation layout
        nav_layout.addWidget(back_btn)
        nav_layout.addWidget(forward_btn)
        nav_layout.addWidget(reload_btn)
        nav_layout.addWidget(home_btn)
        nav_layout.addWidget(new_tab_btn)
        nav_layout.addWidget(self.loading_label)
        nav_layout.addWidget(self.urlbar)
        
        layout.addWidget(nav_bar)
        
        return toolbar

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
        
        # Connect loading signals
        tab.webview.loadStarted.connect(self.start_loading)
        tab.webview.loadFinished.connect(self.stop_loading)
        tab.webview.loadProgress.connect(self.update_loading_progress)
        
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

    def start_loading(self):
        self.loading_label.setText("⟳")
        self.loading_label.show()
        self.start_loading_animation()

    def stop_loading(self):
        self.loading_label.setText("✓")
        self.loading_label.setStyleSheet("""
            QLabel {
                background: transparent;
                color: #4CAF50;
            }
        """)
        QTimer.singleShot(1000, self.loading_label.hide)

    def update_loading_progress(self, progress):
        if progress < 100:
            self.loading_label.setText("⟳")
            self.loading_label.setStyleSheet("""
                QLabel {
                    background: transparent;
                    color: #007acc;
                }
            """)

    def start_loading_animation(self):
        self.loading_angle = 0
        self.loading_timer = QTimer()
        self.loading_timer.timeout.connect(self.rotate_loading_icon)
        self.loading_timer.start(50)  # Update every 50ms

    def rotate_loading_icon(self):
        self.loading_angle = (self.loading_angle + 30) % 360
        self.loading_label.setStyleSheet(f"""
            QLabel {{
                background: transparent;
                color: #007acc;
                transform: rotate({self.loading_angle}deg);
            }}
        """)

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