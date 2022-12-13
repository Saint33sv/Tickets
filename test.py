from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    list_all_price_buttons = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(546, 580)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(140, 60, 279, 434))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_balcony = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_balcony.setObjectName("groupBox_balcony")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_balcony)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_row_3 = QtWidgets.QGroupBox(self.groupBox_balcony)
        self.groupBox_row_3.setObjectName("groupBox_row_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_row_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.pushButton_25 = QtWidgets.QPushButton(self.groupBox_row_3)
        self.pushButton_25.setObjectName("pushButton_25")
        self.horizontalLayout_3.addWidget(self.pushButton_25)
        self.pushButton_26 = QtWidgets.QPushButton(self.groupBox_row_3)
        self.pushButton_26.setObjectName("pushButton_26")
        self.horizontalLayout_3.addWidget(self.pushButton_26)
        self.pushButton_27 = QtWidgets.QPushButton(self.groupBox_row_3)
        self.pushButton_27.setObjectName("pushButton_27")
        self.horizontalLayout_3.addWidget(self.pushButton_27)
        self.verticalLayout.addWidget(self.groupBox_row_3)
        self.groupBox_row_2 = QtWidgets.QGroupBox(self.groupBox_balcony)
        self.groupBox_row_2.setObjectName("groupBox_row_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_row_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton_22 = QtWidgets.QPushButton(self.groupBox_row_2)
        self.pushButton_22.setObjectName("pushButton_22")
        self.horizontalLayout_2.addWidget(self.pushButton_22)
        self.pushButton_23 = QtWidgets.QPushButton(self.groupBox_row_2)
        self.pushButton_23.setObjectName("pushButton_23")
        self.horizontalLayout_2.addWidget(self.pushButton_23)
        self.pushButton_24 = QtWidgets.QPushButton(self.groupBox_row_2)
        self.pushButton_24.setObjectName("pushButton_24")
        self.horizontalLayout_2.addWidget(self.pushButton_24)
        self.verticalLayout.addWidget(self.groupBox_row_2)
        self.groupBox_row_1 = QtWidgets.QGroupBox(self.groupBox_balcony)
        self.groupBox_row_1.setObjectName("groupBox_row_1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_row_1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_19 = QtWidgets.QPushButton(self.groupBox_row_1)
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout.addWidget(self.pushButton_19)
        self.pushButton_20 = QtWidgets.QPushButton(self.groupBox_row_1)
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout.addWidget(self.pushButton_20)
        self.pushButton_21 = QtWidgets.QPushButton(self.groupBox_row_1)
        self.pushButton_21.setObjectName("pushButton_21")
        self.horizontalLayout.addWidget(self.pushButton_21)
        self.verticalLayout.addWidget(self.groupBox_row_1)
        self.verticalLayout_3.addWidget(self.groupBox_balcony)
        self.groupBox_loggia = QtWidgets.QGroupBox(self.layoutWidget)
        self.groupBox_loggia.setObjectName("groupBox_loggia")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_loggia)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_row_4 = QtWidgets.QGroupBox(self.groupBox_loggia)
        self.groupBox_row_4.setObjectName("groupBox_row_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_row_4)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_28 = QtWidgets.QPushButton(self.groupBox_row_4)
        self.pushButton_28.setObjectName("pushButton_28")
        self.horizontalLayout_4.addWidget(self.pushButton_28)
        self.pushButton_29 = QtWidgets.QPushButton(self.groupBox_row_4)
        self.pushButton_29.setObjectName("pushButton_29")
        self.horizontalLayout_4.addWidget(self.pushButton_29)
        self.pushButton_30 = QtWidgets.QPushButton(self.groupBox_row_4)
        self.pushButton_30.setObjectName("pushButton_30")
        self.horizontalLayout_4.addWidget(self.pushButton_30)
        self.verticalLayout_2.addWidget(self.groupBox_row_4)
        self.groupBox_row_5 = QtWidgets.QGroupBox(self.groupBox_loggia)
        self.groupBox_row_5.setObjectName("groupBox_row_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_row_5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton_31 = QtWidgets.QPushButton(self.groupBox_row_5)
        self.pushButton_31.setObjectName("pushButton_31")
        self.horizontalLayout_5.addWidget(self.pushButton_31)
        self.pushButton_32 = QtWidgets.QPushButton(self.groupBox_row_5)
        self.pushButton_32.setObjectName("pushButton_32")
        self.horizontalLayout_5.addWidget(self.pushButton_32)
        self.pushButton_33 = QtWidgets.QPushButton(self.groupBox_row_5)
        self.pushButton_33.setObjectName("pushButton_33")
        self.horizontalLayout_5.addWidget(self.pushButton_33)
        self.verticalLayout_2.addWidget(self.groupBox_row_5)
        self.groupBox_row_6 = QtWidgets.QGroupBox(self.groupBox_loggia)
        self.groupBox_row_6.setObjectName("groupBox_row_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.groupBox_row_6)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.pushButton_34 = QtWidgets.QPushButton(self.groupBox_row_6)
        self.pushButton_34.setObjectName("pushButton_34")
        self.horizontalLayout_6.addWidget(self.pushButton_34)
        self.pushButton_35 = QtWidgets.QPushButton(self.groupBox_row_6)
        self.pushButton_35.setObjectName("pushButton_35")
        self.horizontalLayout_6.addWidget(self.pushButton_35)
        self.pushButton_36 = QtWidgets.QPushButton(self.groupBox_row_6)
        self.pushButton_36.setObjectName("pushButton_36")
        self.horizontalLayout_6.addWidget(self.pushButton_36)
        self.verticalLayout_2.addWidget(self.groupBox_row_6)
        self.verticalLayout_3.addWidget(self.groupBox_loggia)
        self.pushButton_bake = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_bake.setGeometry(QtCore.QRect(440, 380, 75, 23))
        self.pushButton_bake.setObjectName("pushButton_bake")
        self.pushButton_delete = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_delete.setGeometry(QtCore.QRect(440, 340, 75, 23))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 491, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 546, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_balcony.setTitle(_translate("MainWindow", "Балкон"))
        self.groupBox_row_3.setTitle(_translate("MainWindow", "Ряд 3"))
        self.pushButton_25.setText(_translate("MainWindow", "1"))
        self.pushButton_26.setText(_translate("MainWindow", "2"))
        self.pushButton_27.setText(_translate("MainWindow", "3"))
        self.groupBox_row_2.setTitle(_translate("MainWindow", "Ряд 2"))
        self.pushButton_22.setText(_translate("MainWindow", "1"))
        self.pushButton_23.setText(_translate("MainWindow", "2"))
        self.pushButton_24.setText(_translate("MainWindow", "3"))
        self.groupBox_row_1.setTitle(_translate("MainWindow", "Ряд 1"))
        self.pushButton_19.setText(_translate("MainWindow", "1"))
        self.pushButton_20.setText(_translate("MainWindow", "2"))
        self.pushButton_21.setText(_translate("MainWindow", "3"))
        self.groupBox_loggia.setTitle(_translate("MainWindow", "Лоджия"))
        self.groupBox_row_4.setTitle(_translate("MainWindow", "Ряд 3"))
        self.pushButton_28.setText(_translate("MainWindow", "1"))
        self.pushButton_29.setText(_translate("MainWindow", "2"))
        self.pushButton_30.setText(_translate("MainWindow", "3"))
        self.groupBox_row_5.setTitle(_translate("MainWindow", "Ряд 2"))
        self.pushButton_31.setText(_translate("MainWindow", "1"))
        self.pushButton_32.setText(_translate("MainWindow", "2"))
        self.pushButton_33.setText(_translate("MainWindow", "3"))
        self.groupBox_row_6.setTitle(_translate("MainWindow", "Ряд 1"))
        self.pushButton_34.setText(_translate("MainWindow", "1"))
        self.pushButton_35.setText(_translate("MainWindow", "2"))
        self.pushButton_36.setText(_translate("MainWindow", "3"))
        self.pushButton_bake.setText(_translate("MainWindow", "Назад"))
        self.pushButton_delete.setText(_translate("MainWindow", "Удалить"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.list_all_price_buttons.append(self.pushButton_34)
        self.list_all_price_buttons.append(self.pushButton_35)
        self.list_all_price_buttons.append(self.pushButton_36)
        self.list_all_price_buttons.append(self.pushButton_31)
        self.list_all_price_buttons.append(self.pushButton_32)
        self.list_all_price_buttons.append(self.pushButton_33)
        self.list_all_price_buttons.append(self.pushButton_28)
        self.list_all_price_buttons.append(self.pushButton_29)
        self.list_all_price_buttons.append(self.pushButton_30)
        self.list_all_price_buttons.append(self.pushButton_19)
        self.list_all_price_buttons.append(self.pushButton_20)
        self.list_all_price_buttons.append(self.pushButton_21)
        self.list_all_price_buttons.append(self.pushButton_22)
        self.list_all_price_buttons.append(self.pushButton_23)
        self.list_all_price_buttons.append(self.pushButton_24)
        self.list_all_price_buttons.append(self.pushButton_25)
        self.list_all_price_buttons.append(self.pushButton_26)
        self.list_all_price_buttons.append(self.pushButton_27)

    def connected_buttons(self, def_send):
        self.pushButton_34.clicked.connect(def_send)
        self.pushButton_35.clicked.connect(def_send)
        self.pushButton_36.clicked.connect(def_send)
        self.pushButton_31.clicked.connect(def_send)
        self.pushButton_32.clicked.connect(def_send)
        self.pushButton_33.clicked.connect(def_send)
        self.pushButton_28.clicked.connect(def_send)
        self.pushButton_29.clicked.connect(def_send)
        self.pushButton_30.clicked.connect(def_send)
        self.pushButton_19.clicked.connect(def_send)
        self.pushButton_20.clicked.connect(def_send)
        self.pushButton_21.clicked.connect(def_send)
        self.pushButton_22.clicked.connect(def_send)
        self.pushButton_23.clicked.connect(def_send)
        self.pushButton_24.clicked.connect(def_send)
        self.pushButton_25.clicked.connect(def_send)
        self.pushButton_26.clicked.connect(def_send)
        self.pushButton_27.clicked.connect(def_send)
