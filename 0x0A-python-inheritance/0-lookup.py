#!/usr/bin/env python
"""
Contains the lookup function
"""
def lookup(obj):
    attributes_and_methods = dir(obj)
    filtered_attributes_and_methods = [item for item in attributes_and_methods if not item.startswith('_')]

    return filtered_attributes_and_methods
