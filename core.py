from random import *


class Gladiator:
    def __init__(self, name, health, rage, attack_high, attack_low):
        self.name = name
        self.health = health
        self.rage = rage
        self.attack_high = attack_high
        self.attack_low = attack_low

    def __str__(self):
        return '{}\n__________\nHealth: {}\nRage: {}\n__________\n'.format(
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
            self.rage = 0
            return other
        elif critical > self.rage:
            other = damage
            self.rage += 15
            return other

    def heal(self):
        if self.rage < 10:
            return None
        if self.rage >= 10:
            if self.health >= 100:
                return None
            if 86 <= self.health >= 99:
                self.health = 100
                self.rage = self.rage - 10
                return self.health, self.rage
            else:
                self.health = self.health + 15
                self.rage = self.rage - 10
                return self.heatlh, self.rage

    def is_dead(self, other):
        if self.health <= 0:
            print('{} Wins!'.format(other.name))
            exit()
        if other.health <= 0:
            print('{} Wins!'.format(self.name))
            exit()
        else:
            return False
