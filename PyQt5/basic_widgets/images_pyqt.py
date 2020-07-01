import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Images with p=PyQt5")
        self.setGeometry(50, 50, 250, 250)
        self.ui()

    def ui(self):
        self.image = QLabel(self)
        self.image.setPixmap(QPixmap("images/one.png"))
        self.image.move(50, 10)

        remove_button = QPushButton("Hide", self)
        remove_button.move(150, 200)
        remove_button.clicked.connect(self.hide_img)

        show_button = QPushButton("Show", self)
        show_button.move(60, 200)
        show_button.clicked.connect(self.show_img)

        self.show()

    def hide_img(self):
        self.image.hide()

    def show_img(self):
        self.image.show()
        print("showclick")


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
