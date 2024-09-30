import sys
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 300))

        self.setWindowTitle("My App")
        button = QPushButton("Press Me!")
        self.setCentralWidget(button)

#your app
app = QApplication([])

window = MainWindow()
window.show()

#Execute/Start the event loop.
app.exec()