import cv2
import numpy as np
from function.log_function import logFunction

def templateFunctionMulti(lastImage, finalFilter, finalParamFilter, redirectory, output):
    sizeImage = (int(finalParamFilter), int(finalParamFilter))
    kernel = np.ones((int(finalParamFilter), int(finalParamFilter)), np.uint8)

    for loopNumber in range(1, len(lastImage)):
        if finalFilter == "grey":
            optionName = cv2.cvtColor(cv2.imread(f"{redirectory}{lastImage[loopNumber]}"), cv2.COLOR_BGR2GRAY)
        elif finalFilter == "blur":
            optionName = cv2.blur(cv2.imread(f"{redirectory}{lastImage[loopNumber]}"), sizeImage)
        elif finalFilter == "dilate":
            optionName = cv2.dilate(cv2.imread(f"{redirectory}{lastImage[loopNumber]}"), kernel, iterations=1)

        newImage = optionName
        imageFilter = f"image{lastImage[loopNumber]}"
        cv2.imwrite(f'{output}/{imageFilter}', newImage)
        logFunction(f"Création de l'image {lastImage[loopNumber]} avec le filtre : {finalFilter}. Voici la redirection de l'image (output/{imageFilter}.jpg)")
        loopNumber += 1
