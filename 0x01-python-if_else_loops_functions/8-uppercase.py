#!/usr/bin/env python3
def uppercase(str):
    
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            to_uppercase = chr(ord(char) - ord('a') + ord('A'))
            print("{}".format(to_uppercase), end='')
        else:
            print("{}".format(char), end='')
print()
