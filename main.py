'''
项目启动项
1.负责启动项目界面(最后的工程了)
2.解压缩文件(将压缩文件放到本目录下)
3.读取所有文件的内容，并提取敏感信息
'''
import os
import rarfile
from queue import Queue
from tqdm import tqdm
from msn.handleEt import handleEt
from utils.fileInfo import FileInfo

from kevin.handlePic import handleJPGorPNG
from kevin.handlePPT import handlePpt
from msn.handleExcel import handleExcel
from msn.handleTxt import handleTxt
from msn.handleWord import handleWord
from kevin.handleEml import handleEml
import hdy.handleLinuxFiles as handleLinuxFiles
from tang.HandleSrcContent import HandleSrcContent
import time
import json


fileQue = Queue()# 队列保存所有子文件和子目录信息

# f = open('fileData.yml', 'r', encoding='utf-8')# 读yml文件
# cfg = f.read()
# dyml = yaml.load(cfg,Loader=yaml.FullLoader)  # 用load方法转字典


# 解压缩文件
def unzipFile(filePath,desPath=None):
    # 打开 RAR 文件
    # rar = rarfile.RarFile('题目1：富文本敏感信息泄露检测.rar')
    rar = rarfile.RarFile(filePath)

    # 解压缩文件到指定路径
    rar.extractall(desPath)

    # 关闭 RAR 文件
    rar.close()

'''
    统计解压目录下面的目录和文件
'''
def listUnzipFile(filePath):
    # filePath = './赛题材料'
    # current_path = os.path.abspath('..')
    for it in os.scandir(filePath):# 遍历目录下的文件/子目录
        # 分文件和目录进行处理
        if it.is_dir():
            if it.name == 'linux':#判断linux情况
                file = FileInfo(fileName=it.name,filePath=os.path.abspath(it.path))
                fileQue.put(file)
            else:
                listUnzipFile(filePath=it.path)
        else:
            file = FileInfo(fileName=it.name,filePath=os.path.abspath(it.path))
            fileQue.put(file) # 如果是文件，则将文件放入队列


"""
    获取到所有文件信息之后，开始遍历队列，然后分析文件
    可以考虑线程提取文件信息
"""
def handleQue():
    pbar = tqdm(total=fileQue.qsize())
    
    while not fileQue.empty():
        i = fileQue.get()
        extend = i.fileName
        extend = extend.split(".")
        suffix = ''
        if len(extend) >= 2:

            # 有文件后缀
            suffix = extend[-1]#文件后缀

            if suffix == 'jpg' or suffix == 'png': #这里重复逻辑判断
                try:
                    handleJPGorPNG(i.fileName, i.filePath)
                except Exception:
                    pass
            elif suffix == 'xlsx': #这里重复逻辑判断
                try:
                    handleExcel(i.fileName, i.filePath)
                except Exception:
                    pass
            elif suffix == 'txt':
                try:
                    handleTxt(i.fileName, i.filePath)
                except Exception:
                    pass
            elif suffix == 'doc':
                try:
                    handleWord(i.fileName, i.filePath)
                except Exception:
                    pass
            elif suffix == 'et':
                try:
                    handleEt(i.fileName, i.filePath)
                except Exception:
                    pass
            elif suffix == 'ppt':
                try:
                    handlePpt(fileName=extend[0],filePath=i.filePath,isPPT=True)
                except Exception:
                    pass
            elif suffix == 'pptx':
                try:
                    handlePpt(i.fileName, i.filePath)
                except Exception:
                    pass
            elif suffix == 'eml':
                try:
                    handleEml(i.fileName, i.filePath)
                except Exception:
                    pass
            elif suffix == 'zip':
                try:
                    handle_src = HandleSrcContent(i.fileName, i.filePath)
                    handle_src.handle_file()
                except Exception:
                    pass
        else:
            #没有后缀的名字
            if i.fileName == 'linux':
                try:
                    handle_linux = handleLinuxFiles.LinuxFilesHandler(i.filePath,output_file='./hdy/linux_output.txt')
                    handle_linux.write_files_to_txt()
                except Exception:
                    pass

        pbar.update(1)#更新进度条

    pbar.close()

#最终结果文件
def write_result():
    res_list = ['hdy','kevin','msn','tang']
    total_res = []#结果集合
    file_write = open('提取结果.json','w',encoding='utf-8')
    for lis in res_list:
        #分别读每个目录下的结果.txt文件
        lis_path = os.path.join('.',lis)
        for item in  os.scandir(lis_path):
            if item.is_file and item.name[-3:]=='txt':
                try:
                    file_read = open(os.path.abspath(item),'r',)
                    res_str = file_read.read()
                    file_read.close()
                    # res_str = res_str.replace("\'", "\"")
                    # res_str = u'{}'.format(res_str)
                    # res_str = res_str.encode('utf-8').decode("unicode_escape")
                    # print(res_str)
                    res_str = json.dumps(res_str,ensure_ascii=False)
                    new_dict = json.loads(res_str)#转换字符串为字典
                    # new_dict = new_dict.replace("\'", "\"")
                    total_res.append(new_dict)
                except Exception:
                    pass
    res_dic = {}
    res_dic["提取结果"] = total_res
    json.dump(res_dic,file_write,ensure_ascii=False)
    file_write.close()
                
                

        

if __name__ == "__main__":

    start_time = time.time()
    root_path = os.path.abspath(__file__)
    root_path = root_path[:-7]#获取绝对路径
    rarfile_path = ''
    for item in os.scandir(root_path):
        if item.is_file:
            if item.name[-3:] == 'rar':
                rarfile_path = os.path.abspath(item)
                break
    # unzipFile('题目1：富文本敏感信息泄露检测.rar','.') #解压缩文件
    unzipFile(rarfile_path,'./赛题材料') #解压缩文件
    listUnzipFile('./赛题材料')#分析代码
    handleQue() # 处理队列里面记录的文件
    write_result()#写入最终结果文件
    end_time = time.time()
    time_local_start = time.localtime(start_time)
    time_local_end = time.localtime(end_time)

    dt_start = time.strftime("%Y-%m-%d %H:%M:%S", time_local_start)
    dt_end = time.strftime("%Y-%m-%d %H:%M:%S", time_local_end)
    
    print("开始时间:",dt_start)
    print("结束时间:",dt_end)





