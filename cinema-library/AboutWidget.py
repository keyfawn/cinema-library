from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(490, 390)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        Form.setFont(font)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.about_prog = QtWidgets.QLabel(Form)
        self.about_prog.setGeometry(QtCore.QRect(20, 20, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.about_prog.setFont(font)
        self.about_prog.setObjectName("about_prog")
        self.all = QtWidgets.QLabel(Form)
        self.all.setGeometry(QtCore.QRect(20, 70, 461, 121))
        self.all.setTextFormat(QtCore.Qt.AutoText)
        self.all.setObjectName("all")
        self.author = QtWidgets.QLabel(Form)
        self.author.setGeometry(QtCore.QRect(70, 320, 401, 41))
        self.author.setObjectName("author")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "О программе"))
        self.about_prog.setText(_translate("Form", "О программе:"))
        self.all.setText(_translate("Form", "Кинотека - это программа, в которой можно хранить свои\n"
"фильмы, мультфильмы. Есть возможность добавлять кино при\n"
"нажатии Ctrl + A, изменить выбранный фильм с помощью\n"
"Ctrl + E и удалить выделенный мультфильм - Ctrl + D.\n"
"Имеется возможность отсортировать список названий\n"
"фильмов."))
        self.author.setText(_translate("Form", "Автор:     █▀ ▄▀█ █░█ █ █▄░█   █▀█ █░░ █▀▀ █▀▀\n"
"                 ▄█ █▀█ ▀▄▀ █ █░▀█   █▄█ █▄▄ ██▄ █▄█"))
