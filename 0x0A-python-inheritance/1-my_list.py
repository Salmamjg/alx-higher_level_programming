#!/usr/bin/python3
"""Contains the print_stored function"""


class MyList(list):
    """A class that inherits from list"""

    def print_sorted(self):
        """Prints a list sorted in ascending order."""
        print(sorted(self))
