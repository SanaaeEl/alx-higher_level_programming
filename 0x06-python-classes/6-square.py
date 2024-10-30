#!/usr/bin/python3
"""Define a class square
(with methods and instance attributes).
"""


class Square:
    """ Class that defines a square by size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initializes Square instances.
        Args:
            size (int): size of the square.
            position (tuple): position of the square."""
        self.__size = size
        self.__position = position

    def area(self):
        """returns the current square area."""
        return self.__size ** 2

    @property
    def size(self):
        """Retrieves an instances's size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setts an instances's size."""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        """Retrieves an instances's position."""
        return self.__position

    @position.setter
    def position(self, pos):
        """Setts an instances's position."""
        if isinstance(pos, tuple) and len(pos) == 2
        and all(isinstance(i, int) and i > 0 for i in pos):
            self.__position = pos
        else:
            raise TypeError('position must be a tuple of 2 positive integers')

    def my_print(self):
        """Prints the square with the character #."""
        if self.__size == 0:
            print()
        else:
            for a in range(self.__position[1]):
                print("")
            for a in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for b in range(self.__size):
                    print("#", end="")
                print()
