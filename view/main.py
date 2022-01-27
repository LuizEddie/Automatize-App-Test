from tkinter import *
from tkinter import messagebox
from controller import apps as c
from view import show_app_tests


class MainWindow(Frame):
    def __init__(self, *args, **kwargs):
        Frame.__init__(self, master=None)

        self.controller = c.ListApps()

        self.master.title("Automatize")
        self.master.geometry('480x480')

        self.welcome_widget = Frame(self.master)
        self.welcome_msg = Label(self.welcome_widget, text="Welcome!\nPlease select an App and click on Go to Test")

        self.search_widget = Frame(self.master)
        self.search_name = Label(self.search_widget, text="Search using name")
        self.search_field = Entry(self.search_widget)
        self.search_button = Button(self.search_widget, text="Search")

        self.list_widget = Frame(self.master)
        self.list_apps = Listbox(self.list_widget, selectmode=SINGLE)
        self.scrollbar = Scrollbar(self.list_widget)
        self.get_apps()

        self.bottom_widget = Frame(self.master)
        self.close_button = Button(self.bottom_widget, text="Close")
        self.add_app = Button(self.bottom_widget, text="Add App")
        self.go_test_button = Button(self.bottom_widget, text="Go to Test", command=self.go_to_tests)

        self.init_view()

        self.pack(fill="both", expand=True)

    def init_view(self):

        self.welcome_widget.pack()
        self.welcome_msg.pack()

        self.search_widget.pack()
        self.search_name.pack()
        self.search_field.pack(side=LEFT)
        self.search_button.pack(side=RIGHT)

        self.list_widget.pack()
        self.list_apps.pack(side=LEFT, fill=BOTH)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)
        self.list_apps.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.list_apps.yview)

        self.bottom_widget.pack()
        self.close_button.pack(side=LEFT)
        self.add_app.pack(side=LEFT)
        self.go_test_button.pack(side=RIGHT)

    def create_db(self):
        try:
            self.controller.create_dir()
            messagebox.showinfo("Success", "Database created")
        except OSError as error:
            messagebox.showinfo("Success", "Database loaded")
        else:
            messagebox.showerror("Error", "An error has been occured")

    def go_to_tests(self):
        app = self.list_apps.get(self.list_apps.curselection())

        '''messagebox.showinfo("", app.split(": ")[1])'''
        window = show_app_tests.TestsView(app)
        window.mainloop()

    def get_apps(self):
        apps = self.controller.get_apps()
        count = 0
        for app in apps:
            self.list_apps.insert(count, "{}: {}".format(app['name'], app['package']))
            count = count + 1


def start():
    main = MainWindow()
    main.create_db()
    main.mainloop()
