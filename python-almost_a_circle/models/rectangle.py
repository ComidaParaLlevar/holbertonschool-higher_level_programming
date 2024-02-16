#!/usr/bin/python3
""" Module Rectangle
Inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """ Rectangle representation."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes Rectangle object

        Args:
            - __width: width
            - __height: height
            - __x: position
            - __y: position
            - id: id"""

        self.__width = width
        self.__height = height
        self.x = x
        self.y = y
        super().__init__(id)
