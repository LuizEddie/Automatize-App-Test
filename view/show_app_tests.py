from tkinter import *
from tkinter import messagebox
from controller import apps as c


class TestsView(Toplevel):
    def __init__(self, app, master=None):
        Toplevel.__init__(self, master=master)

        self.controller = c.ListApps()

        self.package = app.split(": ")[1]
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

        self.tests_widget = Frame(self)
        self.list_tests = Listbox(self.tests_widget, selectmode=SINGLE)
        self.scrollbar = Scrollbar(self.tests_widget)
        self.get_tests()

        self.buttons_widget = Frame(self)
        self.start_test = Button(self.buttons_widget, text="Start Test")

        self.init_view()

    def init_view(self):
        self.welcome_widget.pack()
        self.welcome_msg.pack()

        self.tests_widget.pack()
        self.list_tests.pack(side=LEFT, fill=BOTH)
        self.scrollbar.pack(side=RIGHT, fill=BOTH)
        self.list_tests.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.list_tests.yview())

        self.buttons_widget.pack()
        self.start_test.pack()
    def get_tests(self):
        tests = self.controller.get_tests(self.package)
        count = 0
        for test in tests:
            self.list_tests.insert(count, test["name"])
            count = count + 1
