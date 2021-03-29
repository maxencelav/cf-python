"""Module name

Copyright (c) 2021 Marion Meurant
All Rights Reserved.
Released under the MIT license

"""


def add_zero(array):
    array_with_zero = [str(item).zfill(8) for item in array]
    return array_with_zero


def create_character_chain(array):
    list_in_string = "".join(array)
    return list_in_string


def chain_in_list(string):
    string_in_array = [string[i:i + 6] for i in range(0, len(string), 6)]
    return string_in_array
