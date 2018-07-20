from random import *


class Gladiator:
    def __init__(self, name, health, rage, magic, attack_low, attack_high):
        self.name = name
        self.health = health
        self.rage = rage
        self.magic = magic
        self.attack_low = attack_low
        self.attack_high = attack_high

    def __str__(self):
        return '\n{}\n---------------\nHealth: {}\nRage: {}\nMagic: {}\n---------------\n'.format(
            self.name, self.health, self.rage, self.magic)

    def __repr__(self):
        return 'Gladiator({}, {}, {}, {}, {}, {})'.format(
            self.name, self.health, self.rage, self.magic, self.attack_high,
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
            print(
                '\n********************\nHealth already full.\n********************'
            )
        if 91 <= self.health <= 99:
            if self.rage <= 9:
                print(
                    '\n*******************\nRage is too low.\n********************'
                )
            elif self.rage >= 10:
                self.rage -= 10
                self.health = 100
                return self.health, self.rage
        elif self.health < 91:
            if self.rage <= 9:
                print(
                    '\n********************\nRage is too low.\n********************'
                )
            elif self.rage >= 10:
                self.rage -= 10
                self.health += 10
                return self.health, self.rage

    def cast(self, other):
        if self.health == 100:
            print(
                '\n********************\nHealth already full.\n*******************'
            )
        if 91 <= self.health <= 99:
            if self.magic <= 9:
                print(
                    '\n********************\nMagic is too low.\n********************'
                )
            elif self.magic >= 10:
                other.health = other.health - 10
                self.magic -= 10
                self.health = 100
                return self.health, self.magic, other
        elif self.health < 91:
            if self.magic <= 9:
                print(
                    '\n********************\nMagic is too low.\n********************'
                )
            elif self.magic >= 10:
                other.health = other.health - 10
                self.magic -= 10
                self.health += 10
                return self.health, self.magic, other

    def passing(self):
        self.rage += 25
        self.magic += 25
        return self.rage, self.magic

    def is_dead(self, other):
        if self.health <= 0:
            return True
        else:
            return False

    def ai_battle(self, other):
        if self.health <= 50:
            if self.rage >= 10:
                print('\nEnemy healed.\n')
                return self.heal()
            elif self.magic >= 10:
                print('\nEnemy cast a spell.\n')
                return self.cast(other)
            else:
                print('\nEnemy Passed.\n')
                return self.passing()
        if self.health > 50:
            print('\nEnemy Attacked.\n')
            return self.attack(other)
