# Afficher le contenu

import sys


def read_script_content(file_name):

    with open(file_name, "r+") as file:
        print(file.read())


agrument = sys.argv[1]
read_script_content(agrument)
