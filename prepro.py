import cv2
import img_operantion as imo
import os_operation as oso
import numpy as np
path='D:/pycv/lessons/res/20.png'



img_ori=cv2.imread(path)

img_single,t1=imo.pre_process(img_ori)
rec_list,t2=imo.find_big_rec(img_single)
dst=imo.draw_big_rec(rec_list,img_ori)


roi_list,t3=imo.pick_up_roi(rec_list,img_ori)
roi_single_list,t4=imo.pre_process2(roi_list)


    
print('t1=',t1)
print('t2=',t2)
print('t3=',t3)
print('t4=',t4)
cv2.namedWindow('hh',cv2.WINDOW_FREERATIO)
cv2.namedWindow('roi',cv2.WINDOW_FREERATIO)
cv2.imshow('hh',dst)
cv2.imshow('roi',roi_single_list[0])
cv2.waitKey(0)
cv2.destroyAllWindows()

    