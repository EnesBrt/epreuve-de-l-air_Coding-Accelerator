# Chercher l’intrus

import sys


def no_pair(numbers):
    numbers = [int(i) for i in numbers]
    found = False
    for n in range(0, len(numbers)):
        found = False
        for x in range(n + 1, len(numbers)):
            if numbers[n] == numbers[x]:
                found = True
                break
        if not found:
            print(numbers[n])
            break


argument = sys.argv[1:]
no_pair(argument)
