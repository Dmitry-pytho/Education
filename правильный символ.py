# number = True
# guess  = input("Введите целое число:")
# if guess == int:
#     print("Вы правильно ввели целое число")
# elif guess == float:
#     print("Вы ввели дробное число")
# else:
#     print("Вы ввели буквенный символ")

# a = 'Hello, "A"'
# b=a
# c='Hello, "B"'
# b=c
# c=a
# a=b
# print(a)


# my_value = 7
# my_bool_1  = my_value %3 ==0
# my_bool_2  = my_value %2 ==0
# print(not my_bool_1 and not my_bool_2)



# my_value_1 = 2
# my_value_2 = "4"
# my_value_1 = str(my_value_1)
# my_value_2 = int(my_value_2)
# print(my_value_1 * my_value_2)


value = input("Введите число:  ")
value = int(value)

if value %2==0 and value %3==0:
    print("Число делится и на 2 и на 3")
elif value % 2 ==0:
    print("Число делится на 2")
elif value %3 ==0:
    print("Число делится на 3")
# elif value %2==0 and value %3==0:
#     print("ЧЧисло делится и на 2 и на 3")
else:
    print("Число не делится ни на 2 ни на 3")

