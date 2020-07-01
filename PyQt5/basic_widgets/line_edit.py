import sys
from PyQt5.QtWidgets import *

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle("Line Edit")
        self.setGeometry(50, 50, 350, 350)
        self.ui()

    def ui(self):
        self.text_box = QLineEdit(self)
        self.text_box.setPlaceholderText("You Name:")
        self.text_box.move(110, 10)

        self.pass_box = QLineEdit(self)
        self.pass_box.setPlaceholderText("Your Password:")
        self.pass_box.setEchoMode(QLineEdit.Password)
        self.pass_box.move(110, 40)

        button = QPushButton("Save", self)
        button.move(140, 70)
        button.clicked.connect(self.get_values)

        self.show()

    def get_values(self):

        name = self.text_box.text()
        password = self.pass_box.text()
        print(name, password)
        self.setWindowTitle(f"Your name is {name}")



def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
