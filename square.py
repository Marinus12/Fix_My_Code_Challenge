#!/usr/bin/python3


class Square():
    """A class representing a square."""
    
    def __init__(self, *args, **kwargs):
        """Initialize a square."""
        if len(args) > 0:
            raise TypeError("Square takes 0 positional argument but "
                            "{} were given".format(len(args)))
        for key, value in kwargs.items():
            setattr(self, key, value)

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    def perimeter_of_my_square(self):
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":

    s = Square(width=12, height=9)
    print(s)
    print("Area:", s.area_of_my_square())
    print("Perimeter:", s.permiter_of_my_square())
