# Contrôle de pass sanitaire

import sys


def delete_absent_character(string_list, letter):
    new_list = []
    for n in string_list:
        if letter.lower() not in n.lower():
            new_list.append(n)

    print(new_list)


try:
    string_list = [arg for arg in sys.argv[1:-1]]
    letter = sys.argv[-1]
    delete_absent_character(string_list, letter)
except IndexError:
    print("error")
    sys.exit()
except ValueError:
    print("error")
    sys.exit()
except TypeError():
    print("error")
    sys.exit()
