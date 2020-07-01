import sys
from PyQt5.QtWidgets import *


class Window(QWidget):

    def __init__(self):
        super().__init__()

        # (first two are position, and last two are for sizes in X, Y direction)
        self.setGeometry(50, 50, 450, 450)
        self.setWindowTitle("First PyQt5 Window")

        # To show the window.
        self.show()


App = QApplication(sys.argv)

# Create an instance of class Window
window = Window()
sys.exit(App.exec_())

