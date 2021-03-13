class Car():
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 53000

    def get_descriptive_name(self):
        long_name = str(self.year) + " " + self.make + " " + self.model
        print(long_name.title())
        return long_name

    def read_odometer(self):
        print("This car has " + str(self.odometer_reading) + " kilometers on it.\n")

    def update_odometer(self,mileage):
        self.odometer_reading = mileage
        # if mileage >= self.odometer_reading:
        #     self.odometer_reading = mileage
        # else:
        #     print("You can't roll back an odometer")

    # def increment_odometer(self, miles):
    #     if miles>=0:
    #         self.odometer_reading = self.odometer_reading + miles
    #     else:
    #         print("You can't roll back an odometer")



my_used_car = Car("subaru", "outback", 2013)
my_used_car.get_descriptive_name()
my_used_car.update_odometer(5400)
my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
