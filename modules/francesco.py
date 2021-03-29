
import string

base64 = string.ascii_uppercase + string.ascii_lowercase + "123456789+/"

"""
list : array of int

translate list of int in list of string base64

return array of string
"""


def exercie9(list):
    return [base64[elem] for elem in list]


"""
list :array of string 

translate list of string to int with base64

return array of int
"""


def exercie9_bis(list):
    return [base64.index(elem) for elem in list]


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
list : string

translate string to list with all values in the string

return array of string
"""


def exercice10_bis(value):
    return [char for char in value]


"""
value :  string

add "=" while value is not multiple of 4

return string
"""


def exercie11(value):
    while len(value) % 4 != 0:
        value = value+"="
    return value


"""
value :  string

remove all "==" added

return string
"""


def exercice11_bis(value):
    return value.replace("=", "")
