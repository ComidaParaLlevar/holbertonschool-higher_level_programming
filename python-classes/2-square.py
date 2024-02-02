#!/usr/bin/python3
"""This module defines a square object"""


class Square:
    """class Square contains method defining attribute size"""
    def __init__(self, size):
        """initialize method for storing attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def size_attr(self):
        return self.__size ** 2
