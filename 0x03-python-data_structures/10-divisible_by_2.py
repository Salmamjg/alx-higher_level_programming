#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible_by_2_list = []

    for x in my_list:
        y = x % 2 == 0
        divisible_by_2_list.append(y)

    return divisible_by_2_list
