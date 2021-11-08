# ----------------------------------------------
class Container:

    # Container constructor.

    def __init__(self):
        self.store = []

    # Printing information about container.

    def Print(self):
        print("Container is store", len(self.store), "shapes:")
        for shape in self.store:
            shape.Print()
        pass

    # Writing information about container to the file.

    def Write(self, ostream):
        ostream.write("Container is store {} shapes:\n".format(len(self.store)))
        for shape in self.store:
            shape.Write(ostream)
            ostream.write("\n")
        pass

    # Searching for the place to insert the element.

    def binarySearch(self, fig, left, right):
        if right <= left:
            if fig.Square() < self.store[left].Square():
               return left + 1
            else:
               return left
        middle = int((left + right) / 2)
        if fig.Square() == self.store[middle].Square():
               return middle + 1
        if fig.Square() < self.store[middle].Square():
               return self.binarySearch(fig, middle + 1, right)

        return self.binarySearch(fig, left, middle - 1)

    # Sorting the container.

    def binarySort(self, size):
        for i in range(1, size):
            rightBound = i-1
            selectedFigure = self.store[i]
            position = self.binarySearch(selectedFigure, 0, rightBound)
            while rightBound >= position:
                self.store[rightBound+1] = self.store[rightBound]
                rightBound = rightBound - 1
            self.store[rightBound+1] = selectedFigure



