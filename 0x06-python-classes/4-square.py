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
        self.size = size

    @property
    def size(self):
        """Retirieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set or change the size of the square.

        Parameters:
        - value (int): The new size value.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Size must be an integer.")
        elif value < 0:
            raise ValueError("size myst be an integer")
        else:
            self.__size = value

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2
