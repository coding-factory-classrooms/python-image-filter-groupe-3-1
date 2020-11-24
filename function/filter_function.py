import os
import cv2
import numpy as np


def filterFunction(filter, lastImage, userTakeDirectory, redirectory):
    if userTakeDirectory:
        if filter == 'grey':
            for loopNumber in range(1,4):

                img = cv2.imread(f"{redirectory}/{lastImage[loopNumber]}.jpg")

                newImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                imageFilter = f"greyImage{loopNumber}"
                cv2.imwrite(f'output/{imageFilter}.jpg', newImage)

                loopNumber += 1
    else:
        if filter == 'grey':
            newImage = cv2.cvtColor(lastImage, cv2.COLOR_BGR2GRAY)
            imageFilter = "greyImage"
        elif filter == 'blur':
            sizeImage = (10, 10)
            newImage = cv2.blur(lastImage, sizeImage)
            imageFilter = "blurImage"
        elif filter == 'dilate':
            kernel = np.ones((5, 5), np.uint8)
            newImage = cv2.dilate(lastImage, kernel, iterations=3)
            imageFilter = "dilateImage"
        try:
            cv2.imwrite(f'output/{imageFilter}.jpg', newImage)
        except UnboundLocalError as filterError:
            print(f"Voici votre erreur : {filterError}")