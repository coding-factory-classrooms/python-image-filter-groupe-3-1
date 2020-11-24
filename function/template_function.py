import cv2
import numpy as np
from function.log_function import logFunction
sizeImage = (10, 10)
kernel = np.ones((5, 5), np.uint8)

def templateFunctionMulti(redirectory, lastImage, filter):
    for loopNumber in range(1, len(lastImage)):
        if filter == "grey":
            filterName = "grey"
            optionName = cv2.cvtColor(cv2.imread(f"{redirectory}{lastImage[loopNumber]}"), cv2.COLOR_BGR2GRAY)
        elif filter == "blur":
            filterName = "blur"
            optionName = cv2.blur(cv2.imread(f"{redirectory}{lastImage[loopNumber]}"), sizeImage)
        elif filter == "dilate":
            filterName = "dilate"
            optionName = cv2.dilate(cv2.imread(f"{redirectory}{lastImage[loopNumber]}"), kernel, iterations=3)
        newImage = optionName
        imageFilter = f"{filterName}{lastImage[loopNumber]}"
        cv2.imwrite(f'output/{imageFilter}', newImage)
        logFunction(f"Création de l'image {lastImage[loopNumber]} avec le filtre : {filter}. Voici la redirection de l'image (output/{imageFilter}.jpg)")

        loopNumber += 1

def templateFunctionSimple(redirectory,lastImage, filter):
    img = cv2.imread(f"{redirectory}{lastImage[0]}")
    if filter == "grey":
        filterName = "grey"
        optionName = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif filter == "blur":
        filterName = "blur"
        optionName = cv2.blur(img, sizeImage)
    elif filter == "dilate":
        filterName = "dilate"
        optionName = cv2.dilate(img, kernel, iterations=3)
    newImage = optionName
    imageFilter = f"{filterName}Image.jpg"
    logFunction(f"Création de l'image {lastImage[0]} avec le filtre : {filter}. Voici la redirection de l'image (output/{imageFilter}.jpg)")

    cv2.imwrite(f'output/{imageFilter}', newImage)