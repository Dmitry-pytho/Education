import requests
import json


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
print(*name_dict_list, sep="\n")

read_quotes_from_url(10)

