from random import randint, choice
import string

# №Задание №1
with open("D:\Дима\Python\Education\domains.txt", "r") as txt:
    spisok_domenov = []
    for line in txt.readlines():
        spisok_domenov.append(line.replace("\n", "").replace(".", ""))
print(spisok_domenov)
#######################################################


# №Задание №2
with open("D:\Дима\Python\Education\_names.txt", "r") as txt:
    spisok_names = []
    for line in txt.readlines():
        spisok_names.append(line.split()[1])
    print(spisok_names)

############################################################

#Задание №3

with open("D:\Дима\Python\Education\domains.txt", "r") as txt:
    spisok_domenov = []
    for line in txt.readlines():
        spisok_domenov.append(line.replace("\n", ""))
        random_domen = choice(spisok_domenov)

with open("D:\Дима\Python\Education\_names.txt", "r") as text:
    spisok_names = []
    for line in text.readlines():
        spisok_names.append(line.split()[1])
        random_name = choice(spisok_names)

for numbers in range(1):
    random_number_for_mail = str(randint(100, 1000))

letter_for_mail = choice(string.ascii_letters.lower())
random_letter_for_mail = ""
for x in range(randint(5,7)):
    random_letter_for_mail = random_letter_for_mail + choice(string.ascii_letters.lower())

email = random_name + "." + random_number_for_mail + "@" + random_letter_for_mail + random_domen
print("e-mail:", email)
