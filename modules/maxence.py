"""Modules made by Maxence LAVENU for base64 exercices

Copyright (c) 2021 Maxence LAVENU
All Rights Reserved.
Released under the MIT license

"""


def array_right_pad(array, length=6):
    paddedArray = []
    for string in array:
        paddedArray.append(string.ljust(length, '0'))
        # adds zeroes to the right to the string until it reaches the wanted length
    return paddedArray


def array_bin_to_int(array):
    intArray = []

    for string in array:
        intArray.append(int(string, 2))
        # converts the binary string as a decimal number
        # (the two is there to specify the original string is in binary)

    return intArray
