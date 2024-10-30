#!/usr/bin/python3
"""Define a class square
(with methods and instance attributes).
"""


class Square:
    """Defines a square by size and position."""
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, s):
        if not isinstance(s, int):
            raise TypeError("size must be an integer")
        if s < 0:
            raise ValueError("size must be >= 0")
        self.__size = s

    @property
    def position(self):
        """Retrieves the instances's position."""
        return self.__position

    @position.setter
    def position(self, pos):
        """Sets an instances's position."""
        if not (isinstance(pos, tuple) and len(pos) == 2
                and all(isinstance(i, int) and i >= 0 for i in pos)):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = pos

    def area(self):
        """returns the current square area."""
        return self.__size ** 2

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
                for i in range(self.__size):
                    print("#", end="")
                print()
