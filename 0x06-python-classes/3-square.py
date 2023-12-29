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
        try:
            self.__size = size
            if size < 0:
                raise ValueError
            if type(size) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2
