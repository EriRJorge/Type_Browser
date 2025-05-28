from PyQt5.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QPushButton, 
                            QTableWidget, QTableWidgetItem, QLabel, QLineEdit,
                            QMessageBox, QHeaderView, QInputDialog)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence

class ShortcutsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.setWindowTitle("Keyboard Shortcuts")
        self.setMinimumSize(600, 400)
        
        # Create layout
        layout = QVBoxLayout()
        
        # Create table
        self.table = QTableWidget()
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(["Action", "Shortcut", "Description"])
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.Stretch)
        
        # Add shortcuts to table
        self.populate_shortcuts()
        
        # Add buttons
        button_layout = QHBoxLayout()
        self.reset_button = QPushButton("Reset to Defaults")
        self.save_button = QPushButton("Save")
        self.cancel_button = QPushButton("Cancel")
        
        self.reset_button.clicked.connect(self.reset_shortcuts)
        self.save_button.clicked.connect(self.save_shortcuts)
        self.cancel_button.clicked.connect(self.reject)
        
        button_layout.addWidget(self.reset_button)
        button_layout.addStretch()
        button_layout.addWidget(self.save_button)
        button_layout.addWidget(self.cancel_button)
        
        # Add widgets to layout
        layout.addWidget(self.table)
        layout.addLayout(button_layout)
        
        self.setLayout(layout)
        
        # Connect cell double-click event
        self.table.cellDoubleClicked.connect(self.edit_shortcut)
        
    def populate_shortcuts(self):
        shortcuts = [
            ("New Tab", "Ctrl+T", "Open a new tab"),
            ("Close Tab", "Ctrl+W", "Close the current tab"),
            ("Reload Page", "Ctrl+R", "Reload the current page"),
            ("Focus URL Bar", "Ctrl+L", "Focus the address bar"),
            ("Toggle Bookmark", "Ctrl+B", "Add or remove bookmark"),
            ("Show History", "Ctrl+H", "Open history panel"),
            ("Show Settings", "Ctrl+,", "Open settings dialog"),
            ("Find in Page", "Ctrl+F", "Search within the current page"),
            ("Zoom In", "Ctrl++", "Increase zoom level"),
            ("Zoom Out", "Ctrl+-", "Decrease zoom level"),
            ("Reset Zoom", "Ctrl+0", "Reset zoom to default"),
            ("Toggle Fullscreen", "F11", "Enter or exit fullscreen mode"),
            ("New Window", "Ctrl+N", "Open a new browser window"),
            ("Quit Browser", "Ctrl+Q", "Close the browser"),
            ("Save Page", "Ctrl+S", "Save the current page"),
            ("Show Downloads", "Ctrl+J", "Open downloads panel"),
            ("Go Back", "Alt+Left", "Navigate to previous page"),
            ("Go Forward", "Alt+Right", "Navigate to next page"),
            ("Go Home", "Alt+Home", "Go to homepage"),
            ("Next Tab", "Ctrl+Tab", "Switch to next tab"),
            ("Previous Tab", "Ctrl+Shift+Tab", "Switch to previous tab"),
            ("Undo", "Ctrl+Z", "Undo last action"),
            ("Redo", "Ctrl+Y", "Redo last action"),
            ("Cut", "Ctrl+X", "Cut selected text"),
            ("Copy", "Ctrl+C", "Copy selected text"),
            ("Paste", "Ctrl+V", "Paste from clipboard"),
            ("Exit Fullscreen", "Escape", "Exit fullscreen mode")
        ]
        
        self.table.setRowCount(len(shortcuts))
        for i, (action, shortcut, description) in enumerate(shortcuts):
            self.table.setItem(i, 0, QTableWidgetItem(action))
            self.table.setItem(i, 1, QTableWidgetItem(shortcut))
            self.table.setItem(i, 2, QTableWidgetItem(description))
            
    def edit_shortcut(self, row, column):
        if column == 1:  # Only allow editing the shortcut column
            item = self.table.item(row, column)
            if item:
                current_shortcut = item.text()
                new_shortcut, ok = QInputDialog.getText(
                    self, "Edit Shortcut",
                    f"Enter new shortcut for {self.table.item(row, 0).text()}:",
                    QLineEdit.Normal,
                    current_shortcut
                )
                if ok and new_shortcut:
                    # Validate the shortcut
                    try:
                        QKeySequence(new_shortcut)
                        item.setText(new_shortcut)
                    except:
                        QMessageBox.warning(
                            self,
                            "Invalid Shortcut",
                            "Please enter a valid keyboard shortcut."
                        )
                        
    def reset_shortcuts(self):
        reply = QMessageBox.question(
            self,
            "Reset Shortcuts",
            "Are you sure you want to reset all shortcuts to their default values?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )
        if reply == QMessageBox.Yes:
            self.populate_shortcuts()
            
    def save_shortcuts(self):
        # TODO: Implement saving shortcuts to settings
        self.accept() 