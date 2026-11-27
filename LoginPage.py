# LoginPage
from pathlib import Path
from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

class Login(QWidget):
    def __init__(self):
        super().__init__()
        ui_file = Path(__file__).resolve().with_name("LoginPage.ui")
        uic.loadUi(str(ui_file), self)

        self.userType = None

    def set_user_type(self, newUserType):
        self.userType = newUserType
        self.label_2.setText(self.userType) 