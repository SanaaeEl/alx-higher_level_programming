#!/usr/bin/python3
"""Define a class square
(with methods and instance attributes).
"""
class Square:
    """Defines a square by size and position."""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position
