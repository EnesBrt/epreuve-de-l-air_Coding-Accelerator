# Split en fonction

import sys


def split_in_function(string, separator):
    array = []
    temp = ""
    i = 0
    while i < len(string):
        if string[i:i + len(separator)] == separator:
            array.append(temp)
            temp = ""
            i += len(separator)
        else:
            temp += string[i]
            i += 1

    if temp != "":
        array.append(temp)

    for x in array:
        print(x)

    return array


try:
    if len(sys.argv) > 2:
        argument_one = sys.argv[1]
        argument_two = sys.argv[2]
        split_in_function(argument_one, argument_two)
    else:
        print("error")
        sys.exit()
except IndexError:
    print("error")
    sys.exit()
except ValueError:
    print("error")
    sys.exit()
except TypeError():
    print("error")
    sys.exit()
