#!/usr/bin/python3
"""
This module contains a function that prints a text with 2 new lines after
each of these characters ., ?, :
"""
def text_indentation(text):
    """
    Prints a text with 2 lines after each of these characters: ., ? and :

    :param text: The input text (must be a string)
    :type text: str

    :raises TypeError: If the input text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for character in text:
        if character in ['.', '?', ':']:
            print(character, end="")
        else:
            print(character, end="")
