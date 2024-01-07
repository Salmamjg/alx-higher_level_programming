#!/usr/bin/python3
"""Defines a class Rectangle that defines a rectangle"""


class Rectangle:
    """A class representing a rectangle.
        Args:
        width (int): The width of the rectangle. Default is 0.
        height (int): The height of the rectangle. Default is 0.

    Attributes:
        __width (int): Private attribute representing the width.
        __height (int): Private attribute representing the height.

    Methods:
        __init__(self, width=0, height=0): Initializes a new instance of the class.
        width(self): Getter method for retrieving the width.
        width(self, value): Setter method for setting the width.
        height(self): Getter method for retrieving the height.
        height(self, value): Setter method for setting the height.

    Raises:
        TypeError: If width or height is not an integer.
        ValueError: If width or height is less than 0.
    """

    def __init__(self, width=0, height=0):
        """Initialize a new instance of the class."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """"Set or change the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set or change the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("Height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
