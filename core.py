from random import *


class Gladiator:
    def __init__(self, name, health, rage, attack_low, attack_high):
        self.name = name
        self.health = health
        self.rage = rage
        self.attack_high = attack_high
        self.attack_low = attack_low

    def __str__(self):
        return '\n{}\n---------------\nHealth: {}\nRage: {}\n---------------\n'.format(
            self.name, self.health, self.rage)

    def __repr__(self):
        return 'Gladiator({}, {}, {}, {}, {})'.format(
            self.name, self.health, self.rage, self.attack_high,
            self.attack_low)

    def attack(self, other):
        damage = other.health - randint(self.attack_low, self.attack_high)
        crit_hit = other.health - (
            randint(self.attack_low, self.attack_high) * 2)
        critical = randrange(1, 101)

        if critical <= self.rage:
            other.health = crit_hit
            print('\n^^^^^^^^^^^^^^^\nCritical Hit!\n^^^^^^^^^^^^^^^')
            self.rage = 0
            return other
        if self.rage < critical:
            other.health = damage
            self.rage += 15
            return other

    def heal(self):
        if self.rage < 10:
            return None
        elif self.rage >= 10:
            self.health += 10
            self.rage -= 10
        if self.health >= 100:
            self.health = 100
            return self.health

    def is_dead(self, other):
        if self.health <= 0:
            return True
        else:
            return False
