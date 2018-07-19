from core import *


class TestGladiator:
    def setup(self):
        self.gladiator = Gladiator('Name', 1, 2, 3, 4)

    def test_gladiator_str(self):
        assert self.gladiator.name == ('Name')
        assert self.gladiator.health == (1)
        assert self.gladiator.rage == (2)
        assert self.gladiator.attack_low == (3)
        assert self.gladiator.attack_high == (4)

    def test_gladiator_heal(self):
        joe = Gladiator('Joe', 25, 25, 1, 2)
        bob = Gladiator('Bob', 35, 5, 1, 2)
        rick = Gladiator('Rick', 99, 10, 1, 2)
        assert joe.heal() == (35, 15)
        assert bob.heal() == None
        assert rick.heal() == (100, 0)
