people = []
person_1 = {"name":"victor",
            "age":"42",
            "city":"medvedevka",
            }
person_2 = {"name":"dima",
            "age":"43",
            "city":"yalta",
            }
person_3 = {"name":"sasha",
            "age":"39",
            "city":"simpheropol",
            }

people.append(person_1)
people.append(person_2)
people.append(person_3)

for person in people:
    for keys, values in person.items():
        print(keys + ": " + values.title())
    # print(person)

# print(people)