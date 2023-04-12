# Concat

import sys

def concat(*string, seperateur):
    array = [i for i in string]
    strings = ""
    for n in array:
        strings += (n + seperateur)
    print(strings)
    return strings


if len(sys.argv) > 2:
    argument_strings = sys.argv[1:-1]
    argument_separator = sys.argv[-1]

    concat(*argument_strings, seperateur=argument_separator)