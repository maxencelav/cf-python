"""Main module for base64 exercise

Copyright (c) 2021 Maxence LAVENU
All Rights Reserved.
Released under the MIT license

"""

from modules.hugo import strToList, strToASCII, strToBinary
from modules.marion import add_zero, create_character_chain, chain_in_list
from modules.maxence import array_right_pad, array_bin_to_int

str = 'ABCDE'


def main():
    val = input("Entrez une chaîne de caractères : ")
    print(val)

    val = strToList(val)
    print(val)

    val = strToASCII(val)
    print(val)

    val = strToBinary(val)
    print(val)

    val = add_zero(val)
    print(val)

    val = create_character_chain(val)
    print(val)

    val = chain_in_list(val)
    print(val)

    val = array_right_pad(val)
    print(val)

    val = array_bin_to_int(val)
    print(val)


if __name__ == '__main__':
    main()
