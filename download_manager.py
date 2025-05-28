from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QLabel, 
                            QPushButton, QProgressBar, QListWidget, QFileDialog,
                            QListWidgetItem, QWidget)
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtWebEngineWidgets import QWebEngineDownloadItem
import os

class DownloadItem:
    def __init__(self, download_item):
        self.download_item = download_item
        self.path = download_item.path()
        self.filename = os.path.basename(self.path)
        self.state = download_item.state()
        self.progress = 0
        self.total_bytes = download_item.totalBytes()
        self.received_bytes = download_item.receivedBytes()
        
        # Connect signals
        download_item.downloadProgress.connect(self.update_progress)
        download_item.stateChanged.connect(self.update_state)
        download_item.finished.connect(self.download_finished)
        
    def update_progress(self, received, total):
        self.received_bytes = received
        self.total_bytes = total
        if total > 0:
            self.progress = int((received / total) * 100)
        else:
            self.progress = 0
            
    def update_state(self, state):
        self.state = state
        
    def download_finished(self):
        self.state = QWebEngineDownloadItem.DownloadCompleted

class DownloadManager(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Downloads")
        self.setMinimumWidth(600)
        self.setMinimumHeight(400)
        
        self.downloads = []
        self.setup_ui()
        
    def setup_ui(self):
        layout = QVBoxLayout()
        
        # Create list widget for downloads
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)
        
        # Add buttons
        button_layout = QHBoxLayout()
        clear_button = QPushButton("Clear Completed")
        open_folder_button = QPushButton("Open Download Folder")
        close_button = QPushButton("Close")
        
        clear_button.clicked.connect(self.clear_completed)
        open_folder_button.clicked.connect(self.open_download_folder)
        close_button.clicked.connect(self.accept)
        
        button_layout.addWidget(clear_button)
        button_layout.addWidget(open_folder_button)
        button_layout.addWidget(close_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
        
    def add_download(self, download_item):
        item = DownloadItem(download_item)
        self.downloads.append(item)
        self.update_list()
        
    def update_list(self):
        self.list_widget.clear()
        for download in self.downloads:
            # Create item widget
            item_widget = QWidget()
            item_layout = QVBoxLayout()
            
            # File name and status
            name_label = QLabel(download.filename)
            status_label = QLabel(self.get_status_text(download))
            
            # Progress bar
            progress_bar = QProgressBar()
            progress_bar.setValue(download.progress)
            
            # Add widgets to layout
            item_layout.addWidget(name_label)
            item_layout.addWidget(status_label)
            item_layout.addWidget(progress_bar)
            
            item_widget.setLayout(item_layout)
            
            # Add to list
            list_item = QListWidgetItem()
            list_item.setSizeHint(item_widget.sizeHint())
            self.list_widget.addItem(list_item)
            self.list_widget.setItemWidget(list_item, item_widget)
            
    def get_status_text(self, download):
        if download.state == QWebEngineDownloadItem.DownloadInProgress:
            return f"Downloading... {download.progress}%"
        elif download.state == QWebEngineDownloadItem.DownloadCompleted:
            return "Completed"
        elif download.state == QWebEngineDownloadItem.DownloadCancelled:
            return "Cancelled"
        elif download.state == QWebEngineDownloadItem.DownloadInterrupted:
            return "Interrupted"
        else:
            return "Unknown"
            
    def clear_completed(self):
        self.downloads = [d for d in self.downloads 
                         if d.state != QWebEngineDownloadItem.DownloadCompleted]
        self.update_list()
        
    def open_download_folder(self):
        if self.downloads:
            path = os.path.dirname(self.downloads[0].path)
            QDesktopServices.openUrl(QUrl.fromLocalFile(path)) 