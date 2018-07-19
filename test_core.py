from core import *


class TestGladiator:
    def setup(self):
        self.gladiator = Gladiator('Name', 1, 2, 3, 4, 5)

    def test_gladiator_str(self):
        assert self.gladiator.name == ('Name')
        assert self.gladiator.health == (1)
        assert self.gladiator.rage == (2)
        assert self.gladiator.magic == (3)
        assert self.gladiator.attack_low == (4)
        assert self.gladiator.attack_high == (5)

    def test_gladiator_attack(self):
        joe = Gladiator('Joe', 25, 25, 5, 5, 5)
        bob = Gladiator('Bob', 35, 5, 1, 2, 3)
        rick = Gladiator('Rick', 99, 10, 1, 2, 3)
        assert joe.attack(bob) == (bob)
        assert bob.attack(rick) == (rick)
        assert rick.attack(joe) == (joe)

    def test_gladiator_heal(self):
        joe = Gladiator('Joe', 25, 25, 1, 2, 3)
        bob = Gladiator('Bob', 35, 5, 1, 2, 3)
        rick = Gladiator('Rick', 99, 10, 1, 2, 3)
        assert joe.heal() == (35, 15)
        assert bob.heal() == None
        assert rick.heal() == (100, 0)

    def test_gladiator_cast(self):
        joe = Gladiator('Joe', 100, 25, 25, 2, 3)
        bob = Gladiator('Bob', 35, 15, 15, 2, 3)
        assert joe.cast(bob) == (None)
        assert bob.cast(joe) == (45, 5, joe)

    def test_gladiator_passing(self):
        joe = Gladiator('Joe', 25, 25, 5, 5, 5)
        bob = Gladiator('Bob', 35, 5, 1, 2, 3)
        assert joe.passing() == (50, 30)
        assert bob.passing() == (30, 26)

    def test_gladiator_is_dead(self):
        joe = Gladiator('Joe', 1, 1, 1, 1, 1)
        not_joe = Gladiator('Not Joe', 0, 0, 0, 0, 0)
        assert joe.is_dead(not_joe) == False
        assert not_joe.is_dead(joe) == True
