#!/usr/bin/python3

"""Defines a class square"""


class Square:
    """ Class that defines a square by size (with conditions)"""

    def __init__(self, size=0):
        """Initializes Square instances"""
        if not isinstance(size, int):
            raise TypeError('size must be an intefer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
