#Задание №1
my_list_1 = ["Hello", "Good morning", "Yes", "No", "Good bye"]
new_list = []
for element in enumerate(my_list_1):
    if element[0] %2==0:
        new_list.append(element[1])
    if element[0] %2 != 0:
        new_list.append(element[1][::-1])
print(new_list)
#####################################################

#Задание №2
my_list = ['America', 'Africa', 'India', 'Germany', 'apple', 'Ukraine', 'Europe']
new_list = []
for word in my_list:
    if word[0] =="a" or word[0] =="A":
        new_list.append(word)
print(new_list)
#############################################################

#Задание №3
my_list = ['America', 'Africa', 'India', 'Germany', 'apple', 'Ukraine', 'Europe', "USA"]
new_list = []
for word in my_list:
    if "a" in word or "A" in word:
        new_list.append(word)
        print(word)
##################################################################

#Задание №4
my_list = ['America', 1976, 'Africa', 1950,'India', 1500,'Germany', 'apple', 'Ukraine',1991, 'Europe', "USA"]
new_list = []
for word in my_list:
    if type(word) ==str:
        new_list.append(word)
print(new_list)
#########################################################

#Задание №5
my_str = "Helloworld"
new_list = []
for symbol in my_str:
    if my_str.count(symbol) ==1:
        new_list.append(symbol)
print(new_list)
#####################################################

#Задание №6
my_str_1 = "Hello, world!"
my_str_2 = "Good morning my friends"
my_set1 = set(my_str_1)
my_set2 = set(my_str_2)
inter_set = my_set1.intersection(my_set2)
new_list = list(inter_set)
print(new_list)

#Задание №7
my_str_1 = "Hello, world!"
my_str_2 = "Good morning my friends"
my_set1 = set(my_str_1)
my_set2 = set(my_str_2)
inter_set = my_set1.union(my_set2)
new_list = list(inter_set)
print(new_list)

#####################################################
#Задание №8
residence = {"Страна":"Украина",
             "Город":"Днепропетровск",
             "Улица":"ж/м Тополь"}
job = {"Наличие":"Да",
       "Должность":"Серивсный менеджер"}
personal_card = {"Фамилия": "Соломянный",
                 "Имя": "Дмитрий",
                 "Возраст":"35",
                 "Проживание":residence,
                 "Работа":job}
print(personal_card)

######################################
#Задание №9
cake = {"Мука":"300г",
        "Молоко":"500мл",
        "Масло":"100г",
        "Яйцо":"2шт"}
cream = {"Сахар":"50г",
         "Масло":"30г",
         "Ваниль":"5г",
         "Сметана":"250мл"}
glaze = {"Какао":"300г",
         "Сахар":"150г",
         "Масло":"100г"}
cake_recipe = {"Коржи":cake,
               "Крем":cream,
               "Глазурь":glaze}
print(cake_recipe)