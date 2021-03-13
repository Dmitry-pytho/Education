def show_magicians(list_of_magicians):
    for magician in list_of_magicians:
        print("\t" + magician.title())


def great_magicians(list_of_magicians):
    for i, name in enumerate(list_of_magicians):
        list_of_magicians[i] = "Great " + name.title()
    for magician in list_of_magicians:
        print(magician)

list_of_magicians = ["piter", "joe", "william"]
show_magicians(list_of_magicians)
great_magicians(list_of_magicians)
