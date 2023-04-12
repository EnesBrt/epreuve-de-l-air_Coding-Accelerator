# Split

import sys


def custom_split(string, separator):
    words = []
    temporary_strings = ""

    for n in string:
        if n == separator:
            words.append(temporary_strings)
            temporary_strings = ""
        else:
            temporary_strings += n

    words.append(temporary_strings)
    print(words)
    for x in words:
        print(x)

    return words


argument_one = sys.argv[1]
argument_two = sys.argv[2]

custom_split(argument_one, argument_two)
