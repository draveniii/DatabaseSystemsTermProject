# UserTypePage.p
from pathlib import Path

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget

class UserType(QWidget):
    def __init__(self):
        super().__init__()
        ui_file = Path(__file__).resolve().with_name("UserTypePage.ui")
        uic.loadUi(str(ui_file), self)