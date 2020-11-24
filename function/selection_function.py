import os
import cv2
from function.filter_function import filterFunction
lastImage = []

def selectionFunction(redirectory, filter, userTakeDirectory):
    global lastImage
    if not os.path.exists('output'):
        os.mkdir('output')

    if userTakeDirectory:
        for resultatFile in os.listdir(redirectory):
            if resultatFile.endswith('.jpg'):
                print(resultatFile)
                lastImage.insert(0, resultatFile)

    else:
       lastImage.insert(0, f"image1")

    filterFunction(filter, lastImage, userTakeDirectory, redirectory)



