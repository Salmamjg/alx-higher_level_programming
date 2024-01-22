#!/usr/bin/python3
"""
    This is a module for performing integer addition.

    This module contains a function 'add_integer(a, b=98)' that
add two numbers.
    """


def add_integer(a, b=98):
    """Add two integers or floats.

        This function adds two numbers 'a' and 'b'.
    If 'b' is not provided, it defaults to 98.
        Both 'a' and 'b' must be integers or floats,
        otherwise a TypeError is raised.
        If 'a' and 'b' are floats, they are first casted to integers.
    The function returns an integer: the addition of 'a' and 'b'.

    Parameters:
        a (int, float): The first number to add.
        b (int, float, optional): The second number to add.
    Defaults to 98.

    Returns:
        int: The sum of 'a' and 'b' as an integer.

    Raises:
        TypeError: If 'a' or 'b' is not integer or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
