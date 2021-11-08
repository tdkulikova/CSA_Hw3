import math
from random import Random, randrange

from shape import *


# ----------------------------------------------
class Triangle(Shape):
    # Function for reading information from file.
    def __init__(self):
        self.ax = 0
        self.ay = 0
        self.bx = 0
        self.by = 0
        self.cx = 0
        self.cy = 0
        self.a = 0
        self.b = 0
        self.c = 0

    # Function for reading information from file.

    def ReadStrArray(self, strArray, i):
        # должно быт как минимум три непрочитанных значения в массиве
        if i >= len(strArray) - 5:
            return 0
        self.ax = int(strArray[i])
        self.ay = int(strArray[i + 1])
        self.bx = int(strArray[i + 2])
        self.by = int(strArray[i + 3])
        self.cx = int(strArray[i + 4])
        self.cy = int(strArray[i + 5])
        self.SidesCalculating()
        i += 6
        return i

    # Function for random generating parameters.

    def RandomGenerating(self):
        self.ax = randrange(1000)
        self.ay = randrange(1000)
        self.bx = randrange(1000)
        self.by = randrange(1000)
        self.cx = randrange(1000)
        self.cy = randrange(1000)
        self.SidesCalculating()

    def SidesCalculating(self):
        a = math.sqrt(pow(self.bx - self.ax, 2) + pow(self.by - self.ay, 2))
        b = math.sqrt(pow(self.cx - self.bx, 2) + pow(self.cy - self.by, 2))
        c = math.sqrt(pow(self.cx - self.ax, 2) + pow(self.cy - self.ay, 2))
        self.a = a
        self.b = b
        self.c = c

    # Function for printing information about the shape.

    def Print(self):
        if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b:
            print("Triangle: a = ", self.a, " b = ", self.b, "c = ", self.c, ", Square = ", self.Square(), ", Color = ", self.color)
        else:
            print("Something wrong with Triangle coordinates! Square = 0")
        pass

    # Function for writing information to the file.

    def Write(self, ostream):
        if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b:
            ostream.write("Triangle: a = {}  b = {}  c = {}, Square = {}, Color = {}".format(self.a, self.b, self.c, self.Square(), self.color))
        else:
            ostream.write("Something wrong with Triangle coordinates! Square = 0")
        pass
    
    # Function for counting the square.

    def Square(self):
        if self.a < self.b + self.c and self.b < self.a + self.c and self.c < self.a + self.b:
            return 0.5 * abs(
                self.ax * (self.by - self.cy) + self.bx * (self.cy - self.ay) + self.cx * (self.ay - self.by))
        else:
            return 0.0
        pass
