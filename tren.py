import os

from os.path import join as path_join
from os.path import isfile
from string import ascii_lowercase as alphabet


def tanos_click(dirname):
    files = ([file for file in os.listdir(dirname) if isfile(path_join(dirname, file))])
    for file in list(set(files))[:len(files)//2]:
        os.remove(path_join(dirname, file))

def create_txt_files(dirname):
    for letter in alphabet:
        file_name = os.path.join(dirname, f"{letter}.txt")
        new_alphabet = alphabet.replace(letter, letter.upper())
        write_txt_file(file_name, new_alphabet)


def write_txt_file(filename, data):
    with open(filename, "w") as txt_file:
        txt_file.write(data)


def create_dir(dir_name):
    try:
        os.mkdir(dir_name)
    except FileExistsError:
        pass


dir_name = "alphabet"
create_dir(dir_name)
create_txt_files(dir_name)
tanos_click(dir_name)