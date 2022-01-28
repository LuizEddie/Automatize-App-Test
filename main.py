import os

from view import main as m


class Main:
    def __init__(self):
        self.main = m.start()

try:
    main = Main()
except OSError as error:
    print(error)
    os.system("pause")
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
