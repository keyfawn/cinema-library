import os
import sys
import shutil
import Utils
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5 import uic
from EditGenreWindow import EditGenre
from AddCinemaWidget import Ui_Form


class AddCinema(QWidget, Ui_Form):
    def __init__(self, parent=None, name=None):
        super(AddCinema, self).__init__()
        #uic.loadUi('designAddCinema.ui', self)
        self.setupUi(self)
        self.db = Utils.DBUtils('cinema.db')
        self.parent = parent
        self.genres = {el[1]: el[0] for el in self.db.get_data('genre', 'id', 'title')}
        self.fillInComboBox()
        self.name = ""
        self.genre = self.genre_cmb.currentText()
        self.year = 2022
        self.description = self.description_plan.toPlainText()
        self.pathPici = None
        self.pathCinema = None
        self.buttonAddGenre.clicked.connect(self.editGenres)
        if not name is None:
            self.nameCinema.setText(name)
            genre, year, description, pathPici, pathCinema = self.db.get_data(
                "cinema",
                "genre",
                "year",
                "description",
                "pathPici",
                "pathCinema",
                name=f"'{name}'")[0]
            genre = self.db.get_data("genre", "title", id=genre)[0][0]
            self.genre_cmb.setCurrentText(genre)
            self.description_plan.setPlainText(description)
            self.year_spin.setValue(int(year))
            self.textShortFileCinema.setText('*файл выбран')
            self.textShortFilePici.setText('*файл выбран')
            self.pathCinema = pathCinema
            self.pathPici = pathPici
            self.setWindowTitle("Изменение фильма")
            self.buttonAddCinema.setText("Изменить")
            self.buttonAddCinema.clicked.connect(self.editCinema)
            self.setFileCinema.clicked.connect(self.editFileCinema)
            self.setFilePici.clicked.connect(self.editFilePici)
            self.name = name
            self.genre = genre
            self.year = int(year)
            self.description = description
        else:
            self.buttonAddCinema.clicked.connect(self.saveCinema)
            self.setFileCinema.clicked.connect(self.addFileCinema)
            self.setFilePici.clicked.connect(self.addFilePici)

    def editGenres(self):
        self.window = EditGenre(self)
        self.setWindowOpacity(0)
        self.window.show()

    def fillInComboBox(self):
        for el in self.genres:
            self.genre_cmb.addItem(el)

    def saveCinema(self):
        if not self.nameCinema.text():
            QMessageBox.critical(self, "Ошибка", "Вы не задали название")
            return
        if self.db.check_film_name(self.nameCinema.text()):
            QMessageBox.critical(self, "Ошибка", "Фильм с таким названием уже есть")
            return
        self.name = self.nameCinema.text()
        if not self.description_plan.toPlainText():
            QMessageBox.critical(self, "Ошибка", "Задайте описание")
            return
        self.description = self.description_plan.toPlainText()
        if self.pathCinema is None:
            QMessageBox.critical(self, "Ошибка", "Выберите фильм")
            return
        self.genre = self.genres[self.genre_cmb.currentText()]
        self.year = self.year_spin.text()
        if self.pathPici is None:
            self.pathPici = "resourses/images/img__.png"
        self.db.add_film(self.name, self.genre, self.year, self.description, self.pathPici, self.pathCinema)
        self.close()

    def editCinema(self):
        if not self.nameCinema.text():
            QMessageBox.critical(self, "Ошибка", "Вы не задали название")
            return
        if self.db.check_film_name(self.nameCinema.text()) and self.nameCinema.text() != self.name:
            QMessageBox.critical(self, "Ошибка", "Фильм с таким названием уже есть")
            return
        old_name = self.name
        self.name = self.nameCinema.text()
        if not self.description_plan.toPlainText():
            QMessageBox.critical(self, "Ошибка", "Задайте описание")
            return
        self.description = self.description_plan.toPlainText()
        if self.pathCinema is None:
            QMessageBox.critical(self, "Ошибка", "Выберите фильм")
            return
        self.genre = self.genres[self.genre_cmb.currentText()]
        self.year = self.year_spin.text()
        if self.pathPici is None:
            self.pathPici = "resourses/images/img__.png"
        self.db.delete_cinema(old_name)
        self.db.add_film(self.name, self.genre, self.year, self.description, self.pathPici, self.pathCinema)
        self.close()

    def addFileCinema(self):
        if not self.nameCinema.text():
            QMessageBox.critical(self, "Ошибка", "Вы не задали название")
            return
        if self.db.check_film_name(self.nameCinema.text()):
            QMessageBox.critical(self, "Ошибка", "Фильм с таким названием уже есть")
            return
        path = QFileDialog.getOpenFileName(self, 'Выбрать кино', '',
                                                          'Видео (*MP4);; Видео (*WebM);; Видео (*MOV);; Видео (*AVI);; Видео (*FLV);; Видео (*WMV);;Все файлы (*)')[0]
        if path:
            self.textShortFileCinema.setText('*файл выбран')
            self.pathCinema = f"resourses/video/vid_{self.nameCinema.text()}_.{Utils.get_file_ex(path)}"
            shutil.copyfile(path, self.pathCinema)

    def addFilePici(self):
        if not self.nameCinema.text():
            QMessageBox.critical(self, "Ошибка", "Вы не задали название")
            return
        if self.db.check_film_name(self.nameCinema.text()):
            QMessageBox.critical(self, "Ошибка", "Фильм с таким названием уже есть")
            return
        path = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '', 'Изображение (*PNG);; Изображение (*JPG);; Все файлы (*)')[0]
        if path:
            self.textShortFilePici.setText('*файл выбран')
            self.pathPici = f"resourses/images/img_{self.nameCinema.text()}_.{Utils.get_file_ex(path)}"
            shutil.copyfile(path, self.pathPici)

    def editFileCinema(self):
        if not self.nameCinema.text():
            QMessageBox.critical(self, "Ошибка", "Вы не задали название")
            return
        if self.db.check_film_name(self.nameCinema.text()) and self.nameCinema.text() != self.name:
            QMessageBox.critical(self, "Ошибка", "Фильм с таким названием уже есть")
            return
        path = QFileDialog.getOpenFileName(self, 'Выбрать кино', '',
                                                          'Видео (*MP4);; Видео (*WebM);; Видео (*MOV);; Видео (*AVI);; Видео (*FLV);; Видео (*WMV);;Все файлы (*)')[0]
        if path:
            self.textShortFileCinema.setText('*файл выбран')
            try:
                os.remove(self.pathCinema)
            except:
                pass
            self.pathCinema = f"resourses/video/vid_{self.nameCinema.text()}_.{Utils.get_file_ex(path)}"
            shutil.copyfile(path, self.pathCinema)

    def editFilePici(self):
        if not self.nameCinema.text():
            QMessageBox.critical(self, "Ошибка", "Вы не задали название")
            return
        if self.db.check_film_name(self.nameCinema.text()) and self.nameCinema.text() != self.name:
            QMessageBox.critical(self, "Ошибка", "Фильм с таким названием уже есть")
            return
        path = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '', 'Изображение (*PNG);; Изображение (*JPG);; Все файлы (*)')[0]
        if path:
            self.textShortFilePici.setText('*файл выбран')
            if self.pathPici != "resourses/images/img__.png":
                try:
                    os.remove(self.pathPici)
                except:
                    pass
            self.pathPici = f"resourses/images/img_{self.nameCinema.text()}_.{Utils.get_file_ex(path)}"
            shutil.copyfile(path, self.pathPici)

    def closeEvent(self, event):
        self.db.close()
        self.parent.ReadFile()
        self.parent.setWindowOpacity(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AddCinema()
    ex.show()
    sys.exit(app.exec())
