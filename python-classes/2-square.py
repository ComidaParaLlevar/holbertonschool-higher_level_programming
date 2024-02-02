#!/usr/bin/python3
"""This module defines a square object"""


class Square:
    """class Square contains method defining attribute size"""
    def __init__(self, size):
        """initialize method for storing attribute"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
