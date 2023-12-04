#!/usr/bin/python3
def no_c(my_string):
    string2 = ''.join(character for character in my_string
                     if character.lower() not in {'c', 'C'})
    return string2
