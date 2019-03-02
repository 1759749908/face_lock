import cv2
import time
       
vc = cv2.VideoCapture(0) #读入视频文件
 
ret,frame = vc.read()

 
 
while True:   #循环读取视频帧
    time.sleep(1)
    #ret , frame = vc.read()
    (cv2.imwrite("image.jpg",frame)) #存储为图像
vc.release()