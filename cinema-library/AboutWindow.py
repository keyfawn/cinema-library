import sys
from PyQt5.QtWidgets import QApplication, QWidget
from AboutWidget import Ui_Form


class WindowAbout(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WindowAbout()
    sys.exit(app.exec())
