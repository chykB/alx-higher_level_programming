#!/usr/bin/python3
"""Creates a text_file"""


def read_file(filename=""):

	with open(filename, 'r', encoding='utf-8') as file:
                print(f.read(), end="")
