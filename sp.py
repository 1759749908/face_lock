import time
from ctypes import *

import cv2

import baiduface

capture = cv2.VideoCapture(0)
if capture.isOpened() != True:
    print("你没有打开摄像头")
    exit()
else:
    print("成功打开摄像头")
face = cv2.CascadeClassifier("haarcascade_frontalface_alt2.xml")
print("人脸模型加载成功")

u=0
time.sleep(1)
while True:
    ret, frame = capture.read()
    cv2.imwrite("image.jpg",frame)
    faces = face.detectMultiScale(frame)
    time.sleep(2)
    if faces != ():
        if baiduface.faceimage("image.jpg","IMG.jpg") != 1:
            u = u + 1
            if (capture.isOpened() == True) & (u>=10):
                windll.LoadLibrary('user32.dll').LockWorkStation()
                #print("ok")
            elif (capture.isOpened() != True):
                u=0
        else:
            u=0

    else:
            u += 1
    print(u)


capture.release()
