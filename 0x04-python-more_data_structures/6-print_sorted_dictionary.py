#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if a_dictionary is None:
        print("The dictionary is empty or None.")
        return
    for key in sorted(a_dictionary):
        print("{}: {}".format(key, a_dictionary[key]))
