
# #Задание №7
# my_str_1 = "Hello, world!"
# my_str_2 = "Good morning my friends"
# new_list = []
# for symbol in my_str_1:
#     if my_str_1.count(symbol)==1 and my_str_2.count(symbol)==1:
#        new_list.append(symbol)
# print(new_list)

my_str_1 = "Hello, world!"
my_str_2 = "Good morning my friends"
my_set1 = set(my_str_1)
my_set2 = set(my_str_2)
inter_set = my_set1.intersection(my_set2)
new_list = list(inter_set)
print(new_list)
