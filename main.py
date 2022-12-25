import sys
import shutil

from test import *
from functions import *
from start_window import *
from event_window import *
from ev_redact_win import *
from choise import *
from statistic import *

from PyQt5.QtCore import QDate, QTime


def show_map():
    """Окно карты зала"""
    global name_item
    MainWindow = QtWidgets.QMainWindow()
    ui_map.setupUi(MainWindow)
    name, data, time, price1, price2, rows_Logia_ff, rows_balcony_ff, project_name, list_but, bil_num, sales_rev \
        = read_from_file()
    new_event = Event(name, data, time, price1, price2)
    new_event.rows_logia = rows_Logia_ff.copy()
    new_event.rows_balcony = rows_balcony_ff.copy()
    new_event.map[0][1] = new_event.rows_logia
    new_event.map[1][1] = new_event.rows_balcony
    new_event.projectname = project_name
    new_event.list_buttons = list_but
    new_event.ticket_num = bil_num
    new_event.sales_revenue = sales_rev
    for button in ui_map.list_all_price_buttons:
        row = button.parent()
        loc = row.parent()
        for parameters in new_event.list_buttons:
            if (button.text() == parameters[2]) and (row.title() == parameters[1]) and (loc.title() == parameters[0]) \
                    and parameters[3] == "red":
                button.setStyleSheet("background: red")
            if (button.text() == parameters[2]) and (row.title() == parameters[1]) and (loc.title() == parameters[0]) \
                    and parameters[3] == "green":
                button.setStyleSheet("background: green")

    def show_choise_window():
        global Window_choise
        Window_choise = QtWidgets.QMainWindow()
        ui_choise.setupUi(Window_choise)
        s_b = MainWindow.sender()
        if s_b.styleSheet() == "background: red":
            ui_choise.pushButton_bay.setEnabled(False)
            ui_choise.pushButton_block.setEnabled(False)
        if s_b.styleSheet() == "background: green":
            ui_choise.pushButton_block.setEnabled(False)

        def click_bay_button():
            new_event.save_ticket(s_b)
            s_b.setStyleSheet("background: red")
            # s_b.setEnabled(False)
            Window_choise.close()

        def click_block_button():
            new_event.book_a_ticket(s_b)
            s_b.setStyleSheet("background: green")
            Window_choise.close()

        def click_cancel_button():
            Window_choise.close()

        def click_clean_button():
            new_event.delete_ticket(s_b)
            s_b.setStyleSheet("")
            Window_choise.close()

        Window_choise.show()
        ui_choise.pushButton_bay.clicked.connect(click_bay_button)
        ui_choise.pushButton_block.clicked.connect(click_block_button)
        ui_choise.pushButton_cuncel.clicked.connect(click_cancel_button)
        ui_choise.pushButton_clean.clicked.connect(click_clean_button)

    def show_statistic_window():
        global Statistic
        Statistic = QtWidgets.QDialog()
        ui_stat.setupUi(Statistic)

        def save_file_stat():
            file = open(f"{new_event.not_path}\\events\\{new_event.projectname}\\config\\Статистика.txt", "w")
            file.write(new_event.make_statistic())
            file.close()
            Statistic.close()

        ui_stat.textBrowser.setText(new_event.make_statistic())
        ui_stat.pushButton_ok.clicked.connect(lambda: Statistic.close())
        ui_stat.pushButton_save.clicked.connect(save_file_stat)
        Statistic.show()

    def send_button():
        show_choise_window()

    ui_map.label.setText(new_event.projectname)
    ui_map.connected_buttons(send_button)
    ui_map.pushButton_bake.clicked.connect(lambda: show_start_window(MainWindow))
    ui_map.pushButton_stat.clicked.connect(show_statistic_window)
    StartWindow.close()
    MainWindow.show()


def show_event_win():
    """Окно нового события появляется после нажатия на кнопку 'Создать'"""
    global EventWindow
    EventWindow = QtWidgets.QMainWindow()
    ui_event.setupUi(EventWindow)
    ui_event.pushButton_make.clicked.connect(clik_make_event)
    ui_event.pushButton_cancel.clicked.connect(lambda: show_start_window(EventWindow))
    StartWindow.close()
    EventWindow.show()


def show_red_ev_win():
    global list_events, path
    """Окно для редактирования событий"""
    global EventRedactWindow
    EventRedactWindow = QtWidgets.QMainWindow()
    ui_red_win = Ui_EventRedactWindow()
    ui_red_win.setupUi(EventRedactWindow)
    name, data, time, price1, price2, rows_Logia, rows_balcony, project_name, list_but, bilet_num, sales_rev = read_from_file()
    redacted_event = Event(name, data, time, price1, price2)
    redacted_event.rows_logia = rows_Logia.copy()
    redacted_event.rows_balcony = rows_balcony.copy()
    ui_red_win.lineEdit_name.setText(redacted_event.name)
    ui_red_win.lineEdit_logia.setText(redacted_event.page_logia)
    ui_red_win.lineEdit_balcony.setText(redacted_event.page_balcony)
    ui_red_win.dateEdit.setDate(QDate(int(redacted_event.data[6:]),
                                      int(redacted_event.data[3:5]),
                                      int(redacted_event.data[:2])))
    ui_red_win.timeEdit.setTime(QTime(int(redacted_event.time[:redacted_event.time.find('.')]),
                                      int(redacted_event.time[-2:]), 0, 0))

    def click_button_box(box, line, location):
        if box.currentText() in location.keys():
            line.setText(location.get(box.currentText()))
        else:
            if box.parent().title() == "Лоджия":
                line.setText(redacted_event.page_logia)
            elif box.parent().title() == "Балкон":
                line.setText(redacted_event.page_balcony)

    def clic_but(line, box):
        local = line.parent().title()
        row = box.currentText()
        price = line.text()
        redacted_event.redact_price_row(local, row, price)
        # redacted_event.make_events()
        # redacted_event.save_config()
        # print(redacted_event.rows_logia)

    def redact_event():
        global list_events, path
        list_events = os.listdir(path)
        redacted_event.name = ui_red_win.lineEdit_name.text()
        redacted_event.data = ui_red_win.dateEdit.text()
        redacted_event.time = ui_red_win.timeEdit.text().replace(":", ".")
        redacted_event.projectname = f"{redacted_event.name}, Дата-{redacted_event.data}, Время-{redacted_event.time}"
        redacted_event.make_events()
        redacted_event.save_config()
        if redacted_event.projectname not in list_events:
            ui.listWidget.addItem(redacted_event.projectname)
        show_start_window(EventRedactWindow)

    print(redacted_event.projectname, type(redacted_event.projectname))
    print(list_events)

    ui_red_win.comboBox_logia.activated.connect(lambda: click_button_box(ui_red_win.comboBox_logia,
                                                                         ui_red_win.lineEdit_logia,
                                                                         redacted_event.rows_logia))
    ui_red_win.comboBox_balcony.activated.connect(lambda: click_button_box(ui_red_win.comboBox_balcony,
                                                                           ui_red_win.lineEdit_balcony,
                                                                           redacted_event.rows_balcony))
    ui_red_win.pushButton_logia.clicked.connect(lambda: clic_but(ui_red_win.lineEdit_logia, ui_red_win.comboBox_logia))
    ui_red_win.pushButton_balcony.clicked.connect(lambda: clic_but(ui_red_win.lineEdit_balcony, ui_red_win.comboBox_balcony))
    ui_red_win.pushButton_redact.clicked.connect(redact_event)
    ui_red_win.pushButton_cancel.clicked.connect(lambda: show_start_window(EventRedactWindow))
    StartWindow.close()
    EventRedactWindow.show()


def show_start_window(closes_window):
    closes_window.close()
    ui.pushButton_2.setEnabled(False)
    ui.pushButton_3.setEnabled(False)
    ui.pushButton_4.setEnabled(False)
    StartWindow.show()


def new_event():
    """Новое событие"""
    name = ui_event.lineEdit_name.text()
    price1 = ui_event.lineEdit_logia.text()
    price2 = ui_event.lineEdit_balcony.text()
    data = ui_event.dateEdit.text()
    time = ui_event.timeEdit.text().replace(":", ".")
    n_e = Event(name, data, time, price1, price2)
    return n_e


def clik_make_event():
    # global list_events
    """Функция описывает логику кнопки "создать" в окне нового события"""
    new_event()
    new_event().make_events()
    new_event().save_config()
    # list_events = os.listdir(path)
    # index_event = list_events.index(new_event().projectname)
    show_start_window(EventWindow)
    ui.listWidget.addItem(new_event().projectname)


def item_path():
    """Возвращает путь к файлу конфигурации"""
    global name_item
    name_item = ui.listWidget.currentItem().text()
    name_path = f"{path}\\{name_item}\\config\\configuration.txt"
    ui.pushButton_2.setEnabled(True)
    ui.pushButton_3.setEnabled(True)
    ui.pushButton_4.setEnabled(True)
    return name_path


def read_from_file():
    """Открывает файл конфигурации и сохраняет информацию в переменные"""
    file = open(item_path(), "rb")
    data_to_load = pickle.load(file)
    file.close()
    name = data_to_load['name']
    data = data_to_load['data']
    time = data_to_load['time']
    price1 = data_to_load['price_l']
    price2 = data_to_load['price_b']
    rows_Logia = data_to_load["rows_logia"]
    rows_balcony = data_to_load["rows_balcony"]
    projectname = data_to_load["name_project"]
    list_buttons = data_to_load["listButtons"]
    ticket_num = data_to_load["ticket_num"]
    sales_rev = data_to_load["sales_revenue"]
    return name, data, time, price1, price2, rows_Logia, rows_balcony, projectname, list_buttons, ticket_num, sales_rev


def delete_event():
    """Удаление папок и файлов событий"""
    item = ui.listWidget.currentItem()
    row = ui.listWidget.row(item)
    ui.listWidget.takeItem(row)
    ui.pushButton_2.setEnabled(False)
    ui.pushButton_3.setEnabled(False)
    ui.pushButton_4.setEnabled(False)
    del_path = f"{path}\{name_item}"
    basket = []
    basket.append(del_path)
    for dir in basket:
        shutil.rmtree(dir)


name_item = None
path = os.getcwd() + r"\events"
list_events = os.listdir(path)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    StartWindow = QtWidgets.QMainWindow()
    ui = Ui_StartWindow()
    ui_map = Ui_MainWindow()
    ui_event = Ui_EventWindow()
    ui_choise = Ui_Window_choise()
    ui_stat = Ui_Statistic()
    ui.setupUi(StartWindow)

    name_item = None
    path = os.getcwd() + r"\events"
    list_events = os.listdir(path)

    ui.pushButton_2.setEnabled(False)
    ui.pushButton_3.setEnabled(False)
    ui.pushButton_4.setEnabled(False)
    ui.listWidget.addItems(list_events)
    ui.pushButton.clicked.connect(show_event_win)
    ui.pushButton_2.clicked.connect(show_map)
    ui.listWidget.itemClicked.connect(item_path)
    ui.pushButton_3.clicked.connect(show_red_ev_win)
    ui.pushButton_4.clicked.connect(delete_event)
    StartWindow.show()
    sys.exit(app.exec_())
