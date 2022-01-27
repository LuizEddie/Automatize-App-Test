import os
import json

class List_Apps:

    json_dir = "data"
    json_file = "apps.json"
    path = "{}/{}".format(json_dir, json_file)
    json_structure = '{"data":[{"name":"example", "package":"example.example", "tests":[{"name":"example", "commands":[]}]}'

    def create_json_file(self):
        file = open(self.path, "x")
        file.close()

    def create_dir(self):
        os.mkdir(self.json_dir)
        self.create_json_file()
        self.write_structure()

    def write_structure(self):
        file = open(self.path, "w")
        file.write(self.json_structure)
        file.close()

    def get_apps(self):
        file = open(self.path, "r", encoding='utf8')
        data = json.load(file)
        apps = []
        for dt in data['data']:
            apps.append({"name": dt['name'], "package": dt['package']})

        return apps

    def get_tests(self, package):
        file = open(self.path, "r", encoding='utf8')
        data = json.load(file)
        app_data = list(filter(lambda x:x["package"] == package, data["data"]))
        return app_data[0]["tests"]

    def start_adb(self):
        os.system("adb devices")