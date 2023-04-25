# Sur chacun d’entre eux

import sys


def add_or_substract(numbers, operator):
    new_list = []

    for n in numbers:
        if "+" in operator:
            result = n + int(operator[1])
            new_list.append(result)
        elif "-" in operator:
            result = n - int(operator[1])
            new_list.append(result)

    for x in new_list:
        print(x, end=" ")


numbers_list = [int(arg) for arg in sys.argv[1:-1]]

try:
    operator = sys.argv[-1]
    add_or_substract(numbers_list, operator)
except IndexError:
    print("error")
    sys.exit()
except ValueError:
    print("error")
    sys.exit()
except TypeError():
    print("error")
    sys.exit()
