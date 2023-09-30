import cv2
import numpy as np
import matplotlib.pyplot as plt

            #gradient operation
kn1=np.ones((4,4),np.unit8)
img_gradient=cv2.morphologyEx(img,cv2.MORPH_GRADIENT,kn1)
img_handmade_gradient=cv2.dilate(img,kn1,iterations=1)-cv2.erode(img,kn1,iterations=1)
"""use gradient to get the border of img"""