import math
from random import Random, randrange

from shape import *


# ----------------------------------------------
class Circle(Shape):

    # Circle constructor.

    def __init__(self):
        self.center_x = 0
        self.center_y = 0
        self.radius = 0

    # Reading parameters from file.

    def ReadStrArray(self, strArray, i):

        # There must be no less than three parameters in the array.

        if i >= len(strArray) - 2:
            return 0
        self.center_x = int(strArray[i])
        self.center_y = int(strArray[i + 1])
        self.radius = int(strArray[i + 2])
        i += 3
        return i

    # Generating random parameters.

    def RandomGenerating(self):
        self.center_x = randrange(1000)
        self.center_y = randrange(1000)
        self.radius = randrange(1000)

    # Printing information about circle.

    def Print(self):
        print("Circle: center coordinates - x =", self.center_x, "y =", self.center_y, "Radius =", self.radius,
              "Square = ", self.Square(), ", Color = ", self.color)

        pass

    # Writing information to the file.

    def Write(self, ostream):
        if self.radius > 0:
            ostream.write(
                "Circle: center coordinates - x = {}, y = {} Radius = {} Square = {} Color = {} ".format(self.center_x,
                                                                                                         self.center_y,
                                                                                                         self.radius,
                                                                                                         self.Square(),
                                                                                                         self.color))
        else:
            ostream.write("Something wrong with rectangle coordinates! Square = 0")
        pass

    # Counting the square.

    def Square(self):
        return math.pi * self.radius * self.radius
        pass
