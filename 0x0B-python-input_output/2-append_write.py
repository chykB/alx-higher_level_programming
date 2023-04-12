#!/usr/bin/python3
"""appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """return the number of character appended"""

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end="")
