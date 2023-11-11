#coding=utf-8
import numpy as np
import math
import cv2

vd=cv2.VideoCapture("rtsp://192.168.1.141:8080/h264_ulaw.sdp")
while True:
    ret, frame = vd.read()  
    if not ret:
        break
    cv2.imshow('ww', frame)  

    if cv2.waitKey(1) & 0xFF ==27:
        break

vd.release()  
cv2.destroyAllWindows()  
   

        
        
        