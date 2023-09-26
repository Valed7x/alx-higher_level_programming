#!/usr/bin/python3

"""Square classes."""


class Square:
    """data defineing."""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
    """Getters."""
    @property
    def size(self):
        return self.__size

    """Setter."""
    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    """Returns the area of the current squares."""
    def area(self):
        return self.__size * self.__size

    """Prints the squares. """
    def my_print(self):
        if self.size == 0:
            print()
            return
        for i in range(self.size):
            print("#" * self.size)
