# Insertion dans un tableau trié

import sys


def sort_list(numbers_list, number):
    numbers_list.append(number)
    numbers_list = [int(i) for i in numbers_list]
    for n in range(0, len(numbers_list)):
        for x in range(n + 1, len(numbers_list)):
            if numbers_list[n] > numbers_list[x]:
                numbers_list[n], numbers_list[x] = numbers_list[x], numbers_list[n]

    for i in numbers_list:
        print(i, end=" ")


number_list = sys.argv[1:-1]
number = sys.argv[-1]
sort_list(number_list, number)

