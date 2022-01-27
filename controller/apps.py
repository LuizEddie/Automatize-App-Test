from model import apps as m


class ListApps:

    model = m.List_Apps()

    def create_dir(self):
        self.model.create_dir()

    def get_apps(self):
        return self.model.get_apps()

    def get_tests(self, package):
        return self.model.get_tests(package)
