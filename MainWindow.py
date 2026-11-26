# MainWindow.py
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QGridLayout


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self, width, height):
        super().__init__()

        self.setWindowTitle("Club Management System")
        self.setGeometry(100, 100, width, height)

        # Create Elements
        studentButton = QPushButton("Student")
        facultyButton = QPushButton("Faculty")
        adminButton = QPushButton("Admin")

        # Size Elements
        studentButton.setFixedSize(QSize(200, 50))
        facultyButton.setFixedSize(QSize(200, 50))   
        adminButton.setFixedSize(QSize(200, 50)) 

        # Stack elements on top of one another
        v_layout = QVBoxLayout()
        v_layout.addWidget(studentButton)
        v_layout.addWidget(facultyButton)
        v_layout.addWidget(adminButton)

        # Center elements in the middle of the window
        main_content = QWidget()
        main_content.setLayout(v_layout)
        center_container = QWidget()
        container_layout = QGridLayout(center_container)
        container_layout.addWidget(main_content, 0, 0, Qt.AlignmentFlag.AlignCenter)

        self.setCentralWidget(center_container)


