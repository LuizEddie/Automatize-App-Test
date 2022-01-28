from model import apps as m


class ListApps:

    model = m.ListApps()

    def create_dir(self):
        self.model.create_dir()

    def get_apps(self):
        return self.model.get_apps()

    def get_tests(self, id):
        return self.model.get_tests(id)

    def start_tests(self, args):
        self.model.start_tests(args)

    def check_adb(self, args):
        return self.model.check_adb(args)

    def get_commands(self, id, test_id):
        return self.model.get_commands(id, test_id)
