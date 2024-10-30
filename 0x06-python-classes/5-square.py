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

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """Prints the square with the character #"""
        if size == 0:
            print()
        else:
            for a in range(self.__size):
                for b in range(self.__size):
                    print("#", end="")
                print()
