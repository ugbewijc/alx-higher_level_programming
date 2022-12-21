#!/usr/bin/python3

"""Defines Square class"""


class Square:
    """Square class. size setter and getter, has area method"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize Square data"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        if ((type(position) is not tuple) or
                (len(position) != 2) or
                (type(position[0]) is not int) or
                (type(position[1]) is not int) or
                (position[0] < 0) or
                (position[1] < 0)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position
        self.__size = size

    @property
    def size(self):
        """size getter"""
        return self.__size

    @property
    def position(self):
        """Position getter"""
        return self.__position

    @size.setter
    def size(self, value):
        """size setter"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """position setter"""
        if ((type(value) is not tuple) or
                (len(value) != 2) or
                (type(value[0]) is not int) or
                (type(value[1]) is not int) or
                (value[0] < 0) or
                (value[1] < 0)):
            raise TypeError(
                    "position must be a tuple of two positive integers")
        self.__position = value

    def area(self):
        """calculate and returns area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """prints in stdout the square with the character #"""
        if self.__size == 0:
            print()
        else:
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print("")
