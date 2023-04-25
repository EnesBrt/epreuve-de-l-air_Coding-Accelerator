# Rotation vers la gauche

import sys


def to_the_left(sting_list):
    index_order = [1, 2, 3, 0]
    new_list = [sting_list[i] for i in index_order]
    print(new_list)

    for n in range(len(new_list)):
        if n == len(new_list) - 1:
            print(new_list[n], end='')
        else:
            print(new_list[n], end=', ')

try:
    string_list = [arg for arg in sys.argv[1:]]
    to_the_left(string_list)
except IndexError:
    print("error")
    sys.exit()
except ValueError:
    print("error")
    sys.exit()
except TypeError():
    print("error")
    sys.exit()
