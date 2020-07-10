import sys
from PyQt5.QtWidgets import *

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Checkboxes")
        self.setGeometry(50, 50, 250, 250)
        self.ui()

    def ui(self):

        self.first_name = QLineEdit(self)
        self.first_name.move(70, 50)
        self.first_name.setPlaceholderText("First Name")

        self.last_name = QLineEdit(self)
        self.last_name.move(70, 90)
        self.last_name.setPlaceholderText("Last Name")

        self.remember = QCheckBox("Remember me", self)
        self.remember.move(70, 130)

        button = QPushButton("Submit", self)
        button.move(85, 160)
        button.clicked.connect(self.submit)

        self.show()

    def submit(self):

        if self.remember.isChecked():
            print(f"First Name: {self.first_name.text()}\nLast Name: {self.last_name.text()}")
            self.first_name.clear()
            self.last_name.clear()

        else:
            print("Nothing is saved")


def main():
    app = QApplication(sys.argv)
    window = Window()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()