import random


class Sword:
    def __init__(self):
        self.damagemin = random.randint(1, 6)
        if self.damagemin <= 2:
            self.type = 'Bronze'
        elif 2 < self.damagemin <= 3:
            self.type = 'Iron'
        elif 3 < self.damagemin <= 5:
            self.type = 'Steel'
        elif 5 < self.damagemin <= 6:
            self.type = 'Titanium'
        self.damagemax = random.randint(6, 12)
        self.damage = (self.damagemin, self.damagemax)
        self.suffix = random.choice(('Ice', 'Fire', 'Flame', 'Death', 'Life', 'Thunder', 'Frost'))
        self.name = str(self.type + ' Sword of ' + self.suffix)
