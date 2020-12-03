# Задание №1
my_list = [50,101,120,99,75,199,200]
for number in my_list:
    if number>100:
        print("100 <", number)
###############################################
#Задание №2
my_list = [50,101,120,99,75,199,200,350]
my_results = []
for index in my_list:
    if index>100:
        my_results.append(index)
print (my_results)
###############################################
#Задание №3
my_list = [50]
if len(my_list)<2:
    my_list.append(0)
    print(my_list)
elif len(my_list)>=2:
    my_list.append(my_list[-1]+my_list[-2])
    print(my_list)

my_list = [50, 20, 30]
if len(my_list)<2:
    my_list.append(0)
    print(my_list)
elif len(my_list)>=2:
    my_list.append(my_list[-1]+my_list[-2])
    print(my_list)
###############################################
#Задание №4
value  = input("Введите дробное число:  ")
try:
    new_value = float(value)
    value = new_value**(-1)
    print(value)
except ZeroDivisionError:
    print("Вы ввели ноль")
except ValueError:
    print("Вы ввели букву")
###############################################
#Задание №5+
my_list = [1990, 1995, 2000, 2005, 2010]
my_index = [0,1,2,3,4]
for index in my_index:
    print (my_list[index])

###############################################
# Задание №6+
my_list_1 = ['a', 'c', 'e', 'g',]
my_list_2 = ['b', 'd', 'f', 'h']
my_index = [0,1,2,3]
for index in my_index:
    print (my_list_1[index],  my_list_2[index])

###############################################
# Задание №7
new_int = "0123456789"
new_list = []
for symb_1 in new_int:
    for symb_2 in new_int:
        chislo = symb_1+symb_2
        new_list.append(int(chislo))
print(new_list)





















my_list = ["a","b","c","d","e","f"]
my_str = "".join(my_list[::2])
print(my_str)




values = [1,2,3,4,5]
new_value = values.copy()
new_value.append(6)
print(values)
# print(new_value)




values = [1,2,3,4,5]
result = []
for value in values[::-1]:
    result.append(value)
print(result)

values = tuple(values)
print(type(values))


my_tuple = (1, 2, 3, 4, 5, 6, "a", 8, 9)

index = -6

print(my_tuple[index])
