
number = int(input("Введите число кратное '5':"))
if number %5==0:
    print (number*2)
else:
    print(number*0,"Вы ввели число не кратное '5'")


###################################################################################



month = int(input("Введите месяц года по порядковому номеру:"))
if month ==2:
    print("в этом месяце 28 дней")
elif month==1 or month==3:
    print("В этом месяце 31 день ")
elif month==5 or month==7:
    print("В этом месяце 31 день ")
elif month==8 or month==10 or month==12:
    print("В этом месяце 31 день ")
else:
    print("В этом месяце 30 дней ")

#######################################################################



month = str(input("Введите название месяца года: "))
if month =="Февраль":
     print("в этом месяце 28 дней")
elif month=="Январь" or month=="Март":
     print("В этом месяце 31 день ")
elif month=="Май" or month=="Июль":
     print("В этом месяце 31 день ")
elif month=="Август" or month=="Октябрь" or month=="Декабрь":
     print("В этом месяце 31 день ")
elif month == "Апрель" or month == "Июнь":
    print("В этом месяце 30 дней ")
elif month == "Сентябрь" or month == "Ноябрь":
    print("В этом месяце 30 дней ")
else:
     print("Вы ввели некорректное название месяца")








# if month == 1:
#     print("В этом месяце 28 дней")
# elif month== "Январь" or month=="Март" or month=="Май" or month =="Июль" or month =="Август" or month =="Октябрь" or month =="Декабрь":
#     print("В этом месяце 31 день")
# elif month== "Апрель" or month=="Июнь" or month=="Сентябрь" or month =="Ноябрь":
#     print("В этом месяце 30 дней")
# else:
#     print("Некорректное название месяца")

