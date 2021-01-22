from random import randint, choice, shuffle
import string


class EmailGeneratror:

    def __init__(self, names, domains):
        self.name_txt = names
        self.domains_txt = domains

        self.domains = self.get_domain()
        self.names = self.get_name()



    def get_domain(self):
        with open(self.domains_txt, "r") as txt:
            spisok_domenov = []
            for line in txt.readlines():
                spisok_domenov.append(line.replace("\n", "").replace(".", ""))
            return spisok_domenov



    def get_name(self):
        with open(self.name_txt, "r") as text:
            spisok_names = []
            for line in text.readlines():
                spisok_names.append(line.split()[1])
            return spisok_names

    def generate_random_numbers(self):
        self.number = str(randint(100, 1000))
        return self.number

    def generate_random_letters(self):
        alphabet = list(string.ascii_lowercase)
        shuffle(alphabet)
        random_letters = ""
        for x in range(randint(5, 7)):
            letter = choice(alphabet)
            random_letters = random_letters + letter
        return random_letters

    def generate_email(self):
        result = choice(
            self.get_name()) + self.generate_random_numbers() + "@" + self.generate_random_letters() + "." + choice(
            self.get_domain())
        return result

    def __repr__(self):
        my_str = ("len domains = " +  str(len(self.domains))) +"," + ("len names = " +  str(len(self.names)))
        return my_str


email_generator = EmailGeneratror("d:\Дима\Python\Education\_names.txt", "d:\Дима\Python\Education\domains.txt")


email = email_generator.generate_email()
print(email)
print(email_generator)
