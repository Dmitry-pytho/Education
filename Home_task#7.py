# Задание№1
# from random import randint
# empty_list = []
# for number in range(1,20+1):
#     x = randint(1, 100)
#     empty_list.append(x)
# print(empty_list)
############################################

# Задание№2
# from random import randint
# def create_random_point():
#     point = (randint(-10, 10),
#             randint(-10, 10),
#             randint(-10, 10))
#     return point
# triangle={"A": create_random_point(),
#           "B": create_random_point(),
#           "C": create_random_point(),
#        }
# print(triangle)
######################################

# Задание №3
# def my_print(body_message):
#     message = "***" + body_message + "***"
#     print(message)
# my_print("I'm the string")
#######################################
# Задание №4a
from collections import defaultdict

persons = [{"Name": "John", "Age": 15},
           {"Name": "Mark", "Age": 18},
           {"Name": "Michael", "Age": 27},
           {"Name": "Jack", "Age": 35},
           {"Name": "Donald", "Age": 38}]
age_by_names = defaultdict(list)
len_name_by_names = defaultdict(list)
ages = []
for p in persons:
    name = p['Name']
    age = p['Age']
    age_by_names[age].append(name)
    len_name_by_names[len(name)].append(name)
    ages.append(age)
min_age = min(age_by_names)
print("самый младший:", *age_by_names[min_age])
max_len_name = max(len_name_by_names)
print("Самое длинное имя:", *len_name_by_names[max_len_name])
print("средний возраст:", sum(ages) // len(ages))
