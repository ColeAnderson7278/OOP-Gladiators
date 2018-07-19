from core import *


def new_gladiator():
    name = input('What is the name of your gladiator? ')
    gladiator = Gladiator(name.capitalize(), 100, 15, 9, 25)
    return gladiator


def battle_phase(player_1, player_2):
    while True:
        choice = input(
            '\n1) Attack\n2) Heal\n3) Pass\n4) Quit\nWhat will you do {}? '.
            format(player_1.name))
        if choice == '1':
            return player_1.attack(player_2)
        elif choice == '2':
            return player_1.heal()
        elif choice == '3':
            return None
        elif choice == '4':
            print('{} Wins!'.format(player_2.name))
            exit()


def who_won(player_1, player_2):
    while True:
        if player_1.is_dead(player_2) == False and player_2.is_dead(
                player_1) == False:
            print(player_1)
            print(player_2)
            battle_phase(player_1, player_2)
            if player_1.is_dead(player_2) == True:
                print('\n---------------\n{} Won!'.format(player_2.name))
                exit()
            if player_2.is_dead(player_1) == True:
                print('\n---------------\n{} Won!'.format(player_1.name))
                exit()
            elif player_1.is_dead(player_2) == False and player_2.is_dead(
                    player_1) == False:
                print(player_1)
                print(player_2)
                battle_phase(player_2, player_1)
                if player_1.is_dead(player_2) == True:
                    print('\n---------------\n{} Won!'.format(player_2.name))
                    exit()
                if player_2.is_dead(player_1) == True:
                    print('\n---------------\n{} Won!'.format(player_1.name))
                    exit()


def main():
    player_1 = new_gladiator()
    player_2 = new_gladiator()
    who_won(player_1, player_2)


if __name__ == '__main__':
    main()
