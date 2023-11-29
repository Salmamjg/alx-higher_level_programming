#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        if ord('a') <= ord(char) <= ord('z'):
            to_uppercase = chr(ord(char) - ord('a') + ord('A'))
            result += "{}".format(to_uppercase)
        else:
            result += "{}".format(char)

    print(result)
