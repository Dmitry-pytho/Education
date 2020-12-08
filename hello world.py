my_list1 = [1, 2, 3, 4]
my_list2 = [10, 15, 20, 25]
new_list = []
for index in range(len(my_list1)):
    if index % 2:
        new_list.append(my_list1[index])
for index in range(len(my_list2)):
    if  index % 2 != 0:
        new_list.append(my_list2[index])
print(new_list)