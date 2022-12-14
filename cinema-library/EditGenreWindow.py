import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox, QTableWidgetItem, QHeaderView
from Utils import DBUtils
from AddGenreWidget import Ui_Form


class EditGenre(QWidget, Ui_Form):
    def __init__(self, parent=None):
        super().__init__()
        self.setupUi(self)
        self.db = DBUtils('cinema.db')
        self.genres = {el[1]: el[0] for el in self.db.get_data('genre', 'id', 'title')}
        self.create_table()
        self.selected = None
        self.tableWidget.itemDoubleClicked.connect(self.get_item)
        self.tableWidget.itemClicked.connect(self.pas_act)
        self.add_button.clicked.connect(self.add_genre)
        self.delete_button.clicked.connect(self.delete_genre)
        self.edit_button.clicked.connect(self.edit_genre)
        self.parent = parent

    def create_table(self):
        self.genres = {el[1]: el[0] for el in self.db.get_data('genre', 'id', 'title')}
        result = self.prepare_table(self.genres)
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderItem(0, QTableWidgetItem('id'))
        self.tableWidget.setHorizontalHeaderItem(1, QTableWidgetItem('Жанр'))
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.Stretch)
        for i, el in enumerate(result):
            for j, val in enumerate(el):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def add_genre(self):
        if not self.name.text():
            QMessageBox.critical(self, "Ошибка", "Вы не задали название")
            return
        if self.name.text() in [i[0] for i in self.db.get_data("genre", "title")]:
            self.name.setText("")
            QMessageBox.critical(self, "Ошибка", "Такой жанр уже есть в таблице")
            return
        self.db.add_genre(self.name.text())
        self.name.setText("")
        self.create_table()

    def edit_genre(self):
        print(self.selected)
        if not self.name.text():
            QMessageBox.critical(self, "Ошибка", "Вы не выбрали жанр")
            return
        if self.selected not in [i[0] for i in self.db.get_data("genre", "id")]:
            QMessageBox.critical(self, "Ошибка", "Такого жанра нет")
            return
        self.db.update_genre(self.selected, self.name.text())
        self.name.setText("")
        self.create_table()

    def delete_genre(self):

        if not self.name.text():
            QMessageBox.critical(self, "Ошибка", "Вы не выбрали жанр")
            return
        if self.selected not in [i[0] for i in self.db.get_data("genre", "id")]:
            QMessageBox.critical(self, "Ошибка", "Такого жанра нет")
            return
        self.db.delete_genre('genre', self.selected)
        self.name.setText("")
        self.create_table()

    def pas_act(self):
        pass

    def get_item(self, item):
        if item.text().isdigit():
            self.selected = int(item.text())
            genre_name = self.db.get_data("genre", "title", id=self.selected)[0][0]
        else:
            self.selected = self.genres[item.text()]
            genre_name = item.text()
        self.name.setText(genre_name)

    def prepare_table(self, data):
        res = []
        for key, value in data.items():
            res.append([value, key])
        return res

    def closeEvent(self, event):
        self.db.close()
        self.parent.setWindowOpacity(1)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EditGenre()
    ex.show()
    sys.exit(app.exec())
