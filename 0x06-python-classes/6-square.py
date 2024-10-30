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
        """Retrieves the instance's size."""
        return self.__size

    @size.setter
    def size(self, s):
        """Sets the instance's size."""
        if not isinstance(s, int):
            raise TypeError('size must be an integer')
        if s < 0:
            raise ValueError('size must be >= 0')
        self.__size = s

    @property
    def position(self):
        """Retrieves an instances's position."""
        return self.__position

    @position.setter
    def position(self, pos):
        """Setts an instances's position."""
        if isinstance(pos, tuple) and len(pos) == 2
        and all(isinstance(i, int) and i >= 0 for i in pos):
            self.__position = pos
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def area(self):
        """Returns the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for a in range(self.position[1]):
                print("")
            for a in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for b in range(self.__size):
                    print("#", end="")
                print()
