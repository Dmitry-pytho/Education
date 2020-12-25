from random import randint, choice, shuffle, random
import string, csv, json


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


def write_csv_file():
    with open("csv_file_for_lesson9.csv", "w") as csv_file:
        writer = csv.writer(csv_file)
        content = generate_rows_and_columns()
        print(content)
        writer.writerows(content)
        return writer


write_csv_file()
