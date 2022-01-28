import os
import json
import subprocess


class ListApps:

    json_dir = "data"
    json_file = "apps.json"
    path = "{}/{}".format(json_dir, json_file)
    json_structure = '{"data":[{"id": 0, "name":"example", "package":"example.example", "tests":[{"id": 0, "name":"example", "commands":[]}]}]}'

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
            apps.append({"id": dt['id'],"name": dt['name'], "package": dt['package']})
        file.close()
        return apps

    def get_tests(self, id):
        file = open(self.path, "r", encoding='utf8')
        data = json.load(file)
        app_data = list(filter(lambda x:x["id"] == id, data["data"]))
        file.close()
        return app_data[0]["tests"]

    def start_tests(self, args):
        os.system(args)

    def check_adb(self, args):
        adb = subprocess.run(args, stdout=subprocess.PIPE)
        output = adb.stdout.decode('utf8').find('unauthorized')
        if output == -1:
            output2 = adb.stdout.decode('utf8').find("\tdevice")
            if output2 == -1:
                return {"message": "Connect a device", "code": 0}
            else:
                return {"message": "ADB OK", "code": 1}
        else:
            return {"message": "ADB Unauthorized", "code": 2}

    def get_commands(self, id, test_id):
        tests = self.get_tests(id)
        test = list(filter(lambda x:x["id"] == test_id, tests))
        return test[0]['commands']

    def edit_app(self):
        pass