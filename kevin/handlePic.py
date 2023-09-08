'''
    处理图片
'''

import easyocr
import os
import cv2
import numpy as np
'''
    用到easyOCR
    路径包含中文会乱码
'''
def handleJPGorPNG(fileName,filePath):
    # print(filePath,sep=",")
    cv_img= cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)#先转换格式为np，否则中文乱码读不到文件
    reader = easyocr.Reader(['ch_sim','en'],gpu=False) # this needs to run only once to load the model into memory
    result = reader.readtext(cv_img,detail=0) 
    print(result)


if __name__ == '__main__':
    cv_img= cv2.imdecode(np.fromfile('./HCC维护信息.png',dtype=np.uint8),-1)#先转换格式为np，否则中文乱码读不到文件
    handleJPGorPNG('carbon.jpg',cv_img)