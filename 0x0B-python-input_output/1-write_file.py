#!/usr/bin/python3
""" writes a string to a text file"""

def write_file(filename="", text=""):
    """ the name of the text file to be written"""
     with open(filename, 'w', encoding='utf-8') as f:
        chars_written = f.write(text)
        return chars_written
