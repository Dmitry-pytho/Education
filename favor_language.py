favorite_language = {"dima": ["python", "ruby"],
                     "eugenij": ["python", "java"],
                     "jouri": ["c++"],
                     "helen": ["forth", "pascal"]
                     }
favorite_language["kate"]=["java", "c#"]
favorite_language["helen"].append("delphi")
favorite_language["dima"].append("assembler")
# for name, languages in favorite_language.items():
#     print("\n" + name.title() + "'s favorite language are: ")
#     for language in languages:
#         print("\t" + language.title())





for name, languages in favorite_language.items():
    if len(languages) >= 2:
        print("\n" + name.title() + "'s favorite languages are: ")
        for language in languages:
            print("\t" + language.title())
    if len(languages)<2:
        print("\n" + name.title() + "'s favorite language is: ")
        # for language in languages:
        print("\t" + languages[0].title())
        # print("\t"+ language.title())




        # if len(languages)<2:
        #     print("\n" + name.title() + "'s favorite language is: ")
        #     print("\t" + language.title())


