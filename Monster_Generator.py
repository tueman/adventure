import random


class Monster:
    def __init__(self):
        self.type = random.choice(('Spider', 'Rat', 'Zombie', 'Skeleton', 'Goblin'))
        self.identifier = random.choice(('Giant', 'Tiny', 'Evil'))
        self.name = str(self.identifier + ' ' + self.type)
        self.damagemin = random.randint(1, 5)
        self.damagemax = random.randint(5, 10)
        self.damagerange = (self.damagemin, self.damagemax)
        self.health = random.randint(5, 20)
