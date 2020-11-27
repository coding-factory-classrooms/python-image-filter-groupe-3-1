import cv2
def FaceRecognition():
    sleeploop=0
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = cv2.imread('imgs/imageFace.PNG')
    nameDev = ["Clement","Yann","Robin","Chris"]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    for (x, y, w, h) in faces:
        #cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(img, nameDev[sleeploop], (x-10,y+20), cv2.FONT_HERSHEY_SIMPLEX ,1, (0,0,80), 2)
        sleeploop+=1
    cv2.imshow('img', img)
    cv2.waitKey()
