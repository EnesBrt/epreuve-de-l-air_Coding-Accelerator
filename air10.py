# Afficher le contenu

import sys


def read_script_content(file_name):

    with open(file_name, "r+") as file:
        print(file.read())


try:
    agrument = sys.argv[1]
    read_script_content(agrument)
except IndexError:
    print("error")
    sys.exit()
except ValueError:
    print("error")
    sys.exit()
except TypeError():
    print("error")
    sys.exit()
