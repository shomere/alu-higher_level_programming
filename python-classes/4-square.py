#!/usr/bin/python3
"""Define a square"""


class Square:
    """Represents a square with a private instance attribute: size"""

    def __init__(self, size=0):
        """Initializes the square with a private size attribute"""
        self.size = size  # Calls the setter to apply validation

    @property
    def size(self):
        """Retrieves the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square with type and value checks"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculates and returns the current square area"""
        return self.__size ** 2

