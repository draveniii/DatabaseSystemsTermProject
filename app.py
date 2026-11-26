import sys
import MainWindow
from PyQt6.QtWidgets import QApplication, QWidget
import sys

WINDOW_WIDTH = 1080
WINDOW_HEIGHT = 720
# You need one (and only one) QApplication instance per application.
# Pass in sys.argv to allow command line arguments for your app.
# If you know you won't use command line arguments QApplication([]) works too.
app = QApplication(sys.argv)



# Create a Qt widget, which will be our window.
window = MainWindow.MainWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

# Start the event loop.
app.exec()


# Your application won't reach here until you exit and the event
# loop has stopped.
