my_list = ['America', 1976, 'Africa', 19, 'India', 1500, 2,'Germany', 'apple', 'Ukraine', 1991, 'Europe', "USA"]
my_list_str = []
my_list_int = []
list_shot_str = []
list_long_str = []
list_shot_int = []
list_long_int = []
for symbol in my_list:
    if type(symbol) ==str:
        my_list_str.append(symbol)
# print(my_list_str)
for symbol in my_list:
    if type(symbol) ==int:
        my_list_int.append(symbol)
# print(my_list_int)
for word in my_list_str:
    if len(word)<=5:
        list_shot_str.append(word)
for word in my_list_str:
    if len(word)>5:
        list_long_str.append(word)
print(list_shot_str)
print(list_long_str)
for number in my_list_int:
    number = str(number)
    if len(number)<=2:
        list_shot_int.append(number)
    if len(number)>2:
        list_long_int.append(number)
print(list_shot_int)
print(list_long_int)

