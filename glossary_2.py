geographic = {"nile":"egypt",
              "dnepr":"ukraine",
              "mercie":"england"}

geographic["volga"]="russia"
geographic["amazon"]="brasil"

long_rivers = ["amazon","nile"]

for river in geographic.keys():
    if river in long_rivers:
        print(river.title() + " is one of the longest river in the world!")


# for river in geographic.keys():
#     print(river.title())
# for country in geographic.values():
#     print(country.title())
# for river, country in sorted(geographic.items()):
#     print(river.title() + " - " + country.title())
#
# if "nile" in geographic.keys():
#     print("You must visit " + geographic["nile"].title() +  " in June!")