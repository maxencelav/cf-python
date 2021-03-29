"""Module name

Copyright (c) 2021 Maxence LAVENU
All Rights Reserved.
Released under the MIT license

"""

import modules.maxence

def main():
    arrayToPad = ['010000', '010100', '001001', '000011', '010001', '000100', '0101']
    binaryArray = modules.maxence.array_right_pad(arrayToPad,6)
    print(binaryArray)

    stringArray = modules.maxence.array_bin_to_int(binaryArray)
    print(stringArray)
    pass


if __name__ == '__main__':
    main()
