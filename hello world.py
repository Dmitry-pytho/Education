my_str = "43 больше чем 34 но меньше чем 56"
parts_my_str = my_str.split()
print(parts_my_str)
suma_chisel = 0
for symbol in parts_my_str:
    if symbol.isdigit():
        suma_chisel = suma_chisel + int(symbol)
print(suma_chisel)