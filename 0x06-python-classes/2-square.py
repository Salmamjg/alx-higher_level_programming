#!/usr/bin/python3

"""Define a class square"""


class Square:
    """Represent a square."""


    def __init__(self, size=0):
        """Initialize a new instance of the class.

        Parameters:
        - size (int): The size of the square. Default is 0.

        Raises:
        - TypeError: If size is not an integer.
        - ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("Size must be an integer.")
        elif size < 0:
            raise ValueError("Size must be >= 0")
        else:
            self.__size = size
