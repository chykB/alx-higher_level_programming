#!/usr/bin/python3
"""function that returns True if the object is an instance"""

def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance of a class that inherited from,
    the specified class; otherwise False.

    :param obj: Object to be checked
    :param a_class: Class to compare against
    :return: True if the object is an instance of, or if the object is an instance of a class that inherited from,     
         the specified class; otherwise False
    """
    if isinstance(obj, a_class):
        return True
    return False
