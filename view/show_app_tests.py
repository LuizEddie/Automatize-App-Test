from tkinter import *
from tkinter import messagebox
from controller import apps as c


class TestsView(Toplevel):
    def __init__(self, app, master=None):
        Toplevel.__init__(self, master=master)

        self.controller = c.ListApps()

        self.id = int(app.split(" - ")[0])
        self.title("Testes {}".format(app.split(": ")[0]))
        self.geometry('480x480')

        self.welcome_widget = Frame(self)
        self.welcome_msg = Label(self.welcome_widget, text="Welcome\n"
                                                           "To start an test, follow these instructions below:\n"
                                                           "1. Install adb on this PC if it wasn't installed\n"
                                                           "2. Active dev mode at your Android smartphone\n"
                                                           "3. Active USB debug\n"
                                                           "4. Connect an Android Smartphone to PC by USB\n"
                                                           "5. Click on Check ADB\n"
                                                           "6. Select an test\n"
                                                           "7. Click on Start Test\n")

        self.search_widget = Frame(self)
        self.search_msg = Label(self.search_widget, text="Search by test name")
        self.search_field = Entry(self.search_widget)
        self.search_button = Button(self.search_widget, text="Search")

        self.tests_widget = Frame(self)
        self.list_tests = Listbox(self.tests_widget, selectmode=SINGLE)
        self.scrollbar = Scrollbar(self.tests_widget)
        self.get_tests()

        self.buttons_widget = Frame(self)
        self.start_test = Button(self.buttons_widget, text="Start Test", command=self.start_test)
        self.add_test = Button(self.buttons_widget, text="Add Test")
        self.edit_test = Button(self.buttons_widget, text="Edit Test")
        self.delete_test = Button(self.buttons_widget, text="Delete Test")

        self.init_view()

    def init_view(self):
        self.welcome_widget.pack()
        self.welcome_msg.pack()

        self.search_widget.pack()
        self.search_msg.pack()
        self.search_field.pack(side=LEFT)
        self.search_button.pack(side=RIGHT)

        self.tests_widget.pack()
        self.list_tests.pack(side=LEFT, fill=BOTH)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)
        self.list_tests.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.list_tests.yview())

        self.buttons_widget.pack()
        self.add_test.pack(side=LEFT)
        self.edit_test.pack(side=LEFT)
        self.delete_test.pack(side=LEFT)

        self.start_test.pack(side=RIGHT)

    def get_tests(self):
        tests = self.controller.get_tests(self.id)
        count = 0

        for test in tests:
            self.list_tests.insert(count, "{} - {}".format(test["id"], test["name"]))
            count = count + 1

    def start_test(self):
        try:
            test_id = int(self.list_tests.get(self.list_tests.curselection()).split(" - ")[0])
            commands = self.controller.get_commands(self.id, test_id)

            for c in commands:
                self.controller.start_tests(c)
        except Exception:
            messagebox.showerror("Error", "Please select a test")