import cv2
import numpy as np

class A:
    def __init__(self) -> None:
        pass
    @classmethod
    def out(self):
        print('out')
    class B:
        def __init__(self) -> None:
            pass
        def inf(self):
            A.out()
        
        
A.out()
        