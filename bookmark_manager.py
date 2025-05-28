from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                            QPushButton, QListWidget, QListWidgetItem, QWidget)
from PyQt5.QtCore import Qt

class BookmarkDialog(QDialog):
    def __init__(self, browser_data, parent=None):
        super().__init__(parent)
        self.browser_data = browser_data
        self.setWindowTitle("Bookmarks")
        self.setMinimumSize(500, 400)
        
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Create list widget for bookmarks
        self.list_widget = QListWidget()
        self.update_bookmark_list()
        layout.addWidget(self.list_widget)
        
        # Add buttons
        button_layout = QHBoxLayout()
        open_button = QPushButton("Open")
        remove_button = QPushButton("Remove")
        close_button = QPushButton("Close")
        
        open_button.clicked.connect(self.open_bookmark)
        remove_button.clicked.connect(self.remove_bookmark)
        close_button.clicked.connect(self.accept)
        
        button_layout.addWidget(open_button)
        button_layout.addWidget(remove_button)
        button_layout.addWidget(close_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
        
    def update_bookmark_list(self):
        self.list_widget.clear()
        for bookmark in self.browser_data.bookmarks:
            item = QListWidgetItem(f"{bookmark['title']} - {bookmark['url']}")
            item.setData(Qt.UserRole, bookmark['url'])  # Store URL for later use
            self.list_widget.addItem(item)
            
    def open_bookmark(self):
        current_item = self.list_widget.currentItem()
        if current_item:
            url = current_item.data(Qt.UserRole)
            if self.parent():
                self.parent().add_new_tab(url)
            self.accept()
            
    def remove_bookmark(self):
        current_item = self.list_widget.currentItem()
        if current_item:
            url = current_item.data(Qt.UserRole)
            self.browser_data.remove_bookmark(url)
            self.update_bookmark_list() 