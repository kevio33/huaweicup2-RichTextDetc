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

from kevin.handlePic import handleJPGorPNG
from kevin.handlePPT import handlePpt
from msn.handleExcel import handleExcel
from msn.handleTxt import handleTxt

fileQue = Queue()# 队列保存所有子文件和子目录信息

# f = open('fileData.yml', 'r', encoding='utf-8')# 读yml文件
# cfg = f.read()
# dyml = yaml.load(cfg,Loader=yaml.FullLoader)  # 用load方法转字典


# 文件类，保存文件路径和父目录名字
class FileInfo:
    def __init__(self,fileName,filePath):
        self.fileName = fileName # 该文件的路径
        self.filePath = filePath # 父目录的名字
    
    def printPath(self):
        print(self.filePath)

    def __getattr__(self,attr): 
        return attr


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

        if len(extend) >= 2:
            # 文件后缀
            suffix = extend[-1]

        if suffix == 'jpg' or extend == 'png': #这里重复逻辑判断
            handleJPGorPNG(i.fileName,i.filePath)
        elif suffix == 'xlsx': #这里重复逻辑判断
            handleExcel(i.fileName,i.filePath)
        elif suffix == 'txt':
            handleTxt(i.fileName,i.filePath)
        elif suffix == 'ppt':
            handlePpt(fileName=extend[0],filePath=i.filePath,isPPT=True)
        elif suffix == 'pptx':
            handlePpt(i.fileName,i.filePath)

        pbar.update(1)#更新进度条
    
    pbar.close()

    # while not fileQue.empty():
    #     i = fileQue.get()
    #     print(i.fileName)

        
if __name__ == "__main__":
    unzipFile('题目1：富文本敏感信息泄露检测.rar','.') #解压缩文件
    listUnzipFile('.\赛题材料')#分析代码
    handleQue() # 处理队列里面记录的文件






