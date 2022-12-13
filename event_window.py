from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_EventWindow(object):
    def setupUi(self, EventWindow):
        EventWindow.setObjectName("EventWindow")
        EventWindow.resize(618, 363)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        EventWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(EventWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit_name = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_name.setGeometry(QtCore.QRect(160, 20, 401, 20))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(160, 70, 301, 61))
        self.groupBox_5.setObjectName("groupBox_5")
        self.lineEdit_balcony = QtWidgets.QLineEdit(self.groupBox_5)
        self.lineEdit_balcony.setGeometry(QtCore.QRect(200, 20, 91, 20))
        self.lineEdit_balcony.setObjectName("lineEdit_balcony")
        self.label_2 = QtWidgets.QLabel(self.groupBox_5)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.label_2.setObjectName("label_2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(160, 150, 301, 61))
        self.groupBox_3.setObjectName("groupBox_3")
        self.lineEdit_logia = QtWidgets.QLineEdit(self.groupBox_3)
        self.lineEdit_logia.setGeometry(QtCore.QRect(200, 20, 91, 20))
        self.lineEdit_logia.setObjectName("lineEdit_logia")
        self.label_6 = QtWidgets.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 141, 16))
        self.label_6.setObjectName("label_6")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(160, 240, 110, 22))
        self.dateEdit.setObjectName("dateEdit")
        self.timeEdit = QtWidgets.QTimeEdit(self.centralwidget)
        self.timeEdit.setGeometry(QtCore.QRect(160, 280, 118, 22))
        self.timeEdit.setObjectName("timeEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 111, 16))
        self.label.setObjectName("label")
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
        self.pushButton_make = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_make.setGeometry(QtCore.QRect(380, 280, 75, 23))
        self.pushButton_make.setObjectName("pushButton_make")
        self.pushButton_cancel = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_cancel.setGeometry(QtCore.QRect(480, 280, 75, 23))
        self.pushButton_cancel.setObjectName("pushButton_cancel")
        EventWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(EventWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 618, 21))
        self.menubar.setObjectName("menubar")
        EventWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(EventWindow)
        self.statusbar.setObjectName("statusbar")
        EventWindow.setStatusBar(self.statusbar)

        self.retranslateUi(EventWindow)
        QtCore.QMetaObject.connectSlotsByName(EventWindow)

    def retranslateUi(self, EventWindow):
        _translate = QtCore.QCoreApplication.translate
        EventWindow.setWindowTitle(_translate("EventWindow", "MainWindow"))
        self.groupBox_5.setTitle(_translate("EventWindow", "Балкон"))
        self.label_2.setText(_translate("EventWindow", "Укажите цены билетов"))
        self.groupBox_3.setTitle(_translate("EventWindow", "Лоджия"))
        self.label_6.setText(_translate("EventWindow", "Укажите цены билетов"))
        self.label.setText(_translate("EventWindow", "Название события"))
        self.label_3.setText(_translate("EventWindow", "Дата "))
        self.label_5.setText(_translate("EventWindow", "Время"))
        self.pushButton_make.setText(_translate("EventWindow", "Создать"))
        self.pushButton_cancel.setText(_translate("EventWindow", "Отмена"))
