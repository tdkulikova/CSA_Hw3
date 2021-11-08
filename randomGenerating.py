from extender import *
from rectangle import Rectangle
from triangle import Triangle


def RandomGenerating(container):
    arrayLen = randrange(10000)
    for i in range(arrayLen):
        # Generating the key of the figure.
        key = randrange(3) + 1
        # Generating the key of the color.
        colorKey = randrange(7) + 1
        if key == 1:
            shape = Rectangle()
            shape.ColorInput(colorKey)
            # Generating the rectangle.
            shape.RandomGenerating()
        elif key == 2:
            shape = Triangle()
            shape.ColorInput(colorKey)
            # Generating the triangle.
            shape.RandomGenerating()
        elif key == 3:
            shape = Circle()
            shape.ColorInput(colorKey)
            # Generating the circle.
            shape.RandomGenerating()
        else:
            return arrayLen
        container.store.append(shape)
    return arrayLen
