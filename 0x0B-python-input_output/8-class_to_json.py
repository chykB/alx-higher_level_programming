#!/usr/bin/python3
""" Creates a Python class-to-JSON function."""


def class_to_json(obj):
    """returns the dict representation of the object's instance variables"""
    return obj.__dict__
