import os
import cv2
from function.filter_function import filterFunction
lastImage = []

def selectionFunction(redirectory, filter, userTakeDirectory):
    global lastImage
    if not os.path.exists('output'):
        os.mkdir('output')

    if userTakeDirectory:
        for loopNumber in range(0, 4):
            loopNumber += 1
            lastImage.insert(loopNumber, f"image{loopNumber}")
    else:
        lastImage = cv2.imread(redirectory + "/image1.jpg")

    filterFunction(filter, lastImage, userTakeDirectory, redirectory)



