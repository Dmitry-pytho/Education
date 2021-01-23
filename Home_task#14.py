class Unit:
    def __init__(self, name, clan):
        self.name = name
        self.clan = clan
        self.healthy = 100
        self.power = 1
        self.ability = 1
        self.brain = 1
        self.unit_type = ""

    def __repr__(self):
        return f"Name: {self.name}, clan: {self.clan}, intellect: {self.brain}, power: {self.power}"

    def get_healthy(self):
        if self.healthy >= 1:
            self.healthy = self.healthy + 10
        if self.healthy > 100:
            self.healthy = 100

    def increase_basic_skill(self):
        if self.unit_type == "magian":
            if self.brain >= 10:
                print("Максимальный уровень навыка")
            else:
                self.brain += 1
        elif self.unit_type == "archer":
            if self.ability >= 10:
                print("Максимальный уровень навыка")
            else:
                self.ability += 1
        elif self.unit_type == "knight":
            if self.power >= 10:
                print("Максимальный уровень навыка")
            else:
                self.power += 1

    def show_basic_skill(self):
        print("brain", self.brain)
        print("ability", self.ability)
        print("power", self.power)


class Magian(Unit):
    def __init__(self, name, clan, type_magic):
        super().__init__(name, clan)
        self.type_magic = type_magic
        self.unit_type = "magian"


class Archer(Unit):
    def __init__(self, name, clan, type_range_weapon):
        super().__init__(name, clan)
        self.type_range_weapon = type_range_weapon
        self.unit_type = "archer"


class Knight(Unit):
    def __init__(self, name, clan, type_weapon):
        super().__init__(name, clan)
        self.type_weapon = type_weapon
        self.unit_type = "knight"


knight1 = Knight("John", "Lancaster", "Sword")
archer1 = Archer("Tom", "Stuart", "Crossbow")
magian1 = Magian("Garry", "Stone", "Fire")
