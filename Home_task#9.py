from random import randint, shuffle, choice, random
import string, json, csv
from re import split


def generate_random_letters():
    symbols = list(string.ascii_letters) + list(string.digits) + list("\n")
    shuffle(symbols)
    random_letters = ""
    str_str2 = ""
    for word in range(randint(100, 1000)):
        letter = choice(symbols)
        random_letters = (random_letters + letter).title()
        str_str1 = split(r'(\d+)', random_letters)
        str_str2 = ", ".join(str_str1)
    return str_str2


def write_txt_file(filename):
    with open(filename, "w") as txt:
        data = []
        data.append(generate_random_letters())
        txt.writelines(data)
    return txt


def generate_random_key_for_dictionary():
    symbols = list(string.ascii_lowercase)
    shuffle(symbols)
    random_key = ""
    for x in range(5):
        symbol = choice(symbols)
        random_key = (random_key + symbol)
    return random_key


generate_random_key_for_dictionary()


def generate_random_values_for_dictionary():
    value1 = round(random(), 4)
    value2 = randint(-100, 100)
    value3 = choice([False, True])
    value = choice([value1, value2, value3])
    return value


generate_random_values_for_dictionary()


def generate_dictionary():
    my_dict = {}
    for x in range(randint(5, 20)):
        my_dict[generate_random_key_for_dictionary()] = generate_random_values_for_dictionary()
    return my_dict


generate_dictionary()


def write_json_file(filename):
    with open(filename, "w") as json_file:
        json.dump(generate_dictionary(), json_file, indent=4)
    return json_file


def generate_rows_and_columns():
    n = randint(3, 10)

    m = randint(3, 10)

    rows = []
    for x in range(n):
        columns = []
        for y in range(m):
            null_or_one = choice([0, 1])
            columns.append(null_or_one)
        rows.append(columns)
    return rows


def write_csv_file(filename):
    with open(filename, "w") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(generate_rows_and_columns())
        return writer


def generate_and_write_file(filename):
    ext = filename.split('.')[-1]
    if ext == "txt":
        result = write_txt_file(filename)
    elif ext == "json":
        result = write_json_file(filename)
    elif ext == "csv":
        result = write_csv_file(filename)
    else:
        print("Unsupported file format")
        result = " "
    return result


generate_and_write_file("d:\Дима\Python\Education\win.json")
