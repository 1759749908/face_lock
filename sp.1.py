import time
from ctypes import *

import cv2

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
    #gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)  #听说可以提高性能，但是我感觉不出来
    faces = face.detectMultiScale(frame)
    if faces == ():
        u = u + 1
        if (capture.isOpened() == True) & (u>=20):
            windll.LoadLibrary('user32.dll').LockWorkStation()
            #print("ok")
        elif (capture.isOpened() == True):
            pass
        else:
            u=0
    else:
        u = 0
    time.sleep(1)
    print(u)

u = 0
while True:
    while u <= 20:
        if a == 1:
            u = 0
        else:
            u = u + 1
    if capture.isOpened() == True:
        windll.LoadLibrary('user32.dll').LockWorkStation()
        #print("ok")
    else:
        u = 0

capture.release()
