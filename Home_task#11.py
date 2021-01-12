import json
import re


def read_json_file(filename):
    with open(filename, "r") as json_file:
        text = json.load(json_file)
        return text


content_file = read_json_file("d:\Дима\Python\lesson 11\data.json")


def key_sorted_by_name(obj_dict):
    name = obj_dict["name"].split()
    return name[-1]


name_dict_list = sorted(content_file, key=key_sorted_by_name)
print(*name_dict_list, sep="\n")



# def key_sorted_by_dates_of_life(obj_dict):
#     dates_of_life = obj_dict["years"].split("-")[1]
#     print(dates_of_life)
#     if len(dates_of_life.split()) ==1:
#         return dates_of_life.split()[0][:-1]
#     return -int(dates_of_life.split(" ")[-2])
#
# dates_of_life_dict_list = sorted(content_file, key=key_sorted_by_dates_of_life)
# print(dates_of_life_dict_list)
