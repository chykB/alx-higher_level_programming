#!/usr/bin/python3


"""This module defines a LockedClass"""


class LockedClass:
   """prevents the user from dynamically creating new instance attributes"""


    __slots__ = ["first_name"]
