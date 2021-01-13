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
# print(name_dict_list)



def key_sorted_by_dates_of_life(obj_dict):
    death_date = obj_dict["years"].split(" – ")[1]
    year = ''
    for liter in death_date:
        if liter.isdigit():
            year += liter
    if "BC" in death_date:
        return -int(year)
    return int(year)


dates_of_life_dict_list = sorted(content_file, key=key_sorted_by_dates_of_life)
# print(*dates_of_life_dict_list, sep="\n")

def key_sorted_by_quantity_words_in_text(obj_dict):
    quantity_words = len(obj_dict["text"].split())
    return quantity_words

quantity_words_dict_list = sorted(content_file, key=key_sorted_by_quantity_words_in_text)
# print(*quantity_words_dict_list, sep="\n")




