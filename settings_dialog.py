from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                            QLineEdit, QPushButton, QComboBox, QCheckBox,
                            QTabWidget, QWidget, QFileDialog, QSpinBox)
from PyQt5.QtCore import Qt

class SettingsDialog(QDialog):
    def __init__(self, browser_data, parent=None):
        super().__init__(parent)
        self.browser_data = browser_data
        self.setWindowTitle("Settings")
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)
        
        self.setup_ui()
        self.load_settings()

    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Create tab widget
        tabs = QTabWidget()
        
        # General tab
        general_tab = QWidget()
        general_layout = QVBoxLayout()
        
        # Homepage
        homepage_layout = QHBoxLayout()
        homepage_label = QLabel("Homepage:")
        self.homepage_edit = QLineEdit()
        homepage_layout.addWidget(homepage_label)
        homepage_layout.addWidget(self.homepage_edit)
        general_layout.addLayout(homepage_layout)
        
        # Search engine
        search_layout = QHBoxLayout()
        search_label = QLabel("Search Engine:")
        self.search_edit = QLineEdit()
        search_layout.addWidget(search_label)
        search_layout.addWidget(self.search_edit)
        general_layout.addLayout(search_layout)
        
        # Theme
        theme_layout = QHBoxLayout()
        theme_label = QLabel("Theme:")
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Light", "Dark"])
        theme_layout.addWidget(theme_label)
        theme_layout.addWidget(self.theme_combo)
        general_layout.addLayout(theme_layout)
        
        # Download path
        download_layout = QHBoxLayout()
        download_label = QLabel("Download Path:")
        self.download_edit = QLineEdit()
        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_download_path)
        download_layout.addWidget(download_label)
        download_layout.addWidget(self.download_edit)
        download_layout.addWidget(browse_button)
        general_layout.addLayout(download_layout)
        
        general_tab.setLayout(general_layout)
        
        # Privacy tab
        privacy_tab = QWidget()
        privacy_layout = QVBoxLayout()
        
        # Privacy settings
        self.clear_history_check = QCheckBox("Clear history on exit")
        self.clear_cookies_check = QCheckBox("Clear cookies on exit")
        self.do_not_track_check = QCheckBox("Send Do Not Track request")
        
        privacy_layout.addWidget(self.clear_history_check)
        privacy_layout.addWidget(self.clear_cookies_check)
        privacy_layout.addWidget(self.do_not_track_check)
        
        privacy_tab.setLayout(privacy_layout)
        
        # Advanced tab
        advanced_tab = QWidget()
        advanced_layout = QVBoxLayout()
        
        # JavaScript
        self.enable_javascript = QCheckBox("Enable JavaScript")
        self.enable_plugins = QCheckBox("Enable Plugins")
        self.enable_images = QCheckBox("Enable Images")
        self.enable_cookies = QCheckBox("Enable Cookies")
        
        advanced_layout.addWidget(self.enable_javascript)
        advanced_layout.addWidget(self.enable_plugins)
        advanced_layout.addWidget(self.enable_images)
        advanced_layout.addWidget(self.enable_cookies)
        
        # Zoom level
        zoom_layout = QHBoxLayout()
        zoom_label = QLabel("Default Zoom Level:")
        self.zoom_spin = QSpinBox()
        self.zoom_spin.setRange(25, 500)
        self.zoom_spin.setSingleStep(25)
        self.zoom_spin.setSuffix("%")
        zoom_layout.addWidget(zoom_label)
        zoom_layout.addWidget(self.zoom_spin)
        advanced_layout.addLayout(zoom_layout)
        
        advanced_tab.setLayout(advanced_layout)
        
        # Add tabs
        tabs.addTab(general_tab, "General")
        tabs.addTab(privacy_tab, "Privacy")
        tabs.addTab(advanced_tab, "Advanced")
        
        layout.addWidget(tabs)
        
        # Buttons
        button_layout = QHBoxLayout()
        save_button = QPushButton("Save")
        cancel_button = QPushButton("Cancel")
        save_button.clicked.connect(self.save_settings)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(save_button)
        button_layout.addWidget(cancel_button)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)

    def load_settings(self):
        settings = self.browser_data.settings
        
        # General settings
        self.homepage_edit.setText(settings.get("homepage", "https://typesearch.click/"))
        self.search_edit.setText(settings.get("search_engine", "https://www.google.com/search?q="))
        self.theme_combo.setCurrentText(settings.get("theme", "Light").capitalize())
        self.download_edit.setText(settings.get("download_path", ""))
        
        # Privacy settings
        self.clear_history_check.setChecked(settings.get("clear_history_on_exit", False))
        self.clear_cookies_check.setChecked(settings.get("clear_cookies_on_exit", False))
        self.do_not_track_check.setChecked(settings.get("do_not_track", False))
        
        # Advanced settings
        self.enable_javascript.setChecked(settings.get("enable_javascript", True))
        self.enable_plugins.setChecked(settings.get("enable_plugins", True))
        self.enable_images.setChecked(settings.get("enable_images", True))
        self.enable_cookies.setChecked(settings.get("enable_cookies", True))
        self.zoom_spin.setValue(settings.get("zoom_level", 100))

    def save_settings(self):
        settings = {
            "homepage": self.homepage_edit.text(),
            "search_engine": self.search_edit.text(),
            "theme": self.theme_combo.currentText().lower(),
            "download_path": self.download_edit.text(),
            "clear_history_on_exit": self.clear_history_check.isChecked(),
            "clear_cookies_on_exit": self.clear_cookies_check.isChecked(),
            "do_not_track": self.do_not_track_check.isChecked(),
            "enable_javascript": self.enable_javascript.isChecked(),
            "enable_plugins": self.enable_plugins.isChecked(),
            "enable_images": self.enable_images.isChecked(),
            "enable_cookies": self.enable_cookies.isChecked(),
            "zoom_level": self.zoom_spin.value()
        }
        
        for key, value in settings.items():
            self.browser_data.update_setting(key, value)
        
        self.accept()

    def browse_download_path(self):
        path = QFileDialog.getExistingDirectory(self, "Select Download Directory")
        if path:
            self.download_edit.setText(path) 