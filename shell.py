from core import *


def new_gladiator():
    name = input('What is the name of your gladiator? ')
    gladiator = Gladiator(name, 100, 15, 10, 25)
    return gladiator


def main():
    player_1 = new_gladiator()
    player_2 = new_gladiator()


if __name__ == '__main__':
    main()
