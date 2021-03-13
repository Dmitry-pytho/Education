filename = "/home/dmitry/PycharmProjects/Education/Files_for_read/pi_digits.txt"
with open(filename) as file_object:
    lines = file_object.readlines()
    for line in lines:
        print(line.rstrip())
