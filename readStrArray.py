from circle import Circle
from extender import *
from rectangle import Rectangle
from triangle import Triangle


def ReadStrArray(container, strArray):
    try:
        arrayLen = len(strArray)
        # Index of the current element in the string.
        i = 0
        figNum = 0
        while i < arrayLen:
            str = strArray[i]
            # Converting to int.
            key = int(str)
            # The shape key.
            if key == 1:
                i += 1
                shape = Rectangle()
                shape.ColorInput(int(strArray[i]))
                i += 1
                # Reading the rectangle, remembering the position in the array.
                i = shape.ReadStrArray(strArray, i)
            elif key == 2:
                i += 1
                shape = Triangle()
                shape.ColorInput(int(strArray[i]))
                i += 1
                # Reading the triangle, remembering the position in the array.
                i = shape.ReadStrArray(strArray, i)
            elif key == 3:
                i += 1
                shape = Circle()
                shape.ColorInput(int(strArray[i]))
                i += 1
                # Reading the circle, remembering the position in the array.
                i = shape.ReadStrArray(strArray, i)
            else:
                # If something is wrong, return the number of shapes.
                return figNum
            if i == 0:
                return figNum
            figNum += 1
            # Adding to the container.
            container.store.append(shape)
            return figNum
    except:
        print("Incorrect format of input data in the file")
        exit(0)

