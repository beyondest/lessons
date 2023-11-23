from typing import Any
import cv2
import numpy as np
class Img:
    def __init__(self) -> None:
        pass
    
    
    class canvas:
        def __init__(self,size_tuple:tuple,color:str='white'):
            '''
            size_tuple: (width,height,channel)
            '''
            img=np.zeros(size_tuple,dtype=np.uint8)
            if color=='white':
                img.fill(255)
            self.img=img
            self.wid=img.shape[0]
            self.hei=img.shape[1]
            
        def draw_rec(self,color:tuple=(0,0,255),mode:int=0,info:tuple|np.ndarray|None=None,nums:int=1):
            '''
            color:(0,0,255) for red
            0 : center
            1 : random
            2 : specified
            info : if mode==2: 
                tuple: ((center_x_int,center_y_int),(wid_int,hei_int),angle_int)
                np.ndarray: batched_boxpoints
                
            nums: if mode==1
            '''
            if mode==0:
                center=(round(self.wid/2),round(self.hei/2))
                width=round(self.wid/6)
                height=round(self.hei/6)
                angle=30
                bp=cv2.boxPoints((center,(width,height),angle))
                Img.draw_rec(self.img,bp,color=color)
            elif mode==1:
                for i in range(nums):
                    center=(np.random.randint(0,self.wid),np.random.randint(0,self.hei))
                    width=np.random.randint(5,min(self.wid,self.hei)/4)
                    height=np.random.randint(5,min(self.wid,self.hei)/4)
                    angle=np.random.randint(1,90)
                    bp=cv2.boxPoints((center,(width,height),angle))
                    Img.draw_rec(self.img,bp,color=color)
            elif mode==2:
                if isinstance(info,tuple):
                    bp=Img.Change.toboxpoints(info)
                    
                elif isinstance(info,np.ndarray):
                    bp=info
                else:
                    raise TypeError('info must be tuple or np.ndarray')
                Img.draw_rec(self.img,bp,color=color)
            else:
                raise TypeError('mode is wrong')
        def show(self):
            cv2.imshow('canvas',self.img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            
            
    class Check:
        def __init__(self) -> None:
            pass
        @classmethod
        def is_3channelimg(cls,img:np.ndarray):
            
            if len(img.shape)==3:
                return True if img.shape[2]==3 else False
            elif len(img.shape)==2:
                return False
            else:
                raise TypeError("img.shape is not 3 or 2 length")
        @classmethod
        def is_batch_contour(cls,mat_like:np.ndarray):
            return True if len(mat_like.shape)==3 else False
        @classmethod
        def is_batch_img(cls,mat_like:np.ndarray):
            return True if len(mat_like.shape)==4 else False
                
    @classmethod
    def draw_rec(cls,
                 ori_img:np.ndarray,
                 box_points_batch:np.ndarray,
                 sequence:np.ndarray|None=None,
                 color:tuple=(127,127,255),
                 thickness:int=-1
                 ):
        """draw a series of rec or a single rec on ori_img.Will change dtype to int32 of box_points

        Args:
            ori_img (np.ndarray): WILL CHANGE ORI_IMG, COPY BEFORE ENTTER
            box_points (np.ndarray): 3 dim array, first dim is batch_size
            sequence (np.ndarray | None, optional): the index array of rec in box_points you want to show, Defaults to None.
            color (tuple, optional): tuple of color Defaults to (127,127,255).
            thickness (int, optional): -1 is solid, other is width. Defaults to -1.
        """
        
        if not cls.Check.is_3channelimg(ori_img):
            ori_img=cv2.cvtColor(ori_img,cv2.COLOR_GRAY2BGR)
        if not cls.Check.is_batch_contour(box_points_batch):
            box_points_batch=np.expand_dims(box_points_batch,axis=0)
        #!!!MUST BE INT OE NP.INT32
        box_points_batch=np.round(box_points_batch).astype(np.int32)
        if sequence==None:
            cv2.drawContours(ori_img,box_points_batch,-1,color,thickness)
        else:
            cv2.drawContours(ori_img,box_points_batch[sequence],-1,color,thickness)
        return ori_img
    @classmethod
    def normalize(cls,ori_img:np.ndarray,scope:tuple=(0,1)):
        '''(y-a)/(b-a)=(x-xmin)/(xmax-xmin)'''
        return (ori_img-ori_img.min())/(ori_img.max()-ori_img.min())*(scope[1]-scope[0])+scope[0]
 
    class Change:
        def __init__(self) -> None:
            pass
        @classmethod
        def toimgbatch(cls,*args:np.ndarray):
            '''
            change to 4 dim, (batchsize,channel,wid,height)
            
            args=img1,img2...
            '''
            for i in args:
                if len(i.shape)==2:
                    i=np.expand_dims(i,0)
                else:
                    i=i.transpose(2,0,1)
            return np.stack(args,axis=0)
        
        @classmethod
        def toboxpoints(cls,info:tuple):
            '''
            tuple=(center,(wid,hei),angle)
            '''
            
            center=(round(info[0][0]),round(info[0][1]))
            wid=round(info[1][0])
            hei=round(info[1][1])
            angle=round(info[2])
            return cv2.boxPoints((center,(wid,hei),angle)).astype(np.int32)
            
        
        
        
    
if __name__=='__main__':
    canvas1=Img.canvas((500,500,3))
    canvas1.draw_rec(color=(0,0,0),mode=2,info=((300.2,40),(30,50.8),10))
    canvas1.show()