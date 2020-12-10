my_str = "Helloworld"
new_list = []
for symbol in my_str:
    if my_str.count(symbol) ==1:
        new_list.append(symbol)
print(new_list)