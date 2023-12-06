#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_integers = {}
    for element in my_list:
        unique_integers[element] = True
    result = sum(unique_integers.keys())
    return result
