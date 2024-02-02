#!/usr/bin/python3
"""This module defines a square object"""


class Square:
    """class Square contains method defining attribute size"""
    def __init__(self, size=0):
        """initialize method for storing attribute"""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def size_attr(self):
        return self.__size ** 2
