'''
    处理图片
'''

import easyocr
import os
import cv2
import numpy as np

from regSensitive import regexSensitive
import sys
sys.path.append(r'..')
'''python import模块时， 是在sys.path里按顺序
'''
import utils.matchSensitive as matchSensitive


current_directory = os.path.dirname(os.path.abspath(__file__))

'''
    用到easyOCR
    路径包含中文会乱码，因此将路径转换为numpy格式
'''

'''
    ocr，返回读取文字内容
'''
# ocr速度有点慢，考虑开线程
def OCR(filePath):
    cv_img= cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)#先转换格式为np，否则中文乱码读不到文件
    reader = easyocr.Reader(['ch_sim','en'],gpu=False) # this needs to run only once to load the model into memory
    result = reader.readtext(cv_img,detail=0)
    return result


def handleJPGorPNG(fileName,filePath):
    sentiWord = matchSensitive.readYaml()# 返回铭感词字典
    sentiWord = sentiWord['sensitive_word']
    result = OCR(filePath=filePath)
    result = "".join(result)
    extract = regexSensitive(textLis=result)
    dic = {}
    dic[fileName+'源']=str(sentiWord)
    dic[fileName+'提取'] = extract
    savePath = os.path.join(current_directory,fileName+".txt")
    file = open(savePath,"w",encoding='utf-8')
    file.write(str(dic))
    file.close()

'''
    匹配敏感信息算法
    origin_str:要匹配的目标list
    senti_list:铭感词的目标list
'''
# def matchSensiti(origin_list,senti_list):
#     extract = []
#     # 遍历读出来的元素，然后匹配铭感词
#     # TODO 上下文匹配不是很好，只匹配到关键词
#     for item in origin_list:
#         item = item.lower()
#         for word in senti_list:
#             if item.find(word) >= 0:
#                 # 匹配铭感词
#                 extract.append(item)
#                 break
#     return extract

if __name__ == '__main__':
    cv_img= cv2.imdecode(np.fromfile('E:\huaweicup\huaweicup2-RichTextDetc\kevin\图片1.png',dtype=np.uint8),-1)#先转换格式为np，否则中文乱码读不到文件
    handleJPGorPNG('图片1.png','E:\huaweicup\huaweicup2-RichTextDetc\kevin\图片1.png')
    # sentiWord = matchSensitive.readYaml()# 返回铭感词字典
    # sentiWord = sentiWord['sensitive_word']
    # print(sentiWord)

    # import pytesseract
    # from PIL import Image
    # text = pytesseract.image_to_string(Image.open('E:\huaweicup\huaweicup2-RichTextDetc\赛题材料\HCC维护信息.png'),lang='ch_sim')
    # print(text)