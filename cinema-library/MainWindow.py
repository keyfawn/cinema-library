import os
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox
from PyQt5 import uic
from Utils import DBUtils
from AboutWindow import WindowAbout
from CinemaWindow import WindowCinema
from AddCinemaWindow import AddCinema
from MainWidget import Ui_MainWindow


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        #uic.loadUi('designMain.ui', self)
        self.setupUi(self)
        self.setFixedSize(810, 530)
        self.db = DBUtils('cinema.db')
        self.ReadFile()
        self.update_sort.clicked.connect(self.updateSort)

        self.about_programm.triggered.connect(self.aboutProgramm)

        self.addCinema.triggered.connect(self.openWindow_AddCinema)
        self.button_create.clicked.connect(self.openWindow_AddCinema)

        self.editCinema.triggered.connect(self.openWindow_EditCinema)
        self.button_edit.clicked.connect(self.openWindow_EditCinema)

        self.deleteCinema.triggered.connect(self.delete_cinema)
        self.button_delete.clicked.connect(self.delete_cinema)

        for x in [self.nameCinema, self.genre, self.year, self.description]:
            x.setHidden(True)

    def aboutProgramm(self):
        self.window = WindowAbout()
        self.show()

    def updateSort(self):
        temp_name = self.result.copy()
        if self.sort3.currentIndex() == 0:
            temp_name.sort()
        elif self.sort3.currentIndex() == 1:
            temp_name.sort(reverse=True)
        elif self.sort3.currentIndex() == 2:
            temp_name.clear()
            title_genres = self.db.get_data('genre', 'id')
            for gen in title_genres:
                title = [el[0] for el in self.db.get_data('cinema', 'name', genre=gen[0])]
                temp_name.extend(title)
        elif self.sort3.currentIndex() == 3:
            temp_name = []
            years = list(set([int(x[0]) for x in self.db.get_data('cinema', 'year')]))
            years.sort()
            for y in years:
                title = [el[0] for el in self.db.get_data('cinema', 'name', year=y)]
                temp_name.extend(title)
        self.result = temp_name.copy()
        self.load_cinema()

    def ReadFile(self):
        self.result = [i[0] for i in self.db.get_data('cinema')]
        self.load_cinema()

    def load_cinema(self):
        if self.result:
            self.listCinema.clear()
            self.listCinema.addItems(self.result)
            self.listCinema.itemDoubleClicked.connect(self.openWindow_Cinema)
            self.listCinema.itemClicked.connect(self.start_shortDescription)

    def start_shortDescription(self):
        film_name = self.listCinema.currentItem().text()
        film_data = self.get_film_data(film_name)
        for x in [self.nameCinema, self.genre, self.year, self.description]:
            x.setHidden(False)
        self.nameCinema.setText(self.listCinema.currentItem().text())
        self.genre.setText(f'Жанр: {self.db.get_data("genre", "title", id=film_data[0])[0][0]}')
        self.year.setText(f'Год: {film_data[1]}')
        self.description.setPlainText(film_data[2])

    def openWindow_AddCinema(self):
        self.window = AddCinema(self)
        self.setWindowOpacity(0)
        self.window.show()

    def openWindow_EditCinema(self):
        if not self.listCinema.selectedItems():
            QMessageBox.critical(self, "Ошибка", "Вы не выбрали фильм для изменения")
            return
        name = list(set([i.text() for i in self.listCinema.selectedItems()]))[0]
        self.window = AddCinema(self, name)
        self.window.show()

    def openWindow_Cinema(self, item):
        self.window = WindowCinema(self, item.text())
        self.setWindowOpacity(0)
        self.window.show()

    def delete_cinema(self):
        if not self.listCinema.selectedItems():
            QMessageBox.critical(self, "Ошибка", "Вы не выбрали фильм для удаления")
            return
        name = list(set([i.text() for i in self.listCinema.selectedItems()]))[0]
        data = self.get_film_data(name)
        if name:
            self.db.delete_cinema(name)
        try:
            os.remove(data[4])
        except:
            pass
        if data[3] != "resourses/images/img__.png":
            try:
                os.remove(data[3])
            except:
                pass
        self.ReadFile()

    def get_film_data(self, name):
        genre, year, description, pathPici, pathCinema = self.db.get_data(
            "cinema",
            "genre",
            "year",
            "description",
            "pathPici",
            "pathCinema",
            name=f"'{name}'")[0]
        return genre, year, description, pathPici, pathCinema


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec())
