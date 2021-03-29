"""Main module for base64 exercise

Copyright (c) 2021 Maxence LAVENU
All Rights Reserved.
Released under the MIT license

"""

from modules.marion import add_zero, create_character_chain, chain_in_list
from modules.maxence import array_right_pad, array_bin_to_int
from modules.hugo import strToList, toASCII, toBinary
from modules.francesco import exercie9, exercie10, exercie11


def main():
    val = input("Entrez une chaîne de caractères : ")
    print(val)

    # Ex 1
    val = strToList(val)
    print(val)

    # Ex 2
    val = toASCII(val)
    print(val)

    # Ex 3
    val = toBinary(val)
    print(val)

    # Ex 4
    val = add_zero(val)
    print(val)

    # Ex 5
    val = create_character_chain(val)
    print(val)

    # Ex 6
    val = chain_in_list(val)
    print(val)

    # Ex 7
    val = array_right_pad(val)
    print(val)

    # Ex 8
    val = array_bin_to_int(val)
    print(val)

    # Ex 9
    val = exercie9(val)
    print(val)

    # Ex 10
    val = exercie10(val)
    print(val)

    # Ex 11
    val = exercie11(val)
    print(val)


if __name__ == '__main__':
    main()
