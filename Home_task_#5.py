#Задание №1
my_int = 123450505608902000222020
new_type = str(my_int)
search_number = "0"
zero = new_type.count(search_number)
print("Количество нулей в числе равно = ", zero)
########################################

#Задание №2
my_int = 5076070000000
new_number = str(my_int)
result = len(new_number) - len(new_number.strip("0"))
print("Количесвто нулей в конце числа равно = ", result)
########################################

#Задание №3a

my_list1 = ["a", 2, "z", 4, 5]
my_list2 = [10, 0, 20, 25, "b"]
new_list = []
for number in range(0, len(my_list1), 2):
    new_list.append(my_list1[number])
for number in range(1, len(my_list2), 2):
    new_list.append(my_list2[number])
print(new_list)

#Задание №3б
my_list1 = [1, 2, 3, 4, 2, 4, 6]
my_list2 = [10, 15, 20, 25, 21, 23]
new_list = []
for element in my_list1:
    if element % 2 == 0:
        new_list.append(element)
for element in my_list2:
    if element % 2 != 0:
        new_list.append(element)
print(new_list)
#########################################

# Задание №4
my_list = [1,2,3,4]
zero_index = my_list.pop(0)
new_list = my_list
new_list.append(zero_index)
print(new_list)

# ####################################

#Задание №5
my_list   = [1,2,3,4]
my_list.append(my_list.pop(0))
print(my_list)

###################################
#Задание№6
my_str = "43 больше чем 34 но меньше чем 56"
parts_my_str = my_str.split()
print(parts_my_str)
suma_chisel = 0
for symbol in parts_my_str:
    if symbol.isdigit():
        suma_chisel = suma_chisel + int(symbol)
print(suma_chisel)

#####################################

#Задание №7a
my_str = "abcd"
my_list = []
for number in range(0, len(my_str), 2):
    para = my_str[number:number+2]
    if len(para) < 2:
        para = para + "_"
    my_list.append(para)
print(my_list)

#Задание №7b
my_str = "abcde"
my_list = []
for number in range(0, len(my_str), 2):
    para = my_str[number:number+2]
    if len(para) < 2:
        para = para + "_"
    my_list.append(para)
print(my_list)

###########################################
#Задание №8
my_str = "My_long str"
l_limit = "o"
r_limit = "t"
left_index = my_str.index(l_limit)
right_index = my_str.index(r_limit)
sub_str = my_str[left_index+1:right_index]
print(sub_str)

##########################################]
# Задание №9
my_str = "My long string"
l_limit = "o"
r_limit = "g"
left_index = my_str.index(l_limit)
right_index = my_str.rindex(r_limit)
sub_str = my_str[left_index+1:right_index]
print(sub_str)

# Задание №10
my_list = [2, 4, 1, 5, 3, 9, 0, 7]
new_list = []
for number in range (1, len(my_list)-1):
    if my_list[number] > my_list[number-1]+my_list[number+1]:
        new_list.append(my_list[number])
        print(number)
print(len(new_list))