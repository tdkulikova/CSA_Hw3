from random import Random, randrange

from shape import *


# ----------------------------------------------
class Rectangle(Shape):
    def __init__(self):
        self.left_up_x = 0
        self.left_up_y = 0
        self.right_down_x = 0
        self.right_down_y = 0

    # Function for reading information from file.

    def ReadStrArray(self, strArray, i):
        # There must be at least four values in array.
        if i >= len(strArray) - 3:
            return 0
        self.left_up_x = int(strArray[i])
        self.left_up_y = int(strArray[i + 1])
        self.right_down_x = int(strArray[i + 2])
        self.right_down_y = int(strArray[i + 3])
        i += 4
        return i

    # Function for random generating parameters.

    def RandomGenerating(self):
        self.left_up_x = randrange(1000)
        self.left_up_y = randrange(1000)
        self.right_down_x = randrange(1000)
        self.right_down_y = randrange(1000)

    # Function for printing information about the shape.

    def Print(self):
        if self.right_down_x != self.left_up_x and self.right_down_y != self.left_up_y:
            print("Rectangle: A = ", abs(self.left_up_y - self.right_down_y), " B = ",
                  abs(self.left_up_x - self.right_down_x), ", Square = ", self.Square(), ", Color = ", self.color)
        else:
            print("Something wrong with rectangle coordinates! Square = 0")
        pass

    # Function for writing information to the file.

    def Write(self, ostream):
        if self.right_down_x != self.left_up_x and self.right_down_y != self.left_up_y:
            ostream.write("Rectangle: x = {}  y = {}, Square = {}, Color = {}".format(abs(self.left_up_y - self.right_down_y),
                                                                          abs(self.left_up_x - self.right_down_x),
                                                                          self.Square(), self.color))
        else:
            ostream.write("Something wrong with rectangle coordinates! Square = 0")
        pass

    # Function for counting the square.

    def Square(self):
        return abs(self.left_up_y - self.right_down_y) * abs(self.right_down_x - self.left_up_x)
        pass
