<<<<<<< Updated upstream
from function.selection_function import selectionFunction
from function.log_function import dump_log

selectionFunction('imgs/', 'blur', True)
dump_log()
=======
import os
import cv2
import numpy as np


def img_filter (redirectory,filter):
    if not os.path.exists('output'):
        os.mkdir('output')

    lastImage = cv2.imread('imgs/image1.jpg')

    if filter=='grey':
        newImage = cv2.cvtColor(lastImage, cv2.COLOR_BGR2GRAY)
        image_filter='grey'
        print("Votre image grise est en train d'etre creer")
    elif filter=='blur':
        sizeImage=(10,10)
        newImage = cv2.blur(lastImage,sizeImage)
        image_filter='blur'
        print("Votre image flou est en train d'etre creer")

    elif filter=='dilatation':
        kernel = np.ones((5, 5), np.uint8)
        newImage = cv2.dilate(lastImage,kernel)
        image_filter = 'dilatation'
        print("Votre image dilater est en train d'etre creer")

    else:
        print("Vous n'avez pas choisis un filtre disponible.")

    try:
        cv2.imwrite(f'output/{image_filter}.jpg',newImage)
    except UnboundLocalError as e:
        print(f'Votre erreur : "{e}" . ')





img_filter('imgs/image1.jpg','dilatation')
>>>>>>> Stashed changes
