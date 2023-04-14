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

# Get the operator argument
operator = sys.argv[-1]

add_or_substract(numbers_list, operator)
