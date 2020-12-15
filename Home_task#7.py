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
def my_print(body_message):
    message = "***" + body_message + "***"
    print(message)
my_print("I'm the string")