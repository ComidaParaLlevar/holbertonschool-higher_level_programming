#!/usr/bin/python3
""" Module Rectangle"""
from .base import Base

if __name__ != "__main__":
    class Rectangle(Base):
        """ Rectangle representation. inherits from base"""

        def __init__(self, width, height, x=0, y=0, id=None):
            """initializes Rectangle object

            Args:
                - __width: width
                - __height: height
                - __x: position
                - __y: position
                - id: id"""

            if True:
                if not isinstance(width, int):
                    raise TypeError("width must be an integer")
                if width <= 0:
                    raise ValueError("width must be > 0")
                if not isinstance(height, int):
                    raise TypeError("height must be an integer")
                if height <= 0:
                    raise ValueError("height must be > 0")
                if not isinstance(x, int):
                    raise TypeError("x must be an integer")
                if x < 0:
                    raise ValueError("x must be >= 0")
                if not isinstance(y, int):
                    raise TypeError("y must be an integer")
                if y < 0:
                    raise ValueError("y must be >= 0")

            self.__width = width
            self.__height = height
            self.__x = x
            self.__y = y
            super().__init__(id)

        @property
        def width(self):
            """Get the width of the Rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value <= 0:
                raise ValueError("width must be > 0")
            self.__width = value

        @property
        def height(self):
            """Get the height of the Rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value <= 0:
                raise ValueError("height must be > 0")
            self.__height = value

        @property
        def x(self):
            """Get the x attribute of the Rectangle."""
            return self.__x

        @x.setter
        def x(self, value):
            if not isinstance(value, int):
                raise TypeError("x must be an integer")
            if value < 0:
                raise ValueError("x must be >= 0")
            self.__x = value

        @property
        def y(self):
            """Get the y attribute of the Rectangle."""
            return self.__y

        @y.setter
        def y(self, value):
            if not isinstance(value, int):
                raise TypeError("y must be an integer")
            if value < 0:
                raise ValueError("y must be >= 0")
            self.__y = value

        def area(self):
            """ returns area of rectangle"""
            return self.__height * self.__width

        def display(self):
            """Prints the rectangle using #"""
            print("\n" * self.__y, end="")
            for i in range(self.__height):
                print(" " * self.__x, end="")
                print("#" * self.__width)

        def __str__(self):
            return f"[Rectangle] ({self.id}) {self.__x}/{self.__y}" +\
                f" - {self.__width}/{self.__height}"

        def update(self, *args, **kwargs):
            """ assigns an argument to each attribute """
            if args is not None and len(args) != 0:
                if len(args) >= 1:
                    if type(args[0]) != int and args[0] is not None:
                        raise TypeError("id must be an integer")
                    self.id = args[0]
                if len(args) > 1:
                    self.width = args[1]
                if len(args) > 2:
                    self.height = args[2]
                if len(args) > 3:
                    self.x = args[3]
                if len(args) > 4:
                    self.y = args[4]
                else:
                    for key, value in kwargs.items():
                        if key == "id":
                            if type(value) != int and value is not None:
                                raise TypeError("id must be an integer")
                            self.id = value
                        if key == "width":
                            self.width = value
                        if key == "height":
                            self.height = value
                        if key == "x":
                            self.x = value
                        if key == "y":
                            self.y = value
