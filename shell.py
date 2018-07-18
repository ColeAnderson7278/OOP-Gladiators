from core import *


def making_gladiator():
    gladiator_name = input('What is your name gladiator? ')
    return Gladiator(str(gladiator_name), 100, 15, 25, 10)


def main():
    gladiator1 = making_gladiator()
    print(gladiator1)


if __name__ == '__main__':
    main()
