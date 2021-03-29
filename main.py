"""Main module for base64 exercise

Copyright (c) 2021 Maxence LAVENU
All Rights Reserved.
Released under the MIT license

"""

from modules.hugo import strToList, strToASCII, strToBinary

str = 'ABCDE'


def main():
    val = input("Entrez une chaîne de caractères : ")
    print(val)
    valList = strToList(val)
    print(valList)

    valAscii = strToASCII(valList)
    print(valAscii)

    valBinary = strToBinary(valAscii)
    print(valBinary)


if __name__ == '__main__':
    main()
