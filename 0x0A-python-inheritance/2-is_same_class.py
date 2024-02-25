#!/usr/bin/python3
"""Defines a class-checking function"""


def is_same_class(obj, a_class):
    """Check if the object is exactly an instance of the specified class

        Parameters:
            - obj (any): The object to check.
            - a_class (Type): The class to match the type of obj to.
        Returns:
            bool: True if obj is exactly an instance of a_class,
            False otherwise.
    """
    if type(obj) == a_class:

        return True
    return False
