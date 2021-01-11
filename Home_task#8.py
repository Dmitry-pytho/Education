from random import randint, choice, shuffle
import string
#
with open("domains.txt", "r") as txt:
    spisok_domenov = []
    for line in txt.readlines():
        spisok_domenov.append(line.replace("\n", "").replace(".", ""))
        random_domen = choice(spisok_domenov)
#
#
with open("_names.txt", "r") as text:
    spisok_names = []
    for line in text.readlines():
        spisok_names.append(line.split()[1])

print(spisok_names)
#
# def generate_random_numbers():
#     number = str(randint(100, 1000))
#     return number
#
#
# random_number = generate_random_numbers()
#
#
# def generate_random_letters():
#     alphabet = list(string.ascii_lowercase)
#     shuffle(alphabet)
#     random_letters = ""
#     for x in range(randint(5, 7)):
#         letter = choice(alphabet)
#         random_letters = random_letters + letter
#     return random_letters
#
#
# rand_letters = generate_random_letters()
#
#
# def generate_email(domains, names):
#     result = names + generate_random_numbers() + "@" + generate_random_letters() + "." + domains
#     return result
#
#
# email = generate_email(random_domen, random_name)
# print(email)
