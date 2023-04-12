#!/usr/bin/python3
"""Contain an object represented by JSON string"""


import json


def from_json_string(my_str):
    """returns a string object"""
    return json.loads(my_str)
