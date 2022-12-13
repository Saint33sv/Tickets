from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EventRedactWindow(object):
    def setupUi(self, EventRedactWindow):
        EventRedactWindow.setObjectName("EventRedactWindow")
        EventRedactWindow.resize(618, 363)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        EventRedactWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(EventRedactWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(160, 20, 401, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(160, 80, 331, 61))
        self.groupBox_5.setObjectName("groupBox_5")
        self.comboBox_balcony = QtWidgets.QComboBox(self.groupBox_5)
        self.comboBox_balcony.setGeometry(QtCore.QRect(10, 20, 101, 22))
        self.comboBox_balcony.setObjectName("comboBox_balciny")
        self.comboBox_balcony.addItem("")
        self.comboBox_balcony.addItem("")
        self.comboBox_balcony.addItem("")
        self.comboBox_balcony.addItem("")
        self.lineEdit_balcony = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_balcony.setGeometry(QtCore.QRect(130, 20, 91, 20))
        self.lineEdit_balcony.setObjectName("lineEdit_balcony")
        self.pushButton_balcony = QtWidgets.QPushButton(self.groupBox_5)
        self.pushButton_balcony.setGeometry(QtCore.QRect(240, 20, 75, 23))
        self.pushButton_balcony.setObjectName("pushButton_balcony")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(160, 150, 331, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.comboBox_logia = QtWidgets.QComboBox(self.groupBox_3)
        self.comboBox_logia.setGeometry(QtCore.QRect(10, 20, 101, 22))
        self.comboBox_logia.setObjectName("comboBox_logia")
        self.comboBox_logia.addItem("")
        self.comboBox_logia.addItem("")
        self.comboBox_logia.addItem("")
        self.comboBox_logia.addItem("")
        self.lineEdit_logia = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_logia.setGeometry(QtCore.QRect(130, 20, 91, 20))
        self.lineEdit_logia.setObjectName("lineEdit_logia")
        self.pushButton_logia = QtWidgets.QPushButton(self.groupBox_3)
        self.pushButton_logia.setGeometry(QtCore.QRect(240, 20, 75, 23))
        self.pushButton_logia.setObjectName("pushButton_logia")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(160, 240, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(160, 280, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 111, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 80, 141, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(120, 240, 31, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 290, 47, 13))
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(110, 280, 41, 16))
        self.label_5.setObjectName("label_5")
        self.pushButton_redact = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_redact.setGeometry(QtCore.QRect(354, 280, 101, 23))
        self.pushButton_redact.setObjectName("pushButton_redact")
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(480, 280, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        EventRedactWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EventRedactWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 21))
        self.menubar.setObjectName("menubar")
        EventRedactWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EventRedactWindow)
        self.statusbar.setObjectName("statusbar")
        EventRedactWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EventRedactWindow)
        QtCore.QMetaObject.connectSlotsByName(EventRedactWindow)

    def retranslateUi(self, EventRedactWindow):
        _translate = QtCore.QCoreApplication.translate
        EventRedactWindow.setWindowTitle(_translate("EventRedactWindow", "MainWindow"))
        self.groupBox_5.setTitle(_translate("EventRedactWindow", "Балкон"))
        self.comboBox_balcony.setItemText(0, _translate("EventRedactWindow", "Вся локация"))
        self.comboBox_balcony.setItemText(1, _translate("EventRedactWindow", "Ряд 1"))
        self.comboBox_balcony.setItemText(2, _translate("EventRedactWindow", "Ряд 2"))
        self.comboBox_balcony.setItemText(3, _translate("EventRedactWindow", "Ряд 3"))
        self.pushButton_balcony.setText(_translate("EventRedactWindow", "Изменить"))
        self.groupBox_3.setTitle(_translate("EventRedactWindow", "Лоджия"))
        self.comboBox_logia.setItemText(0, _translate("EventRedactWindow", "Вся локация"))
        self.comboBox_logia.setItemText(1, _translate("EventRedactWindow", "Ряд 1"))
        self.comboBox_logia.setItemText(2, _translate("EventRedactWindow", "Ряд 2"))
        self.comboBox_logia.setItemText(3, _translate("EventRedactWindow", "Ряд 3"))
        self.pushButton_logia.setText(_translate("EventRedactWindow", "Изменить"))
        self.label.setText(_translate("EventRedactWindow", "Название события"))
        self.label_2.setText(_translate("EventRedactWindow", "Укажите цены билетов"))
        self.label_3.setText(_translate("EventRedactWindow", "Дата "))
        self.label_5.setText(_translate("EventRedactWindow", "Время"))
        self.pushButton_redact.setText(_translate("EventRedactWindow", "Редактировать"))
        self.pushButton_cancel.setText(_translate("EventRedactWindow", "Отмена"))




