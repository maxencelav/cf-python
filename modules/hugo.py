"""Main module for 1,2,3 exercises

Copyright (c) 2021 Hugo Monnerie
All Rights Reserved.
Released under the MIT license

"""


def strToList(str):
    return list(str.strip())


def toASCII(array):
    result = []
    for letter in array:
        result.append(ord(letter))
    return result


def toBinary(array):
    result = []
    for number in array:
        result.append(bin(int(number)).replace("0b", ""))
    return result
