from core import *
from random import choice, randint


class Program:
    def single_multi(self):
        while True:
            choice = input(
                '1) Single Player 2) Multi. Player\n\nWhich would you like to play? '
            )
            if choice == '2':
                name_1 = self.gladiator_name()
                player_1 = self.gladiator_class(name_1)
                name_2 = self.gladiator_name()
                player_2 = self.gladiator_class(name_2)
                self.who_won(player_1, player_2)
            if choice == '1':
                name_1 = self.gladiator_name()
                player_1 = self.gladiator_class(name_1)
                player_2 = Gladiator('Enemy', randint(75, 100), randint(0, 25),
                                     randint(0, 30), randint(5, 15),
                                     randint(15, 50))
                self.single_who_won(player_1, player_2)
            else:
                print('\nPlease put in a valid choice.\n')

    def gladiator_class(self, name):
        while True:
            class_choice = input(
                '\n1) Warrior(Base Stats)\n2) Monk(High Health and Magic, Low Rage, Precision Accuracy)\n3) Berserker(High Rage, Low Magic, Grazing Possibility)\n4) Jester(Very Low Health, Chance To One Shot)\n\nWhat class will you choose? '
            )
            if class_choice == '1':
                gladiator = Gladiator(str(name), 80, 15, 10, 10, 25)
                return gladiator
            if class_choice == '2':
                gladiator = Gladiator(str(name), 100, 0, 30, 25, 25)
                return gladiator
            if class_choice == '3':
                gladiator = Gladiator(str(name), 80, 30, 0, 0, 40)
                return gladiator
            if class_choice == '4':
                gladiator = Gladiator(str(name), 50, 0, 20, 0, 100)
                return gladiator
            else:
                print('\nPlease put in correct number.\n')

    def gladiator_name(self):
        while True:
            name = input('\nWhat is the name of your gladiator? ')
            if name.strip() == '':
                print('\nPlease put in a name.')
            if name.isalpha() == False:
                print('\nPlease put in a name.')
            else:
                return name.capitalize().strip()

    def battle_phase(self, player_1, player_2):
        while True:
            choice = input(
                '\n1) Attack(+15 Rage)\n2) Heal(+10 Health, -10 Rage)\n3) Cast(+10 Health, -10 Magic, -10 Enemy Health)\n4) Pass(+25 Rage, +25 Magic)\n5) Quit\nWhat will you do {}? '.
                format(player_1.name))
            if choice == '1':
                return player_1.attack(player_2)
            elif choice == '2':
                return player_1.heal()
            elif choice == '3':
                return player_1.cast(player_2)
            elif choice == '4':
                return player_1.passing()
            elif choice == '5':
                print('{} Wins!'.format(player_2.name))
                exit()

    def who_won(self, player_1, player_2):
        while True:
            if player_1.is_dead(player_2) == False and player_2.is_dead(
                    player_1) == False:
                print(player_1)
                print(player_2)
                self.battle_phase(player_1, player_2)
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
                    self.battle_phase(player_2, player_1)
                    if player_1.is_dead(player_2) == True:
                        print('\n---------------\n{} Won!'.format(
                            player_2.name))
                        exit()
                    if player_2.is_dead(player_1) == True:
                        print('\n---------------\n{} Won!'.format(
                            player_1.name))
                        exit()

    def single_who_won(self, player_1, player_2):
        while True:
            if player_1.is_dead(player_2) == False and player_2.is_dead(
                    player_1) == False:
                print(player_1)
                print(player_2)
                self.battle_phase(player_1, player_2)
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
                    player_2.ai_battle(player_1)
                    if player_1.is_dead(player_2) == True:
                        print('\n---------------\n{} Won!'.format(
                            player_2.name))
                        exit()
                    if player_2.is_dead(player_1) == True:
                        print('\n---------------\n{} Won!'.format(
                            player_1.name))
                        exit()

    def main(self):
        self.single_multi()


if __name__ == '__main__':
    Program().main()
