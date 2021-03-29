"""Main module for 1,2,3 exercises

Copyright (c) 2021 Hugo Monnerie
All Rights Reserved.
Released under the MIT license

"""

def strToList(str):
    return list(str.strip())


def toASCII(str):
    result = []
    for s in str:
        result.append(ord(c) for c in s)
    return result


def toBinary(str):
    result = []
    for s in str:
        result.append(format(ord(x), "b") for x in s)
    return result