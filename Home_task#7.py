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
# Задание №4

# list_age = []
# list_name = []
# persons = [{"Name": "John", "Age": 29},
#            {"Name": "Mark", "Age": 26},
#            {"Name": "Michael", "Age": 35},
#            {"Name": "Jack", "Age": 39},
#            {"Name": "Donald", "Age": 48}]
#
# for dictionary in persons:
#     list_age.append(dictionary['Age'])
# min_age = min(list_age)
# for separated_dictionary in persons:
#     if separated_dictionary['Age'] == min_age:
#         print("Самый молодой:",separated_dictionary['Name'])
# max_len_name = 0
# for dictionary in persons:
#     if len(dictionary["Name"]) >= max_len_name:
#         max_len_name = len(dictionary["Name"])
# for separated_dictionary in persons:
#     if len(separated_dictionary["Name"]) ==max_len_name:
#         print("Самое длинное имя:", separated_dictionary["Name"])
# print("Средний возраст:", sum(list_age)//len(list_age))

# # Задание №5
double_keys_list = []
first_keys_list = []
my_dict1 = {"name": "William",
            "age": 25,
            "profession": "engineer",
            "city": "Liverpool",
            "status": "single",
            "education": "higher education",
            "driver license": "B1"
            }
my_dict2 = {"name": "Garry",
            "age": 30,
            "profession": "lawyer",
            "country": "USA",
            "height": "185cm",
            "weight": "80kg",
            "driver license": "B2"
            }
# for keys in my_dict1:
#     print(keys)
set_for_my_dict1 = set(my_dict1)
set_for_my_dict2 = set(my_dict2)
inter_set = set_for_my_dict1.intersection(set_for_my_dict2)
double_keys_list.append(inter_set)
print(double_keys_list)