import ctypes
import cv2 as cv
from numpy.ctypeslib import ndpointer
import numpy as np


src = cv.imread("D:/pig1/pig_50000.jpg")
row = src.shape[0]
col = src.shape[1]

dll = ctypes.cdll.LoadLibrary('D:/pycvtest2/x64/Debug/pycvtest2.dll')

path = bytes("D:/pig1/pig_50000.jpg","gbk")

dll.graymat.restype = ctypes.POINTER(ctypes.c_uint8)

pointer = dll.graymat(path)

result = np.array(np.fromiter(pointer, dtype=np.uint8, count=row*col)) 

cv.imshow('result', result.reshape(row, col))

cv.waitKey(0)
dll.release(pointer)

'''
dll=ctypes.WinDLL('D:/pycvtest2/x64/Debug/pycvtest2.dll') 

def cpp_canny(input):
    if len(img.shape)>=3 and img.shape[-1]>1:
        gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

    h,w=gray.shape[0],gray.shape[1] 
    
    # 获取numpy对象的数据指针
    frame_data = np.asarray(gray, dtype=np.uint8)
    frame_data = frame_data.ctypes.data_as(ctypes.c_char_p)  
    
    # 设置输出数据类型为uint8的指针
    dll.cpp_canny.restype = ctypes.POINTER(ctypes.c_uint8)
     
    # 调用dll里的cpp_canny函数
    pointer = dll.cpp_canny(h,w,frame_data)  
     
    # 从指针指向的地址中读取数据，并转为numpy array
    np_canny =  np.array(np.fromiter(pointer, dtype=np.uint8, count=h*w)) 
    
    return pointer,np_canny.reshape((h,w))

img=cv.imread('D:/pig1/pig_50000.jpg')
ptr,canny=cpp_canny(img)
cv.imshow('canny',canny)
cv.waitKey(2000)
#将内存释放
dll.release(ptr)
'''
