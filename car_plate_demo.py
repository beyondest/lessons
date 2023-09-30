
#导库
import cv2 as cv
import numpy as np
import os
#方法
#导入图片资源 path为路径
def load_image(path):
    src=cv.imread(path)
    return src
#灰度拉伸方法 

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

    #寻找轮廓
    contours,hierarchy=cv.findContours(image,cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    img_copy = after.copy()
    #找出最大的三个区域
    solving=[]
    for c in contours:
        r=find_rectangle(c)
        a=(r[2]-r[0])*(r[3]-r[1]) 
        s=(r[2]-r[0])/(r[3]-r[1])

        solving.append([r,a,s])
    #通过参考选出面积最大的区域
    solving=sorted(solving,key=lambda b: b[1])[-3:]
    #颜色识别
    maxweight,maxindex=0,-1
    for i in range(len(solving)):#
        wait_solve=after[solving[i][0][1]:solving[i][0][3],solving[i][0][0]:solving[i][0][2]]
        #BGR转HSV
        hsv=cv.cvtColor(wait_solve,cv.COLOR_BGR2HSV)
        #蓝色车牌的范围 Hsv色彩空间的设置。
        lower=np.array([100,50,50])
        upper=np.array([140,255,255])
        #利用inrange找出掩膜
        mask=cv.inRange(hsv,lower,upper)
        #计算权值用来判断。
        w1=0
        for m in mask:
            w1+=m/255
        w2=0
        for n in w1:
            w2+=n
        #选出最大权值的区域
        if w2>maxweight:
            maxindex=i
            maxweight=w2
    return solving[maxindex][0]  

#对图像的预处理
def find_plates(image):
    image=cv.resize(image,(400,int(400 * image.shape[0] / image.shape[1])))
    #转换为灰度图像
    gray_image=cv.cvtColor(image,cv.COLOR_BGR2GRAY)
    #灰度拉伸
    #如果一幅图像的灰度集中在较暗的区域而导致图像偏暗，可以用灰度拉伸功能来拉伸(斜率>1)物体灰度区间以改善图像；
    # 同样如果图像灰度集中在较亮的区域而导致图像偏亮，也可以用灰度拉伸功能来压缩(斜率<1)物体灰度区间以改善图像质量
    stretchedimage=gray_stretch(gray_image)#进行灰度拉伸，是因为可以改善图像的质量

    #构造卷积核

    kernel=cv.getStructuringElement(cv.MORPH_ELLIPSE,(30,30))
    #开运算
    openingimage=cv.morphologyEx(stretchedimage,cv.MORPH_OPEN,kernel)
    #获取差分图，两幅图像做差  cv2.absdiff('图像1','图像2')
    strtimage=cv.absdiff(stretchedimage,openingimage)

    #图像二值化
    binaryimage=image_binary(strtimage)
    #canny边缘检测
    canny=cv.Canny(binaryimage,binaryimage.shape[0],binaryimage.shape[1])
    #5 24效果最好
    kernel=np.ones((5,24),np.uint8)
    closingimage=cv.morphologyEx(canny,cv.MORPH_CLOSE,kernel)
    openingimage=cv.morphologyEx(closingimage,cv.MORPH_OPEN,kernel)
    #11 6的效果最好
    kernel=np.ones((11,6),np.uint8)
    openingimage=cv.morphologyEx(openingimage,cv.MORPH_OPEN,kernel)
    #消除小区域，定位车牌位置
    rect=loacte_plate(openingimage,image)#rect包括轮廓的左上点和右下点，长宽比以及面积
    #展示图像
    cv.imshow('image',image)
    cv.rectangle(image, (rect[0]-5, rect[1]-5), (rect[2]+5,rect[3]+5), (0, 255, 0), 2)
    cv.imshow('after', image)
    cv.waitKey(0)
    cv.destroyAllWindows()
def runing(): 
    file_path='.\\plates'
    for filewalks in os.walk(file_path):
        for files in filewalks[2]:
            print('正在处理',os.path.join(filewalks[0],files))
            find_plates(load_image(os.path.join(filewalks[0],files)))

runing()


