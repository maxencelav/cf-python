"""Module name

Copyright (c) 2021 Maxence LAVENU
All Rights Reserved.
Released under the MIT license

"""

from modules.hugo import strToList, strToASCII, strToBinary

str = 'ABCDE'

def main():
    strToList(str)
    strToASCII(str)
    strToBinary(str)


if __name__ == '__main__':
    main()
