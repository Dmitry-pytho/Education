# my_list_1 = ["Hello", "Good morning", "Yes", "No", "Good bye"]
# new_list = []
# for element in enumerate(my_list_1):
#     if element[0] %2==0:
#         new_list.append(element[1])
#     if element[0] %2 != 0:
#         word = element[1]
#         invert_word = word[::-1]
#         new_list.append(invert_word)
# print(new_list)

'''2. Дан список строк my_list. Создать новый список в который поместить
элементы из my_list у которых первый символ - буква "a".'''

my_list = ['America', 'Africa', 'India', 'Germany', 'apple', 'Ukraine', 'Europe']
new_list = []
for word in my_list:
    if word[0] =="a" or word[0] =="A":
        new_list.append(word)
print(new_list)





