import cv2
                    #average filter
img_blur=cv2.blur(img,(3,3))
'''(3,3)means 3*3matrix gets average'''
'''[[1,1,1],
    [1,1,1]
    [1,1,1]] * 1/9 * img'''
 
                    #box filter
img_box=cv2.boxFilter(img,-1,(3,3),normalize=False)
'''if false,thers's no 1/9, but if over 255, remains 255'''
'''if true, same as average'''

                    #gaussian filter
img_gaussian=cv2.GaussianBlur(img,(3,3),1)
'''add the weight to each pixel, such as
[[0.5,0.8,0.5],
 [0.8,1.0,0.8],
 [0.5,0.8,0.5]]'''
                    #median filter
img_median=cv2.medianBlur(img,3)
'''same as average, but change average into median'''
