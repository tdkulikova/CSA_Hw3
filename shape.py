# ----------------------------------------------
from enum import Enum


class Shape:
    # The color of the figure.
    class Color(Enum):
        RED = 1,
        ORANGE = 2,
        YELLOW = 3,
        GREEN = 4,
        CYAN = 5,
        BLUE = 6,
        PURPLE = 7

    def __init__(self):
        self.color = self.Color.RED

    def ReadStrArray(self, strArray, i):
        pass

    def Print(self):
        pass

    def Write(self, ostream):
        pass

    def Perimeter(self):
        pass

    # Function for converting color key to the color.

    def ColorInput(self, key):
        if key == 1:
            self.color = self.Color.RED
        if key == 2:
            self.color = self.Color.ORANGE
        if key == 3:
            self.color = self.Color.YELLOW
        if key == 4:
            self.color = self.Color.GREEN
        if key == 5:
            self.color = self.Color.CYAN
        if key == 6:
            self.color = self.Color.BLUE
        if key == 7:
            self.color = self.Color.PURPLE
        else:
            self.color = self.Color.RED


