#!/usr/bin/python3
"""Create an inherited class-checking function."""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified
    class; otherwise False.

    :param obj: Object to be checked
    :param a_class: Class to compare against
    :return: True if the object is an instance of a class that inherited (directly or indirectly) from the specified
             class; otherwise False
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
