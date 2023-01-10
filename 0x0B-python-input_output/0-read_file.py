#!/usr/bin/python3
"""Defines a read text function"""


def read_file(filename=""):
    """Prints content of a UTF8 text file to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
