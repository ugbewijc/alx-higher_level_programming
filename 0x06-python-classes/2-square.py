#!/usr/bin/python3

"""
"""

class Square:
    """
        A Square class

        Arg:
            size: size of the square, it must be number

        Return: void

    """

    def __init__(self,size=0):
        """ Iniitialize data """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
