'''
    读
'''
from flanker import mime
import os
from kevin.handlePic import OCR
from kevin.handlePPT import readPPt
from msn.handleExcel import readExcel
from msn.handleTxt import handleTxt
from msn.handleWord import handleWord
from regSensitive import regexSensitive
#读邮件的内容
def readBody(eml):
    # 判断是否为单部分
    if eml.content_type.is_singlepart():
        eml_body = eml.body
    else:
        eml_body = ''
        for part in eml.parts:
            # 判断是否是多部分
            if part.content_type.is_multipart():
                eml_body = readBody(part)
            else:
                if part.content_type.main == 'text':
                    eml_body = part.body
    return eml_body

'''
    处理eml文件
'''
def handleEml(fileName,filePath):
    res = {}
    # with open(filePath,"r") as emlFile:
    emlFile = open(filePath,"r")
    raw_email = emlFile.read()
    eml = mime.from_string(raw_email)
    # print(eml.headers.items())#邮件头
    header = []
    #读文件头
    for item in eml.headers.items():
        # item[1] = str(item[1])
        if type(item[1]) is not str:#如果键值不是字符串
            item1 = str(item[1])
            header.append(item[0]+":"+item1)
        else:
            #邮件头的内容全部读出来
            item = ":".join(item)
            header.append(item)
    res['header'] = header

    #读body内容
    eml_body = readBody(eml)
    lis_body = []
    lis_body.append(eml_body)
    lis_body = regexSensitive(lis_body)
    res['body'] = lis_body
    # 读附件内容
    for part in eml.parts:
        # if part.is_attachment():
            # filename = part.detected_file_name 
            # print(f'Found attachment: {filename}')
        if not part.content_type.is_multipart():   
            if not os.path.exists('kevin/attach'):#创建存放附件的目录
               os.makedirs('kevin/attach') 
            name = part.detected_file_name
            name = name.split('"')

            file = open('kevin/attach/'+name[0],'wb')
            file.write(part.body)
            file.close()
    
    attachRes = handleAttach()#处理附件
    res['attach'] = attachRes

    outputfile = open('kevin/output.txt','w',encoding='utf-8')
    outputfile.write(str(res))
    outputfile.close()

    emlFile.close()

'''
    处理附件
'''
def handleAttach():
    attachRes = {}
    if os.path.exists('kevin/attach'):
        for it in os.scandir('kevin/attach'):# 遍历附件目录下的文件/子目录
            filePath=os.path.abspath(it.path)
            extend = it.name
            extend = extend.split(".")
            suffix = ''
            if len(extend) >= 2:#如果文件有后缀
                # 文件后缀
                suffix = extend[-1]
                res = []
                if suffix == 'jpg' or extend == 'png': #这里重复逻辑判断
                    res = OCR(filePath)
                    res = regexSensitive(res)
                elif suffix == 'xlsx': #这里重复逻辑判断
                    res = readExcel(filePath)
                    # res = regexSensitive(res)
                elif suffix == 'txt':
                    res = handleTxt(it.name,filePath)
                    # res = regexSensitive(res)
                elif suffix == 'doc':
                    res = handleWord(it.name, filePath)
                elif suffix == 'ppt':
                    res = readPPt(fileName=extend[0],filePath=filePath,isPPT=True)
                    res = regexSensitive(res)
                elif suffix == 'pptx':
                    res = readPPt(it.name,filePath)
                    res = regexSensitive(res)
                attachRes[it.name] = res
            else:
                pass
    return attachRes
    

if __name__ == '__main__':
    handleEml('',r'E:\huaweicup\huaweicup2-RichTextDetc\赛题材料\xxx部门弱口令漏洞问题和整改 2023-05-25T17_27_32+08_00.eml')