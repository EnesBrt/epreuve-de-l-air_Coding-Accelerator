# Le roi des tris
import random
import sys


def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = random.choice(array)
    left = []
    right = []
    for n in array:
        if n < pivot:
            left.append(n)
        elif n > pivot:
            right.append(n)

    sorted_left = quick_sort(left)
    sorted_right = quick_sort(right)

    sorted_list = sorted_left + [pivot] + sorted_right

    return sorted_list


try:
    argument = [int(arg) for arg in sys.argv[1:]]
    sorted_array = quick_sort(argument)
    for number in sorted_array:
        print(number, end=" ")
except IndexError:
    print("error")
    sys.exit()
except ValueError:
    print("error")
    sys.exit()
except TypeError():
    print("error")
    sys.exit()
