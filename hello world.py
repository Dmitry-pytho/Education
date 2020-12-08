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
