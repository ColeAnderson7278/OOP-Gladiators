from core import *


def new_gladiator():
    name = input('What is the name of your gladiator? ')
    gladiator = Gladiator(name, 100, 15, 10, 25)
    return gladiator


def battle_phase(player_1, player_2):
    while True:
        choice = input(
            '\n1) Attack\n2) Heal\n3) Pass\n4) Quit\nWhat will you do {}? '.
            format(player_1.name))
        if choice == '1':
            return player_1.attack(player_2)
        if choice == '2':
            return player_1.heal()
        if choice == '3':
            return None
        if choice == '4':
            print('{} Wins!'.format(player_2.name))


def who_won(player_1, player_2):
    if player_1.is_dead(player_2) == True:
        print('{} Won!'.format(player_2.name))
        return True
    if player_2.is_dead(player_1) == True:
        print('{} Won!'.format(player_1.name))
        return True
    else:
        return False


def main():
    player_1 = new_gladiator()
    player_2 = new_gladiator()
    while who_won(player_1, player_2) == False:
        battle_phase(player_1, player_2)
        print(player_1)
        print(player_2)
        battle_phase(player_2, player_1)
        print(player_1)
        print(player_2)


if __name__ == '__main__':
    main()
