#!/usr/bin/python3

"""Defines a file writing function."""


def write_file(filename="", text=""):
    """writes a string to a text file (UTF8)
    Returns: returns the number of characters written
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
