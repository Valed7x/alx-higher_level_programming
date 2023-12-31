#!/usr/bin/python3

"""Define a class Squares."""


class Square:
    """Represent a squares."""

    def __init__(self, size=0):
        """Initialize a new squares.

        Args:
            size (int): The size of the new squares.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the squares."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current area of the squares."""
        return (self.__size * self.__size)
