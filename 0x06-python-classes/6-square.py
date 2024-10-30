#!/usr/bin/python3
"""Define a class square
(with methods and instance attributes).
    Attributes:
            size (int): size of the square.
            position (tuple): position of the square.
"""
class Square:
    """Defines a square by size and position."""
    def __init__(self, size=0, position=(0, 0)):
         """Initializes Square instances.
        """
        self.__size = size
        self.__position = position
