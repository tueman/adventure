import random


class Sword:
    def __init__(self):
        self.damage = random.randint(1, 10)
        if self.damage <= 2:
            self.type = 'Bronze'
        elif 2 < self.damage <= 4:
            self.type = 'Iron'
        elif 4 < self.damage <= 7:
            self.type = 'Steel'
        elif 7 < self.damage <= 10:
            self.type = 'Titanium'
        self.suffix = random.choice(('Ice', 'Fire', 'Flame', 'Death', 'Life', 'Thunder', 'Frost'))
        self.name = str(self.type + ' Sword of ' + self.suffix)
