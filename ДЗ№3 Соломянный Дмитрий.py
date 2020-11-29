#1
value = 123
new_value = (value/2) if value <100 else value *-1
print(new_value)

###########################################################
#2
value = 100
new_value = 1 if value <100 else 0
print(new_value)

##########################################################
#3
value = 90
new_value = True if value <100 else False
print(new_value)

#########################################################
#4
my_str = "я учусь в школе hillel!"
my_str_big = my_str.upper()
print(my_str_big)

###########################################################
#5
my_str = "И ЭТО КЛАССНО!"
my_str_big = my_str.lower()
print(my_str_big)

###########################################################
#6
my_str = "Киев"
new_my_str = "Киев самый большой город в Украине" if len(my_str)<5 else my_str
print(new_my_str)

###########################################################
#7
my_str = "Киев"
new_my_str = my_str[::-1] if len(my_str)<5 else my_str
print(new_my_str)

###########################################################
#8
my_str = "Днепропетровск основан в 1776 году"
for symbol in my_str:
    if  symbol.isalnum():
        print("символ", symbol)

##########################################################
#9
my_str = "Днепропетровск основан в 1776 году!!!!???"
for symbol in my_str:
    if  not symbol.isalnum():
        print("символ", symbol)

###########################################################
#10
my_str = "Днепропетровск основан в 1776 году+++---"
for symbol in my_str:
    if  not symbol.isalnum() and not symbol ==" ":
        print("символ", symbol)
