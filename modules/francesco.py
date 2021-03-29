
import string

base64 = string.ascii_uppercase + string.ascii_lowercase + "123456789+/"


def exercie9(list):
    list = [elem.to_bytes(5, byteorder='big').decode('utf-8') for elem in list]

    return list


def int_to_base64(value):
    if base64 / value >= len(base64)


def exercie10(list):
    val = ""
    for i in list:
        val = val+i
    return val


def exercie11(string):
    while len(string) % 4 != 0:
        string = string+"="
    return string


exercie9([1, 2, 2])
