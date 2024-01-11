#!/usr/bin/python3
"""Defines a class Rectangle that defines a rectangle"""


class Rectangle:
    """Defines class representing a rectangle.
         Args:
        width (int): The width of the rectangle. Default is 0.
        height (int): The height of the rectangle. Default is 0.
    """

    def __init__(self, width=0, height=0):
        """Initialize a new instance of the class."""
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getter retrieve the width of the rectangle. """
        return self.__width

    @width.setter
    def width(self, value):
        """"Set or change the width of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getter retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set or change the height of the rectangle."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (2 * self.__width) + (2 * self.height)

    def __str__(self):
        """Return a string representation of the rectangle."""
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_str = ""
        for _ in range(self.__height):
            rectangle_str += '#' * self.__width + '\n'
        return rectangle_str[:-1]

    def __repr__(self):
        """Return a string representation of the rectangle for recreation."""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Print a message when an instance of Rectangle is deleted."""
        print("Bye rectangle...")
