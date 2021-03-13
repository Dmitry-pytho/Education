class User():
    def __init__(self, first_name, last_name, age):
        self.first = first_name
        self.last = last_name
        self.age = age

    def describe_user(self):
        print(self.first.title() + " " + self.last.title() + " " + str(self.age))

    def greet_user(self):
        print("Hi, " + self.first.title() + "!\n")

class Privileges():
    def __init__(self):
        self.privileges = ["разрешено добавлять сообщения", "разрешено удалять пользователей", "разрешено банить пользователей"]

    def show_privileges(self):
        print("Полномочия администратора: " + str(self.privileges))

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()




admin = Admin("dmitry", "solomiannyi", 36)

admin.describe_user()

admin.privileges.show_privileges()


