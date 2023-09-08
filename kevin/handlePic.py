'''
    处理图片
'''

import easyocr
import os

'''
    用到easyOCR
    路径包含中文会乱码
'''
def handleJPG(fileName,filePath):
    print(filePath,sep=",")
    reader = easyocr.Reader(['ch_sim','en'],gpu=False) # this needs to run only once to load the model into memory
    result = reader.readtext(filePath,detail=0) 
    print(result)

