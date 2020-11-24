import os
import cv2
import numpy as np


def imageTransform(redirectory, filter):
    if not os.path.exists('output'):
        os.mkdir('output')

    lastImage = cv2.imread(redirectory)

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
    else:
        print("Vous n'avez pas choisis un filtre disponible")

    cv2.imwrite(f'output/{imageFilter}.jpg', newImage)




imageTransform('imgs/image1.jpg', 'dilate')
