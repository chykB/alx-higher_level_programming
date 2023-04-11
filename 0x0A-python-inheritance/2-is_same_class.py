#!/usr/bin/python3
"""function that returns True if the object is exactly an instance of the specified class"""

def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class; otherwise False.
    parameter obj: Object to be checked
    parameter a_class: true is object is exactly the same
    """
    if type(obj) == a_class:
	return True
    else:
	return False
