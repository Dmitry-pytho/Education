filename = "/home/dmitry/PycharmProjects/Education/Files_for_read/greet_guests.txt"
name = "\nPlease enter your name:"
name += "\n(Enter 'quit' when you are finished.) "
while True:
    with open(filename, "w") as txt_file:
        txt_file.write(input(name))
        txt_file.write("Hello " + name)
        if name=="quit":
            break
        else:
            print("Hello " + name + "!")

