from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(479, 492)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.textNameCinema = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textNameCinema.sizePolicy().hasHeightForWidth())
        self.textNameCinema.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textNameCinema.setFont(font)
        self.textNameCinema.setObjectName("textNameCinema")
        self.horizontalLayout.addWidget(self.textNameCinema)
        self.nameCinema = QtWidgets.QLineEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.nameCinema.setFont(font)
        self.nameCinema.setObjectName("nameCinema")
        self.horizontalLayout.addWidget(self.nameCinema)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pici = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pici.sizePolicy().hasHeightForWidth())
        self.pici.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.pici.setFont(font)
        self.pici.setObjectName("pici")
        self.horizontalLayout_2.addWidget(self.pici)
        self.setFilePici = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.setFilePici.setFont(font)
        self.setFilePici.setObjectName("setFilePici")
        self.horizontalLayout_2.addWidget(self.setFilePici)
        self.textShortFilePici = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textShortFilePici.setFont(font)
        self.textShortFilePici.setObjectName("textShortFilePici")
        self.horizontalLayout_2.addWidget(self.textShortFilePici)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.fileCinema = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fileCinema.sizePolicy().hasHeightForWidth())
        self.fileCinema.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.fileCinema.setFont(font)
        self.fileCinema.setObjectName("fileCinema")
        self.horizontalLayout_3.addWidget(self.fileCinema)
        self.setFileCinema = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.setFileCinema.setFont(font)
        self.setFileCinema.setObjectName("setFileCinema")
        self.horizontalLayout_3.addWidget(self.setFileCinema)
        self.textShortFileCinema = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(10)
        self.textShortFileCinema.setFont(font)
        self.textShortFileCinema.setObjectName("textShortFileCinema")
        self.horizontalLayout_3.addWidget(self.textShortFileCinema)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textGenre = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textGenre.sizePolicy().hasHeightForWidth())
        self.textGenre.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textGenre.setFont(font)
        self.textGenre.setObjectName("textGenre")
        self.horizontalLayout_4.addWidget(self.textGenre)
        self.genre_cmb = QtWidgets.QComboBox(Form)
        self.genre_cmb.setObjectName("genre_cmb")
        self.horizontalLayout_4.addWidget(self.genre_cmb)
        self.buttonAddGenre = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.buttonAddGenre.setFont(font)
        self.buttonAddGenre.setObjectName("buttonAddGenre")
        self.horizontalLayout_4.addWidget(self.buttonAddGenre)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textYear = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textYear.sizePolicy().hasHeightForWidth())
        self.textYear.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textYear.setFont(font)
        self.textYear.setObjectName("textYear")
        self.horizontalLayout_5.addWidget(self.textYear)
        self.year_spin = QtWidgets.QSpinBox(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.year_spin.setFont(font)
        self.year_spin.setMinimum(1900)
        self.year_spin.setMaximum(2022)
        self.year_spin.setProperty("value", 2022)
        self.year_spin.setObjectName("year_spin")
        self.horizontalLayout_5.addWidget(self.year_spin)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.textDescription = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.textDescription.setFont(font)
        self.textDescription.setObjectName("textDescription")
        self.horizontalLayout_6.addWidget(self.textDescription)
        self.description_plan = QtWidgets.QPlainTextEdit(Form)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.description_plan.setFont(font)
        self.description_plan.setObjectName("description_plan")
        self.horizontalLayout_6.addWidget(self.description_plan)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.buttonAddCinema = QtWidgets.QPushButton(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonAddCinema.sizePolicy().hasHeightForWidth())
        self.buttonAddCinema.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        self.buttonAddCinema.setFont(font)
        self.buttonAddCinema.setObjectName("buttonAddCinema")
        self.verticalLayout.addWidget(self.buttonAddCinema)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "???????????????? ????????"))
        self.textNameCinema.setText(_translate("Form", "???????????????? ????????"))
        self.pici.setText(_translate("Form", "??????????????????????"))
        self.setFilePici.setText(_translate("Form", "?????????????? ????????"))
        self.textShortFilePici.setText(_translate("Form", "*???????? ???? ????????????"))
        self.fileCinema.setText(_translate("Form", "???????? ????????"))
        self.setFileCinema.setText(_translate("Form", "?????????????? ????????"))
        self.textShortFileCinema.setText(_translate("Form", "*???????? ???? ????????????"))
        self.textGenre.setText(_translate("Form", "????????"))
        self.buttonAddGenre.setText(_translate("Form", "?????????????????????????? ??????????"))
        self.textYear.setText(_translate("Form", "??????"))
        self.textDescription.setText(_translate("Form", "????????????????"))
        self.buttonAddCinema.setText(_translate("Form", "???????????????? ????????"))
