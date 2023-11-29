#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)
last_digit_of = number % 10  # Consider the sign of the last digit

if last_digit_of > 5:
    variable = "and is greater than 5"
elif last_digit_of == 0:
    variable = "and is 0"
elif -5 < last_digit_of < 0:
    variable = f"and is less than 6 and not 0"

print(f"Last digit of {number} is {last_digit_of} {variable}")
