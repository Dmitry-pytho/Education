# Логический тип bool
my_bool_f = False
my_bool_t = True

res_bool = my_bool_f and not (my_bool_t or my_bool_t)
print(res_bool)
my_bool = False
print(my_bool, type(my_bool))

value = 11
condition = value == 10
print(condition)

# Оператор if
# if условие:
#     код с отступом если ДА
# else:
#     код с отступом если НЕТ


if value != 10 and (not (value < 10)):
    print("Yes!")
else:
    print("No!")

value = "False"
res = value != "False"
# res = bool(value)
print(str(False))

value = 1230

if value % 5 == 0:
    print("Число делится на 5")
elif value % 3 == 0:
    print("Число делится на 3")
elif value % 2 == 0:
    print("Число делится на 2")
else:
    print("Число не делится на 2 и 3")



################################################
# Приведение типов

value = int(input("Введи целое число и нажми Enter: "))
value = input("Введи целое число и нажми Enter: ")
value = float(value)
value = int(value)
print(value, type(value))
print(value * 10)

my_int = 10
my_float = -10.9
my_str = "10.2"

# result = str(my_float) + my_str
result = int(my_float)

print(result)