import sys
from PyQt5.QtWidgets import *


class Window(QWidget):

    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("PyQt5 Buttons")
        self.setGeometry(50, 50, 300, 300)
        self.ui()

    def ui(self):
        self.text = QLabel("Just a Label", self)
        self.text.move(110, 10)
        enter_button = QPushButton("Enter", self)
        exit_button = QPushButton("Exit", self)
        enter_button.move(50, 30)
        exit_button.move(150, 30)

        enter_button.clicked.connect(self.enter_func)
        exit_button.clicked.connect(self.exit_func)

        self.show()

    def enter_func(self):
        self.text.setText("You clicked Enter")
        self.text.resize(150, 10)

    def exit_func(self):
        self.text.setText("You clicked Exit")
        self.text.resize(150, 10)


def main():
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec_())


if __name__ == '__main__':
    main()
