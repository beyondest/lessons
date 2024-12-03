import cv2
import matplotlib.pyplot as plt
import numpy
						#basic knowledge

'''white =255, black=0, 0<color<255 '''

						#property of a picture
img.size	---------------amount of pixels=L*W*C(usually 3)
img.dtype--------------kind of data
img.shape--------------(length,width,channel(usually 3))
=(y,x,3),'y is up_down,x is left_right'

cont_coordinate=(x,y)

'''x is from left to right, y is from up to down'''
cv2.drawContours()


'''
draw cont follow this order:
left_down, left_up, right_up, right_down	
'''


                   #how to open a picture in gray
'''cv2 imread =(y,x,(B,G,R)), but plt imread =(y,x,(R,G,B))'''
"""cv2 imshow autoly show single channel, but plt imshow show single channel only if cmp=='gray' """
img_gray=cv2.imread('picture.jpg',cv2.IMREAD_GRAYSCALE)
'''notice that img_gray is single channel'''
cv2.imshow('tmd',img_gray)
cv2.waitKey()
cv2.destroyAllWindows()

'''if you want to show in plt(matplotlib.pyplot),must use 'gray' in imshow'''
plt.imshow(img_gray,'gray')


                  #how to open a video in gray

vd=cv2.VideoCapture('video.mp4')
if vd.isOpened():
	open,frame=vd.read()
else:
	open=False
while open:
	ret,frame=vd.read()
	if frame is None:					
		break
	if ret==True:
		gray_vd=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)'''this is not nesessary'''
		cv2.imshow('win1',gray_vd)
		if cv2.waitKey(anti_speed) & 0xff==27:		
'''anti_speed means more big more slow video'''
		 #break
'''cv2.release(),it will go wrong'''
cv2.destroyAllWindows()


                           #how to spilt BGR


b,g,r=cv2.spilt(img)
img=cv2.merge(b,g,r)

img[ : , : , 0]=0-----------img_b=0
0,1,2-------------------b,g,r

							#Border expansion

							METHODS:

1.border_replicate--------------just copy the border part and add to original border
A||ABC||C

2.border_reflect----------------reflect by border,
ABCD||DCBA

3.border_reflect_101------------reflect by border but do not copy border,
ABCD||CBA

4.border_wrap----------------end to end match,
ABCD||ABCD||ABCD

5.border_constant-------------fill the border with just one color
V||ABCD||V

							FUNCTION:

img_replicate=cv2.copyMakeBorder(img, top_size, bottom_size, left_size,right_size,
border_type)
'''notice that border_type must come after cv2.'''
border_type={
						BORDER_REPLICATE
						BORDER_REFLECT
						BORDER_REFLECT_101
						BORDER_WRAP
						BORDER_CONSTANT, value=x

					}
                        #show by matplotlib


import matplotlib.pyplot as plt
plt.subplot(231),plt.imshow(img,'gray'),plt.title('hello')
plt.show()

'''subplot means location, imshow show the picture,show only use when you want to show many pictures'''
'''subplot at least claim once at first'''

				#show many pictures at the same time by matplotlib

img_hand_gray=cv2.imread('/home/liyuxuan/vscode/res\hand.jpg',cv2.IMREAD_GRAYSCALE)
ret,thresh_bin=cv2.threshold(img_hand_gray,127,255,cv2.THRESH_BINARY)
ret,thresh_tozero=cv2.threshold(img_hand_gray,200,255,cv2.THRESH_TOZERO)
ret,thresh_trunc=cv2.threshold(img_hand_gray,100,255,cv2.THRESH_TRUNC)
show_thresh=[img_hand_gray,thresh_bin,thresh_tozero,thresh_trunc]
thresh_title=['original','bin','tozero','trunc']
for i in range(4):
    plt.subplot(2,3,i+1),plt.imshow(show_thresh[i],'gray')
    plt.title(thresh_title[i])
    plt.xticks([]),plt.yticks([])
plt.show()

					#link pictures end to end
res=numpy.hstack((img_1,img_2,img_3))
plt.imshow(res)
'''notice that tuple,and sizeof 1,2,3 must match'''

