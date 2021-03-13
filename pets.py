# pets = []
# tom = {"animal": "cat",
#        "name owner": "jack"}
# plutto = {"animal": "dog",
#           "name owner": "william"}
# boosya = {"animal": "sea pig",
#           "name owner": "mary"}
# pets.append(tom)
# pets.append(plutto)
# pets.append(boosya)
# for pet in pets:
#     for animal, owner in pet.items():
#         print(animal.title() + ": " "\n" +"\t" + owner.title())

def describe_pet(pet_name, animal_type):
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")



describe_pet("bob")
# describe_pet("dog", "black")
# describe_pet("cat", "merlin")
