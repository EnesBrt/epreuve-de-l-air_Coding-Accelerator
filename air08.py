# Mélanger deux tableaux triés

import sys


def fusion(list_one, word, list_two):
    new_list = []

    if word == "fusion":
        for y in list_one:
            new_list.append(y)
        for z in list_two:
            new_list.append(z)

    for n in range(0, len(new_list)):
        for x in range(n + 1, len(new_list)):
            if new_list[n] > new_list[x]:
                new_list[n], new_list[x] = new_list[x], new_list[n]

    for i in new_list:
        print(i, end=" ")


try:
    fusion_index = sys.argv.index("fusion")
    list_one = [int(arg) for arg in sys.argv[1:fusion_index]]
    list_two = [int(arg) for arg in sys.argv[fusion_index + 1:]]
    fusion(list_one, "fusion", list_two)
except IndexError:
    print("error")
    sys.exit()
except ValueError:
    print("error")
    sys.exit()
except TypeError():
    print("error")
    sys.exit()
