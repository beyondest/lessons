
#����
import cv2 as cv
import numpy as np
import os
#����
#����ͼƬ��Դ pathΪ·��
def load_image(path):
    src=cv.imread(path)
    return src
#�Ҷ����췽�� 

def gray_stretch(image):
    max_value=float(image.max())
    min_value=float(image.min())
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            image[i,j]=(255/(max_value-min_value)*image[i,j]-(255*min_value)/(max_value-min_value))
    return image

def image_binary(image):
    max_value=float(image.max())
    min_value=float(image.min()) 

    ret=max_value-(max_value-min_value)/2
    ret,thresh=cv.threshold(image,ret,255,cv.THRESH_BINARY)
    return thresh


def find_rectangle(contour):
    y,x=[],[]
    for value in contour:
        y.append(value[0][0])
        x.append(value[0][1])
    return [min(y),min(x),max(y),max(x)]


def loacte_plate(image,after):

    #Ѱ������
    contours,hierarchy=cv.findContours(image,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    img_copy = after.copy()
    #�ҳ�������������
    solving=[]
    for c in contours:
        r=find_rectangle(c)
        a=(r[2]-r[0])*(r[3]-r[1]) 
        s=(r[2]-r[0])/(r[3]-r[1])

        solving.append([r,a,s])
    #ͨ���ο�ѡ�������������
    solving=sorted(solving,key=lambda b: b[1])[-3:]
    #��ɫʶ��
    maxweight,maxindex=0,-1
    for i in range(len(solving)):#
        wait_solve=after[solving[i][0][1]:solving[i][0][3],solving[i][0][0]:solving[i][0][2]]
        #BGRתHSV
        hsv=cv.cvtColor(wait_solve,cv.COLOR_BGR2HSV)
        #��ɫ���Ƶķ�Χ Hsvɫ�ʿռ�����á�
        lower=np.array([100,50,50])
        upper=np.array([140,255,255])
        #����inrange�ҳ���Ĥ
        mask=cv.inRange(hsv,lower,upper)
        #����Ȩֵ�����жϡ�
        w1=0
        for m in mask:
            w1+=m/255
        w2=0
        for n in w1:
            w2+=n
        #ѡ�����Ȩֵ������
        if w2>maxweight:
            maxindex=i
            maxweight=w2
    return solving[maxindex][0]  

#��ͼ���Ԥ����
def find_plates(image):
    image=cv.resize(image,(400,int(400 * image.shape[0] / image.shape[1])))
    #ת��Ϊ�Ҷ�ͼ��
    gray_image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    #�Ҷ�����
    #���һ��ͼ��ĻҶȼ����ڽϰ������������ͼ��ƫ���������ûҶ����칦��������(б��>1)����Ҷ������Ը���ͼ��
    # ͬ�����ͼ��Ҷȼ����ڽ��������������ͼ��ƫ����Ҳ�����ûҶ����칦����ѹ��(б��<1)����Ҷ������Ը���ͼ������
    stretchedimage=gray_stretch(gray_image)#���лҶ����죬����Ϊ���Ը���ͼ�������

    #��������

    kernel=cv.getStructuringElement(cv.MORPH_ELLIPSE,(30,30))
    #������
    openingimage=cv.morphologyEx(stretchedimage,cv.MORPH_OPEN,kernel)
    #��ȡ���ͼ������ͼ������  cv2.absdiff('ͼ��1','ͼ��2')
    strtimage=cv.absdiff(stretchedimage,openingimage)

    #ͼ���ֵ��
    binaryimage=image_binary(strtimage)
    #canny��Ե���
    canny=cv.Canny(binaryimage,binaryimage.shape[0],binaryimage.shape[1])
    #5 24Ч�����
    kernel=np.ones((5,24),np.uint8)
    closingimage=cv.morphologyEx(canny,cv.MORPH_CLOSE,kernel)
    openingimage=cv.morphologyEx(closingimage,cv.MORPH_OPEN,kernel)
    #11 6��Ч�����
    kernel=np.ones((11,6),np.uint8)
    openingimage=cv.morphologyEx(openingimage,cv.MORPH_OPEN,kernel)
    #����С���򣬶�λ����λ��
    rect=loacte_plate(openingimage,image)#rect�������������ϵ�����µ㣬������Լ����
    #չʾͼ��
    cv.imshow('image',image)
    cv.rectangle(image, (rect[0]-5, rect[1]-5), (rect[2]+5,rect[3]+5), (0, 255, 0), 2)
    cv.imshow('after', image)
    cv.waitKey(0)
    cv.destroyAllWindows()
def runing(): 
    file_path='.\\plates'
    for filewalks in os.walk(file_path):
        for files in filewalks[2]:
            print('���ڴ���',os.path.join(filewalks[0],files))
            find_plates(load_image(os.path.join(filewalks[0],files)))

runing()


