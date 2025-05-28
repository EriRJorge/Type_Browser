from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import Qt

class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Type Browser")
        self.setFixedSize(400, 300)
        
        layout = QVBoxLayout()
        
        # App info
        title_label = QLabel("<h1>Type Browser</h1>")
        title_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(title_label)
        
        version_label = QLabel("<h3>Version 1.0.2</h3>")
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