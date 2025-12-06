#!/usr/bin/python3
"""
This module provides a function that prints text with specific indentation.
"""


def text_indentation(text):
    """
    Print text with two new lines after each '.', '?' and ':'.

    Args:
        text: The input string.

    Raises:
        TypeError: If text is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separators = ".?:"
    buffer = ""

    for char in text:
        buffer += char
        if char in separators:
            print(buffer.strip())
            print()
            buffer = ""

    # Print remaining text if not empty
    if buffer.strip():
        print(buffer.strip(), end="")

