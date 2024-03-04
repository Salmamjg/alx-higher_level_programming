#!/usr/bin/python3

def is_kind_of_class(obj, a_class):
    """
    Check if the object is an instance of, or if the object is an instance of
    a class that inherited from, the speficied class.
    
    Parameters
        - obj (any): The object to check.
        a_class (_type_): The class to check if obj is an instance of or inherited from.
    
    Returns:
        bool: True if obj is an instance of a_class or its subclass, False otherwise. 
    """
    return isinstance(obj, a_class)