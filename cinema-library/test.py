import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sqlite3
from Utils import DBUtils


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('designMain.ui', self)
        self.setFixedSize(810, 530)
        self.ReadFile()
        self.addCinema.triggered.connect(self.openWindow_AddCinema)
        self.editCinema.triggered.connect(self.openWindow_EditCinema)
        self.deleteCinema.triggered.connect(self.delete_cinema)
        self.about_programm.triggered.connect(self.aboutProgramm)
        self.update_sort.clicked.connect(self.updateSort)
        self.button_create.clicked.connect(self.openWindow_AddCinema)
        self.button_edit.clicked.connect(self.openWindow_EditCinema)
        self.about_programm.triggered.connect(self.aboutProgramm)

        for x in [self.nameCinema, self.genre, self.year, self.description]:
            x.setHidden(True)

    def aboutProgramm(self):
        self.window = WindowAbout()
        self.show()

    def updateSort(self):
        temp, temp_name = [], []
        for sort in self.result:
            temp_name.append(sort[0])
        if self.sort3.currentIndex() == 0:
            temp_name.sort()
        elif self.sort3.currentIndex() == 1:
            temp_name.sort(reverse=True)
        elif self.sort3.currentIndex() == 2:
            genres = DBUtils('cinema.db')
            temp_name.clear()
            title_genres = genres.create_execute(f"""SELECT id FROM genre""")
            for genre in title_genres:
                title = genres.create_execute(f"""SELECT name FROM cinema WHERE genre = {genre[0]}""")
                for cinema in title:
                    temp_name.append(cinema[0])
        elif self.sort3.currentIndex() == 3:
            genres = DBUtils('cinema.db')
            temp_name.clear()
            title_genres = genres.create_execute(f"""SELECT year FROM cinema""")
            title_genres = list(map(lambda x: int(x[0]), title_genres))
            title_genres.sort()
            for genre in title_genres:
                title = genres.create_execute(f"""SELECT name FROM cinema WHERE year = {genre}""")
                for cinema in title:
                    temp_name.append(cinema[0])
        for i in temp_name:
            for j in self.result:
                if i == j[0]:
                    temp.append(j)
        self.result = temp.copy()
        self.listCinema.clear()
        self.load_cinema()

    def ReadFile(self):
        self.con = sqlite3.connect('cinema.db')

        self.result = [list(i) for i in self.create_execute("""SELECT * FROM cinema""")]
        self.load_cinema()

    def load_cinema(self):
        if self.result[0][0]:
            self.listCinema.addItems([cinemaStr[0] for cinemaStr in self.result])
            self.listCinema.itemDoubleClicked.connect(self.openWindow_Cinema)
            self.listCinema.itemClicked.connect(self.start_shortDescription)

    def start_shortDescription(self):
        for cin in self.result:
            if cin[0] == self.listCinema.currentItem().text():
                cinema = cin
        for x in [self.nameCinema, self.genre, self.year, self.description]:
            x.setHidden(False)
        self.nameCinema.setText(cinema[0])
        genre = DBUtils('cinema.db')
        self.genre.setText(f'Жанр: {genre.create_execute(f"SELECT title FROM genre WHERE id = {cinema[1]}")[0][0]}')
        self.year.setText(f'Год: {cinema[2]}')
        self.description.setText(cinema[3])

    def openWindow_AddCinema(self):
        self.window = AddCinema()
        self.window.show()

    def openWindow_EditCinema(self):
        if self.listCinema.currentItem().text() != None:
            for cin in self.result:
                if cin[0] == self.listCinema.currentItem().text():
                    cinema = cin
            self.window = AddCinema()
            self.window.nameCinema.setText(cinema[0])
            genre_db = DBUtils('cinema.db')
            genre = genre_db.create_execute(f"""SELECT title FROM genre WHERE id = {cinema[1]}""")
            self.window.genre.setText(genre[0][0])
            self.window.description.setPlainText(cinema[3])
            self.window.year.setValue(cinema[2])
            self.window.textShortFileCinema.setText('*файл выбран')
            self.window.textShortFilePici.setText('*файл выбран')
            self.window.nameFileCinema = cinema[5]
            self.window.nameFilePici = cinema[4]
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
            for index, i in enumerate(self.result):
                if self.listCinema.currentRow() == index:
                    what = i
            self.create_execute(f"""DELETE FROM cinema WHERE name = '{what[0]}'""")
            self.con.commit()
            self.listCinema.clear()
            self.ReadFile()

    def check_newCinema(self, genre):
        print('start')
        print(genre)
        genr = DBUtils('cinema.db')
        what = genr.create_execute(f"""SELECT id FROM genre WHERE title = '{genre}'""")
        print(what)
        if not what:
            print(3)
            genr.create_execute(f"""INSERT INTO genre(title) VALUES('{genre}')""")
            what = genr.create_execute(f"""SELECT id FROM genre WHERE title = '{genre}'""")
            print(4)
        print('low')
        return what

    def create_execute(self, execute):
        cur = self.con.cursor()
        if execute[:6] == 'SELECT':
            return cur.execute(execute).fetchall()
        else:
            cur.execute(execute).fetchall()


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
            what = ex.check_newCinema(self.genre.text())
            print(2)
            genr = DBUtils('cinema.db')
            genr.create_execute(f"""INSERT INTO cinema(name, genre, year, description, pathPici, pathCinema) VALUES('{self.nameCinema.text()}', '{what[0][0]}', {self.year.text()}, '{self.description.toPlainText()}', '{self.nameFilePici}', '{self.nameFileCinema}')""")
            print(55)
            ex.listCinema.clear()
            ex.ReadFile()
            self.close()
        else:
            valid = QMessageBox.question(self, 'Ошибка', 'Ошибка заполнения нового кино', QMessageBox.Ok)

    def addFileCinema(self):
        self.nameFileCinema = QFileDialog.getOpenFileName(self, 'Выбрать кино', '',
                                                          'Видео (*WebM);; Видео (*MOV);; Видео (*MP4);; Видео (*AVI);; Видео (*FLV);; Видео (*WMV)')[0]
        if self.nameFileCinema:
            self.textShortFileCinema.setText('*файл выбран')

    def addFilePici(self):
        self.nameFilePici = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '', 'Изображение (*JPG);; Изображение (*PNG)')[0]
        if self.nameFilePici:
            self.textShortFilePici.setText('*файл выбран')


class WindowCinema(QWidget):
    def __init__(self, name, genre, year, description, pathPici, pathCinema):
        super(WindowCinema, self).__init__()
        uic.loadUi('designWindowCinema.ui', self)

        self.setWindowTitle(name)
        self.nameCinema.setText(name)
        self.nameCinema.adjustSize()
        self.ut = DBUtils('cinema.db')
        genre = self.ut.create_execute(f"""SELECT title FROM genre WHERE id = {genre}""")[0][0]
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


class WindowAbout(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('designAbout.ui', self)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    ex.con.close()
    sys.exit(app.exec())