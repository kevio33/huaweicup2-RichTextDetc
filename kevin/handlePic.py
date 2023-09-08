'''
    处理图片
'''

import easyocr
import os
import cv2
import numpy as np
'''
    用到easyOCR
    路径包含中文会乱码，因此将路径转换为numpy格式
'''
def handleJPGorPNG(fileName,filePath):
    # print(filePath,sep=",")
    cv_img= cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)#先转换格式为np，否则中文乱码读不到文件
    reader = easyocr.Reader(['ch_sim','en'],gpu=False) # this needs to run only once to load the model into memory
    result = reader.readtext(cv_img,detail=0) 
    dic = {}
    dic[fileName] = result
    # print(dic)
    file = open(fileName+'.txt',"w",encoding='utf-8')
    file.write(str(dic))
    file.close()




if __name__ == '__main__':
    # cv_img= cv2.imdecode(np.fromfile('E:\huaweicup\huaweicup2-RichTextDetc\赛题材料\carbon.jpg',dtype=np.uint8),-1)#先转换格式为np，否则中文乱码读不到文件
    handleJPGorPNG('carbon.jpg','E:\huaweicup\huaweicup2-RichTextDetc\赛题材料\carbon.jpg')