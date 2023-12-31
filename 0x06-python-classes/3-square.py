#!/usr/bin/python3

""" defines a square """


class Square:
    """ square with private instance attribute sizes """

    def __init__(self, size=0):
        """
        initializes squares.
        Args:
            size: size of side of squares.
        """

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """
        finds area of squares.
        Returns:
            the area of the squares.
        """

        return self.__size ** 2
