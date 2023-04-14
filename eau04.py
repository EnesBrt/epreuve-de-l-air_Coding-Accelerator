# Un seul à la fois

import sys


def one_at_the_time(string):
    result = ""
    for n in range(len(string) - 1):
        character = string[n]
        next_character = string[n + 1]
        if character != next_character:
            result += string[n]
        else:
            continue

    result += string[-1]


    print(result)


argument = sys.argv[1]
one_at_the_time(argument)
