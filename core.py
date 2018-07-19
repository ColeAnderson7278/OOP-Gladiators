from random import *


class Gladiator:
    def __init__(self, name, health, rage, attack_low, attack_high):
        self.name = name
        self.health = health
        self.rage = rage
        self.attack_low = attack_low
        self.attack_high = attack_high

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
            if self.rage >= 100:
                other.health = damage
                self.rage = 100
                return other
            if 86 <= self.rage <= 99:
                other.health = damage
                self.rage = 100
                return other
            if self.rage < 86:
                other.health = damage
                self.rage += 15
                return other

    def heal(self):
        if self.health == 100:
            return None
        if 91 <= self.health <= 99:
            if self.rage <= 9:
                return None
            elif self.rage >= 10:
                self.rage -= 10
                self.health = 100
                return self.health, self.rage
        elif self.health < 91:
            if self.rage <= 9:
                return None
            elif self.rage >= 10:
                self.rage -= 10
                self.health += 10
                return self.health, self.rage

    def passing(self):
        if self.rage >= 100:
            self.rage = 100
            return self.rage
        if 76 <= self.rage <= 99:
            self.rage = 100
            return self.rage
        if self.rage < 76:
            self.rage += 25
            return self.rage

    def is_dead(self, other):
        if self.health <= 0:
            return True
        else:
            return False
