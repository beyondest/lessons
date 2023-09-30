import cv2
                            #calculate the pictures

'''addend has to match the shape,e.g.:200*200*3+200*200*3'''
'''shape change'''
cv2.resize(img,(x,y),fx=k1,fy=k2)
'notice that shape=(y,x,3)'
'fx means larger x in fx times,which larger pixels too'

img_1+10=every item +10
img_1+img_2=every_1+every_2
'''cause dtype=uint8,ndarry[] is in 0-255, if out, sum=sum%256'''

cv2.add(img_1,img_2)
'''every+every, but if out, sum=255'''

cv2.addWeighted(img1,k1,img2,k2,b)
'return k1*img1+k2*img2+b'

                        #threshold of picture


ret,img_treshed=cv2.threshold(single_channel_img,thresh,maxval,type)

single_channel_img:'''usually img_gray'''
thresh:'''usually 127'''
maxval:'''usually 255'''

type:   {
            cv2.THRESH_BINARY'''maxval if >thresh else 0'''
                             '''the lighter will be the lightest,the darker will be darkest'''
            cv2.THRESH_TOZERO'''remain if >thresh else 0'''
                             '''darkest the darker part,remain the lighter'''
            cv2.THRESH_TRUNC'''255 if >thresh else remain'''
                            '''lighter to lightest,remaiin the darker'''
            cv2.THRESH_BINARY_INV'''reverse'''
            cv2.THRESH_TOZERO_INV'''reverse'''
            cv2.THRESH_OTSU'''a way to caculate best thresh then binary'''
        }