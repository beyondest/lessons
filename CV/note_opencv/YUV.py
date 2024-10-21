import cv2
import img_operantion as imo

#blue
#156-255,u, for bar(90-128 old)
#77-158,y,opposite for num
#0-99,v, for bar

#red
#0-116,u,for bar
#152-255,v,for bar
#60-157,y,opposite for num

path='D:/pycv/lessons/res/20.png'
img = cv2.imread(path)
img=cv2.GaussianBlur(img,(3,3),1)
img = cv2.cvtColor(img,cv2.COLOR_BGR2YUV)
y,u,v= cv2.split(img)
#130 is default

def none_use(x):
    pass
cv2.namedWindow('u',cv2.WINDOW_FREERATIO)
cv2.createTrackbar("Max", "u", 0, 255,none_use)
cv2.createTrackbar("Min", "u", 0, 255,none_use)



while cv2.waitKey(1)!=27:
    min=cv2.getTrackbarPos('Min','u')
    max=cv2.getTrackbarPos('Max','u')
    img = cv2.inRange(v,min,max)
    cv2.imshow('haha',img)


cv2.destroyAllWindows()



