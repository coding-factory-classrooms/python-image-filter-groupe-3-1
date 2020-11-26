import os
from function.color_function import colorFunction
from function.filter_function import filterFunction
from function.createimg_function import createImgFunction
newImage = []


def selectionFunction(redirectory, output, finalFilter, finalParamFilter):
    lastImage = []
    if os.path.exists(redirectory):
        redirectoryValide = True

    else:
        redirectoryValide = False


    if redirectoryValide:
        for resultatFile in os.listdir(output):
            if resultatFile.endswith('.jpg'):
                lastImage.insert(0, resultatFile)
                lastImage=sorted(lastImage)
    else:
        print(f"{colorFunction.HEADER}IMAGE FILTER GROUP 3.")
        print(f"{colorFunction.WARNING}Votre redirection est invalide.")

    filterFunction(lastImage, finalFilter, finalParamFilter, redirectory, output)

def displayAllFilter():
    print(f'{colorFunction.OKBLUE}Voici la liste des filtres :\n')
    print(f'{colorFunction.FAIL}grey')
    print(f'{colorFunction.FAIL}grayscale')
    print(f'{colorFunction.FAIL}dilate')
