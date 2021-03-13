users = {"aeinstein": {"first name": "albert",
                       "last name": "aeinstein",
                       "location": "princeton"
                       },
         "mcurie": {"first name": "marie",
                    "last name": "curie",
                    "location": "paris"
                    },
         "dmendeleev": {"first name": "dmitry",
                    "last name": "mendeleev",
                    "location": "moscow"
                    }
         }

for username, user_info in users.items():
    print("\nUsername: " + username)

    full_name = user_info["first name"]+ " " + user_info["last name"]
    location = user_info["location"]
    print("\tFull name: " + full_name.title())
    print("\t Location: " + location.title())