#!/usr/bin/python3

"""Define a class square"""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
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
        try:
            self.__position = position
            if type(position) is not tuple:
                raise TypeError
            if len(position) != 2:
                raise TypeError
            if position[0] < 0 or position[1] < 0:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")

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
        try:
            self.__size = value
            if value < 0:
                raise ValueError
            if type(value) is not int:
                raise TypeError
        except TypeError:
            raise TypeError("size must be an integer")
        except ValueError:
            raise ValueError("size must be >= 0")

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__postion

    @position.setter
    def position(self, value):
        """Set or change the position of the square.

        Parameters:
        - value (tuple): The new position value.

        Raises:
        - TypeError: If value is not a tuple of 2 positive integers.
        - ValueError: If position contains non-positive integers.
        """
        try:
            self.__position = value
            if type(value) is not tuple:
                raise TypeError
            if len(value) != 2:
                raise TypeError
            if value[0] < 0 or value[1] < 0:
                raise TypeError
        except TypeError:
            raise TypeError("Position must be a tuple of 2 positive integers.")

    def area(self):
        """Compute the area of the square."""
        return self.__size ** 2

    def my_print(self):
        """Print the square using # characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                for _ in range(self.__position[0]):
                    print(" ",end= '')
                for _ in range(self.__size):
                    print("#", end= '')
                print()
