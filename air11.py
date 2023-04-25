# Afficher une pyramide

import sys


def pyramid(string, number):
    for i in range(number):
        spaces = number - i
        for n in range(spaces):
            print(" ", end="")
        num = ((i + 1) * 2) - 1
        for x in range(num):
            print(string, end="")
        print("\n")


try:
    argument_one = sys.argv[1]
    argument_two = int(sys.argv[2])
    pyramid(argument_one, argument_two)
except IndexError:
    print("error")
    sys.exit()
except ValueError:
    print("error")
    sys.exit()
except TypeError():
    print("error")
    sys.exit()
