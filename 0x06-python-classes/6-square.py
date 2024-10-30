#!/usr/bin/python3
"""Define a class square
(with methods and instance attributes).
"""
class Square:
    """Defines a square by size and position."""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, s):
        if not isinstance(s, int):
            raise TypeError('size must be an integer')
        if s < 0:
            raise ValueError('size must be >= 0')
        self.__size = s

    @property
    def position(self):
        """Retrieves the instances's position."""
        return self.__position

    @position.setter
    def position(self, pos):
        """Sets an instances's position."""
        if (
                isinstance(pos, tuple) and len(pos) == 2
                and all(isinstance(i, int) and i > 0 for i in pos)
            ):
            self.__position = pos
        else:
            raise TypeError('position must be a tuple of 2 positive integers')
