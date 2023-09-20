import sys
import PyQt5
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction

# add a menu bar with "File", "AI", and "Help" options
app = QApplication(sys.argv)
window = QMainWindow()
window.setGeometry(100, 100, 300, 200)
menubar = window.menuBar()
fileMenu = menubar.addMenu("File")
aiMenu = menubar.addMenu("AI")
helpMenu = menubar.addMenu("Help")

# add a "File" option to create a new file
fileNewAction = QAction("New", window)
fileNewAction.setShortcut("Ctrl+N")
fileNewAction.setStatusTip("Create a new file")
