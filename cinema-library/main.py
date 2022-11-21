import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sqlite3


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('designMain.ui', self)
        self.setFixedSize(810, 530)
        self.ReadFile()
        self.addCinema.triggered.connect(self.openWindow_AddCinema)
        self.deleteCinema.triggered.connect(self.delete_cinema)

    def ReadFile(self):
        self.con = sqlite3.connect('cinema.db')
        cur = self.con.cursor()
        self.result = [list(i) for i in cur.execute("""SELECT * FROM cinema""").fetchall()]
        self.load_cinema()

    def load_cinema(self):
        if self.result[0][0]:
            self.listCinema.addItems([cinemaStr[0] for cinemaStr in self.result])
            self.listCinema.itemDoubleClicked.connect(self.openWindow_Cinema)

    def openWindow_AddCinema(self):
        self.window = AddCinema()
        self.window.show()

    def openWindow_Cinema(self, item):
        for y in self.result:
            if y[0] == item.text():
                nameWindow = y[0]
                genreWindow = y[1]
                yearWindow = str(y[2])
                descriptionWindow = y[3]
                pathPiciWindow = y[4]
                pathCinemaWindow = y[5]
                self.window = WindowCinema(nameWindow, genreWindow, yearWindow, descriptionWindow, pathPiciWindow,
                                           pathCinemaWindow)
                self.window.show()

    def delete_cinema(self):
        if self.listCinema.currentRow():
            cur = self.con.cursor()
            for index, i in enumerate(self.result):
                if self.listCinema.currentRow() == index:
                    what = i
            cur.execute(f"""DELETE FROM cinema WHERE name = '{what[0]}'""").fetchall()
            self.con.commit()
            self.listCinema.clear()
            self.ReadFile()

    def check_newCinema(self):
        cur = self.con.cursor()
        what = cur.execute(f"""SELECT id FROM genre WHERE title == '{self.genre.text()}'""").fetchall()
        print(22)
        if not what:
            print(3)
            cur.execute(f"""INSERT INTO genre(title) VALUES('{self.genre.text()}')""")
            what = cur.execute(f"""SELECT id FROM genre WHERE title == '{self.genre.text()}'""")
            print(4)
        cur.execute(
            f"""INSERT INTO cinema(name, genre, year, description, pathPici, pathCinema) VALUES('{self.nameCinema.text()}', '{what}', {self.year.text()}, '{self.description.toPlainText()}', '{self.nameFilePici}', '{self.nameFileCinema}')""").fetchall()
        con.commit()


class AddCinema(QWidget):
    def __init__(self):
        super(AddCinema, self).__init__()
        uic.loadUi('designAddCinema.ui', self)
        self.setFixedSize(500, 450)

        self.buttonAddCinema.clicked.connect(self.saveCinema)
        self.setFileCinema.clicked.connect(self.addFileCinema)
        self.setFilePici.clicked.connect(self.addFilePici)

        self.show()

    def saveCinema(self):
        if self.nameCinema.text() and self.nameFileCinema and self.nameFilePici and self.genre.text() and self.year.text() and self.description.toPlainText():
            print(1)
            ex.check_newCinema()
            print(2)
            ex.listCinema.clear()
            ex.ReadFile()
            self.close()
        else:
            valid = QMessageBox.question(self, 'Ошибка', 'Ошибка заполнения нового кино', QMessageBox.Ok)

    def addFileCinema(self):
        self.nameFileCinema = QFileDialog.getOpenFileName(self, 'Выбрать кино', '',
                                                          'Видео (*WebM);; Видео (*MOV);; Видео (*MP4);; Видео (*AVI);; Видео (*FLV);; Видео (*WMV)')[
            0]
        if self.nameFileCinema:
            self.textShortFileCinema.setText('*файл выбран')

    def addFilePici(self):
        self.nameFilePici = \
        QFileDialog.getOpenFileName(self, 'Выбрать картинку', '', 'Изображение (*JPG);; Изображение (*PNG)')[0]
        if self.nameFilePici:
            self.textShortFilePici.setText('*файл выбран')


class WindowCinema(QWidget):
    def __init__(self, name, genre, year, description, pathPici, pathCinema):
        super(WindowCinema, self).__init__()
        uic.loadUi('designWindowCinema.ui', self)

        self.setWindowTitle(name)
        self.nameCinema.setText(name)
        self.nameCinema.adjustSize()
        cur = ex.con
        cur = cur.cursor()
        print('he')
        genre = cur.execute(f"""SELECT title WHERE id == '{genre}'""").fetchall()
        self.genre.setText(f'Жанр: {genre}')
        self.genre.adjustSize()
        self.year.setText(f'Год: {year}')
        self.year.adjustSize()
        self.plainTextEdit.setPlainText(description)
        self.pici.setPixmap(QPixmap(pathPici))
        self.pushButton.clicked.connect(self.open_cinema)
        self.pathCinema = pathCinema

        self.setFixedSize(700, 500)

        self.show()

    def open_cinema(self):
        os.startfile(self.pathCinema)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    ex.con.close()
    sys.exit(app.exec())