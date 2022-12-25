from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Statistic(object):
    def setupUi(self, Statistic):
        Statistic.setObjectName("Statistic")
        Statistic.resize(400, 300)
        self.textBrowser = QtWidgets.QTextBrowser(Statistic)
        self.textBrowser.setGeometry(QtCore.QRect(5, 11, 391, 251))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_ok = QtWidgets.QPushButton(Statistic)
        self.pushButton_ok.setGeometry(QtCore.QRect(50, 270, 75, 23))
        self.pushButton_ok.setObjectName("pushButton_ok")
        self.pushButton_save = QtWidgets.QPushButton(Statistic)
        self.pushButton_save.setGeometry(QtCore.QRect(250, 270, 75, 23))
        self.pushButton_save.setObjectName("pushButton_save")

        self.retranslateUi(Statistic)
        QtCore.QMetaObject.connectSlotsByName(Statistic)

    def retranslateUi(self, Statistic):
        _translate = QtCore.QCoreApplication.translate
        Statistic.setWindowTitle(_translate("Statistic", "Статистика"))
        self.pushButton_ok.setText(_translate("Statistic", "Ok"))
        self.pushButton_save.setText(_translate("Statistic", "Сохранить"))


