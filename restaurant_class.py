class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.type = cuisine_type
        self.number_served = 0

    def name_restaurant(self):
        print('"' + self.name.title() + '"')

    def type_cuisine(self):
        print("Has " + self.type.title() + " cuisine")

    def full_describe(self):
        str(self.name_restaurant()) + str(self.type_cuisine())

    def counter_of_numbers(self):
        print("This restaurant served " + str(self.number_served) + " people today")

    def update_counter_of_numbers(self, quantity):
        self.number_served = quantity

    def increment_people(self, people):
        self.number_served = self.number_served + people

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["fruit ice cream", "milk ice cream", "cacao ice cream"]

    def show_ice_creams(self):
        print("There are next types of ice cream: ")
        print(str(self.flavors).title())


new_restaurant = IceCreamStand("frozen planet", "ice cream" )
new_restaurant.full_describe()

new_restaurant.show_ice_creams()

# restaurant_1 = Restaurant("white nights", "russian")
#
# restaurant_1.counter_of_numbers()
# restaurant_1.update_counter_of_numbers(30)
# restaurant_1.counter_of_numbers()
# restaurant_1.increment_people(25)
# restaurant_1.counter_of_numbers()
