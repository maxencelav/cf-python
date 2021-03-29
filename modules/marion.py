"""Module name

Copyright (c) 2021 Marion Meurant
All Rights Reserved.
Released under the MIT license

"""

def add_zero():
    array = ['1000001', '1000010', '1000011', '1000100', '1000101']
    array_with_zero = [str(item).zfill(8) for item in array]
    print(array_with_zero)

def create_character_chain():
    array = ['01000001', '01000010', '01000011', '01000100', '01000101']
    list_in_string = "".join(array)
    print(list_in_string)

def chain_in_list():
    string = "0100000101000010010000110100010001000101"
    string_in_array = [string[i:i+6] for i in range(0, len(string), 6)]
    print(string_in_array)

def main():
    add_zero()
    create_character_chain()
    chain_in_list()


if __name__ == '__main__':
    main()
