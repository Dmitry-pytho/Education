from random import randint, shuffle, choice
import string
from re import split




def generate_random_letters():
    symbols = list(string.ascii_letters) + list(string.digits) + list(string.whitespace)
    shuffle(symbols)
    random_letters = ""
    str_str2 = ""
    for word in range(randint(50, 300)):
        letter = choice(symbols)
        random_letters = (random_letters + letter).title()
        str_str1 = split(r'(\d+)', random_letters)
        str_str2 = ",".join(str_str1)
    return str_str2


print(generate_random_letters())


def write_txt_file():
    with open ("txt_for_lesson9.txt", "w") as text_file:
        text_file.write(generate_random_letters())