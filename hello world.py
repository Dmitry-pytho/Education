my_int = 5076070000000
new_number = str(my_int)
result = len(new_number) - len(new_number.rstrip('0'))
print(result)
