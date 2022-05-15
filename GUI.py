from tkinter import Tk, BOTH, RIGHT, RAISED, LEFT, TOP, X, Label, Toplevel, Entry, NSEW, Frame, E, EW, Listbox, SINGLE, \
    Scrollbar, Y, END
from tkinter.ttk import Button
from tkinter import messagebox as mb
from Homory_method import Homory_method_calculator
import pickle


class Route:
    def __init__(self, title, length, characteristics=None):
        if characteristics is None:
            characteristics = []
        self.title = title
        self.length = length
        self.characteristics = characteristics

    def add_charact(self, value):
        self.characteristics.append(value)

    def delete_charact(self, index):
        self.characteristics.pop(index)


class TransportType:
    def __init__(self, title, ammount, cost_per_day, cost_per_km, characteristics=None):
        if characteristics is None:
            characteristics = []
        self.title = title
        self.ammount = ammount
        self.characteristics = characteristics
        self.cost_per_day = cost_per_day
        self.cost_per_km = cost_per_km

    def add_charact(self, value):
        self.characteristics.append(value)

    def delete_charact(self, index):
        self.characteristics.pop(index)


class Result:
    def __init__(self, title, results, cost):
        self.title = title
        self.results = results
        self.cost = cost


class RoutesAndTransportCharacteristics:
    def __init__(self, t_char=None, r_char=None):
        if r_char is None:
            r_char = []
        if t_char is None:
            t_char = []
        self.t_char = t_char
        self.r_char = r_char


def save_characteristics(characteristics):
    try:
        with open("characteristics", "wb") as f:
            pickle.dump(characteristics, f)
    except Exception as ex:
        print("Error while saving characteristics, ", ex)


def load_characteristics():
    try:
        with open("characteristics", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error while loading characteristics, ", ex)


def save_routes(routes):
    try:
        with open("routes", "wb") as f:
            pickle.dump(routes, f)
    except Exception as ex:
        print("Error while saving routes, ", ex)


def save_transport(transport_types):
    try:
        with open("transports", "wb") as f:
            pickle.dump(transport_types, f)
    except Exception as ex:
        print("Error while saving transport, ", ex)


def load_routes():
    try:
        with open("routes", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error while loading routes, ", ex)


def load_transport():
    try:
        with open("transports", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error while loading transport, ", ex)


def save_results(results):
    try:
        with open("results", "wb") as f:
            pickle.dump(results, f)
    except Exception as ex:
        print("Error while saving results, ", ex)


def load_results():
    try:
        with open("results", "rb") as f:
            return pickle.load(f)
    except Exception as ex:
        print("Error while loading results, ", ex)


class add_new_route_popup:
    def __init__(self, master, characteristics):
        self.top = Toplevel(master)
        self.characteristics = characteristics
        self.char_labels = []
        self.entries = []
        self.new_route = None
        self.initUI()

    def initUI(self):
        self.centerWindow()
        self.central_frame = Frame(self.top, relief=RAISED, borderwidth=1)
        self.central_frame.pack(fill=BOTH, expand=True)
        self.title = Label(self.central_frame, text="Название")
        self.title.grid(row=0, column=0)

        self.length = Label(self.central_frame, text="Протяженность")
        self.length.grid(row=0, column=1)

        for i in range(len(self.characteristics)):
            self.char_labels.append(Label(self.central_frame, text=self.characteristics[i].r_char))
            self.char_labels[-1].grid(row=0, column=2 + i)
        for i in range(len(self.characteristics) + 2):
            self.entries.append(Entry(self.central_frame))
            self.entries[-1].grid(row=1, column=i)

        self.close_button = Button(self.top, text="Закрыть", command=self.close)
        self.close_button.pack(side=RIGHT, padx=5, pady=5)

        self.add_button = Button(self.top, text="Добавить", command=self.submit)
        self.add_button.pack(side=RIGHT, padx=5, pady=5)

    def close(self):
        self.top.destroy()

    def submit(self):
        title = self.entries[0].get()
        if title == "":
            mb.showerror("Ошибка", "Введите название")
            return
        length = self.entries[1].get()
        if not length.isdigit():
            mb.showerror("Ошибка", "В качестве протяженности принимаются только числа")
            return
        characteristics = []
        for i in range(len(self.characteristics)):
            charact = self.entries[2 + i].get()
            if charact.isdigit():
                characteristics.append(charact)
            else:
                mb.showerror("Ошибка", "В качестве значение параметров принимаются только числа")
                return

        self.new_route = Route(title, length, characteristics)
        self.top.destroy()

    def centerWindow(self):
        sw = self.top.winfo_screenwidth()
        sh = self.top.winfo_screenheight()

        h = sh / 3
        w = round(sw * h / sh)

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.top.geometry('%dx%d+%d+%d' % (w, h, x, y))


class add_new_transport_popup:
    def __init__(self, master, characteristics):
        self.top = Toplevel(master)
        self.characteristics = characteristics
        self.char_labels = []
        self.entries = []
        self.new_transport = None
        self.initUI()

    def initUI(self):
        self.centerWindow()

        self.central_frame = Frame(self.top, relief=RAISED, borderwidth=1)
        self.central_frame.pack(fill=BOTH, expand=True)

        self.title = Label(self.central_frame, text="Название")
        self.title.grid(row=0, column=0)

        self.ammount = Label(self.central_frame, text="Количество")
        self.ammount.grid(row=0, column=1)

        self.cost_per_day = Label(self.central_frame, text="Цена за день")
        self.cost_per_day.grid(row=0, column=2)

        self.cost_per_km = Label(self.central_frame, text="Цена за километр")
        self.cost_per_km.grid(row=0, column=3)

        for i in range(len(self.characteristics)):
            self.char_labels.append(Label(self.central_frame, text=self.characteristics[i].t_char))
            self.char_labels[-1].grid(row=0, column=4 + i)
        for i in range(len(self.characteristics) + 4):
            self.entries.append(Entry(self.central_frame))
            self.entries[-1].grid(row=1, column=i)

        self.close_button = Button(self.top, text="Закрыть", command=self.close)
        self.close_button.pack(side=RIGHT, padx=5, pady=5)

        self.add_button = Button(self.top, text="Добавить", command=self.submit)
        self.add_button.pack(side=RIGHT, padx=5, pady=5)

    def close(self):
        self.top.destroy()

    def submit(self):
        title = self.entries[0].get()
        if title == "":
            mb.showerror("Ошибка", "Введите название")
            return
        ammount = self.entries[1].get()
        if not ammount.isdigit():
            mb.showerror("Ошибка", "Введите количество единиц транспорта")
            return
        cost_per_day = self.entries[2].get()
        if not cost_per_day.isdigit():
            mb.showerror("Ошибка", "Введите цену использования за день")
            return
        cost_per_km = self.entries[3].get()
        if not cost_per_km.isdigit():
            mb.showerror("Ошибка", "Введите цену использования за километр")
            return
        characteristics = []
        for i in range(len(self.characteristics)):
            charact = self.entries[4 + i].get()
            if charact.isdigit():
                characteristics.append(charact)
            else:
                mb.showerror("Ошибка", "В качестве значения параметров принимаются только числа")
                return

        self.new_transport = TransportType(title, ammount, cost_per_day, cost_per_km, characteristics)
        self.top.destroy()

    def centerWindow(self):
        sw = self.top.winfo_screenwidth()
        sh = self.top.winfo_screenheight()

        h = sh / 3
        w = round(sw * h / sh)

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.top.geometry('%dx%d+%d+%d' % (w, h, x, y))


class add_characteristics_popup:
    def __init__(self, master):
        self.top = Toplevel(master)
        self.new_char_pair = None
        self.initUI()

    def initUI(self):
        self.centerWindow()
        self.central_frame = Frame(self.top, relief=RAISED, borderwidth=1)
        self.central_frame.pack(fill=BOTH, expand=True)
        self.central_frame.columnconfigure(0, weight=1)
        self.central_frame.rowconfigure(0, weight=1)
        self.central_frame.rowconfigure(1, weight=1)
        self.central_frame.rowconfigure(2, weight=1)
        self.central_frame.rowconfigure(3, weight=1)
        self.central_frame.rowconfigure(4, weight=1)
        self.central_frame.rowconfigure(5, weight=1)

        self.title = Label(self.central_frame, text="Добавить характеристики", font=("Arial", 15))
        self.title.grid(row=0, column=0)

        self.first_text = Label(self.central_frame, text="Введите название новой характеристики маршрута:")
        self.first_text.grid(row=1, column=0)

        self.route_char_name_entry = Entry(self.central_frame)
        self.route_char_name_entry.grid(row=2, column=0)

        self.second_text = Label(self.central_frame, text="Введите название связанной характеристики транспорта:")
        self.second_text.grid(row=3, column=0)

        self.transport_char_name_entry = Entry(self.central_frame)
        self.transport_char_name_entry.grid(row=4, column=0)

        self.submit_button = Button(self.central_frame, text="Добавить", command=self.submit)
        self.submit_button.grid(row=5, column=0)

    def submit(self):
        route_char = self.route_char_name_entry.get()
        transport_char = self.transport_char_name_entry.get()
        if route_char == "" or transport_char == "":
            mb.showerror("Ошибка", "Пожалуйста, заполните оба поля")
            return
        self.new_char_pair = RoutesAndTransportCharacteristics(transport_char, route_char)
        self.top.destroy()

    def centerWindow(self):
        sw = self.top.winfo_screenwidth()
        sh = self.top.winfo_screenheight()

        h = 300
        w = 400

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.top.geometry('%dx%d+%d+%d' % (w, h, x, y))


class delete_characteristics_popup:
    def __init__(self, master, characteristics):
        self.top = Toplevel(master)
        self.characteristics = []
        self.deleted_characteristics = None
        for i in range(len(characteristics)):
            self.characteristics.append(characteristics[i].r_char + " - " + characteristics[i].t_char)
        self.initUI()

    def initUI(self):
        self.centerWindow()
        self.central_frame = Frame(self.top, relief=RAISED, borderwidth=1)
        self.central_frame.pack(fill=BOTH, expand=True)
        self.central_frame.rowconfigure(0, weight=1)
        self.central_frame.rowconfigure(1, weight=1)
        self.central_frame.rowconfigure(2, weight=1)
        self.central_frame.columnconfigure(0, weight=2)
        self.central_frame.columnconfigure(1, weight=1)
        scrollbar = Scrollbar(self.central_frame)

        scrollbar.grid(row=0, column=1, rowspan=3, sticky=E)

        self.title = Label(self.central_frame, text="Выберите пару характеристик для удаления")
        self.title.grid(row=0, column=0)

        self.list = Listbox(self.central_frame, selectmode=SINGLE, yscrollcommand=scrollbar.set)
        for charact in self.characteristics:
            self.list.insert(END, charact)
        self.list.grid(row=1, column=0)

        scrollbar.config(command=self.list.yview)

        self.submit_btn = Button(self.central_frame, text="Подтвердить", command=self.submit)
        self.submit_btn.grid(row=2, column=0)

    def submit(self):
        self.deleted_characteristics = self.list.curselection()
        self.top.destroy()

    def centerWindow(self):
        sw = self.top.winfo_screenwidth()
        sh = self.top.winfo_screenheight()

        h = 300
        w = 400

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.top.geometry('%dx%d+%d+%d' % (w, h, x, y))


class delete_transport_or_route_popup:
    def __init__(self, master, transport_titles, routes, on_page):
        self.top = Toplevel(master)
        self.titles = []
        self.page = on_page
        self.deleted_element = None
        if self.page == "Routes":
            for i in routes:
                self.titles.append(i.title)
        else:
            for i in transport_titles:
                self.titles.append(i.title)
        self.initUI()

    def initUI(self):
        self.centerWindow()
        self.central_frame = Frame(self.top, relief=RAISED, borderwidth=1)
        self.central_frame.pack(fill=BOTH, expand=True)
        self.central_frame.rowconfigure(0, weight=1)
        self.central_frame.rowconfigure(1, weight=1)
        self.central_frame.rowconfigure(2, weight=1)
        self.central_frame.columnconfigure(0, weight=2)
        self.central_frame.columnconfigure(1, weight=1)
        scrollbar = Scrollbar(self.central_frame)

        scrollbar.grid(row=0, column=1, rowspan=3, sticky=E)
        if self.page == "Routes":
            self.title = Label(self.central_frame, text="Выберите маршрут для удаления")
        else:
            self.title = Label(self.central_frame, text="Выберите тип транспорта для удаления")
        self.title.grid(row=0, column=0)

        self.list = Listbox(self.central_frame, selectmode=SINGLE, yscrollcommand=scrollbar.set)
        for title in self.titles:
            self.list.insert(END, title)
        self.list.grid(row=1, column=0)

        scrollbar.config(command=self.list.yview)

        self.submit_btn = Button(self.central_frame, text="Подтвердить", command=self.submit)
        self.submit_btn.grid(row=2, column=0)

    def submit(self):
        self.deleted_element = self.list.curselection()
        self.top.destroy()

    def centerWindow(self):
        sw = self.top.winfo_screenwidth()
        sh = self.top.winfo_screenheight()

        h = 300
        w = 400

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.top.geometry('%dx%d+%d+%d' % (w, h, x, y))


class input_new_characteristics():
    def __init__(self, master, charact, titles, routes_or_transport):
        self.top = Toplevel(master)
        self.charact = charact
        self.titles = titles
        self.r_or_t = routes_or_transport
        self.title_lables = []
        self.entries = []
        self.new_values = []
        self.initUI()

    def initUI(self):
        self.centerWindow()
        self.central_frame = Frame(self.top, relief=RAISED, borderwidth=1)
        self.central_frame.pack(fill=BOTH, expand=True)
        self.central_frame.columnconfigure(0, weight=1)
        self.central_frame.columnconfigure(1, weight=1)

        for i in range(len(self.titles) + 2):
            self.central_frame.rowconfigure(i, weight=1)

        if self.r_or_t == "Routes":
            self.header = Label(self.central_frame, text="Маршруты")
            self.header.grid(row=0, column=0, columnspan=2)

            self.title = Label(self.central_frame, text="Название")
            self.title.grid(row=1, column=0)

            self.charact_name = Label(self.central_frame, text=self.charact.r_char)
            self.charact_name.grid(row=1, column=1)
        else:
            self.header = Label(self.central_frame, text="Типы транспорта")
            self.header.grid(row=0, column=0, columnspan=2)

            self.title = Label(self.central_frame, text="Тип")
            self.title.grid(row=1, column=0)

            self.charact_name = Label(self.central_frame, text=self.charact.t_char)
            self.charact_name.grid(row=1, column=1)

        for i in range(len(self.titles)):
            self.title_lables.append(Label(self.central_frame, text=self.titles[i].title))
            self.title_lables[-1].grid(row=2 + i, column=0)
            self.entries.append(Entry(self.central_frame))
            self.entries[-1].grid(row=2 + i, column=1)

        self.submit_btn = Button(self.central_frame, text="Подтвердить", command=self.submit)
        self.submit_btn.grid(row=len(self.titles) + 2, column=0, columnspan=2)

    def submit(self):
        for i in range(len(self.titles)):
            value = self.entries[i].get()
            if value == "":
                mb.showerror("Ошибка", "Пожалуйста, заполните все поля")
                return
            else:
                self.new_values.append(value)
        self.top.destroy()

    def centerWindow(self):
        sw = self.top.winfo_screenwidth()
        sh = self.top.winfo_screenheight()

        h = 300
        w = 400

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.top.geometry('%dx%d+%d+%d' % (w, h, x, y))


class Interface(Frame):
    def __init__(self, args):
        super().__init__()
        self.labels = []
        self.characteristics = load_characteristics()
        self.routes = load_routes()
        self.transport_types = load_transport()
        self.results = load_results()

        if self.characteristics is None:
            self.characteristics = []
        if self.routes is None:
            self.routes = []
        if self.transport_types is None:
            self.transport_types = []
        if self.results is None:
            self.results = []
            self.actual_calcs = False
        else:
            self.actual_calcs = self.results[-1]
            self.results.pop()
        self.total_cost = 0
        self.initUI()

    def initUI(self):
        self.master.title("Расчет маршрутов")

        self.centerWindow()

        self.makeToolbar()

        self.central_frame = Frame(self, relief=RAISED, borderwidth=1)
        self.central_frame.pack(fill=BOTH, expand=True)

        for i in range(len(self.characteristics) + 4):
            self.central_frame.columnconfigure(i, weight=1)

        self.name = Label(self.central_frame, text="Тип")
        self.name.grid(row=0, column=0)

        self.ammount = Label(self.central_frame, text="Количество")
        self.ammount.grid(row=0, column=1)

        self.cost_per_day = Label(self.central_frame, text="Цена в день")
        self.cost_per_day.grid(row=0, column=2)

        self.cost_or_length = Label(self.central_frame, text="Цена за км")
        self.cost_or_length.grid(row=0, column=3)

        self.total_cost_label = Label(self, text="Суммарные расходы: ")

        self.transport_button['state'] = 'disabled'

        for i in range(len(self.characteristics)):
            self.labels.append(Label(self.central_frame, text=self.characteristics[i].t_char))
            self.labels[i].grid(row=0, column=4 + i, sticky=NSEW)
        for i in range(len(self.transport_types)):
            tr_type = self.transport_types[i]
            self.labels.append(Label(self.central_frame, text=tr_type.title))
            self.labels[-1].grid(row=1 + i, column=0, sticky=EW)
            self.labels.append(Label(self.central_frame, text=tr_type.ammount))
            self.labels[-1].grid(row=1 + i, column=1, sticky=EW)
            self.labels.append(Label(self.central_frame, text=tr_type.cost_per_day))
            self.labels[-1].grid(row=1 + i, column=2, sticky=EW)
            self.labels.append(Label(self.central_frame, text=tr_type.cost_per_km))
            self.labels[-1].grid(row=1 + i, column=3, sticky=EW)
            for j in range(len(tr_type.characteristics)):
                self.labels.append(Label(self.central_frame, text=tr_type.characteristics[j]))
                self.labels[-1].grid(row=1 + i, column=4 + j, sticky=EW)

        self.pack(fill=BOTH, expand=True)

        self.closeButton = Button(self, text="Закрыть", command=self.close_app)
        self.closeButton.pack(side=RIGHT, padx=5, pady=5)

        self.addButton = Button(self, text="Добавить тип транспорта", command=self.add_data)
        self.addButton.pack(side=RIGHT, padx=5, pady=5)

        self.deleteButton = Button(self, text="Удалить тип транспорта", command=self.delete_element)
        self.deleteButton.pack(side=RIGHT, padx=5, pady=5)

        self.on_page = "Transport"

    def add_data(self):
        if self.on_page == "Routes":
            self.popup = add_new_route_popup(self.master, self.characteristics)
            self.addButton['state'] = 'disabled'
            self.master.wait_window(self.popup.top)
            if self.popup.new_route is not None:
                self.routes.append(self.popup.new_route)
                self.change_to_routes()
                self.actual_calcs = False
            self.addButton['state'] = 'normal'
        elif self.on_page == "Transport":
            self.popup = add_new_transport_popup(self.master, self.characteristics)
            self.addButton['state'] = 'disabled'
            self.master.wait_window(self.popup.top)
            if self.popup.new_transport is not None:
                self.transport_types.append(self.popup.new_transport)
                self.change_to_transport()
                self.actual_calcs = False
            self.addButton['state'] = 'normal'

    def delete_element(self):
        self.popup = delete_transport_or_route_popup(self.master, self.transport_types, self.routes, self.on_page)
        self.deleteButton['state'] = 'disable'
        self.master.wait_window(self.popup.top)
        if self.popup.deleted_element is not None:
            index_to_delete = self.popup.deleted_element[0]
            if self.on_page == "Routes":
                self.routes.pop(index_to_delete)
            else:
                self.transport_types.pop(index_to_delete)
            self.actual_calcs = False
        self.deleteButton['state'] = 'normal'
        if self.on_page == "Routes":
            self.change_to_routes()
        else:
            self.change_to_transport()

    def close_app(self):
        save_routes(self.routes)
        save_transport(self.transport_types)
        save_characteristics(self.characteristics)
        self.results.append(self.actual_calcs)
        save_results(self.results)
        self.quit()

    def makeToolbar(self):
        self.toolbar = Frame(self.master, borderwidth=1, relief=RAISED)

        self.routes_button = Button(self.toolbar, text="Маршруты", command=self.change_to_routes)
        self.routes_button.pack(side=LEFT, padx=2, pady=2)

        self.transport_button = Button(self.toolbar, text="Транспорт", command=self.change_to_transport)
        self.transport_button.pack(side=LEFT, padx=2, pady=2)

        self.results_button = Button(self.toolbar, text="Расчеты", command=self.change_to_results)
        self.results_button.pack(side=LEFT, padx=2, pady=2)

        self.add_char_button = Button(self.toolbar, text="Добавить пару характеристик", command=self.add_charact_pair)
        self.add_char_button.pack(side=RIGHT, padx=2, pady=2)

        self.delete_char_button = Button(self.toolbar, text="Удалить пару характеристик",
                                         command=self.delete_charact_pair)
        self.delete_char_button.pack(side=RIGHT, padx=2, pady=2)

        self.toolbar.pack(side=TOP, fill=X)

    def delete_charact_pair(self):
        self.popup = delete_characteristics_popup(self.master, self.characteristics)
        self.delete_char_button['state'] = 'disabled'
        self.master.wait_window(self.popup.top)
        if self.popup.deleted_characteristics is not None and self.popup.deleted_characteristics != ():
            self.central_frame.columnconfigure(len(self.characteristics) + 1, weight=0)
            index_to_delete = self.popup.deleted_characteristics[0]
            self.characteristics.pop(index_to_delete)
            for route in self.routes:
                route.delete_charact(index_to_delete)
            for transport in self.transport_types:
                transport.delete_charact(index_to_delete)
            self.actual_calcs = False
        self.delete_char_button['state'] = 'normal'
        if self.on_page == "Routes":
            self.change_to_routes()
        else:
            self.change_to_transport()

    def add_charact_pair(self):
        self.popup = add_characteristics_popup(self.master)
        self.add_char_button['state'] = 'disabled'
        self.master.wait_window(self.popup.top)
        if self.popup.new_char_pair is not None:
            self.central_frame.columnconfigure(len(self.characteristics) + 1, weight=1)
            self.characteristics.append(self.popup.new_char_pair)
            mb.showinfo("Внимание", "Пожалуйста, заполните новые значения характеристик маршрутов и типов транспорта")
            if len(self.routes) > 0:
                self.popup = input_new_characteristics(self.master, self.characteristics[-1], self.routes, "Routes")
                self.master.wait_window(self.popup.top)
                if self.popup.new_values:
                    for i in range(len(self.routes)):
                        self.routes[i].add_charact(self.popup.new_values[i])
            if len(self.transport_types) > 0:
                self.popup = input_new_characteristics(self.master, self.characteristics[-1], self.transport_types,
                                                       "Transport")
                self.master.wait_window(self.popup.top)
                if self.popup.new_values:
                    for i in range(len(self.transport_types)):
                        self.transport_types[i].add_charact(self.popup.new_values[i])
            self.actual_calcs = False
        self.add_char_button['state'] = 'normal'
        if self.on_page == "Routes":
            self.change_to_routes()
        else:
            self.change_to_transport()

    def centerWindow(self):
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        w = sw // 1.5
        h = round(sh * w / sw)

        x = (sw - w) / 2
        y = (sh - h) / 2
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def change_to_transport(self):
        for i in range(len(self.transport_types) + 2):
            self.central_frame.columnconfigure(i, weight=0)

        for i in range(len(self.characteristics) + 4):
            self.central_frame.columnconfigure(i, weight=1)

        self.ammount.grid(row=0, column=1)
        self.cost_per_day.grid(row=0, column=2)

        self.total_cost_label.pack_forget()

        self.name.configure(text="Тип")
        self.cost_or_length.configure(text="Цена за км")
        self.cost_or_length.grid_forget()
        self.cost_or_length.grid(row=0, column=3)

        self.transport_button['state'] = 'disabled'
        self.routes_button['state'] = 'normal'
        self.results_button['state'] = 'normal'

        self.addButton.pack(side=RIGHT, padx=5, pady=5)
        self.deleteButton.pack(side=RIGHT, padx=5, pady=5)
        self.add_char_button.pack(side=RIGHT, padx=2, pady=2)
        self.delete_char_button.pack(side=RIGHT, padx=2, pady=2)

        self.addButton.configure(text="Добавить тип транспорта")
        self.deleteButton.configure(text="Удалить тип транспорта")

        self.on_page = "Transport"

        for i in range(len(self.labels)):
            self.labels[i].destroy()
        self.labels = []
        for i in range(len(self.characteristics)):
            self.labels.append(Label(self.central_frame, text=self.characteristics[i].t_char))
            self.labels[-1].grid(row=0, column=4 + i)
        for i in range(len(self.transport_types)):
            tr_type = self.transport_types[i]
            self.labels.append(Label(self.central_frame, text=tr_type.title))
            self.labels[-1].grid(row=1 + i, column=0)
            self.labels.append(Label(self.central_frame, text=tr_type.ammount))
            self.labels[-1].grid(row=1 + i, column=1)
            self.labels.append(Label(self.central_frame, text=tr_type.cost_per_day))
            self.labels[-1].grid(row=1 + i, column=2)
            self.labels.append(Label(self.central_frame, text=tr_type.cost_per_km))
            self.labels[-1].grid(row=1 + i, column=3)
            for j in range(len(tr_type.characteristics)):
                self.labels.append(Label(self.central_frame, text=tr_type.characteristics[j]))
                self.labels[-1].grid(row=1 + i, column=4 + j)

    def change_to_routes(self):
        for i in range(len(self.transport_types) + 2):
            self.central_frame.columnconfigure(i, weight=0)
        for i in range(len(self.characteristics) + 4):
            self.central_frame.columnconfigure(i, weight=1)

        self.ammount.grid_forget()
        self.cost_per_day.grid_forget()

        self.total_cost_label.pack_forget()

        self.name.configure(text="Название")
        self.cost_or_length.configure(text="Протяженность")
        self.cost_or_length.grid_forget()
        self.cost_or_length.grid(row=0, column=1)

        self.central_frame.columnconfigure(len(self.characteristics) + 3, weight=0, pad=3)
        self.central_frame.columnconfigure(len(self.characteristics) + 2, weight=0, pad=3)

        self.routes_button['state'] = 'disabled'
        self.transport_button['state'] = 'normal'
        self.results_button['state'] = 'normal'

        self.addButton.configure(text="Добавить маршрут")
        self.deleteButton.configure(text="Удалить маршрут")

        self.addButton.pack(side=RIGHT, padx=5, pady=5)
        self.deleteButton.pack(side=RIGHT, padx=5, pady=5)
        self.add_char_button.pack(side=RIGHT, padx=2, pady=2)
        self.delete_char_button.pack(side=RIGHT, padx=2, pady=2)

        self.on_page = "Routes"

        for i in range(len(self.labels)):
            self.labels[i].destroy()
        self.labels = []
        for i in range(len(self.characteristics)):
            self.labels.append(Label(self.central_frame, text=self.characteristics[i].r_char))
            self.labels[i].grid(row=0, column=2 + i)
        for i in range(len(self.routes)):
            route = self.routes[i]
            self.labels.append(Label(self.central_frame, text=route.title))
            self.labels[-1].grid(row=1 + i, column=0)
            self.labels.append(Label(self.central_frame, text=route.length))
            self.labels[-1].grid(row=1 + i, column=1)
            for j in range(len(route.characteristics)):
                self.labels.append(Label(self.central_frame, text=route.characteristics[j]))
                self.labels[-1].grid(row=1 + i, column=2 + j)

    def change_to_results(self):
        if not self.results:
            answer = mb.askyesno(title="Внимание", message="Расчеты отсутствуют, провести их?")
            if answer:
                self.make_calc()

                if self.calculator.result == 1:
                    results = []
                    self.results = []
                    for i in range(self.calculator.true_variants):
                        results.append(0)
                    for i in range(len(self.calculator.b_vect)):
                        if self.calculator.basis[i] <= self.calculator.true_variants:
                            results[self.calculator.basis[i] - 1] = self.calculator.b_vect[i]
                    for i in range(len(self.routes)):
                        route_results = []
                        cost = 0
                        for j in range(i * len(self.transport_types), (i + 1) * len(self.transport_types)):
                            route_results.append(results[j])
                        for j in range(len(route_results)):
                            cost += self.calculator.prices_vect[i * len(self.transport_types) + j] * route_results[j]
                        self.results.append(Result(self.routes[i].title, route_results, cost))
                    self.actual_calcs = True
                else:
                    mb.showerror("Внивание", "Не удается найти оптимальное решение, вероятно, транспортных средств не хватает.")
                    if self.on_page == "Routes":
                        self.change_to_routes()
                        return
                    else:
                        self.change_to_transport()
                        return
            else:
                if self.on_page == "Routes":
                    self.change_to_routes()
                    return
                else:
                    self.change_to_transport()
                    return
        if not self.actual_calcs:
            answer = mb.askyesno(title="Внимание", message="Расчеты устарели, провести новые?")
            if answer:
                self.make_calc()

                if self.calculator.result == 1:
                    results = []
                    self.results = []
                    for i in range(self.calculator.true_variants):
                        results.append(0)
                    for i in range(len(self.calculator.b_vect)):
                        if self.calculator.basis[i] <= self.calculator.true_variants:
                            results[self.calculator.basis[i] - 1] = self.calculator.b_vect[i]
                    for i in range(len(self.routes)):
                        route_results = []
                        cost = 0
                        for j in range(i * len(self.transport_types), (i + 1) * len(self.transport_types)):
                            route_results.append(results[j])
                        for j in range(len(route_results)):
                            cost += self.calculator.prices_vect[i * len(self.transport_types) + j] * route_results[j]
                        self.results.append(Result(self.routes[i].title, route_results, cost))
                    self.actual_calcs = True
                else:
                    if self.on_page == "Routes":
                        self.change_to_routes()
                        return
                    else:
                        self.change_to_transport()
                        return

        self.results_button['state'] = 'disabled'
        self.routes_button['state'] = 'normal'
        self.transport_button['state'] = 'normal'

        self.on_page = "Results"

        self.delete_char_button.pack_forget()
        self.addButton.pack_forget()
        self.deleteButton.pack_forget()
        self.add_char_button.pack_forget()

        self.ammount.grid_forget()
        self.cost_per_day.grid_forget()
        self.cost_or_length.grid_forget()

        for i in range(len(self.characteristics) + 4):
            self.central_frame.columnconfigure(i, weight=0)
        self.central_frame.columnconfigure(0, weight=1)
        for i in range(len(self.labels)):
            self.labels[i].destroy()
        self.labels = []
        for i in range(len(self.transport_types)):
            self.central_frame.columnconfigure(1 + i, weight=1)
            self.labels.append(Label(self.central_frame, text=self.transport_types[i].title))
            self.labels[-1].grid(row=0, column=1 + i)
        self.name.configure(text="Название")
        self.central_frame.columnconfigure(len(self.transport_types) + 1, weight=1)
        self.labels.append(Label(self.central_frame, text="Расходы"))
        self.labels[-1].grid(row=0, column=len(self.transport_types) + 1)
        total_cost = 0
        for i in range(len(self.results)):
            self.labels.append(Label(self.central_frame, text=self.results[i].title))
            self.labels[-1].grid(row=1 + i, column=0)
            for j in range(len(self.transport_types)):
                self.labels.append(Label(self.central_frame, text=self.results[i].results[j]))
                self.labels[-1].grid(row=1 + i, column=1 + j)
            self.labels.append(Label(self.central_frame, text=self.results[i].cost))
            total_cost += self.results[i].cost
            self.labels[-1].grid(row=1 + i, column=len(self.transport_types) + 1)

        self.total_cost_label = Label(self, text="Суммарные расходы: " + str(total_cost))
        self.total_cost_label.pack(side=LEFT, padx=5, pady=5)

    def make_calc(self):
        self.calculator = Homory_method_calculator(self.routes, self.transport_types)


def main():
    root = Tk()
    ex = Interface(root)
    root.mainloop()


if __name__ == '__main__':
    main()
