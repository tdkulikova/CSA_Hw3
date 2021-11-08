# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import sys
import time
import string

from extender import *

# ----------------------------------------------
from randomGenerating import RandomGenerating

if __name__ == '__main__':
    start_time = time.time()
    if len(sys.argv) == 3:
        inputFileName = sys.argv[1]
        outputFileName = sys.argv[2]
    elif len(sys.argv) == 2:
        inputFileName = sys.argv[1]
        outputFileName = "output.txt"
    elif len(sys.argv) == 1:
        print("Incorrect command line! You must write: python main <inputFileName> [<outputFileName>]")
        exit()
    print("Choose the way of data input:\n1 - from file\n2 - random input")
    commandNumber = input()

    if commandNumber == '1':
        # Reading the file.
        ifile = open(inputFileName)
        str = ifile.read()
        ifile.close()
        # Checking the string and deleting all whitespaces and '\n'.
        if str != "":
            strArray = str.replace("\n", " ").split(" ")
        else:
            print("Container contains 0 shapes")
            ofile = open(outputFileName, 'w')
            ofile.write("Container contains 0 shapes")
            ofile.close()
            exit(0)

    print('==> Start')
    container = Container()
    if commandNumber == '1':
        figNum = ReadStrArray(container, strArray)
    else:
        figNum = RandomGenerating(container)
    container.Print()
    ofile = open(outputFileName, 'w')
    container.Write(ofile)
    container.binarySort(figNum)
    ofile.write("\nSorted container:\n")
    container.Write(ofile)
    ofile.close()
    print("\nSorted container:")
    container.Print()

    print('==> Finish')
    print("{:g} s".format(time.time() - start_time))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
