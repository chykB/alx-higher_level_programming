#!/usr/bin/python3
# 101-locked_class.py

"""This module defines a LockedClass"""


class LockedClass:
    """
    prevents the user from dynamically creating new instance attributes
    """

    __slots__ = ["first_name"]
