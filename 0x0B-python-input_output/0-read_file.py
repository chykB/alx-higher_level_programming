#!/usr/bin/python3
"""Creates a text_file"""


def read_file(filename=""):
    """ prints its contents to stdout"""
    with open(filename, 'r', encoding='utf-8') as file:
        print(f.read(), end="")
