"""Module name

Copyright (c) 2021 Hugo Monnerie
All Rights Reserved.
Released under the MIT license

"""

def strToList(str):
    print(f'exo1: {list(str.strip())}')


def strToASCII(str):
    print(f'exo2: {[ord(c) for c in str]}')


def strToBinary(str):
    print(f'exo3: ' + ' '.join(format(ord(i), '08b') for i in str))
