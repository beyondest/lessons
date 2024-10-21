import cv2
import numpy as np
import matplotlib.pyplot as plt
                #set kernel size,then smaller by erode or bigger by dilate
kernel=np.ones((3,3),np.uint8)
img_erode=cv2.erode(img,kernel=kernel,iterations=1)
'''iterate 1 time, check in 3*3 size pixels, main in white, background in black'''

img_dilate=cv2.dilate(img,kernel=kernel,iterations=1)
'''same as above, but bigger not smaller the img'''