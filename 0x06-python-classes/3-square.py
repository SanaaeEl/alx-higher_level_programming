#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """ Class that defines a square by size"""

    def __init__(self, size=0):
        """Initializes Square instances"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size

    def area(self):
        """returns the current square area"""
        return self.__size ** 2
