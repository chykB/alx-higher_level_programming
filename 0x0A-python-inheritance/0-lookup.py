#!/usr/bin/python3
"""
Object attribute function
"""

def lookup(obj):
    """
    returns the list of available attributes and methods of an object
    """
    return (dir(obj))
