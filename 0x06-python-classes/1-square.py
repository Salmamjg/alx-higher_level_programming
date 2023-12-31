#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """
    Represents a square.

    Attributes:
         __size (int):representing the size of the square.

    Methods:
         __init__(self, size): Initializes with a given size.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
