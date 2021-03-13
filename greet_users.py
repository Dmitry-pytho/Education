class User():
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print("Full information of person:")
        print("\t" + self.first_name.title())
        print("\t" + self.last_name.title())
        print("\t" + str(self.age) + " years old")

    def greet_user(self):
        print("Hello, " + self.first_name.title() + " " + self.last_name.title())

    def print_login_attempts(self):
        print("The number of login attempts is: "+ str(self.login_attempts))

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


person1 = User("john", "travolta", 67)

person1.describe_user()

person1.print_login_attempts()

person1.increment_login_attempts()

person1.print_login_attempts()
person1.increment_login_attempts()
person1.print_login_attempts()
person1.reset_login_attempts()
person1.print_login_attempts()
