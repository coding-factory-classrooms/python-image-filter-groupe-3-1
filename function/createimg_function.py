import os
import cv2


def createImgFunction():
    lastImage = []

    for resultatFile in os.listdir('imgs/'):
        if resultatFile.endswith('.jpg'):
            lastImage.insert(0, resultatFile)
            lastImage = sorted(lastImage)
            for numberLoop in range(1, 5):
                cv2.imwrite(f'output/image{numberLoop}.jpg',cv2.imread(f"imgs/image{numberLoop}.jpg"))
