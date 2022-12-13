from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window_choise(object):
    def setupUi(self, Window_choise):
        Window_choise.setObjectName("Window_choise")
        Window_choise.resize(357, 83)
        self.centralwidget = QtWidgets.QWidget(Window_choise)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(10, 10, 331, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_bay = QtWidgets.QPushButton(self.widget)
        self.pushButton_bay.setObjectName("pushButton_bay")
        self.horizontalLayout.addWidget(self.pushButton_bay)
        self.pushButton_block = QtWidgets.QPushButton(self.widget)
        self.pushButton_block.setObjectName("pushButton_block")
        self.horizontalLayout.addWidget(self.pushButton_block)
        self.pushButton_clean = QtWidgets.QPushButton(self.widget)
        self.pushButton_clean.setObjectName("pushButton_clean")
        self.horizontalLayout.addWidget(self.pushButton_clean)
        self.pushButton_cuncel = QtWidgets.QPushButton(self.widget)
        self.pushButton_cuncel.setObjectName("pushButton_cuncel")
        self.horizontalLayout.addWidget(self.pushButton_cuncel)
        Window_choise.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Window_choise)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 357, 21))
        self.menubar.setObjectName("menubar")
        Window_choise.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Window_choise)
        self.statusbar.setObjectName("statusbar")
        Window_choise.setStatusBar(self.statusbar)

        self.retranslateUi(Window_choise)
        QtCore.QMetaObject.connectSlotsByName(Window_choise)

    def retranslateUi(self, Window_choise):
        _translate = QtCore.QCoreApplication.translate
        Window_choise.setWindowTitle(_translate("Window_choise", "Продажа билетов"))
        self.pushButton_bay.setText(_translate("Window_choise", "Купить"))
        self.pushButton_block.setText(_translate("Window_choise", "Забронировать"))
        self.pushButton_clean.setText(_translate("Window_choise", "Очистить"))
        self.pushButton_cuncel.setText(_translate("Window_choise", "Отмена"))
