#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints the string "My name is <first name> <last name>"

    :param first_name: First name as a string
    :param last_name: Last name as a string (default is an empty string)
    :raises TypeError: If first_name or last_name is not a string
    """
    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string "
                        "or last_name must be a string")
    full_name = f"My name is {first_name} {last_name}"
    print(full_name)
