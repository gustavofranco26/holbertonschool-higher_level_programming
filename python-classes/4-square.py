#!/usr/bin/python3
"""Created an empty class with named Square"""


class Square:
    """A class Square name"""
    def __init__(self, size=0):
        """size (int): size for __size attribute of class instance"""
        self.__size = size

    def area(self):
        """Calculate and return the current square area"""
        return self.__size * self.__size

    @property
    def size(self):
        """Gets the size of the class instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size o the class instance"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
