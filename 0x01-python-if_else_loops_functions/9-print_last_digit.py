#!/usr/bin/python3

def print_last_digit(number):
    number = abs(number)
    print("".join(str(digit) for digit in str(number)))
    