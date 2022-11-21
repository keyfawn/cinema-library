import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFileDialog, QMessageBox
from PyQt5.QtGui import QPixmap
from PyQt5 import uic
import sqlite3

class DBUtils:
    def __init__(self, name_db):
        self.con = sqlite3.connect(name_db)

    def create_execute(self, execute):
        cur = self.con.cursor()
        if execute[:6] == 'SELECT':
            return cur.execute(execute).fetchall()
        cur.execute(execute).fetchall()
        self.con.commit()