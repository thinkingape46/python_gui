import  sys
from PyQt5.QtWidgets import *

class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Using Labels")
        self.setGeometry(50, 50, 400, 400)
        self.ui()

    # Create a new function for UI widgets.

    def ui(self):
        text1 = QLabel("Hello Python", self)
        text2 = QLabel("Hello PyQt5", self)
        # Move the label using the move method.
        text1.move(100, 50)
        text2.move(250, 50)
        self.show()


def main():
    # More professional way
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == "__main__":
    main()
