#!/usr/bin/python3
"""Module that provides a function to write text to a file."""


def write_file(filename="", text=""):
    """Write a string to a text file (UTF-8)
    and return the number of characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
