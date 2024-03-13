#!/usr/bin/python3
""" Square class """


class Square():
    """ Square class
    Attribute:
    width (int): width of the square
    height (int): height of the square

    methods:
    area_of_my_square(self): returns the area of the square
    PermiterOfMySquare(self): returns the permiter of the square
    __str__(self): returns the string representation of the square
    """

    width = 0
    height = 0

    def __init__(self, *args, **kwargs):
        """ Constructor """
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the Square """
        return self.width * self.height

    def permiter_of_my_square(self):
        """Permiter of the Square """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """ String representation """
        return "{}/{}".format(self.width, self.height)


if __name__ == "__main__":
    """ executes when main """
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.permiter_of_my_square())
