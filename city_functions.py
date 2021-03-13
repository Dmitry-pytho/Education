def get_formatted_name_city(city, country, population=""):
    if population:
        full_name_city = city + ", " + country  + " population - " + str(population)
    else:
        full_name_city = city + ", " + country
    return full_name_city.title()
