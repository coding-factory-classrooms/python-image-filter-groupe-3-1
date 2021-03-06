import os
from function.color_function import colorFunction
from function.filter_function import filterFunction

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
                lastImage = sorted(lastImage)
    else:
        print(f"{colorFunction.HEADER}IMAGE FILTER GROUP 3.")
        print(f"{colorFunction.WARNING}Votre redirection est invalide.")

    filterFunction(lastImage, finalFilter, finalParamFilter, output)


def displayAllFilter():
    print(f'{colorFunction.OKBLUE}Voici la liste des filtres :')
    print(f'{colorFunction.FAIL}grey')
    print(f'{colorFunction.FAIL}blur:x')
    print(f'{colorFunction.FAIL}dilate:x')
