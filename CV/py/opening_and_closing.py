import cv2
import numpy as np
import matplotlib.pyplot as plt

            #opening operation
kn1=np.ones((4,4),np.uint8)
img_opening=cv2.morphologyEx(img,cv2.MORPH_OPEN,kn1)
"""open = first erode then dilate"""
'''open to delete white small blocks'''
            #closing operation
img_closing=cv2.morphologyEx(img,cv2.MORPH_CLOSE,kn1)
"""close = first dilate then erode"""
'''close to delete black small blocks'''