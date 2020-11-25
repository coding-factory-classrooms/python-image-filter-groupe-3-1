import os
from function.color_function import colorFunction
from function.filter_function import filterFunction

lastImage = []


def selectionFunction(redirectory, filter, userTakeDirectory):
    global lastImage
    if os.path.exists(redirectory):
        redirectoryValide = True
        if os.path.exists('output'):
            os.mkdir('output')
    else:
        redirectoryValide = False


    if userTakeDirectory and redirectoryValide:
        for resultatFile in os.listdir(redirectory):
            if resultatFile.endswith('.jpg'):
                lastImage.insert(0, resultatFile)

    elif redirectoryValide:
        lastImage.insert(0, f"image1.jpg")
    else:
        print(f"{colorFunction.HEADER}IMAGE FILTER GROUP 3.")
        print(f"{colorFunction.WARNING}Votre redirection est invalide.")

    filterFunction(filter, lastImage, userTakeDirectory, redirectory)

def displayAllFilter():
    print(f'{colorFunction.OKBLUE}Voici la liste des filtres :\n')
    print(f'{colorFunction.FAIL}grey')
    print(f'{colorFunction.FAIL}grayscale')
    print(f'{colorFunction.FAIL}dilate')
