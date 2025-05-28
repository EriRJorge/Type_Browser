import json
import os
from datetime import datetime
from PyQt5.QtCore import QObject, pyqtSignal

class BrowserData(QObject):
    bookmarks_changed = pyqtSignal()
    history_changed = pyqtSignal()
    settings_changed = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.data_dir = os.path.expanduser("~/.type_browser")
        self.bookmarks_file = os.path.join(self.data_dir, "bookmarks.json")
        self.history_file = os.path.join(self.data_dir, "history.json")
        self.settings_file = os.path.join(self.data_dir, "settings.json")
        
        # Create data directory if it doesn't exist
        os.makedirs(self.data_dir, exist_ok=True)
        
        # Initialize data structures
        self.bookmarks = self.load_bookmarks()
        self.history = self.load_history()
        self.settings = self.load_settings()

    def load_bookmarks(self):
        if os.path.exists(self.bookmarks_file):
            try:
                with open(self.bookmarks_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def load_history(self):
        if os.path.exists(self.history_file):
            try:
                with open(self.history_file, 'r') as f:
                    return json.load(f)
            except:
                return []
        return []

    def load_settings(self):
        default_settings = {
            "homepage": "https://typesearch.click/",
            "search_engine": "https://www.google.com/search?q=",
            "theme": "light",
            "download_path": os.path.expanduser("~/Downloads"),
            "zoom_level": 100,
            "enable_javascript": True,
            "enable_plugins": True,
            "enable_images": True,
            "enable_cookies": True,
            "enable_javascript_popups": True,
            "enable_auto_load_images": True,
            "enable_webgl": True,
            "enable_webaudio": True,
            "enable_webgl_draft": False,
            "enable_webgl_2": True,
            "enable_webgl_2_draft": False,
            "enable_webgl_2_antialiasing": True,
            "enable_webgl_2_multisampling": True,
            "enable_webgl_2_preserve_drawing_buffer": False,
            "enable_webgl_2_power_preference": "default",
            "enable_webgl_2_fail_if_major_performance_caveat": False,
            "enable_webgl_2_desynchronized": False,
            "enable_webgl_2_antialiasing": True,
            "enable_webgl_2_multisampling": True,
            "enable_webgl_2_preserve_drawing_buffer": False,
            "enable_webgl_2_power_preference": "default",
            "enable_webgl_2_fail_if_major_performance_caveat": False,
            "enable_webgl_2_desynchronized": False,
        }
        
        if os.path.exists(self.settings_file):
            try:
                with open(self.settings_file, 'r') as f:
                    loaded_settings = json.load(f)
                    default_settings.update(loaded_settings)
            except:
                pass
        return default_settings

    def save_bookmarks(self):
        with open(self.bookmarks_file, 'w') as f:
            json.dump(self.bookmarks, f)
        self.bookmarks_changed.emit()

    def save_history(self):
        with open(self.history_file, 'w') as f:
            json.dump(self.history, f)
        self.history_changed.emit()

    def save_settings(self):
        with open(self.settings_file, 'w') as f:
            json.dump(self.settings, f)
        self.settings_changed.emit()

    def add_bookmark(self, title, url):
        bookmark = {
            "title": title,
            "url": url,
            "date_added": datetime.now().isoformat()
        }
        self.bookmarks.append(bookmark)
        self.save_bookmarks()

    def remove_bookmark(self, url):
        self.bookmarks = [b for b in self.bookmarks if b["url"] != url]
        self.save_bookmarks()

    def add_history(self, title, url):
        history_item = {
            "title": title,
            "url": url,
            "date_visited": datetime.now().isoformat()
        }
        self.history.append(history_item)
        self.save_history()

    def clear_history(self):
        self.history = []
        self.save_history()

    def update_setting(self, key, value):
        self.settings[key] = value
        self.save_settings()

    def get_setting(self, key, default=None):
        return self.settings.get(key, default) 