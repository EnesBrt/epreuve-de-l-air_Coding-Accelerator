# Concat

import sys


def concat(*string, seperateur):
    array = [i for i in string]
    strings = ""
    for n in array:
        strings += (n + seperateur)
    print(strings)
    return strings


try:
    if len(sys.argv) > 2:
        argument_strings = sys.argv[1:-1]
        argument_separator = sys.argv[-1]
        concat(*argument_strings, seperateur=argument_separator)
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
