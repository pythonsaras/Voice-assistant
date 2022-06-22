import cv2
import numpy as np
from takecmd import *

def image2cartoon():
    Speak("Give the path of image")
    path=input("Give the path of image")
    img=cv2.imread(path)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    gray=cv2.medianBlur(gray,5)
    edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
    color=cv2.bilateralFilter(img,9,250,250)
    cartoon=cv2.bitwise_and(color,color,mask=edges)
    cv2.imshow("Image",cartoon)
    cv2.waitKey(0)
    Speak("image convert in cartoon Successful ")
    cv2.destroyAllWindows()



