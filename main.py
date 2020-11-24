<<<<<<< HEAD
import os
import cv2

def img_filter (redirectory):
    if not os.path.exists('/Users/sco/Desktop/TRAVAIL/imageFilter/output'):
        os.mkdir('/Users/sco/Desktop/TRAVAIL/imageFilter/output')

    lastImage = cv2.imread('imgs/image1.jpg')
    newImage = cv2.cvtColor(lastImage, cv2.COLOR_BGR2GRAY)
    cv2.imwrite('imgs/imageGrey.jpg', newImage)





img_filter('/Users/sco/Desktop/TRAVAIL/imageFilter/imgs/image1.jpg')
=======
import os
import cv2

def img_filter (redirectory):
    if not os.path.exists('C:/Users/admin/Documents/repository git hub/image_filter/python-image-filter-groupe-3-1/output'):
        os.mkdir('C:/Users/admin/Documents/repository git hub/image_filter/python-image-filter-groupe-3-1/output')

    input = open(redirectory, 'r')
    output =open('output/image1.jpg','w')

    image = cv2.imread('imgs/image1.jpg')
    grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    cv2.imshow('image grise',grey)
    cv2.imwrite('output',grey,None)

    input.close()
    output.close()

img_filter('C:/Users/admin/Documents/repository git hub/image_filter/python-image-filter-groupe-3-1/imgs/image1.jpg')

>>>>>>> master
