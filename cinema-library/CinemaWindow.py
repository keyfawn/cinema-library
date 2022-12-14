import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
from CinemaWidget import Ui_Form
import Utils
import subprocess


class WindowCinema(QWidget, Ui_Form):
    def __init__(self, parent=None, name="test"):
        super(WindowCinema, self).__init__()
        #uic.loadUi('designWindowCinema.ui', self)
        self.setupUi(self)
        self.parent = parent
        self.db = Utils.DBUtils('cinema.db')
        self.setWindowTitle(name)
        self.nameCinema.setText(name)
        self.nameCinema.adjustSize()

        genre, year, description, pathPici, pathCinema = self.db.get_data(
            "cinema",
            "genre",
            "year",
            "description",
            "pathPici",
            "pathCinema",
            name=f"'{name}'")[0]

        genre = self.db.get_data("genre", "title", id=genre)[0][0]
        self.genre.setText(f'Жанр: {genre}')
        self.genre.adjustSize()
        self.year.setText(f'Год: {year}')
        self.year.adjustSize()
        self.plainTextEdit.setPlainText(description)
        self.pici.setPixmap(QPixmap(pathPici))
        self.pushButton.clicked.connect(self.open_cinema)
        self.pathCinema = pathCinema
        self.setFixedSize(700, 500)

    def open_cinema(self):
        #можно проверку добавить на то, что файл по пути существует
        subprocess.call(os.path.abspath(self.pathCinema), shell=True)

    def closeEvent(self, event):
        self.db.close()
        self.parent.ReadFile()
        self.parent.setWindowOpacity(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WindowCinema()
    ex.show()
    sys.exit(app.exec())
