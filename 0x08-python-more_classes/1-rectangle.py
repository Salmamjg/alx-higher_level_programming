#!/usr/bin/python3
"""Defines a class Rectangle that defines a rectangle"""


class Rectangle:
    """A class representing a rectangle."""
    def __init__(self, width=0, height=0):
        """Initialize a new instance of the class.

        Parameters:
        - width (int): The width of the rectangle. Default is 0.
        - height (int): The height of the rectangle. Default is 0.

        Raises:
        - TypeError: If width or height is not an integer.
        - ValueError: If width or height is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """"Set or change the width of the rectangle.

        Parameters:
        - value (int): The new width value.

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set or change the height of the rectangle.

        Parameters:
        - value (int): The new height value.

        Raises:
        - TypeError: If value is not integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value