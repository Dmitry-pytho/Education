import requests
import json, csv

from dateutil.parser import parse


def read_quotes_from_url(amount):
    url = "http://api.forismatic.com/api/1.0/"

    params = {"method": "getQuote",
              "format": "json",
              "key": 1,
              "lang": "ru"}
    list_of_quotes = []
    for i in range(amount):
        params["key"] = i
        r = requests.get(url, params=params)
        quote = r.json()
        new_dict = {}
        quote_text = quote["quoteText"]
        quote_author = quote["quoteAuthor"]
        quote_url = quote["quoteLink"]
        new_dict["quoteText"] = quote_text
        new_dict["quoteAuthor"] = quote_author
        new_dict["quoteLink"] = quote_url
        if new_dict["quoteAuthor"] != "":
            list_of_quotes.append(new_dict)

    return list_of_quotes


def key_sorted_by_name_author(list_of_quotes):
    name = list_of_quotes["quoteAuthor"].split()
    return name


spisok = read_quotes_from_url(10)

name_dict_list = sorted(spisok, key=key_sorted_by_name_author)

read_quotes_from_url(5)


def write_csv_file(filename):
    with open(filename, "w") as csv_file:
        fieldnames = spisok[0].keys()
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(spisok)


write_csv_file("d:\Дима\Python\Education\_quotes.csv")


def get_full_info(filename):
    full_list = []
    with open(filename, "r") as txt_file:
        data = txt_file.readlines()
    for line in data:
        if "birthday" in line or "death" in line:
            if "'" in line:
                full_list.append(line)
    return full_list



def get_name_and_date(full_list):
    result_data = []
    for line in full_list:
        parts = line.split("-")
        date = parse(parts[0]).date().strftime("%d/%m/%Y")
        name = parts[1].split("'s")[0][1:]
        result_data.append({
            'date': date,
            'name': name
        })
    return result_data

my_info = get_full_info("d:\Дима\Python\Education\_authors.txt")
my_data = get_name_and_date(my_info)

def write_json_file(filename):
    with open(filename, "w") as json_file:
        json.dump(my_data, json_file, indent=4)


write_json_file("D:\Дима\Python\Education\data_and_authors.json")


