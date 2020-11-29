my_str = "My name is Vova. I'm a teacher !"
for symbol in my_str:
    if not symbol.isupper() and symbol.isalpha() :
        print(symbol)