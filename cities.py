cities = {"milan": {"country": "italy",
                    "population": "60 millions",
                    "fact": "two big football club"
                    },
          "liverpool": {"country": "england",
                         "population": "80 millions",
                         "fact": " 'The Beatles' is from Liverpool"
                         },
           "madrid": {"country": "spain",
                       "population": "50 millions",
                       "fact": "The best football club in the world  - Real Madrid"
                       }
          }

for city, city_info in cities.items():
    print("City name: " + city.title())
    print("Country: " + city_info["country"].title())
    print("Population of " + city_info["country"].title() + ": " + city_info["population"])
    print("Famous fact about city: " + city_info["fact"] + "\n")