from core import *


class TestGladiator:
    def setup(self):
        self.gladiator = Gladiator('Name', 1, 2, 3, 4)

    def test_gladiator_str(self):
        assert self.gladiator.name == ('Name')
        assert self.gladiator.health == (1)
        assert self.gladiator.rage == (2)
        assert self.gladiator.attack_high == (3)
        assert self.gladiator.attack_low == (4)
