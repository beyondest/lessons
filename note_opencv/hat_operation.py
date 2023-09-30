import cv2

#tophat and blackhat operation
img_tophat=cv2.morphologyEx(img,cv2.MORPH_TOPHAT,kn1)
img_blackhat=cv2.morphologyEx(img,cv2.MORPH_BLACKHAT,kn1)
"""tophat = img-img_opening"""
"""tophat shows the stinger"""
"""blackhat = img_closing-img"""
"""blackhat shows the border included stinger"""