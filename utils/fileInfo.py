# 文件类，保存文件路径和父目录名字
class FileInfo:
    def __init__(self,fileName,filePath):
        self.fileName = fileName # 该文件的路径
        self.filePath = filePath # 父目录的名字
    
    def printPath(self):
        print(self.filePath)

    def __getattr__(self,attr): 
        return attr