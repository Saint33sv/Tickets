import os
import pickle


class Event(object):
    def __init__(self, name, data, time, page_location, page_location_1):
        self.name = name
        self.data = data
        self.time = time
        self.page_logia = page_location
        self.page_balcony = page_location_1
        self.rows_logia = {'Ряд 1': self.page_logia, 'Ряд 2': self.page_logia, 'Ряд 3': self.page_logia}
        self.rows_balcony = {'Ряд 1': self.page_balcony, 'Ряд 2': self.page_balcony, 'Ряд 3': self.page_balcony}
        self.map = [["Лоджия", self.rows_logia], ["Балкон", self.rows_balcony]]
        self.not_path = os.getcwd()
        self.projectname = f"{self.name}, Дата-{self.data}, Время-{self.time}"
        self.list_buttons = []
        self.ticket_num = 0
        self.sales_revenue = 0

    def find_price(self, location, row):
        page = None
        for i in self.map:
            if location == i[0]:
                page = i[1].get(row)
        return page

    def save_ticket(self, button):
        row = button.parent()
        loc = row.parent()
        price = str(self.find_price(location=loc.title(), row=row.title()))
        place = button.text()
        self.sales_revenue += int(price)
        self.ticket_num += 1
        name_ticket = f"Билет№ {self.ticket_num}_{loc.title()}_{row.title()}_Место_{place}"
        self.list_buttons.append((loc.title(), row.title(), place, "red", name_ticket))
        text_ticket = f"""Билет №{str(self.ticket_num)}
{self.name}
Дата: {self.data}
Время: {self.time}
{loc.title()}
{row.title()}
Место: {place}
Цена: {price}"""
        print(text_ticket)
        self.save_config()
        file = open(f"{self.not_path}\\events\\{self.projectname}\\tickets\\{name_ticket}.txt", 'w')
        file.write(text_ticket)
        file.close()

    def book_a_ticket(self, button):
        row = button.parent()
        loc = row.parent()
        place = button.text()
        self.list_buttons.append((loc.title(), row.title(), place, "green"))
        self.save_config()

    def delete_ticket(self, button):
        row = button.parent()
        loc = row.parent()
        place = button.text()
        price = str(self.find_price(location=loc.title(), row=row.title()))
        for ticket in self.list_buttons:
            if (loc.title() == ticket[0]) and (row.title() == ticket[1]) and \
                    (place == ticket[2]) and (ticket[3] == "red"):
                name_ticket = ticket[4]
                self.sales_revenue -= int(price)
                os.remove(f"{self.not_path}\\events\\{self.projectname}\\tickets\\{name_ticket}.txt")
                self.list_buttons.pop(self.list_buttons.index((loc.title(), row.title(), place, "red", name_ticket)))
            if (loc.title(), row.title(), place, "green") in self.list_buttons:
                self.list_buttons.pop(self.list_buttons.index((loc.title(), row.title(), place, "green")))
        self.save_config()

    def make_statistic(self):
        ticketslogia = 0
        ticketsbalcony = 0
        ticketsnum = 0
        bookticketslogia = 0
        bookticketsbalcony = 0
        bookticketsnum = 0
        for ticket in self.list_buttons:
            if ticket[0] == "Лоджия" and ticket[3] == "red":
                ticketslogia += 1
                ticketsnum += 1
            if ticket[0] == "Балкон" and ticket[3] == "red":
                ticketsbalcony += 1
                ticketsnum += 1
            if ticket[0] == "Лоджия" and ticket[3] == "green":
                bookticketslogia += 1
                bookticketsnum += 1
            if ticket[0] == "Балкон" and ticket[3] == "green":
                bookticketsbalcony += 1
                bookticketsnum += 1

        textstat = f"""Статистика проданных-забронированных билетов.
Всего продано: {ticketsnum}
Лоджия: {ticketslogia} 
Балкон: {ticketsbalcony} 
Всего забронировано: {bookticketsnum}
Лоджия: {bookticketslogia} 
Балкон: {bookticketsbalcony} 
Общая стоимость проданных билетов: {str(self.sales_revenue)} руб."""
        return textstat

    def make_events(self):
        """Функция указывает пути для создания папок и их названия"""
        path = f"{self.not_path}\\events"
        folders = ('config', 'tickets')
        full_path = os.path.join(path, self.projectname)
        self.make_dirs(full_path)
        for f in folders:
            folder = os.path.join(full_path, f)
            self.make_dirs(folder)

    def make_dirs(self, pathname):
        """Функция создает папку"""
        if not os.path.exists(pathname):
            os.mkdir(pathname)

    def save_config(self):
        """Создает файл конфигурации"""
        data_to_save = {"name": self.name, "data": self.data, "time": self.time, "price_l": self.page_logia,
                        "price_b": self.page_balcony, "rows_logia": self.rows_logia,
                        "rows_balcony": self.rows_balcony, "name_project": self.projectname,
                        "listButtons": self.list_buttons, "ticket_num": self.ticket_num,
                        "sales_revenue": self.sales_revenue}
        file = open(f"{self.not_path}\\events\\{self.projectname}\\config\\configuration.txt", "wb")
        pickle.dump(data_to_save, file)
        file.close()

    def redact_price_row(self, local, row, price):
        if local == 'Лоджия' and row in ["Ряд 1", "Ряд 2", "Ряд 3"]:
            self.rows_logia[row] = price
        elif local == 'Лоджия' and row == "Вся локация":
            self.page_logia = price
            for i in self.rows_logia.keys():
                self.rows_logia[i] = self.page_logia
        elif local == 'Балкон' and row in ["Ряд 1", "Ряд 2", "Ряд 3"]:
            self.rows_balcony[row] = price
        elif local == 'Балкон' and row == "Вся локация":
            self.page_balcony = price
            for i in self.rows_balcony.keys():
                self.rows_balcony[i] = self.page_balcony


# new_event = Event('Иван Дурак', '24.11.2022', '18.00', '320', '200')
# print(new_event.page_balcony, new_event.rows_balcony)
# new_event.redact_price_row("Балкон", "Вся локация", "600")
# print(new_event.page_balcony)
# new_event.make_events()
# new_event.save_config()
# new_event.rows_balcony = new_event.rows_logia.copy()
# print(new_event.rows_balcony)
