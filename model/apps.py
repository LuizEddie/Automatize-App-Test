import os
import json
import subprocess


class ListApps:

    json_dir = "data"
    json_file = "apps.json"
    path = "{}/{}".format(json_dir, json_file)
    json_structure = '{"data":[{' \
                            '"id": 0, ' \
                            '"name":"example", ' \
                            '"original_res":{"x": 1080, ' \
                                            '"y": 2400}, ' \
                            '"package":"example.example", ' \
                            '"tests":[{' \
                                    '"id": 0, ' \
                                    '"name":"example", ' \
                                    '"commands":[{' \
                                                '"id": 0, ' \
                                                '"command": "adb shell input touchscreen tap",' \
                                                '"x":0,'\
                                                '"y":0' \    
                                                '},' \
                                                '{' \
                                                '"id": 0, ' \
                                                '"command": "adb shell input touchscreen swipe",' \
                                                '"x1":0,'\
                                                '"y1":0,' \
                                                '"x2":0,' \
                                                '"y2":0' \    
                                                '},' \
                                                '{' \
                                                '"id": 0, ' \
                                                '"command": "adb shell input touchscreen swipe",' \
                                    '}] ' \
                            '}]' \
                        '}]}'

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
            apps.append({"id": dt['id'], "name": dt['name'], "original_res":dt["original_res"], "package": dt['package']})
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

    def add_app(self, app_data):
        file = open(self.path, "r", encoding="utf8")
        data = json.load(file)
        file.close()

        data["data"].append(app_data)

        file = open(self.path, "w")
        json.dump(data, file, indent=4, separators=(',', ':'))

    def res_calc(self, id, res):
        data = self.get_apps()
        app_data = list(filter(lambda x: x["id"] == id, data))
        original_res = app_data[0]["original_res"]
        x = (res["x"] * 100)/original_res["x"]
        y = (res["y"] * 100)/original_res["y"]
        diff_per_x = x * 0.01
        diff_per_y = y * 0.01
        ref_resolution_calc = {"x": diff_per_x, "y": diff_per_y}
        return ref_resolution_calc
