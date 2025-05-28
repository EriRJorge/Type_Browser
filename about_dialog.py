from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, 
                            QLabel, QPushButton)
from PyQt5.QtCore import Qt

VERSION = "1.1.0"

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Type Browser")
        self.setFixedSize(400, 300)
        
        layout = QVBoxLayout()
        
        # Title
        title = QLabel("Type Browser")
        title.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 24px;
                font-weight: bold;
                padding: 20px;
            }
        """)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Version
        version = QLabel(f"Version {VERSION}")
        version.setStyleSheet("""
            QLabel {
                color: #cccccc;
                font-size: 14px;
                padding: 10px;
            }
        """)
        version.setAlignment(Qt.AlignCenter)
        layout.addWidget(version)
        
        # Description
        description = QLabel(
            "A modern, lightweight web browser built with Python and Qt.\n\n"
            "Features:\n"
            "• Fast and secure browsing\n"
            "• Modern dark theme UI\n"
            "• Tabbed browsing\n"
            "• Bookmark management\n"
            "• Download manager\n"
            "• Customizable settings"
        )
        description.setStyleSheet("""
            QLabel {
                color: #ffffff;
                font-size: 12px;
                padding: 20px;
                line-height: 1.5;
            }
        """)
        description.setAlignment(Qt.AlignCenter)
        layout.addWidget(description)
        
        # Copyright
        copyright = QLabel("© 2024 Type Browser Team")
        copyright.setStyleSheet("""
            QLabel {
                color: #cccccc;
                font-size: 11px;
                padding: 10px;
            }
        """)
        copyright.setAlignment(Qt.AlignCenter)
        layout.addWidget(copyright)
        
        # Close button
        close_button = QPushButton("Close")
        close_button.setStyleSheet("""
            QPushButton {
                background: #2d2d2d;
                color: #ffffff;
                border: 1px solid #333333;
                padding: 8px 24px;
                border-radius: 4px;
                font-size: 12px;
                min-width: 80px;
            }
            QPushButton:hover {
                background: #3d3d3d;
            }
            QPushButton:pressed {
                background: #4d4d4d;
            }
        """)
        close_button.clicked.connect(self.accept)
        
        button_layout = QHBoxLayout()
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        button_layout.addStretch()
        layout.addLayout(button_layout)
        
        self.setLayout(layout) 