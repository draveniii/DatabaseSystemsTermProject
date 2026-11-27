# MainWindow.py
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys

from UserTypePage import UserType

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Club Management System")

        # mainwindow.ui was created in QT Designer then loaded here
        uic.loadUi('MainWindow.ui', self)
        self.userType = UserType()
        self.stackedWidget.addWidget(self.userType)


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
        



