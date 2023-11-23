#coding=utf-8
import numpy as np
import math
import cv2
path="rtsp://127.0.0.1:8080/h264_pcm.sdp"
vd=cv2.VideoCapture(path)
while True:
    ret, frame = vd.read()  
    if not ret:
        break
    cv2.imshow('ww', frame)  

    if cv2.waitKey(1) & 0xFF ==27:
        break



vd.release()  
cv2.destroyAllWindows()  
   

        
        
        