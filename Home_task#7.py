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

#Задание №3
my_str = "I'm the string"
def print_my_str():
    str = "***" + my_str + "***"
    return str
print(print_my_str())