import os
from function.filter_function import filterFunction
lastImage = []

def selectionFunction(redirectory, filter, userTakeDirectory):
    global lastImage
    if not os.path.exists('output'):
        os.mkdir('output')

    if userTakeDirectory:
        for resultatFile in os.listdir(redirectory):
            if resultatFile.endswith('.jpg'):
                lastImage.insert(0, resultatFile)

    else:
       lastImage.insert(0, f"image1.jpg")

    filterFunction(filter, lastImage, userTakeDirectory, redirectory)



