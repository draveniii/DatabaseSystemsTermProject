# MainWindow.py
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication
import sys

from UserTypePage import UserType
from LoginPage import Login

# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()        

        # MainWindow.ui was created in QT Designer then loaded here
        uic.loadUi('MainWindow.ui', self)
        self.setWindowTitle("Club Management System")

        # Add pages to stackedWidget
        self.userType = UserType()
        self.stackedWidget.addWidget(self.userType)
        self.login = Login()
        self.stackedWidget.addWidget(self.login)

        # Attribute to track the last page accessed
        self.lastPage = None

        # Connect userType buttons to function
        self.userType.studentButton.clicked.connect(
            lambda: self.go_to_login("Student")
        )
        self.userType.facultyButton.clicked.connect(
            lambda: self.go_to_login("Faculty")
        )
        self.userType.adminButton.clicked.connect(
            lambda: self.go_to_login("Admin")
        )

        # Connect login back button to function
        self.login.backButton.clicked.connect(
            lambda: self.go_back_one_page()
        )
        

    # Goes back to previous page
    def go_back_one_page(self):        
        self.stackedWidget.setCurrentWidget(self.lastPage)

    def go_to_login(self, newUserType):
        self.login.set_user_type(newUserType)
        self.set_last_page()
        self.stackedWidget.setCurrentWidget(self.login)

    def set_last_page(self):
        self.lastPage = self.stackedWidget.currentWidget()



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
        



