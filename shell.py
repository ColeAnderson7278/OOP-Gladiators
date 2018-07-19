from core import *


def new_gladiator():
    name = input('\nWhat is the name of your gladiator? ')
    name = name.capitalize()
    class_choice = input(
        '\n1) Warrior(Base Stats)\n2) Monk(High Health, Low Rage, Precision Accuracy)\n3) Berserker(High Rage, Low Health, Grazing Possibility)\n4) Jester(Very Low Health, Chance To One Shot)\nWhat class will you choose? '
    )
    if class_choice == '1':
        gladiator = Gladiator(name, 80, 15, 10, 25)
        return gladiator
    if class_choice == '2':
        gladiator = Gladiator(name, 100, 0, 30, 30)
        return gladiator
    if class_choice == '3':
        gladiator = Gladiator(name, 75, 30, 0, 40)
        return gladiator
    if class_choice == '4':
        gladiator = Gladiator(name, 50, 0, 0, 100)
        return gladiator
    else:
        print('\nPlease put in correct number.\n')


def battle_phase(player_1, player_2):
    while True:
        choice = input(
            '\n1) Attack(+15 Rage)\n2) Heal(+10 Health, -10 Rage)\n3) Pass(+25 Rage)\n4) Quit\nWhat will you do {}? '.
            format(player_1.name))
        if choice == '1':
            return player_1.attack(player_2)
        elif choice == '2':
            return player_1.heal()
        elif choice == '3':
            return player_1.passing()
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
