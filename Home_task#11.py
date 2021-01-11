import json


def read_json_file(filename):
    with open(filename, "r") as json_file:
        text = json.load(json_file)
        return text


read_json_file("d:\Дима\Python\lesson 11\data.json")

def
