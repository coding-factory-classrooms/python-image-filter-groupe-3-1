import os
import cv2

def img_filter (redirectory):
    if not os.path.exists('/Users/sco/Desktop/TRAVAIL/imageFilter/output'):
        os.mkdir('/Users/sco/Desktop/TRAVAIL/imageFilter/output')

    lastImage = cv2.imread('imgs/image1.jpg')
    newImage = cv2.cvtColor(lastImage, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('imgs/imageGrey.jpg', newImage)





img_filter('/Users/sco/Desktop/TRAVAIL/imageFilter/imgs/image1.jpg')