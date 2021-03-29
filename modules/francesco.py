
import string

base64 = string.ascii_uppercase + string.ascii_lowercase + "123456789+/"


def exercie9(list):
    list = [elem.to_bytes(5, byteorder='big').decode('utf-8') for elem in list]
    return list


def int_to_base64(value):
    if base64 / value >= len(base64):
        print("hello")


"""
list : array of string

translate list to string with all values in the list

return string
"""


def exercie10(list):
    val = ""
    for i in list:
        val = val+i
    return val


"""
value :  string

add "=" while value is not multiple of 4

return string
"""


def exercie11(value):
    while len(value) % 4 != 0:
        value = value+"="
    return value
