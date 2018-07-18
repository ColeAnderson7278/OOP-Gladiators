class Gladiator:
    def __init__(self, name, health, rage, attack_high, attack_low):
        self.name = name
        self.health = health
        self.rage = rage
        self.attack_high = attack_high
        self.attack_low = attack_low

    def __str__(self):
        return '{}\n----------\nHealth: {}\nRage: {}\n----------'.format(
            self.name, self.health, self.rage)

    def __repr__(self):
        return 'Gladiator({}, {}, {}, {}, {})'.format(
            self.name, self.health, self.rage, self.attack_high,
            self.attack_low)


#class Battle(Gladiator):
#    def __init__(self,other):
