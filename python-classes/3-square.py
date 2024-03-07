#!/usr/bin/python3

"""This is a class that defines the square"""


class Square:
        """Another square"""

        def __init__(self, size=0):
            """A new sqaure now"""

            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")

            self.__size = size

        def area(self):
            """Returns the current square area"""
            return (self.__size*self.__size)
