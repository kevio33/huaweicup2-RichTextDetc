'''
    读
'''
from flanker import mime
from flanker.addresslib import address
import os



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

def handleEml(fileName,filePath):
    res = {}
    # with open(filePath,"r") as emlFile:
    emlFile = open(filePath,"r")
    raw_email = emlFile.read()
    eml = mime.from_string(raw_email)
    # print(eml.headers.items())#邮件头
    header = []
    for item in eml.headers.items():
        #邮件头的内容全部读出来
        item = ":".join(item)
        header.append(item)
    res['header'] = header

    #读body内容
    eml_body = readBody(eml)
    lis_body = []
    lis_body.append(eml_body)
    res['body'] = lis_body
    # 读附件内容
    for part in eml.parts:
        # if part.is_attachment():
            # filename = part.detected_file_name 
            # print(f'Found attachment: {filename}')
        if not part.content_type.is_multipart():
            if os.path.exists('emlattach'):
                os.makedirs()     
            name = part.detected_file_name
            name = name.split('"')
            file = open(name[0],'wb')
            file.write(part.body)
            file.close()
    

    emlFile.close()

'''
    处理附件
'''
def handleAttach():
    pass


if __name__ == '__main__':

    handleEml('',r'E:\huaweicup\huaweicup2-RichTextDetc\赛题材料\xxx部门弱口令漏洞问题和整改 2023-05-25T17_27_32+08_00.eml')